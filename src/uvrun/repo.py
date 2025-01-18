from pathlib import Path
import git
from typing import Optional

def clone_repo(url: str, target_dir: Path) -> Optional[Path]:
    try:
        repo = git.Repo.clone_from(url, target_dir)
        return target_dir
    except git.GitCommandError:
        return None