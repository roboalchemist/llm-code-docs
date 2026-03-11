# Source: https://cmake.org/cmake/help/latest/manual/cmake.1.html

Title: cmake(1) — CMake 4.3.0-rc3 Documentation

URL Source: https://cmake.org/cmake/help/latest/manual/cmake.1.html

Published Time: Tue, 10 Mar 2026 19:18:20 GMT

Markdown Content:
cmake(1) — CMake 4.3.0-rc3 Documentation
===============
- [x] 

### Navigation

*   [index](https://cmake.org/cmake/help/latest/genindex.html "General Index")
*   [next](https://cmake.org/cmake/help/latest/manual/ctest.1.html "ctest(1)") |
*   [previous](https://cmake.org/cmake/help/latest/index.html "Introduction") |

*   ![Image 1](https://cmake.org/cmake/help/latest/_static/cmake-logo-16.png)[CMake](https://cmake.org/)4.3.0-rc3 »
*   [Documentation](https://cmake.org/cmake/help/latest/index.html) » 
*   [cmake(1)](https://cmake.org/cmake/help/latest/manual/cmake.1.html)

cmake(1)[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmake-1 "Link to this heading")
===================================================================================================

Synopsis[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#synopsis "Link to this heading")
----------------------------------------------------------------------------------------------------

[Generate a Project Buildsystem](https://cmake.org/cmake/help/latest/manual/cmake.1.html#generate-a-project-buildsystem)
 cmake [<options>] -B <path-to-build> [-S <path-to-source>]
 cmake [<options>] <path-to-source | path-to-existing-build>

[Build a Project](https://cmake.org/cmake/help/latest/manual/cmake.1.html#build-a-project)
 cmake --build <dir> [<options>] [-- <build-tool-options>]

[Install a Project](https://cmake.org/cmake/help/latest/manual/cmake.1.html#install-a-project)
 cmake --install <dir> [<options>]

[Open a Project](https://cmake.org/cmake/help/latest/manual/cmake.1.html#open-a-project)
 cmake --open <dir>

[Run a Script](https://cmake.org/cmake/help/latest/manual/cmake.1.html#run-a-script)
 cmake [-D <var>=<value>]... -P <cmake-script-file>

[Run a Command-Line Tool](https://cmake.org/cmake/help/latest/manual/cmake.1.html#run-a-command-line-tool)
 cmake -E <command> [<options>]

[Run the Find-Package Tool](https://cmake.org/cmake/help/latest/manual/cmake.1.html#run-the-find-package-tool)
 cmake --find-package [<options>]

[Run a Workflow Preset](https://cmake.org/cmake/help/latest/manual/cmake.1.html#run-a-workflow-preset)
 cmake --workflow <options>

[View Help](https://cmake.org/cmake/help/latest/manual/cmake.1.html#view-help)
 cmake --help[-<topic>]
Description[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#description "Link to this heading")
----------------------------------------------------------------------------------------------------------

The **cmake** executable is the command-line interface of the cross-platform buildsystem generator CMake. The above [Synopsis](https://cmake.org/cmake/help/latest/manual/cmake.1.html#synopsis) lists various actions the tool can perform as described in sections below.

To build a software project with CMake, [Generate a Project Buildsystem](https://cmake.org/cmake/help/latest/manual/cmake.1.html#generate-a-project-buildsystem). Optionally use **cmake** to [Build a Project](https://cmake.org/cmake/help/latest/manual/cmake.1.html#build-a-project), [Install a Project](https://cmake.org/cmake/help/latest/manual/cmake.1.html#install-a-project) or just run the corresponding build tool (e.g. `make`) directly. **cmake** can also be used to [View Help](https://cmake.org/cmake/help/latest/manual/cmake.1.html#view-help).

The other actions are meant for use by software developers writing scripts in the [`CMake language`](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#manual:cmake-language(7) "cmake-language(7)") to support their builds.

For graphical user interfaces that may be used in place of **cmake**, see [`ccmake`](https://cmake.org/cmake/help/latest/manual/ccmake.1.html#manual:ccmake(1) "ccmake(1)") and [`cmake-gui`](https://cmake.org/cmake/help/latest/manual/cmake-gui.1.html#manual:cmake-gui(1) "cmake-gui(1)"). For command-line interfaces to the CMake testing and packaging facilities, see [`ctest`](https://cmake.org/cmake/help/latest/manual/ctest.1.html#manual:ctest(1) "ctest(1)") and [`cpack`](https://cmake.org/cmake/help/latest/manual/cpack.1.html#manual:cpack(1) "cpack(1)").

For more information on CMake at large, [see also](https://cmake.org/cmake/help/latest/manual/cmake.1.html#see-also) the links at the end of this manual.

Introduction to CMake Buildsystems[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#introduction-to-cmake-buildsystems "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------------------

A _buildsystem_ describes how to build a project's executables and libraries from its source code using a _build tool_ to automate the process. For example, a buildsystem may be a `Makefile` for use with a command-line `make` tool or a project file for an Integrated Development Environment (IDE). In order to avoid maintaining multiple such buildsystems, a project may specify its buildsystem abstractly using files written in the [`CMake language`](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#manual:cmake-language(7) "cmake-language(7)"). From these files CMake generates a preferred buildsystem locally for each user through a backend called a _generator_.

To generate a buildsystem with CMake, the following must be selected:

Source Tree
The top-level directory containing source files provided by the project. The project specifies its buildsystem using files as described in the [`cmake-language(7)`](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#manual:cmake-language(7) "cmake-language(7)") manual, starting with a top-level file named `CMakeLists.txt`. These files specify build targets and their dependencies as described in the [`cmake-buildsystem(7)`](https://cmake.org/cmake/help/latest/manual/cmake-buildsystem.7.html#manual:cmake-buildsystem(7) "cmake-buildsystem(7)") manual.

Build Tree
The top-level directory in which buildsystem files and build output artifacts (e.g. executables and libraries) are to be stored. CMake will write a `CMakeCache.txt` file to identify the directory as a build tree and store persistent information such as buildsystem configuration options.

To maintain a pristine source tree, perform an _out-of-source_ build by using a separate dedicated build tree. An _in-source_ build in which the build tree is placed in the same directory as the source tree is also supported, but discouraged.

Generator
This chooses the kind of buildsystem to generate. See the [`cmake-generators(7)`](https://cmake.org/cmake/help/latest/manual/cmake-generators.7.html#manual:cmake-generators(7) "cmake-generators(7)") manual for documentation of all generators. Run [`cmake --help`](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-h) to see a list of generators available locally. Optionally use the [`-G`](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-G) option below to specify a generator, or simply accept the default CMake chooses for the current platform.

When using one of the [Command-Line Build Tool Generators](https://cmake.org/cmake/help/latest/manual/cmake-generators.7.html#command-line-build-tool-generators) CMake expects that the environment needed by the compiler toolchain is already configured in the shell. When using one of the [IDE Build Tool Generators](https://cmake.org/cmake/help/latest/manual/cmake-generators.7.html#ide-build-tool-generators), no particular environment is needed.

Generate a Project Buildsystem[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#generate-a-project-buildsystem "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------------------------

Run CMake with one of the following command signatures to specify the source and build trees and generate a buildsystem:

`cmake [<options>] -B <path-to-build> [-S <path-to-source>]`

> Added in version 3.13.
> 
> 
> Uses `<path-to-build>` as the build tree and `<path-to-source>` as the source tree. The specified paths may be absolute or relative to the current working directory. The source tree must contain a `CMakeLists.txt` file. The build tree will be created automatically if it does not already exist. For example:
> 
> 
> 
> $ cmake -S src -B build

`cmake [<options>] <path-to-source>`
Uses the current working directory as the build tree, and `<path-to-source>` as the source tree. The specified path may be absolute or relative to the current working directory. The source tree must contain a `CMakeLists.txt` file and must _not_ contain a `CMakeCache.txt` file because the latter identifies an existing build tree. For example:

$ mkdir build ; cd build
$ cmake ../src

`cmake [<options>] <path-to-existing-build>`
Uses `<path-to-existing-build>` as the build tree, and loads the path to the source tree from its `CMakeCache.txt` file, which must have already been generated by a previous run of CMake. The specified path may be absolute or relative to the current working directory. For example:

$ cd build
$ cmake .

In all cases the `<options>` may be zero or more of the [Options](https://cmake.org/cmake/help/latest/manual/cmake.1.html#options) below.

The above styles for specifying the source and build trees may be mixed. Paths specified with [`-S`](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-S) or [`-B`](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-B) are always classified as source or build trees, respectively. Paths specified with plain arguments are classified based on their content and the types of paths given earlier. If only one type of path is given, the current working directory (cwd) is used for the other. For example:

| Command Line | Source Dir | Build Dir |
| --- | --- | --- |
| `cmake -B build` | _cwd_ | `build` |
| `cmake -B build src` | `src` | `build` |
| `cmake -B build -S src` | `src` | `build` |
| `cmake src` | `src` | _cwd_ |
| `cmake build` (existing) | _loaded_ | `build` |
| `cmake -S src` | `src` | _cwd_ |
| `cmake -S src build` | `src` | `build` |
| `cmake -S src -B build` | `src` | `build` |

Changed in version 3.23: CMake warns when multiple source paths are specified. This has never been officially documented or supported, but older versions accidentally accepted multiple source paths and used the last path specified. Avoid passing multiple source path arguments.

After generating a buildsystem one may use the corresponding native build tool to build the project. For example, after using the [`Unix Makefiles`](https://cmake.org/cmake/help/latest/generator/Unix%20Makefiles.html#generator:Unix%20Makefiles "Unix Makefiles") generator one may run `make` directly:

> $ make
> $ make install

Alternatively, one may use **cmake** to [Build a Project](https://cmake.org/cmake/help/latest/manual/cmake.1.html#build-a-project) by automatically choosing and invoking the appropriate native build tool.

### Options[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#options "Link to this heading")

-S<path-to-source>[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-S "Link to this definition")
Path to root directory of the CMake project to build.

-B<path-to-build>[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-B "Link to this definition")
Path to directory which CMake will use as the root of build directory.

If the directory doesn't already exist CMake will make it.

-C<initial-cache>[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-C "Link to this definition")
Pre-load a script to populate the cache.

When CMake is first run in an empty build tree, it creates a `CMakeCache.txt` file and populates it with customizable settings for the project. This option may be used to specify a file from which to load cache entries before the first pass through the project's CMake listfiles. The loaded entries take priority over the project's default values. The given file should be a CMake script containing [`set()`](https://cmake.org/cmake/help/latest/command/set.html#command:set "set") commands that use the `CACHE` option, not a cache-format file.

References to [`CMAKE_SOURCE_DIR`](https://cmake.org/cmake/help/latest/variable/CMAKE_SOURCE_DIR.html#variable:CMAKE_SOURCE_DIR "CMAKE_SOURCE_DIR") and [`CMAKE_BINARY_DIR`](https://cmake.org/cmake/help/latest/variable/CMAKE_BINARY_DIR.html#variable:CMAKE_BINARY_DIR "CMAKE_BINARY_DIR") within the script evaluate to the top-level source and build tree.

-D<var>:<type>=<value>,-D<var>=<value>[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-D "Link to this definition")
Create or update a CMake `CACHE` entry.

When CMake is first run in an empty build tree, it creates a `CMakeCache.txt` file and populates it with customizable settings for the project. This option may be used to specify a setting that takes priority over the project's default value. The option may be repeated for as many `CACHE` entries as desired.

If the `:<type>` portion is given it must be one of the types specified by the [`set()`](https://cmake.org/cmake/help/latest/command/set.html#command:set "set") command documentation for its `CACHE` signature. If the `:<type>` portion is omitted the entry will be created with no type if it does not exist with a type already. If a command in the project sets the type to `PATH` or `FILEPATH` then the `<value>` will be converted to an absolute path.

This option may also be given as a single argument: `-D<var>:<type>=<value>` or `-D<var>=<value>`.

It's important to note that the order of `-C` and `-D` arguments is significant. They will be carried out in the order they are listed, with the last argument taking precedence over the previous ones. For example, if you specify `-DCMAKE_BUILD_TYPE=Debug`, followed by a `-C` argument with a file that calls:

set(CMAKE_BUILD_TYPE "Release" CACHE STRING "" FORCE)

then the `-C` argument will take precedence, and `CMAKE_BUILD_TYPE` will be set to `Release`. However, if the `-D` argument comes after the `-C` argument, it will be set to `Debug`.

If a `set(... CACHE ...)` call in the `-C` file does not use `FORCE`, and a `-D` argument sets the same variable, the `-D` argument will take precedence regardless of order because of the nature of non-`FORCE``set(... CACHE ...)` calls.

-U<globbing_expr>[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-U "Link to this definition")
Remove matching entries from CMake `CACHE`.

This option may be used to remove one or more variables from the `CMakeCache.txt` file, globbing expressions using `*` and `?` are supported. The option may be repeated for as many `CACHE` entries as desired.

Use with care, you can make your `CMakeCache.txt` non-working.

-G<generator-name>[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-G "Link to this definition")
Specify a build system generator.

CMake may support multiple native build systems on certain platforms. A generator is responsible for generating a particular build system. Possible generator names are specified in the [`cmake-generators(7)`](https://cmake.org/cmake/help/latest/manual/cmake-generators.7.html#manual:cmake-generators(7) "cmake-generators(7)") manual.

If not specified, CMake checks the [`CMAKE_GENERATOR`](https://cmake.org/cmake/help/latest/envvar/CMAKE_GENERATOR.html#envvar:CMAKE_GENERATOR "CMAKE_GENERATOR") environment variable and otherwise falls back to a builtin default selection.

-T<toolset-spec>[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-T "Link to this definition")
Toolset specification for the generator, if supported.

Some CMake generators support a toolset specification to tell the native build system how to choose a compiler. See the [`CMAKE_GENERATOR_TOOLSET`](https://cmake.org/cmake/help/latest/variable/CMAKE_GENERATOR_TOOLSET.html#variable:CMAKE_GENERATOR_TOOLSET "CMAKE_GENERATOR_TOOLSET") variable for details.

-A<platform-name>[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-A "Link to this definition")
Specify platform name if supported by generator.

Some CMake generators support a platform name to be given to the native build system to choose a compiler or SDK. See the [`CMAKE_GENERATOR_PLATFORM`](https://cmake.org/cmake/help/latest/variable/CMAKE_GENERATOR_PLATFORM.html#variable:CMAKE_GENERATOR_PLATFORM "CMAKE_GENERATOR_PLATFORM") variable for details.

--toolchain<path-to-file>[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-toolchain "Link to this definition")

Added in version 3.21.

Specify the cross compiling toolchain file, equivalent to setting [`CMAKE_TOOLCHAIN_FILE`](https://cmake.org/cmake/help/latest/variable/CMAKE_TOOLCHAIN_FILE.html#variable:CMAKE_TOOLCHAIN_FILE "CMAKE_TOOLCHAIN_FILE") variable. Relative paths are interpreted as relative to the build directory, and if not found, relative to the source directory.

--install-prefix<directory>[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-install-prefix "Link to this definition")

Added in version 3.21.

Specify the installation directory, used by the [`CMAKE_INSTALL_PREFIX`](https://cmake.org/cmake/help/latest/variable/CMAKE_INSTALL_PREFIX.html#variable:CMAKE_INSTALL_PREFIX "CMAKE_INSTALL_PREFIX") variable. Must be an absolute path.

--project-file<project-file-name>[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-project-file "Link to this definition")

Added in version 4.0.

Specify an alternate project file name.

This determines the top-level file processed by CMake when configuring a project, and the file processed by [`add_subdirectory()`](https://cmake.org/cmake/help/latest/command/add_subdirectory.html#command:add_subdirectory "add_subdirectory").

By default, this is `CMakeLists.txt`. If set to anything else, `CMakeLists.txt` will be used as a fallback whenever the specified file cannot be found within a project subdirectory.

Note

This feature is intended for temporary use by developers during an incremental transition and not for publication of a final product. CMake will always emit a warning when the project file is anything other than `CMakeLists.txt`.

-Wno-dev[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-Wno-dev "Link to this definition")
Suppress developer warnings.

Suppress warnings that are meant for the author of the `CMakeLists.txt` files. By default this will also turn off deprecation warnings.

-Wdev[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-Wdev "Link to this definition")
Enable developer warnings.

Enable warnings that are meant for the author of the `CMakeLists.txt` files. By default this will also turn on deprecation warnings.

-Wdeprecated[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-Wdeprecated "Link to this definition")
Enable deprecated functionality warnings.

Enable warnings for usage of deprecated functionality, that are meant for the author of the `CMakeLists.txt` files.

-Wno-deprecated[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-Wno-deprecated "Link to this definition")
Suppress deprecated functionality warnings.

Suppress warnings for usage of deprecated functionality, that are meant for the author of the `CMakeLists.txt` files.

-Werror=<what>[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-Werror "Link to this definition")
Treat CMake warnings as errors. `<what>` must be one of the following:

`dev`
Make developer warnings errors.

Make warnings that are meant for the author of the `CMakeLists.txt` files errors. By default this will also turn on deprecated warnings as errors.

`deprecated`
Make deprecated macro and function warnings errors.

Make warnings for usage of deprecated macros and functions, that are meant for the author of the `CMakeLists.txt` files, errors.

-Wno-error=<what>[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-Wno-error "Link to this definition")
Do not treat CMake warnings as errors. `<what>` must be one of the following:

`dev`
Make warnings that are meant for the author of the `CMakeLists.txt` files not errors. By default this will also turn off deprecated warnings as errors.

`deprecated`
Make warnings for usage of deprecated macros and functions, that are meant for the author of the `CMakeLists.txt` files, not errors.

--fresh[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-fresh "Link to this definition")

Added in version 3.24.

Perform a fresh configuration of the build tree. This removes any existing `CMakeCache.txt` file and associated `CMakeFiles/` directory, and recreates them from scratch.

Changed in version 3.30: For dependencies previously populated by [`FetchContent`](https://cmake.org/cmake/help/latest/module/FetchContent.html#module:FetchContent "FetchContent") with the `NEW` setting for policy [`CMP0168`](https://cmake.org/cmake/help/latest/policy/CMP0168.html#policy:CMP0168 "CMP0168"), their stamp and script files from any previous run will be removed. The download, update, and patch steps will therefore be forced to re-execute.

-L[A][H][¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-L-A-H "Link to this definition")
List non-advanced cached variables.

List `CACHE` variables will run CMake and list all the variables from the CMake `CACHE` that are not marked as `INTERNAL` or [`ADVANCED`](https://cmake.org/cmake/help/latest/prop_cache/ADVANCED.html#prop_cache:ADVANCED "ADVANCED"). This will effectively display current CMake settings, which can then be changed with [`-D`](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-D) option. Changing some of the variables may result in more variables being created. If `A` is specified, then it will display also advanced variables. If `H` is specified, it will also display help for each variable.

-LR[A][H]<regex>[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-LR-A-H "Link to this definition")

Added in version 3.31.

Show specific non-advanced cached variables

Show non-`INTERNAL` nor [`ADVANCED`](https://cmake.org/cmake/help/latest/prop_cache/ADVANCED.html#prop_cache:ADVANCED "ADVANCED") variables from the CMake `CACHE` that match the given regex. If `A` is specified, then it will also show advanced variables. If `H` is specified, it will also display help for each variable.

-N[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-N "Link to this definition")
View mode only.

Only load the cache. Do not actually run configure and generate steps.

--graphviz=<file>[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-graphviz "Link to this definition")
Generate [Graphviz](https://www.graphviz.org/) of dependencies

This option generates a graphviz input file that will contain all the library and executable dependencies in the project showing the dependencies between the targets in a project, as well as external libraries which are linked against.

When running CMake with the `--graphviz=foo.dot` option, it produces:

*   a `foo.dot` file, showing all dependencies in the project

*   a `foo.dot.<target>` file for each target, showing on which other targets it depends

*   a `foo.dot.<target>.dependers` file for each target, showing which other targets depend on it

Those .dot files can be converted to images using the _dot_ command from the Graphviz package:

dot -Tpng -o foo.png foo.dot

Added in version 3.10: The different dependency types `PUBLIC`, `INTERFACE` and `PRIVATE` are represented as solid, dashed and dotted edges.

Variables specific to the Graphviz support

The resulting graphs can be huge. The look and content of the generated graphs can be controlled using the file `CMakeGraphVizOptions.cmake`. This file is first searched in [`CMAKE_BINARY_DIR`](https://cmake.org/cmake/help/latest/variable/CMAKE_BINARY_DIR.html#variable:CMAKE_BINARY_DIR "CMAKE_BINARY_DIR"), and then in [`CMAKE_SOURCE_DIR`](https://cmake.org/cmake/help/latest/variable/CMAKE_SOURCE_DIR.html#variable:CMAKE_SOURCE_DIR "CMAKE_SOURCE_DIR"). If found, the variables set in it are used to adjust options for the generated Graphviz files.

GRAPHVIZ_GRAPH_NAME[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#variable:GRAPHVIZ_GRAPH_NAME "Link to this definition")
The graph name.

*   Mandatory: NO

*   Default: value of [`CMAKE_PROJECT_NAME`](https://cmake.org/cmake/help/latest/variable/CMAKE_PROJECT_NAME.html#variable:CMAKE_PROJECT_NAME "CMAKE_PROJECT_NAME")

GRAPHVIZ_GRAPH_HEADER[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#variable:GRAPHVIZ_GRAPH_HEADER "Link to this definition")
The header written at the top of the Graphviz files.

*   Mandatory: NO

*   Default: "node [ fontsize = "12" ];"

GRAPHVIZ_NODE_PREFIX[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#variable:GRAPHVIZ_NODE_PREFIX "Link to this definition")
The prefix for each node in the Graphviz files.

*   Mandatory: NO

*   Default: "node"

GRAPHVIZ_EXECUTABLES[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#variable:GRAPHVIZ_EXECUTABLES "Link to this definition")
Set to FALSE to exclude executables from the generated graphs.

*   Mandatory: NO

*   Default: TRUE

GRAPHVIZ_STATIC_LIBS[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#variable:GRAPHVIZ_STATIC_LIBS "Link to this definition")
Set to FALSE to exclude static libraries from the generated graphs.

*   Mandatory: NO

*   Default: TRUE

GRAPHVIZ_SHARED_LIBS[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#variable:GRAPHVIZ_SHARED_LIBS "Link to this definition")
Set to FALSE to exclude shared libraries from the generated graphs.

*   Mandatory: NO

*   Default: TRUE

GRAPHVIZ_MODULE_LIBS[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#variable:GRAPHVIZ_MODULE_LIBS "Link to this definition")
Set to FALSE to exclude module libraries from the generated graphs.

*   Mandatory: NO

*   Default: TRUE

GRAPHVIZ_INTERFACE_LIBS[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#variable:GRAPHVIZ_INTERFACE_LIBS "Link to this definition")
Set to FALSE to exclude interface libraries from the generated graphs.

*   Mandatory: NO

*   Default: TRUE

GRAPHVIZ_OBJECT_LIBS[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#variable:GRAPHVIZ_OBJECT_LIBS "Link to this definition")
Set to FALSE to exclude object libraries from the generated graphs.

*   Mandatory: NO

*   Default: TRUE

GRAPHVIZ_UNKNOWN_LIBS[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#variable:GRAPHVIZ_UNKNOWN_LIBS "Link to this definition")
Set to FALSE to exclude unknown libraries from the generated graphs.

*   Mandatory: NO

*   Default: TRUE

GRAPHVIZ_EXTERNAL_LIBS[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#variable:GRAPHVIZ_EXTERNAL_LIBS "Link to this definition")
Set to FALSE to exclude external libraries from the generated graphs.

*   Mandatory: NO

*   Default: TRUE

GRAPHVIZ_CUSTOM_TARGETS[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#variable:GRAPHVIZ_CUSTOM_TARGETS "Link to this definition")
Set to TRUE to include custom targets in the generated graphs.

*   Mandatory: NO

*   Default: FALSE

GRAPHVIZ_IGNORE_TARGETS[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#variable:GRAPHVIZ_IGNORE_TARGETS "Link to this definition")
A list of regular expressions for names of targets to exclude from the generated graphs.

*   Mandatory: NO

*   Default: empty

GRAPHVIZ_GENERATE_PER_TARGET[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#variable:GRAPHVIZ_GENERATE_PER_TARGET "Link to this definition")
Set to FALSE to not generate per-target graphs `foo.dot.<target>`.

*   Mandatory: NO

*   Default: TRUE

GRAPHVIZ_GENERATE_DEPENDERS[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#variable:GRAPHVIZ_GENERATE_DEPENDERS "Link to this definition")
Set to FALSE to not generate depender graphs `foo.dot.<target>.dependers`.

*   Mandatory: NO

*   Default: TRUE

--system-information[file][¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-system-information "Link to this definition")
Dump information about this system.

Dump a wide range of information about the current system. If run from the top of a binary tree for a CMake project it will dump additional information such as the cache, log files etc.

--print-config-dir[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-print-config-dir "Link to this definition")

Added in version 3.31.

Print CMake config directory for user-wide FileAPI queries.

See [`CMAKE_CONFIG_DIR`](https://cmake.org/cmake/help/latest/envvar/CMAKE_CONFIG_DIR.html#envvar:CMAKE_CONFIG_DIR "CMAKE_CONFIG_DIR") for more details.

--log-level=<level>[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-log-level "Link to this definition")

Added in version 3.16.

Set the log `<level>`.

The [`message()`](https://cmake.org/cmake/help/latest/command/message.html#command:message "message") command will only output messages of the specified log level or higher. The valid log levels are `ERROR`, `WARNING`, `NOTICE`, `STATUS` (default), `VERBOSE`, `DEBUG`, or `TRACE`.

To make a log level persist between CMake runs, set [`CMAKE_MESSAGE_LOG_LEVEL`](https://cmake.org/cmake/help/latest/variable/CMAKE_MESSAGE_LOG_LEVEL.html#variable:CMAKE_MESSAGE_LOG_LEVEL "CMAKE_MESSAGE_LOG_LEVEL") as a cache variable instead. If both the command line option and the variable are given, the command line option takes precedence.

For backward compatibility reasons, `--loglevel` is also accepted as a synonym for this option.

Added in version 3.25: See the [`cmake_language()`](https://cmake.org/cmake/help/latest/command/cmake_language.html#command:cmake_language "cmake_language") command for a way to [query the current message logging level](https://cmake.org/cmake/help/latest/command/cmake_language.html#query-message-log-level).

--log-context[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-log-context "Link to this definition")
Enable the [`message()`](https://cmake.org/cmake/help/latest/command/message.html#command:message "message") command outputting context attached to each message.

This option turns on showing context for the current CMake run only. To make showing the context persistent for all subsequent CMake runs, set [`CMAKE_MESSAGE_CONTEXT_SHOW`](https://cmake.org/cmake/help/latest/variable/CMAKE_MESSAGE_CONTEXT_SHOW.html#variable:CMAKE_MESSAGE_CONTEXT_SHOW "CMAKE_MESSAGE_CONTEXT_SHOW") as a cache variable instead. When this command line option is given, [`CMAKE_MESSAGE_CONTEXT_SHOW`](https://cmake.org/cmake/help/latest/variable/CMAKE_MESSAGE_CONTEXT_SHOW.html#variable:CMAKE_MESSAGE_CONTEXT_SHOW "CMAKE_MESSAGE_CONTEXT_SHOW") is ignored.

--sarif-output=<path>[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-sarif-output "Link to this definition")

Added in version 4.0.

Enable logging of diagnostic messages produced by CMake in the SARIF format.

Write diagnostic messages to a SARIF file at the path specified. Projects can also set [`CMAKE_EXPORT_SARIF`](https://cmake.org/cmake/help/latest/variable/CMAKE_EXPORT_SARIF.html#variable:CMAKE_EXPORT_SARIF "CMAKE_EXPORT_SARIF") to `ON` to enable this feature for a build tree.

--debug-trycompile[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-debug-trycompile "Link to this definition")
Do not delete the files and directories created for [`try_compile()`](https://cmake.org/cmake/help/latest/command/try_compile.html#command:try_compile "try_compile") / [`try_run()`](https://cmake.org/cmake/help/latest/command/try_run.html#command:try_run "try_run") calls. This is useful in debugging failed checks.

Note that some uses of [`try_compile()`](https://cmake.org/cmake/help/latest/command/try_compile.html#command:try_compile "try_compile") may use the same build tree, which will limit the usefulness of this option if a project executes more than one [`try_compile()`](https://cmake.org/cmake/help/latest/command/try_compile.html#command:try_compile "try_compile"). For example, such uses may change results as artifacts from a previous try-compile may cause a different test to either pass or fail incorrectly. This option is best used only when debugging.

(With respect to the preceding, the [`try_run()`](https://cmake.org/cmake/help/latest/command/try_run.html#command:try_run "try_run") command is effectively a [`try_compile()`](https://cmake.org/cmake/help/latest/command/try_compile.html#command:try_compile "try_compile"). Any combination of the two is subject to the potential issues described.)

Added in version 3.25: When this option is enabled, every try-compile check prints a log message reporting the directory in which the check is performed.

--debug-output[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-debug-output "Link to this definition")
Put cmake in a debug mode.

Print extra information during the cmake run like stack traces with [`message(SEND_ERROR)`](https://cmake.org/cmake/help/latest/command/message.html#command:message "message(send_error)") calls.

--debug-find[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-debug-find "Link to this definition")

Added in version 3.17.

Put cmake find commands in a debug mode.

Print extra find call information during the cmake run to standard error. Output is designed for human consumption and not for parsing. See also the [`CMAKE_FIND_DEBUG_MODE`](https://cmake.org/cmake/help/latest/variable/CMAKE_FIND_DEBUG_MODE.html#variable:CMAKE_FIND_DEBUG_MODE "CMAKE_FIND_DEBUG_MODE") variable for debugging a more local part of the project.

--debug-find-pkg=<pkg>[,...][¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-debug-find-pkg "Link to this definition")

Added in version 3.23.

Put cmake find commands in a debug mode when running under calls to [`find_package(<pkg>)`](https://cmake.org/cmake/help/latest/command/find_package.html#command:find_package "find_package"), where `<pkg>` is an entry in the given comma-separated list of case-sensitive package names.

Like [`--debug-find`](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-debug-find), but limiting scope to the specified packages.

--debug-find-var=<var>[,...][¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-debug-find-var "Link to this definition")

Added in version 3.23.

Put cmake find commands in a debug mode when called with `<var>` as the result variable, where `<var>` is an entry in the given comma-separated list.

Like [`--debug-find`](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-debug-find), but limiting scope to the specified variable names.

--trace[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-trace "Link to this definition")
Put cmake in trace mode.

Print a trace of all calls made and from where.

--trace-expand[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-trace-expand "Link to this definition")
Put cmake in trace mode.

Like [`--trace`](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-trace), but with variables expanded.

--trace-format=<format>[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-trace-format "Link to this definition")

Added in version 3.17.

Put cmake in trace mode and sets the trace output format.

`<format>` can be one of the following values.

> `human`
> Prints each trace line in a human-readable format. This is the default format.
> 
> `json-v1`
> Prints each line as a separate JSON document. Each document is separated by a newline (`\n`). It is guaranteed that no newline characters will be present inside a JSON document.
> 
> 
> 
> JSON trace format[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#id3 "Link to this code")
> 
> 
> 
> {
>  "file": "/full/path/to/the/CMake/file.txt",
>  "line": 0,
>  "cmd": "add_executable",
>  "args": ["foo", "bar"],
>  "time": 1579512535.9687231,
>  "frame": 2,
>  "global_frame": 4
> }
> 
> 
> The members are:
> 
> `file`
> The full path to the CMake source file where the function was called.
> 
> `line`
> The line in `file` where the function call begins.
> 
> `line_end`
> If the function call spans multiple lines, this field will be set to the line where the function call ends. If the function calls spans a single line, this field will be unset. This field was added in minor version 2 of the `json-v1` format.
> 
> `defer`
> Optional member that is present when the function call was deferred by [`cmake_language(DEFER)`](https://cmake.org/cmake/help/latest/command/cmake_language.html#defer "cmake_language(defer)"). If present, its value is a string containing the deferred call `<id>`.
> 
> `cmd`
> The name of the function that was called.
> 
> `args`
> A string list of all function parameters.
> 
> `time`
> Timestamp (seconds since epoch) of the function call.
> 
> `frame`
> Stack frame depth of the function that was called, within the context of the `CMakeLists.txt` being processed currently.
> 
> `global_frame`
> Stack frame depth of the function that was called, tracked globally across all `CMakeLists.txt` files involved in the trace. This field was added in minor version 2 of the `json-v1` format.
> 
> 
> Additionally, the first JSON document outputted contains the `version` key for the current major and minor version of the
> 
> 
> 
> JSON version format[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#id4 "Link to this code")
> 
> 
> 
> {
>  "version": {
>  "major": 1,
>  "minor": 2
>  }
> }
> 
> 
> The members are:
> 
> `version`
> Indicates the version of the JSON format. The version has a major and minor components following semantic version conventions.

--trace-source=<file>[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-trace-source "Link to this definition")
Put cmake in trace mode, but output only lines of a specified file.

Multiple options are allowed.

--trace-redirect=<file>[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-trace-redirect "Link to this definition")
Put cmake in trace mode and redirect trace output to a file instead of stderr.

--warn-uninitialized[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-warn-uninitialized "Link to this definition")
Warn about uninitialized values.

Print a warning when an uninitialized variable is used.

--warn-unused-vars[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-warn-unused-vars "Link to this definition")
Does nothing. In CMake versions 3.2 and below this enabled warnings about unused variables. In CMake versions 3.3 through 3.18 the option was broken. In CMake 3.19 and above the option has been removed.

--no-warn-unused-cli[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-no-warn-unused-cli "Link to this definition")
Don't warn about command line options.

Don't find variables that are declared on the command line, but not used.

--check-system-vars[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-check-system-vars "Link to this definition")
Find problems with variable usage in system files.

Normally, unused and uninitialized variables are searched for only in [`CMAKE_SOURCE_DIR`](https://cmake.org/cmake/help/latest/variable/CMAKE_SOURCE_DIR.html#variable:CMAKE_SOURCE_DIR "CMAKE_SOURCE_DIR") and [`CMAKE_BINARY_DIR`](https://cmake.org/cmake/help/latest/variable/CMAKE_BINARY_DIR.html#variable:CMAKE_BINARY_DIR "CMAKE_BINARY_DIR"). This flag tells CMake to warn about other files as well.

--compile-no-warning-as-error[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-compile-no-warning-as-error "Link to this definition")

Added in version 3.24.

Ignore target property [`COMPILE_WARNING_AS_ERROR`](https://cmake.org/cmake/help/latest/prop_tgt/COMPILE_WARNING_AS_ERROR.html#prop_tgt:COMPILE_WARNING_AS_ERROR "COMPILE_WARNING_AS_ERROR") and variable [`CMAKE_COMPILE_WARNING_AS_ERROR`](https://cmake.org/cmake/help/latest/variable/CMAKE_COMPILE_WARNING_AS_ERROR.html#variable:CMAKE_COMPILE_WARNING_AS_ERROR "CMAKE_COMPILE_WARNING_AS_ERROR"), preventing warnings from being treated as errors on compile.

--link-no-warning-as-error[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-link-no-warning-as-error "Link to this definition")

Added in version 4.0.

Ignore target property [`LINK_WARNING_AS_ERROR`](https://cmake.org/cmake/help/latest/prop_tgt/LINK_WARNING_AS_ERROR.html#prop_tgt:LINK_WARNING_AS_ERROR "LINK_WARNING_AS_ERROR") and variable [`CMAKE_LINK_WARNING_AS_ERROR`](https://cmake.org/cmake/help/latest/variable/CMAKE_LINK_WARNING_AS_ERROR.html#variable:CMAKE_LINK_WARNING_AS_ERROR "CMAKE_LINK_WARNING_AS_ERROR"), preventing warnings from being treated as errors on link.

--profiling-output=<path>[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-profiling-output "Link to this definition")

Added in version 3.18.

Used in conjunction with [`--profiling-format`](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-profiling-format) to output to a given path.

--profiling-format=<file>[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-profiling-format "Link to this definition")
Enable the output of profiling data of CMake script in the given format.

This can aid performance analysis of CMake scripts executed. Third party applications should be used to process the output into human readable format.

Currently supported values are: `google-trace` Outputs in Google Trace Format, which can be parsed by the [about:tracing](about:tracing) tab of Google Chrome or using a plugin for a tool like Trace Compass.

--preset<preset>,--preset=<preset>[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-preset "Link to this definition")
Reads a [`preset`](https://cmake.org/cmake/help/latest/manual/cmake-presets.7.html#manual:cmake-presets(7) "cmake-presets(7)") from `CMakePresets.json` and `CMakeUserPresets.json` files, which must be located in the same directory as the top level `CMakeLists.txt` file. The preset may specify the generator, the build directory, a list of variables, and other arguments to pass to CMake. At least one of `CMakePresets.json` or `CMakeUserPresets.json` must be present. The [`CMake GUI`](https://cmake.org/cmake/help/latest/manual/cmake-gui.1.html#manual:cmake-gui(1) "cmake-gui(1)") also recognizes and supports `CMakePresets.json` and `CMakeUserPresets.json` files. For full details on these files, see [`cmake-presets(7)`](https://cmake.org/cmake/help/latest/manual/cmake-presets.7.html#manual:cmake-presets(7) "cmake-presets(7)").

The presets are read before all other command line options, although the [`-S`](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-S) option can be used to specify the source directory containing the `CMakePresets.json` and `CMakeUserPresets.json` files. If [`-S`](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-S) is not given, the current directory is assumed to be the top level source directory and must contain the presets files. The options specified by the chosen preset (variables, generator, etc.) can all be overridden by manually specifying them on the command line. For example, if the preset sets a variable called `MYVAR` to `1`, but the user sets it to `2` with a `-D` argument, the value `2` is preferred.

--list-presets[=<type>][¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-list-presets "Link to this definition")
Lists the available presets of the specified `<type>`. Valid values for `<type>` are `configure`, `build`, `test`, `package`, or `all`. If `<type>` is omitted, `configure` is assumed. The current working directory must contain CMake preset files unless the [`-S`](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-S) option is used to specify a different top level source directory.

--debugger[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-debugger "Link to this definition")
Enables interactive debugging of the CMake language. CMake exposes a debugging interface on the pipe named by [`--debugger-pipe`](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-debugger-pipe) that conforms to the [Debug Adapter Protocol](https://microsoft.github.io/debug-adapter-protocol/) specification with the following modifications.

The `initialize` response includes an additional field named `cmakeVersion` which specifies the version of CMake being debugged.

Debugger initialize response[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#id5 "Link to this code")

{
 "cmakeVersion": {
 "major": 3,
 "minor": 27,
 "patch": 0,
 "full": "3.27.0"
 }
}

The members are:

`major`
An integer specifying the major version number.

`minor`
An integer specifying the minor version number.

`patch`
An integer specifying the patch version number.

`full`
A string specifying the full CMake version.

--debugger-pipe<pipe name>,--debugger-pipe=<pipe name>[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-debugger-pipe "Link to this definition")
Name of the pipe (on Windows) or domain socket (on Unix) to use for debugger communication.

--debugger-dap-log<log path>,--debugger-dap-log=<log path>[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-debugger-dap-log "Link to this definition")
Logs all debugger communication to the specified file.

Build a Project[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#build-a-project "Link to this heading")
------------------------------------------------------------------------------------------------------------------

CMake provides a command-line signature to build an already-generated project binary tree:

cmake --build <dir> [<options>] [-- <build-tool-options>]
cmake --build --preset <preset> [<options>] [-- <build-tool-options>]

This abstracts a native build tool's command-line interface with the following options:

--build<dir>[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-build "Link to this definition")
Project binary directory to be built. This is required (unless a preset is specified) and must be first.

--preset<preset>,--preset=<preset>[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-build-preset "Link to this definition")
Use a build preset to specify build options. The project binary directory is inferred from the `configurePreset` key unless a directory is specified after `--build`. The current working directory must contain CMake preset files. See [`preset`](https://cmake.org/cmake/help/latest/manual/cmake-presets.7.html#manual:cmake-presets(7) "cmake-presets(7)") for more details.

Changed in version 4.3: `cmake --build` now supports specifying a build directory and preset together.

--list-presets[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-build-list-presets "Link to this definition")
Lists the available build presets. The current working directory must contain CMake preset files.

-j[<jobs>],--parallel[<jobs>][¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-build-j "Link to this definition")

Added in version 3.12.

The maximum number of concurrent processes to use when building. If `<jobs>` is omitted the native build tool's default number is used.

The [`CMAKE_BUILD_PARALLEL_LEVEL`](https://cmake.org/cmake/help/latest/envvar/CMAKE_BUILD_PARALLEL_LEVEL.html#envvar:CMAKE_BUILD_PARALLEL_LEVEL "CMAKE_BUILD_PARALLEL_LEVEL") environment variable, if set, specifies a default parallel level when this option is not given.

Some native build tools always build in parallel. The use of `<jobs>` value of `1` can be used to limit to a single job.

-t<tgt>...,--target<tgt>...[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-build-t "Link to this definition")
Build `<tgt>` instead of the default target. Multiple targets may be given, separated by spaces.

--config<cfg>[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-build-config "Link to this definition")
For multi-configuration tools, choose configuration `<cfg>`.

--clean-first[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-build-clean-first "Link to this definition")
Build target `clean` first, then build. (To clean only, use [`--target clean`](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-build-t).)

--resolve-package-references=<value>[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-build-resolve-package-references "Link to this definition")

Added in version 3.23.

Resolve remote package references from external package managers (e.g. NuGet) before build. When `<value>` is set to `on` (default), packages will be restored before building a target. When `<value>` is set to `only`, the packages will be restored, but no build will be performed. When `<value>` is set to `off`, no packages will be restored.

If the target does not define any package references, this option does nothing.

This setting can be specified in a build preset (using `resolvePackageReferences`). The preset setting will be ignored, if this command line option is specified.

If no command line parameter or preset option are provided, an environment- specific cache variable will be evaluated to decide, if package restoration should be performed.

When using [Visual Studio Generators](https://cmake.org/cmake/help/latest/manual/cmake-generators.7.html#visual-studio-generators), package references are defined using the [`VS_PACKAGE_REFERENCES`](https://cmake.org/cmake/help/latest/prop_tgt/VS_PACKAGE_REFERENCES.html#prop_tgt:VS_PACKAGE_REFERENCES "VS_PACKAGE_REFERENCES") property. Package references are restored using NuGet. It can be disabled by setting the `CMAKE_VS_NUGET_PACKAGE_RESTORE` variable to `OFF`.

--use-stderr[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-build-use-stderr "Link to this definition")
Ignored. Behavior is default in CMake >= 3.0.

-v,--verbose[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-build-v "Link to this definition")
Enable verbose output - if supported - including the build commands to be executed.

This option can be omitted if [`VERBOSE`](https://cmake.org/cmake/help/latest/envvar/VERBOSE.html#envvar:VERBOSE "VERBOSE") environment variable or [`CMAKE_VERBOSE_MAKEFILE`](https://cmake.org/cmake/help/latest/variable/CMAKE_VERBOSE_MAKEFILE.html#variable:CMAKE_VERBOSE_MAKEFILE "CMAKE_VERBOSE_MAKEFILE") cached variable is set.

--[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake--build-0 "Link to this definition")
Pass remaining options to the native tool.

Run [`cmake --build`](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-build) with no options for quick help.

### Generator-Specific Build Tool Behavior[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#generator-specific-build-tool-behavior "Link to this heading")

`cmake --build` has special behavior with some generators:

[`Xcode`](https://cmake.org/cmake/help/latest/generator/Xcode.html#generator:Xcode "Xcode")

> Added in version 4.1: If a third-party tool has written a `.xcworkspace` next to the CMake-generated `.xcodeproj`, `cmake --build` drives the build through the workspace instead.

Install a Project[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#install-a-project "Link to this heading")
----------------------------------------------------------------------------------------------------------------------

CMake provides a command-line signature to install an already-generated project binary tree:

cmake --install <dir> [<options>]

This may be used after building a project to run installation without using the generated build system or the native build tool. The options are:

--install<dir>[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-install "Link to this definition")
Project binary directory to install. This is required and must be first.

--config<cfg>[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-install-config "Link to this definition")
For multi-configuration generators, choose configuration `<cfg>`.

--component<comp>[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-install-component "Link to this definition")
Component-based install. Only install component `<comp>`.

--default-directory-permissions<permissions>[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-install-default-directory-permissions "Link to this definition")
Default directory install permissions. Permissions in format `<u=rwx,g=rx,o=rx>`.

--prefix<prefix>[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake--install-0 "Link to this definition")
Specifies an alternative installation prefix, temporarily replacing the value of the [`CMAKE_INSTALL_PREFIX`](https://cmake.org/cmake/help/latest/variable/CMAKE_INSTALL_PREFIX.html#variable:CMAKE_INSTALL_PREFIX "CMAKE_INSTALL_PREFIX") variable at the installation phase.

The main purpose of this option is to allow installation to occur in an arbitrary location. This is commonly used in certain installation and packaging workflows. It is analogous to selecting the installation directory during the installation phase. For example, on Windows, where a user may choose the destination folder for the project.

Note

When the project is using the [`GNUInstallDirs`](https://cmake.org/cmake/help/latest/module/GNUInstallDirs.html#module:GNUInstallDirs "GNUInstallDirs") module, there are some [special cases](https://cmake.org/cmake/help/latest/module/GNUInstallDirs.html#gnuinstalldirs-special-cases) that are evaluated based on the value of the [`CMAKE_INSTALL_PREFIX`](https://cmake.org/cmake/help/latest/variable/CMAKE_INSTALL_PREFIX.html#variable:CMAKE_INSTALL_PREFIX "CMAKE_INSTALL_PREFIX") variable during the configuration phase. The results persist even if an alternative prefix is used during installation.

--strip[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-install-strip "Link to this definition")
Strip before installing.

-v,--verbose[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-install-v "Link to this definition")
Enable verbose output.

This option can be omitted if [`VERBOSE`](https://cmake.org/cmake/help/latest/envvar/VERBOSE.html#envvar:VERBOSE "VERBOSE") environment variable is set.

-j<jobs>,--parallel<jobs>[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-install-j "Link to this definition")

Added in version 3.31.

Install in parallel using the given number of jobs. Only available if [`INSTALL_PARALLEL`](https://cmake.org/cmake/help/latest/prop_gbl/INSTALL_PARALLEL.html#prop_gbl:INSTALL_PARALLEL "INSTALL_PARALLEL") is enabled. The [`CMAKE_INSTALL_PARALLEL_LEVEL`](https://cmake.org/cmake/help/latest/envvar/CMAKE_INSTALL_PARALLEL_LEVEL.html#envvar:CMAKE_INSTALL_PARALLEL_LEVEL "CMAKE_INSTALL_PARALLEL_LEVEL") environment variable specifies a default parallel level when this option is not provided.

Run [`cmake --install`](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-install) with no options for quick help.

Open a Project[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#open-a-project "Link to this heading")
----------------------------------------------------------------------------------------------------------------

cmake --open <dir>

Open the generated project in the associated application. This is only supported by some generators.

Run a Script[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#run-a-script "Link to this heading")
------------------------------------------------------------------------------------------------------------

cmake [-D <var>=<value>]... -P <cmake-script-file> [-- <unparsed-options>...]

-D<var>=<value>[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-P-D "Link to this definition")
Define a variable for script mode.

-P<cmake-script-file>[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-P "Link to this definition")
Process the given cmake file as a script written in the CMake language. No configure or generate step is performed and the cache is not modified. If variables are defined using `-D`, this must be done before the `-P` argument.

Any options after `--` are not parsed by CMake, but they are still included in the set of [`CMAKE_ARGV<n>`](https://cmake.org/cmake/help/latest/variable/CMAKE_ARGV0.html#variable:CMAKE_ARGV0 "CMAKE_ARGV0") variables passed to the script (including the `--` itself).

Run a Command-Line Tool[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#run-a-command-line-tool "Link to this heading")
----------------------------------------------------------------------------------------------------------------------------------

CMake provides builtin command-line tools through the signature

cmake -E <command> [<options>]

-E[help][¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-E "Link to this definition")
Run `cmake -E` or `cmake -E help` for a summary of commands.

Available commands are:

bin2c[<options>...][--][<input-file>[<output-file>]][¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-E-arg-bin2c "Link to this definition")

Added in version 4.3.

Convert a binary file to a C array. If input file is unspecified or `-`, read from standard input instead of a file. If output file is unspecified or `-`, write to standard output instead of a file.

By default, this prints only the bytes. Enclosing text can be added with the `--template-file` argument. You can also `#include` the bytes from another file, acting as a drop-in replacement for the `#embed` directive from C23 and C++26:

unsigned char my_bytes[] = {
/* #embed "bin2c_input.bin" */
#include "bin2c_output.c.txt"
};

--signed[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-E_bin2c-signed "Link to this definition")
Print the bytes as signed integers rather than unsigned.

--decimal[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-E_bin2c-decimal "Link to this definition")
Print the bytes as decimal rather than hexadecimal.

--trailing-comma[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-E_bin2c-trailing-comma "Link to this definition")
Append a trailing comma after the last byte (not included by default.)

--template-file<template-file>[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-E_bin2c-template-file "Link to this definition")
Format from a template file. The template file contains placeholders for the array and optionally the length (which will be a non-negative decimal integer). Such placeholders are enclosed in `@` at the beginning and end of the placeholder. This functionality is similar to [`configure_file()`](https://cmake.org/cmake/help/latest/command/configure_file.html#command:configure_file "configure_file") called with the `@ONLY` argument, but only the array and length placeholders will be replaced, and any other placeholders will be left as-is.

An example of a potential template file:

unsigned char my_bytes[] = {@array@};

size_t length = @length@;

The array placeholder may occur at most once in the template file. The length placeholder may occur zero or more times after the array placeholder, but not before it.

Note that the length is the number of elements printed, and may not match the `sizeof` the resulting array if a type other than `unsigned char` is used.

--template-array-placeholder<placeholder-name>[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-E_bin2c-template-array-placeholder "Link to this definition")
Specify a name for the array placeholder in the template file. Set to `array` by default.

--template-length-placeholder<placeholder-name>[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-E_bin2c-template-length-placeholder "Link to this definition")
Specify a name for the length placeholder in the template file. Set to `length` by default.

capabilities[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-E-arg-capabilities "Link to this definition")

Added in version 3.7.

Report cmake capabilities in JSON format. The output is a JSON object with the following keys:

`version`
A JSON object with version information. Keys are:

`string`
The full version string as displayed by cmake [`--version`](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-version).

`major`
The major version number in integer form.

`minor`
The minor version number in integer form.

`patch`
The patch level in integer form.

`suffix`
The cmake version suffix string.

`isDirty`
A bool that is set if the cmake build is from a dirty tree.

`generators`
A list available generators. Each generator is a JSON object with the following keys:

`name`
A string containing the name of the generator.

`toolsetSupport`
`true` if the generator supports toolsets and `false` otherwise.

`platformSupport`
`true` if the generator supports platforms and `false` otherwise.

`supportedPlatforms`

Added in version 3.21.

Optional member that may be present when the generator supports platform specification via [`CMAKE_GENERATOR_PLATFORM`](https://cmake.org/cmake/help/latest/variable/CMAKE_GENERATOR_PLATFORM.html#variable:CMAKE_GENERATOR_PLATFORM "CMAKE_GENERATOR_PLATFORM") ([`-A ...`](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-A)). The value is a list of platforms known to be supported.

`extraGenerators`
A list of strings with all the [Extra Generators](https://cmake.org/cmake/help/latest/manual/cmake-generators.7.html#extra-generators) compatible with the generator.

`fileApi`
Optional member that is present when the [`cmake-file-api(7)`](https://cmake.org/cmake/help/latest/manual/cmake-file-api.7.html#manual:cmake-file-api(7) "cmake-file-api(7)") is available. The value is a JSON object with one member:

`requests`
A JSON array containing zero or more supported file-api requests. Each request is a JSON object with members:

`kind`
Specifies one of the supported [Object Kinds](https://cmake.org/cmake/help/latest/manual/cmake-file-api.7.html#file-api-object-kinds).

`version`
A JSON array whose elements are each a JSON object containing `major` and `minor` members specifying non-negative integer version components.

`serverMode`
`true` if cmake supports server-mode and `false` otherwise. Always false since CMake 3.20.

`tls`

Added in version 3.25.

`true` if TLS support is enabled and `false` otherwise.

`debugger`

Added in version 3.27.

`true` if the [`--debugger`](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-debugger) mode is supported and `false` otherwise.

cat[--]<files>...[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-E-arg-cat "Link to this definition")

Added in version 3.18.

Concatenate files and print on the standard output.

--[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-E_cat-0 "Link to this definition")

Added in version 3.24.

Added support for the double dash argument `--`. This basic implementation of `cat` does not support any options, so using a option starting with `-` will result in an error. Use `--` to indicate the end of options, in case a file starts with `-`.

Added in version 3.29: `cat` can now print the standard input by passing the `-` argument.

chdir<dir><cmd>[<arg>...][¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-E-arg-chdir "Link to this definition")
Change the current working directory and run a command.

compare_files[--ignore-eol]<file1><file2>[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-E-arg-compare_files "Link to this definition")
Check if `<file1>` is same as `<file2>`. If files are the same, then returns `0`, if not it returns `1`. In case of invalid arguments, it returns 2.

--ignore-eol[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-E_compare_files-ignore-eol "Link to this definition")

Added in version 3.14.

The option implies line-wise comparison and ignores LF/CRLF differences.

copy<file>...<destination>,copy-t<destination><file>...[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-E-arg-copy "Link to this definition")
Copy files to `<destination>` (either file or directory). If multiple files are specified, or if `-t` is specified, the `<destination>` must be directory and it must exist. If `-t` is not specified, the last argument is assumed to be the `<destination>`. Wildcards are not supported. `copy` does follow symlinks. That means it does not copy symlinks, but the files or directories it point to.

Added in version 3.5: Support for multiple input files.

Added in version 3.26: Support for `-t` argument.

copy_directory<dir>...<destination>[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-E-arg-copy_directory "Link to this definition")
Copy content of `<dir>...` directories to `<destination>` directory. If `<destination>` directory does not exist it will be created. `copy_directory` does follow symlinks.

Added in version 3.5: Support for multiple input directories.

Added in version 3.15: The command now fails when the source directory does not exist. Previously it succeeded by creating an empty destination directory.

copy_directory_if_different<dir>...<destination>[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-E-arg-copy_directory_if_different "Link to this definition")

Added in version 3.26.

Copy changed content of `<dir>...` directories to `<destination>` directory. If `<destination>` directory does not exist it will be created.

`copy_directory_if_different` does follow symlinks. The command fails when the source directory does not exist.

copy_directory_if_newer<dir>...<destination>[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-E-arg-copy_directory_if_newer "Link to this definition")

Added in version 4.2.

Copy content of `<dir>...` directories to `<destination>` directory if source files are newer than destination files (based on file timestamps). If `<destination>` directory does not exist it will be created.

`copy_directory_if_newer` does follow symlinks. The command fails when the source directory does not exist. This is faster than `copy_directory_if_different` as it only compares file timestamps instead of file contents.

copy_if_different<file>...<destination>[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-E-arg-copy_if_different "Link to this definition")
Copy files to `<destination>` (either file or directory) if they have changed. If multiple files are specified, the `<destination>` must be directory and it must exist. `copy_if_different` does follow symlinks.

Added in version 3.5: Support for multiple input files.

copy_if_newer<file>...<destination>[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-E-arg-copy_if_newer "Link to this definition")

Added in version 4.2.

Copy files to `<destination>` (either file or directory) if source files are newer than destination files (based on file timestamps). If multiple files are specified, the `<destination>` must be directory and it must exist. `copy_if_newer` does follow symlinks. This is faster than `copy_if_different` as it only compares file timestamps instead of file contents.

create_symlink<old><new>[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-E-arg-create_symlink "Link to this definition")
Create a symbolic link `<new>` naming `<old>`.

Added in version 3.13: Support for creating symlinks on Windows.

Note

Path to where `<new>` symbolic link will be created has to exist beforehand.

create_hardlink<old><new>[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-E-arg-create_hardlink "Link to this definition")

Added in version 3.19.

Create a hard link `<new>` naming `<old>`.

Note

Path to where `<new>` hard link will be created has to exist beforehand. `<old>` has to exist beforehand.

echo[<string>...][¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-E-arg-echo "Link to this definition")
Displays arguments as text.

echo_append[<string>...][¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-E-arg-echo_append "Link to this definition")
Displays arguments as text but no new line.

env[<options>][--]<command>[<arg>...][¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-E-arg-env "Link to this definition")

Added in version 3.1.

Run command in a modified environment. Options are:

NAME=VALUE[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-E_env-arg-NAME "Link to this definition")
Replaces the current value of `NAME` with `VALUE`.

--unset=NAME[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-E_env-unset "Link to this definition")
Unsets the current value of `NAME`.

--modify ENVIRONMENT_MODIFICATION[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-E_env-modify "Link to this definition")

Added in version 3.25.

Apply a single [`ENVIRONMENT_MODIFICATION`](https://cmake.org/cmake/help/latest/prop_test/ENVIRONMENT_MODIFICATION.html#prop_test:ENVIRONMENT_MODIFICATION "ENVIRONMENT_MODIFICATION") operation to the modified environment.

The `NAME=VALUE` and `--unset=NAME` options are equivalent to `--modify NAME=set:VALUE` and `--modify NAME=unset:`, respectively. Note that `--modify NAME=reset:` resets `NAME` to the value it had when **cmake** launched (or unsets it), not to the most recent `NAME=VALUE` option.

--[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-E_env-0 "Link to this definition")

Added in version 3.24.

Added support for the double dash argument `--`. Use `--` to stop interpreting options/environment variables and treat the next argument as the command, even if it start with `-` or contains a `=`.

environment[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-E-arg-environment "Link to this definition")
Display the current environment variables.

false[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-E-arg-false "Link to this definition")

Added in version 3.16.

Do nothing, with an exit code of 1.

make_directory<dir>...[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-E-arg-make_directory "Link to this definition")
Create `<dir>` directories. If necessary, create parent directories too. If a directory already exists it will be silently ignored.

Added in version 3.5: Support for multiple input directories.

md5sum<file>...[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-E-arg-md5sum "Link to this definition")
Create MD5 checksum of files in `md5sum` compatible format:

351abe79cd3800b38cdfb25d45015a15  file1.txt
052f86c15bbde68af55c7f7b340ab639  file2.txt

Changed in version 4.3: Passing `-` reads from standard input.

sha1sum<file>...[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-E-arg-sha1sum "Link to this definition")

Added in version 3.10.

Create SHA1 checksum of files in `sha1sum` compatible format:

4bb7932a29e6f73c97bb9272f2bdc393122f86e0  file1.txt
1df4c8f318665f9a5f2ed38f55adadb7ef9f559c  file2.txt

Changed in version 4.3: Passing `-` reads from standard input.

sha224sum<file>...[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-E-arg-sha224sum "Link to this definition")

Added in version 3.10.

Create SHA224 checksum of files in `sha224sum` compatible format:

b9b9346bc8437bbda630b0b7ddfc5ea9ca157546dbbf4c613192f930  file1.txt
6dfbe55f4d2edc5fe5c9197bca51ceaaf824e48eba0cc453088aee24  file2.txt

Changed in version 4.3: Passing `-` reads from standard input.

sha256sum<file>...[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-E-arg-sha256sum "Link to this definition")

Added in version 3.10.

Create SHA256 checksum of files in `sha256sum` compatible format:

76713b23615d31680afeb0e9efe94d47d3d4229191198bb46d7485f9cb191acc  file1.txt
15b682ead6c12dedb1baf91231e1e89cfc7974b3787c1e2e01b986bffadae0ea  file2.txt

Changed in version 4.3: Passing `-` reads from standard input.

sha384sum<file>...[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-E-arg-sha384sum "Link to this definition")

Added in version 3.10.

Create SHA384 checksum of files in `sha384sum` compatible format:

acc049fedc091a22f5f2ce39a43b9057fd93c910e9afd76a6411a28a8f2b8a12c73d7129e292f94fc0329c309df49434  file1.txt
668ddeb108710d271ee21c0f3acbd6a7517e2b78f9181c6a2ff3b8943af92b0195dcb7cce48aa3e17893173c0a39e23d  file2.txt

Changed in version 4.3: Passing `-` reads from standard input.

sha512sum<file>...[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-E-arg-sha512sum "Link to this definition")

Added in version 3.10.

Create SHA512 checksum of files in `sha512sum` compatible format:

2a78d7a6c5328cfb1467c63beac8ff21794213901eaadafd48e7800289afbc08e5fb3e86aa31116c945ee3d7bf2a6194489ec6101051083d1108defc8e1dba89  file1.txt
7a0b54896fe5e70cca6dd643ad6f672614b189bf26f8153061c4d219474b05dad08c4e729af9f4b009f1a1a280cb625454bf587c690f4617c27e3aebdf3b7a2d  file2.txt

Changed in version 4.3: Passing `-` reads from standard input.

remove[-f]<file>...[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-E-arg-remove "Link to this definition")

Deprecated since version 3.17.

Remove the file(s). The planned behavior was that if any of the listed files already do not exist, the command returns a non-zero exit code, but no message is logged. The `-f` option changes the behavior to return a zero exit code (i.e. success) in such situations instead. `remove` does not follow symlinks. That means it remove only symlinks and not files it point to.

The implementation was buggy and always returned 0. It cannot be fixed without breaking backwards compatibility. Use `rm` instead.

remove_directory<dir>...[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-E-arg-remove_directory "Link to this definition")

Deprecated since version 3.17.

Remove `<dir>` directories and their contents. If a directory does not exist it will be silently ignored. Use `rm` instead.

Added in version 3.15: Support for multiple directories.

Added in version 3.16: If `<dir>` is a symlink to a directory, just the symlink will be removed.

rename<oldname><newname>[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-E-arg-rename "Link to this definition")
Rename a file or directory (on one volume). If file with the `<newname>` name already exists, then it will be silently replaced.

rm[-rRf][--]<file|dir>...[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-E-arg-rm "Link to this definition")

Added in version 3.17.

Remove the files `<file>` or directories `<dir>`. Use `-r` or `-R` to remove directories and their contents recursively. If any of the listed files/directories do not exist, the command returns a non-zero exit code, but no message is logged. The `-f` option changes the behavior to return a zero exit code (i.e. success) in such situations instead. Use `--` to stop interpreting options and treat all remaining arguments as paths, even if they start with `-`.

sleep<number>[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-E-arg-sleep "Link to this definition")

Added in version 3.0.

Sleep for `<number>` seconds. `<number>` may be a floating point number. A practical minimum is about 0.1 seconds due to overhead in starting/stopping CMake executable. This can be useful in a CMake script to insert a delay:

# Sleep for about 0.5 seconds
execute_process(COMMAND ${CMAKE_COMMAND} -E sleep 0.5)

tar[cxt][vf][zjJ]file.tar[<options>][--][<pathname>...][¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-E-arg-tar "Link to this definition")
Create or extract a tar or zip archive. Options are:

c[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-E_tar-arg-c "Link to this definition")
Create a new archive containing the specified files. If used, the `<pathname>...` argument is mandatory.

x[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-E_tar-arg-x "Link to this definition")
Extract to disk from the archive.

Added in version 3.15: The `<pathname>...` argument could be used to extract only selected files or directories. When extracting selected files or directories, you must provide their exact names including the path, as printed by list (`-t`).

Changed in version 4.3: Archive entries containing path traversal sequences (`..`), or absolute paths, are rejected for security.

t[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-E_tar-arg-t "Link to this definition")
List archive contents.

Added in version 3.15: The `<pathname>...` argument could be used to list only selected files or directories.

v[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-E_tar-arg-v "Link to this definition")
Produce verbose output.

z[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-E_tar-arg-z "Link to this definition")
Compress the resulting archive with gzip (Deflate).

j[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-E_tar-arg-j "Link to this definition")
Compress the resulting archive with bzip2.

J[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-E_tar-arg-J "Link to this definition")

Added in version 3.1.

Compress the resulting archive with XZ (LZMA2).

--zstd[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-E_tar-zstd "Link to this definition")

Added in version 3.15.

Compress the resulting archive with Zstandard.

--lzma[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-E_tar-lzma "Link to this definition")

Added in version 4.3.

Compress the resulting archive with LZMA algorithm.

--files-from=<file>[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-E_tar-files-from "Link to this definition")

Added in version 3.1.

Read file names from the given file, one per line. Blank lines are ignored. Lines may not start in `-` except for `--add-file=<name>` to add files whose names start in `-`.

--format=<format>[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-E_tar-format "Link to this definition")

Added in version 3.3.

Specify the format of the archive to be created. Supported formats are:

*   `7zip`

*   `gnutar`

*   `pax`

*   `paxr` (restricted pax, default)

*   `raw`

Added in version 4.3. 
If this format is used, only one file will be compressed with the compression type specified by the [`--cmake-tar-compression-method`](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-E_tar-cmake-tar-compression-method).

*   `zip`

If the compression method is not specified, the compression method depends on the format:

*   `7zip` uses `LZMA` compression

*   `zip` uses `Deflate` compression

*   others uses no compression by default

Added in version 4.3: The `7zip` and `zip` formats support changing the default compression method and compression level.

--mtime=<date>[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-E_tar-mtime "Link to this definition")

Added in version 3.1.

Specify modification time recorded in tarball entries.

--cmake-tar-compression-method=<compression-method>[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-E_tar-cmake-tar-compression-method "Link to this definition")

Added in version 4.3.

The `<compression-method>` must be one of the following:

*   `none` or `store` - no compression is used

*   `deflate` or `gzip` - Deflate-based

*   `bzip2` - BZip2-based

*   `lzma` - LZMA-based

*   `lzma2` or `xz` - LZMA2-based

*   `ppmd` - PPMd-based

This compression method is only supported by the `7zip` archive format.

*   `zstd` - Zstandard-based

This is the second variant for the compression method selection. It provide more compression methods, that the classic `tar`-like interface. You can use any of them.

The default value depends on the [`--format`](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-E_tar-format) option value and described in the corresponding section.

--cmake-tar-compression-level=<compression-level>[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-E_tar-cmake-tar-compression-level "Link to this definition")

Added in version 4.3.

The `<compression-level>` should be between `0` and `9`, with the default being `0`. The compression algorithm must be selected when the `--cmake-tar-compression-level` option is given.

The `<compression-level>` of the `Zstd` algorithm can be set between `0` and `19`, except for the `zip` format.

The value `0` is used to specify the default compression level. It is selected automatically by the archive library backend and not directly set by CMake itself. The default compression level may vary between archive formats, platforms, etc.

--cmake-tar-threads=<number>[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-E_tar-cmake-tar-threads "Link to this definition")

Added in version 4.3.

Use the `<number>` threads to operate on the archive. Currently only multi-threaded compression is supported.

If set to `0`, the number of available cores on the machine will be used instead. Note that not all compression modes support threading in all environments.

--touch[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-E_tar-touch "Link to this definition")

Added in version 3.24.

Use current local timestamp instead of extracting file timestamps from the archive.

--[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-E_tar-0 "Link to this definition")

Added in version 3.1.

Stop interpreting options and treat all remaining arguments as file names, even if they start with `-`.

Added in version 3.1: LZMA (7zip) support.

Added in version 3.15: The command now continues adding files to an archive even if some of the files are not readable. This behavior is more consistent with the classic `tar` tool. The command now also parses all flags, and if an invalid flag was provided, a warning is issued.

time<command>[<args>...][¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-E-arg-time "Link to this definition")
Run `<command>` and display elapsed time (including overhead of CMake frontend).

Added in version 3.5: The command now properly passes arguments with spaces or special characters through to the child process. This may break scripts that worked around the bug with their own extra quoting or escaping.

touch<file>...[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-E-arg-touch "Link to this definition")
Creates `<file>` if file do not exist. If `<file>` exists, it is changing `<file>` access and modification times.

touch_nocreate<file>...[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-E-arg-touch_nocreate "Link to this definition")
Touch a file if it exists but do not create it. If a file does not exist it will be silently ignored.

true[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-E-arg-true "Link to this definition")

Added in version 3.16.

Do nothing, with an exit code of 0.

### Windows-specific Command-Line Tools[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#windows-specific-command-line-tools "Link to this heading")

The following `cmake -E` commands are available only on Windows:

delete_regv<key>[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-E-arg-delete_regv "Link to this definition")
Delete Windows registry value.

env_vs8_wince<sdkname>[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-E-arg-env_vs8_wince "Link to this definition")

Added in version 3.2.

Displays a batch file which sets the environment for the provided Windows CE SDK installed in VS2005.

env_vs9_wince<sdkname>[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-E-arg-env_vs9_wince "Link to this definition")

Added in version 3.2.

Displays a batch file which sets the environment for the provided Windows CE SDK installed in VS2008.

write_regv<key><value>[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-E-arg-write_regv "Link to this definition")
Write Windows registry value.

Run the Find-Package Tool[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#run-the-find-package-tool "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------

CMake provides a pkg-config like helper for Makefile-based projects:

cmake --find-package [<options>]

Note

This mode is not well-supported due to some technical limitations. It is kept for compatibility but should not be used in new projects.

--find-package[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-find-package-find-package "Link to this definition")
It searches a package using the [`find_package()`](https://cmake.org/cmake/help/latest/command/find_package.html#command:find_package "find_package") command and prints the resulting flags to stdout. This can be used instead of pkg-config to find installed libraries in plain Makefile-based projects or in Autoconf-based projects, using auxiliary macros installed in `share/aclocal/cmake.m4` on the system.

When using this option, the following variables are expected:

`NAME`
Name of the package as called in `find_package(<PackageName>)`.

`COMPILER_ID`
[`Compiler ID`](https://cmake.org/cmake/help/latest/variable/CMAKE_LANG_COMPILER_ID.html#variable:CMAKE_%3CLANG%3E_COMPILER_ID "CMAKE_<LANG>_COMPILER_ID") used for searching the package, i.e. GNU/Intel/Clang/MSVC, etc.

`LANGUAGE`
Language used for searching the package, i.e. C/CXX/Fortran/ASM, etc.

`MODE`
The package search mode. Value can be one of:

`EXIST`
Only checks for existence of the given package.

`COMPILE`
Prints the flags needed for compiling an object file which uses the given package.

`LINK`
Prints the flags needed for linking when using the given package.

`SILENT`
(Optional) If TRUE, find result message is not printed.

For example:

cmake --find-package -DNAME=CURL -DCOMPILER_ID=GNU -DLANGUAGE=C -DMODE=LINK

Run a Workflow Preset[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#run-a-workflow-preset "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------

Added in version 3.25.

[`CMake Presets`](https://cmake.org/cmake/help/latest/manual/cmake-presets.7.html#manual:cmake-presets(7) "cmake-presets(7)") provides a way to execute multiple build steps in order:

cmake --workflow <options>

The options are:

--workflow[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-workflow "Link to this definition")
Select a [Workflow Preset](https://cmake.org/cmake/help/latest/manual/cmake-presets.7.html#workflow-preset) using one of the following options.

--preset<preset>,--preset=<preset>[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-workflow-preset "Link to this definition")
Use a workflow preset to specify a workflow. The project binary directory is inferred from the initial configure preset. The current working directory must contain CMake preset files. See [`preset`](https://cmake.org/cmake/help/latest/manual/cmake-presets.7.html#manual:cmake-presets(7) "cmake-presets(7)") for more details.

Changed in version 3.31: When following immediately after the `--workflow` option, the `--preset` argument can be omitted and just the `<preset>` name can be given. This means the following syntax is valid:

$ cmake --workflow my-preset

--list-presets[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-workflow-list-presets "Link to this definition")
Lists the available workflow presets. The current working directory must contain CMake preset files.

--fresh[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-workflow-fresh "Link to this definition")
Perform a fresh configuration of the build tree, which has the same effect as [`cmake --fresh`](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-fresh).

View Help[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#view-help "Link to this heading")
------------------------------------------------------------------------------------------------------

To print selected pages from the CMake documentation, use

cmake --help[-<topic>]

with one of the following options:

-version[=json-v1][<file>],--version[=json-v1][<file>],/V[=json-v1][<file>],/version[=json-v1][<file>][¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-version "Link to this definition")
Show program name/version banner and exit. If `json-v1` is specified, print extended version information in JSON format. The JSON output contains the versions for the CMake and its dependencies. The output is printed to a named `<file>` if given.

The JSON output format is described in machine-readable form by [`this JSON schema`](https://cmake.org/cmake/help/latest/_downloads/8841c8b524587a9aee211c0ac198f604/version-schema.json).

-h,-H,--help,-help,-usage,/?[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-h "Link to this definition")
Print usage information and exit.

Usage describes the basic command line interface and its options.

--help<keyword>[<file>][¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-1 "Link to this definition")
Print help for one CMake keyword.

`<keyword>` can be a property, variable, command, policy, generator or module.

The relevant manual entry for `<keyword>` is printed in a human-readable text format. The output is printed to a named `<file>` if given.

Changed in version 3.28: Prior to CMake 3.28, this option supported command names only.

--help-full[<file>][¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-help-full "Link to this definition")
Print all help manuals and exit.

All manuals are printed in a human-readable text format. The output is printed to a named `<file>` if given.

--help-manual<man>[<file>][¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-help-manual "Link to this definition")
Print one help manual and exit.

The specified manual is printed in a human-readable text format. The output is printed to a named `<file>` if given.

--help-manual-list[<file>][¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-help-manual-list "Link to this definition")
List help manuals available and exit.

The list contains all manuals for which help may be obtained by using the `--help-manual` option followed by a manual name. The output is printed to a named `<file>` if given.

--help-command<cmd>[<file>][¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-help-command "Link to this definition")
Print help for one command and exit.

The [`cmake-commands(7)`](https://cmake.org/cmake/help/latest/manual/cmake-commands.7.html#manual:cmake-commands(7) "cmake-commands(7)") manual entry for `<cmd>` is printed in a human-readable text format. The output is printed to a named `<file>` if given.

--help-command-list[<file>][¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-help-command-list "Link to this definition")
List commands with help available and exit.

The list contains all commands for which help may be obtained by using the `--help-command` option followed by a command name. The output is printed to a named `<file>` if given.

--help-commands[<file>][¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-help-commands "Link to this definition")
Print cmake-commands manual and exit.

The [`cmake-commands(7)`](https://cmake.org/cmake/help/latest/manual/cmake-commands.7.html#manual:cmake-commands(7) "cmake-commands(7)") manual is printed in a human-readable text format. The output is printed to a named `<file>` if given.

--help-module<mod>[<file>][¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-help-module "Link to this definition")
Print help for one module and exit.

The [`cmake-modules(7)`](https://cmake.org/cmake/help/latest/manual/cmake-modules.7.html#manual:cmake-modules(7) "cmake-modules(7)") manual entry for `<mod>` is printed in a human-readable text format. The output is printed to a named `<file>` if given.

--help-module-list[<file>][¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-help-module-list "Link to this definition")
List modules with help available and exit.

The list contains all modules for which help may be obtained by using the `--help-module` option followed by a module name. The output is printed to a named `<file>` if given.

--help-modules[<file>][¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-help-modules "Link to this definition")
Print cmake-modules manual and exit.

The [`cmake-modules(7)`](https://cmake.org/cmake/help/latest/manual/cmake-modules.7.html#manual:cmake-modules(7) "cmake-modules(7)") manual is printed in a human-readable text format. The output is printed to a named `<file>` if given.

--help-policy<cmp>[<file>][¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-help-policy "Link to this definition")
Print help for one policy and exit.

The [`cmake-policies(7)`](https://cmake.org/cmake/help/latest/manual/cmake-policies.7.html#manual:cmake-policies(7) "cmake-policies(7)") manual entry for `<cmp>` is printed in a human-readable text format. The output is printed to a named `<file>` if given.

--help-policy-list[<file>][¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-help-policy-list "Link to this definition")
List policies with help available and exit.

The list contains all policies for which help may be obtained by using the `--help-policy` option followed by a policy name. The output is printed to a named `<file>` if given.

--help-policies[<file>][¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-help-policies "Link to this definition")
Print cmake-policies manual and exit.

The [`cmake-policies(7)`](https://cmake.org/cmake/help/latest/manual/cmake-policies.7.html#manual:cmake-policies(7) "cmake-policies(7)") manual is printed in a human-readable text format. The output is printed to a named `<file>` if given.

--help-property<prop>[<file>][¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-help-property "Link to this definition")
Print help for one property and exit.

The [`cmake-properties(7)`](https://cmake.org/cmake/help/latest/manual/cmake-properties.7.html#manual:cmake-properties(7) "cmake-properties(7)") manual entries for `<prop>` are printed in a human-readable text format. The output is printed to a named `<file>` if given.

--help-property-list[<file>][¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-help-property-list "Link to this definition")
List properties with help available and exit.

The list contains all properties for which help may be obtained by using the `--help-property` option followed by a property name. The output is printed to a named `<file>` if given.

--help-properties[<file>][¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-help-properties "Link to this definition")
Print cmake-properties manual and exit.

The [`cmake-properties(7)`](https://cmake.org/cmake/help/latest/manual/cmake-properties.7.html#manual:cmake-properties(7) "cmake-properties(7)") manual is printed in a human-readable text format. The output is printed to a named `<file>` if given.

--help-variable<var>[<file>][¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-help-variable "Link to this definition")
Print help for one variable and exit.

The [`cmake-variables(7)`](https://cmake.org/cmake/help/latest/manual/cmake-variables.7.html#manual:cmake-variables(7) "cmake-variables(7)") manual entry for `<var>` is printed in a human-readable text format. The output is printed to a named `<file>` if given.

--help-variable-list[<file>][¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-help-variable-list "Link to this definition")
List variables with help available and exit.

The list contains all variables for which help may be obtained by using the `--help-variable` option followed by a variable name. The output is printed to a named `<file>` if given.

--help-variables[<file>][¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-help-variables "Link to this definition")
Print cmake-variables manual and exit.

The [`cmake-variables(7)`](https://cmake.org/cmake/help/latest/manual/cmake-variables.7.html#manual:cmake-variables(7) "cmake-variables(7)") manual is printed in a human-readable text format. The output is printed to a named `<file>` if given.

To view the presets available for a project, use

cmake <source-dir> --list-presets

Return Value (Exit Code)[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#return-value-exit-code "Link to this heading")
----------------------------------------------------------------------------------------------------------------------------------

Upon regular termination, the **cmake** executable returns the exit code `0`.

If termination is caused by the command [`message(FATAL_ERROR)`](https://cmake.org/cmake/help/latest/command/message.html#command:message "message(fatal_error)"), or another error condition, then a non-zero exit code is returned.

See Also[¶](https://cmake.org/cmake/help/latest/manual/cmake.1.html#see-also "Link to this heading")
----------------------------------------------------------------------------------------------------

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

### Table of Contents

*   [cmake(1)](https://cmake.org/cmake/help/latest/manual/cmake.1.html#)
    *   [Synopsis](https://cmake.org/cmake/help/latest/manual/cmake.1.html#synopsis)
    *   [Description](https://cmake.org/cmake/help/latest/manual/cmake.1.html#description)
    *   [Introduction to CMake Buildsystems](https://cmake.org/cmake/help/latest/manual/cmake.1.html#introduction-to-cmake-buildsystems)
    *   [Generate a Project Buildsystem](https://cmake.org/cmake/help/latest/manual/cmake.1.html#generate-a-project-buildsystem)
        *   [Options](https://cmake.org/cmake/help/latest/manual/cmake.1.html#options)

    *   [Build a Project](https://cmake.org/cmake/help/latest/manual/cmake.1.html#build-a-project)
        *   [Generator-Specific Build Tool Behavior](https://cmake.org/cmake/help/latest/manual/cmake.1.html#generator-specific-build-tool-behavior)

    *   [Install a Project](https://cmake.org/cmake/help/latest/manual/cmake.1.html#install-a-project)
    *   [Open a Project](https://cmake.org/cmake/help/latest/manual/cmake.1.html#open-a-project)
    *   [Run a Script](https://cmake.org/cmake/help/latest/manual/cmake.1.html#run-a-script)
    *   [Run a Command-Line Tool](https://cmake.org/cmake/help/latest/manual/cmake.1.html#run-a-command-line-tool)
        *   [Windows-specific Command-Line Tools](https://cmake.org/cmake/help/latest/manual/cmake.1.html#windows-specific-command-line-tools)

    *   [Run the Find-Package Tool](https://cmake.org/cmake/help/latest/manual/cmake.1.html#run-the-find-package-tool)
    *   [Run a Workflow Preset](https://cmake.org/cmake/help/latest/manual/cmake.1.html#run-a-workflow-preset)
    *   [View Help](https://cmake.org/cmake/help/latest/manual/cmake.1.html#view-help)
    *   [Return Value (Exit Code)](https://cmake.org/cmake/help/latest/manual/cmake.1.html#return-value-exit-code)
    *   [See Also](https://cmake.org/cmake/help/latest/manual/cmake.1.html#see-also)

#### Previous topic

[Introduction](https://cmake.org/cmake/help/latest/index.html "previous chapter")

#### Next topic

[ctest(1)](https://cmake.org/cmake/help/latest/manual/ctest.1.html "next chapter")

### This Page

*   [Show Source](https://cmake.org/cmake/help/latest/_sources/manual/cmake.1.rst.txt)

### Quick search

### Navigation

*   [index](https://cmake.org/cmake/help/latest/genindex.html "General Index")
*   [next](https://cmake.org/cmake/help/latest/manual/ctest.1.html "ctest(1)") |
*   [previous](https://cmake.org/cmake/help/latest/index.html "Introduction") |

*   ![Image 2](https://cmake.org/cmake/help/latest/_static/cmake-logo-16.png)[CMake](https://cmake.org/)4.3.0-rc3 »
*   [Documentation](https://cmake.org/cmake/help/latest/index.html) » 
*   [cmake(1)](https://cmake.org/cmake/help/latest/manual/cmake.1.html)

 © Copyright 2000-2026 Kitware, Inc. and Contributors. Created using [Sphinx](https://www.sphinx-doc.org/) 8.2.3.
