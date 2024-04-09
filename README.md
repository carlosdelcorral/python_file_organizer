# File Organizer Script

## Overview

The File Organizer Script is a Python-based utility designed to help users automate the process of organizing files within a specified directory. By categorizing files based on their modification date, type (extension), or size, it simplifies file management and enhances productivity.

## Features

- **Date Organization**: Sorts files into subdirectories named after their modification date.
- **Type Organization**: Groups files into subdirectories based on their extension.
- **Size Organization**: Segregates files into "Small", "Medium", or "Large" folders based on predefined size thresholds.
- **Verbose Mode**: Provides detailed logs of the script’s operations, facilitating easy tracking and debugging.

## Requirements

- Python 3.x
- No additional Python packages are required, as the script utilizes only built-in libraries (`os`, `shutil`, `argparse`, `datetime`).

## Installation

No installation is necessary beyond having Python 3.x installed on your system. To get started with the File Organizer Script, clone this repository or download the script to your local machine:

```bash
git clone https://github.com/carlosdelcorral/file-organizer.git
```

## Usage
Navigate to the script's directory in your command line interface and execute the script as follows:
```bash
python file_organizer.py <directory> [options]
```

## Arguments

<directory>: Path to the directory you wish to organize.

## Options

--criteria <criteria>: Specifies the organization criteria as a comma-separated list (date, type, size). Defaults to type if not specified.

-v, --verbose: Enables verbose mode, printing detailed information about file movements.

## Examples
Organize files by type in a specific directory:

```bash
python file_organizer.py /path/to/your/directory --criteria type
```

Organize files by date, then by type, and finally by size with verbose output:

```bash
python file_organizer.py /path/to/your/directory --criteria date,type,size --verbose
```
