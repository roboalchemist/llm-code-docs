# Source: https://cmake.org/cmake/help/latest/manual/cmake-toolchains.7.html

Title: cmake-toolchains(7) — CMake 4.3.0-rc3 Documentation

URL Source: https://cmake.org/cmake/help/latest/manual/cmake-toolchains.7.html

Published Time: Tue, 10 Mar 2026 19:18:20 GMT

Markdown Content:
cmake-toolchains(7) — CMake 4.3.0-rc3 Documentation
===============
- [x] 

### Navigation

*   [index](https://cmake.org/cmake/help/latest/genindex.html "General Index")
*   [next](https://cmake.org/cmake/help/latest/manual/cmake-variables.7.html "cmake-variables(7)") |
*   [previous](https://cmake.org/cmake/help/latest/manual/cmake-server.7.html "cmake-server(7)") |

*   ![Image 1](https://cmake.org/cmake/help/latest/_static/cmake-logo-16.png)[CMake](https://cmake.org/)4.3.0-rc3 »
*   [Documentation](https://cmake.org/cmake/help/latest/index.html) » 
*   [cmake-toolchains(7)](https://cmake.org/cmake/help/latest/manual/cmake-toolchains.7.html)

[cmake-toolchains(7)](https://cmake.org/cmake/help/latest/manual/cmake-toolchains.7.html#id9)[¶](https://cmake.org/cmake/help/latest/manual/cmake-toolchains.7.html#cmake-toolchains-7 "Link to this heading")
==============================================================================================================================================================================================================

Contents

*   [cmake-toolchains(7)](https://cmake.org/cmake/help/latest/manual/cmake-toolchains.7.html#cmake-toolchains-7)

    *   [Introduction](https://cmake.org/cmake/help/latest/manual/cmake-toolchains.7.html#introduction)

    *   [Languages](https://cmake.org/cmake/help/latest/manual/cmake-toolchains.7.html#languages)

    *   [Variables and Properties](https://cmake.org/cmake/help/latest/manual/cmake-toolchains.7.html#variables-and-properties)

    *   [Toolchain Features](https://cmake.org/cmake/help/latest/manual/cmake-toolchains.7.html#toolchain-features)

    *   [Cross Compiling](https://cmake.org/cmake/help/latest/manual/cmake-toolchains.7.html#cross-compiling)

        *   [Cross Compiling for Linux](https://cmake.org/cmake/help/latest/manual/cmake-toolchains.7.html#cross-compiling-for-linux)

        *   [Cross Compiling for the Cray Linux Environment](https://cmake.org/cmake/help/latest/manual/cmake-toolchains.7.html#cross-compiling-for-the-cray-linux-environment)

        *   [Cross Compiling using Clang](https://cmake.org/cmake/help/latest/manual/cmake-toolchains.7.html#cross-compiling-using-clang)

        *   [Cross Compiling for QNX](https://cmake.org/cmake/help/latest/manual/cmake-toolchains.7.html#cross-compiling-for-qnx)

        *   [Cross Compiling for Windows CE](https://cmake.org/cmake/help/latest/manual/cmake-toolchains.7.html#cross-compiling-for-windows-ce)

        *   [Cross Compiling for Windows 10 Universal Applications](https://cmake.org/cmake/help/latest/manual/cmake-toolchains.7.html#cross-compiling-for-windows-10-universal-applications)

        *   [Cross Compiling for Windows Phone](https://cmake.org/cmake/help/latest/manual/cmake-toolchains.7.html#cross-compiling-for-windows-phone)

        *   [Cross Compiling for Windows Store](https://cmake.org/cmake/help/latest/manual/cmake-toolchains.7.html#cross-compiling-for-windows-store)

        *   [Cross Compiling for ADSP SHARC/Blackfin](https://cmake.org/cmake/help/latest/manual/cmake-toolchains.7.html#cross-compiling-for-adsp-sharc-blackfin)

        *   [Cross Compiling for Android](https://cmake.org/cmake/help/latest/manual/cmake-toolchains.7.html#cross-compiling-for-android)

            *   [Cross Compiling for Android with the NDK](https://cmake.org/cmake/help/latest/manual/cmake-toolchains.7.html#cross-compiling-for-android-with-the-ndk)

            *   [Cross Compiling for Android with a Standalone Toolchain](https://cmake.org/cmake/help/latest/manual/cmake-toolchains.7.html#cross-compiling-for-android-with-a-standalone-toolchain)

            *   [Cross Compiling for Android with NVIDIA Nsight Tegra Visual Studio Edition](https://cmake.org/cmake/help/latest/manual/cmake-toolchains.7.html#cross-compiling-for-android-with-nvidia-nsight-tegra-visual-studio-edition)

        *   [Cross Compiling for iOS, tvOS, visionOS, or watchOS](https://cmake.org/cmake/help/latest/manual/cmake-toolchains.7.html#cross-compiling-for-ios-tvos-visionos-or-watchos)

            *   [Code Signing](https://cmake.org/cmake/help/latest/manual/cmake-toolchains.7.html#code-signing)

            *   [Switching Between Device and Simulator](https://cmake.org/cmake/help/latest/manual/cmake-toolchains.7.html#switching-between-device-and-simulator)

        *   [Cross Compiling for Emscripten](https://cmake.org/cmake/help/latest/manual/cmake-toolchains.7.html#cross-compiling-for-emscripten)

        *   [Cross Compiling using Renesas compilers](https://cmake.org/cmake/help/latest/manual/cmake-toolchains.7.html#cross-compiling-using-renesas-compilers)

            *   [Renesas CC-RX](https://cmake.org/cmake/help/latest/manual/cmake-toolchains.7.html#renesas-cc-rx)

            *   [Renesas CC-RL](https://cmake.org/cmake/help/latest/manual/cmake-toolchains.7.html#renesas-cc-rl)

            *   [Renesas CC-RH](https://cmake.org/cmake/help/latest/manual/cmake-toolchains.7.html#renesas-cc-rh)

[Introduction](https://cmake.org/cmake/help/latest/manual/cmake-toolchains.7.html#id10)[¶](https://cmake.org/cmake/help/latest/manual/cmake-toolchains.7.html#introduction "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

CMake uses a toolchain of utilities to compile, link libraries and create archives, and other tasks to drive the build. The toolchain utilities available are determined by the languages enabled. In normal builds, CMake automatically determines the toolchain for host builds based on system introspection and defaults. In cross-compiling scenarios, a toolchain file may be specified with information about compiler and utility paths.

Added in version 3.19: One may use [`cmake-presets(7)`](https://cmake.org/cmake/help/latest/manual/cmake-presets.7.html#manual:cmake-presets(7) "cmake-presets(7)") to specify toolchain files.

[Languages](https://cmake.org/cmake/help/latest/manual/cmake-toolchains.7.html#id11)[¶](https://cmake.org/cmake/help/latest/manual/cmake-toolchains.7.html#languages "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Languages are enabled by the [`project()`](https://cmake.org/cmake/help/latest/command/project.html#command:project "project") command. Language-specific built-in variables, such as [`CMAKE_CXX_COMPILER`](https://cmake.org/cmake/help/latest/variable/CMAKE_LANG_COMPILER.html#variable:CMAKE_%3CLANG%3E_COMPILER "CMAKE_<LANG>_COMPILER"), [`CMAKE_CXX_COMPILER_ID`](https://cmake.org/cmake/help/latest/variable/CMAKE_LANG_COMPILER_ID.html#variable:CMAKE_%3CLANG%3E_COMPILER_ID "CMAKE_<LANG>_COMPILER_ID") etc are set by invoking the [`project()`](https://cmake.org/cmake/help/latest/command/project.html#command:project "project") command. If no project command is in the top-level CMakeLists file, one will be implicitly generated. By default the enabled languages are `C` and `CXX`:

project(C_Only C)

A special value of `NONE` can also be used with the [`project()`](https://cmake.org/cmake/help/latest/command/project.html#command:project "project") command to enable no languages:

project(MyProject NONE)

The [`enable_language()`](https://cmake.org/cmake/help/latest/command/enable_language.html#command:enable_language "enable_language") command can be used to enable languages after the [`project()`](https://cmake.org/cmake/help/latest/command/project.html#command:project "project") command:

enable_language(CXX)

When a language is enabled, CMake finds a compiler for that language, and determines some information, such as the vendor and version of the compiler, the target architecture and bitwidth, the location of corresponding utilities etc.

The [`ENABLED_LANGUAGES`](https://cmake.org/cmake/help/latest/prop_gbl/ENABLED_LANGUAGES.html#prop_gbl:ENABLED_LANGUAGES "ENABLED_LANGUAGES") global property contains the languages which are currently enabled.

[Variables and Properties](https://cmake.org/cmake/help/latest/manual/cmake-toolchains.7.html#id12)[¶](https://cmake.org/cmake/help/latest/manual/cmake-toolchains.7.html#variables-and-properties "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Several variables relate to the language components of a toolchain which are enabled:

[`CMAKE_<LANG>_COMPILER`](https://cmake.org/cmake/help/latest/variable/CMAKE_LANG_COMPILER.html#variable:CMAKE_%3CLANG%3E_COMPILER "CMAKE_<LANG>_COMPILER")
The full path to the compiler used for `<LANG>`

[`CMAKE_<LANG>_COMPILER_ID`](https://cmake.org/cmake/help/latest/variable/CMAKE_LANG_COMPILER_ID.html#variable:CMAKE_%3CLANG%3E_COMPILER_ID "CMAKE_<LANG>_COMPILER_ID")
The compiler identifier used by CMake

[`CMAKE_<LANG>_COMPILER_VERSION`](https://cmake.org/cmake/help/latest/variable/CMAKE_LANG_COMPILER_VERSION.html#variable:CMAKE_%3CLANG%3E_COMPILER_VERSION "CMAKE_<LANG>_COMPILER_VERSION")
The version of the compiler.

[`CMAKE_<LANG>_FLAGS`](https://cmake.org/cmake/help/latest/variable/CMAKE_LANG_FLAGS.html#variable:CMAKE_%3CLANG%3E_FLAGS "CMAKE_<LANG>_FLAGS")
The variables and the configuration-specific equivalents contain flags that will be added to the compile command when compiling a file of a particular language.

CMake needs a way to determine which compiler to use to invoke the linker. This is determined by the [`LANGUAGE`](https://cmake.org/cmake/help/latest/prop_sf/LANGUAGE.html#prop_sf:LANGUAGE "LANGUAGE") property of source files of the [`target`](https://cmake.org/cmake/help/latest/manual/cmake-buildsystem.7.html#manual:cmake-buildsystem(7) "cmake-buildsystem(7)"), and in the case of static libraries, the `LANGUAGE` of the dependent libraries. The choice CMake makes may be overridden with the [`LINKER_LANGUAGE`](https://cmake.org/cmake/help/latest/prop_tgt/LINKER_LANGUAGE.html#prop_tgt:LINKER_LANGUAGE "LINKER_LANGUAGE") target property.

[Toolchain Features](https://cmake.org/cmake/help/latest/manual/cmake-toolchains.7.html#id13)[¶](https://cmake.org/cmake/help/latest/manual/cmake-toolchains.7.html#toolchain-features "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

CMake provides the [`try_compile()`](https://cmake.org/cmake/help/latest/command/try_compile.html#command:try_compile "try_compile") command and modules such as [`CheckSourceCompiles`](https://cmake.org/cmake/help/latest/module/CheckSourceCompiles.html#module:CheckSourceCompiles "CheckSourceCompiles"), [`CheckCXXSymbolExists`](https://cmake.org/cmake/help/latest/module/CheckCXXSymbolExists.html#module:CheckCXXSymbolExists "CheckCXXSymbolExists") and [`CheckIncludeFile`](https://cmake.org/cmake/help/latest/module/CheckIncludeFile.html#module:CheckIncludeFile "CheckIncludeFile") to test capability and availability of various toolchain features. These APIs test the toolchain in some way and cache the result so that the test does not have to be performed again the next time CMake runs.

Some toolchain features have built-in handling in CMake, and do not require compile-tests. For example, [`POSITION_INDEPENDENT_CODE`](https://cmake.org/cmake/help/latest/prop_tgt/POSITION_INDEPENDENT_CODE.html#prop_tgt:POSITION_INDEPENDENT_CODE "POSITION_INDEPENDENT_CODE") allows specifying that a target should be built as position-independent code, if the compiler supports that feature. The [`<LANG>_VISIBILITY_PRESET`](https://cmake.org/cmake/help/latest/prop_tgt/LANG_VISIBILITY_PRESET.html#prop_tgt:%3CLANG%3E_VISIBILITY_PRESET "<LANG>_VISIBILITY_PRESET") and [`VISIBILITY_INLINES_HIDDEN`](https://cmake.org/cmake/help/latest/prop_tgt/VISIBILITY_INLINES_HIDDEN.html#prop_tgt:VISIBILITY_INLINES_HIDDEN "VISIBILITY_INLINES_HIDDEN") target properties add flags for hidden visibility, if supported by the compiler.

[Cross Compiling](https://cmake.org/cmake/help/latest/manual/cmake-toolchains.7.html#id14)[¶](https://cmake.org/cmake/help/latest/manual/cmake-toolchains.7.html#cross-compiling "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

If [`cmake(1)`](https://cmake.org/cmake/help/latest/manual/cmake.1.html#manual:cmake(1) "cmake(1)") is invoked with the command line parameter [`--toolchain path/to/file`](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-toolchain) or [`-DCMAKE_TOOLCHAIN_FILE=path/to/file`](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-D), the file will be loaded early to set values for the compilers. The [`CMAKE_CROSSCOMPILING`](https://cmake.org/cmake/help/latest/variable/CMAKE_CROSSCOMPILING.html#variable:CMAKE_CROSSCOMPILING "CMAKE_CROSSCOMPILING") variable is set to true when CMake is cross-compiling.

Note that using the [`CMAKE_SOURCE_DIR`](https://cmake.org/cmake/help/latest/variable/CMAKE_SOURCE_DIR.html#variable:CMAKE_SOURCE_DIR "CMAKE_SOURCE_DIR") or [`CMAKE_BINARY_DIR`](https://cmake.org/cmake/help/latest/variable/CMAKE_BINARY_DIR.html#variable:CMAKE_BINARY_DIR "CMAKE_BINARY_DIR") variables inside a toolchain file is typically undesirable. The toolchain file is used in contexts where these variables have different values when used in different places (e.g. as part of a call to [`try_compile()`](https://cmake.org/cmake/help/latest/command/try_compile.html#command:try_compile "try_compile")). In most cases, where there is a need to evaluate paths inside a toolchain file, the more appropriate variable to use would be [`CMAKE_CURRENT_LIST_DIR`](https://cmake.org/cmake/help/latest/variable/CMAKE_CURRENT_LIST_DIR.html#variable:CMAKE_CURRENT_LIST_DIR "CMAKE_CURRENT_LIST_DIR"), since it always has an unambiguous, predictable value.

### [Cross Compiling for Linux](https://cmake.org/cmake/help/latest/manual/cmake-toolchains.7.html#id15)[¶](https://cmake.org/cmake/help/latest/manual/cmake-toolchains.7.html#cross-compiling-for-linux "Link to this heading")

A typical cross-compiling toolchain for Linux has content such as:

set(CMAKE_SYSTEM_NAME Linux)
set(CMAKE_SYSTEM_PROCESSOR arm)

set(CMAKE_SYSROOT /home/devel/rasp-pi-rootfs)
set(CMAKE_STAGING_PREFIX /home/devel/stage)

set(tools /home/devel/gcc-4.7-linaro-rpi-gnueabihf)
set(CMAKE_C_COMPILER ${tools}/bin/arm-linux-gnueabihf-gcc)
set(CMAKE_CXX_COMPILER ${tools}/bin/arm-linux-gnueabihf-g++)

set(CMAKE_FIND_ROOT_PATH_MODE_PROGRAM NEVER)
set(CMAKE_FIND_ROOT_PATH_MODE_LIBRARY ONLY)
set(CMAKE_FIND_ROOT_PATH_MODE_INCLUDE ONLY)
set(CMAKE_FIND_ROOT_PATH_MODE_PACKAGE ONLY)

Where:

[`CMAKE_SYSTEM_NAME`](https://cmake.org/cmake/help/latest/variable/CMAKE_SYSTEM_NAME.html#variable:CMAKE_SYSTEM_NAME "CMAKE_SYSTEM_NAME")
is the CMake-identifier of the target platform to build for.

[`CMAKE_SYSTEM_PROCESSOR`](https://cmake.org/cmake/help/latest/variable/CMAKE_SYSTEM_PROCESSOR.html#variable:CMAKE_SYSTEM_PROCESSOR "CMAKE_SYSTEM_PROCESSOR")
is the CMake-identifier of the target architecture.

[`CMAKE_SYSROOT`](https://cmake.org/cmake/help/latest/variable/CMAKE_SYSROOT.html#variable:CMAKE_SYSROOT "CMAKE_SYSROOT")
is optional, and may be specified if a sysroot is available.

[`CMAKE_STAGING_PREFIX`](https://cmake.org/cmake/help/latest/variable/CMAKE_STAGING_PREFIX.html#variable:CMAKE_STAGING_PREFIX "CMAKE_STAGING_PREFIX")
is also optional. It may be used to specify a path on the host to install to. The [`CMAKE_INSTALL_PREFIX`](https://cmake.org/cmake/help/latest/variable/CMAKE_INSTALL_PREFIX.html#variable:CMAKE_INSTALL_PREFIX "CMAKE_INSTALL_PREFIX") is always the runtime installation location, even when cross-compiling.

[`CMAKE_<LANG>_COMPILER`](https://cmake.org/cmake/help/latest/variable/CMAKE_LANG_COMPILER.html#variable:CMAKE_%3CLANG%3E_COMPILER "CMAKE_<LANG>_COMPILER")
variable may be set to full paths, or to names of compilers to search for in standard locations. For toolchains that do not support linking binaries without custom flags or scripts one may set the [`CMAKE_TRY_COMPILE_TARGET_TYPE`](https://cmake.org/cmake/help/latest/variable/CMAKE_TRY_COMPILE_TARGET_TYPE.html#variable:CMAKE_TRY_COMPILE_TARGET_TYPE "CMAKE_TRY_COMPILE_TARGET_TYPE") variable to `STATIC_LIBRARY` to tell CMake not to try to link executables during its checks.

CMake `find_*` commands will look in the sysroot, and the [`CMAKE_FIND_ROOT_PATH`](https://cmake.org/cmake/help/latest/variable/CMAKE_FIND_ROOT_PATH.html#variable:CMAKE_FIND_ROOT_PATH "CMAKE_FIND_ROOT_PATH") entries by default in all cases, as well as looking in the host system root prefix. Although this can be controlled on a case-by-case basis, when cross-compiling, it can be useful to exclude looking in either the host or the target for particular artifacts. Generally, includes, libraries and packages should be found in the target system prefixes, whereas executables which must be run as part of the build should be found only on the host and not on the target. This is the purpose of the `CMAKE_FIND_ROOT_PATH_MODE_*` variables.

### [Cross Compiling for the Cray Linux Environment](https://cmake.org/cmake/help/latest/manual/cmake-toolchains.7.html#id16)[¶](https://cmake.org/cmake/help/latest/manual/cmake-toolchains.7.html#cross-compiling-for-the-cray-linux-environment "Link to this heading")

Cross compiling for compute nodes in the Cray Linux Environment can be done without needing a separate toolchain file. Specifying `-DCMAKE_SYSTEM_NAME=CrayLinuxEnvironment` on the CMake command line will ensure that the appropriate build settings and search paths are configured. The platform will pull its configuration from the current environment variables and will configure a project to use the compiler wrappers from the Cray Programming Environment's `PrgEnv-*` modules if present and loaded.

The default configuration of the Cray Programming Environment is to only support static libraries. This can be overridden and shared libraries enabled by setting the `CRAYPE_LINK_TYPE` environment variable to `dynamic`.

Running CMake without specifying [`CMAKE_SYSTEM_NAME`](https://cmake.org/cmake/help/latest/variable/CMAKE_SYSTEM_NAME.html#variable:CMAKE_SYSTEM_NAME "CMAKE_SYSTEM_NAME") will run the configure step in host mode assuming a standard Linux environment. If not overridden, the `PrgEnv-*` compiler wrappers will end up getting used, which if targeting the either the login node or compute node, is likely not the desired behavior. The exception to this would be if you are building directly on a NID instead of cross-compiling from a login node. If trying to build software for a login node, you will need to either first unload the currently loaded `PrgEnv-*` module or explicitly tell CMake to use the system compilers in `/usr/bin` instead of the Cray wrappers. If instead targeting a compute node is desired, just specify the [`CMAKE_SYSTEM_NAME`](https://cmake.org/cmake/help/latest/variable/CMAKE_SYSTEM_NAME.html#variable:CMAKE_SYSTEM_NAME "CMAKE_SYSTEM_NAME") as mentioned above.

### [Cross Compiling using Clang](https://cmake.org/cmake/help/latest/manual/cmake-toolchains.7.html#id17)[¶](https://cmake.org/cmake/help/latest/manual/cmake-toolchains.7.html#cross-compiling-using-clang "Link to this heading")

Some compilers such as Clang are inherently cross compilers. The [`CMAKE_<LANG>_COMPILER_TARGET`](https://cmake.org/cmake/help/latest/variable/CMAKE_LANG_COMPILER_TARGET.html#variable:CMAKE_%3CLANG%3E_COMPILER_TARGET "CMAKE_<LANG>_COMPILER_TARGET") can be set to pass a value to those supported compilers when compiling:

set(CMAKE_SYSTEM_NAME Linux)
set(CMAKE_SYSTEM_PROCESSOR arm)

set(triple arm-linux-gnueabihf)

set(CMAKE_C_COMPILER clang)
set(CMAKE_C_COMPILER_TARGET ${triple})
set(CMAKE_CXX_COMPILER clang++)
set(CMAKE_CXX_COMPILER_TARGET ${triple})

Similarly, some compilers do not ship their own supplementary utilities such as linkers, but provide a way to specify the location of the external toolchain which will be used by the compiler driver. The [`CMAKE_<LANG>_COMPILER_EXTERNAL_TOOLCHAIN`](https://cmake.org/cmake/help/latest/variable/CMAKE_LANG_COMPILER_EXTERNAL_TOOLCHAIN.html#variable:CMAKE_%3CLANG%3E_COMPILER_EXTERNAL_TOOLCHAIN "CMAKE_<LANG>_COMPILER_EXTERNAL_TOOLCHAIN") variable can be set in a toolchain file to pass the path to the compiler driver.

### [Cross Compiling for QNX](https://cmake.org/cmake/help/latest/manual/cmake-toolchains.7.html#id18)[¶](https://cmake.org/cmake/help/latest/manual/cmake-toolchains.7.html#cross-compiling-for-qnx "Link to this heading")

As the Clang compiler the QNX QCC compile is inherently a cross compiler. And the [`CMAKE_<LANG>_COMPILER_TARGET`](https://cmake.org/cmake/help/latest/variable/CMAKE_LANG_COMPILER_TARGET.html#variable:CMAKE_%3CLANG%3E_COMPILER_TARGET "CMAKE_<LANG>_COMPILER_TARGET") can be set to pass a value to those supported compilers when compiling:

set(CMAKE_SYSTEM_NAME QNX)

set(arch gcc_ntoaarch64)

set(CMAKE_C_COMPILER qcc)
set(CMAKE_C_COMPILER_TARGET ${arch})
set(CMAKE_CXX_COMPILER q++)
set(CMAKE_CXX_COMPILER_TARGET ${arch})

set(CMAKE_SYSROOT $ENV{QNX_TARGET})

### [Cross Compiling for Windows CE](https://cmake.org/cmake/help/latest/manual/cmake-toolchains.7.html#id19)[¶](https://cmake.org/cmake/help/latest/manual/cmake-toolchains.7.html#cross-compiling-for-windows-ce "Link to this heading")

Cross compiling for Windows CE requires the corresponding SDK being installed on your system. These SDKs are usually installed under `C:/Program Files (x86)/Windows CE Tools/SDKs`.

A toolchain file to configure [Visual Studio Generators](https://cmake.org/cmake/help/latest/manual/cmake-generators.7.html#visual-studio-generators) for Windows CE may look like this:

set(CMAKE_SYSTEM_NAME WindowsCE)

set(CMAKE_SYSTEM_VERSION 8.0)
set(CMAKE_SYSTEM_PROCESSOR arm)

set(CMAKE_GENERATOR_TOOLSET CE800) # Can be omitted for 8.0
set(CMAKE_GENERATOR_PLATFORM SDK_AM335X_SK_WEC2013_V310)

The [`CMAKE_GENERATOR_PLATFORM`](https://cmake.org/cmake/help/latest/variable/CMAKE_GENERATOR_PLATFORM.html#variable:CMAKE_GENERATOR_PLATFORM "CMAKE_GENERATOR_PLATFORM") tells the generator which SDK to use. Further [`CMAKE_SYSTEM_VERSION`](https://cmake.org/cmake/help/latest/variable/CMAKE_SYSTEM_VERSION.html#variable:CMAKE_SYSTEM_VERSION "CMAKE_SYSTEM_VERSION") tells the generator what version of Windows CE to use. Currently version 8.0 (Windows Embedded Compact 2013) is supported out of the box. Other versions may require one to set [`CMAKE_GENERATOR_TOOLSET`](https://cmake.org/cmake/help/latest/variable/CMAKE_GENERATOR_TOOLSET.html#variable:CMAKE_GENERATOR_TOOLSET "CMAKE_GENERATOR_TOOLSET") to the correct value.

### [Cross Compiling for Windows 10 Universal Applications](https://cmake.org/cmake/help/latest/manual/cmake-toolchains.7.html#id20)[¶](https://cmake.org/cmake/help/latest/manual/cmake-toolchains.7.html#cross-compiling-for-windows-10-universal-applications "Link to this heading")

A toolchain file to configure [Visual Studio Generators](https://cmake.org/cmake/help/latest/manual/cmake-generators.7.html#visual-studio-generators) for a Windows 10 Universal Application may look like this:

set(CMAKE_SYSTEM_NAME WindowsStore)
set(CMAKE_SYSTEM_VERSION 10.0)

A Windows 10 Universal Application targets both Windows Store and Windows Phone. Specify the [`CMAKE_SYSTEM_VERSION`](https://cmake.org/cmake/help/latest/variable/CMAKE_SYSTEM_VERSION.html#variable:CMAKE_SYSTEM_VERSION "CMAKE_SYSTEM_VERSION") variable to be `10.0` or higher.

CMake selects a Windows SDK as described by documentation of the [`CMAKE_VS_WINDOWS_TARGET_PLATFORM_VERSION`](https://cmake.org/cmake/help/latest/variable/CMAKE_VS_WINDOWS_TARGET_PLATFORM_VERSION.html#variable:CMAKE_VS_WINDOWS_TARGET_PLATFORM_VERSION "CMAKE_VS_WINDOWS_TARGET_PLATFORM_VERSION") variable.

### [Cross Compiling for Windows Phone](https://cmake.org/cmake/help/latest/manual/cmake-toolchains.7.html#id21)[¶](https://cmake.org/cmake/help/latest/manual/cmake-toolchains.7.html#cross-compiling-for-windows-phone "Link to this heading")

A toolchain file to configure [Visual Studio Generators](https://cmake.org/cmake/help/latest/manual/cmake-generators.7.html#visual-studio-generators) for Windows Phone may look like this:

set(CMAKE_SYSTEM_NAME WindowsPhone)
set(CMAKE_SYSTEM_VERSION 8.1)

### [Cross Compiling for Windows Store](https://cmake.org/cmake/help/latest/manual/cmake-toolchains.7.html#id22)[¶](https://cmake.org/cmake/help/latest/manual/cmake-toolchains.7.html#cross-compiling-for-windows-store "Link to this heading")

A toolchain file to configure a [Visual Studio Generators](https://cmake.org/cmake/help/latest/manual/cmake-generators.7.html#visual-studio-generators) for Windows Store may look like this:

set(CMAKE_SYSTEM_NAME WindowsStore)
set(CMAKE_SYSTEM_VERSION 8.1)

### [Cross Compiling for ADSP SHARC/Blackfin](https://cmake.org/cmake/help/latest/manual/cmake-toolchains.7.html#id23)[¶](https://cmake.org/cmake/help/latest/manual/cmake-toolchains.7.html#cross-compiling-for-adsp-sharc-blackfin "Link to this heading")

Cross-compiling for ADSP SHARC or Blackfin can be configured by setting the [`CMAKE_SYSTEM_NAME`](https://cmake.org/cmake/help/latest/variable/CMAKE_SYSTEM_NAME.html#variable:CMAKE_SYSTEM_NAME "CMAKE_SYSTEM_NAME") variable to `ADSP` and the [`CMAKE_SYSTEM_PROCESSOR`](https://cmake.org/cmake/help/latest/variable/CMAKE_SYSTEM_PROCESSOR.html#variable:CMAKE_SYSTEM_PROCESSOR "CMAKE_SYSTEM_PROCESSOR") variable to the "part number", excluding the `ADSP-` prefix, for example, `21594`, `SC589`, etc. This value is case insensitive.

CMake will automatically search for CCES or VDSP++ installs in their default install locations and select the most recent version found. CCES will be selected over VDSP++ if both are installed. Custom install paths can be set via the [`CMAKE_ADSP_ROOT`](https://cmake.org/cmake/help/latest/variable/CMAKE_ADSP_ROOT.html#variable:CMAKE_ADSP_ROOT "CMAKE_ADSP_ROOT") variable or the [`ADSP_ROOT`](https://cmake.org/cmake/help/latest/envvar/ADSP_ROOT.html#envvar:ADSP_ROOT "ADSP_ROOT") environment variable.

The compiler (`cc21k` vs. `ccblkfn`) is selected automatically based on the [`CMAKE_SYSTEM_PROCESSOR`](https://cmake.org/cmake/help/latest/variable/CMAKE_SYSTEM_PROCESSOR.html#variable:CMAKE_SYSTEM_PROCESSOR "CMAKE_SYSTEM_PROCESSOR") value provided.

### [Cross Compiling for Android](https://cmake.org/cmake/help/latest/manual/cmake-toolchains.7.html#id24)[¶](https://cmake.org/cmake/help/latest/manual/cmake-toolchains.7.html#cross-compiling-for-android "Link to this heading")

A toolchain file may configure cross-compiling for Android by setting the [`CMAKE_SYSTEM_NAME`](https://cmake.org/cmake/help/latest/variable/CMAKE_SYSTEM_NAME.html#variable:CMAKE_SYSTEM_NAME "CMAKE_SYSTEM_NAME") variable to `Android`. Further configuration is specific to the Android development environment to be used.

For [Visual Studio Generators](https://cmake.org/cmake/help/latest/manual/cmake-generators.7.html#visual-studio-generators), CMake expects [NVIDIA Nsight Tegra Visual Studio Edition](https://cmake.org/cmake/help/latest/manual/cmake-toolchains.7.html#cross-compiling-for-android-with-nvidia-nsight-tegra-visual-studio-edition) or the [Visual Studio tools for Android](https://cmake.org/cmake/help/latest/manual/cmake-toolchains.7.html#cross-compiling-for-android-with-the-ndk) to be installed. See those sections for further configuration details.

For [Makefile Generators](https://cmake.org/cmake/help/latest/manual/cmake-generators.7.html#makefile-generators) and the [`Ninja`](https://cmake.org/cmake/help/latest/generator/Ninja.html#generator:Ninja "Ninja") generator, CMake expects one of these environments:

*   [NDK](https://cmake.org/cmake/help/latest/manual/cmake-toolchains.7.html#cross-compiling-for-android-with-the-ndk)

*   [Standalone Toolchain](https://cmake.org/cmake/help/latest/manual/cmake-toolchains.7.html#cross-compiling-for-android-with-a-standalone-toolchain)

CMake uses the following steps to select one of the environments:

*   If the [`CMAKE_ANDROID_NDK`](https://cmake.org/cmake/help/latest/variable/CMAKE_ANDROID_NDK.html#variable:CMAKE_ANDROID_NDK "CMAKE_ANDROID_NDK") variable is set, the NDK at the specified location will be used.

*   Else, if the [`CMAKE_ANDROID_STANDALONE_TOOLCHAIN`](https://cmake.org/cmake/help/latest/variable/CMAKE_ANDROID_STANDALONE_TOOLCHAIN.html#variable:CMAKE_ANDROID_STANDALONE_TOOLCHAIN "CMAKE_ANDROID_STANDALONE_TOOLCHAIN") variable is set, the Standalone Toolchain at the specified location will be used.

*   Else, if the [`CMAKE_SYSROOT`](https://cmake.org/cmake/help/latest/variable/CMAKE_SYSROOT.html#variable:CMAKE_SYSROOT "CMAKE_SYSROOT") variable is set to a directory of the form `<ndk>/platforms/android-<api>/arch-<arch>`, the `<ndk>` part will be used as the value of [`CMAKE_ANDROID_NDK`](https://cmake.org/cmake/help/latest/variable/CMAKE_ANDROID_NDK.html#variable:CMAKE_ANDROID_NDK "CMAKE_ANDROID_NDK") and the NDK will be used.

*   Else, if the [`CMAKE_SYSROOT`](https://cmake.org/cmake/help/latest/variable/CMAKE_SYSROOT.html#variable:CMAKE_SYSROOT "CMAKE_SYSROOT") variable is set to a directory of the form `<standalone-toolchain>/sysroot`, the `<standalone-toolchain>` part will be used as the value of [`CMAKE_ANDROID_STANDALONE_TOOLCHAIN`](https://cmake.org/cmake/help/latest/variable/CMAKE_ANDROID_STANDALONE_TOOLCHAIN.html#variable:CMAKE_ANDROID_STANDALONE_TOOLCHAIN "CMAKE_ANDROID_STANDALONE_TOOLCHAIN") and the Standalone Toolchain will be used.

*   Else, if a cmake variable `ANDROID_NDK` is set it will be used as the value of [`CMAKE_ANDROID_NDK`](https://cmake.org/cmake/help/latest/variable/CMAKE_ANDROID_NDK.html#variable:CMAKE_ANDROID_NDK "CMAKE_ANDROID_NDK"), and the NDK will be used.

*   Else, if a cmake variable `ANDROID_STANDALONE_TOOLCHAIN` is set, it will be used as the value of [`CMAKE_ANDROID_STANDALONE_TOOLCHAIN`](https://cmake.org/cmake/help/latest/variable/CMAKE_ANDROID_STANDALONE_TOOLCHAIN.html#variable:CMAKE_ANDROID_STANDALONE_TOOLCHAIN "CMAKE_ANDROID_STANDALONE_TOOLCHAIN"), and the Standalone Toolchain will be used.

*   Else, if an environment variable `ANDROID_NDK_ROOT` or `ANDROID_NDK` is set, it will be used as the value of [`CMAKE_ANDROID_NDK`](https://cmake.org/cmake/help/latest/variable/CMAKE_ANDROID_NDK.html#variable:CMAKE_ANDROID_NDK "CMAKE_ANDROID_NDK"), and the NDK will be used.

*   Else, if an environment variable `ANDROID_STANDALONE_TOOLCHAIN` is set then it will be used as the value of [`CMAKE_ANDROID_STANDALONE_TOOLCHAIN`](https://cmake.org/cmake/help/latest/variable/CMAKE_ANDROID_STANDALONE_TOOLCHAIN.html#variable:CMAKE_ANDROID_STANDALONE_TOOLCHAIN "CMAKE_ANDROID_STANDALONE_TOOLCHAIN"), and the Standalone Toolchain will be used.

*   Else, an error diagnostic will be issued that neither the NDK or Standalone Toolchain can be found.

Added in version 3.20: If an Android NDK is selected, its version number is reported in the [`CMAKE_ANDROID_NDK_VERSION`](https://cmake.org/cmake/help/latest/variable/CMAKE_ANDROID_NDK_VERSION.html#variable:CMAKE_ANDROID_NDK_VERSION "CMAKE_ANDROID_NDK_VERSION") variable.

#### [Cross Compiling for Android with the NDK](https://cmake.org/cmake/help/latest/manual/cmake-toolchains.7.html#id25)[¶](https://cmake.org/cmake/help/latest/manual/cmake-toolchains.7.html#cross-compiling-for-android-with-the-ndk "Link to this heading")

A toolchain file may configure [Makefile Generators](https://cmake.org/cmake/help/latest/manual/cmake-generators.7.html#makefile-generators), [Ninja Generators](https://cmake.org/cmake/help/latest/manual/cmake-generators.7.html#ninja-generators), or [Visual Studio Generators](https://cmake.org/cmake/help/latest/manual/cmake-generators.7.html#visual-studio-generators) to target Android for cross-compiling.

Configure use of an Android NDK with the following variables:

[`CMAKE_SYSTEM_NAME`](https://cmake.org/cmake/help/latest/variable/CMAKE_SYSTEM_NAME.html#variable:CMAKE_SYSTEM_NAME "CMAKE_SYSTEM_NAME")
Set to `Android`. Must be specified to enable cross compiling for Android.

[`CMAKE_SYSTEM_VERSION`](https://cmake.org/cmake/help/latest/variable/CMAKE_SYSTEM_VERSION.html#variable:CMAKE_SYSTEM_VERSION "CMAKE_SYSTEM_VERSION")
Set to the Android API level. If not specified, the value is determined as follows:

*   If the [`CMAKE_ANDROID_API`](https://cmake.org/cmake/help/latest/variable/CMAKE_ANDROID_API.html#variable:CMAKE_ANDROID_API "CMAKE_ANDROID_API") variable is set, its value is used as the API level.

*   If the [`CMAKE_SYSROOT`](https://cmake.org/cmake/help/latest/variable/CMAKE_SYSROOT.html#variable:CMAKE_SYSROOT "CMAKE_SYSROOT") variable is set, the API level is detected from the NDK directory structure containing the sysroot.

*   Otherwise, the latest API level available in the NDK is used.

[`CMAKE_ANDROID_ARCH_ABI`](https://cmake.org/cmake/help/latest/variable/CMAKE_ANDROID_ARCH_ABI.html#variable:CMAKE_ANDROID_ARCH_ABI "CMAKE_ANDROID_ARCH_ABI")
Set to the Android ABI (architecture). If not specified, this variable will default to the first supported ABI in the list of `armeabi`, `armeabi-v7a` and `arm64-v8a`. The [`CMAKE_ANDROID_ARCH`](https://cmake.org/cmake/help/latest/variable/CMAKE_ANDROID_ARCH.html#variable:CMAKE_ANDROID_ARCH "CMAKE_ANDROID_ARCH") variable will be computed from `CMAKE_ANDROID_ARCH_ABI` automatically. Also see the [`CMAKE_ANDROID_ARM_MODE`](https://cmake.org/cmake/help/latest/variable/CMAKE_ANDROID_ARM_MODE.html#variable:CMAKE_ANDROID_ARM_MODE "CMAKE_ANDROID_ARM_MODE") and [`CMAKE_ANDROID_ARM_NEON`](https://cmake.org/cmake/help/latest/variable/CMAKE_ANDROID_ARM_NEON.html#variable:CMAKE_ANDROID_ARM_NEON "CMAKE_ANDROID_ARM_NEON") variables.

[`CMAKE_ANDROID_NDK`](https://cmake.org/cmake/help/latest/variable/CMAKE_ANDROID_NDK.html#variable:CMAKE_ANDROID_NDK "CMAKE_ANDROID_NDK")
Set to the absolute path to the Android NDK root directory. If not specified, a default for this variable will be chosen as specified [above](https://cmake.org/cmake/help/latest/manual/cmake-toolchains.7.html#cross-compiling-for-android).

[`CMAKE_ANDROID_NDK_DEPRECATED_HEADERS`](https://cmake.org/cmake/help/latest/variable/CMAKE_ANDROID_NDK_DEPRECATED_HEADERS.html#variable:CMAKE_ANDROID_NDK_DEPRECATED_HEADERS "CMAKE_ANDROID_NDK_DEPRECATED_HEADERS")
Set to a true value to use the deprecated per-api-level headers instead of the unified headers. If not specified, the default will be false unless using a NDK that does not provide unified headers.

[`CMAKE_ANDROID_NDK_TOOLCHAIN_VERSION`](https://cmake.org/cmake/help/latest/variable/CMAKE_ANDROID_NDK_TOOLCHAIN_VERSION.html#variable:CMAKE_ANDROID_NDK_TOOLCHAIN_VERSION "CMAKE_ANDROID_NDK_TOOLCHAIN_VERSION")
On NDK r19 or above, this variable must be unset or set to `clang`. On NDK r18 or below, set this to the version of the NDK toolchain to be selected as the compiler. If not specified, the default will be the latest available GCC toolchain.

[`CMAKE_ANDROID_STL_TYPE`](https://cmake.org/cmake/help/latest/variable/CMAKE_ANDROID_STL_TYPE.html#variable:CMAKE_ANDROID_STL_TYPE "CMAKE_ANDROID_STL_TYPE")
Set to specify which C++ standard library to use. If not specified, a default will be selected as described in the variable documentation.

The following variables will be computed and provided automatically:

[`CMAKE_<LANG>_ANDROID_TOOLCHAIN_PREFIX`](https://cmake.org/cmake/help/latest/variable/CMAKE_LANG_ANDROID_TOOLCHAIN_PREFIX.html#variable:CMAKE_%3CLANG%3E_ANDROID_TOOLCHAIN_PREFIX "CMAKE_<LANG>_ANDROID_TOOLCHAIN_PREFIX")
The absolute path prefix to the binutils in the NDK toolchain.

[`CMAKE_<LANG>_ANDROID_TOOLCHAIN_SUFFIX`](https://cmake.org/cmake/help/latest/variable/CMAKE_LANG_ANDROID_TOOLCHAIN_SUFFIX.html#variable:CMAKE_%3CLANG%3E_ANDROID_TOOLCHAIN_SUFFIX "CMAKE_<LANG>_ANDROID_TOOLCHAIN_SUFFIX")
The host platform suffix of the binutils in the NDK toolchain.

For example, a toolchain file might contain:

set(CMAKE_SYSTEM_NAME Android)
set(CMAKE_SYSTEM_VERSION 21) # API level
set(CMAKE_ANDROID_ARCH_ABI arm64-v8a)
set(CMAKE_ANDROID_NDK /path/to/android-ndk)
set(CMAKE_ANDROID_STL_TYPE gnustl_static)

Alternatively one may specify the values without a toolchain file:

$ cmake ../src \
 -DCMAKE_SYSTEM_NAME=Android \
 -DCMAKE_SYSTEM_VERSION=21 \
 -DCMAKE_ANDROID_ARCH_ABI=arm64-v8a \
 -DCMAKE_ANDROID_NDK=/path/to/android-ndk \
 -DCMAKE_ANDROID_STL_TYPE=gnustl_static

#### [Cross Compiling for Android with a Standalone Toolchain](https://cmake.org/cmake/help/latest/manual/cmake-toolchains.7.html#id26)[¶](https://cmake.org/cmake/help/latest/manual/cmake-toolchains.7.html#cross-compiling-for-android-with-a-standalone-toolchain "Link to this heading")

A toolchain file may configure [Makefile Generators](https://cmake.org/cmake/help/latest/manual/cmake-generators.7.html#makefile-generators) or the [`Ninja`](https://cmake.org/cmake/help/latest/generator/Ninja.html#generator:Ninja "Ninja") generator to target Android for cross-compiling using a standalone toolchain.

Configure use of an Android standalone toolchain with the following variables:

[`CMAKE_SYSTEM_NAME`](https://cmake.org/cmake/help/latest/variable/CMAKE_SYSTEM_NAME.html#variable:CMAKE_SYSTEM_NAME "CMAKE_SYSTEM_NAME")
Set to `Android`. Must be specified to enable cross compiling for Android.

[`CMAKE_ANDROID_STANDALONE_TOOLCHAIN`](https://cmake.org/cmake/help/latest/variable/CMAKE_ANDROID_STANDALONE_TOOLCHAIN.html#variable:CMAKE_ANDROID_STANDALONE_TOOLCHAIN "CMAKE_ANDROID_STANDALONE_TOOLCHAIN")
Set to the absolute path to the standalone toolchain root directory. A `${CMAKE_ANDROID_STANDALONE_TOOLCHAIN}/sysroot` directory must exist. If not specified, a default for this variable will be chosen as specified [above](https://cmake.org/cmake/help/latest/manual/cmake-toolchains.7.html#cross-compiling-for-android).

[`CMAKE_ANDROID_ARM_MODE`](https://cmake.org/cmake/help/latest/variable/CMAKE_ANDROID_ARM_MODE.html#variable:CMAKE_ANDROID_ARM_MODE "CMAKE_ANDROID_ARM_MODE")
When the standalone toolchain targets ARM, optionally set this to `ON` to target 32-bit ARM instead of 16-bit Thumb. See variable documentation for details.

[`CMAKE_ANDROID_ARM_NEON`](https://cmake.org/cmake/help/latest/variable/CMAKE_ANDROID_ARM_NEON.html#variable:CMAKE_ANDROID_ARM_NEON "CMAKE_ANDROID_ARM_NEON")
When the standalone toolchain targets ARM v7, optionally set thisto `ON` to target ARM NEON devices. See variable documentation for details.

The following variables will be computed and provided automatically:

[`CMAKE_SYSTEM_VERSION`](https://cmake.org/cmake/help/latest/variable/CMAKE_SYSTEM_VERSION.html#variable:CMAKE_SYSTEM_VERSION "CMAKE_SYSTEM_VERSION")
The Android API level detected from the standalone toolchain.

[`CMAKE_ANDROID_ARCH_ABI`](https://cmake.org/cmake/help/latest/variable/CMAKE_ANDROID_ARCH_ABI.html#variable:CMAKE_ANDROID_ARCH_ABI "CMAKE_ANDROID_ARCH_ABI")
The Android ABI detected from the standalone toolchain.

[`CMAKE_<LANG>_ANDROID_TOOLCHAIN_PREFIX`](https://cmake.org/cmake/help/latest/variable/CMAKE_LANG_ANDROID_TOOLCHAIN_PREFIX.html#variable:CMAKE_%3CLANG%3E_ANDROID_TOOLCHAIN_PREFIX "CMAKE_<LANG>_ANDROID_TOOLCHAIN_PREFIX")
The absolute path prefix to the `binutils` in the standalone toolchain.

[`CMAKE_<LANG>_ANDROID_TOOLCHAIN_SUFFIX`](https://cmake.org/cmake/help/latest/variable/CMAKE_LANG_ANDROID_TOOLCHAIN_SUFFIX.html#variable:CMAKE_%3CLANG%3E_ANDROID_TOOLCHAIN_SUFFIX "CMAKE_<LANG>_ANDROID_TOOLCHAIN_SUFFIX")
The host platform suffix of the `binutils` in the standalone toolchain.

For example, a toolchain file might contain:

set(CMAKE_SYSTEM_NAME Android)
set(CMAKE_ANDROID_STANDALONE_TOOLCHAIN /path/to/android-toolchain)

Alternatively one may specify the values without a toolchain file:

$ cmake ../src \
 -DCMAKE_SYSTEM_NAME=Android \
 -DCMAKE_ANDROID_STANDALONE_TOOLCHAIN=/path/to/android-toolchain

#### [Cross Compiling for Android with NVIDIA Nsight Tegra Visual Studio Edition](https://cmake.org/cmake/help/latest/manual/cmake-toolchains.7.html#id27)[¶](https://cmake.org/cmake/help/latest/manual/cmake-toolchains.7.html#cross-compiling-for-android-with-nvidia-nsight-tegra-visual-studio-edition "Link to this heading")

A toolchain file to configure one of the [Visual Studio Generators](https://cmake.org/cmake/help/latest/manual/cmake-generators.7.html#visual-studio-generators) to build using NVIDIA Nsight Tegra targeting Android may look like this:

set(CMAKE_SYSTEM_NAME Android)

The [`CMAKE_GENERATOR_TOOLSET`](https://cmake.org/cmake/help/latest/variable/CMAKE_GENERATOR_TOOLSET.html#variable:CMAKE_GENERATOR_TOOLSET "CMAKE_GENERATOR_TOOLSET") may be set to select the Nsight Tegra "Toolchain Version" value.

See also target properties:

*   [`ANDROID_ANT_ADDITIONAL_OPTIONS`](https://cmake.org/cmake/help/latest/prop_tgt/ANDROID_ANT_ADDITIONAL_OPTIONS.html#prop_tgt:ANDROID_ANT_ADDITIONAL_OPTIONS "ANDROID_ANT_ADDITIONAL_OPTIONS")

*   [`ANDROID_API_MIN`](https://cmake.org/cmake/help/latest/prop_tgt/ANDROID_API_MIN.html#prop_tgt:ANDROID_API_MIN "ANDROID_API_MIN")

*   [`ANDROID_API`](https://cmake.org/cmake/help/latest/prop_tgt/ANDROID_API.html#prop_tgt:ANDROID_API "ANDROID_API")

*   [`ANDROID_ARCH`](https://cmake.org/cmake/help/latest/prop_tgt/ANDROID_ARCH.html#prop_tgt:ANDROID_ARCH "ANDROID_ARCH")

*   [`ANDROID_ASSETS_DIRECTORIES`](https://cmake.org/cmake/help/latest/prop_tgt/ANDROID_ASSETS_DIRECTORIES.html#prop_tgt:ANDROID_ASSETS_DIRECTORIES "ANDROID_ASSETS_DIRECTORIES")

*   [`ANDROID_GUI`](https://cmake.org/cmake/help/latest/prop_tgt/ANDROID_GUI.html#prop_tgt:ANDROID_GUI "ANDROID_GUI")

*   [`ANDROID_JAR_DEPENDENCIES`](https://cmake.org/cmake/help/latest/prop_tgt/ANDROID_JAR_DEPENDENCIES.html#prop_tgt:ANDROID_JAR_DEPENDENCIES "ANDROID_JAR_DEPENDENCIES")

*   [`ANDROID_JAR_DIRECTORIES`](https://cmake.org/cmake/help/latest/prop_tgt/ANDROID_JAR_DIRECTORIES.html#prop_tgt:ANDROID_JAR_DIRECTORIES "ANDROID_JAR_DIRECTORIES")

*   [`ANDROID_JAVA_SOURCE_DIR`](https://cmake.org/cmake/help/latest/prop_tgt/ANDROID_JAVA_SOURCE_DIR.html#prop_tgt:ANDROID_JAVA_SOURCE_DIR "ANDROID_JAVA_SOURCE_DIR")

*   [`ANDROID_NATIVE_LIB_DEPENDENCIES`](https://cmake.org/cmake/help/latest/prop_tgt/ANDROID_NATIVE_LIB_DEPENDENCIES.html#prop_tgt:ANDROID_NATIVE_LIB_DEPENDENCIES "ANDROID_NATIVE_LIB_DEPENDENCIES")

*   [`ANDROID_NATIVE_LIB_DIRECTORIES`](https://cmake.org/cmake/help/latest/prop_tgt/ANDROID_NATIVE_LIB_DIRECTORIES.html#prop_tgt:ANDROID_NATIVE_LIB_DIRECTORIES "ANDROID_NATIVE_LIB_DIRECTORIES")

*   [`ANDROID_PROCESS_MAX`](https://cmake.org/cmake/help/latest/prop_tgt/ANDROID_PROCESS_MAX.html#prop_tgt:ANDROID_PROCESS_MAX "ANDROID_PROCESS_MAX")

*   [`ANDROID_PROGUARD_CONFIG_PATH`](https://cmake.org/cmake/help/latest/prop_tgt/ANDROID_PROGUARD_CONFIG_PATH.html#prop_tgt:ANDROID_PROGUARD_CONFIG_PATH "ANDROID_PROGUARD_CONFIG_PATH")

*   [`ANDROID_PROGUARD`](https://cmake.org/cmake/help/latest/prop_tgt/ANDROID_PROGUARD.html#prop_tgt:ANDROID_PROGUARD "ANDROID_PROGUARD")

*   [`ANDROID_SECURE_PROPS_PATH`](https://cmake.org/cmake/help/latest/prop_tgt/ANDROID_SECURE_PROPS_PATH.html#prop_tgt:ANDROID_SECURE_PROPS_PATH "ANDROID_SECURE_PROPS_PATH")

*   [`ANDROID_SKIP_ANT_STEP`](https://cmake.org/cmake/help/latest/prop_tgt/ANDROID_SKIP_ANT_STEP.html#prop_tgt:ANDROID_SKIP_ANT_STEP "ANDROID_SKIP_ANT_STEP")

*   [`ANDROID_STL_TYPE`](https://cmake.org/cmake/help/latest/prop_tgt/ANDROID_STL_TYPE.html#prop_tgt:ANDROID_STL_TYPE "ANDROID_STL_TYPE")

### [Cross Compiling for iOS, tvOS, visionOS, or watchOS](https://cmake.org/cmake/help/latest/manual/cmake-toolchains.7.html#id28)[¶](https://cmake.org/cmake/help/latest/manual/cmake-toolchains.7.html#cross-compiling-for-ios-tvos-visionos-or-watchos "Link to this heading")

For cross-compiling to iOS, tvOS, visionOS, or watchOS, the [`Xcode`](https://cmake.org/cmake/help/latest/generator/Xcode.html#generator:Xcode "Xcode") generator is recommended. The [`Unix Makefiles`](https://cmake.org/cmake/help/latest/generator/Unix%20Makefiles.html#generator:Unix%20Makefiles "Unix Makefiles") or [`Ninja`](https://cmake.org/cmake/help/latest/generator/Ninja.html#generator:Ninja "Ninja") generators can also be used, but they require the project to handle more areas like target CPU selection and code signing.

Any of the Apple device platforms can be targeted by setting the [`CMAKE_SYSTEM_NAME`](https://cmake.org/cmake/help/latest/variable/CMAKE_SYSTEM_NAME.html#variable:CMAKE_SYSTEM_NAME "CMAKE_SYSTEM_NAME") variable to a value from the table below. By default, the latest Device SDK is chosen. As for all Apple platforms, a different SDK (e.g. a simulator) can be selected by setting the [`CMAKE_OSX_SYSROOT`](https://cmake.org/cmake/help/latest/variable/CMAKE_OSX_SYSROOT.html#variable:CMAKE_OSX_SYSROOT "CMAKE_OSX_SYSROOT") variable, although this should rarely be necessary (see [Switching Between Device and Simulator](https://cmake.org/cmake/help/latest/manual/cmake-toolchains.7.html#switching-between-device-and-simulator) below). A list of available SDKs can be obtained by running `xcodebuild -showsdks`.

| OS | CMAKE_SYSTEM_NAME | Device SDK (default) | Simulator SDK | Catalyst SDK |
| --- | --- | --- | --- | --- |
| iOS | iOS | iphoneos | iphonesimulator | macosx |
| tvOS | tvOS | appletvos | appletvsimulator | N/A |
| visionOS | visionOS | xros | xrsimulator | N/A |
| watchOS | watchOS | watchos | watchsimulator | N/A |

For example, to create a CMake configuration for iOS, the following command is sufficient:

cmake .. -GXcode -DCMAKE_SYSTEM_NAME=iOS

Variable [`CMAKE_OSX_ARCHITECTURES`](https://cmake.org/cmake/help/latest/variable/CMAKE_OSX_ARCHITECTURES.html#variable:CMAKE_OSX_ARCHITECTURES "CMAKE_OSX_ARCHITECTURES") can be used to set architectures for both device and simulator. Variable [`CMAKE_OSX_DEPLOYMENT_TARGET`](https://cmake.org/cmake/help/latest/variable/CMAKE_OSX_DEPLOYMENT_TARGET.html#variable:CMAKE_OSX_DEPLOYMENT_TARGET "CMAKE_OSX_DEPLOYMENT_TARGET") can be used to set an iOS/tvOS/visionOS/watchOS deployment target.

The next example installs five architectures in a universal binary for an iOS library. It adds the relevant `-miphoneos-version-min=9.3` or `-mios-simulator-version-min=9.3` compiler flag where appropriate. Note that the [`CMAKE_IOS_INSTALL_COMBINED`](https://cmake.org/cmake/help/latest/variable/CMAKE_IOS_INSTALL_COMBINED.html#variable:CMAKE_IOS_INSTALL_COMBINED "CMAKE_IOS_INSTALL_COMBINED") variable used in the example is now deprecated, so this approach is no longer recommended.

$ cmake -S. -B_builds -GXcode \
 -DCMAKE_SYSTEM_NAME=iOS \
 "-DCMAKE_OSX_ARCHITECTURES=armv7;armv7s;arm64;i386;x86_64" \
 -DCMAKE_OSX_DEPLOYMENT_TARGET=9.3 \
 -DCMAKE_INSTALL_PREFIX=`pwd`/_install \
 -DCMAKE_XCODE_ATTRIBUTE_ONLY_ACTIVE_ARCH=NO \
 -DCMAKE_IOS_INSTALL_COMBINED=YES

Example:

# CMakeLists.txt
cmake_minimum_required(VERSION 3.14)
project(foo)
add_library(foo foo.cpp)
install(TARGETS foo DESTINATION lib)

Install:

$ cmake --build _builds --config Release --target install

Check library:

$ lipo -info _install/lib/libfoo.a
Architectures in the fat file: _install/lib/libfoo.a are: i386 armv7 armv7s x86_64 arm64

$ otool -l _install/lib/libfoo.a | grep -A2 LC_VERSION_MIN_IPHONEOS
 cmd LC_VERSION_MIN_IPHONEOS
 cmdsize 16
 version 9.3

#### [Code Signing](https://cmake.org/cmake/help/latest/manual/cmake-toolchains.7.html#id29)[¶](https://cmake.org/cmake/help/latest/manual/cmake-toolchains.7.html#code-signing "Link to this heading")

Some build artifacts for the embedded Apple platforms require mandatory code signing. If the [`Xcode`](https://cmake.org/cmake/help/latest/generator/Xcode.html#generator:Xcode "Xcode") generator is being used and code signing is required or desired, the development team ID can be specified via the `CMAKE_XCODE_ATTRIBUTE_DEVELOPMENT_TEAM` CMake variable. This team ID will then be included in the generated Xcode project. By default, CMake avoids the need for code signing during the internal configuration phase (i.e compiler ID and feature detection).

#### [Switching Between Device and Simulator](https://cmake.org/cmake/help/latest/manual/cmake-toolchains.7.html#id30)[¶](https://cmake.org/cmake/help/latest/manual/cmake-toolchains.7.html#switching-between-device-and-simulator "Link to this heading")

When configuring for any of the embedded platforms, one can target either real devices or the simulator. Both have their own separate SDK, but CMake only supports specifying a single SDK for the configuration phase. This means the developer must select one or the other at configuration time. When using the [`Xcode`](https://cmake.org/cmake/help/latest/generator/Xcode.html#generator:Xcode "Xcode") generator, this is less of a limitation because Xcode still allows you to build for either a device or a simulator, even though configuration was only performed for one of the two. From within the Xcode IDE, builds are performed for the selected "destination" platform. When building from the command line, the desired sdk can be specified directly by passing a `-sdk` option to the underlying build tool (`xcodebuild`). For example:

$ cmake --build ... -- -sdk iphonesimulator

Please note that checks made during configuration were performed against the configure-time SDK and might not hold true for other SDKs. Commands like [`find_package()`](https://cmake.org/cmake/help/latest/command/find_package.html#command:find_package "find_package"), [`find_library()`](https://cmake.org/cmake/help/latest/command/find_library.html#command:find_library "find_library"), etc. store and use details only for the configured SDK/platform, so they can be problematic if wanting to switch between device and simulator builds. You can follow the next rules to make device + simulator configuration work:

*   Use explicit `-l` linker flag, e.g. `target_link_libraries(foo PUBLIC "-lz")`

*   Use explicit `-framework` linker flag, e.g. `target_link_libraries(foo PUBLIC "-framework CoreFoundation")`

*   Use [`find_package()`](https://cmake.org/cmake/help/latest/command/find_package.html#command:find_package "find_package") only for libraries installed with [`CMAKE_IOS_INSTALL_COMBINED`](https://cmake.org/cmake/help/latest/variable/CMAKE_IOS_INSTALL_COMBINED.html#variable:CMAKE_IOS_INSTALL_COMBINED "CMAKE_IOS_INSTALL_COMBINED") feature

### [Cross Compiling for Emscripten](https://cmake.org/cmake/help/latest/manual/cmake-toolchains.7.html#id31)[¶](https://cmake.org/cmake/help/latest/manual/cmake-toolchains.7.html#cross-compiling-for-emscripten "Link to this heading")

Added in version 4.2.

A toolchain file may configure cross-compiling for [Emscripten](https://emscripten.org/) by setting the [`CMAKE_SYSTEM_NAME`](https://cmake.org/cmake/help/latest/variable/CMAKE_SYSTEM_NAME.html#variable:CMAKE_SYSTEM_NAME "CMAKE_SYSTEM_NAME") variable to `Emscripten`. For example, a toolchain file might contain:

set(CMAKE_SYSTEM_NAME Emscripten)
set(CMAKE_C_COMPILER /path/to/emcc)
set(CMAKE_CXX_COMPILER /path/to/em++)

### [Cross Compiling using Renesas compilers](https://cmake.org/cmake/help/latest/manual/cmake-toolchains.7.html#id32)[¶](https://cmake.org/cmake/help/latest/manual/cmake-toolchains.7.html#cross-compiling-using-renesas-compilers "Link to this heading")

For cross-compiling with Renesas compilers, specify at least:

[`CMAKE_SYSTEM_NAME`](https://cmake.org/cmake/help/latest/variable/CMAKE_SYSTEM_NAME.html#variable:CMAKE_SYSTEM_NAME "CMAKE_SYSTEM_NAME")
Set to `Generic`. Must be specified to enable cross compiling.

[`CMAKE_C_COMPILER`](https://cmake.org/cmake/help/latest/variable/CMAKE_LANG_COMPILER.html#variable:CMAKE_%3CLANG%3E_COMPILER "CMAKE_<LANG>_COMPILER")
Set to the path to the Renesas C compiler, e.g., `ccrx`, `ccrl`, or `ccrh`.

[`CMAKE_C_FLAGS`](https://cmake.org/cmake/help/latest/variable/CMAKE_LANG_FLAGS.html#variable:CMAKE_%3CLANG%3E_FLAGS "CMAKE_<LANG>_FLAGS")
Set to the `-isa=` or `-cpu=` flag the compiler requires.

See example toolchain files in the following sections.

#### [Renesas CC-RX](https://cmake.org/cmake/help/latest/manual/cmake-toolchains.7.html#id33)[¶](https://cmake.org/cmake/help/latest/manual/cmake-toolchains.7.html#renesas-cc-rx "Link to this heading")

set(CMAKE_SYSTEM_NAME Generic)
set(CMAKE_C_COMPILER "ccrx.exe")
set(CMAKE_ASM_COMPILER "ccrx.exe") # if using ASM language
set(CMAKE_C_FLAGS "-isa=rxv3") # specify the version of target RX CPU
set(CMAKE_EXE_LINKER_FLAGS "-lnkopt=<your linker option here>")

#### [Renesas CC-RL](https://cmake.org/cmake/help/latest/manual/cmake-toolchains.7.html#id34)[¶](https://cmake.org/cmake/help/latest/manual/cmake-toolchains.7.html#renesas-cc-rl "Link to this heading")

set(CMAKE_SYSTEM_NAME Generic)
set(CMAKE_C_COMPILER "ccrl.exe")
set(CMAKE_ASM_COMPILER "ccrl.exe") # if using ASM language
set(CMAKE_C_FLAGS "-cpu=S3") # specify the version of target RL CPU
# To avoid test executable runs out of const section's size.
set(CMAKE_TRY_COMPILE_TARGET_TYPE STATIC_LIBRARY)
# Specifying device file and section layout linker options through compiler driver.
set(CMAKE_EXE_LINKER_FLAGS "-lnkopt=-device=dr5f10y14.dvf -lnkopt=-auto_section_layout")

#### [Renesas CC-RH](https://cmake.org/cmake/help/latest/manual/cmake-toolchains.7.html#id35)[¶](https://cmake.org/cmake/help/latest/manual/cmake-toolchains.7.html#renesas-cc-rh "Link to this heading")

set(CMAKE_SYSTEM_NAME Generic)
set(CMAKE_C_COMPILER "ccrh.exe")
set(CMAKE_ASM_COMPILER "ccrh.exe") # if using ASM language
set(CMAKE_C_FLAGS "-Xcommon=rh850") # specify the version of target RH850 CPU
set(CMAKE_EXE_LINKER_FLAGS "-lnkopt=<your linker option here>")

### Table of Contents

*   [cmake-toolchains(7)](https://cmake.org/cmake/help/latest/manual/cmake-toolchains.7.html#)
    *   [Introduction](https://cmake.org/cmake/help/latest/manual/cmake-toolchains.7.html#introduction)
    *   [Languages](https://cmake.org/cmake/help/latest/manual/cmake-toolchains.7.html#languages)
    *   [Variables and Properties](https://cmake.org/cmake/help/latest/manual/cmake-toolchains.7.html#variables-and-properties)
    *   [Toolchain Features](https://cmake.org/cmake/help/latest/manual/cmake-toolchains.7.html#toolchain-features)
    *   [Cross Compiling](https://cmake.org/cmake/help/latest/manual/cmake-toolchains.7.html#cross-compiling)
        *   [Cross Compiling for Linux](https://cmake.org/cmake/help/latest/manual/cmake-toolchains.7.html#cross-compiling-for-linux)
        *   [Cross Compiling for the Cray Linux Environment](https://cmake.org/cmake/help/latest/manual/cmake-toolchains.7.html#cross-compiling-for-the-cray-linux-environment)
        *   [Cross Compiling using Clang](https://cmake.org/cmake/help/latest/manual/cmake-toolchains.7.html#cross-compiling-using-clang)
        *   [Cross Compiling for QNX](https://cmake.org/cmake/help/latest/manual/cmake-toolchains.7.html#cross-compiling-for-qnx)
        *   [Cross Compiling for Windows CE](https://cmake.org/cmake/help/latest/manual/cmake-toolchains.7.html#cross-compiling-for-windows-ce)
        *   [Cross Compiling for Windows 10 Universal Applications](https://cmake.org/cmake/help/latest/manual/cmake-toolchains.7.html#cross-compiling-for-windows-10-universal-applications)
        *   [Cross Compiling for Windows Phone](https://cmake.org/cmake/help/latest/manual/cmake-toolchains.7.html#cross-compiling-for-windows-phone)
        *   [Cross Compiling for Windows Store](https://cmake.org/cmake/help/latest/manual/cmake-toolchains.7.html#cross-compiling-for-windows-store)
        *   [Cross Compiling for ADSP SHARC/Blackfin](https://cmake.org/cmake/help/latest/manual/cmake-toolchains.7.html#cross-compiling-for-adsp-sharc-blackfin)
        *   [Cross Compiling for Android](https://cmake.org/cmake/help/latest/manual/cmake-toolchains.7.html#cross-compiling-for-android)
            *   [Cross Compiling for Android with the NDK](https://cmake.org/cmake/help/latest/manual/cmake-toolchains.7.html#cross-compiling-for-android-with-the-ndk)
            *   [Cross Compiling for Android with a Standalone Toolchain](https://cmake.org/cmake/help/latest/manual/cmake-toolchains.7.html#cross-compiling-for-android-with-a-standalone-toolchain)
            *   [Cross Compiling for Android with NVIDIA Nsight Tegra Visual Studio Edition](https://cmake.org/cmake/help/latest/manual/cmake-toolchains.7.html#cross-compiling-for-android-with-nvidia-nsight-tegra-visual-studio-edition)

        *   [Cross Compiling for iOS, tvOS, visionOS, or watchOS](https://cmake.org/cmake/help/latest/manual/cmake-toolchains.7.html#cross-compiling-for-ios-tvos-visionos-or-watchos)
            *   [Code Signing](https://cmake.org/cmake/help/latest/manual/cmake-toolchains.7.html#code-signing)
            *   [Switching Between Device and Simulator](https://cmake.org/cmake/help/latest/manual/cmake-toolchains.7.html#switching-between-device-and-simulator)

        *   [Cross Compiling for Emscripten](https://cmake.org/cmake/help/latest/manual/cmake-toolchains.7.html#cross-compiling-for-emscripten)
        *   [Cross Compiling using Renesas compilers](https://cmake.org/cmake/help/latest/manual/cmake-toolchains.7.html#cross-compiling-using-renesas-compilers)
            *   [Renesas CC-RX](https://cmake.org/cmake/help/latest/manual/cmake-toolchains.7.html#renesas-cc-rx)
            *   [Renesas CC-RL](https://cmake.org/cmake/help/latest/manual/cmake-toolchains.7.html#renesas-cc-rl)
            *   [Renesas CC-RH](https://cmake.org/cmake/help/latest/manual/cmake-toolchains.7.html#renesas-cc-rh)

#### Previous topic

[cmake-server(7)](https://cmake.org/cmake/help/latest/manual/cmake-server.7.html "previous chapter")

#### Next topic

[cmake-variables(7)](https://cmake.org/cmake/help/latest/manual/cmake-variables.7.html "next chapter")

### This Page

*   [Show Source](https://cmake.org/cmake/help/latest/_sources/manual/cmake-toolchains.7.rst.txt)

### Quick search

### Navigation

*   [index](https://cmake.org/cmake/help/latest/genindex.html "General Index")
*   [next](https://cmake.org/cmake/help/latest/manual/cmake-variables.7.html "cmake-variables(7)") |
*   [previous](https://cmake.org/cmake/help/latest/manual/cmake-server.7.html "cmake-server(7)") |

*   ![Image 2](https://cmake.org/cmake/help/latest/_static/cmake-logo-16.png)[CMake](https://cmake.org/)4.3.0-rc3 »
*   [Documentation](https://cmake.org/cmake/help/latest/index.html) » 
*   [cmake-toolchains(7)](https://cmake.org/cmake/help/latest/manual/cmake-toolchains.7.html)

 © Copyright 2000-2026 Kitware, Inc. and Contributors. Created using [Sphinx](https://www.sphinx-doc.org/) 8.2.3.
