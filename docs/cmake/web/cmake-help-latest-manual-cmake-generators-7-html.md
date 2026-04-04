# Source: https://cmake.org/cmake/help/latest/manual/cmake-generators.7.html

Title: cmake-generators(7) — CMake 4.3.0-rc3 Documentation

URL Source: https://cmake.org/cmake/help/latest/manual/cmake-generators.7.html

Markdown Content:
Contents

*   [cmake-generators(7)](https://cmake.org/cmake/help/latest/manual/cmake-generators.7.html#cmake-generators-7)

    *   [Introduction](https://cmake.org/cmake/help/latest/manual/cmake-generators.7.html#introduction)

    *   [CMake Generators](https://cmake.org/cmake/help/latest/manual/cmake-generators.7.html#cmake-generators)

        *   [Command-Line Build Tool Generators](https://cmake.org/cmake/help/latest/manual/cmake-generators.7.html#command-line-build-tool-generators)

            *   [Makefile Generators](https://cmake.org/cmake/help/latest/manual/cmake-generators.7.html#makefile-generators)

            *   [Ninja Generators](https://cmake.org/cmake/help/latest/manual/cmake-generators.7.html#ninja-generators)

            *   [FASTBuild Generator](https://cmake.org/cmake/help/latest/manual/cmake-generators.7.html#fastbuild-generator)

        *   [IDE Build Tool Generators](https://cmake.org/cmake/help/latest/manual/cmake-generators.7.html#ide-build-tool-generators)

            *   [Visual Studio Generators](https://cmake.org/cmake/help/latest/manual/cmake-generators.7.html#visual-studio-generators)

            *   [Other Generators](https://cmake.org/cmake/help/latest/manual/cmake-generators.7.html#other-generators)

    *   [Extra Generators](https://cmake.org/cmake/help/latest/manual/cmake-generators.7.html#extra-generators)

[Introduction](https://cmake.org/cmake/help/latest/manual/cmake-generators.7.html#id8)[¶](https://cmake.org/cmake/help/latest/manual/cmake-generators.7.html#introduction "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

A _CMake Generator_ is responsible for writing the input files for a native build system. Exactly one of the [CMake Generators](https://cmake.org/cmake/help/latest/manual/cmake-generators.7.html#cmake-generators) must be selected for a build tree to determine what native build system is to be used. Optionally one of the [Extra Generators](https://cmake.org/cmake/help/latest/manual/cmake-generators.7.html#extra-generators) may be selected as a variant of some of the [Command-Line Build Tool Generators](https://cmake.org/cmake/help/latest/manual/cmake-generators.7.html#command-line-build-tool-generators) to produce project files for an auxiliary IDE.

CMake Generators are platform-specific so each may be available only on certain platforms. The [`cmake(1)`](https://cmake.org/cmake/help/latest/manual/cmake.1.html#manual:cmake(1) "cmake(1)") command-line tool [`--help`](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-h) output lists available generators on the current platform. Use its [`-G`](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-G) option to specify the generator for a new build tree. The [`cmake-gui(1)`](https://cmake.org/cmake/help/latest/manual/cmake-gui.1.html#manual:cmake-gui(1) "cmake-gui(1)") offers interactive selection of a generator when creating a new build tree.

[CMake Generators](https://cmake.org/cmake/help/latest/manual/cmake-generators.7.html#id9)[¶](https://cmake.org/cmake/help/latest/manual/cmake-generators.7.html#cmake-generators "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### [Command-Line Build Tool Generators](https://cmake.org/cmake/help/latest/manual/cmake-generators.7.html#id10)[¶](https://cmake.org/cmake/help/latest/manual/cmake-generators.7.html#command-line-build-tool-generators "Link to this heading")

These generators support command-line build tools. In order to use them, one must launch CMake from a command-line prompt whose environment is already configured for the chosen compiler and build tool.

#### [Makefile Generators](https://cmake.org/cmake/help/latest/manual/cmake-generators.7.html#id11)[¶](https://cmake.org/cmake/help/latest/manual/cmake-generators.7.html#makefile-generators "Link to this heading")

*   [Borland Makefiles](https://cmake.org/cmake/help/latest/generator/Borland%20Makefiles.html)
*   [MSYS Makefiles](https://cmake.org/cmake/help/latest/generator/MSYS%20Makefiles.html)
*   [MinGW Makefiles](https://cmake.org/cmake/help/latest/generator/MinGW%20Makefiles.html)
*   [NMake Makefiles](https://cmake.org/cmake/help/latest/generator/NMake%20Makefiles.html)
*   [NMake Makefiles JOM](https://cmake.org/cmake/help/latest/generator/NMake%20Makefiles%20JOM.html)
*   [Unix Makefiles](https://cmake.org/cmake/help/latest/generator/Unix%20Makefiles.html)
*   [Watcom WMake](https://cmake.org/cmake/help/latest/generator/Watcom%20WMake.html)

#### [Ninja Generators](https://cmake.org/cmake/help/latest/manual/cmake-generators.7.html#id12)[¶](https://cmake.org/cmake/help/latest/manual/cmake-generators.7.html#ninja-generators "Link to this heading")

*   [Ninja](https://cmake.org/cmake/help/latest/generator/Ninja.html)
*   [Ninja Multi-Config](https://cmake.org/cmake/help/latest/generator/Ninja%20Multi-Config.html)

#### [FASTBuild Generator](https://cmake.org/cmake/help/latest/manual/cmake-generators.7.html#id13)[¶](https://cmake.org/cmake/help/latest/manual/cmake-generators.7.html#fastbuild-generator "Link to this heading")

*   [FASTBuild](https://cmake.org/cmake/help/latest/generator/FASTBuild.html)

### [IDE Build Tool Generators](https://cmake.org/cmake/help/latest/manual/cmake-generators.7.html#id14)[¶](https://cmake.org/cmake/help/latest/manual/cmake-generators.7.html#ide-build-tool-generators "Link to this heading")

These generators support Integrated Development Environment (IDE) project files. Since the IDEs configure their own environment one may launch CMake from any environment.

#### [Visual Studio Generators](https://cmake.org/cmake/help/latest/manual/cmake-generators.7.html#id15)[¶](https://cmake.org/cmake/help/latest/manual/cmake-generators.7.html#visual-studio-generators "Link to this heading")

*   [Visual Studio 6](https://cmake.org/cmake/help/latest/generator/Visual%20Studio%206.html)
*   [Visual Studio 7](https://cmake.org/cmake/help/latest/generator/Visual%20Studio%207.html)
*   [Visual Studio 7 .NET 2003](https://cmake.org/cmake/help/latest/generator/Visual%20Studio%207%20.NET%202003.html)
*   [Visual Studio 8 2005](https://cmake.org/cmake/help/latest/generator/Visual%20Studio%208%202005.html)
*   [Visual Studio 9 2008](https://cmake.org/cmake/help/latest/generator/Visual%20Studio%209%202008.html)
*   [Visual Studio 10 2010](https://cmake.org/cmake/help/latest/generator/Visual%20Studio%2010%202010.html)
*   [Visual Studio 11 2012](https://cmake.org/cmake/help/latest/generator/Visual%20Studio%2011%202012.html)
*   [Visual Studio 12 2013](https://cmake.org/cmake/help/latest/generator/Visual%20Studio%2012%202013.html)
*   [Visual Studio 14 2015](https://cmake.org/cmake/help/latest/generator/Visual%20Studio%2014%202015.html)
*   [Visual Studio 15 2017](https://cmake.org/cmake/help/latest/generator/Visual%20Studio%2015%202017.html)
*   [Visual Studio 16 2019](https://cmake.org/cmake/help/latest/generator/Visual%20Studio%2016%202019.html)
*   [Visual Studio 17 2022](https://cmake.org/cmake/help/latest/generator/Visual%20Studio%2017%202022.html)
*   [Visual Studio 18 2026](https://cmake.org/cmake/help/latest/generator/Visual%20Studio%2018%202026.html)

#### [Other Generators](https://cmake.org/cmake/help/latest/manual/cmake-generators.7.html#id16)[¶](https://cmake.org/cmake/help/latest/manual/cmake-generators.7.html#other-generators "Link to this heading")

*   [Green Hills MULTI](https://cmake.org/cmake/help/latest/generator/Green%20Hills%20MULTI.html)
*   [Xcode](https://cmake.org/cmake/help/latest/generator/Xcode.html)

[Extra Generators](https://cmake.org/cmake/help/latest/manual/cmake-generators.7.html#id17)[¶](https://cmake.org/cmake/help/latest/manual/cmake-generators.7.html#extra-generators "Link to this heading")
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Deprecated since version 3.27: Support for "Extra Generators" is deprecated and will be removed from a future version of CMake. IDEs may use the [`cmake-file-api(7)`](https://cmake.org/cmake/help/latest/manual/cmake-file-api.7.html#manual:cmake-file-api(7) "cmake-file-api(7)") to view CMake-generated project build trees.

Some of the [CMake Generators](https://cmake.org/cmake/help/latest/manual/cmake-generators.7.html#cmake-generators) listed in the [`cmake(1)`](https://cmake.org/cmake/help/latest/manual/cmake.1.html#manual:cmake(1) "cmake(1)") command-line tool [`--help`](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-h) output may have variants that specify an extra generator for an auxiliary IDE tool. Such generator names have the form `<extra-generator> - <main-generator>`. The following extra generators are known to CMake.

*   [CodeBlocks](https://cmake.org/cmake/help/latest/generator/CodeBlocks.html)
*   [CodeLite](https://cmake.org/cmake/help/latest/generator/CodeLite.html)
*   [Eclipse CDT4](https://cmake.org/cmake/help/latest/generator/Eclipse%20CDT4.html)
*   [Kate](https://cmake.org/cmake/help/latest/generator/Kate.html)
*   [Sublime Text 2](https://cmake.org/cmake/help/latest/generator/Sublime%20Text%202.html)
