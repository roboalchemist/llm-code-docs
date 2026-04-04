# Source: https://docs.pyinvoke.org/en/stable/api/loader.html

Title: loader — Invoke documentation

URL Source: https://docs.pyinvoke.org/en/stable/api/loader.html

Markdown Content:
_class_ invoke.loader.Loader(_config:Optional[[invoke.config.Config](https://docs.pyinvoke.org/en/stable/api/config.html#invoke.config.Config "invoke.config.Config")]=None_)[¶](https://docs.pyinvoke.org/en/stable/api/loader.html#invoke.loader.Loader "Permalink to this definition")
Abstract class defining how to find/import a session’s base [`Collection`](https://docs.pyinvoke.org/en/stable/api/collection.html#invoke.collection.Collection "invoke.collection.Collection").

New in version 1.0.

 __init__ (_config:Optional[[invoke.config.Config](https://docs.pyinvoke.org/en/stable/api/config.html#invoke.config.Config "invoke.config.Config")]=None_)→[None](https://docs.python.org/2.7/library/constants.html#None "(in Python v2.7)")[¶](https://docs.pyinvoke.org/en/stable/api/loader.html#invoke.loader.Loader.__init__ "Permalink to this definition")
Set up a new loader with some [`Config`](https://docs.pyinvoke.org/en/stable/api/config.html#invoke.config.Config "invoke.config.Config").

Parameters
**config** – An explicit [`Config`](https://docs.pyinvoke.org/en/stable/api/config.html#invoke.config.Config "invoke.config.Config") to use; it is referenced for loading-related config options. Defaults to an anonymous `Config()` if none is given.

find(_name:[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")_)→Optional[_frozen_importlib.ModuleSpec][¶](https://docs.pyinvoke.org/en/stable/api/loader.html#invoke.loader.Loader.find "Permalink to this definition")
Implementation-specific finder method seeking collection `name`.

Must return a ModuleSpec valid for use by [`importlib`](https://docs.python.org/2.7/library/importlib.html#module-importlib "(in Python v2.7)"), which is typically a name string followed by the contents of the 3-tuple returned by `importlib.module_from_spec` (`name`, `loader`, `origin`.)

For a sample implementation, see [`FilesystemLoader`](https://docs.pyinvoke.org/en/stable/api/loader.html#invoke.loader.FilesystemLoader "invoke.loader.FilesystemLoader").

New in version 1.0.

load(_name:Optional[[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")]=None_)→Tuple[module,[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")][¶](https://docs.pyinvoke.org/en/stable/api/loader.html#invoke.loader.Loader.load "Permalink to this definition")
Load and return collection module identified by `name`.

This method requires a working implementation of [`find`](https://docs.pyinvoke.org/en/stable/api/loader.html#invoke.loader.Loader.find "invoke.loader.Loader.find") in order to function.

In addition to importing the named module, it will add the module’s parent directory to the front of [`sys.path`](https://docs.python.org/2.7/library/sys.html#sys.path "(in Python v2.7)") to provide normal Python import behavior (i.e. so the loaded module may load local-to-it modules or packages.)

Returns
Two-tuple of `(module, directory)` where `module` is the collection-containing Python module object, and `directory` is the string path to the directory the module was found in.

New in version 1.0.

_class_ invoke.loader.FilesystemLoader(_start:Optional[[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")]=None_, _**kwargs:Any_)[¶](https://docs.pyinvoke.org/en/stable/api/loader.html#invoke.loader.FilesystemLoader "Permalink to this definition")
Loads Python files from the filesystem (e.g. `tasks.py`.)

Searches recursively towards filesystem root from a given start point.

New in version 1.0.

 __init__ (_start:Optional[[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")]=None_, _**kwargs:Any_)→[None](https://docs.python.org/2.7/library/constants.html#None "(in Python v2.7)")[¶](https://docs.pyinvoke.org/en/stable/api/loader.html#invoke.loader.FilesystemLoader.__init__ "Permalink to this definition")
Set up a new loader with some [`Config`](https://docs.pyinvoke.org/en/stable/api/config.html#invoke.config.Config "invoke.config.Config").

Parameters
**config** – An explicit [`Config`](https://docs.pyinvoke.org/en/stable/api/config.html#invoke.config.Config "invoke.config.Config") to use; it is referenced for loading-related config options. Defaults to an anonymous `Config()` if none is given.

find(_name:[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")_)→Optional[_frozen_importlib.ModuleSpec][¶](https://docs.pyinvoke.org/en/stable/api/loader.html#invoke.loader.FilesystemLoader.find "Permalink to this definition")
Implementation-specific finder method seeking collection `name`.

Must return a ModuleSpec valid for use by [`importlib`](https://docs.python.org/2.7/library/importlib.html#module-importlib "(in Python v2.7)"), which is typically a name string followed by the contents of the 3-tuple returned by `importlib.module_from_spec` (`name`, `loader`, `origin`.)

For a sample implementation, see [`FilesystemLoader`](https://docs.pyinvoke.org/en/stable/api/loader.html#invoke.loader.FilesystemLoader "invoke.loader.FilesystemLoader").

New in version 1.0.
