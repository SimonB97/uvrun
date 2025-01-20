from pathlib import Path
from typing import Dict, Optional
import tomllib
import tomli_w

class Config:
    def __init__(self):
        self.config_dir = Path.home() / ".config" / "uvrun"
        self.config_file = self.config_dir / "config.toml"
        self._ensure_dirs()
        self.config = self._load_config()

    def _ensure_dirs(self) -> None:
        self.config_dir.mkdir(parents=True, exist_ok=True)

    def _load_config(self) -> dict:
        if not self.config_file.exists():
            default_config = {"repos": {}}
            self._save_config(default_config)
            return default_config
        return tomllib.loads(self.config_file.read_text())

    def _save_config(self, config: dict) -> None:
        self.config_file.write_text(tomli_w.dumps(config))

    def add_repo(self, url: str, scripts: Dict[str, str]) -> None:
        raw_base = self._get_raw_url_base(url)
        self.config["repos"][url] = {
            "raw_base": raw_base,
            "scripts": scripts
        }
        self._save_config(self.config)

    def get_script_url(self, script_name: str) -> Optional[str]:
        # Support both with and without .py extension
        if not script_name.endswith('.py'):
            script_name += '.py'
        
        for repo_info in self.config["repos"].values():
            if script_name in repo_info["scripts"]:
                return f"{repo_info['raw_base']}/{repo_info['scripts'][script_name]}"
        return None

    def _get_raw_url_base(self, url: str) -> str:
        # Convert GitHub URLs to raw content URLs
        if "github.com" in url:
            parts = url.split("github.com/", 1)[1].split("/")
            return f"https://raw.githubusercontent.com/{parts[0]}/{parts[1]}/main"
        return url  # For other platforms or direct raw URLs