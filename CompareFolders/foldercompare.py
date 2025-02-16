import os
import unicodedata

def normalize_unicode(value):
    """Normalize Unicode strings to NFC form."""
    return unicodedata.normalize('NFC', value).lower()

def remove_extension(filename):
    """Remove file extension for comparison purposes."""
    return os.path.splitext(filename)[0]

IGNORE_LIST = {".ds_store"}  # Files to ignore in the comparison

def compare_folder_contents(folder1, folder2):
    try:
        # Walk through the directory trees
        folder1_items = {}
        folder2_items = {}

        for root, dirs, files in os.walk(folder1):
            relative_path = normalize_unicode(os.path.relpath(root, folder1).strip())
            normalized_items = set(normalize_unicode(remove_extension(item)) for item in dirs + files if item.lower() not in IGNORE_LIST)
            folder1_items[relative_path] = normalized_items

        for root, dirs, files in os.walk(folder2):
            relative_path = normalize_unicode(os.path.relpath(root, folder2).strip())
            normalized_items = set(normalize_unicode(remove_extension(item)) for item in dirs + files if item.lower() not in IGNORE_LIST)
            folder2_items[relative_path] = normalized_items

        # Find all unique relative paths from both folder trees
        all_paths = set(folder1_items.keys()).union(set(folder2_items.keys()))

        for path in sorted(all_paths):
            items1 = folder1_items.get(path, set())
            items2 = folder2_items.get(path, set())

            only_in_folder1 = items1 - items2
            only_in_folder2 = items2 - items1

            if only_in_folder1 or only_in_folder2:
                print(f"Differences in '{path}':")
                if only_in_folder1:
                    print("  Items only in folder 1:")
                    for item in sorted(only_in_folder1):
                        print(f"    {item}")
                if only_in_folder2:
                    print("  Items only in folder 2:")
                    for item in sorted(only_in_folder2):
                        print(f"    {item}")

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
