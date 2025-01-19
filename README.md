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
pip install uvrun_simonb97
```

## Usage

Add a repository:

```bash
uvrun --add-repo https://github.com/username/repo
```

List available scripts:

```bash
uvrun --list
```

Run a script:

```bash
uvrun script_name arg1 arg2
```

With specific Python version:

```bash
uvrun script_name --uv-args "--python 3.11"
```

## Script Metadata

To make a script discoverable by uvrun, add the following metadata:

```python
# /// script
# /// description: What your script does
# ///
```

## License

MIT [License](LICENSE)
