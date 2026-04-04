# Source: https://cmake.org/cmake/help/latest/manual/ccmake.1.html

Title: ccmake(1) — CMake 4.3.0-rc3 Documentation

URL Source: https://cmake.org/cmake/help/latest/manual/ccmake.1.html

Markdown Content:
Synopsis[¶](https://cmake.org/cmake/help/latest/manual/ccmake.1.html#synopsis "Link to this heading")
-----------------------------------------------------------------------------------------------------

ccmake [<options>] -B <path-to-build> [-S <path-to-source>]
ccmake [<options>] <path-to-source | path-to-existing-build>

Description[¶](https://cmake.org/cmake/help/latest/manual/ccmake.1.html#description "Link to this heading")
-----------------------------------------------------------------------------------------------------------

The **ccmake** executable is the CMake curses interface. Project configuration settings may be specified interactively through this GUI. Brief instructions are provided at the bottom of the terminal when the program is running.

CMake is a cross-platform build system generator. Projects specify their build process with platform-independent CMake listfiles included in each directory of a source tree with the name `CMakeLists.txt`. Users build a project by using CMake to generate a build system for a native tool on their platform.

Options[¶](https://cmake.org/cmake/help/latest/manual/ccmake.1.html#options "Link to this heading")
---------------------------------------------------------------------------------------------------

-S<path-to-source>[¶](https://cmake.org/cmake/help/latest/manual/ccmake.1.html#cmdoption-ccmake-S "Link to this definition")
Path to root directory of the CMake project to build.

-B<path-to-build>[¶](https://cmake.org/cmake/help/latest/manual/ccmake.1.html#cmdoption-ccmake-B "Link to this definition")
Path to directory which CMake will use as the root of build directory.

If the directory doesn't already exist CMake will make it.

-C<initial-cache>[¶](https://cmake.org/cmake/help/latest/manual/ccmake.1.html#cmdoption-ccmake-C "Link to this definition")
Pre-load a script to populate the cache.

When CMake is first run in an empty build tree, it creates a `CMakeCache.txt` file and populates it with customizable settings for the project. This option may be used to specify a file from which to load cache entries before the first pass through the project's CMake listfiles. The loaded entries take priority over the project's default values. The given file should be a CMake script containing [`set()`](https://cmake.org/cmake/help/latest/command/set.html#command:set "set") commands that use the `CACHE` option, not a cache-format file.

References to [`CMAKE_SOURCE_DIR`](https://cmake.org/cmake/help/latest/variable/CMAKE_SOURCE_DIR.html#variable:CMAKE_SOURCE_DIR "CMAKE_SOURCE_DIR") and [`CMAKE_BINARY_DIR`](https://cmake.org/cmake/help/latest/variable/CMAKE_BINARY_DIR.html#variable:CMAKE_BINARY_DIR "CMAKE_BINARY_DIR") within the script evaluate to the top-level source and build tree.

-D<var>:<type>=<value>,-D<var>=<value>[¶](https://cmake.org/cmake/help/latest/manual/ccmake.1.html#cmdoption-ccmake-D "Link to this definition")
Create or update a CMake `CACHE` entry.

When CMake is first run in an empty build tree, it creates a `CMakeCache.txt` file and populates it with customizable settings for the project. This option may be used to specify a setting that takes priority over the project's default value. The option may be repeated for as many `CACHE` entries as desired.

If the `:<type>` portion is given it must be one of the types specified by the [`set()`](https://cmake.org/cmake/help/latest/command/set.html#command:set "set") command documentation for its `CACHE` signature. If the `:<type>` portion is omitted the entry will be created with no type if it does not exist with a type already. If a command in the project sets the type to `PATH` or `FILEPATH` then the `<value>` will be converted to an absolute path.

This option may also be given as a single argument: `-D<var>:<type>=<value>` or `-D<var>=<value>`.

It's important to note that the order of `-C` and `-D` arguments is significant. They will be carried out in the order they are listed, with the last argument taking precedence over the previous ones. For example, if you specify `-DCMAKE_BUILD_TYPE=Debug`, followed by a `-C` argument with a file that calls:

set(CMAKE_BUILD_TYPE "Release" CACHE STRING "" FORCE)

then the `-C` argument will take precedence, and `CMAKE_BUILD_TYPE` will be set to `Release`. However, if the `-D` argument comes after the `-C` argument, it will be set to `Debug`.

If a `set(... CACHE ...)` call in the `-C` file does not use `FORCE`, and a `-D` argument sets the same variable, the `-D` argument will take precedence regardless of order because of the nature of non-`FORCE``set(... CACHE ...)` calls.

-U<globbing_expr>[¶](https://cmake.org/cmake/help/latest/manual/ccmake.1.html#cmdoption-ccmake-U "Link to this definition")
Remove matching entries from CMake `CACHE`.

This option may be used to remove one or more variables from the `CMakeCache.txt` file, globbing expressions using `*` and `?` are supported. The option may be repeated for as many `CACHE` entries as desired.

Use with care, you can make your `CMakeCache.txt` non-working.

-G<generator-name>[¶](https://cmake.org/cmake/help/latest/manual/ccmake.1.html#cmdoption-ccmake-G "Link to this definition")
Specify a build system generator.

CMake may support multiple native build systems on certain platforms. A generator is responsible for generating a particular build system. Possible generator names are specified in the [`cmake-generators(7)`](https://cmake.org/cmake/help/latest/manual/cmake-generators.7.html#manual:cmake-generators(7) "cmake-generators(7)") manual.

If not specified, CMake checks the [`CMAKE_GENERATOR`](https://cmake.org/cmake/help/latest/envvar/CMAKE_GENERATOR.html#envvar:CMAKE_GENERATOR "CMAKE_GENERATOR") environment variable and otherwise falls back to a builtin default selection.

-T<toolset-spec>[¶](https://cmake.org/cmake/help/latest/manual/ccmake.1.html#cmdoption-ccmake-T "Link to this definition")
Toolset specification for the generator, if supported.

Some CMake generators support a toolset specification to tell the native build system how to choose a compiler. See the [`CMAKE_GENERATOR_TOOLSET`](https://cmake.org/cmake/help/latest/variable/CMAKE_GENERATOR_TOOLSET.html#variable:CMAKE_GENERATOR_TOOLSET "CMAKE_GENERATOR_TOOLSET") variable for details.

-A<platform-name>[¶](https://cmake.org/cmake/help/latest/manual/ccmake.1.html#cmdoption-ccmake-A "Link to this definition")
Specify platform name if supported by generator.

Some CMake generators support a platform name to be given to the native build system to choose a compiler or SDK. See the [`CMAKE_GENERATOR_PLATFORM`](https://cmake.org/cmake/help/latest/variable/CMAKE_GENERATOR_PLATFORM.html#variable:CMAKE_GENERATOR_PLATFORM "CMAKE_GENERATOR_PLATFORM") variable for details.

--toolchain<path-to-file>[¶](https://cmake.org/cmake/help/latest/manual/ccmake.1.html#cmdoption-ccmake-toolchain "Link to this definition")
Added in version 3.21.

Specify the cross compiling toolchain file, equivalent to setting [`CMAKE_TOOLCHAIN_FILE`](https://cmake.org/cmake/help/latest/variable/CMAKE_TOOLCHAIN_FILE.html#variable:CMAKE_TOOLCHAIN_FILE "CMAKE_TOOLCHAIN_FILE") variable. Relative paths are interpreted as relative to the build directory, and if not found, relative to the source directory.

--install-prefix<directory>[¶](https://cmake.org/cmake/help/latest/manual/ccmake.1.html#cmdoption-ccmake-install-prefix "Link to this definition")
Added in version 3.21.

Specify the installation directory, used by the [`CMAKE_INSTALL_PREFIX`](https://cmake.org/cmake/help/latest/variable/CMAKE_INSTALL_PREFIX.html#variable:CMAKE_INSTALL_PREFIX "CMAKE_INSTALL_PREFIX") variable. Must be an absolute path.

--project-file<project-file-name>[¶](https://cmake.org/cmake/help/latest/manual/ccmake.1.html#cmdoption-ccmake-project-file "Link to this definition")
Added in version 4.0.

Specify an alternate project file name.

This determines the top-level file processed by CMake when configuring a project, and the file processed by [`add_subdirectory()`](https://cmake.org/cmake/help/latest/command/add_subdirectory.html#command:add_subdirectory "add_subdirectory").

By default, this is `CMakeLists.txt`. If set to anything else, `CMakeLists.txt` will be used as a fallback whenever the specified file cannot be found within a project subdirectory.

Note

This feature is intended for temporary use by developers during an incremental transition and not for publication of a final product. CMake will always emit a warning when the project file is anything other than `CMakeLists.txt`.

-Wno-dev[¶](https://cmake.org/cmake/help/latest/manual/ccmake.1.html#cmdoption-ccmake-Wno-dev "Link to this definition")
Suppress developer warnings.

Suppress warnings that are meant for the author of the `CMakeLists.txt` files. By default this will also turn off deprecation warnings.

-Wdev[¶](https://cmake.org/cmake/help/latest/manual/ccmake.1.html#cmdoption-ccmake-Wdev "Link to this definition")
Enable developer warnings.

Enable warnings that are meant for the author of the `CMakeLists.txt` files. By default this will also turn on deprecation warnings.

-Wdeprecated[¶](https://cmake.org/cmake/help/latest/manual/ccmake.1.html#cmdoption-ccmake-Wdeprecated "Link to this definition")
Enable deprecated functionality warnings.

Enable warnings for usage of deprecated functionality, that are meant for the author of the `CMakeLists.txt` files.

-Wno-deprecated[¶](https://cmake.org/cmake/help/latest/manual/ccmake.1.html#cmdoption-ccmake-Wno-deprecated "Link to this definition")
Suppress deprecated functionality warnings.

Suppress warnings for usage of deprecated functionality, that are meant for the author of the `CMakeLists.txt` files.

-Werror=<what>[¶](https://cmake.org/cmake/help/latest/manual/ccmake.1.html#cmdoption-ccmake-Werror "Link to this definition")
Treat CMake warnings as errors. `<what>` must be one of the following:

`dev`
Make developer warnings errors.

Make warnings that are meant for the author of the `CMakeLists.txt` files errors. By default this will also turn on deprecated warnings as errors.

`deprecated`
Make deprecated macro and function warnings errors.

Make warnings for usage of deprecated macros and functions, that are meant for the author of the `CMakeLists.txt` files, errors.

-Wno-error=<what>[¶](https://cmake.org/cmake/help/latest/manual/ccmake.1.html#cmdoption-ccmake-Wno-error "Link to this definition")
Do not treat CMake warnings as errors. `<what>` must be one of the following:

`dev`
Make warnings that are meant for the author of the `CMakeLists.txt` files not errors. By default this will also turn off deprecated warnings as errors.

`deprecated`
Make warnings for usage of deprecated macros and functions, that are meant for the author of the `CMakeLists.txt` files, not errors.

-version[=json-v1][<file>],--version[=json-v1][<file>],/V[=json-v1][<file>],/version[=json-v1][<file>][¶](https://cmake.org/cmake/help/latest/manual/ccmake.1.html#cmdoption-ccmake-version "Link to this definition")
Show program name/version banner and exit. If `json-v1` is specified, print extended version information in JSON format. The JSON output contains the versions for the CMake and its dependencies. The output is printed to a named `<file>` if given.

The JSON output format is described in machine-readable form by [`this JSON schema`](https://cmake.org/cmake/help/latest/_downloads/8841c8b524587a9aee211c0ac198f604/version-schema.json).

-h,-H,--help,-help,-usage,/?[¶](https://cmake.org/cmake/help/latest/manual/ccmake.1.html#cmdoption-ccmake-h "Link to this definition")
Print usage information and exit.

Usage describes the basic command line interface and its options.

--help<keyword>[<file>][¶](https://cmake.org/cmake/help/latest/manual/ccmake.1.html#cmdoption-ccmake-1 "Link to this definition")
Print help for one CMake keyword.

`<keyword>` can be a property, variable, command, policy, generator or module.

The relevant manual entry for `<keyword>` is printed in a human-readable text format. The output is printed to a named `<file>` if given.

Changed in version 3.28: Prior to CMake 3.28, this option supported command names only.

--help-full[<file>][¶](https://cmake.org/cmake/help/latest/manual/ccmake.1.html#cmdoption-ccmake-help-full "Link to this definition")
Print all help manuals and exit.

All manuals are printed in a human-readable text format. The output is printed to a named `<file>` if given.

--help-manual<man>[<file>][¶](https://cmake.org/cmake/help/latest/manual/ccmake.1.html#cmdoption-ccmake-help-manual "Link to this definition")
Print one help manual and exit.

The specified manual is printed in a human-readable text format. The output is printed to a named `<file>` if given.

--help-manual-list[<file>][¶](https://cmake.org/cmake/help/latest/manual/ccmake.1.html#cmdoption-ccmake-help-manual-list "Link to this definition")
List help manuals available and exit.

The list contains all manuals for which help may be obtained by using the `--help-manual` option followed by a manual name. The output is printed to a named `<file>` if given.

--help-command<cmd>[<file>][¶](https://cmake.org/cmake/help/latest/manual/ccmake.1.html#cmdoption-ccmake-help-command "Link to this definition")
Print help for one command and exit.

The [`cmake-commands(7)`](https://cmake.org/cmake/help/latest/manual/cmake-commands.7.html#manual:cmake-commands(7) "cmake-commands(7)") manual entry for `<cmd>` is printed in a human-readable text format. The output is printed to a named `<file>` if given.

--help-command-list[<file>][¶](https://cmake.org/cmake/help/latest/manual/ccmake.1.html#cmdoption-ccmake-help-command-list "Link to this definition")
List commands with help available and exit.

The list contains all commands for which help may be obtained by using the `--help-command` option followed by a command name. The output is printed to a named `<file>` if given.

--help-commands[<file>][¶](https://cmake.org/cmake/help/latest/manual/ccmake.1.html#cmdoption-ccmake-help-commands "Link to this definition")
Print cmake-commands manual and exit.

The [`cmake-commands(7)`](https://cmake.org/cmake/help/latest/manual/cmake-commands.7.html#manual:cmake-commands(7) "cmake-commands(7)") manual is printed in a human-readable text format. The output is printed to a named `<file>` if given.

--help-module<mod>[<file>][¶](https://cmake.org/cmake/help/latest/manual/ccmake.1.html#cmdoption-ccmake-help-module "Link to this definition")
Print help for one module and exit.

The [`cmake-modules(7)`](https://cmake.org/cmake/help/latest/manual/cmake-modules.7.html#manual:cmake-modules(7) "cmake-modules(7)") manual entry for `<mod>` is printed in a human-readable text format. The output is printed to a named `<file>` if given.

--help-module-list[<file>][¶](https://cmake.org/cmake/help/latest/manual/ccmake.1.html#cmdoption-ccmake-help-module-list "Link to this definition")
List modules with help available and exit.

The list contains all modules for which help may be obtained by using the `--help-module` option followed by a module name. The output is printed to a named `<file>` if given.

--help-modules[<file>][¶](https://cmake.org/cmake/help/latest/manual/ccmake.1.html#cmdoption-ccmake-help-modules "Link to this definition")
Print cmake-modules manual and exit.

The [`cmake-modules(7)`](https://cmake.org/cmake/help/latest/manual/cmake-modules.7.html#manual:cmake-modules(7) "cmake-modules(7)") manual is printed in a human-readable text format. The output is printed to a named `<file>` if given.

--help-policy<cmp>[<file>][¶](https://cmake.org/cmake/help/latest/manual/ccmake.1.html#cmdoption-ccmake-help-policy "Link to this definition")
Print help for one policy and exit.

The [`cmake-policies(7)`](https://cmake.org/cmake/help/latest/manual/cmake-policies.7.html#manual:cmake-policies(7) "cmake-policies(7)") manual entry for `<cmp>` is printed in a human-readable text format. The output is printed to a named `<file>` if given.

--help-policy-list[<file>][¶](https://cmake.org/cmake/help/latest/manual/ccmake.1.html#cmdoption-ccmake-help-policy-list "Link to this definition")
List policies with help available and exit.

The list contains all policies for which help may be obtained by using the `--help-policy` option followed by a policy name. The output is printed to a named `<file>` if given.

--help-policies[<file>][¶](https://cmake.org/cmake/help/latest/manual/ccmake.1.html#cmdoption-ccmake-help-policies "Link to this definition")
Print cmake-policies manual and exit.

The [`cmake-policies(7)`](https://cmake.org/cmake/help/latest/manual/cmake-policies.7.html#manual:cmake-policies(7) "cmake-policies(7)") manual is printed in a human-readable text format. The output is printed to a named `<file>` if given.

--help-property<prop>[<file>][¶](https://cmake.org/cmake/help/latest/manual/ccmake.1.html#cmdoption-ccmake-help-property "Link to this definition")
Print help for one property and exit.

The [`cmake-properties(7)`](https://cmake.org/cmake/help/latest/manual/cmake-properties.7.html#manual:cmake-properties(7) "cmake-properties(7)") manual entries for `<prop>` are printed in a human-readable text format. The output is printed to a named `<file>` if given.

--help-property-list[<file>][¶](https://cmake.org/cmake/help/latest/manual/ccmake.1.html#cmdoption-ccmake-help-property-list "Link to this definition")
List properties with help available and exit.

The list contains all properties for which help may be obtained by using the `--help-property` option followed by a property name. The output is printed to a named `<file>` if given.

--help-properties[<file>][¶](https://cmake.org/cmake/help/latest/manual/ccmake.1.html#cmdoption-ccmake-help-properties "Link to this definition")
Print cmake-properties manual and exit.

The [`cmake-properties(7)`](https://cmake.org/cmake/help/latest/manual/cmake-properties.7.html#manual:cmake-properties(7) "cmake-properties(7)") manual is printed in a human-readable text format. The output is printed to a named `<file>` if given.

--help-variable<var>[<file>][¶](https://cmake.org/cmake/help/latest/manual/ccmake.1.html#cmdoption-ccmake-help-variable "Link to this definition")
Print help for one variable and exit.

The [`cmake-variables(7)`](https://cmake.org/cmake/help/latest/manual/cmake-variables.7.html#manual:cmake-variables(7) "cmake-variables(7)") manual entry for `<var>` is printed in a human-readable text format. The output is printed to a named `<file>` if given.

--help-variable-list[<file>][¶](https://cmake.org/cmake/help/latest/manual/ccmake.1.html#cmdoption-ccmake-help-variable-list "Link to this definition")
List variables with help available and exit.

The list contains all variables for which help may be obtained by using the `--help-variable` option followed by a variable name. The output is printed to a named `<file>` if given.

--help-variables[<file>][¶](https://cmake.org/cmake/help/latest/manual/ccmake.1.html#cmdoption-ccmake-help-variables "Link to this definition")
Print cmake-variables manual and exit.

The [`cmake-variables(7)`](https://cmake.org/cmake/help/latest/manual/cmake-variables.7.html#manual:cmake-variables(7) "cmake-variables(7)") manual is printed in a human-readable text format. The output is printed to a named `<file>` if given.

See Also[¶](https://cmake.org/cmake/help/latest/manual/ccmake.1.html#see-also "Link to this heading")
-----------------------------------------------------------------------------------------------------

The following resources are available to get help using CMake:

Home Page
[https://cmake.org](https://cmake.org/)

The primary starting point for learning about CMake.

Online Documentation and Community Resources
[https://cmake.org/documentation](https://cmake.org/documentation)

Links to available documentation and community resources may be found on this web page.

Discourse Forum
[https://discourse.cmake.org](https://discourse.cmake.org/)

The Discourse Forum hosts discussion and questions about CMake.
