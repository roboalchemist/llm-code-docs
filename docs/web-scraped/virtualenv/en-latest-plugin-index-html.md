# Source: https://virtualenv.pypa.io/en/latest/plugin/index.html

Title: Plugins - virtualenv

URL Source: https://virtualenv.pypa.io/en/latest/plugin/index.html

Markdown Content:
virtualenv can be extended via plugins using Python entry points. Plugins are automatically discovered from the Python environment where virtualenv is installed, allowing you to customize how virtual environments are created, seeded, and activated.

Extension points[¶](https://virtualenv.pypa.io/en/latest/plugin/index.html#extension-points "Link to this heading")
-------------------------------------------------------------------------------------------------------------------

virtualenv provides four extension points through entry point groups:

`virtualenv.discovery`
Python interpreter discovery plugins. These plugins locate and identify Python interpreters that will be used as the base for creating virtual environments.

`virtualenv.create`
Virtual environment creator plugins. These plugins handle the actual creation of the virtual environment structure, including copying or symlinking the Python interpreter and standard library.

`virtualenv.seed`
Seed package installer plugins. These plugins install initial packages (like pip, setuptools, wheel) into newly created virtual environments.

`virtualenv.activate`
Shell activation script plugins. These plugins generate shell-specific activation scripts that modify the environment to use the virtual environment.

All extension points follow a common pattern: virtualenv discovers registered entry points, builds CLI options from them, and executes the selected implementations during environment creation.

* [Your first plugin](https://virtualenv.pypa.io/en/latest/plugin/tutorial.html)
  * [Create the package structure](https://virtualenv.pypa.io/en/latest/plugin/tutorial.html#create-the-package-structure)
  * [Configure the entry point](https://virtualenv.pypa.io/en/latest/plugin/tutorial.html#configure-the-entry-point)
  * [Implement the plugin](https://virtualenv.pypa.io/en/latest/plugin/tutorial.html#implement-the-plugin)
  * [Install the plugin](https://virtualenv.pypa.io/en/latest/plugin/tutorial.html#install-the-plugin)
  * [Verify the plugin](https://virtualenv.pypa.io/en/latest/plugin/tutorial.html#verify-the-plugin)

* [Plugin how-to guides](https://virtualenv.pypa.io/en/latest/plugin/how-to.html)
  * [Create a discovery plugin](https://virtualenv.pypa.io/en/latest/plugin/how-to.html#create-a-discovery-plugin)
  * [Create a creator plugin](https://virtualenv.pypa.io/en/latest/plugin/how-to.html#create-a-creator-plugin)
  * [Create a seeder plugin](https://virtualenv.pypa.io/en/latest/plugin/how-to.html#create-a-seeder-plugin)
  * [Create an activator plugin](https://virtualenv.pypa.io/en/latest/plugin/how-to.html#create-an-activator-plugin)
  * [Package and distribute a plugin](https://virtualenv.pypa.io/en/latest/plugin/how-to.html#package-and-distribute-a-plugin)

* [Plugin API reference](https://virtualenv.pypa.io/en/latest/plugin/api.html)
  * [Discovery](https://virtualenv.pypa.io/en/latest/plugin/api.html#discovery)
    * [`Discover`](https://virtualenv.pypa.io/en/latest/plugin/api.html#virtualenv.discovery.discover.Discover)
      * [`Discover.add_parser_arguments()`](https://virtualenv.pypa.io/en/latest/plugin/api.html#virtualenv.discovery.discover.Discover.add_parser_arguments)
      * [`Discover.run()`](https://virtualenv.pypa.io/en/latest/plugin/api.html#virtualenv.discovery.discover.Discover.run)
      * [`Discover.interpreter`](https://virtualenv.pypa.io/en/latest/plugin/api.html#virtualenv.discovery.discover.Discover.interpreter)

    * [PythonInfo](https://virtualenv.pypa.io/en/latest/plugin/api.html#pythoninfo)
      * [`PythonInfo`](https://virtualenv.pypa.io/en/latest/plugin/api.html#virtualenv.discovery.py_info.PythonInfo)
        * [`PythonInfo.install_path()`](https://virtualenv.pypa.io/en/latest/plugin/api.html#virtualenv.discovery.py_info.PythonInfo.install_path)
        * [`PythonInfo.version_str`](https://virtualenv.pypa.io/en/latest/plugin/api.html#virtualenv.discovery.py_info.PythonInfo.version_str)
        * [`PythonInfo.version_release_str`](https://virtualenv.pypa.io/en/latest/plugin/api.html#virtualenv.discovery.py_info.PythonInfo.version_release_str)
        * [`PythonInfo.python_name`](https://virtualenv.pypa.io/en/latest/plugin/api.html#virtualenv.discovery.py_info.PythonInfo.python_name)
        * [`PythonInfo.is_old_virtualenv`](https://virtualenv.pypa.io/en/latest/plugin/api.html#virtualenv.discovery.py_info.PythonInfo.is_old_virtualenv)
        * [`PythonInfo.is_venv`](https://virtualenv.pypa.io/en/latest/plugin/api.html#virtualenv.discovery.py_info.PythonInfo.is_venv)
        * [`PythonInfo.sysconfig_path()`](https://virtualenv.pypa.io/en/latest/plugin/api.html#virtualenv.discovery.py_info.PythonInfo.sysconfig_path)
        * [`PythonInfo.system_include`](https://virtualenv.pypa.io/en/latest/plugin/api.html#virtualenv.discovery.py_info.PythonInfo.system_include)
        * [`PythonInfo.system_prefix`](https://virtualenv.pypa.io/en/latest/plugin/api.html#virtualenv.discovery.py_info.PythonInfo.system_prefix)
        * [`PythonInfo.system_exec_prefix`](https://virtualenv.pypa.io/en/latest/plugin/api.html#virtualenv.discovery.py_info.PythonInfo.system_exec_prefix)
        * [`PythonInfo.machine`](https://virtualenv.pypa.io/en/latest/plugin/api.html#virtualenv.discovery.py_info.PythonInfo.machine)
        * [`PythonInfo.spec`](https://virtualenv.pypa.io/en/latest/plugin/api.html#virtualenv.discovery.py_info.PythonInfo.spec)
        * [`PythonInfo.clear_cache()`](https://virtualenv.pypa.io/en/latest/plugin/api.html#virtualenv.discovery.py_info.PythonInfo.clear_cache)
        * [`PythonInfo.satisfies()`](https://virtualenv.pypa.io/en/latest/plugin/api.html#virtualenv.discovery.py_info.PythonInfo.satisfies)
        * [`PythonInfo.current()`](https://virtualenv.pypa.io/en/latest/plugin/api.html#virtualenv.discovery.py_info.PythonInfo.current)
        * [`PythonInfo.current_system()`](https://virtualenv.pypa.io/en/latest/plugin/api.html#virtualenv.discovery.py_info.PythonInfo.current_system)
        * [`PythonInfo.to_json()`](https://virtualenv.pypa.io/en/latest/plugin/api.html#virtualenv.discovery.py_info.PythonInfo.to_json)
        * [`PythonInfo.to_dict()`](https://virtualenv.pypa.io/en/latest/plugin/api.html#virtualenv.discovery.py_info.PythonInfo.to_dict)
        * [`PythonInfo.from_exe()`](https://virtualenv.pypa.io/en/latest/plugin/api.html#virtualenv.discovery.py_info.PythonInfo.from_exe)
        * [`PythonInfo.from_json()`](https://virtualenv.pypa.io/en/latest/plugin/api.html#virtualenv.discovery.py_info.PythonInfo.from_json)
        * [`PythonInfo.from_dict()`](https://virtualenv.pypa.io/en/latest/plugin/api.html#virtualenv.discovery.py_info.PythonInfo.from_dict)
        * [`PythonInfo.resolve_to_system()`](https://virtualenv.pypa.io/en/latest/plugin/api.html#virtualenv.discovery.py_info.PythonInfo.resolve_to_system)
        * [`PythonInfo.discover_exe()`](https://virtualenv.pypa.io/en/latest/plugin/api.html#virtualenv.discovery.py_info.PythonInfo.discover_exe)

  * [App data](https://virtualenv.pypa.io/en/latest/plugin/api.html#app-data)
    * [`AppData`](https://virtualenv.pypa.io/en/latest/plugin/api.html#virtualenv.app_data.base.AppData)
      * [`AppData.close()`](https://virtualenv.pypa.io/en/latest/plugin/api.html#virtualenv.app_data.base.AppData.close)
      * [`AppData.reset()`](https://virtualenv.pypa.io/en/latest/plugin/api.html#virtualenv.app_data.base.AppData.reset)
      * [`AppData.py_info()`](https://virtualenv.pypa.io/en/latest/plugin/api.html#virtualenv.app_data.base.AppData.py_info)
      * [`AppData.py_info_clear()`](https://virtualenv.pypa.io/en/latest/plugin/api.html#virtualenv.app_data.base.AppData.py_info_clear)
      * [`AppData.can_update`](https://virtualenv.pypa.io/en/latest/plugin/api.html#virtualenv.app_data.base.AppData.can_update)
      * [`AppData.embed_update_log()`](https://virtualenv.pypa.io/en/latest/plugin/api.html#virtualenv.app_data.base.AppData.embed_update_log)
      * [`AppData.house`](https://virtualenv.pypa.io/en/latest/plugin/api.html#virtualenv.app_data.base.AppData.house)
      * [`AppData.transient`](https://virtualenv.pypa.io/en/latest/plugin/api.html#virtualenv.app_data.base.AppData.transient)
      * [`AppData.wheel_image()`](https://virtualenv.pypa.io/en/latest/plugin/api.html#virtualenv.app_data.base.AppData.wheel_image)
      * [`AppData.ensure_extracted()`](https://virtualenv.pypa.io/en/latest/plugin/api.html#virtualenv.app_data.base.AppData.ensure_extracted)
      * [`AppData.extract()`](https://virtualenv.pypa.io/en/latest/plugin/api.html#virtualenv.app_data.base.AppData.extract)
      * [`AppData.locked()`](https://virtualenv.pypa.io/en/latest/plugin/api.html#virtualenv.app_data.base.AppData.locked)

  * [Creators](https://virtualenv.pypa.io/en/latest/plugin/api.html#creators)
    * [`CreatorMeta`](https://virtualenv.pypa.io/en/latest/plugin/api.html#virtualenv.create.creator.CreatorMeta)
    * [`Creator`](https://virtualenv.pypa.io/en/latest/plugin/api.html#virtualenv.create.creator.Creator)
      * [`Creator.can_create()`](https://virtualenv.pypa.io/en/latest/plugin/api.html#virtualenv.create.creator.Creator.can_create)
      * [`Creator.add_parser_arguments()`](https://virtualenv.pypa.io/en/latest/plugin/api.html#virtualenv.create.creator.Creator.add_parser_arguments)
      * [`Creator.create()`](https://virtualenv.pypa.io/en/latest/plugin/api.html#virtualenv.create.creator.Creator.create)
      * [`Creator.add_cachedir_tag()`](https://virtualenv.pypa.io/en/latest/plugin/api.html#virtualenv.create.creator.Creator.add_cachedir_tag)
      * [`Creator.setup_ignore_vcs()`](https://virtualenv.pypa.io/en/latest/plugin/api.html#virtualenv.create.creator.Creator.setup_ignore_vcs)

  * [Seeders](https://virtualenv.pypa.io/en/latest/plugin/api.html#seeders)
    * [`Seeder`](https://virtualenv.pypa.io/en/latest/plugin/api.html#virtualenv.seed.seeder.Seeder)
      * [`Seeder.add_parser_arguments()`](https://virtualenv.pypa.io/en/latest/plugin/api.html#virtualenv.seed.seeder.Seeder.add_parser_arguments)
      * [`Seeder.run()`](https://virtualenv.pypa.io/en/latest/plugin/api.html#virtualenv.seed.seeder.Seeder.run)

  * [Activators](https://virtualenv.pypa.io/en/latest/plugin/api.html#activators)
    * [`Activator`](https://virtualenv.pypa.io/en/latest/plugin/api.html#virtualenv.activation.activator.Activator)
      * [`Activator.supports()`](https://virtualenv.pypa.io/en/latest/plugin/api.html#virtualenv.activation.activator.Activator.supports)
      * [`Activator.add_parser_arguments()`](https://virtualenv.pypa.io/en/latest/plugin/api.html#virtualenv.activation.activator.Activator.add_parser_arguments)
      * [`Activator.generate()`](https://virtualenv.pypa.io/en/latest/plugin/api.html#virtualenv.activation.activator.Activator.generate)

* [Plugin architecture](https://virtualenv.pypa.io/en/latest/plugin/architecture.html)
  * [Entry points](https://virtualenv.pypa.io/en/latest/plugin/architecture.html#entry-points)
  * [Plugin lifecycle](https://virtualenv.pypa.io/en/latest/plugin/architecture.html#plugin-lifecycle)
  * [Extension point design](https://virtualenv.pypa.io/en/latest/plugin/architecture.html#extension-point-design)
  * [How plugins interact](https://virtualenv.pypa.io/en/latest/plugin/architecture.html#how-plugins-interact)
    * [Plugin isolation](https://virtualenv.pypa.io/en/latest/plugin/architecture.html#plugin-isolation)
