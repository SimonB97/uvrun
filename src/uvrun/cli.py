import click
from rich.console import Console
from typing import Optional
import subprocess

from .config import Config
from .discover import fetch_script_list

console = Console()

@click.command(help="Run Python scripts with inline metadata directly from URLs")
@click.version_option()
@click.option("--add-repo", "-ar", help="Add a repository URL containing Python scripts")
@click.option("--list", "-l", is_flag=True, help="List all available scripts")
@click.option("--script", "-s", help="Script name to run followed by optional quoted arguments")
def cli(add_repo: Optional[str], list: bool, script: Optional[str]) -> None:
    config = Config()

    if add_repo:
        try:
            scripts = fetch_script_list(add_repo)
            config.add_repo(add_repo, scripts)
            script_count = len(scripts)
            console.print(f"[green]Found {script_count} script{'s' if script_count != 1 else ''} in repository[/green]")
        except Exception as e:
            console.print(f"[red]Failed to add repository: {e}[/red]")
            return

    if list:
        show_list()
        return
        
    if script:
        script_parts = script.split() if '"' not in script else script[1:-1].split()
        script_name = script_parts[0]
        script_args = script_parts[1:] if len(script_parts) > 1 else []
        
        script_url = config.get_script_url(script_name)
        if script_url:
            cmd = ["uv", "run", script_url] + script_args
            subprocess.run(cmd)
        else:
            console.print(f"[red]Script {script_name} not found[/red]")

def show_list():
    config = Config()
    for repo_url, repo_info in config.config["repos"].items():
        console.print(f"\n[bold blue]{repo_url}[/bold blue]")
        for script_name, script_path in sorted(repo_info["scripts"].items()):
            console.print(f"  [green]{script_name}[/green] - {script_path}")

def main():
    cli()