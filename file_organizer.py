import os
import shutil
import argparse
from datetime import datetime


def create_and_move(file_path, destination, verbose=False):
    """
    Creates a directory if it doesn't exist and moves the file to this directory.
    Args:
    file_path (str): The full path of the file to be moved.
    destination (str): The target directory to move the file to.
    verbose (bool): If True, prints detailed information about the file movement.
    """
    os.makedirs(destination, exist_ok=True)
    shutil.move(file_path, os.path.join(
        destination, os.path.basename(file_path)))
    if verbose:
        print(f"Moved '{os.path.basename(file_path)}' to '{destination}'.")


def organize_by_date(directory, verbose=False):
    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)
        if os.path.isfile(file_path):
            mod_date = datetime.fromtimestamp(
                os.path.getmtime(file_path)).strftime('%Y-%m-%d')
            destination = os.path.join(directory, mod_date)
            create_and_move(file_path, destination, verbose)


def organize_by_type(directory, verbose=False):
    for file in os.listdir(directory):
        if not os.path.isfile(os.path.join(directory, file)):
            continue
        file_type = file.split('.')[-1]
        target_dir = os.path.join(directory, file_type)
        create_and_move(os.path.join(directory, file), target_dir, verbose)


def organize_by_size(directory, verbose=False, small_limit=10*1024**2, medium_limit=50*1024**2):
    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)
        if os.path.isfile(file_path):
            size = os.path.getsize(file_path)
            if size < small_limit:
                size_folder = "Small"
            elif size < medium_limit:
                size_folder = "Medium"
            else:
                size_folder = "Large"
            destination = os.path.join(directory, size_folder)
            create_and_move(file_path, destination, verbose)


def parse_args():
    parser = argparse.ArgumentParser(
        description="Organizes files in the specified directory based on specific criteria.")
    parser.add_argument('directory', type=str, help="Directory to organize.")
    parser.add_argument('--criteria', type=str, default="type",
                        help="Order of organization criteria, separated by commas: date,type,size")
    parser.add_argument('-v', '--verbose', action='store_true',
                        help="Enable verbose output for detailed information.")
    return parser.parse_args()


def apply_criterion(directory, criterion, remaining_criteria, verbose=False):
    functions = {
        'date': organize_by_date,
        'type': organize_by_type,
        'size': organize_by_size,
    }
    if criterion in functions:
        if verbose:
            print(f"Organizing by {criterion} in {directory}...")
        functions[criterion](directory, verbose)

        if remaining_criteria:
            for subdirectory in [d for d in os.listdir(directory) if os.path.isdir(os.path.join(directory, d))]:
                next_criterion = remaining_criteria[0]
                apply_criterion(os.path.join(directory, subdirectory),
                                next_criterion, remaining_criteria[1:], verbose)


def organize_files(directory, criteria, verbose=False):
    criteria_list = criteria.split(',')
    if criteria_list:
        apply_criterion(
            directory, criteria_list[0], criteria_list[1:], verbose)


def main():
    args = parse_args()
    organize_files(args.directory, args.criteria, args.verbose)


if __name__ == "__main__":
    main()
