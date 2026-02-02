# hacky-bits

## Tools

### `foldercompare` 🔧

A small CLI tool for comparing the contents of two folder trees.

**What it does**
- Walks two directory trees and prints differences per relative path.
- Normalizes Unicode (NFC) and compares names case-insensitively.
- Compares item names without file extensions (so `file.txt` and `file.md` match by name).
- Shows directories in blue and files in green in the terminal output.

**Usage**

Run from the repository root or the script directory:

```bash
# From repo root
python foldercompare/foldercompare.py <path/to/folder1> <path/to/folder2>

# Or from inside the foldercompare directory
python foldercompare.py <path/to/folder1> <path/to/folder2>
```

**Configuration & Notes**
- Edit the `IGNORE_LIST` set in `foldercompare/foldercompare.py` to ignore additional filenames (defaults to `.ds_store`).
- The script strips file extensions during comparison. To make comparisons extension-aware, modify `remove_extension()` in `foldercompare/foldercompare.py`.
- Requires Python 3.6+.

**Example output**

```
Differences in 'some/subpath':
  Items only in folder 1:
    - \033[34mmydir\033[0m
    - \033[32mmyfile\033[0m
  Items only in folder 2:
    - \033[32motherfile\033[0m
```

(Note: color escape sequences will render as colored text in most terminals.)

---

