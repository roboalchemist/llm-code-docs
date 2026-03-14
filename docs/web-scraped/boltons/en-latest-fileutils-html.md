# Source: https://boltons.readthedocs.io/en/latest/fileutils.html

Title: Filesystem helpers — boltons 25.0.0 documentation

URL Source: https://boltons.readthedocs.io/en/latest/fileutils.html

Markdown Content:
`fileutils` - Filesystem helpers[](https://boltons.readthedocs.io/en/latest/fileutils.html#module-boltons.fileutils "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------

Virtually every Python programmer has used Python for wrangling disk contents, and `fileutils` collects solutions to some of the most commonly-found gaps in the standard library.

Creating, Finding, and Copying[](https://boltons.readthedocs.io/en/latest/fileutils.html#creating-finding-and-copying "Link to this heading")
----------------------------------------------------------------------------------------------------------------------------------------------

Python’s [`os`](https://docs.python.org/3/library/os.html#module-os "(in Python v3.14)"), [`os.path`](https://docs.python.org/3/library/os.path.html#module-os.path "(in Python v3.14)"), and [`shutil`](https://docs.python.org/3/library/shutil.html#module-shutil "(in Python v3.14)") modules provide good coverage of file wrangling fundamentals, and these functions help close a few remaining gaps.

boltons.fileutils.mkdir_p(_path_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/fileutils.html#mkdir_p)[](https://boltons.readthedocs.io/en/latest/fileutils.html#boltons.fileutils.mkdir_p "Link to this definition")
Creates a directory and any parent directories that may need to be created along the way, without raising errors for any existing directories. This function mimics the behavior of the `mkdir -p` command available in Linux/BSD environments, but also works on Windows.

boltons.fileutils.iter_find_files(_directory_, _patterns_, _ignored=None_, _include\_dirs=False_, _max\_depth=None_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/fileutils.html#iter_find_files)[](https://boltons.readthedocs.io/en/latest/fileutils.html#boltons.fileutils.iter_find_files "Link to this definition")
Returns a generator that yields file paths under a _directory_, matching _patterns_ using [glob](https://en.wikipedia.org/wiki/Glob_%28programming%29) syntax (e.g., `*.txt`). Also supports _ignored_ patterns.

Parameters:
*   **directory** ([_str_](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) – Path that serves as the root of the search. Yielded paths will include this as a prefix.

*   **patterns** ([_str_](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")_or_[_list_](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")) – A single pattern or list of glob-formatted patterns to find under _directory_.

*   **ignored** ([_str_](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")_or_[_list_](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")) – A single pattern or list of glob-formatted patterns to ignore.

*   **include_dirs** ([_bool_](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")) – Whether to include directories that match patterns, as well. Defaults to `False`.

*   **max_depth** ([_int_](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")) – traverse up to this level of subdirectory. I.e., 0 for the specified _directory_ only, 1 for _directory_ and one level of subdirectory.

For example, finding Python files in the current directory:

>>> _CUR_DIR = os.path.dirname(os.path.abspath( __file__ ))
>>> filenames = sorted(iter_find_files(_CUR_DIR, '*.py'))
>>> os.path.basename(filenames[-1])
'urlutils.py'

Or, Python files while ignoring emacs lockfiles:

>>> filenames = iter_find_files(_CUR_DIR, '*.py', ignored='.#*')

boltons.fileutils.copytree(_src_, _dst_, _symlinks=False_, _ignore=None_)[](https://boltons.readthedocs.io/en/latest/fileutils.html#boltons.fileutils.copytree "Link to this definition")
The `copy_tree` function is an exact copy of the built-in [`shutil.copytree()`](https://docs.python.org/3/library/shutil.html#shutil.copytree "(in Python v3.14)"), with one key difference: it will not raise an exception if part of the tree already exists. It achieves this by using [`mkdir_p()`](https://boltons.readthedocs.io/en/latest/fileutils.html#boltons.fileutils.mkdir_p "boltons.fileutils.mkdir_p").

As of Python 3.8, you may pass [`shutil.copytree()`](https://docs.python.org/3/library/shutil.html#shutil.copytree "(in Python v3.14)") the dirs_exist_ok=True flag to achieve the same effect.

Parameters:
*   **src** ([_str_](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) – Path of the source directory to copy.

*   **dst** ([_str_](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) – Destination path. Existing directories accepted.

*   **symlinks** ([_bool_](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")) – If `True`, copy symlinks rather than their contents.

*   **ignore** (_callable_) – A callable that takes a path and directory listing, returning the files within the listing to be ignored.

For more details, check out [`shutil.copytree()`](https://docs.python.org/3/library/shutil.html#shutil.copytree "(in Python v3.14)") and [`shutil.copy2()`](https://docs.python.org/3/library/shutil.html#shutil.copy2 "(in Python v3.14)").

boltons.fileutils.rotate_file(_filename_, _*_, _keep:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")=5_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/fileutils.html#rotate_file)[](https://boltons.readthedocs.io/en/latest/fileutils.html#boltons.fileutils.rotate_file "Link to this definition")
If _filename.ext_ exists, it will be moved to _filename.1.ext_, with all conflicting filenames being moved up by one, dropping any files beyond _keep_.

After rotation, _filename_ will be available for creation as a new file.

Fails if _filename_ is not a file or if _keep_ is not > 0.

Atomic File Saving[](https://boltons.readthedocs.io/en/latest/fileutils.html#atomic-file-saving "Link to this heading")
------------------------------------------------------------------------------------------------------------------------

Ideally, the road to success should never put current progress at risk. And that’s exactly why [`atomic_save()`](https://boltons.readthedocs.io/en/latest/fileutils.html#boltons.fileutils.atomic_save "boltons.fileutils.atomic_save") and [`AtomicSaver`](https://boltons.readthedocs.io/en/latest/fileutils.html#boltons.fileutils.AtomicSaver "boltons.fileutils.AtomicSaver") exist.

Using the same API as a writable file, all output is saved to a temporary file, and when the file is closed, the old file is replaced by the new file in a single system call, portable across all major operating systems. No more partially-written or partially-overwritten files.

boltons.fileutils.atomic_save(_dest\_path_, _**kwargs_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/fileutils.html#atomic_save)[](https://boltons.readthedocs.io/en/latest/fileutils.html#boltons.fileutils.atomic_save "Link to this definition")
A convenient interface to the [`AtomicSaver`](https://boltons.readthedocs.io/en/latest/fileutils.html#boltons.fileutils.AtomicSaver "boltons.fileutils.AtomicSaver") type. Example:

>>> try:
...     with atomic_save("file.txt", text_mode=True) as fo:
...         _ = fo.write('bye')
...         1/0  # will error
...         fo.write('bye')
... except ZeroDivisionError:
...     pass  # at least our file.txt didn't get overwritten

See the [`AtomicSaver`](https://boltons.readthedocs.io/en/latest/fileutils.html#boltons.fileutils.AtomicSaver "boltons.fileutils.AtomicSaver") documentation for details.

_class_ boltons.fileutils.AtomicSaver(_dest\_path_, _**kwargs_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/fileutils.html#AtomicSaver)[](https://boltons.readthedocs.io/en/latest/fileutils.html#boltons.fileutils.AtomicSaver "Link to this definition")
`AtomicSaver` is a configurable [context manager](https://docs.python.org/2/reference/compound_stmts.html#with) that provides a writable `file` which will be moved into place as long as no exceptions are raised within the context manager’s block. These “part files” are created in the same directory as the destination path to ensure atomic move operations (i.e., no cross-filesystem moves occur).

Parameters:
*   **dest_path** ([_str_](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) – The path where the completed file will be written.

*   **overwrite** ([_bool_](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")) – Whether to overwrite the destination file if it exists at completion time. Defaults to `True`.

*   **file_perms** ([_int_](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")) – Integer representation of file permissions for the newly-created file. Defaults are, when the destination path already exists, to copy the permissions from the previous file, or if the file did not exist, to respect the user’s configured [umask](https://en.wikipedia.org/wiki/Umask), usually resulting in octal 0644 or 0664.

*   **text_mode** ([_bool_](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")) – Whether to open the destination file in text mode (i.e., `'w'` not `'wb'`). Defaults to `False` (`wb`).

*   **part_file** ([_str_](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) – Name of the temporary _part\_file_. Defaults to _dest\_path_ + `.part`. Note that this argument is just the filename, and not the full path of the part file. To guarantee atomic saves, part files are always created in the same directory as the destination path.

*   **overwrite_part** ([_bool_](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")) – Whether to overwrite the _part\_file_, should it exist at setup time. Defaults to `False`, which results in an [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "(in Python v3.14)") being raised on pre-existing part files. Be careful of setting this to `True` in situations when multiple threads or processes could be writing to the same part file.

*   **rm_part_on_exc** ([_bool_](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")) – Remove _part\_file_ on exception cases. Defaults to `True`, but `False` can be useful for recovery in some cases. Note that resumption is not automatic and by default an [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "(in Python v3.14)") is raised if the _part\_file_ exists.

Practically, the AtomicSaver serves a few purposes:

> *   Avoiding overwriting an existing, valid file with a partially written one.
> 
> *   Providing a reasonable guarantee that a part file only has one writer at a time.
> 
> *   Optional recovery of partial data in failure cases.

boltons.fileutils.atomic_rename(_src_, _dst_, _overwrite=False_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/fileutils.html#atomic_rename)[](https://boltons.readthedocs.io/en/latest/fileutils.html#boltons.fileutils.atomic_rename "Link to this definition")
Rename _src_ to _dst_, replacing _dst_ if [*](https://boltons.readthedocs.io/en/latest/fileutils.html#id1)overwrite is True

boltons.fileutils.replace(_src_, _dst_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/fileutils.html#replace)[](https://boltons.readthedocs.io/en/latest/fileutils.html#boltons.fileutils.replace "Link to this definition")
Similar to [`os.replace()`](https://docs.python.org/3/library/os.html#os.replace "(in Python v3.14)") in Python 3.3+, this function will atomically create or replace the file at path _dst_ with the file at path _src_.

On Windows, this function uses the ReplaceFile API for maximum possible atomicity on a range of filesystems.

File Permissions[](https://boltons.readthedocs.io/en/latest/fileutils.html#file-permissions "Link to this heading")
--------------------------------------------------------------------------------------------------------------------

Linux, BSD, Mac OS, and other Unix-like operating systems all share a simple, foundational file permission structure that is commonly complicit in accidental access denial, as well as file leakage. [`FilePerms`](https://boltons.readthedocs.io/en/latest/fileutils.html#boltons.fileutils.FilePerms "boltons.fileutils.FilePerms") was built to increase clarity and cut down on permission-related accidents when working with files from Python code.

_class_ boltons.fileutils.FilePerms(_user=''_, _group=''_, _other=''_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/fileutils.html#FilePerms)[](https://boltons.readthedocs.io/en/latest/fileutils.html#boltons.fileutils.FilePerms "Link to this definition")
The [`FilePerms`](https://boltons.readthedocs.io/en/latest/fileutils.html#boltons.fileutils.FilePerms "boltons.fileutils.FilePerms") type is used to represent standard POSIX filesystem permissions:

> *   Read
> 
> *   Write
> 
> *   Execute

Across three classes of user:

> *   Owning (u)ser
> 
> *   Owner’s (g)roup
> 
> *   Any (o)ther user

This class assists with computing new permissions, as well as working with numeric octal `777`-style and `rwx`-style permissions. Currently it only considers the bottom 9 permission bits; it does not support sticky bits or more advanced permission systems.

Parameters:
*   **user** ([_str_](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) – A string in the ‘rwx’ format, omitting characters for which owning user’s permissions are not provided.

*   **group** ([_str_](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) – A string in the ‘rwx’ format, omitting characters for which owning group permissions are not provided.

*   **other** ([_str_](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) – A string in the ‘rwx’ format, omitting characters for which owning other/world permissions are not provided.

There are many ways to use [`FilePerms`](https://boltons.readthedocs.io/en/latest/fileutils.html#boltons.fileutils.FilePerms "boltons.fileutils.FilePerms"):

>>> FilePerms(user='rwx', group='xrw', other='wxr')  # note character order
FilePerms(user='rwx', group='rwx', other='rwx')
>>> int(FilePerms('r', 'r', ''))
288
>>> oct(288)[-3:]  # XXX Py3k
'440'

See also the `FilePerms.from_int()` and `FilePerms.from_path()` classmethods for useful alternative ways to construct [`FilePerms`](https://boltons.readthedocs.io/en/latest/fileutils.html#boltons.fileutils.FilePerms "boltons.fileutils.FilePerms") objects.

Miscellaneous[](https://boltons.readthedocs.io/en/latest/fileutils.html#miscellaneous "Link to this heading")
--------------------------------------------------------------------------------------------------------------

_class_ boltons.fileutils.DummyFile(_path_, _mode='r'_, _buffering=None_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/fileutils.html#DummyFile)[](https://boltons.readthedocs.io/en/latest/fileutils.html#boltons.fileutils.DummyFile "Link to this definition")
