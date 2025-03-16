import os
import unicodedata

def normalize_unicode(value):
    """Normalize Unicode strings to NFC form."""
    return unicodedata.normalize('NFC', value).lower()

def remove_extension(filename):
    """Remove file extension for comparison purposes."""
    return os.path.splitext(filename)[0]

def print_differences(items, folder_number):
    if items:
        print(f"  Items only in folder {folder_number}:")
        for item, is_dir in sorted(items):
            color = "\033[34m" if is_dir else "\033[32m"
            print(f"    - {color}{item}\033[0m")  # Blue for directories, Green for files


IGNORE_LIST = {".ds_store"}  # Files to ignore in the comparison

def compare_folder_contents(folder1, folder2):
    try:
        # Walk through the directory trees
        folder1_items = {}
        folder2_items = {}

        for root, dirs, files in os.walk(folder1):
            relative_path = normalize_unicode(os.path.relpath(root, folder1).strip())
            normalized_items = {(normalize_unicode(remove_extension(item)), True) for item in dirs if item.lower() not in IGNORE_LIST}
            normalized_items.update({(normalize_unicode(remove_extension(item)), False) for item in files if item.lower() not in IGNORE_LIST})
            folder1_items[relative_path] = normalized_items

        for root, dirs, files in os.walk(folder2):
            relative_path = normalize_unicode(os.path.relpath(root, folder2).strip())
            normalized_items = {(normalize_unicode(remove_extension(item)), True) for item in dirs if item.lower() not in IGNORE_LIST}
            normalized_items.update({(normalize_unicode(remove_extension(item)), False) for item in files if item.lower() not in IGNORE_LIST})
            folder2_items[relative_path] = normalized_items

        # Find all unique relative paths from both folder trees
        all_paths = set(folder1_items.keys()).union(set(folder2_items.keys()))

        for path in sorted(all_paths):
            items1 = folder1_items.get(path, set())
            items2 = folder2_items.get(path, set())

            only_in_folder1 = items1 - items2
            only_in_folder2 = items2 - items1

            if only_in_folder1 or only_in_folder2:
                print(f"\nDifferences in '{path}':")
                print_differences(only_in_folder1, 1)
                print_differences(only_in_folder2, 2)

    except Exception as e:
        print(f"An error occurred while comparing folders: {e}")

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 3:
        print("Usage: python script.py <folder_path1> <folder_path2>")
        sys.exit(1)

    folder_path1 = sys.argv[1]
    folder_path2 = sys.argv[2]

    compare_folder_contents(folder_path1, folder_path2)
