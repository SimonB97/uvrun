# CHANGELOG



## v0.1.0 (2025-01-19)

### Build

* build: modify build requirements and command in pyproject.toml ([`2726818`](https://github.com/SimonB97/uvrun/commit/2726818395898ecfbc3b31a823365fdc204d7de7))

### Ci

* ci: update workflows and commitlint configuration ([`7f26f75`](https://github.com/SimonB97/uvrun/commit/7f26f754102daaf4f2e08c55b2d83b8c15c4a506))

### Feature

* feat: add commit linting, automated publishing workflow, pre-commit hooks, and code quality tools ([`567d365`](https://github.com/SimonB97/uvrun/commit/567d3656510c6ca777b2786635eb83def775b72e))

### Unknown

* Merge branch &#39;feat/improve-cli&#39; ([`eff7e2a`](https://github.com/SimonB97/uvrun/commit/eff7e2a67e3239182c272dc17a5ea4ff4590fdb1))

* Merge pull request #1 from SimonB97/feat/improve-cli

feat: add commit linting, automated publishing workflow, pre-commit hooks, and code quality tools ([`e17d377`](https://github.com/SimonB97/uvrun/commit/e17d3770cca20c8a773714dc3cbbf27fadb24b29))

* Refactor uvrun CLI: rename --add-repo option to --add

- Changed the CLI option from --add-repo to --add for clarity.
- Updated the corresponding function parameter and internal logic to reflect this change. ([`304deee`](https://github.com/SimonB97/uvrun/commit/304deee4151ab4009ec861f6554eb47e8d166910))

* Add MIT License, update project name and version

- Added LICENSE file with MIT License.
- Renamed project from &#34;uvrun&#34; to &#34;uvrun_simonb97&#34; and updated version to 0.0.1 in pyproject.toml.
- Created README.md with installation and usage instructions.
- Initialized __init__.py for the package structure. ([`6e13c3f`](https://github.com/SimonB97/uvrun/commit/6e13c3fc4605c1df341981784ce87d5804d51944))

* Refactor uvrun CLI and remove unused files:
- Updated the help text for the --add-repo option to specify GitHub repository URLs.
- Deleted the execute.py and repo.py files as they are no longer needed for the current functionality. ([`9e6a0f6`](https://github.com/SimonB97/uvrun/commit/9e6a0f67bb9f3e923c5ba20bd25ecc4080bfed93))

* Update author information in pyproject.toml ([`e455c3b`](https://github.com/SimonB97/uvrun/commit/e455c3ba60d333e06fb93d5a1f225a460b651a9b))

* Update .gitignore ([`ccd4c2d`](https://github.com/SimonB97/uvrun/commit/ccd4c2d6db0a57cf9b986dee5cd5dd8060aec689))

* Enhance uvrun CLI:
- Added support for passing additional arguments to the `uv run` command.
- Updated script handling to allow both `.py` and non-`.py` extensions.
- Improved script listing format for better readability.
- Refactored argument parsing in the CLI for clarity and flexibility. ([`4ff5213`](https://github.com/SimonB97/uvrun/commit/4ff5213c9089a33c7514b71e905f381ba575fe35))

* Initialize uvrun project with core functionality- initial running state ([`000fd5d`](https://github.com/SimonB97/uvrun/commit/000fd5dd6afbcf307e18782234f7ef0b270cc294))
