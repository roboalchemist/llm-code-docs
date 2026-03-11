# Source: https://cmake.org/cmake/help/latest/guide/importing-exporting/index.html

Title: Importing and Exporting Guide — CMake 4.3.0-rc3 Documentation

URL Source: https://cmake.org/cmake/help/latest/guide/importing-exporting/index.html

Published Time: Tue, 10 Mar 2026 19:18:15 GMT

Markdown Content:
Importing and Exporting Guide — CMake 4.3.0-rc3 Documentation
===============
- [x] 

### Navigation

*   [index](https://cmake.org/cmake/help/latest/genindex.html "General Index")
*   [next](https://cmake.org/cmake/help/latest/guide/ide-integration/index.html "IDE Integration Guide") |
*   [previous](https://cmake.org/cmake/help/latest/guide/using-dependencies/index.html "Using Dependencies Guide") |

*   ![Image 1](https://cmake.org/cmake/help/latest/_static/cmake-logo-16.png)[CMake](https://cmake.org/)4.3.0-rc3 »
*   [Documentation](https://cmake.org/cmake/help/latest/index.html) » 
*   [Importing and Exporting Guide](https://cmake.org/cmake/help/latest/guide/importing-exporting/index.html)

[Importing and Exporting Guide](https://cmake.org/cmake/help/latest/guide/importing-exporting/index.html#id1)[¶](https://cmake.org/cmake/help/latest/guide/importing-exporting/index.html#importing-and-exporting-guide "Link to this heading")
===============================================================================================================================================================================================================================================

Contents

*   [Importing and Exporting Guide](https://cmake.org/cmake/help/latest/guide/importing-exporting/index.html#importing-and-exporting-guide)

    *   [Introduction](https://cmake.org/cmake/help/latest/guide/importing-exporting/index.html#introduction)

    *   [Importing Targets](https://cmake.org/cmake/help/latest/guide/importing-exporting/index.html#importing-targets)

        *   [Importing Executables](https://cmake.org/cmake/help/latest/guide/importing-exporting/index.html#importing-executables)

        *   [Importing Libraries](https://cmake.org/cmake/help/latest/guide/importing-exporting/index.html#importing-libraries)

    *   [Exporting Targets](https://cmake.org/cmake/help/latest/guide/importing-exporting/index.html#exporting-targets)

        *   [Creating Packages](https://cmake.org/cmake/help/latest/guide/importing-exporting/index.html#creating-packages)

            *   [Creating a Package Configuration File](https://cmake.org/cmake/help/latest/guide/importing-exporting/index.html#creating-a-package-configuration-file)

            *   [Creating a Package Version File](https://cmake.org/cmake/help/latest/guide/importing-exporting/index.html#creating-a-package-version-file)

        *   [Exporting Targets from the Build Tree](https://cmake.org/cmake/help/latest/guide/importing-exporting/index.html#exporting-targets-from-the-build-tree)

        *   [Building and Installing a Package](https://cmake.org/cmake/help/latest/guide/importing-exporting/index.html#building-and-installing-a-package)

    *   [Creating Relocatable Packages](https://cmake.org/cmake/help/latest/guide/importing-exporting/index.html#creating-relocatable-packages)

    *   [Using the Package Configuration File](https://cmake.org/cmake/help/latest/guide/importing-exporting/index.html#using-the-package-configuration-file)

    *   [Adding Components](https://cmake.org/cmake/help/latest/guide/importing-exporting/index.html#adding-components)

[Introduction](https://cmake.org/cmake/help/latest/guide/importing-exporting/index.html#id2)[¶](https://cmake.org/cmake/help/latest/guide/importing-exporting/index.html#introduction "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

In this guide, we will present the concept of [`IMPORTED`](https://cmake.org/cmake/help/latest/prop_tgt/IMPORTED.html#prop_tgt:IMPORTED "IMPORTED") targets and demonstrate how to import existing executable or library files from disk into a CMake project. We will then show how CMake supports exporting targets from one CMake-based project and importing them into another. Finally, we will demonstrate how to package a project with a configuration file to allow for easy integration into other CMake projects. This guide and the complete example source code can be found in the `Help/guide/importing-exporting` directory of the CMake source code tree.

[Importing Targets](https://cmake.org/cmake/help/latest/guide/importing-exporting/index.html#id3)[¶](https://cmake.org/cmake/help/latest/guide/importing-exporting/index.html#importing-targets "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[`IMPORTED`](https://cmake.org/cmake/help/latest/prop_tgt/IMPORTED.html#prop_tgt:IMPORTED "IMPORTED") targets are used to convert files outside of a CMake project into logical targets inside of the project. [`IMPORTED`](https://cmake.org/cmake/help/latest/prop_tgt/IMPORTED.html#prop_tgt:IMPORTED "IMPORTED") targets are created using the `IMPORTED` option of the [`add_executable()`](https://cmake.org/cmake/help/latest/command/add_executable.html#command:add_executable "add_executable") and [`add_library()`](https://cmake.org/cmake/help/latest/command/add_library.html#command:add_library "add_library") commands. No build files are generated for [`IMPORTED`](https://cmake.org/cmake/help/latest/prop_tgt/IMPORTED.html#prop_tgt:IMPORTED "IMPORTED") targets. Once imported, [`IMPORTED`](https://cmake.org/cmake/help/latest/prop_tgt/IMPORTED.html#prop_tgt:IMPORTED "IMPORTED") targets may be referenced like any other target within the project and provide a convenient, flexible reference to outside executables and libraries.

By default, the [`IMPORTED`](https://cmake.org/cmake/help/latest/prop_tgt/IMPORTED.html#prop_tgt:IMPORTED "IMPORTED") target name has scope in the directory in which it is created and below. We can use the `GLOBAL` option to extended visibility so that the target is accessible globally in the build system.

Details about the [`IMPORTED`](https://cmake.org/cmake/help/latest/prop_tgt/IMPORTED.html#prop_tgt:IMPORTED "IMPORTED") target are specified by setting properties whose names begin in `IMPORTED_` and `INTERFACE_`. For example, [`IMPORTED_LOCATION`](https://cmake.org/cmake/help/latest/prop_tgt/IMPORTED_LOCATION.html#prop_tgt:IMPORTED_LOCATION "IMPORTED_LOCATION") contains the full path to the target on disk.

### [Importing Executables](https://cmake.org/cmake/help/latest/guide/importing-exporting/index.html#id4)[¶](https://cmake.org/cmake/help/latest/guide/importing-exporting/index.html#importing-executables "Link to this heading")

To start, we will walk through a simple example that creates an [`IMPORTED`](https://cmake.org/cmake/help/latest/prop_tgt/IMPORTED.html#prop_tgt:IMPORTED "IMPORTED") executable target and then references it from the [`add_custom_command()`](https://cmake.org/cmake/help/latest/command/add_custom_command.html#command:add_custom_command "add_custom_command") command.

We'll need to do some setup to get started. We want to create an executable that when run creates a basic `main.cc` file in the current directory. The details of this project are not important. Navigate to `Help/guide/importing-exporting/MyExe`, create a build directory, run [`cmake`](https://cmake.org/cmake/help/latest/manual/cmake.1.html#manual:cmake(1) "cmake(1)") and build and install the project.

$ cd Help/guide/importing-exporting/MyExe
$ mkdir build
$ cd build
$ cmake ..
$ cmake --build .
$ cmake --install . --prefix <install location>
$ <install location>/myexe
$ ls
[...] main.cc [...]

Now we can import this executable into another CMake project. The source code for this section is available in `Help/guide/importing-exporting/Importing`. In the CMakeLists file, use the [`add_executable()`](https://cmake.org/cmake/help/latest/command/add_executable.html#command:add_executable "add_executable") command to create a new target called `myexe`. Use the `IMPORTED` option to tell CMake that this target references an executable file located outside of the project. No rules will be generated to build it and the [`IMPORTED`](https://cmake.org/cmake/help/latest/prop_tgt/IMPORTED.html#prop_tgt:IMPORTED "IMPORTED") target property will be set to `true`.

add_executable(myexe IMPORTED)

Next, set the [`IMPORTED_LOCATION`](https://cmake.org/cmake/help/latest/prop_tgt/IMPORTED_LOCATION.html#prop_tgt:IMPORTED_LOCATION "IMPORTED_LOCATION") property of the target using the [`set_property()`](https://cmake.org/cmake/help/latest/command/set_property.html#command:set_property "set_property") command. This will tell CMake the location of the target on disk. The location may need to be adjusted to the `<install location>` specified in the previous step.

set_property(TARGET myexe PROPERTY
 IMPORTED_LOCATION "../InstallMyExe/bin/myexe")

We can now reference this [`IMPORTED`](https://cmake.org/cmake/help/latest/prop_tgt/IMPORTED.html#prop_tgt:IMPORTED "IMPORTED") target just like any target built within the project. In this instance, let's imagine that we want to use the generated source file in our project. Use the [`IMPORTED`](https://cmake.org/cmake/help/latest/prop_tgt/IMPORTED.html#prop_tgt:IMPORTED "IMPORTED") target in the [`add_custom_command()`](https://cmake.org/cmake/help/latest/command/add_custom_command.html#command:add_custom_command "add_custom_command") command:

add_custom_command(OUTPUT main.cc COMMAND myexe)

As `COMMAND` specifies an executable target name, it will automatically be replaced by the location of the executable given by the [`IMPORTED_LOCATION`](https://cmake.org/cmake/help/latest/prop_tgt/IMPORTED_LOCATION.html#prop_tgt:IMPORTED_LOCATION "IMPORTED_LOCATION") property above.

Finally, use the output from [`add_custom_command()`](https://cmake.org/cmake/help/latest/command/add_custom_command.html#command:add_custom_command "add_custom_command"):

add_executable(mynewexe main.cc)

### [Importing Libraries](https://cmake.org/cmake/help/latest/guide/importing-exporting/index.html#id5)[¶](https://cmake.org/cmake/help/latest/guide/importing-exporting/index.html#importing-libraries "Link to this heading")

In a similar manner, libraries from other projects may be accessed through [`IMPORTED`](https://cmake.org/cmake/help/latest/prop_tgt/IMPORTED.html#prop_tgt:IMPORTED "IMPORTED") targets.

Note: The full source code for the examples in this section is not provided and is left as an exercise for the reader.

In the CMakeLists file, add an [`IMPORTED`](https://cmake.org/cmake/help/latest/prop_tgt/IMPORTED.html#prop_tgt:IMPORTED "IMPORTED") library and specify its location on disk:

add_library(foo STATIC IMPORTED)
set_property(TARGET foo PROPERTY
 IMPORTED_LOCATION "/path/to/libfoo.a")

Then use the [`IMPORTED`](https://cmake.org/cmake/help/latest/prop_tgt/IMPORTED.html#prop_tgt:IMPORTED "IMPORTED") library inside of our project:

add_executable(myexe src1.c src2.c)
target_link_libraries(myexe PRIVATE foo)

On Windows, a .dll and its .lib import library may be imported together:

add_library(bar SHARED IMPORTED)
set_property(TARGET bar PROPERTY
 IMPORTED_LOCATION "c:/path/to/bar.dll")
set_property(TARGET bar PROPERTY
 IMPORTED_IMPLIB "c:/path/to/bar.lib")
add_executable(myexe src1.c src2.c)
target_link_libraries(myexe PRIVATE bar)

A library with multiple configurations may be imported with a single target:

find_library(math_REL NAMES m)
find_library(math_DBG NAMES md)
add_library(math STATIC IMPORTED GLOBAL)
set_target_properties(math PROPERTIES
 IMPORTED_LOCATION "${math_REL}"
 IMPORTED_LOCATION_DEBUG "${math_DBG}"
 IMPORTED_CONFIGURATIONS "RELEASE;DEBUG"
)
add_executable(myexe src1.c src2.c)
target_link_libraries(myexe PRIVATE math)

The generated build system will link `myexe` to `m.lib` when built in the release configuration, and `md.lib` when built in the debug configuration.

[Exporting Targets](https://cmake.org/cmake/help/latest/guide/importing-exporting/index.html#id6)[¶](https://cmake.org/cmake/help/latest/guide/importing-exporting/index.html#exporting-targets "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

While [`IMPORTED`](https://cmake.org/cmake/help/latest/prop_tgt/IMPORTED.html#prop_tgt:IMPORTED "IMPORTED") targets on their own are useful, they still require that the project that imports them knows the locations of the target files on disk. The real power of [`IMPORTED`](https://cmake.org/cmake/help/latest/prop_tgt/IMPORTED.html#prop_tgt:IMPORTED "IMPORTED") targets is when the project providing the target files also provides a CMake file to help import them. A project can be setup to produce the necessary information so that it can easily be used by other CMake projects be it from a build directory, a local install or when packaged.

In the remaining sections, we will walk through a set of example projects step-by-step. The first project will create and install a library and corresponding CMake configuration and package files. The second project will use the generated package.

Let's start by looking at the `MathFunctions` project in the `Help/guide/importing-exporting/MathFunctions` directory. Here we have a header file `MathFunctions.h` that declares a `sqrt` function:

#pragma once

namespace MathFunctions {
double sqrt(double x);
}

And a corresponding source file `MathFunctions.cxx`:

#include "MathFunctions.h"

#include <cmath>

namespace MathFunctions {
double sqrt(double x)
{
 return std::sqrt(x);
}
}

Don't worry too much about the specifics of the C++ files, they are just meant to be a simple example that will compile and run on many build systems.

Now we can create a `CMakeLists.txt` file for the `MathFunctions` project. Start by specifying the [`cmake_minimum_required()`](https://cmake.org/cmake/help/latest/command/cmake_minimum_required.html#command:cmake_minimum_required "cmake_minimum_required") version and [`project()`](https://cmake.org/cmake/help/latest/command/project.html#command:project "project") name:

cmake_minimum_required(VERSION 3.15)
project(MathFunctions)

# make cache variables for install destinations
include(GNUInstallDirs)

# specify the C++ standard
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED True)

The [`GNUInstallDirs`](https://cmake.org/cmake/help/latest/module/GNUInstallDirs.html#module:GNUInstallDirs "GNUInstallDirs") module is included in order to provide the project with the flexibility to install into different platform layouts by making the directories available as cache variables.

Create a library called `MathFunctions` with the [`add_library()`](https://cmake.org/cmake/help/latest/command/add_library.html#command:add_library "add_library") command:

add_library(MathFunctions STATIC MathFunctions.cxx)

And then use the [`target_include_directories()`](https://cmake.org/cmake/help/latest/command/target_include_directories.html#command:target_include_directories "target_include_directories") command to specify the include directories for the target:

target_include_directories(MathFunctions
 PUBLIC
 "$<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}>"
 "$<INSTALL_INTERFACE:${CMAKE_INSTALL_INCLUDEDIR}>"
)

We need to tell CMake that we want to use different include directories depending on if we're building the library or using it from an installed location. If we don't do this, when CMake creates the export information it will export a path that is specific to the current build directory and will not be valid for other projects. We can use [`generator expressions`](https://cmake.org/cmake/help/latest/manual/cmake-generator-expressions.7.html#manual:cmake-generator-expressions(7) "cmake-generator-expressions(7)") to specify that if we're building the library include the current source directory. Otherwise, when installed, include the `include` directory. See the [Creating Relocatable Packages](https://cmake.org/cmake/help/latest/guide/importing-exporting/index.html#creating-relocatable-packages) section for more details.

The [`install(TARGETS)`](https://cmake.org/cmake/help/latest/command/install.html#targets "install(targets)") and [`install(EXPORT)`](https://cmake.org/cmake/help/latest/command/install.html#export "install(export)") commands work together to install both targets (a library in our case) and a CMake file designed to make it easy to import the targets into another CMake project.

First, in the [`install(TARGETS)`](https://cmake.org/cmake/help/latest/command/install.html#targets "install(targets)") command we will specify the target, the `EXPORT` name and the destinations that tell CMake where to install the targets.

install(TARGETS MathFunctions
 EXPORT MathFunctionsTargets
 LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
 ARCHIVE DESTINATION ${CMAKE_INSTALL_LIBDIR}
 RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR}
 INCLUDES DESTINATION ${CMAKE_INSTALL_INCLUDEDIR}
)

Here, the `EXPORT` option tells CMake to create an export called `MathFunctionsTargets`. The generated [`IMPORTED`](https://cmake.org/cmake/help/latest/prop_tgt/IMPORTED.html#prop_tgt:IMPORTED "IMPORTED") targets have appropriate properties set to define their [usage requirements](https://cmake.org/cmake/help/latest/manual/cmake-buildsystem.7.html#target-usage-requirements), such as [`INTERFACE_INCLUDE_DIRECTORIES`](https://cmake.org/cmake/help/latest/prop_tgt/INTERFACE_INCLUDE_DIRECTORIES.html#prop_tgt:INTERFACE_INCLUDE_DIRECTORIES "INTERFACE_INCLUDE_DIRECTORIES"), [`INTERFACE_COMPILE_DEFINITIONS`](https://cmake.org/cmake/help/latest/prop_tgt/INTERFACE_COMPILE_DEFINITIONS.html#prop_tgt:INTERFACE_COMPILE_DEFINITIONS "INTERFACE_COMPILE_DEFINITIONS") and other relevant built-in `INTERFACE_` properties. The `INTERFACE` variant of user-defined properties listed in [`COMPATIBLE_INTERFACE_STRING`](https://cmake.org/cmake/help/latest/prop_tgt/COMPATIBLE_INTERFACE_STRING.html#prop_tgt:COMPATIBLE_INTERFACE_STRING "COMPATIBLE_INTERFACE_STRING") and other [Compatible Interface Properties](https://cmake.org/cmake/help/latest/manual/cmake-buildsystem.7.html#compatible-interface-properties) are also propagated to the generated [`IMPORTED`](https://cmake.org/cmake/help/latest/prop_tgt/IMPORTED.html#prop_tgt:IMPORTED "IMPORTED") targets. For example, in this case, the [`IMPORTED`](https://cmake.org/cmake/help/latest/prop_tgt/IMPORTED.html#prop_tgt:IMPORTED "IMPORTED") target will have its [`INTERFACE_INCLUDE_DIRECTORIES`](https://cmake.org/cmake/help/latest/prop_tgt/INTERFACE_INCLUDE_DIRECTORIES.html#prop_tgt:INTERFACE_INCLUDE_DIRECTORIES "INTERFACE_INCLUDE_DIRECTORIES") property populated with the directory specified by the `INCLUDES DESTINATION` property. As a relative path was given, it is treated as relative to the [`CMAKE_INSTALL_PREFIX`](https://cmake.org/cmake/help/latest/variable/CMAKE_INSTALL_PREFIX.html#variable:CMAKE_INSTALL_PREFIX "CMAKE_INSTALL_PREFIX").

Note, we have _not_ asked CMake to install the export yet.

We don't want to forget to install the `MathFunctions.h` header file with the [`install(FILES)`](https://cmake.org/cmake/help/latest/command/install.html#files "install(files)") command. The header file should be installed to the `include` directory, as specified by the [`target_include_directories()`](https://cmake.org/cmake/help/latest/command/target_include_directories.html#command:target_include_directories "target_include_directories") command above.

install(FILES MathFunctions.h DESTINATION ${CMAKE_INSTALL_INCLUDEDIR})

Now that the `MathFunctions` library and header file are installed, we also need to explicitly install the `MathFunctionsTargets` export details. Use the [`install(EXPORT)`](https://cmake.org/cmake/help/latest/command/install.html#export "install(export)") command to export the targets in `MathFunctionsTargets`, as defined by the [`install(TARGETS)`](https://cmake.org/cmake/help/latest/command/install.html#targets "install(targets)") command.

install(EXPORT MathFunctionsTargets
 FILE MathFunctionsTargets.cmake
 NAMESPACE MathFunctions::
 DESTINATION ${CMAKE_INSTALL_LIBDIR}/cmake/MathFunctions
)

This command generates the `MathFunctionsTargets.cmake` file and arranges to install it to `${CMAKE_INSTALL_LIBDIR}/cmake/MathFunctions`. The file contains code suitable for use by downstreams to import all targets listed in the install command from the installation tree.

The `NAMESPACE` option will prepend `MathFunctions::` to the target names as they are written to the export file. This convention of double-colons gives CMake a hint that the name is an [`IMPORTED`](https://cmake.org/cmake/help/latest/prop_tgt/IMPORTED.html#prop_tgt:IMPORTED "IMPORTED") target when it is used by downstream projects. This way, CMake can issue a diagnostic message if the package providing it was not found.

The generated export file contains code that creates an [`IMPORTED`](https://cmake.org/cmake/help/latest/prop_tgt/IMPORTED.html#prop_tgt:IMPORTED "IMPORTED") library.

# Create imported target MathFunctions::MathFunctions
add_library(MathFunctions::MathFunctions STATIC IMPORTED)

set_target_properties(MathFunctions::MathFunctions PROPERTIES
 INTERFACE_INCLUDE_DIRECTORIES "${_IMPORT_PREFIX}/include"
)

This code is very similar to the example we created by hand in the [Importing Libraries](https://cmake.org/cmake/help/latest/guide/importing-exporting/index.html#importing-libraries) section. Note that `${_IMPORT_PREFIX}` is computed relative to the file location.

An outside project may load this file with the [`include()`](https://cmake.org/cmake/help/latest/command/include.html#command:include "include") command and reference the `MathFunctions` library from the installation tree as if it were built in its own tree. For example:

1 include(GNUInstallDirs)
2 include(${INSTALL_PREFIX}/${CMAKE_INSTALL_LIBDIR}/cmake/MathFunctions/MathFunctionTargets.cmake)
3 add_executable(myexe src1.c src2.c)
4 target_link_libraries(myexe PRIVATE MathFunctions::MathFunctions)

Line 2 loads the target CMake file. Although we only exported a single target, this file may import any number of targets. Their locations are computed relative to the file location so that the install tree may be easily moved. Line 4 references the imported `MathFunctions` library. The resulting build system will link to the library from its installed location.

Executables may also be exported and imported using the same process.

Any number of target installations may be associated with the same export name. Export names are considered global so any directory may contribute a target installation. The [`install(EXPORT)`](https://cmake.org/cmake/help/latest/command/install.html#export "install(export)") command only needs to be called once to install a file that references all targets. Below is an example of how multiple exports may be combined into a single export file, even if they are in different subdirectories of the project.

# A/CMakeLists.txt
add_executable(myexe src1.c)
install(TARGETS myexe DESTINATION lib/myproj
 EXPORT myproj-targets)

# B/CMakeLists.txt
add_library(foo STATIC foo1.c)
install(TARGETS foo DESTINATION lib EXPORTS myproj-targets)

# Top CMakeLists.txt
add_subdirectory (A)
add_subdirectory (B)
install(EXPORT myproj-targets DESTINATION lib/myproj)

### [Creating Packages](https://cmake.org/cmake/help/latest/guide/importing-exporting/index.html#id7)[¶](https://cmake.org/cmake/help/latest/guide/importing-exporting/index.html#creating-packages "Link to this heading")

At this point, the `MathFunctions` project is exporting the target information required to be used by other projects. We can make this project even easier for other projects to use by generating a configuration file so that the CMake [`find_package()`](https://cmake.org/cmake/help/latest/command/find_package.html#command:find_package "find_package") command can find our project.

To start, we will need to make a few additions to the `CMakeLists.txt` file. First, include the [`CMakePackageConfigHelpers`](https://cmake.org/cmake/help/latest/module/CMakePackageConfigHelpers.html#module:CMakePackageConfigHelpers "CMakePackageConfigHelpers") module to get access to some helper functions for creating config files.

include(CMakePackageConfigHelpers)

Then we will create a package configuration file and a package version file.

#### [Creating a Package Configuration File](https://cmake.org/cmake/help/latest/guide/importing-exporting/index.html#id8)[¶](https://cmake.org/cmake/help/latest/guide/importing-exporting/index.html#creating-a-package-configuration-file "Link to this heading")

Use the [`configure_package_config_file()`](https://cmake.org/cmake/help/latest/module/CMakePackageConfigHelpers.html#command:configure_package_config_file "configure_package_config_file") command provided by the [`CMakePackageConfigHelpers`](https://cmake.org/cmake/help/latest/module/CMakePackageConfigHelpers.html#module:CMakePackageConfigHelpers "CMakePackageConfigHelpers") to generate the package configuration file. Note that this command should be used instead of the plain [`configure_file()`](https://cmake.org/cmake/help/latest/command/configure_file.html#command:configure_file "configure_file") command. It helps to ensure that the resulting package is relocatable by avoiding hardcoded paths in the installed configuration file. The path given to `INSTALL_DESTINATION` must be the destination where the `MathFunctionsConfig.cmake` file will be installed. We will examine the contents of the package configuration file in the next section.

configure_package_config_file(${CMAKE_CURRENT_SOURCE_DIR}/Config.cmake.in
 "${CMAKE_CURRENT_BINARY_DIR}/MathFunctionsConfig.cmake"
 INSTALL_DESTINATION ${CMAKE_INSTALL_LIBDIR}/cmake/MathFunctions
)

Install the generated configuration files with the [`install(FILES)`](https://cmake.org/cmake/help/latest/command/install.html#files "install(files)") command. Both `MathFunctionsConfigVersion.cmake` and `MathFunctionsConfig.cmake` are installed to the same location, completing the package.

install(FILES
 "${CMAKE_CURRENT_BINARY_DIR}/MathFunctionsConfig.cmake"
 "${CMAKE_CURRENT_BINARY_DIR}/MathFunctionsConfigVersion.cmake"
 DESTINATION ${CMAKE_INSTALL_LIBDIR}/cmake/MathFunctions
)

Now we need to create the package configuration file itself. In this case, the `Config.cmake.in` file is very simple but sufficient to allow downstreams to use the [`IMPORTED`](https://cmake.org/cmake/help/latest/prop_tgt/IMPORTED.html#prop_tgt:IMPORTED "IMPORTED") targets.

@PACKAGE_INIT@

include("${CMAKE_CURRENT_LIST_DIR}/MathFunctionsTargets.cmake")

check_required_components(MathFunctions)

The first line of the file contains only the string `@PACKAGE_INIT@`. This expands when the file is configured and allows the use of relocatable paths prefixed with `PACKAGE_`. It also provides the `set_and_check()` and `check_required_components()` macros.

The `check_required_components` helper macro ensures that all requested, non-optional components have been found by checking the `<Package>_<Component>_FOUND` variables for all required components. This macro should be called at the end of the package configuration file even if the package does not have any components. This way, CMake can make sure that the downstream project hasn't specified any non-existent components. If `check_required_components` fails, the `<Package>_FOUND` variable is set to FALSE, and the package is considered to be not found.

The `set_and_check()` macro should be used in configuration files instead of the normal `set()` command for setting directories and file locations. If a referenced file or directory does not exist, the macro will fail.

If any macros should be provided by the `MathFunctions` package, they should be in a separate file which is installed to the same location as the `MathFunctionsConfig.cmake` file, and included from there.

**All required dependencies of a package must also be found in the package configuration file.** Let's imagine that we require the `Stats` library in our project. In the CMakeLists file, we would add:

find_package(Stats 2.6.4 REQUIRED)
target_link_libraries(MathFunctions PUBLIC Stats::Types)

As the `Stats::Types` target is a `PUBLIC` dependency of `MathFunctions`, downstreams must also find the `Stats` package and link to the `Stats::Types` library. The `Stats` package should be found in the configuration file to ensure this.

include(CMakeFindDependencyMacro)
find_dependency(Stats 2.6.4)

The `find_dependency` macro from the [`CMakeFindDependencyMacro`](https://cmake.org/cmake/help/latest/module/CMakeFindDependencyMacro.html#module:CMakeFindDependencyMacro "CMakeFindDependencyMacro") module helps by propagating whether the package is `REQUIRED`, or `QUIET`, etc. The `find_dependency` macro also sets `MathFunctions_FOUND` to `False` if the dependency is not found, along with a diagnostic that the `MathFunctions` package cannot be used without the `Stats` package.

**Exercise:** Add a required library to the `MathFunctions` project.

#### [Creating a Package Version File](https://cmake.org/cmake/help/latest/guide/importing-exporting/index.html#id9)[¶](https://cmake.org/cmake/help/latest/guide/importing-exporting/index.html#creating-a-package-version-file "Link to this heading")

The [`CMakePackageConfigHelpers`](https://cmake.org/cmake/help/latest/module/CMakePackageConfigHelpers.html#module:CMakePackageConfigHelpers "CMakePackageConfigHelpers") module provides the [`write_basic_package_version_file()`](https://cmake.org/cmake/help/latest/module/CMakePackageConfigHelpers.html#command:write_basic_package_version_file "write_basic_package_version_file") command for creating a simple package version file. This file is read by CMake when [`find_package()`](https://cmake.org/cmake/help/latest/command/find_package.html#command:find_package "find_package") is called to determine the compatibility with the requested version, and to set some version-specific variables such as `<PackageName>_VERSION`, `<PackageName>_VERSION_MAJOR`, `<PackageName>_VERSION_MINOR`, etc. See [`cmake-packages`](https://cmake.org/cmake/help/latest/manual/cmake-packages.7.html#manual:cmake-packages(7) "cmake-packages(7)") documentation for more details.

set(version 3.4.1)

set_property(TARGET MathFunctions PROPERTY VERSION ${version})
set_property(TARGET MathFunctions PROPERTY SOVERSION 3)
set_property(TARGET MathFunctions PROPERTY
 INTERFACE_MathFunctions_MAJOR_VERSION 3)
set_property(TARGET MathFunctions APPEND PROPERTY
 COMPATIBLE_INTERFACE_STRING MathFunctions_MAJOR_VERSION
)

# generate the version file for the config file
write_basic_package_version_file(
 "${CMAKE_CURRENT_BINARY_DIR}/MathFunctionsConfigVersion.cmake"
 VERSION "${version}"
 COMPATIBILITY AnyNewerVersion
)

In our example, `MathFunctions_MAJOR_VERSION` is defined as a [`COMPATIBLE_INTERFACE_STRING`](https://cmake.org/cmake/help/latest/prop_tgt/COMPATIBLE_INTERFACE_STRING.html#prop_tgt:COMPATIBLE_INTERFACE_STRING "COMPATIBLE_INTERFACE_STRING") which means that it must be compatible among the dependencies of any depender. By setting this custom defined user property in this version and in the next version of `MathFunctions`, [`cmake`](https://cmake.org/cmake/help/latest/manual/cmake.1.html#manual:cmake(1) "cmake(1)") will issue a diagnostic if there is an attempt to use version 3 together with version 4. Packages can choose to employ such a pattern if different major versions of the package are designed to be incompatible.

### [Exporting Targets from the Build Tree](https://cmake.org/cmake/help/latest/guide/importing-exporting/index.html#id10)[¶](https://cmake.org/cmake/help/latest/guide/importing-exporting/index.html#exporting-targets-from-the-build-tree "Link to this heading")

Typically, projects are built and installed before being used by an outside project. However, in some cases, it is desirable to export targets directly from a build tree. The targets may then be used by an outside project that references the build tree with no installation involved. The [`export()`](https://cmake.org/cmake/help/latest/command/export.html#command:export "export") command is used to generate a file exporting targets from a project build tree.

If we want our example project to also be used from a build directory we only have to add the following to `CMakeLists.txt`:

export(EXPORT MathFunctionsTargets
 FILE "${CMAKE_CURRENT_BINARY_DIR}/cmake/MathFunctionsTargets.cmake"
 NAMESPACE MathFunctions::
)

Here we use the [`export()`](https://cmake.org/cmake/help/latest/command/export.html#command:export "export") command to generate the export targets for the build tree. In this case, we'll create a file called `MathFunctionsTargets.cmake` in the `cmake` subdirectory of the build directory. The generated file contains the required code to import the target and may be loaded by an outside project that is aware of the project build tree. This file is specific to the build-tree, and **is not relocatable**.

It is possible to create a suitable package configuration file and package version file to define a package for the build tree which may be used without installation. Consumers of the build tree can simply ensure that the [`CMAKE_PREFIX_PATH`](https://cmake.org/cmake/help/latest/variable/CMAKE_PREFIX_PATH.html#variable:CMAKE_PREFIX_PATH "CMAKE_PREFIX_PATH") contains the build directory, or set the `MathFunctions_DIR` to `<build_dir>/MathFunctions` in the cache.

An example application of this feature is for building an executable on a host platform when cross-compiling. The project containing the executable may be built on the host platform and then the project that is being cross-compiled for another platform may load it.

### [Building and Installing a Package](https://cmake.org/cmake/help/latest/guide/importing-exporting/index.html#id11)[¶](https://cmake.org/cmake/help/latest/guide/importing-exporting/index.html#building-and-installing-a-package "Link to this heading")

At this point, we have generated a relocatable CMake configuration for our project that can be used after the project has been installed. Let's try to build the `MathFunctions` project:

mkdir MathFunctions_build
cd MathFunctions_build
cmake ../MathFunctions
cmake --build .

In the build directory, notice that the file `MathFunctionsTargets.cmake` has been created in the `cmake` subdirectory.

Now install the project:

$ cmake --install . --prefix "/home/myuser/installdir"

[Creating Relocatable Packages](https://cmake.org/cmake/help/latest/guide/importing-exporting/index.html#id12)[¶](https://cmake.org/cmake/help/latest/guide/importing-exporting/index.html#creating-relocatable-packages "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Packages created by [`install(EXPORT)`](https://cmake.org/cmake/help/latest/command/install.html#export "install(export)") are designed to be relocatable, using paths relative to the location of the package itself. They must not reference absolute paths of files on the machine where the package is built that will not exist on the machines where the package may be installed.

When defining the interface of a target for `EXPORT`, keep in mind that the include directories should be specified as relative paths to the [`CMAKE_INSTALL_PREFIX`](https://cmake.org/cmake/help/latest/variable/CMAKE_INSTALL_PREFIX.html#variable:CMAKE_INSTALL_PREFIX "CMAKE_INSTALL_PREFIX") but should not explicitly include the [`CMAKE_INSTALL_PREFIX`](https://cmake.org/cmake/help/latest/variable/CMAKE_INSTALL_PREFIX.html#variable:CMAKE_INSTALL_PREFIX "CMAKE_INSTALL_PREFIX"):

target_include_directories(tgt INTERFACE
 # Wrong, not relocatable:
 $<INSTALL_INTERFACE:${CMAKE_INSTALL_PREFIX}/include/TgtName>
)

target_include_directories(tgt INTERFACE
 # Ok, relocatable:
 $<INSTALL_INTERFACE:include/TgtName>
)

The [`$<INSTALL_PREFIX>`](https://cmake.org/cmake/help/latest/manual/cmake-generator-expressions.7.html#genex:INSTALL_PREFIX "INSTALL_PREFIX") generator expression may be used as a placeholder for the install prefix without resulting in a non-relocatable package. This is necessary if complex generator expressions are used:

target_include_directories(tgt INTERFACE
 # Ok, relocatable:
 $<INSTALL_INTERFACE:$<INSTALL_PREFIX>/include/TgtName>
)

This also applies to paths referencing external dependencies. It is not advisable to populate any properties which may contain paths, such as [`INTERFACE_INCLUDE_DIRECTORIES`](https://cmake.org/cmake/help/latest/prop_tgt/INTERFACE_INCLUDE_DIRECTORIES.html#prop_tgt:INTERFACE_INCLUDE_DIRECTORIES "INTERFACE_INCLUDE_DIRECTORIES") or [`INTERFACE_LINK_LIBRARIES`](https://cmake.org/cmake/help/latest/prop_tgt/INTERFACE_LINK_LIBRARIES.html#prop_tgt:INTERFACE_LINK_LIBRARIES "INTERFACE_LINK_LIBRARIES"), with paths relevant to dependencies. For example, this code may not work well for a relocatable package:

target_link_libraries(MathFunctions INTERFACE
 ${Foo_LIBRARIES} ${Bar_LIBRARIES}
 )
target_include_directories(MathFunctions INTERFACE
 "$<INSTALL_INTERFACE:${Foo_INCLUDE_DIRS};${Bar_INCLUDE_DIRS}>"
 )

The referenced variables may contain the absolute paths to libraries and include directories **as found on the machine the package was made on**. This would create a package with hard-coded paths to dependencies not suitable for relocation.

Ideally such dependencies should be used through their own [IMPORTED targets](https://cmake.org/cmake/help/latest/manual/cmake-buildsystem.7.html#imported-targets) that have their own [`IMPORTED_LOCATION`](https://cmake.org/cmake/help/latest/prop_tgt/IMPORTED_LOCATION.html#prop_tgt:IMPORTED_LOCATION "IMPORTED_LOCATION") and usage requirement properties such as [`INTERFACE_INCLUDE_DIRECTORIES`](https://cmake.org/cmake/help/latest/prop_tgt/INTERFACE_INCLUDE_DIRECTORIES.html#prop_tgt:INTERFACE_INCLUDE_DIRECTORIES "INTERFACE_INCLUDE_DIRECTORIES") populated appropriately. Those imported targets may then be used with the [`target_link_libraries()`](https://cmake.org/cmake/help/latest/command/target_link_libraries.html#command:target_link_libraries "target_link_libraries") command for `MathFunctions`:

target_link_libraries(MathFunctions INTERFACE Foo::Foo Bar::Bar)

With this approach the package references its external dependencies only through the names of [IMPORTED targets](https://cmake.org/cmake/help/latest/manual/cmake-buildsystem.7.html#imported-targets). When a consumer uses the installed package, the consumer will run the appropriate [`find_package()`](https://cmake.org/cmake/help/latest/command/find_package.html#command:find_package "find_package") commands (via the `find_dependency` macro described above) to find the dependencies and populate the imported targets with appropriate paths on their own machine.

[Using the Package Configuration File](https://cmake.org/cmake/help/latest/guide/importing-exporting/index.html#id13)[¶](https://cmake.org/cmake/help/latest/guide/importing-exporting/index.html#using-the-package-configuration-file "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Now we're ready to create a project to use the installed `MathFunctions` library. In this section we will be using source code from `Help\guide\importing-exporting\Downstream`. In this directory, there is a source file called `main.cc` that uses the `MathFunctions` library to calculate the square root of a given number and then prints the results:

// A simple program that outputs the square root of a number
#include <iostream>
#include <string>

#include "MathFunctions.h"

int main(int argc, char* argv[])
{
 if (argc < 2) {
 std::cout << "Usage: " << argv[0] << " number" << std::endl;
 return 1;
 }

 // convert input to double
 double const inputValue = std::stod(argv[1]);

 // calculate square root
 double const sqrt = MathFunctions::sqrt(inputValue);
 std::cout << "The square root of " << inputValue << " is " << sqrt
 << std::endl;

 return 0;
}

As before, we'll start with the [`cmake_minimum_required()`](https://cmake.org/cmake/help/latest/command/cmake_minimum_required.html#command:cmake_minimum_required "cmake_minimum_required") and [`project()`](https://cmake.org/cmake/help/latest/command/project.html#command:project "project") commands in the `CMakeLists.txt` file. For this project, we'll also specify the C++ standard.

cmake_minimum_required(VERSION 3.15)
project(Downstream)

# specify the C++ standard
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED True)

We can use the [`find_package()`](https://cmake.org/cmake/help/latest/command/find_package.html#command:find_package "find_package") command:

find_package(MathFunctions 3.4.1 EXACT)

Create an executable:

add_executable(myexe main.cc)

And link to the `MathFunctions` library:

target_link_libraries(myexe PRIVATE MathFunctions::MathFunctions)

That's it! Now let's try to build the `Downstream` project.

mkdir Downstream_build
cd Downstream_build
cmake ../Downstream
cmake --build .

A warning may have appeared during CMake configuration:

CMake Warning at CMakeLists.txt:4 (find_package):
 By not providing "FindMathFunctions.cmake" in CMAKE_MODULE_PATH this
 project has asked CMake to find a package configuration file provided by
 "MathFunctions", but CMake did not find one.

 Could not find a package configuration file provided by "MathFunctions"
 with any of the following names:

 MathFunctionsConfig.cmake
 mathfunctions-config.cmake

 Add the installation prefix of "MathFunctions" to CMAKE_PREFIX_PATH or set
 "MathFunctions_DIR" to a directory containing one of the above files. If
 "MathFunctions" provides a separate development package or SDK, be sure it
 has been installed.

Set the `CMAKE_PREFIX_PATH` to where MathFunctions was installed previously and try again. Ensure that the newly created executable runs as expected.

[Adding Components](https://cmake.org/cmake/help/latest/guide/importing-exporting/index.html#id14)[¶](https://cmake.org/cmake/help/latest/guide/importing-exporting/index.html#adding-components "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Let's edit the `MathFunctions` project to use components. The source code for this section can be found in `Help\guide\importing-exporting\MathFunctionsComponents`. The CMakeLists file for this project adds two subdirectories: `Addition` and `SquareRoot`.

cmake_minimum_required(VERSION 3.15)
project(MathFunctionsComponents)

# make cache variables for install destinations
include(GNUInstallDirs)

# specify the C++ standard
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED True)

add_subdirectory(Addition)
add_subdirectory(SquareRoot)

Generate and install the package configuration and package version files:

include(CMakePackageConfigHelpers)

# set version
set(version 3.4.1)

# generate the version file for the config file
write_basic_package_version_file(
 "${CMAKE_CURRENT_BINARY_DIR}/MathFunctionsConfigVersion.cmake"
 VERSION "${version}"
 COMPATIBILITY AnyNewerVersion
)

# create config file
configure_package_config_file(${CMAKE_CURRENT_SOURCE_DIR}/Config.cmake.in
 "${CMAKE_CURRENT_BINARY_DIR}/MathFunctionsConfig.cmake"
 INSTALL_DESTINATION ${CMAKE_INSTALL_LIBDIR}/cmake/MathFunctions
 NO_CHECK_REQUIRED_COMPONENTS_MACRO
)

# install config files
install(FILES
 "${CMAKE_CURRENT_BINARY_DIR}/MathFunctionsConfig.cmake"
 "${CMAKE_CURRENT_BINARY_DIR}/MathFunctionsConfigVersion.cmake"
 DESTINATION ${CMAKE_INSTALL_LIBDIR}/cmake/MathFunctions
)

If `COMPONENTS` are specified when the downstream uses [`find_package()`](https://cmake.org/cmake/help/latest/command/find_package.html#command:find_package "find_package"), they are listed in the `<PackageName>_FIND_COMPONENTS` variable. We can use this variable to verify that all necessary component targets are included in `Config.cmake.in`. At the same time, this function will act as a custom `check_required_components` macro to ensure that the downstream only attempts to use supported components.

@PACKAGE_INIT@

set(_MathFunctions_supported_components Addition SquareRoot)

foreach(_comp ${MathFunctions_FIND_COMPONENTS})
  if (NOT _comp IN_LIST _MathFunctions_supported_components)
    set(MathFunctions_FOUND False)
    set(MathFunctions_NOT_FOUND_MESSAGE "Unsupported component: ${_comp}")
  endif()
  include("${CMAKE_CURRENT_LIST_DIR}/MathFunctions${_comp}Targets.cmake")
endforeach()

Here, the `MathFunctions_NOT_FOUND_MESSAGE` is set to a diagnosis that the package could not be found because an invalid component was specified. This message variable can be set for any case where the `_FOUND` variable is set to `False`, and will be displayed to the user.

The `Addition` and `SquareRoot` directories are similar. Let's look at one of the CMakeLists files:

# create library
add_library(SquareRoot STATIC SquareRoot.cxx)

add_library(MathFunctions::SquareRoot ALIAS SquareRoot)

# add include directories
target_include_directories(SquareRoot
 PUBLIC
 "$<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}>"
 "$<INSTALL_INTERFACE:${CMAKE_INSTALL_INCLUDEDIR}>"
)

# install the target and create export-set
install(TARGETS SquareRoot
 EXPORT SquareRootTargets
 LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
 ARCHIVE DESTINATION ${CMAKE_INSTALL_LIBDIR}
 RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR}
 INCLUDES DESTINATION ${CMAKE_INSTALL_INCLUDEDIR}
)

# install header file
install(FILES SquareRoot.h DESTINATION ${CMAKE_INSTALL_INCLUDEDIR})

# generate and install export file
install(EXPORT SquareRootTargets
 FILE MathFunctionsSquareRootTargets.cmake
 NAMESPACE MathFunctions::
 DESTINATION ${CMAKE_INSTALL_LIBDIR}/cmake/MathFunctions
)

Now we can build the project as described in earlier sections. To test using this package, we can use the project in `Help\guide\importing-exporting\DownstreamComponents`. There's two differences from the previous `Downstream` project. First, we need to find the package components. Change the `find_package` line from:

find_package(MathFunctions 3.4.1 EXACT)

To:

find_package(MathFunctions 3.4 COMPONENTS Addition SquareRoot)

and the `target_link_libraries` line from:

target_link_libraries(myexe PRIVATE MathFunctions::MathFunctions)

To:

target_link_libraries(myexe PRIVATE MathFunctions::Addition MathFunctions::SquareRoot)

In `main.cc`, replace `#include MathFunctions.h` with:

#include "Addition.h"
#include "SquareRoot.h"

Finally, use the `Addition` library:

 double const sum = MathFunctions::add(inputValue, inputValue);
 std::cout << inputValue << " + " << inputValue << " = " << sum << std::endl;

Build the `Downstream` project and confirm that it can find and use the package components.

### Table of Contents

*   [Importing and Exporting Guide](https://cmake.org/cmake/help/latest/guide/importing-exporting/index.html#)
    *   [Introduction](https://cmake.org/cmake/help/latest/guide/importing-exporting/index.html#introduction)
    *   [Importing Targets](https://cmake.org/cmake/help/latest/guide/importing-exporting/index.html#importing-targets)
        *   [Importing Executables](https://cmake.org/cmake/help/latest/guide/importing-exporting/index.html#importing-executables)
        *   [Importing Libraries](https://cmake.org/cmake/help/latest/guide/importing-exporting/index.html#importing-libraries)

    *   [Exporting Targets](https://cmake.org/cmake/help/latest/guide/importing-exporting/index.html#exporting-targets)
        *   [Creating Packages](https://cmake.org/cmake/help/latest/guide/importing-exporting/index.html#creating-packages)
            *   [Creating a Package Configuration File](https://cmake.org/cmake/help/latest/guide/importing-exporting/index.html#creating-a-package-configuration-file)
            *   [Creating a Package Version File](https://cmake.org/cmake/help/latest/guide/importing-exporting/index.html#creating-a-package-version-file)

        *   [Exporting Targets from the Build Tree](https://cmake.org/cmake/help/latest/guide/importing-exporting/index.html#exporting-targets-from-the-build-tree)
        *   [Building and Installing a Package](https://cmake.org/cmake/help/latest/guide/importing-exporting/index.html#building-and-installing-a-package)

    *   [Creating Relocatable Packages](https://cmake.org/cmake/help/latest/guide/importing-exporting/index.html#creating-relocatable-packages)
    *   [Using the Package Configuration File](https://cmake.org/cmake/help/latest/guide/importing-exporting/index.html#using-the-package-configuration-file)
    *   [Adding Components](https://cmake.org/cmake/help/latest/guide/importing-exporting/index.html#adding-components)

#### Previous topic

[Using Dependencies Guide](https://cmake.org/cmake/help/latest/guide/using-dependencies/index.html "previous chapter")

#### Next topic

[IDE Integration Guide](https://cmake.org/cmake/help/latest/guide/ide-integration/index.html "next chapter")

### This Page

*   [Show Source](https://cmake.org/cmake/help/latest/_sources/guide/importing-exporting/index.rst.txt)

### Quick search

### Navigation

*   [index](https://cmake.org/cmake/help/latest/genindex.html "General Index")
*   [next](https://cmake.org/cmake/help/latest/guide/ide-integration/index.html "IDE Integration Guide") |
*   [previous](https://cmake.org/cmake/help/latest/guide/using-dependencies/index.html "Using Dependencies Guide") |

*   ![Image 2](https://cmake.org/cmake/help/latest/_static/cmake-logo-16.png)[CMake](https://cmake.org/)4.3.0-rc3 »
*   [Documentation](https://cmake.org/cmake/help/latest/index.html) » 
*   [Importing and Exporting Guide](https://cmake.org/cmake/help/latest/guide/importing-exporting/index.html)

 © Copyright 2000-2026 Kitware, Inc. and Contributors. Created using [Sphinx](https://www.sphinx-doc.org/) 8.2.3.
