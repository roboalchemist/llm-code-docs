# Source: https://cmake.org/cmake/help/latest/manual/cmake-gui.1.html

Title: cmake-gui(1) — CMake 4.3.0-rc3 Documentation

URL Source: https://cmake.org/cmake/help/latest/manual/cmake-gui.1.html

Markdown Content:
Synopsis[¶](https://cmake.org/cmake/help/latest/manual/cmake-gui.1.html#synopsis "Link to this heading")
--------------------------------------------------------------------------------------------------------

cmake-gui [<options>]
cmake-gui [<options>] -B <path-to-build> [-S <path-to-source>]
cmake-gui [<options>] <path-to-source | path-to-existing-build>
cmake-gui [<options>] --browse-manual [<filename>]

Description[¶](https://cmake.org/cmake/help/latest/manual/cmake-gui.1.html#description "Link to this heading")
--------------------------------------------------------------------------------------------------------------

The **cmake-gui** executable is the CMake GUI. Project configuration settings may be specified interactively. Brief instructions are provided at the bottom of the window when the program is running.

CMake is a cross-platform build system generator. Projects specify their build process with platform-independent CMake listfiles included in each directory of a source tree with the name `CMakeLists.txt`. Users build a project by using CMake to generate a build system for a native tool on their platform.

Options[¶](https://cmake.org/cmake/help/latest/manual/cmake-gui.1.html#options "Link to this heading")
------------------------------------------------------------------------------------------------------

-S<path-to-source>[¶](https://cmake.org/cmake/help/latest/manual/cmake-gui.1.html#cmdoption-cmake-gui-S "Link to this definition")
Path to root directory of the CMake project to build.

-B<path-to-build>[¶](https://cmake.org/cmake/help/latest/manual/cmake-gui.1.html#cmdoption-cmake-gui-B "Link to this definition")
Path to directory which CMake will use as the root of build directory.

If the directory doesn't already exist CMake will make it.

--preset=<preset-name>[¶](https://cmake.org/cmake/help/latest/manual/cmake-gui.1.html#cmdoption-cmake-gui-preset "Link to this definition")
Name of the preset to use from the project's [`presets`](https://cmake.org/cmake/help/latest/manual/cmake-presets.7.html#manual:cmake-presets(7) "cmake-presets(7)") files, if it has them.

--browse-manual[<filename>][¶](https://cmake.org/cmake/help/latest/manual/cmake-gui.1.html#cmdoption-cmake-gui-browse-manual "Link to this definition")
Open the CMake reference manual in a browser and immediately exit. If `<filename>` is specified, open that file within the reference manual instead of `index.html`.

-version[=json-v1][<file>],--version[=json-v1][<file>],/V[=json-v1][<file>],/version[=json-v1][<file>][¶](https://cmake.org/cmake/help/latest/manual/cmake-gui.1.html#cmdoption-cmake-gui-version "Link to this definition")
Show program name/version banner and exit. If `json-v1` is specified, print extended version information in JSON format. The JSON output contains the versions for the CMake and its dependencies. The output is printed to a named `<file>` if given.

The JSON output format is described in machine-readable form by [`this JSON schema`](https://cmake.org/cmake/help/latest/_downloads/8841c8b524587a9aee211c0ac198f604/version-schema.json).

-h,-H,--help,-help,-usage,/?[¶](https://cmake.org/cmake/help/latest/manual/cmake-gui.1.html#cmdoption-cmake-gui-h "Link to this definition")
Print usage information and exit.

Usage describes the basic command line interface and its options.

--help<keyword>[<file>][¶](https://cmake.org/cmake/help/latest/manual/cmake-gui.1.html#cmdoption-cmake-gui-1 "Link to this definition")
Print help for one CMake keyword.

`<keyword>` can be a property, variable, command, policy, generator or module.

The relevant manual entry for `<keyword>` is printed in a human-readable text format. The output is printed to a named `<file>` if given.

Changed in version 3.28: Prior to CMake 3.28, this option supported command names only.

--help-full[<file>][¶](https://cmake.org/cmake/help/latest/manual/cmake-gui.1.html#cmdoption-cmake-gui-help-full "Link to this definition")
Print all help manuals and exit.

All manuals are printed in a human-readable text format. The output is printed to a named `<file>` if given.

--help-manual<man>[<file>][¶](https://cmake.org/cmake/help/latest/manual/cmake-gui.1.html#cmdoption-cmake-gui-help-manual "Link to this definition")
Print one help manual and exit.

The specified manual is printed in a human-readable text format. The output is printed to a named `<file>` if given.

--help-manual-list[<file>][¶](https://cmake.org/cmake/help/latest/manual/cmake-gui.1.html#cmdoption-cmake-gui-help-manual-list "Link to this definition")
List help manuals available and exit.

The list contains all manuals for which help may be obtained by using the `--help-manual` option followed by a manual name. The output is printed to a named `<file>` if given.

--help-command<cmd>[<file>][¶](https://cmake.org/cmake/help/latest/manual/cmake-gui.1.html#cmdoption-cmake-gui-help-command "Link to this definition")
Print help for one command and exit.

The [`cmake-commands(7)`](https://cmake.org/cmake/help/latest/manual/cmake-commands.7.html#manual:cmake-commands(7) "cmake-commands(7)") manual entry for `<cmd>` is printed in a human-readable text format. The output is printed to a named `<file>` if given.

--help-command-list[<file>][¶](https://cmake.org/cmake/help/latest/manual/cmake-gui.1.html#cmdoption-cmake-gui-help-command-list "Link to this definition")
List commands with help available and exit.

The list contains all commands for which help may be obtained by using the `--help-command` option followed by a command name. The output is printed to a named `<file>` if given.

--help-commands[<file>][¶](https://cmake.org/cmake/help/latest/manual/cmake-gui.1.html#cmdoption-cmake-gui-help-commands "Link to this definition")
Print cmake-commands manual and exit.

The [`cmake-commands(7)`](https://cmake.org/cmake/help/latest/manual/cmake-commands.7.html#manual:cmake-commands(7) "cmake-commands(7)") manual is printed in a human-readable text format. The output is printed to a named `<file>` if given.

--help-module<mod>[<file>][¶](https://cmake.org/cmake/help/latest/manual/cmake-gui.1.html#cmdoption-cmake-gui-help-module "Link to this definition")
Print help for one module and exit.

The [`cmake-modules(7)`](https://cmake.org/cmake/help/latest/manual/cmake-modules.7.html#manual:cmake-modules(7) "cmake-modules(7)") manual entry for `<mod>` is printed in a human-readable text format. The output is printed to a named `<file>` if given.

--help-module-list[<file>][¶](https://cmake.org/cmake/help/latest/manual/cmake-gui.1.html#cmdoption-cmake-gui-help-module-list "Link to this definition")
List modules with help available and exit.

The list contains all modules for which help may be obtained by using the `--help-module` option followed by a module name. The output is printed to a named `<file>` if given.

--help-modules[<file>][¶](https://cmake.org/cmake/help/latest/manual/cmake-gui.1.html#cmdoption-cmake-gui-help-modules "Link to this definition")
Print cmake-modules manual and exit.

The [`cmake-modules(7)`](https://cmake.org/cmake/help/latest/manual/cmake-modules.7.html#manual:cmake-modules(7) "cmake-modules(7)") manual is printed in a human-readable text format. The output is printed to a named `<file>` if given.

--help-policy<cmp>[<file>][¶](https://cmake.org/cmake/help/latest/manual/cmake-gui.1.html#cmdoption-cmake-gui-help-policy "Link to this definition")
Print help for one policy and exit.

The [`cmake-policies(7)`](https://cmake.org/cmake/help/latest/manual/cmake-policies.7.html#manual:cmake-policies(7) "cmake-policies(7)") manual entry for `<cmp>` is printed in a human-readable text format. The output is printed to a named `<file>` if given.

--help-policy-list[<file>][¶](https://cmake.org/cmake/help/latest/manual/cmake-gui.1.html#cmdoption-cmake-gui-help-policy-list "Link to this definition")
List policies with help available and exit.

The list contains all policies for which help may be obtained by using the `--help-policy` option followed by a policy name. The output is printed to a named `<file>` if given.

--help-policies[<file>][¶](https://cmake.org/cmake/help/latest/manual/cmake-gui.1.html#cmdoption-cmake-gui-help-policies "Link to this definition")
Print cmake-policies manual and exit.

The [`cmake-policies(7)`](https://cmake.org/cmake/help/latest/manual/cmake-policies.7.html#manual:cmake-policies(7) "cmake-policies(7)") manual is printed in a human-readable text format. The output is printed to a named `<file>` if given.

--help-property<prop>[<file>][¶](https://cmake.org/cmake/help/latest/manual/cmake-gui.1.html#cmdoption-cmake-gui-help-property "Link to this definition")
Print help for one property and exit.

The [`cmake-properties(7)`](https://cmake.org/cmake/help/latest/manual/cmake-properties.7.html#manual:cmake-properties(7) "cmake-properties(7)") manual entries for `<prop>` are printed in a human-readable text format. The output is printed to a named `<file>` if given.

--help-property-list[<file>][¶](https://cmake.org/cmake/help/latest/manual/cmake-gui.1.html#cmdoption-cmake-gui-help-property-list "Link to this definition")
List properties with help available and exit.

The list contains all properties for which help may be obtained by using the `--help-property` option followed by a property name. The output is printed to a named `<file>` if given.

--help-properties[<file>][¶](https://cmake.org/cmake/help/latest/manual/cmake-gui.1.html#cmdoption-cmake-gui-help-properties "Link to this definition")
Print cmake-properties manual and exit.

The [`cmake-properties(7)`](https://cmake.org/cmake/help/latest/manual/cmake-properties.7.html#manual:cmake-properties(7) "cmake-properties(7)") manual is printed in a human-readable text format. The output is printed to a named `<file>` if given.

--help-variable<var>[<file>][¶](https://cmake.org/cmake/help/latest/manual/cmake-gui.1.html#cmdoption-cmake-gui-help-variable "Link to this definition")
Print help for one variable and exit.

The [`cmake-variables(7)`](https://cmake.org/cmake/help/latest/manual/cmake-variables.7.html#manual:cmake-variables(7) "cmake-variables(7)") manual entry for `<var>` is printed in a human-readable text format. The output is printed to a named `<file>` if given.

--help-variable-list[<file>][¶](https://cmake.org/cmake/help/latest/manual/cmake-gui.1.html#cmdoption-cmake-gui-help-variable-list "Link to this definition")
List variables with help available and exit.

The list contains all variables for which help may be obtained by using the `--help-variable` option followed by a variable name. The output is printed to a named `<file>` if given.

--help-variables[<file>][¶](https://cmake.org/cmake/help/latest/manual/cmake-gui.1.html#cmdoption-cmake-gui-help-variables "Link to this definition")
Print cmake-variables manual and exit.

The [`cmake-variables(7)`](https://cmake.org/cmake/help/latest/manual/cmake-variables.7.html#manual:cmake-variables(7) "cmake-variables(7)") manual is printed in a human-readable text format. The output is printed to a named `<file>` if given.

See Also[¶](https://cmake.org/cmake/help/latest/manual/cmake-gui.1.html#see-also "Link to this heading")
--------------------------------------------------------------------------------------------------------

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
