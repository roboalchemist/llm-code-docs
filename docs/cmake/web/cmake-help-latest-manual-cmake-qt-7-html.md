# Source: https://cmake.org/cmake/help/latest/manual/cmake-qt.7.html

Title: cmake-qt(7) — CMake 4.3.0-rc3 Documentation

URL Source: https://cmake.org/cmake/help/latest/manual/cmake-qt.7.html

Markdown Content:
Contents

*   [cmake-qt(7)](https://cmake.org/cmake/help/latest/manual/cmake-qt.7.html#cmake-qt-7)

    *   [Introduction](https://cmake.org/cmake/help/latest/manual/cmake-qt.7.html#introduction)

    *   [Qt Build Tools](https://cmake.org/cmake/help/latest/manual/cmake-qt.7.html#qt-build-tools)

        *   [AUTOMOC](https://cmake.org/cmake/help/latest/manual/cmake-qt.7.html#automoc)

        *   [AUTOUIC](https://cmake.org/cmake/help/latest/manual/cmake-qt.7.html#autouic)

        *   [AUTORCC](https://cmake.org/cmake/help/latest/manual/cmake-qt.7.html#autorcc)

    *   [The `<ORIGIN>_autogen` target](https://cmake.org/cmake/help/latest/manual/cmake-qt.7.html#the-origin-autogen-target)

    *   [The `<ORIGIN>_autogen_timestamp_deps` target](https://cmake.org/cmake/help/latest/manual/cmake-qt.7.html#the-origin-autogen-timestamp-deps-target)

    *   [Visual Studio Generators](https://cmake.org/cmake/help/latest/manual/cmake-qt.7.html#visual-studio-generators)

    *   [qtmain.lib on Windows](https://cmake.org/cmake/help/latest/manual/cmake-qt.7.html#qtmain-lib-on-windows)

[Introduction](https://cmake.org/cmake/help/latest/manual/cmake-qt.7.html#id2)[¶](https://cmake.org/cmake/help/latest/manual/cmake-qt.7.html#introduction "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

CMake can find and use Qt 4, Qt 5 and Qt 6 libraries. The Qt 4 libraries are found by the [`FindQt4`](https://cmake.org/cmake/help/latest/module/FindQt4.html#module:FindQt4 "FindQt4") find-module shipped with CMake, whereas the Qt 5 and Qt 6 libraries are found using "Config-file Packages" shipped with Qt 5 and Qt 6. See [`cmake-packages(7)`](https://cmake.org/cmake/help/latest/manual/cmake-packages.7.html#manual:cmake-packages(7) "cmake-packages(7)") for more information about CMake packages, and see [the Qt cmake manual](https://doc.qt.io/qt-6/cmake-manual.html) for your Qt version.

Qt 4, Qt 5 and Qt 6 may be used together in the same [`CMake buildsystem`](https://cmake.org/cmake/help/latest/manual/cmake-buildsystem.7.html#manual:cmake-buildsystem(7) "cmake-buildsystem(7)"):

cmake_minimum_required(VERSION 3.16 FATAL_ERROR)

project(Qt4_5_6)

set(CMAKE_AUTOMOC ON)

find_package(Qt6 COMPONENTS Widgets DBus REQUIRED)
add_executable(publisher publisher.cpp)
target_link_libraries(publisher Qt6::Widgets Qt6::DBus)

find_package(Qt5 COMPONENTS Gui DBus REQUIRED)
add_executable(subscriber1 subscriber1.cpp)
target_link_libraries(subscriber1 Qt5::Gui Qt5::DBus)

find_package(Qt4 REQUIRED)
add_executable(subscriber2 subscriber2.cpp)
target_link_libraries(subscriber2 Qt4::QtGui Qt4::QtDBus)

A CMake target may not link to more than one Qt version. A diagnostic is issued if this is attempted or results from transitive target dependency evaluation.

[Qt Build Tools](https://cmake.org/cmake/help/latest/manual/cmake-qt.7.html#id3)[¶](https://cmake.org/cmake/help/latest/manual/cmake-qt.7.html#qt-build-tools "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Qt relies on some bundled tools for code generation, such as `moc` for meta-object code generation, `uic` for widget layout and population, and `rcc` for virtual file system content generation. These tools may be automatically invoked by [`cmake(1)`](https://cmake.org/cmake/help/latest/manual/cmake.1.html#manual:cmake(1) "cmake(1)") if the appropriate conditions are met. The automatic tool invocation may be used with Qt version 4 to 6.

### [AUTOMOC](https://cmake.org/cmake/help/latest/manual/cmake-qt.7.html#id4)[¶](https://cmake.org/cmake/help/latest/manual/cmake-qt.7.html#automoc "Link to this heading")

The [`AUTOMOC`](https://cmake.org/cmake/help/latest/prop_tgt/AUTOMOC.html#prop_tgt:AUTOMOC "AUTOMOC") target property controls whether [`cmake(1)`](https://cmake.org/cmake/help/latest/manual/cmake.1.html#manual:cmake(1) "cmake(1)") inspects the C++ files in the target to determine if they require `moc` to be run, and to create rules to execute `moc` at the appropriate time.

If a macro from [`AUTOMOC_MACRO_NAMES`](https://cmake.org/cmake/help/latest/prop_tgt/AUTOMOC_MACRO_NAMES.html#prop_tgt:AUTOMOC_MACRO_NAMES "AUTOMOC_MACRO_NAMES") is found in a header file, `moc` will be run on the file. The result will be put into a file named according to `moc_<basename>.cpp`. If the macro is found in a C++ implementation file, the moc output will be put into a file named according to `<basename>.moc`, following the Qt conventions. The `<basename>.moc` must be included by the user in the C++ implementation file with a preprocessor `#include`.

Included `moc_*.cpp` and `*.moc` files will be generated in the `<AUTOGEN_BUILD_DIR>/include` directory which is automatically added to the target's [`INCLUDE_DIRECTORIES`](https://cmake.org/cmake/help/latest/prop_tgt/INCLUDE_DIRECTORIES.html#prop_tgt:INCLUDE_DIRECTORIES "INCLUDE_DIRECTORIES").

*   This differs from CMake 3.7 and below; see their documentation for details.

*   For [`multi configuration generators`](https://cmake.org/cmake/help/latest/prop_gbl/GENERATOR_IS_MULTI_CONFIG.html#prop_gbl:GENERATOR_IS_MULTI_CONFIG "GENERATOR_IS_MULTI_CONFIG"), the include directory is `<AUTOGEN_BUILD_DIR>/include_<CONFIG>`.

*   See [`AUTOGEN_BUILD_DIR`](https://cmake.org/cmake/help/latest/prop_tgt/AUTOGEN_BUILD_DIR.html#prop_tgt:AUTOGEN_BUILD_DIR "AUTOGEN_BUILD_DIR").

Not included `moc_<basename>.cpp` files will be generated in custom folders to avoid name collisions and included in a separate file which is compiled into the target, named either `<AUTOGEN_BUILD_DIR>/mocs_compilation.cpp` or `<AUTOGEN_BUILD_DIR>/mocs_compilation_$<CONFIG>.cpp`.

*   See [`AUTOGEN_BUILD_DIR`](https://cmake.org/cmake/help/latest/prop_tgt/AUTOGEN_BUILD_DIR.html#prop_tgt:AUTOGEN_BUILD_DIR "AUTOGEN_BUILD_DIR").

The `moc` command line will consume the [`COMPILE_DEFINITIONS`](https://cmake.org/cmake/help/latest/prop_tgt/COMPILE_DEFINITIONS.html#prop_tgt:COMPILE_DEFINITIONS "COMPILE_DEFINITIONS") and [`INCLUDE_DIRECTORIES`](https://cmake.org/cmake/help/latest/prop_tgt/INCLUDE_DIRECTORIES.html#prop_tgt:INCLUDE_DIRECTORIES "INCLUDE_DIRECTORIES") target properties from the target it is being invoked for, and for the appropriate build configuration.

The [`AUTOMOC`](https://cmake.org/cmake/help/latest/prop_tgt/AUTOMOC.html#prop_tgt:AUTOMOC "AUTOMOC") target property may be pre-set for all following targets by setting the [`CMAKE_AUTOMOC`](https://cmake.org/cmake/help/latest/variable/CMAKE_AUTOMOC.html#variable:CMAKE_AUTOMOC "CMAKE_AUTOMOC") variable. The [`AUTOMOC_MOC_OPTIONS`](https://cmake.org/cmake/help/latest/prop_tgt/AUTOMOC_MOC_OPTIONS.html#prop_tgt:AUTOMOC_MOC_OPTIONS "AUTOMOC_MOC_OPTIONS") target property may be populated to set options to pass to `moc`. The [`CMAKE_AUTOMOC_MOC_OPTIONS`](https://cmake.org/cmake/help/latest/variable/CMAKE_AUTOMOC_MOC_OPTIONS.html#variable:CMAKE_AUTOMOC_MOC_OPTIONS "CMAKE_AUTOMOC_MOC_OPTIONS") variable may be populated to pre-set the options for all following targets.

Additional macro names to search for can be added to [`AUTOMOC_MACRO_NAMES`](https://cmake.org/cmake/help/latest/prop_tgt/AUTOMOC_MACRO_NAMES.html#prop_tgt:AUTOMOC_MACRO_NAMES "AUTOMOC_MACRO_NAMES").

Additional `moc` dependency file names can be extracted from source code by using [`AUTOMOC_DEPEND_FILTERS`](https://cmake.org/cmake/help/latest/prop_tgt/AUTOMOC_DEPEND_FILTERS.html#prop_tgt:AUTOMOC_DEPEND_FILTERS "AUTOMOC_DEPEND_FILTERS").

Source C++ files can be excluded from [`AUTOMOC`](https://cmake.org/cmake/help/latest/prop_tgt/AUTOMOC.html#prop_tgt:AUTOMOC "AUTOMOC") processing by enabling [`SKIP_AUTOMOC`](https://cmake.org/cmake/help/latest/prop_sf/SKIP_AUTOMOC.html#prop_sf:SKIP_AUTOMOC "SKIP_AUTOMOC") or the broader [`SKIP_AUTOGEN`](https://cmake.org/cmake/help/latest/prop_sf/SKIP_AUTOGEN.html#prop_sf:SKIP_AUTOGEN "SKIP_AUTOGEN").

### [AUTOUIC](https://cmake.org/cmake/help/latest/manual/cmake-qt.7.html#id5)[¶](https://cmake.org/cmake/help/latest/manual/cmake-qt.7.html#autouic "Link to this heading")

The [`AUTOUIC`](https://cmake.org/cmake/help/latest/prop_tgt/AUTOUIC.html#prop_tgt:AUTOUIC "AUTOUIC") target property controls whether [`cmake(1)`](https://cmake.org/cmake/help/latest/manual/cmake.1.html#manual:cmake(1) "cmake(1)") inspects the C++ files in the target to determine if they require `uic` to be run, and to create rules to execute `uic` at the appropriate time.

If a preprocessor `#include` directive is found which matches `<path>ui_<basename>.h`, and a `<basename>.ui` file exists, then `uic` will be executed to generate the appropriate file. The `<basename>.ui` file is searched for in the following places

1.   `<source_dir>/<basename>.ui`

2.   `<source_dir>/<path><basename>.ui`

3.   `<AUTOUIC_SEARCH_PATHS>/<basename>.ui`

4.   `<AUTOUIC_SEARCH_PATHS>/<path><basename>.ui`

where `<source_dir>` is the directory of the C++ file and [`AUTOUIC_SEARCH_PATHS`](https://cmake.org/cmake/help/latest/prop_tgt/AUTOUIC_SEARCH_PATHS.html#prop_tgt:AUTOUIC_SEARCH_PATHS "AUTOUIC_SEARCH_PATHS") is a list of additional search paths.

The generated generated `ui_*.h` files are placed in the `<AUTOGEN_BUILD_DIR>/include` directory which is automatically added to the target's [`INCLUDE_DIRECTORIES`](https://cmake.org/cmake/help/latest/prop_tgt/INCLUDE_DIRECTORIES.html#prop_tgt:INCLUDE_DIRECTORIES "INCLUDE_DIRECTORIES").

*   This differs from CMake 3.7 and below; see their documentation for details.

*   For [`multi configuration generators`](https://cmake.org/cmake/help/latest/prop_gbl/GENERATOR_IS_MULTI_CONFIG.html#prop_gbl:GENERATOR_IS_MULTI_CONFIG "GENERATOR_IS_MULTI_CONFIG"), the include directory is `<AUTOGEN_BUILD_DIR>/include_<CONFIG>`.

*   See [`AUTOGEN_BUILD_DIR`](https://cmake.org/cmake/help/latest/prop_tgt/AUTOGEN_BUILD_DIR.html#prop_tgt:AUTOGEN_BUILD_DIR "AUTOGEN_BUILD_DIR").

The [`AUTOUIC`](https://cmake.org/cmake/help/latest/prop_tgt/AUTOUIC.html#prop_tgt:AUTOUIC "AUTOUIC") target property may be pre-set for all following targets by setting the [`CMAKE_AUTOUIC`](https://cmake.org/cmake/help/latest/variable/CMAKE_AUTOUIC.html#variable:CMAKE_AUTOUIC "CMAKE_AUTOUIC") variable. The [`AUTOUIC_OPTIONS`](https://cmake.org/cmake/help/latest/prop_tgt/AUTOUIC_OPTIONS.html#prop_tgt:AUTOUIC_OPTIONS "AUTOUIC_OPTIONS") target property may be populated to set options to pass to `uic`. The [`CMAKE_AUTOUIC_OPTIONS`](https://cmake.org/cmake/help/latest/variable/CMAKE_AUTOUIC_OPTIONS.html#variable:CMAKE_AUTOUIC_OPTIONS "CMAKE_AUTOUIC_OPTIONS") variable may be populated to pre-set the options for all following targets. The [`AUTOUIC_OPTIONS`](https://cmake.org/cmake/help/latest/prop_sf/AUTOUIC_OPTIONS.html#prop_sf:AUTOUIC_OPTIONS "AUTOUIC_OPTIONS") source file property may be set on the `<basename>.ui` file to set particular options for the file. This overrides options from the [`AUTOUIC_OPTIONS`](https://cmake.org/cmake/help/latest/prop_tgt/AUTOUIC_OPTIONS.html#prop_tgt:AUTOUIC_OPTIONS "AUTOUIC_OPTIONS") target property.

A target may populate the [`INTERFACE_AUTOUIC_OPTIONS`](https://cmake.org/cmake/help/latest/prop_tgt/INTERFACE_AUTOUIC_OPTIONS.html#prop_tgt:INTERFACE_AUTOUIC_OPTIONS "INTERFACE_AUTOUIC_OPTIONS") target property with options that should be used when invoking `uic`. This must be consistent with the [`AUTOUIC_OPTIONS`](https://cmake.org/cmake/help/latest/prop_tgt/AUTOUIC_OPTIONS.html#prop_tgt:AUTOUIC_OPTIONS "AUTOUIC_OPTIONS") target property content of the depender target. The [`CMAKE_DEBUG_TARGET_PROPERTIES`](https://cmake.org/cmake/help/latest/variable/CMAKE_DEBUG_TARGET_PROPERTIES.html#variable:CMAKE_DEBUG_TARGET_PROPERTIES "CMAKE_DEBUG_TARGET_PROPERTIES") variable may be used to track the origin target of such [`INTERFACE_AUTOUIC_OPTIONS`](https://cmake.org/cmake/help/latest/prop_tgt/INTERFACE_AUTOUIC_OPTIONS.html#prop_tgt:INTERFACE_AUTOUIC_OPTIONS "INTERFACE_AUTOUIC_OPTIONS"). This means that a library which provides an alternative translation system for Qt may specify options which should be used when running `uic`:

add_library(KI18n klocalizedstring.cpp)
target_link_libraries(KI18n Qt6::Core)

# KI18n uses the tr2i18n() function instead of tr(). That function is
# declared in the klocalizedstring.h header.
set(autouic_options
 -tr tr2i18n
 -include klocalizedstring.h
)

set_property(TARGET KI18n APPEND PROPERTY
 INTERFACE_AUTOUIC_OPTIONS ${autouic_options}
)

A consuming project linking to the target exported from upstream automatically uses appropriate options when `uic` is run by [`AUTOUIC`](https://cmake.org/cmake/help/latest/prop_tgt/AUTOUIC.html#prop_tgt:AUTOUIC "AUTOUIC"), as a result of linking with the [`IMPORTED`](https://cmake.org/cmake/help/latest/prop_tgt/IMPORTED.html#prop_tgt:IMPORTED "IMPORTED") target:

set(CMAKE_AUTOUIC ON)
# Uses a libwidget.ui file:
add_library(LibWidget libwidget.cpp)
target_link_libraries(LibWidget
 KF5::KI18n
 Qt5::Widgets
)

Source files can be excluded from [`AUTOUIC`](https://cmake.org/cmake/help/latest/prop_tgt/AUTOUIC.html#prop_tgt:AUTOUIC "AUTOUIC") processing by enabling [`SKIP_AUTOUIC`](https://cmake.org/cmake/help/latest/prop_sf/SKIP_AUTOUIC.html#prop_sf:SKIP_AUTOUIC "SKIP_AUTOUIC") or the broader [`SKIP_AUTOGEN`](https://cmake.org/cmake/help/latest/prop_sf/SKIP_AUTOGEN.html#prop_sf:SKIP_AUTOGEN "SKIP_AUTOGEN").

### [AUTORCC](https://cmake.org/cmake/help/latest/manual/cmake-qt.7.html#id6)[¶](https://cmake.org/cmake/help/latest/manual/cmake-qt.7.html#autorcc "Link to this heading")

The [`AUTORCC`](https://cmake.org/cmake/help/latest/prop_tgt/AUTORCC.html#prop_tgt:AUTORCC "AUTORCC") target property controls whether [`cmake(1)`](https://cmake.org/cmake/help/latest/manual/cmake.1.html#manual:cmake(1) "cmake(1)") creates rules to execute `rcc` at the appropriate time on source files which have the suffix `.qrc`.

add_executable(myexe main.cpp resource_file.qrc)

The [`AUTORCC`](https://cmake.org/cmake/help/latest/prop_tgt/AUTORCC.html#prop_tgt:AUTORCC "AUTORCC") target property may be pre-set for all following targets by setting the [`CMAKE_AUTORCC`](https://cmake.org/cmake/help/latest/variable/CMAKE_AUTORCC.html#variable:CMAKE_AUTORCC "CMAKE_AUTORCC") variable. The [`AUTORCC_OPTIONS`](https://cmake.org/cmake/help/latest/prop_tgt/AUTORCC_OPTIONS.html#prop_tgt:AUTORCC_OPTIONS "AUTORCC_OPTIONS") target property may be populated to set options to pass to `rcc`. The [`CMAKE_AUTORCC_OPTIONS`](https://cmake.org/cmake/help/latest/variable/CMAKE_AUTORCC_OPTIONS.html#variable:CMAKE_AUTORCC_OPTIONS "CMAKE_AUTORCC_OPTIONS") variable may be populated to pre-set the options for all following targets. The [`AUTORCC_OPTIONS`](https://cmake.org/cmake/help/latest/prop_sf/AUTORCC_OPTIONS.html#prop_sf:AUTORCC_OPTIONS "AUTORCC_OPTIONS") source file property may be set on the `<name>.qrc` file to set particular options for the file. This overrides options from the [`AUTORCC_OPTIONS`](https://cmake.org/cmake/help/latest/prop_tgt/AUTORCC_OPTIONS.html#prop_tgt:AUTORCC_OPTIONS "AUTORCC_OPTIONS") target property.

Source files can be excluded from [`AUTORCC`](https://cmake.org/cmake/help/latest/prop_tgt/AUTORCC.html#prop_tgt:AUTORCC "AUTORCC") processing by enabling [`SKIP_AUTORCC`](https://cmake.org/cmake/help/latest/prop_sf/SKIP_AUTORCC.html#prop_sf:SKIP_AUTORCC "SKIP_AUTORCC") or the broader [`SKIP_AUTOGEN`](https://cmake.org/cmake/help/latest/prop_sf/SKIP_AUTOGEN.html#prop_sf:SKIP_AUTOGEN "SKIP_AUTOGEN").

[The `<ORIGIN>_autogen` target](https://cmake.org/cmake/help/latest/manual/cmake-qt.7.html#id7)[¶](https://cmake.org/cmake/help/latest/manual/cmake-qt.7.html#the-origin-autogen-target "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The `moc` and `uic` tools are executed as part of a synthesized `<ORIGIN>_autogen`[`custom target`](https://cmake.org/cmake/help/latest/command/add_custom_target.html#command:add_custom_target "add_custom_target") generated by CMake. By default, that `<ORIGIN>_autogen` target inherits the dependencies of the `<ORIGIN>` target (see [`AUTOGEN_ORIGIN_DEPENDS`](https://cmake.org/cmake/help/latest/prop_tgt/AUTOGEN_ORIGIN_DEPENDS.html#prop_tgt:AUTOGEN_ORIGIN_DEPENDS "AUTOGEN_ORIGIN_DEPENDS")). Target dependencies may be added to the `<ORIGIN>_autogen` target by adding them to the [`AUTOGEN_TARGET_DEPENDS`](https://cmake.org/cmake/help/latest/prop_tgt/AUTOGEN_TARGET_DEPENDS.html#prop_tgt:AUTOGEN_TARGET_DEPENDS "AUTOGEN_TARGET_DEPENDS") target property.

[The `<ORIGIN>_autogen_timestamp_deps` target](https://cmake.org/cmake/help/latest/manual/cmake-qt.7.html#id8)[¶](https://cmake.org/cmake/help/latest/manual/cmake-qt.7.html#the-origin-autogen-timestamp-deps-target "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

If Qt 5.15 or later is used and the generator is either [`Ninja`](https://cmake.org/cmake/help/latest/generator/Ninja.html#generator:Ninja "Ninja") or [Makefile Generators](https://cmake.org/cmake/help/latest/manual/cmake-generators.7.html#makefile-generators), the `<ORIGIN>_autogen_timestamp_deps` target is also created in addition to the [<ORIGIN>_autogen](https://cmake.org/cmake/help/latest/manual/cmake-qt.7.html#origin-autogen) target. This target does not have any sources or commands to execute, but it has dependencies that were previously inherited by the pre-Qt 5.15 [<ORIGIN>_autogen](https://cmake.org/cmake/help/latest/manual/cmake-qt.7.html#origin-autogen) target. These dependencies will serve as a list of order-only dependencies for the custom command, without forcing the custom command to re-execute.

[Visual Studio Generators](https://cmake.org/cmake/help/latest/manual/cmake-qt.7.html#id9)[¶](https://cmake.org/cmake/help/latest/manual/cmake-qt.7.html#visual-studio-generators "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

When using the [Visual Studio Generators](https://cmake.org/cmake/help/latest/manual/cmake-generators.7.html#visual-studio-generators), CMake generates a `PRE_BUILD`[`custom command`](https://cmake.org/cmake/help/latest/command/add_custom_command.html#command:add_custom_command "add_custom_command") instead of the [<ORIGIN>_autogen](https://cmake.org/cmake/help/latest/manual/cmake-qt.7.html#origin-autogen)[`custom target`](https://cmake.org/cmake/help/latest/command/add_custom_target.html#command:add_custom_target "add_custom_target") (for [`AUTOMOC`](https://cmake.org/cmake/help/latest/prop_tgt/AUTOMOC.html#prop_tgt:AUTOMOC "AUTOMOC") and [`AUTOUIC`](https://cmake.org/cmake/help/latest/prop_tgt/AUTOUIC.html#prop_tgt:AUTOUIC "AUTOUIC")). This isn't always possible though and an [<ORIGIN>_autogen](https://cmake.org/cmake/help/latest/manual/cmake-qt.7.html#origin-autogen)[`custom target`](https://cmake.org/cmake/help/latest/command/add_custom_target.html#command:add_custom_target "add_custom_target") is used, when either

*   the `<ORIGIN>` target depends on [`GENERATED`](https://cmake.org/cmake/help/latest/prop_sf/GENERATED.html#prop_sf:GENERATED "GENERATED") files which aren't excluded from [`AUTOMOC`](https://cmake.org/cmake/help/latest/prop_tgt/AUTOMOC.html#prop_tgt:AUTOMOC "AUTOMOC") and [`AUTOUIC`](https://cmake.org/cmake/help/latest/prop_tgt/AUTOUIC.html#prop_tgt:AUTOUIC "AUTOUIC") by [`SKIP_AUTOMOC`](https://cmake.org/cmake/help/latest/prop_sf/SKIP_AUTOMOC.html#prop_sf:SKIP_AUTOMOC "SKIP_AUTOMOC"), [`SKIP_AUTOUIC`](https://cmake.org/cmake/help/latest/prop_sf/SKIP_AUTOUIC.html#prop_sf:SKIP_AUTOUIC "SKIP_AUTOUIC"), [`SKIP_AUTOGEN`](https://cmake.org/cmake/help/latest/prop_sf/SKIP_AUTOGEN.html#prop_sf:SKIP_AUTOGEN "SKIP_AUTOGEN") or [`CMP0071`](https://cmake.org/cmake/help/latest/policy/CMP0071.html#policy:CMP0071 "CMP0071")

*   [`AUTOGEN_TARGET_DEPENDS`](https://cmake.org/cmake/help/latest/prop_tgt/AUTOGEN_TARGET_DEPENDS.html#prop_tgt:AUTOGEN_TARGET_DEPENDS "AUTOGEN_TARGET_DEPENDS") lists a source file

*   [`CMAKE_GLOBAL_AUTOGEN_TARGET`](https://cmake.org/cmake/help/latest/variable/CMAKE_GLOBAL_AUTOGEN_TARGET.html#variable:CMAKE_GLOBAL_AUTOGEN_TARGET "CMAKE_GLOBAL_AUTOGEN_TARGET") is enabled

[qtmain.lib on Windows](https://cmake.org/cmake/help/latest/manual/cmake-qt.7.html#id10)[¶](https://cmake.org/cmake/help/latest/manual/cmake-qt.7.html#qtmain-lib-on-windows "Link to this heading")
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The Qt 4 and 5 [`IMPORTED`](https://cmake.org/cmake/help/latest/prop_tgt/IMPORTED.html#prop_tgt:IMPORTED "IMPORTED") targets for the QtGui libraries specify that the qtmain.lib static library shipped with Qt will be linked by all dependent executables which have the [`WIN32_EXECUTABLE`](https://cmake.org/cmake/help/latest/prop_tgt/WIN32_EXECUTABLE.html#prop_tgt:WIN32_EXECUTABLE "WIN32_EXECUTABLE") enabled.

To disable this behavior, enable the `Qt5_NO_LINK_QTMAIN` target property for Qt 5 based targets or `QT4_NO_LINK_QTMAIN` target property for Qt 4 based targets.

add_executable(myexe WIN32 main.cpp)
target_link_libraries(myexe Qt4::QtGui)

add_executable(myexe_no_qtmain WIN32 main_no_qtmain.cpp)
set_property(TARGET main_no_qtmain PROPERTY QT4_NO_LINK_QTMAIN ON)
target_link_libraries(main_no_qtmain Qt4::QtGui)
