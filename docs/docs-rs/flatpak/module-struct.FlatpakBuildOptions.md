flatpak::module
# Struct FlatpakBuildOptions 
Source 

```
pub struct FlatpakBuildOptions {}
```

## Fields§
§`cflags: String`

This is set in the environment variable CFLAGS during the build.
Multiple specifications of this (in e.g. per-arch area) are concatenated, separated by spaces.
§`cflags_override: Option<bool>`

If this is true, clear cflags from previous build options before adding it from these options.
§`cppflags: String`

This is set in the environment variable CPPFLAGS during the build.
Multiple specifications of this (in e.g. per-arch area) are concatenated, separated by spaces.
§`cppflags_override: Option<bool>`

If this is true, clear cppflags from previous build options before adding it from these options.
§`cxxflags: String`

This is set in the environment variable CXXFLAGS during the build.
Multiple specifications of this (in e.g. per-arch area) are concatenated, separated by spaces.
§`cxxflags_override: Option<bool>`

If this is true, clear cxxflags from previous build options before adding it from these options.
§`ldflags: String`

This is set in the environment variable LDFLAGS during the build.
Multiple specifications of this (in e.g. per-arch area) are concatenated,
separated by spaces.
§`ldflags_override: Option<bool>`

If this is true, clear ldflags from previous build options before adding it from these options.
§`prefix: String`

The build prefix for the modules (defaults to /app for applications and /usr for runtimes).
§`libdir: String`

The build libdir for the modules (defaults to /app/lib for applications and /usr/lib for runtimes).
§`append_path: String`

This will get appended to PATH in the build environment (with an leading colon if needed).
§`prepend_path: String`

This will get prepended to PATH in the build environment (with an trailing colon if needed).
§`append_ld_library_path: String`

This will get appended to LD_LIBRARY_PATH in the build environment (with an leading colon if needed).
§`prepend_ld_library_path: String`

This will get prepended to LD_LIBRARY_PATH in the build environment (with an trailing colon if needed).
§`append_pkg_config_path: String`

This will get appended to PKG_CONFIG_PATH in the build environment (with an leading colon if needed).
§`prepend_pkg_config_path: String`

This will get prepended to PKG_CONFIG_PATH in the build environment (with an trailing colon if needed).
§`env: FlatpakBuildOptionsEnv`§`build_args: Vec<String>`

This is an array containing extra options to pass to flatpak build.
§`test_args: Vec<String>`

Similar to build-args but affects the tests, not the normal build.
§`config_opts: Vec<String>`

This is an array containing extra options to pass to configure.
§`make_args: Vec<String>`

An array of extra arguments that will be passed to make
§`make_install_args: Vec<String>`

An array of extra arguments that will be passed to make install
§`strip: Option<bool>`

If this is true (the default is false) then all ELF files will be stripped after install.
§`no_debuginfo: Option<bool>`

By default (if strip is not true) flatpak-builder extracts all debug info in ELF files to a
separate files and puts this in an extension. If you want to disable this, set no-debuginfo
to true.
§`no_debuginfo_compression: Option<bool>`

By default when extracting debuginfo we compress the debug sections.
If you want to disable this, set no-debuginfo-compression to true.
§`arch: BTreeMap<String, FlatpakBuildOptions>`

This is a dictionary defining for each arch a separate build options object that override the main one.

## Trait Implementations§