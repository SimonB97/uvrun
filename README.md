# uvrun

Run Python scripts with inline metadata directly from URLs. This simple tool integrates with [uv](https://github.com/astral-sh/uv) to provide a seamless experience for running Python scripts from GitHub repositories.

## Features

- Run Python scripts directly from GitHub repositories
- Manage multiple script repositories
- Smart script discovery with inline metadata
- Pass arguments directly to scripts and uv
- List available scripts with a nice directory structure

## Installation

```bash
pip install uvrun
```

## Usage

Add a repository:

```bash
uvrun --add https://github.com/username/repo
```

List available scripts:

```bash
uvrun --list
```

Run a script:

```bash
uvrun script_name arg1 arg2
```

(Note: both script_name and script_name.py are valid)

With specific Python version:

```bash
uvrun script_name --uv-args "--refresh"
```

## Script Metadata

To make a script discoverable by uvrun, add the following [inline metadata](https://peps.python.org/pep-0723/) at the top of the file:

```python
# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "flask>=2.0.0",
#     "requests>=2.31.0",
# ]
# ///
```

## License

[MIT License](LICENSE)
