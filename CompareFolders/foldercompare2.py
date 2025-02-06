import os

def compare_dir_layout(folder_path1, folder_path2):
	def _compare_dir_layout(folder_path1, folder_path2):
		for (dirpath, dirnames, filenames) in os.walk(folder_path1):
			for filename in filenames:
				relative_path = dirpath.replace(folder_path1, "")
				if os.path.exists( folder_path2 + relative_path + '\\' +  filename) is False:
					print(relative_path, filename)
		return

	print('files in "' + folder_path1 + '" but not in "' + folder_path2 +'"')
	_compare_dir_layout(folder_path1, folder_path2)
	print('files in "' + folder_path2 + '" but not in "' + folder_path1 +'"')
	_compare_dir_layout(folder_path2, folder_path1)

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 3:
        print("Usage: python script.py <folder_path1> <folder_path2>")
        sys.exit(1)

    folder_path1 = sys.argv[1]
    folder_path2 = sys.argv[2]

    compare_dir_layout(folder_path1, folder_path2)