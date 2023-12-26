# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2023-12-26
### Changed
- Moved away from using `dotenvs` to using a JSON config file
- Improved the `README.md` file by adding further information, todo items and such
- Changed `.gitignore` to only exclude `config.json` as opposed to all `*.json` files

### Added
- `requirements.txt` file

## [0.0.1] - 2023-12-07
### Added
- Comments along the code

### Changed
- Variable name for storing response data went from `r` to `getRequest`
- Header size from `<h3>` to `<h2>`
 
### Fixed
- Double encoding causing to pages breaking when double quotes being used

## [0.0.1] - 2023-12-06
### Added
- Strip new line characters from user input to prevent `\n` characters from being added
- Current date and time header using `datetime` module

### Removed
- Removed additional loop to convert user input to markdown - now handled in iniital user capture loop
- Removed `print()` statements and cleaned up code

## [0.0.1] - 2023-12-03

### Added
- Initial commit adding main script, readme and changelog
