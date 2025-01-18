import subprocess
from pathlib import Path

def run_script(script_path: Path, args: tuple[str, ...]) -> int:
    cmd = ["uv", "run", str(script_path)] + list(args)
    return subprocess.run(cmd).returncode