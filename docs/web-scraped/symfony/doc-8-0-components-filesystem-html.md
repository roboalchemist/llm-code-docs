# Source: https://symfony.com/doc/8.0/components/filesystem.html

Title: The Filesystem Component (Symfony Docs)

URL Source: https://symfony.com/doc/8.0/components/filesystem.html

Markdown Content:
[Edit this page](https://github.com/symfony/symfony-docs/edit/8.0/components/filesystem.rst)

> The Filesystem component provides platform-independent utilities for filesystem operations and for file/directory paths manipulation.

[Installation](https://symfony.com/doc/8.0/components/filesystem.html#installation "Permalink to this headline")
----------------------------------------------------------------------------------------------------------------

Note

If you install this component outside of a Symfony application, you must require the `vendor/autoload.php` file in your code to enable the class autoloading mechanism provided by Composer. Read [this article](https://symfony.com/doc/current/components/using_components.html) for more details.

[Filesystem Utilities](https://symfony.com/doc/8.0/components/filesystem.html#filesystem-utilities "Permalink to this headline")
--------------------------------------------------------------------------------------------------------------------------------

### [`mkdir`](https://symfony.com/doc/8.0/components/filesystem.html#mkdir "Permalink to this headline")

[mkdir()](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Filesystem/Filesystem.php#:~:text=function%20mkdir "Symfony\Component\Filesystem\Filesystem::mkdir()") creates a directory recursively. On POSIX filesystems, directories are created with a default mode value `0777`. You can use the second argument to set your own mode:

Note

You can pass an array or any [Traversable](https://secure.php.net/manual/en/class.traversable.php "Traversable") object as the first argument.

Note

This function ignores already existing directories.

Note

The directory permissions are affected by the current [umask](https://en.wikipedia.org/wiki/Umask). Set the `umask` for your webserver, use PHP's [umask](https://secure.php.net/manual/en/function.umask.php "umask") function or use the [chmod](https://secure.php.net/manual/en/function.chmod.php "chmod") function after the directory has been created.

### [`exists`](https://symfony.com/doc/8.0/components/filesystem.html#exists "Permalink to this headline")

[exists()](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Filesystem/Filesystem.php#:~:text=function%20exists "Symfony\Component\Filesystem\Filesystem::exists()") checks for the presence of one or more files or directories and returns `false` if any of them is missing:

Note

You can pass an array or any [Traversable](https://secure.php.net/manual/en/class.traversable.php "Traversable") object as the first argument.

### [`copy`](https://symfony.com/doc/8.0/components/filesystem.html#copy "Permalink to this headline")

[copy()](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Filesystem/Filesystem.php#:~:text=function%20copy "Symfony\Component\Filesystem\Filesystem::copy()") makes a copy of a single file (use [mirror()](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Filesystem/Filesystem.php#:~:text=function%20mirror "Symfony\Component\Filesystem\Filesystem::mirror()") to copy directories). If the target already exists, the file is copied only if the source modification date is later than the target. This behavior can be overridden by the third boolean argument:

### [`touch`](https://symfony.com/doc/8.0/components/filesystem.html#touch "Permalink to this headline")

[touch()](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Filesystem/Filesystem.php#:~:text=function%20touch "Symfony\Component\Filesystem\Filesystem::touch()") sets access and modification time for a file. The current time is used by default. You can set your own with the second argument. The third argument is the access time:

Note

You can pass an array or any [Traversable](https://secure.php.net/manual/en/class.traversable.php "Traversable") object as the first argument.

### [`chown`](https://symfony.com/doc/8.0/components/filesystem.html#chown "Permalink to this headline")

[chown()](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Filesystem/Filesystem.php#:~:text=function%20chown "Symfony\Component\Filesystem\Filesystem::chown()") changes the owner of a file. The third argument is a boolean recursive option:

Note

You can pass an array or any [Traversable](https://secure.php.net/manual/en/class.traversable.php "Traversable") object as the first argument.

### [`chgrp`](https://symfony.com/doc/8.0/components/filesystem.html#chgrp "Permalink to this headline")

[chgrp()](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Filesystem/Filesystem.php#:~:text=function%20chgrp "Symfony\Component\Filesystem\Filesystem::chgrp()") changes the group of a file. The third argument is a boolean recursive option:

Note

You can pass an array or any [Traversable](https://secure.php.net/manual/en/class.traversable.php "Traversable") object as the first argument.

### [`chmod`](https://symfony.com/doc/8.0/components/filesystem.html#chmod "Permalink to this headline")

[chmod()](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Filesystem/Filesystem.php#:~:text=function%20chmod "Symfony\Component\Filesystem\Filesystem::chmod()") changes the mode or permissions of a file. The fourth argument is a boolean recursive option:

Note

You can pass an array or any [Traversable](https://secure.php.net/manual/en/class.traversable.php "Traversable") object as the first argument.

### [`remove`](https://symfony.com/doc/8.0/components/filesystem.html#remove "Permalink to this headline")

[remove()](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Filesystem/Filesystem.php#:~:text=function%20remove "Symfony\Component\Filesystem\Filesystem::remove()") deletes files, directories and symlinks:

Note

You can pass an array or any [Traversable](https://secure.php.net/manual/en/class.traversable.php "Traversable") object as the first argument.

### [`rename`](https://symfony.com/doc/8.0/components/filesystem.html#rename "Permalink to this headline")

[rename()](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Filesystem/Filesystem.php#:~:text=function%20rename "Symfony\Component\Filesystem\Filesystem::rename()") changes the name of a single file or directory:

### [`symlink`](https://symfony.com/doc/8.0/components/filesystem.html#symlink "Permalink to this headline")

[symlink()](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Filesystem/Filesystem.php#:~:text=function%20symlink "Symfony\Component\Filesystem\Filesystem::symlink()") creates a symbolic link from the target to the destination. If the filesystem does not support symbolic links, a third boolean argument is available:

### [`readlink`](https://symfony.com/doc/8.0/components/filesystem.html#readlink "Permalink to this headline")

[readlink()](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Filesystem/Filesystem.php#:~:text=function%20readlink "Symfony\Component\Filesystem\Filesystem::readlink()") read links targets.

The [readlink()](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Filesystem/Filesystem.php#:~:text=function%20readlink "Symfony\Component\Filesystem\Filesystem::readlink()") method provided by the Filesystem component behaves in the same way on all operating systems (unlike PHP's [readlink](https://secure.php.net/manual/en/function.readlink.php "readlink") function):

Its behavior is the following:

* When `$canonicalize` is `false`:

  * if `$path` does not exist or is not a link, it returns `null`.
  * if `$path` is a link, it returns the next direct target of the link without considering the existence of the target.

* When `$canonicalize` is `true`:

  * if `$path` does not exist, it returns null.
  * if `$path` exists, it returns its absolute fully resolved final version.

Note

If you wish to canonicalize the path without checking its existence, you can use [canonicalize()](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Filesystem/Path.php#:~:text=function%20canonicalize "Symfony\Component\Filesystem\Path::canonicalize()") method instead.

### [`makePathRelative`](https://symfony.com/doc/8.0/components/filesystem.html#makepathrelative "Permalink to this headline")

[makePathRelative()](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Filesystem/Filesystem.php#:~:text=function%20makePathRelative "Symfony\Component\Filesystem\Filesystem::makePathRelative()") takes two absolute paths and returns the relative path from the second path to the first one:

### [`mirror`](https://symfony.com/doc/8.0/components/filesystem.html#mirror "Permalink to this headline")

[mirror()](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Filesystem/Filesystem.php#:~:text=function%20mirror "Symfony\Component\Filesystem\Filesystem::mirror()") copies all the contents of the source directory into the target one (use the [copy()](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Filesystem/Filesystem.php#:~:text=function%20copy "Symfony\Component\Filesystem\Filesystem::copy()") method to copy single files):

The available options are:

> * `override` (default: `false`): If true, target files newer than origin files are overwritten (see [copy()](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Filesystem/Filesystem.php#:~:text=function%20copy "Symfony\Component\Filesystem\Filesystem::copy()"))
> * `copy_on_windows` (default: `false`): Whether to copy files instead of links on Windows (see [symlink()](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Filesystem/Filesystem.php#:~:text=function%20symlink "Symfony\Component\Filesystem\Filesystem::symlink()"))
> * `delete` (default: `false`): Whether to delete files that are not in the source directory

### [`tempnam`](https://symfony.com/doc/8.0/components/filesystem.html#tempnam "Permalink to this headline")

[tempnam()](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Filesystem/Filesystem.php#:~:text=function%20tempnam "Symfony\Component\Filesystem\Filesystem::tempnam()") creates a temporary file with a unique filename, and returns its path, or throw an exception on failure:

### [`dumpFile`](https://symfony.com/doc/8.0/components/filesystem.html#dumpfile "Permalink to this headline")

[dumpFile()](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Filesystem/Filesystem.php#:~:text=function%20dumpFile "Symfony\Component\Filesystem\Filesystem::dumpFile()") saves the given contents into a file (creating the file and its directory if they don't exist). It does this in an atomic manner: it writes a temporary file first and then moves it to the new file location when it's finished. This means that the user will always see either the complete old file or complete new file (but never a partially-written file):

The `file.txt` file contains `Hello World` now.

### [`appendToFile`](https://symfony.com/doc/8.0/components/filesystem.html#appendtofile "Permalink to this headline")

[appendToFile()](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Filesystem/Filesystem.php#:~:text=function%20appendToFile "Symfony\Component\Filesystem\Filesystem::appendToFile()") adds new contents at the end of some file:

If either the file or its containing directory doesn't exist, this method creates them before appending the contents.

### [`readFile`](https://symfony.com/doc/8.0/components/filesystem.html#readfile "Permalink to this headline")

[readFile()](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Filesystem/Filesystem.php#:~:text=function%20readFile "Symfony\Component\Filesystem\Filesystem::readFile()") returns all the contents of a file as a string. Unlike the [file_get_contents](https://secure.php.net/manual/en/function.file-get-contents.php "file_get_contents") function from PHP, it throws an exception when the given file path is not readable and when passing the path to a directory instead of a file:

The `$contents` variable now stores all the contents of the `file.txt` file.

[Path Manipulation Utilities](https://symfony.com/doc/8.0/components/filesystem.html#path-manipulation-utilities "Permalink to this headline")
----------------------------------------------------------------------------------------------------------------------------------------------

Dealing with file paths usually involves some difficulties:

* Platform differences: file paths look different on different platforms. UNIX file paths start with a slash ("/"), while Windows file paths start with a system drive ("C:"). UNIX uses forward slashes, while Windows uses backslashes by default. However, Windows also accepts forward slashes, so both types of separators generally work.
* Absolute/relative paths: web applications frequently need to deal with absolute and relative paths. Converting one to the other properly is tricky and repetitive.

[Path](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Filesystem/Path.php "Symfony\Component\Filesystem\Path") provides utility methods to tackle those issues.

### [Canonicalization](https://symfony.com/doc/8.0/components/filesystem.html#canonicalization "Permalink to this headline")

Returns the shortest path name equivalent to the given path. It applies the following rules iteratively until no further processing can be done:

* "." segments are removed;
* ".." segments are resolved;
* backslashes ("\") are converted into forward slashes ("/");
* root paths ("/" and "C:/") always terminate with a slash;
* non-root paths never terminate with a slash;
* schemes (such as "phar://") are kept;
* replace `~` with the user's home directory.

You can canonicalize a path with [canonicalize()](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Filesystem/Path.php#:~:text=function%20canonicalize "Symfony\Component\Filesystem\Path::canonicalize()"):

You can pass absolute paths and relative paths to the [canonicalize()](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Filesystem/Path.php#:~:text=function%20canonicalize "Symfony\Component\Filesystem\Path::canonicalize()") method. When a relative path is passed, ".." segments at the beginning of the path are kept:

Malformed paths are returned unchanged:

### [Joining Paths](https://symfony.com/doc/8.0/components/filesystem.html#joining-paths "Permalink to this headline")

The [join()](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Filesystem/Path.php#:~:text=function%20join "Symfony\Component\Filesystem\Path::join()") method concatenates the given paths and normalizes separators. It's a cleaner alternative to string concatenation for building file paths:

The `join()` method handles multiple scenarios correctly:

Empty parts are ignored:

Leading slashes in subsequent arguments are removed:

Trailing slashes are preserved only for root paths:

Works with any number of arguments:

### [Converting Absolute/Relative Paths](https://symfony.com/doc/8.0/components/filesystem.html#converting-absolute-relative-paths "Permalink to this headline")

Absolute/relative paths can be converted with the methods [makeAbsolute()](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Filesystem/Path.php#:~:text=function%20makeAbsolute "Symfony\Component\Filesystem\Path::makeAbsolute()") and [makeRelative()](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Filesystem/Path.php#:~:text=function%20makeRelative "Symfony\Component\Filesystem\Path::makeRelative()").

[makeAbsolute()](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Filesystem/Path.php#:~:text=function%20makeAbsolute "Symfony\Component\Filesystem\Path::makeAbsolute()") method expects a relative path and a base path to base that relative path upon:

If an absolute path is passed in the first argument, the absolute path is returned unchanged:

The method resolves ".." segments, if there are any:

This method is very useful if you want to be able to accept relative paths (for example, relative to the root directory of your project) and absolute paths at the same time.

[makeRelative()](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Filesystem/Path.php#:~:text=function%20makeRelative "Symfony\Component\Filesystem\Path::makeRelative()") is the inverse operation to [makeAbsolute()](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Filesystem/Path.php#:~:text=function%20makeAbsolute "Symfony\Component\Filesystem\Path::makeAbsolute()"):

If the path is not within the base path, the method will prepend ".." segments as necessary:

Use [isAbsolute()](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Filesystem/Path.php#:~:text=function%20isAbsolute "Symfony\Component\Filesystem\Path::isAbsolute()") and [isRelative()](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Filesystem/Path.php#:~:text=function%20isRelative "Symfony\Component\Filesystem\Path::isRelative()") to check whether a path is absolute or relative:

All four methods internally canonicalize the passed path.

### [Finding Longest Common Base Paths](https://symfony.com/doc/8.0/components/filesystem.html#finding-longest-common-base-paths "Permalink to this headline")

When you store absolute file paths on the file system, this leads to a lot of duplicated information:

Especially when storing many paths, the amount of duplicated information is noticeable. You can use [getLongestCommonBasePath()](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Filesystem/Path.php#:~:text=function%20getLongestCommonBasePath "Symfony\Component\Filesystem\Path::getLongestCommonBasePath()") to check a list of paths for a common base path:

Use this common base path to shorten the stored paths:

[getLongestCommonBasePath()](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Filesystem/Path.php#:~:text=function%20getLongestCommonBasePath "Symfony\Component\Filesystem\Path::getLongestCommonBasePath()") always returns canonical paths.

Use [isBasePath()](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Filesystem/Path.php#:~:text=function%20isBasePath "Symfony\Component\Filesystem\Path::isBasePath()") to test whether a path is a base path of another path:

### [Finding Directories/Root Directories](https://symfony.com/doc/8.0/components/filesystem.html#finding-directories-root-directories "Permalink to this headline")

PHP offers the function [dirname](https://secure.php.net/manual/en/function.dirname.php "dirname") to obtain the directory path of a file path. This method has a few quirks:

* `dirname()` does not accept backslashes on UNIX
* `dirname("C:/Programs")` returns "C:", not "C:/"
* `dirname("C:/")` returns ".", not "C:/"
* `dirname("C:")` returns ".", not "C:/"
* `dirname("Programs")` returns ".", not ""
* `dirname()` does not canonicalize the result

[getDirectory()](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Filesystem/Path.php#:~:text=function%20getDirectory "Symfony\Component\Filesystem\Path::getDirectory()") fixes these shortcomings:

Additionally, you can use [getRoot()](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Filesystem/Path.php#:~:text=function%20getRoot "Symfony\Component\Filesystem\Path::getRoot()") to obtain the root of a path:

This work, including the code samples, is licensed under a [Creative Commons BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/) license.
