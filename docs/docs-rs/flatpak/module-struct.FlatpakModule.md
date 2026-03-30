flatpak::module
# Struct FlatpakModule 
Source 

```
pub struct FlatpakModule {}
```

## Fields§
§`format: FlatpakManifestFormat`§`name: String`

The name of the module, used in e.g. build logs. The name is also
used for constructing filenames and commandline arguments,
therefore using spaces or ‘/’ in this string is a bad idea.
§`disabled: Option<bool>`

If true, skip this module
§`sources: Vec<FlatpakSourceItem>`

An array of objects defining sources that will be downloaded and extracted in order.
String members in the array are interpreted as the name of a separate
json or yaml file that contains sources. See below for details.
§`config_opts: Vec<String>`

An array of options that will be passed to configure
§`make_args: Vec<String>`

An array of arguments that will be passed to make
§`make_install_args: Vec<String>`

An array of arguments that will be passed to make install
§`rm_configure: Option<bool>`

If true, remove the configure script before starting build
§`no_autogen: Option<bool>`

Ignore the existence of an autogen script
§`no_parallel_make: Option<bool>`

Don’t call make with arguments to build in parallel
§`install_rule: String`

Name of the rule passed to make for the install phase, default is install
§`no_make_install: Option<bool>`

Don’t run the make install (or equivalent) stage
§`no_python_timestamp_fix: Option<bool>`

Don’t fix up the python (*.pyo or *.pyc) header timestamps for ostree use.
§`cmake: Option<bool>`

Use cmake instead of configure (deprecated: use buildsystem instead)
§`buildsystem: Option<FlatpakBuildSystem>`

Build system to use.
§`builddir: Option<bool>`

Use a build directory that is separate from the source directory
§`subdir: String`

Build inside this subdirectory of the extracted sources
§`build_options: Option<FlatpakBuildOptions>`

A build options object that can override global options
§`build_commands: Vec<String>`

An array of commands to run during build (between make and make install if those are used).
This is primarily useful when using the “simple” buildsystem.
Each command is run in /bin/sh -c, so it can use standard POSIX shell syntax such as piping output.
§`post_install: Vec<String>`

An array of shell commands that are run after the install phase.
Can for example clean up the install dir, or install extra files.
§`cleanup: Vec<String>`

An array of file patterns that should be removed at the end.
Patterns starting with / are taken to be full pathnames (without the /app prefix), otherwise
they just match the basename. Note that any patterns will only match
files installed by this module.
§`ensure_writable: Vec<String>`

The way the builder works is that files in the install directory are hard-links to the cached files,
so you’re not allowed to modify them in-place. If you list a file in this then the hardlink
will be broken and you can modify it. This is a workaround, ideally installing files should
replace files, not modify existing ones.
§`only_arches: Vec<String>`

If non-empty, only build the module on the arches listed.
§`skip_arches: Vec<String>`

Don’t build on any of the arches listed.
§`cleanup_platform: Vec<String>`

Extra files to clean up in the platform.
§`run_tests: Option<bool>`

If true this will run the tests after installing.
§`test_rule: String`

The target to build when running the tests. Defaults to “check” for make and “test” for ninja.
Set to empty to disable.
§`test_commands: Vec<String>`

Array of commands to run during the tests.
§`modules: Vec<FlatpakModuleItem>`

An array of objects specifying nested modules to be built before this one.
String members in the array are interpreted as names of a separate json or
yaml file that contains a module.

## Implementations§