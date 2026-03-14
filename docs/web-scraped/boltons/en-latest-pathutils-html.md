# Source: https://boltons.readthedocs.io/en/latest/pathutils.html

Title: Filesystem fun — boltons 25.0.0 documentation

URL Source: https://boltons.readthedocs.io/en/latest/pathutils.html

Markdown Content:
`pathutils` - Filesystem fun[](https://boltons.readthedocs.io/en/latest/pathutils.html#module-boltons.pathutils "Link to this heading")
----------------------------------------------------------------------------------------------------------------------------------------

Functions for working with filesystem paths.

The [`expandpath()`](https://boltons.readthedocs.io/en/latest/pathutils.html#boltons.pathutils.expandpath "boltons.pathutils.expandpath") function expands the tilde to $HOME and environment variables to their values.

The [`augpath()`](https://boltons.readthedocs.io/en/latest/pathutils.html#boltons.pathutils.augpath "boltons.pathutils.augpath") function creates variants of an existing path without having to spend multiple lines of code splitting it up and stitching it back together.

The [`shrinkuser()`](https://boltons.readthedocs.io/en/latest/pathutils.html#boltons.pathutils.shrinkuser "boltons.pathutils.shrinkuser") function replaces your home directory with a tilde.

boltons.pathutils.augpath(_path_, _suffix=''_, _prefix=''_, _ext=None_, _base=None_, _dpath=None_, _multidot=False_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/pathutils.html#augpath)[](https://boltons.readthedocs.io/en/latest/pathutils.html#boltons.pathutils.augpath "Link to this definition")
Augment a path by modifying its components.

Creates a new path with a different extension, basename, directory, prefix, and/or suffix.

A prefix is inserted before the basename. A suffix is inserted between the basename and the extension. The basename and extension can be replaced with a new one. Essentially a path is broken down into components (dpath, base, ext), and then recombined as (dpath, prefix, base, suffix, ext) after replacing any specified component.

Parameters:
*   **path** ([_str_](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")_|_ _PathLike_) – a path to augment

*   **suffix** ([_str_](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")_,_ _default=''_) – placed between the basename and extension

*   **prefix** ([_str_](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")_,_ _default=''_) – placed in front of the basename

*   **ext** ([_str_](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")_,_ _default=None_) – if specified, replaces the extension

*   **base** ([_str_](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")_,_ _default=None_) – if specified, replaces the basename without extension

*   **dpath** ([_str_](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")_|_ _PathLike_ _,_ _default=None_) – if specified, replaces the directory

*   **multidot** ([_bool_](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")_,_ _default=False_) – Allows extensions to contain multiple dots. Specifically, if False, everything after the last dot in the basename is the extension. If True, everything after the first dot in the basename is the extension.

Returns:
augmented path

Return type:
[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")

Example

>>> path = 'foo.bar'
>>> suffix = '_suff'
>>> prefix = 'pref_'
>>> ext = '.baz'
>>> newpath = augpath(path, suffix, prefix, ext=ext, base='bar')
>>> print('newpath = %s' % (newpath,))
newpath = pref_bar_suff.baz

Example

>>> augpath('foo.bar')
'foo.bar'
>>> augpath('foo.bar', ext='.BAZ')
'foo.BAZ'
>>> augpath('foo.bar', suffix='_')
'foo_.bar'
>>> augpath('foo.bar', prefix='_')
'_foo.bar'
>>> augpath('foo.bar', base='baz')
'baz.bar'
>>> augpath('foo.tar.gz', ext='.zip', multidot=True)
'foo.zip'
>>> augpath('foo.tar.gz', ext='.zip', multidot=False)
'foo.tar.zip'
>>> augpath('foo.tar.gz', suffix='_new', multidot=True)
'foo_new.tar.gz'

boltons.pathutils.expandpath(_path_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/pathutils.html#expandpath)[](https://boltons.readthedocs.io/en/latest/pathutils.html#boltons.pathutils.expandpath "Link to this definition")
Shell-like expansion of environment variables and tilde home directory.

Parameters:
**path** ([_str_](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")_|_ _PathLike_) – the path to expand

Returns:
expanded path

Return type:
[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")

Example

>>> import os
>>> os.environ['SPAM'] = 'eggs'
>>> assert expandpath('~/$SPAM') == expanduser('~/eggs')
>>> assert expandpath('foo') == 'foo'

boltons.pathutils.shrinkuser(_path_, _home='~'_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/pathutils.html#shrinkuser)[](https://boltons.readthedocs.io/en/latest/pathutils.html#boltons.pathutils.shrinkuser "Link to this definition")
Inverse of [`os.path.expanduser()`](https://docs.python.org/3/library/os.path.html#os.path.expanduser "(in Python v3.14)").

Parameters:
*   **path** ([_str_](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")_|_ _PathLike_) – path in system file structure

*   **home** ([_str_](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")_,_ _default='~'_) – symbol used to replace the home path. Defaults to ‘~’, but you might want to use ‘$HOME’ or ‘%USERPROFILE%’ instead.

Returns:
path: shortened path replacing the home directory with a tilde

Return type:
[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")

Example

>>> path = expanduser('~')
>>> assert path != '~'
>>> assert shrinkuser(path) == '~'
>>> assert shrinkuser(path + '1') == path + '1'
>>> assert shrinkuser(path + '/1') == join('~', '1')
>>> assert shrinkuser(path + '/1', '$HOME') == join('$HOME', '1')
