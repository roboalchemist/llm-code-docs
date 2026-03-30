# Source: https://docs.pyinvoke.org/en/stable/api/config.html

Title: config — Invoke documentation

URL Source: https://docs.pyinvoke.org/en/stable/api/config.html

Markdown Content:
_exception_ invoke.config.AmbiguousMergeError[¶](https://docs.pyinvoke.org/en/stable/api/config.html#invoke.config.AmbiguousMergeError "Permalink to this definition") __weakref__ [¶](https://docs.pyinvoke.org/en/stable/api/config.html#invoke.config.AmbiguousMergeError.__weakref__ "Permalink to this definition")
list of weak references to the object (if defined)

_class_ invoke.config.Config(_overrides:Optional[Dict[[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)"),Any]]=None_, _defaults:Optional[Dict[[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)"),Any]]=None_, _system\_prefix:Optional[[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")]=None_, _user\_prefix:Optional[[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")]=None_, _project\_location:Optional[os.PathLike]=None_, _runtime\_path:Optional[os.PathLike]=None_, _lazy:[bool](https://docs.python.org/2.7/library/functions.html#bool "(in Python v2.7)")=False_)[¶](https://docs.pyinvoke.org/en/stable/api/config.html#invoke.config.Config "Permalink to this definition")
Invoke’s primary configuration handling class.

See [Configuration](https://docs.pyinvoke.org/en/stable/concepts/configuration.html) for details on the configuration system this class implements, including the [configuration hierarchy](https://docs.pyinvoke.org/en/stable/concepts/configuration.html#config-hierarchy). The rest of this class’ documentation assumes familiarity with that document.

**Access**

Configuration values may be accessed and/or updated using dict syntax:

config['foo']

or attribute syntax:

config.foo

Nesting works the same way - dict config values are turned into objects which honor both the dictionary protocol and the attribute-access method:

config['foo']['bar']
config.foo.bar

**A note about attribute access and methods**

This class implements the entire dictionary protocol: methods such as `keys`, `values`, `items`, `pop` and so forth should all function as they do on regular dicts. It also implements new config-specific methods such as [`load_system`](https://docs.pyinvoke.org/en/stable/api/config.html#invoke.config.Config.load_system "invoke.config.Config.load_system"), [`load_collection`](https://docs.pyinvoke.org/en/stable/api/config.html#invoke.config.Config.load_collection "invoke.config.Config.load_collection"), [`merge`](https://docs.pyinvoke.org/en/stable/api/config.html#invoke.config.Config.merge "invoke.config.Config.merge"), [`clone`](https://docs.pyinvoke.org/en/stable/api/config.html#invoke.config.Config.clone "invoke.config.Config.clone"), etc.

Warning

Accordingly, this means that if you have configuration options sharing names with these methods, you **must** use dictionary syntax (e.g. `myconfig['keys']`) to access the configuration data.

**Lifecycle**

At initialization time, [`Config`](https://docs.pyinvoke.org/en/stable/api/config.html#invoke.config.Config "invoke.config.Config"):

*   creates per-level data structures;

*   stores any levels supplied to [`__init__`](https://docs.pyinvoke.org/en/stable/api/config.html#invoke.config.Config.__init__ "invoke.config.Config.__init__"), such as defaults or overrides, as well as the various config file paths/filename patterns;

*   and loads config files, if found (though typically this just means system and user-level files, as project and runtime files need more info before they can be found and loaded.)

> *   This step can be skipped by specifying `lazy=True`.

At this point, [`Config`](https://docs.pyinvoke.org/en/stable/api/config.html#invoke.config.Config "invoke.config.Config") is fully usable - and because it pre-emptively loads some config files, those config files can affect anything that comes after, like CLI parsing or loading of task collections.

In the CLI use case, further processing is done after instantiation, using the `load_*` methods such as [`load_overrides`](https://docs.pyinvoke.org/en/stable/api/config.html#invoke.config.Config.load_overrides "invoke.config.Config.load_overrides"), [`load_project`](https://docs.pyinvoke.org/en/stable/api/config.html#invoke.config.Config.load_project "invoke.config.Config.load_project"), etc:

*   the result of argument/option parsing is applied to the overrides level;

*   a project-level config file is loaded, as it’s dependent on a loaded tasks collection;

*   a runtime config file is loaded, if its flag was supplied;

*   then, for each task being executed:

> *   per-collection data is loaded (only possible now that we have collection & task in hand);
> 
>     *   shell environment data is loaded (must be done at end of process due to using the rest of the config as a guide for interpreting env var names.)

At this point, the config object is handed to the task being executed, as part of its execution [`Context`](https://docs.pyinvoke.org/en/stable/api/context.html#invoke.context.Context "invoke.context.Context").

Any modifications made directly to the [`Config`](https://docs.pyinvoke.org/en/stable/api/config.html#invoke.config.Config "invoke.config.Config") itself after this point end up stored in their own (topmost) config level, making it easier to debug final values.

Finally, any _deletions_ made to the [`Config`](https://docs.pyinvoke.org/en/stable/api/config.html#invoke.config.Config "invoke.config.Config") (e.g. applications of dict-style mutators like `pop`, `clear` etc) are also tracked in their own structure, allowing the config object to honor such method calls without mutating the underlying source data.

**Special class attributes**

The following class-level attributes are used for low-level configuration of the config system itself, such as which file paths to load. They are primarily intended for overriding by subclasses.

*   `prefix`: Supplies the default value for `file_prefix` (directly) and `env_prefix` (uppercased). See their descriptions for details. Its default value is `"invoke"`.

*   `file_prefix`: The config file ‘basename’ default (though it is not a literal basename; it can contain path parts if desired) which is appended to the configured values of `system_prefix`, `user_prefix`, etc, to arrive at the final (pre-extension) file paths.

Thus, by default, a system-level config file path concatenates the `system_prefix` of `/etc/` with the `file_prefix` of `invoke` to arrive at paths like `/etc/invoke.json`.

Defaults to `None`, meaning to use the value of `prefix`.

*   `env_prefix`: A prefix used (along with a joining underscore) to determine which environment variables are loaded as the env var configuration level. Since its default is the value of `prefix` capitalized, this means env vars like `INVOKE_RUN_ECHO` are sought by default.

Defaults to `None`, meaning to use the value of `prefix`.

New in version 1.0.

 __init__ (_overrides:Optional[Dict[[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)"),Any]]=None_, _defaults:Optional[Dict[[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)"),Any]]=None_, _system\_prefix:Optional[[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")]=None_, _user\_prefix:Optional[[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")]=None_, _project\_location:Optional[os.PathLike]=None_, _runtime\_path:Optional[os.PathLike]=None_, _lazy:[bool](https://docs.python.org/2.7/library/functions.html#bool "(in Python v2.7)")=False_)[¶](https://docs.pyinvoke.org/en/stable/api/config.html#invoke.config.Config.__init__ "Permalink to this definition")
Creates a new config object.

Parameters
*   **defaults** ([_dict_](https://docs.python.org/2.7/library/stdtypes.html#dict "(in Python v2.7)")) – A dict containing default (lowest level) config data. Default: [`global_defaults`](https://docs.pyinvoke.org/en/stable/api/config.html#invoke.config.Config.global_defaults "invoke.config.Config.global_defaults").

*   **overrides** ([_dict_](https://docs.python.org/2.7/library/stdtypes.html#dict "(in Python v2.7)")) – A dict containing override-level config data. Default: `{}`.

*   **system_prefix** ([_str_](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")) –

Base path for the global config file location; combined with the prefix and file suffixes to arrive at final file path candidates.

Default: `/etc/` (thus e.g. `/etc/invoke.yaml` or `/etc/invoke.json`).

*   **user_prefix** ([_str_](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")) –

Like `system_prefix` but for the per-user config file. These variables are joined as strings, not via path-style joins, so they may contain partial file paths; for the per-user config file this often means a leading dot, to make the final result a hidden file on most systems.

Default: `~/.` (e.g. `~/.invoke.yaml`).

*   **project_location** ([_str_](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")) – Optional directory path of the currently loaded [`Collection`](https://docs.pyinvoke.org/en/stable/api/collection.html#invoke.collection.Collection "invoke.collection.Collection") (as loaded by [`Loader`](https://docs.pyinvoke.org/en/stable/api/loader.html#invoke.loader.Loader "invoke.loader.Loader")). When non-empty, will trigger seeking of per-project config files in this directory.

*   **runtime_path** ([_str_](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")) –

Optional file path to a runtime configuration file.

Used to fill the penultimate slot in the config hierarchy. Should be a full file path to an existing file, not a directory path or a prefix.

*   **lazy** ([_bool_](https://docs.python.org/2.7/library/functions.html#bool "(in Python v2.7)")) –

Whether to automatically load some of the lower config levels.

By default (`lazy=False`), `__init__` automatically calls [`load_system`](https://docs.pyinvoke.org/en/stable/api/config.html#invoke.config.Config.load_system "invoke.config.Config.load_system") and [`load_user`](https://docs.pyinvoke.org/en/stable/api/config.html#invoke.config.Config.load_user "invoke.config.Config.load_user") to load system and user config files, respectively.

For more control over what is loaded when, you can say `lazy=True`, and no automatic loading is done.

Note

If you give `defaults` and/or `overrides` as `__init__` kwargs instead of waiting to use [`load_defaults`](https://docs.pyinvoke.org/en/stable/api/config.html#invoke.config.Config.load_defaults "invoke.config.Config.load_defaults") or [`load_overrides`](https://docs.pyinvoke.org/en/stable/api/config.html#invoke.config.Config.load_overrides "invoke.config.Config.load_overrides") afterwards, those _will_ still end up ‘loaded’ immediately. 

clone(_into:Optional[Type[[invoke.config.Config](https://docs.pyinvoke.org/en/stable/api/config.html#invoke.config.Config "invoke.config.Config")]]=None_)→[invoke.config.Config](https://docs.pyinvoke.org/en/stable/api/config.html#invoke.config.Config "invoke.config.Config")[¶](https://docs.pyinvoke.org/en/stable/api/config.html#invoke.config.Config.clone "Permalink to this definition")
Return a copy of this configuration object.

The new object will be identical in terms of configured sources and any loaded (or user-manipulated) data, but will be a distinct object with as little shared mutable state as possible.

Specifically, all [`dict`](https://docs.python.org/2.7/library/stdtypes.html#dict "(in Python v2.7)") values within the config are recursively recreated, with non-dict leaf values subjected to [`copy.copy`](https://docs.python.org/2.7/library/copy.html#copy.copy "(in Python v2.7)") (note: _not_[`copy.deepcopy`](https://docs.python.org/2.7/library/copy.html#copy.deepcopy "(in Python v2.7)"), as this can cause issues with various objects such as compiled regexen or threading locks, often found buried deep within rich aggregates like API or DB clients).

The only remaining config values that may end up shared between a config and its clone are thus those ‘rich’ objects that do not [`copy.copy`](https://docs.python.org/2.7/library/copy.html#copy.copy "(in Python v2.7)") cleanly, or compound non-dict objects (such as lists or tuples).

Parameters
**into** –

A [`Config`](https://docs.pyinvoke.org/en/stable/api/config.html#invoke.config.Config "invoke.config.Config") subclass that the new clone should be “upgraded” to.

Used by client libraries which have their own [`Config`](https://docs.pyinvoke.org/en/stable/api/config.html#invoke.config.Config "invoke.config.Config") subclasses that e.g. define additional defaults; cloning “into” one of these subclasses ensures that any new keys/subtrees are added gracefully, without overwriting anything that may have been pre-defined.

Default: `None` (just clone into another regular [`Config`](https://docs.pyinvoke.org/en/stable/api/config.html#invoke.config.Config "invoke.config.Config")).

Returns
A [`Config`](https://docs.pyinvoke.org/en/stable/api/config.html#invoke.config.Config "invoke.config.Config"), or an instance of the class given to `into`.

New in version 1.0.

_static_ global_defaults()→Dict[[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)"),Any][¶](https://docs.pyinvoke.org/en/stable/api/config.html#invoke.config.Config.global_defaults "Permalink to this definition")
Return the core default settings for Invoke.

Generally only for use by [`Config`](https://docs.pyinvoke.org/en/stable/api/config.html#invoke.config.Config "invoke.config.Config") internals. For descriptions of these values, see [Default configuration values](https://docs.pyinvoke.org/en/stable/concepts/configuration.html#default-values).

Subclasses may choose to override this method, calling `Config.global_defaults` and applying [`merge_dicts`](https://docs.pyinvoke.org/en/stable/api/config.html#invoke.config.merge_dicts "invoke.config.merge_dicts") to the result, to add to or modify these values.

New in version 1.0.

load_collection(_data:Dict[[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)"),Any]_, _merge:[bool](https://docs.python.org/2.7/library/functions.html#bool "(in Python v2.7)")=True_)→[None](https://docs.python.org/2.7/library/constants.html#None "(in Python v2.7)")[¶](https://docs.pyinvoke.org/en/stable/api/config.html#invoke.config.Config.load_collection "Permalink to this definition")
Update collection-driven config data.

[`load_collection`](https://docs.pyinvoke.org/en/stable/api/config.html#invoke.config.Config.load_collection "invoke.config.Config.load_collection") is intended for use by the core task execution machinery, which is responsible for obtaining collection-driven data. See [Collection-based configuration](https://docs.pyinvoke.org/en/stable/concepts/configuration.html#collection-configuration) for details.

New in version 1.0.

load_defaults(_data:Dict[[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)"),Any]_, _merge:[bool](https://docs.python.org/2.7/library/functions.html#bool "(in Python v2.7)")=True_)→[None](https://docs.python.org/2.7/library/constants.html#None "(in Python v2.7)")[¶](https://docs.pyinvoke.org/en/stable/api/config.html#invoke.config.Config.load_defaults "Permalink to this definition")
Set or replace the ‘defaults’ configuration level, from `data`.

Parameters
*   **data** ([_dict_](https://docs.python.org/2.7/library/stdtypes.html#dict "(in Python v2.7)")) – The config data to load as the defaults level.

*   **merge** ([_bool_](https://docs.python.org/2.7/library/functions.html#bool "(in Python v2.7)")) – Whether to merge the loaded data into the central config. Default: `True`.

Returns
`None`.

New in version 1.0.

load_overrides(_data:Dict[[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)"),Any]_, _merge:[bool](https://docs.python.org/2.7/library/functions.html#bool "(in Python v2.7)")=True_)→[None](https://docs.python.org/2.7/library/constants.html#None "(in Python v2.7)")[¶](https://docs.pyinvoke.org/en/stable/api/config.html#invoke.config.Config.load_overrides "Permalink to this definition")
Set or replace the ‘overrides’ configuration level, from `data`.

Parameters
*   **data** ([_dict_](https://docs.python.org/2.7/library/stdtypes.html#dict "(in Python v2.7)")) – The config data to load as the overrides level.

*   **merge** ([_bool_](https://docs.python.org/2.7/library/functions.html#bool "(in Python v2.7)")) – Whether to merge the loaded data into the central config. Default: `True`.

Returns
`None`.

New in version 1.0.

load_project(_merge:[bool](https://docs.python.org/2.7/library/functions.html#bool "(in Python v2.7)")=True_)→[None](https://docs.python.org/2.7/library/constants.html#None "(in Python v2.7)")[¶](https://docs.pyinvoke.org/en/stable/api/config.html#invoke.config.Config.load_project "Permalink to this definition")
Load a project-level config file, if possible.

Checks the configured `_project_prefix` value derived from the path given to [`set_project_location`](https://docs.pyinvoke.org/en/stable/api/config.html#invoke.config.Config.set_project_location "invoke.config.Config.set_project_location"), which is typically set to the directory containing the loaded task collection.

Thus, if one were to run the CLI tool against a tasks collection `/home/myuser/code/tasks.py`, [`load_project`](https://docs.pyinvoke.org/en/stable/api/config.html#invoke.config.Config.load_project "invoke.config.Config.load_project") would seek out files like `/home/myuser/code/invoke.yml`.

Parameters
**merge** ([_bool_](https://docs.python.org/2.7/library/functions.html#bool "(in Python v2.7)")) – Whether to merge the loaded data into the central config. Default: `True`.

Returns
`None`.

New in version 1.0.

load_runtime(_merge:[bool](https://docs.python.org/2.7/library/functions.html#bool "(in Python v2.7)")=True_)→[None](https://docs.python.org/2.7/library/constants.html#None "(in Python v2.7)")[¶](https://docs.pyinvoke.org/en/stable/api/config.html#invoke.config.Config.load_runtime "Permalink to this definition")
Load a runtime-level config file, if one was specified.

When the CLI framework creates a [`Config`](https://docs.pyinvoke.org/en/stable/api/config.html#invoke.config.Config "invoke.config.Config"), it sets `_runtime_path`, which is a full path to the requested config file. This method attempts to load that file.

Parameters
**merge** ([_bool_](https://docs.python.org/2.7/library/functions.html#bool "(in Python v2.7)")) – Whether to merge the loaded data into the central config. Default: `True`.

Returns
`None`.

New in version 1.0.

load_shell_env()→[None](https://docs.python.org/2.7/library/constants.html#None "(in Python v2.7)")[¶](https://docs.pyinvoke.org/en/stable/api/config.html#invoke.config.Config.load_shell_env "Permalink to this definition")
Load values from the shell environment.

[`load_shell_env`](https://docs.pyinvoke.org/en/stable/api/config.html#invoke.config.Config.load_shell_env "invoke.config.Config.load_shell_env") is intended for execution late in a [`Config`](https://docs.pyinvoke.org/en/stable/api/config.html#invoke.config.Config "invoke.config.Config") object’s lifecycle, once all other sources (such as a runtime config file or per-collection configurations) have been loaded. Loading from the shell is not terrifically expensive, but must be done at a specific point in time to ensure the “only known config keys are loaded from the env” behavior works correctly.

See [Environment variables](https://docs.pyinvoke.org/en/stable/concepts/configuration.html#env-vars) for details on this design decision and other info re: how environment variables are scanned and loaded.

New in version 1.0.

load_system(_merge:[bool](https://docs.python.org/2.7/library/functions.html#bool "(in Python v2.7)")=True_)→[None](https://docs.python.org/2.7/library/constants.html#None "(in Python v2.7)")[¶](https://docs.pyinvoke.org/en/stable/api/config.html#invoke.config.Config.load_system "Permalink to this definition")
Load a system-level config file, if possible.

Checks the configured `_system_prefix` path, which defaults to `/etc`, and will thus load files like `/etc/invoke.yml`.

Parameters
**merge** ([_bool_](https://docs.python.org/2.7/library/functions.html#bool "(in Python v2.7)")) – Whether to merge the loaded data into the central config. Default: `True`.

Returns
`None`.

New in version 1.0.

load_user(_merge:[bool](https://docs.python.org/2.7/library/functions.html#bool "(in Python v2.7)")=True_)→[None](https://docs.python.org/2.7/library/constants.html#None "(in Python v2.7)")[¶](https://docs.pyinvoke.org/en/stable/api/config.html#invoke.config.Config.load_user "Permalink to this definition")
Load a user-level config file, if possible.

Checks the configured `_user_prefix` path, which defaults to `~/.`, and will thus load files like `~/.invoke.yml`.

Parameters
**merge** ([_bool_](https://docs.python.org/2.7/library/functions.html#bool "(in Python v2.7)")) – Whether to merge the loaded data into the central config. Default: `True`.

Returns
`None`.

New in version 1.0.

merge()→[None](https://docs.python.org/2.7/library/constants.html#None "(in Python v2.7)")[¶](https://docs.pyinvoke.org/en/stable/api/config.html#invoke.config.Config.merge "Permalink to this definition")
Merge all config sources, in order.

New in version 1.0.

set_project_location(_path:Optional[Union[os.PathLike,[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")]]_)→[None](https://docs.python.org/2.7/library/constants.html#None "(in Python v2.7)")[¶](https://docs.pyinvoke.org/en/stable/api/config.html#invoke.config.Config.set_project_location "Permalink to this definition")
Set the directory path where a project-level config file may be found.

Does not do any file loading on its own; for that, see [`load_project`](https://docs.pyinvoke.org/en/stable/api/config.html#invoke.config.Config.load_project "invoke.config.Config.load_project").

New in version 1.0.

set_runtime_path(_path:Optional[os.PathLike]_)→[None](https://docs.python.org/2.7/library/constants.html#None "(in Python v2.7)")[¶](https://docs.pyinvoke.org/en/stable/api/config.html#invoke.config.Config.set_runtime_path "Permalink to this definition")
Set the runtime config file path.

New in version 1.0.

_class_ invoke.config.DataProxy[¶](https://docs.pyinvoke.org/en/stable/api/config.html#invoke.config.DataProxy "Permalink to this definition")
Helper class implementing nested dict+attr access for [`Config`](https://docs.pyinvoke.org/en/stable/api/config.html#invoke.config.Config "invoke.config.Config").

Specifically, is used both for [`Config`](https://docs.pyinvoke.org/en/stable/api/config.html#invoke.config.Config "invoke.config.Config") itself, and to wrap any other dicts assigned as config values (recursively).

Warning

All methods (of this object or in subclasses) must take care to initialize new attributes via `self._set(name='value')`, or they’ll run into recursion errors!

New in version 1.0.

 __delattr__ (_name:[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")_)→[None](https://docs.python.org/2.7/library/constants.html#None "(in Python v2.7)")[¶](https://docs.pyinvoke.org/en/stable/api/config.html#invoke.config.DataProxy.__delattr__ "Permalink to this definition")
Implement delattr(self, name).

 __eq__ (_other:[object](https://docs.python.org/2.7/library/functions.html#object "(in Python v2.7)")_)→[bool](https://docs.python.org/2.7/library/functions.html#bool "(in Python v2.7)")[¶](https://docs.pyinvoke.org/en/stable/api/config.html#invoke.config.DataProxy.__eq__ "Permalink to this definition")
Return self==value.

 __hash__ _=None_[¶](https://docs.pyinvoke.org/en/stable/api/config.html#invoke.config.DataProxy.__hash__ "Permalink to this definition") __repr__ ()→[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")[¶](https://docs.pyinvoke.org/en/stable/api/config.html#invoke.config.DataProxy.__repr__ "Permalink to this definition")
Return repr(self).

 __setattr__ (_key:[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")_, _value:Any_)→[None](https://docs.python.org/2.7/library/constants.html#None "(in Python v2.7)")[¶](https://docs.pyinvoke.org/en/stable/api/config.html#invoke.config.DataProxy.__setattr__ "Permalink to this definition")
Implement setattr(self, name, value).

 __weakref__ [¶](https://docs.pyinvoke.org/en/stable/api/config.html#invoke.config.DataProxy.__weakref__ "Permalink to this definition")
list of weak references to the object (if defined)

_classmethod_ from_data(_data:Dict[[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)"),Any]_, _root:Optional[[invoke.config.DataProxy](https://docs.pyinvoke.org/en/stable/api/config.html#invoke.config.DataProxy "invoke.config.DataProxy")]=None_, _keypath:Tuple[[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)"),...]=()_)→[invoke.config.DataProxy](https://docs.pyinvoke.org/en/stable/api/config.html#invoke.config.DataProxy "invoke.config.DataProxy")[¶](https://docs.pyinvoke.org/en/stable/api/config.html#invoke.config.DataProxy.from_data "Permalink to this definition")
Alternate constructor for ‘baby’ DataProxies used as sub-dict values.

Allows creating standalone DataProxy objects while also letting subclasses like [`Config`](https://docs.pyinvoke.org/en/stable/api/config.html#invoke.config.Config "invoke.config.Config") define their own `__init__` without muddling the two.

Parameters
*   **data** ([_dict_](https://docs.python.org/2.7/library/stdtypes.html#dict "(in Python v2.7)")) – This particular DataProxy’s personal data. Required, it’s the Data being Proxied.

*   **root** – Optional handle on a root DataProxy/Config which needs notification on data updates.

*   **keypath** (_tuple_) – Optional tuple describing the path of keys leading to this DataProxy’s location inside the `root` structure. Required if `root` was given (and vice versa.)

New in version 1.0.

invoke.config.copy_dict(_source:Dict[[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)"),Any]_)→Dict[[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)"),Any][¶](https://docs.pyinvoke.org/en/stable/api/config.html#invoke.config.copy_dict "Permalink to this definition")
Return a fresh copy of `source` with as little shared state as possible.

Uses [`merge_dicts`](https://docs.pyinvoke.org/en/stable/api/config.html#invoke.config.merge_dicts "invoke.config.merge_dicts") under the hood, with an empty `base` dict; see its documentation for details on behavior.

New in version 1.0.

invoke.config.excise(_dict\_:Dict[[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)"),Any]_, _keypath:Tuple[[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)"),...]_)→[None](https://docs.python.org/2.7/library/constants.html#None "(in Python v2.7)")[¶](https://docs.pyinvoke.org/en/stable/api/config.html#invoke.config.excise "Permalink to this definition")
Remove key pointed at by `keypath` from nested dict `dict_`, if exists.

New in version 1.0.

invoke.config.merge_dicts(_base:Dict[[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)"),Any]_, _updates:Dict[[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)"),Any]_)→Dict[[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)"),Any][¶](https://docs.pyinvoke.org/en/stable/api/config.html#invoke.config.merge_dicts "Permalink to this definition")
Recursively merge dict `updates` into dict `base` (mutating `base`.)

*   Values which are themselves dicts will be recursed into.

*   Values which are a dict in one input and _not_ a dict in the other input (e.g. if our inputs were `{'foo': 5}` and `{'foo': {'bar': 5}}`) are irreconciliable and will generate an exception.

*   Non-dict leaf values are run through [`copy.copy`](https://docs.python.org/2.7/library/copy.html#copy.copy "(in Python v2.7)") to avoid state bleed.

Note

This is effectively a lightweight [`copy.deepcopy`](https://docs.python.org/2.7/library/copy.html#copy.deepcopy "(in Python v2.7)") which offers protection from mismatched types (dict vs non-dict) and avoids some core deepcopy problems (such as how it explodes on certain object types).

Returns
The value of `base`, which is mostly useful for wrapper functions like [`copy_dict`](https://docs.pyinvoke.org/en/stable/api/config.html#invoke.config.copy_dict "invoke.config.copy_dict").

New in version 1.0.

invoke.config.obliterate(_base:Dict[[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)"),Any]_, _deletions:Dict[[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)"),Any]_)→[None](https://docs.python.org/2.7/library/constants.html#None "(in Python v2.7)")[¶](https://docs.pyinvoke.org/en/stable/api/config.html#invoke.config.obliterate "Permalink to this definition")
Remove all (nested) keys mentioned in `deletions`, from `base`.

New in version 1.0.
