# Source: https://cmake.org/cmake/help/latest/guide/ide-integration/index.html

Title: IDE Integration Guide — CMake 4.3.0-rc3 Documentation

URL Source: https://cmake.org/cmake/help/latest/guide/ide-integration/index.html

Markdown Content:
Contents

*   [IDE Integration Guide](https://cmake.org/cmake/help/latest/guide/ide-integration/index.html#guide:IDE%20Integration%20Guide)

    *   [Introduction](https://cmake.org/cmake/help/latest/guide/ide-integration/index.html#introduction)

    *   [Bundling](https://cmake.org/cmake/help/latest/guide/ide-integration/index.html#bundling)

    *   [Presets](https://cmake.org/cmake/help/latest/guide/ide-integration/index.html#presets)

    *   [Configuring](https://cmake.org/cmake/help/latest/guide/ide-integration/index.html#configuring)

    *   [Building](https://cmake.org/cmake/help/latest/guide/ide-integration/index.html#building)

    *   [Testing](https://cmake.org/cmake/help/latest/guide/ide-integration/index.html#testing)

    *   [IDEs with CMake integration](https://cmake.org/cmake/help/latest/guide/ide-integration/index.html#ides-with-cmake-integration)

[Introduction](https://cmake.org/cmake/help/latest/guide/ide-integration/index.html#id2)[¶](https://cmake.org/cmake/help/latest/guide/ide-integration/index.html#introduction "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Integrated development environments (IDEs) may want to integrate with CMake to improve the development experience for CMake users. This document lays out the recommended best practices for such integration.

[Bundling](https://cmake.org/cmake/help/latest/guide/ide-integration/index.html#id3)[¶](https://cmake.org/cmake/help/latest/guide/ide-integration/index.html#bundling "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Many IDE vendors will want to bundle a copy of CMake with their IDE. IDEs that bundle CMake should present the user with the option of using an external CMake installation instead of the bundled one, in case the bundled copy becomes outdated and the user wants to use a newer version.

While IDE vendors may be tempted to bundle different versions of CMake with their application, such practice is not recommended. CMake has strong guarantees of backwards compatibility, and there is no reason not to use a newer version of CMake than what a project requires, or indeed, the very latest version. Therefore, it is recommended that IDE vendors that bundle CMake with their application always include the very latest patch version of CMake available at the time of release.

As a suggestion, IDEs may also ship a copy of the Ninja buildsystem alongside CMake. Ninja is highly performant and well-supported on all platforms that support CMake. IDEs that bundle Ninja should use Ninja 1.10 or later, which contains features needed to support Fortran builds.

[Presets](https://cmake.org/cmake/help/latest/guide/ide-integration/index.html#id4)[¶](https://cmake.org/cmake/help/latest/guide/ide-integration/index.html#presets "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

CMake supports a file format called `CMakePresets.json`, and its user-specific counterpart, `CMakeUserPresets.json`. This file contains information on the various configure presets that a user may want. Each preset may have a different compiler, build flags, etc. The details of this format are explained in the [`cmake(1)`](https://cmake.org/cmake/help/latest/manual/cmake.1.html#manual:cmake(1) "cmake(1)") manual.

IDE vendors are encouraged to read and evaluate this file the same way CMake does, and present the user with the presets listed in the file. Users should be able to see (and possibly edit) the CMake cache variables, environment variables, and command line options that are defined for a given preset. The IDE should then construct the list of appropriate [`cmake(1)`](https://cmake.org/cmake/help/latest/manual/cmake.1.html#manual:cmake(1) "cmake(1)") command line arguments based on these settings, rather than using the [`--preset=`](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-preset) option directly. The [`--preset=`](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-preset) option is intended only as a convenient frontend for command line users, and should not be used by the IDE.

For example, if a preset named `ninja` specifies `Ninja` as the generator and `${sourceDir}/build` as the build directory, instead of running:

cmake -S /path/to/source --preset=ninja

the IDE should instead calculate the settings of the `ninja` preset, and then run:

cmake -S /path/to/source -B /path/to/source/build -G Ninja

In cases where a preset contains lots of cache variables, and passing all of them as [`-D`](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-D) flags would cause the command line length limit of the platform to be exceeded, the IDE should instead construct a temporary cache script and pass it with the [`-C`](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-C) flag.

While reading, parsing, and evaluating the contents of `CMakePresets.json` is straightforward, it is not trivial. In addition to the documentation, IDE vendors may also wish to refer to the CMake source code and test cases for a better understanding of how to implement the format. [`This file`](https://cmake.org/cmake/help/latest/_downloads/3e2d73bff478d88a7de0de736ba5e361/schema.json) provides a machine-readable JSON schema for the `CMakePresets.json` format that IDE vendors may find useful for validation and providing editing assistance.

[Configuring](https://cmake.org/cmake/help/latest/guide/ide-integration/index.html#id5)[¶](https://cmake.org/cmake/help/latest/guide/ide-integration/index.html#configuring "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

IDEs that invoke [`cmake(1)`](https://cmake.org/cmake/help/latest/manual/cmake.1.html#manual:cmake(1) "cmake(1)") to run the configure step may wish to receive information about the artifacts that the build will produce, as well as the include directories, compile definitions, etc. used to build the artifacts. Such information can be obtained by using the [`File API`](https://cmake.org/cmake/help/latest/manual/cmake-file-api.7.html#manual:cmake-file-api(7) "cmake-file-api(7)"). The manual page for the File API contains more information about the API and how to invoke it. [`Server mode`](https://cmake.org/cmake/help/latest/manual/cmake-server.7.html#manual:cmake-server(7) "cmake-server(7)") was removed as of CMake 3.20 and should not be used on CMake 3.14 or later.

IDEs should avoid creating more build trees than necessary, and only create multiple build trees if the user wishes to switch to a different compiler, use different compile flags, etc. In particular, IDEs should NOT create multiple single-config build trees which all have the same properties except for a differing [`CMAKE_BUILD_TYPE`](https://cmake.org/cmake/help/latest/variable/CMAKE_BUILD_TYPE.html#variable:CMAKE_BUILD_TYPE "CMAKE_BUILD_TYPE"), effectively creating a multi-config environment. Instead, the [`Ninja Multi-Config`](https://cmake.org/cmake/help/latest/generator/Ninja%20Multi-Config.html#generator:Ninja%20Multi-Config "Ninja Multi-Config") generator, in conjunction with the [`File API`](https://cmake.org/cmake/help/latest/manual/cmake-file-api.7.html#manual:cmake-file-api(7) "cmake-file-api(7)") to get the list of build configurations, should be used for this purpose.

IDEs should not use the "extra generators" with Makefile or Ninja generators, which generate IDE project files in addition to the Makefile or Ninja files. Instead the [`File API`](https://cmake.org/cmake/help/latest/manual/cmake-file-api.7.html#manual:cmake-file-api(7) "cmake-file-api(7)") should be used to get the list of build artifacts.

[Building](https://cmake.org/cmake/help/latest/guide/ide-integration/index.html#id6)[¶](https://cmake.org/cmake/help/latest/guide/ide-integration/index.html#building "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

If a Makefile or Ninja generator is used to generate the build tree, it is not recommended to invoke `make` or `ninja` directly. Instead, it is recommended that the IDE invoke [`cmake(1)`](https://cmake.org/cmake/help/latest/manual/cmake.1.html#manual:cmake(1) "cmake(1)") with the [`--build`](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-build) argument, which will in turn invoke the appropriate build tool.

If an IDE project generator is used, such as [`Xcode`](https://cmake.org/cmake/help/latest/generator/Xcode.html#generator:Xcode "Xcode") or one of the [Visual Studio Generators](https://cmake.org/cmake/help/latest/manual/cmake-generators.7.html#visual-studio-generators), and the IDE understands the project format used, the IDE should read the project file and build it the same way it would otherwise.

The [`File API`](https://cmake.org/cmake/help/latest/manual/cmake-file-api.7.html#manual:cmake-file-api(7) "cmake-file-api(7)") can be used to obtain a list of build configurations from the build tree, and the IDE should present this list to the user to select a build configuration.

[Testing](https://cmake.org/cmake/help/latest/guide/ide-integration/index.html#id7)[¶](https://cmake.org/cmake/help/latest/guide/ide-integration/index.html#testing "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[`ctest(1)`](https://cmake.org/cmake/help/latest/manual/ctest.1.html#manual:ctest(1) "ctest(1)") supports outputting a JSON format with information about the available tests and test configurations. IDEs which want to run CTest should obtain this information and use it to present the user with a list of tests.

IDEs should not invoke the `test` target of the generated buildsystem. Instead, they should invoke [`ctest(1)`](https://cmake.org/cmake/help/latest/manual/ctest.1.html#manual:ctest(1) "ctest(1)") directly.

[IDEs with CMake integration](https://cmake.org/cmake/help/latest/guide/ide-integration/index.html#id8)[¶](https://cmake.org/cmake/help/latest/guide/ide-integration/index.html#ides-with-cmake-integration "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The following IDEs support CMake natively:

*   [CLion](https://www.jetbrains.com/clion/)

*   [KDevelop](https://kdevelop.org/)

*   [QtCreator](https://www.qt.io/development/tools)

*   [Vim](https://www.vim.org/) (via a plugin)

*   [Visual Studio](https://visualstudio.microsoft.com/)

*   [VSCode](https://code.visualstudio.com/) (via a plugin)

Additionally, CMake has builtin support for some IDEs:

*   [IDE Build Tool Generators](https://cmake.org/cmake/help/latest/manual/cmake-generators.7.html#ide-build-tool-generators): Generate IDE native build systems such as [Visual Studio](https://cmake.org/cmake/help/latest/manual/cmake-generators.7.html#visual-studio-generators) or [`Xcode`](https://cmake.org/cmake/help/latest/generator/Xcode.html#generator:Xcode "Xcode").

*   [Extra Generators](https://cmake.org/cmake/help/latest/manual/cmake-generators.7.html#extra-generators): Extend [Command-Line Build Tool Generators](https://cmake.org/cmake/help/latest/manual/cmake-generators.7.html#command-line-build-tool-generators) to generate IDE project files that hook into the command-line build system. Superseded by the [`File API`](https://cmake.org/cmake/help/latest/manual/cmake-file-api.7.html#manual:cmake-file-api(7) "cmake-file-api(7)").
