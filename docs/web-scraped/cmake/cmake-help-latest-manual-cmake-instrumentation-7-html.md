# Source: https://cmake.org/cmake/help/latest/manual/cmake-instrumentation.7.html

Title: cmake-instrumentation(7) — CMake 4.3.0-rc3 Documentation

URL Source: https://cmake.org/cmake/help/latest/manual/cmake-instrumentation.7.html

Markdown Content:
Added in version 4.3.

Contents

*   [cmake-instrumentation(7)](https://cmake.org/cmake/help/latest/manual/cmake-instrumentation.7.html#cmake-instrumentation-7)

    *   [Introduction](https://cmake.org/cmake/help/latest/manual/cmake-instrumentation.7.html#introduction)

        *   [Data Collection](https://cmake.org/cmake/help/latest/manual/cmake-instrumentation.7.html#data-collection)

        *   [Indexing](https://cmake.org/cmake/help/latest/manual/cmake-instrumentation.7.html#indexing)

        *   [Callbacks](https://cmake.org/cmake/help/latest/manual/cmake-instrumentation.7.html#callbacks)

    *   [Enabling Instrumentation](https://cmake.org/cmake/help/latest/manual/cmake-instrumentation.7.html#enabling-instrumentation)

        *   [Enabling Instrumentation at the Project-Level](https://cmake.org/cmake/help/latest/manual/cmake-instrumentation.7.html#enabling-instrumentation-at-the-project-level)

        *   [Enabling Instrumentation at the User-Level](https://cmake.org/cmake/help/latest/manual/cmake-instrumentation.7.html#enabling-instrumentation-at-the-user-level)

        *   [Enabling Instrumentation for CDash Submissions](https://cmake.org/cmake/help/latest/manual/cmake-instrumentation.7.html#enabling-instrumentation-for-cdash-submissions)

    *   [API v1](https://cmake.org/cmake/help/latest/manual/cmake-instrumentation.7.html#api-v1)

        *   [v1 Query Files](https://cmake.org/cmake/help/latest/manual/cmake-instrumentation.7.html#v1-query-files)

    *   [Data v1](https://cmake.org/cmake/help/latest/manual/cmake-instrumentation.7.html#data-v1)

        *   [v1 Snippet File](https://cmake.org/cmake/help/latest/manual/cmake-instrumentation.7.html#v1-snippet-file)

        *   [v1 Index File](https://cmake.org/cmake/help/latest/manual/cmake-instrumentation.7.html#v1-index-file)

        *   [v1 CMake Content File](https://cmake.org/cmake/help/latest/manual/cmake-instrumentation.7.html#v1-cmake-content-file)

        *   [Google Trace File](https://cmake.org/cmake/help/latest/manual/cmake-instrumentation.7.html#google-trace-file)

[Introduction](https://cmake.org/cmake/help/latest/manual/cmake-instrumentation.7.html#id2)[¶](https://cmake.org/cmake/help/latest/manual/cmake-instrumentation.7.html#introduction "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The CMake Instrumentation API allows for the collection of timing data, target information and system diagnostic information during the configure, generate, build, test and install steps for a CMake project.

This feature is only available for projects using the [Makefile Generators](https://cmake.org/cmake/help/latest/manual/cmake-generators.7.html#makefile-generators), [Ninja Generators](https://cmake.org/cmake/help/latest/manual/cmake-generators.7.html#ninja-generators) or [`FASTBuild`](https://cmake.org/cmake/help/latest/generator/FASTBuild.html#generator:FASTBuild "FASTBuild").

All interactions with the CMake instrumentation API must specify both an API version and a Data version. At this time, there is only one version for each of these: the [API v1](https://cmake.org/cmake/help/latest/manual/cmake-instrumentation.7.html#api-v1) and [Data v1](https://cmake.org/cmake/help/latest/manual/cmake-instrumentation.7.html#data-v1).

### [Data Collection](https://cmake.org/cmake/help/latest/manual/cmake-instrumentation.7.html#id3)[¶](https://cmake.org/cmake/help/latest/manual/cmake-instrumentation.7.html#data-collection "Link to this heading")

Whenever a command is executed with instrumentation enabled, a [v1 Snippet File](https://cmake.org/cmake/help/latest/manual/cmake-instrumentation.7.html#v1-snippet-file) is created in the project build tree with data specific to that command. These files remain until after [Indexing](https://cmake.org/cmake/help/latest/manual/cmake-instrumentation.7.html#indexing) occurs.

CMake sets the [`RULE_LAUNCH_COMPILE`](https://cmake.org/cmake/help/latest/prop_gbl/RULE_LAUNCH_COMPILE.html#prop_gbl:RULE_LAUNCH_COMPILE "RULE_LAUNCH_COMPILE"), [`RULE_LAUNCH_LINK`](https://cmake.org/cmake/help/latest/prop_gbl/RULE_LAUNCH_LINK.html#prop_gbl:RULE_LAUNCH_LINK "RULE_LAUNCH_LINK") and [`RULE_LAUNCH_CUSTOM`](https://cmake.org/cmake/help/latest/prop_gbl/RULE_LAUNCH_CUSTOM.html#prop_gbl:RULE_LAUNCH_CUSTOM "RULE_LAUNCH_CUSTOM") global properties to wrap each compile, link and custom command invocation in a launcher that performs instrumentation and writes out a [v1 Snippet File](https://cmake.org/cmake/help/latest/manual/cmake-instrumentation.7.html#v1-snippet-file). If the project has been configured with [`CTestUseLaunchers`](https://cmake.org/cmake/help/latest/module/CTestUseLaunchers.html#module:CTestUseLaunchers "CTestUseLaunchers"), the launcher will collect instrumentation data in addition to performing the communication typically handled by that module.

### [Indexing](https://cmake.org/cmake/help/latest/manual/cmake-instrumentation.7.html#id4)[¶](https://cmake.org/cmake/help/latest/manual/cmake-instrumentation.7.html#indexing "Link to this heading")

Indexing is the process of collating generated instrumentation data. Indexing occurs at specific intervals called hooks, such as after every build. These hooks are configured as part of the [v1 Query Files](https://cmake.org/cmake/help/latest/manual/cmake-instrumentation.7.html#v1-query-files). Whenever a hook is triggered, an index file is generated containing a list of snippet files newer than the previous indexing.

Indexing and can also be performed by manually invoking [`ctest --collect-instrumentation`](https://cmake.org/cmake/help/latest/manual/ctest.1.html#cmdoption-ctest-collect-instrumentation).

### [Callbacks](https://cmake.org/cmake/help/latest/manual/cmake-instrumentation.7.html#id5)[¶](https://cmake.org/cmake/help/latest/manual/cmake-instrumentation.7.html#callbacks "Link to this heading")

As part of the [v1 Query Files](https://cmake.org/cmake/help/latest/manual/cmake-instrumentation.7.html#v1-query-files), users can provide a list of callbacks intended to handle data collected by this feature.

Whenever [Indexing](https://cmake.org/cmake/help/latest/manual/cmake-instrumentation.7.html#indexing) occurs, each provided callback is executed, passing the path to the generated index file as an argument.

These callbacks, defined either at the user-level or project-level should read the instrumentation data and perform any desired handling of it. The index file and its listed snippets are automatically deleted by CMake once all callbacks have completed. Note that a callback should never move or delete these data files manually as they may be needed by other callbacks.

[Enabling Instrumentation](https://cmake.org/cmake/help/latest/manual/cmake-instrumentation.7.html#id6)[¶](https://cmake.org/cmake/help/latest/manual/cmake-instrumentation.7.html#enabling-instrumentation "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Instrumentation can be enabled either for an individual CMake project, or for all CMake projects configured and built by a user. For both cases, see the [v1 Query Files](https://cmake.org/cmake/help/latest/manual/cmake-instrumentation.7.html#v1-query-files) for details on configuring this feature.

### [Enabling Instrumentation at the Project-Level](https://cmake.org/cmake/help/latest/manual/cmake-instrumentation.7.html#id7)[¶](https://cmake.org/cmake/help/latest/manual/cmake-instrumentation.7.html#enabling-instrumentation-at-the-project-level "Link to this heading")

Project code can contain instrumentation queries with the [`cmake_instrumentation()`](https://cmake.org/cmake/help/latest/command/cmake_instrumentation.html#command:cmake_instrumentation "cmake_instrumentation") command.

In addition, query files can be placed manually under `<build>/.cmake/instrumentation/<version>/query/` at the top of a build tree. This version of CMake supports only one version schema, [API v1](https://cmake.org/cmake/help/latest/manual/cmake-instrumentation.7.html#api-v1).

### [Enabling Instrumentation at the User-Level](https://cmake.org/cmake/help/latest/manual/cmake-instrumentation.7.html#id8)[¶](https://cmake.org/cmake/help/latest/manual/cmake-instrumentation.7.html#enabling-instrumentation-at-the-user-level "Link to this heading")

Instrumentation can be configured at the user-level by placing query files in the [`CMAKE_CONFIG_DIR`](https://cmake.org/cmake/help/latest/envvar/CMAKE_CONFIG_DIR.html#envvar:CMAKE_CONFIG_DIR "CMAKE_CONFIG_DIR") under `<config_dir>/instrumentation/<version>/query/`.

### [Enabling Instrumentation for CDash Submissions](https://cmake.org/cmake/help/latest/manual/cmake-instrumentation.7.html#id9)[¶](https://cmake.org/cmake/help/latest/manual/cmake-instrumentation.7.html#enabling-instrumentation-for-cdash-submissions "Link to this heading")

You can enable instrumentation when using [`CTest`](https://cmake.org/cmake/help/latest/module/CTest.html#module:CTest "CTest") in [Dashboard Client](https://cmake.org/cmake/help/latest/manual/ctest.1.html#dashboard-client) mode by setting the [`CTEST_USE_INSTRUMENTATION`](https://cmake.org/cmake/help/latest/envvar/CTEST_USE_INSTRUMENTATION.html#envvar:CTEST_USE_INSTRUMENTATION "CTEST_USE_INSTRUMENTATION") environment variable. Doing so automatically enables the `dynamicSystemInformation` option.

The following table shows how each type of instrumented command gets mapped to a corresponding type of CTest XML file.

| [Snippet Role](https://cmake.org/cmake/help/latest/manual/cmake-instrumentation.7.html#cmake-instrumentation-data-v1) | CTest XML File |
| --- | --- |
| `configure` | `Configure.xml` |
| `generate` | `Configure.xml` |
| `compile` | `Build.xml` |
| `link` | `Build.xml` |
| `custom` | `Build.xml` |
| `build` | unused! |
| `cmakeBuild` | `Build.xml` |
| `cmakeInstall` | `Build.xml` |
| `install` | `Build.xml` |
| `ctest` | `Build.xml` |
| `test` | `Test.xml` |

By default the command line reported to CDash is truncated at the first space. You can instead choose to report the full command line (including arguments) by setting [`CTEST_USE_VERBOSE_INSTRUMENTATION`](https://cmake.org/cmake/help/latest/envvar/CTEST_USE_VERBOSE_INSTRUMENTATION.html#envvar:CTEST_USE_VERBOSE_INSTRUMENTATION "CTEST_USE_VERBOSE_INSTRUMENTATION") to 1.

Alternatively, you can use the [v1 Query Files](https://cmake.org/cmake/help/latest/manual/cmake-instrumentation.7.html#v1-query-files) to enable instrumentation for CDash using the `cdashSubmit` and `cdashVerbose` options.

In order for the submitted `Build.xml` file to group the snippet files correctly, all configure and build commands should be executed with CTest in Dashboard Client mode.

[API v1](https://cmake.org/cmake/help/latest/manual/cmake-instrumentation.7.html#id10)[¶](https://cmake.org/cmake/help/latest/manual/cmake-instrumentation.7.html#api-v1 "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The API version specifies the layout of the instrumentation directory, as well as the general format of the query files and [`cmake_instrumentation()`](https://cmake.org/cmake/help/latest/command/cmake_instrumentation.html#command:cmake_instrumentation "cmake_instrumentation") command arguments.

The Instrumentation API v1 is housed in the `instrumentation/v1/` directory under either `<build>/.cmake/` for output data and project-level queries, or `<config_dir>/` for user-level queries. The `v1` component of this directory is what signifies the API version. It has the following subdirectories:

`query/`
Holds query files written by users or clients. Any file with the `.json` file extension will be recognized as a query file. These files are owned by whichever client or user creates them.

`query/generated/`
Holds query files generated by a CMake project with the [`cmake_instrumentation()`](https://cmake.org/cmake/help/latest/command/cmake_instrumentation.html#command:cmake_instrumentation "cmake_instrumentation") command or the [`CTEST_USE_INSTRUMENTATION`](https://cmake.org/cmake/help/latest/envvar/CTEST_USE_INSTRUMENTATION.html#envvar:CTEST_USE_INSTRUMENTATION "CTEST_USE_INSTRUMENTATION") variable. These files are owned by CMake and are deleted and regenerated automatically during the CMake configure step.

`data/`
Holds instrumentation data collected on the project. CMake owns all data files, they should never be removed by other processes. Data collected here remains until after [Indexing](https://cmake.org/cmake/help/latest/manual/cmake-instrumentation.7.html#indexing) occurs and all [Callbacks](https://cmake.org/cmake/help/latest/manual/cmake-instrumentation.7.html#callbacks) are executed.

`data/index/`
A subset of the collected data, containing any [v1 Index Files](https://cmake.org/cmake/help/latest/manual/cmake-instrumentation.7.html#v1-index-file).

`data/content/`
A subset of the collected data, containing any [v1 CMake Content Files](https://cmake.org/cmake/help/latest/manual/cmake-instrumentation.7.html#v1-cmake-content-file).

`data/trace/`
A subset of the collected data, containing the [Google Trace File](https://cmake.org/cmake/help/latest/manual/cmake-instrumentation.7.html#google-trace-file) created from the most recent [Indexing](https://cmake.org/cmake/help/latest/manual/cmake-instrumentation.7.html#indexing). Unlike other data files, the most recent trace file remains even after [Indexing](https://cmake.org/cmake/help/latest/manual/cmake-instrumentation.7.html#indexing) occurs and all [Callbacks](https://cmake.org/cmake/help/latest/manual/cmake-instrumentation.7.html#callbacks) are executed, until the next time [Indexing](https://cmake.org/cmake/help/latest/manual/cmake-instrumentation.7.html#indexing) occurs.

`cdash/`
Holds temporary files used internally to generate XML content to be submitted to CDash.

### [v1 Query Files](https://cmake.org/cmake/help/latest/manual/cmake-instrumentation.7.html#id11)[¶](https://cmake.org/cmake/help/latest/manual/cmake-instrumentation.7.html#v1-query-files "Link to this heading")

Any file with the `.json` extension under the `instrumentation/v1/query/` directory is recognized as a query for instrumentation data.

These files must contain a JSON object with the following keys. The `version` key is required, but all other fields are optional.

`version`
The Data version of snippet file to generate, an integer. Currently the only supported version is `1`.

`callbacks`
A list of command-line strings for [Callbacks](https://cmake.org/cmake/help/latest/manual/cmake-instrumentation.7.html#callbacks) to handle collected instrumentation data. Whenever these callbacks are executed, the full path to a [v1 Index File](https://cmake.org/cmake/help/latest/manual/cmake-instrumentation.7.html#v1-index-file) is appended to the arguments included in the string.

`hooks`
A list of strings specifying when [Indexing](https://cmake.org/cmake/help/latest/manual/cmake-instrumentation.7.html#indexing) should occur automatically. These are the intervals when instrumentation data should be collated and user [Callbacks](https://cmake.org/cmake/help/latest/manual/cmake-instrumentation.7.html#callbacks) should be invoked to handle the data. Elements in this list should be one of the following:

*   `postGenerate`

*   `preBuild` (called when `ninja` or `make` is invoked)

*   `postBuild` (called when `ninja` or `make` completes)

*   `preCMakeBuild` (called when [`cmake --build`](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-build) is invoked)

*   `postCMakeBuild` (called when [`cmake --build`](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-build) completes)

*   `postCMakeInstall`

*   `postCMakeWorkflow`

*   `postCTest`

`preBuild` and `postBuild` are not supported when using the [`MSYS Makefiles`](https://cmake.org/cmake/help/latest/generator/MSYS%20Makefiles.html#generator:MSYS%20Makefiles "MSYS Makefiles") or [`FASTBuild`](https://cmake.org/cmake/help/latest/generator/FASTBuild.html#generator:FASTBuild "FASTBuild") generators. Additionally, they will not be triggered when the build tool is invoked by [`cmake --build`](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-build).

`options`
A list of strings used to enable certain optional behavior, including the collection of certain additional data. Elements in this list should be one of the following:

> `staticSystemInformation`
> Enables collection of the static information about the host machine CMake is being run from. This data is collected during [Indexing](https://cmake.org/cmake/help/latest/manual/cmake-instrumentation.7.html#indexing) and is included in the generated [v1 Index File](https://cmake.org/cmake/help/latest/manual/cmake-instrumentation.7.html#v1-index-file).
> 
> `dynamicSystemInformation`
> Enables collection of the dynamic information about the host machine CMake is being run from. Data is collected for every [v1 Snippet File](https://cmake.org/cmake/help/latest/manual/cmake-instrumentation.7.html#v1-snippet-file) generated by CMake, and includes information from immediately before and after the command is executed.
> 
> `cdashSubmit`
> Enables including instrumentation data in CDash. This is equivalent to having the [`CTEST_USE_INSTRUMENTATION`](https://cmake.org/cmake/help/latest/envvar/CTEST_USE_INSTRUMENTATION.html#envvar:CTEST_USE_INSTRUMENTATION "CTEST_USE_INSTRUMENTATION") environment variable enabled.
> 
> `cdashVerbose`
> Enables including the full untruncated commands in data submitted to CDash. Equivalent to having the [`CTEST_USE_VERBOSE_INSTRUMENTATION`](https://cmake.org/cmake/help/latest/envvar/CTEST_USE_VERBOSE_INSTRUMENTATION.html#envvar:CTEST_USE_VERBOSE_INSTRUMENTATION "CTEST_USE_VERBOSE_INSTRUMENTATION") and [`CTEST_USE_INSTRUMENTATION`](https://cmake.org/cmake/help/latest/envvar/CTEST_USE_INSTRUMENTATION.html#envvar:CTEST_USE_INSTRUMENTATION "CTEST_USE_INSTRUMENTATION") environment variables enabled.
> 
> `trace`
> Enables generation of a [Google Trace File](https://cmake.org/cmake/help/latest/manual/cmake-instrumentation.7.html#google-trace-file) during [Indexing](https://cmake.org/cmake/help/latest/manual/cmake-instrumentation.7.html#indexing) to visualize data from the [v1 Snippet Files](https://cmake.org/cmake/help/latest/manual/cmake-instrumentation.7.html#v1-snippet-file) collected.

The `callbacks` listed will be invoked during the specified hooks _at a minimum_. When there are multiple query files, the `callbacks`, `hooks` and `options` between them will be merged. Therefore, if any query file includes any `hooks`, every `callback` across all query files will be executed at every `hook` across all query files. Additionally, if any query file requests optional data using the `options` field, any related data will be present in all snippet files. User written `callbacks` should be able to handle the presence of this optional data, since it may be requested by an unrelated query.

The JSON format is described in machine-readable form by [`this JSON schema`](https://cmake.org/cmake/help/latest/_downloads/eb9fce565e82cb518917ef965f4ecf04/query-v1-schema.json).

Example:

{
 "version": 1,
 "callbacks": [
 "/usr/bin/python callback.py",
 "/usr/bin/cmake -P callback.cmake arg",
 ],
 "hooks": [
 "postCMakeBuild",
 "postCMakeInstall"
 ],
 "options": [
 "staticSystemInformation",
 "dynamicSystemInformation",
 "cdashSubmit",
 "trace"
 ]
}

In this example, after every [`cmake --build`](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-build) or [`cmake --install`](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-install) invocation, an index file `index-<timestamp>.json` will be generated in `<build>/.cmake/instrumentation/v1/data/index` containing a list of data snippet files created since the previous indexing. The commands `/usr/bin/python callback.py index-<timestamp>.json` and `/usr/bin/cmake -P callback.cmake arg index-<timestamp>.json` will be executed in that order. The index file will contain the `staticSystemInformation` data and each snippet file listed in the index will contain the `dynamicSystemInformation` data. Additionally, the index file will contain the path to the generated [Google Trace File](https://cmake.org/cmake/help/latest/manual/cmake-instrumentation.7.html#google-trace-file). Once both callbacks have completed, the index file and data files listed by it (including snippet files, but not the trace file) will be deleted from the project build tree. The instrumentation data will be present in the XML files submitted to CDash, but with truncated command strings because `cdashVerbose` was not enabled.

[Data v1](https://cmake.org/cmake/help/latest/manual/cmake-instrumentation.7.html#id12)[¶](https://cmake.org/cmake/help/latest/manual/cmake-instrumentation.7.html#data-v1 "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Data version specifies the contents of the output files generated by the CMake instrumentation API as part of the [Data Collection](https://cmake.org/cmake/help/latest/manual/cmake-instrumentation.7.html#data-collection) and [Indexing](https://cmake.org/cmake/help/latest/manual/cmake-instrumentation.7.html#indexing). A new version number will be created whenever previously included data is removed or reformatted such that scripts written to parse this data may become incompatible with the new format. There are four types of data files generated: the [v1 Snippet File](https://cmake.org/cmake/help/latest/manual/cmake-instrumentation.7.html#v1-snippet-file), [v1 Index File](https://cmake.org/cmake/help/latest/manual/cmake-instrumentation.7.html#v1-index-file), [v1 CMake Content File](https://cmake.org/cmake/help/latest/manual/cmake-instrumentation.7.html#v1-cmake-content-file), and the [Google Trace File](https://cmake.org/cmake/help/latest/manual/cmake-instrumentation.7.html#google-trace-file). When using the [API v1](https://cmake.org/cmake/help/latest/manual/cmake-instrumentation.7.html#api-v1), these files live in `<build>/.cmake/instrumentation/v1/data/` under the project build tree.

### [v1 Snippet File](https://cmake.org/cmake/help/latest/manual/cmake-instrumentation.7.html#id13)[¶](https://cmake.org/cmake/help/latest/manual/cmake-instrumentation.7.html#v1-snippet-file "Link to this heading")

Snippet files are generated for every compile, link and custom command invoked as part of the CMake build or install step and contain instrumentation data about the command executed. Additionally, snippet files are created for the following:

*   The CMake configure step

*   The CMake generate step

*   Entire build step (executed with [`cmake --build`](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-build))

*   Entire install step (executed with [`cmake --install`](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-install))

*   Each time [`ctest`](https://cmake.org/cmake/help/latest/manual/ctest.1.html#manual:ctest(1) "ctest(1)") is invoked to [run tests](https://cmake.org/cmake/help/latest/manual/ctest.1.html#run-tests) (even if no tests are found)

*   Each individual test executed by [`ctest`](https://cmake.org/cmake/help/latest/manual/ctest.1.html#manual:ctest(1) "ctest(1)")

These files remain in the build tree until after [Indexing](https://cmake.org/cmake/help/latest/manual/cmake-instrumentation.7.html#indexing) occurs and any user-specified [Callbacks](https://cmake.org/cmake/help/latest/manual/cmake-instrumentation.7.html#callbacks) are executed.

Note

Configure and generate snippet files are not written by CMake until the generate step is complete. When using [`cmake-gui(1)`](https://cmake.org/cmake/help/latest/manual/cmake-gui.1.html#manual:cmake-gui(1) "cmake-gui(1)") or [`ccmake(1)`](https://cmake.org/cmake/help/latest/manual/ccmake.1.html#manual:ccmake(1) "ccmake(1)"), triggering only configure step(s) without generating the project files will not generate any configure snippets. Once the generate step is run, there will be one configure snippet for each time the configure step was run.

Snippet files have a filename with the syntax `<role>-<hash>-<timestamp>.json` and contain the following data:

> `version`
> The Data version of the snippet file, an integer. Currently the version is always `1`.
> 
> `command`
> The full command executed. Excluded when `role` is `build`.
> 
> `workingDir`
> The working directory in which the `command` was executed.
> 
> `result`
> The exit code of the command, an integer. This will be `null` when `role` is `build`.
> 
> `role`
> The type of command executed, which will be one of the following values:
> 
> 
> *   `configure`: the CMake configure step
> 
> *   `generate`: the CMake generate step
> 
> *   `compile`: an individual compile step invoked during the build
> 
> *   `link`: an individual link step invoked during the build
> 
> *   `custom`: an individual custom command invoked during the build
> 
> *   `build`: a complete `make` or `ninja` invocation (not through [`cmake --build`](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-build)).
> 
> *   `cmakeBuild`: a complete [`cmake --build`](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-build) invocation
> 
> *   `cmakeInstall`: a complete [`cmake --install`](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-install) invocation
> 
> *   `install`: an individual `cmake -P cmake_install.cmake` invocation
> 
> *   `ctest`: a complete [`ctest`](https://cmake.org/cmake/help/latest/manual/ctest.1.html#manual:ctest(1) "ctest(1)") command invocation
> 
> *   `test`: a single test executed by [`ctest`](https://cmake.org/cmake/help/latest/manual/ctest.1.html#manual:ctest(1) "ctest(1)")
> 
> 
> `target`
> The CMake target associated with the command. Only included when `role` is `compile` or `link`, or when `role` is `custom` and the custom command is attached to a target with [Build Events](https://cmake.org/cmake/help/latest/command/add_custom_command.html#add-custom-command-target). In conjunction with `cmakeContent`, this can be used to look up the target [`TYPE`](https://cmake.org/cmake/help/latest/prop_tgt/TYPE.html#prop_tgt:TYPE "TYPE") and [`LABELS`](https://cmake.org/cmake/help/latest/prop_tgt/LABELS.html#prop_tgt:LABELS "LABELS").
> 
> `timeStart`
> Time at which the command started, expressed as the number of milliseconds since the system epoch.
> 
> `duration`
> The duration that the command ran for, expressed in milliseconds.
> 
> `outputs`
> The command's output file(s), an array. Only included when `role` is one of: `compile`, `link`, `custom`.
> 
> `outputSizes`
> The size(s) in bytes of the `outputs`, an array. For files which do not exist, the size is 0. Included under the same conditions as the `outputs` field.
> 
> `source`
> The source file being compiled. Only included when `role` is `compile`.
> 
> `language`
> The language of the source file being compiled. Only included when `role` is `compile` or `link`.
> 
> `testName`
> The name of the test being executed. Only included when `role` is `test`.
> 
> `config`
> The [Build Configuration](https://cmake.org/cmake/help/latest/manual/cmake-buildsystem.7.html#build-configurations), such as `Release` or `Debug`. Only included when `role` is one of: `compile`, `link`, `custom`, `install`, `test`.
> 
> `dynamicSystemInformation`
> Specifies the dynamic information collected about the host machine CMake is being run from. Data is collected for every snippet file generated by CMake, with data immediately before and after the command is executed. Only included when enabled by the [v1 Query Files](https://cmake.org/cmake/help/latest/manual/cmake-instrumentation.7.html#v1-query-files).
> 
> `beforeHostMemoryUsed`
> The Host Memory Used in KiB at `timeStart`.
> 
> `afterHostMemoryUsed`
> The Host Memory Used in KiB at `timeStart + duration`.
> 
> `beforeCPULoadAverage`
> The Average CPU Load at `timeStart`, or `null` if it cannot be determined.
> 
> `afterCPULoadAverage`
> The Average CPU Load at `timeStart + duration`, or `null` if it cannot be determined.
> 
> `cmakeContent`
> The path to a [v1 CMake Content File](https://cmake.org/cmake/help/latest/manual/cmake-instrumentation.7.html#v1-cmake-content-file) located under `data`, which contains information about the CMake configure and generate steps responsible for generating the `command` in this snippet. When using [`cmake-gui(1)`](https://cmake.org/cmake/help/latest/manual/cmake-gui.1.html#manual:cmake-gui(1) "cmake-gui(1)") or [`ccmake(1)`](https://cmake.org/cmake/help/latest/manual/ccmake.1.html#manual:ccmake(1) "ccmake(1)"), this field may be `null` for all configure steps up to the most recent one before the generate step.
> 
> `showOnly`
> A boolean representing whether the [`--show-only`](https://cmake.org/cmake/help/latest/manual/ctest.1.html#cmdoption-ctest-N) option was passed to [`ctest`](https://cmake.org/cmake/help/latest/manual/ctest.1.html#manual:ctest(1) "ctest(1)"). Only included when `role` is `ctest`.

Example:

{
 "version": 1,
 "command" : "\"/usr/bin/c++\" \"-MD\" \"-MT\" \"CMakeFiles/main.dir/main.cxx.o\" \"-MF\" \"CMakeFiles/main.dir/main.cxx.o.d\" \"-o\" \"CMakeFiles/main.dir/main.cxx.o\" \"-c\" \"<src>/main.cxx\"",
 "role" : "compile",
 "result" : 1,
 "target": "main",
 "language" : "C++",
 "outputs" : [ "CMakeFiles/main.dir/main.cxx.o" ],
 "outputSizes" : [ 0 ],
 "source" : "<src>/main.cxx",
 "config" : "Debug",
 "dynamicSystemInformation" :
 {
 "afterCPULoadAverage" : 2.3500000000000001,
 "afterHostMemoryUsed" : 6635680.0
 "beforeCPULoadAverage" : 2.3500000000000001,
 "beforeHostMemoryUsed" : 6635832.0
 },
 "timeStart" : 1737053448177,
 "duration" : 31,
 "cmakeContent" : "content/cmake-2025-07-11T12-46-32-0572.json"
}

### [v1 Index File](https://cmake.org/cmake/help/latest/manual/cmake-instrumentation.7.html#id14)[¶](https://cmake.org/cmake/help/latest/manual/cmake-instrumentation.7.html#v1-index-file "Link to this heading")

Index files contain a list of [v1 Snippet Files](https://cmake.org/cmake/help/latest/manual/cmake-instrumentation.7.html#v1-snippet-file). It serves as an entry point for navigating the instrumentation data. They are generated whenever [Indexing](https://cmake.org/cmake/help/latest/manual/cmake-instrumentation.7.html#indexing) occurs and deleted after any user-specified [Callbacks](https://cmake.org/cmake/help/latest/manual/cmake-instrumentation.7.html#callbacks) are executed.

`version`
The Data version of the index file, an integer. Currently the version is always `1`.

`buildDir`
The build directory of the CMake project.

`dataDir`
The full path to the `<build>/.cmake/instrumentation/v1/data/` directory.

`hook`
The name of the hook responsible for generating the index file. In addition to the hooks that can be specified by one of the [v1 Query Files](https://cmake.org/cmake/help/latest/manual/cmake-instrumentation.7.html#v1-query-files), this value may be set to `manual` if indexing is performed by invoking [`ctest --collect-instrumentation`](https://cmake.org/cmake/help/latest/manual/ctest.1.html#cmdoption-ctest-collect-instrumentation).

`snippets`
Contains a list of [v1 Snippet Files](https://cmake.org/cmake/help/latest/manual/cmake-instrumentation.7.html#v1-snippet-file). This includes all snippet files generated since the previous index file was created. The file paths are relative to `dataDir`.

`trace`
Contains the path to the [Google Trace File](https://cmake.org/cmake/help/latest/manual/cmake-instrumentation.7.html#google-trace-file). This includes data from all corresponding `snippets` in the index file. The file path is relative to `dataDir`. Only included when enabled by the [v1 Query Files](https://cmake.org/cmake/help/latest/manual/cmake-instrumentation.7.html#v1-query-files).

`staticSystemInformation`
Specifies the static information collected about the host machine CMake is being run from. If CMake is unable to determine the value of any given field, it will be `null`. See [`cmake_host_system_information()`](https://cmake.org/cmake/help/latest/command/cmake_host_system_information.html#command:cmake_host_system_information "cmake_host_system_information") for a description of each of the following fields.

Only included when enabled by the [v1 Query Files](https://cmake.org/cmake/help/latest/manual/cmake-instrumentation.7.html#v1-query-files).

*   `OSName`

*   `OSPlatform`

*   `OSRelease`

*   `OSVersion`

*   `familyId`

*   `hostname`

*   `is64Bits`

*   `modelId`

*   `modelName`

*   `numberOfLogicalCPU`

*   `numberOfPhysicalCPU`

*   `processorAPICID`

*   `processorCacheSize`

*   `processorClockFrequency`

*   `processorName`

*   `totalPhysicalMemory`

*   `totalVirtualMemory`

*   `vendorID`

*   `vendorString`

Example:

{
 "version": 1,
 "hook": "manual",
 "buildDir": "<build>",
 "dataDir": "<build>/.cmake/instrumentation/v1/data",
 "snippets": [
 "configure-<hash>-<timestamp>.json",
 "generate-<hash>-<timestamp>.json",
 "compile-<hash>-<timestamp>.json",
 "compile-<hash>-<timestamp>.json",
 "link-<hash>-<timestamp>.json",
 "install-<hash>-<timestamp>.json",
 "ctest-<hash>-<timestamp>.json",
 "test-<hash>-<timestamp>.json",
 "test-<hash>-<timestamp>.json",
 ],
 "trace": "trace/trace-<timestamp>.json"
}

### [v1 CMake Content File](https://cmake.org/cmake/help/latest/manual/cmake-instrumentation.7.html#id15)[¶](https://cmake.org/cmake/help/latest/manual/cmake-instrumentation.7.html#v1-cmake-content-file "Link to this heading")

CMake content files contain information about the CMake configure and generate steps. Each [v1 Snippet File](https://cmake.org/cmake/help/latest/manual/cmake-instrumentation.7.html#v1-snippet-file) provides the path to one of these files corresponding to the CMake invocation responsible for generating its command.

Each CMake content file contains the following:

> `project`
> The value of [`CMAKE_PROJECT_NAME`](https://cmake.org/cmake/help/latest/variable/CMAKE_PROJECT_NAME.html#variable:CMAKE_PROJECT_NAME "CMAKE_PROJECT_NAME").
> 
> `custom`
> An object containing arbitrary JSON data specified by the user with the [Custom CMake Content](https://cmake.org/cmake/help/latest/command/cmake_instrumentation.html#cmake-instrumentation-custom-content) functionality of the [`cmake_instrumentation()`](https://cmake.org/cmake/help/latest/command/cmake_instrumentation.html#command:cmake_instrumentation "cmake_instrumentation") command.
> 
> `targets`
> An object containing CMake targets, indexed by name, that have corresponding instrumentation data. Each target contains the following:
> 
> `type`
> The [`TYPE`](https://cmake.org/cmake/help/latest/prop_tgt/TYPE.html#prop_tgt:TYPE "TYPE") property of the target. Only `EXECUTABLE`, `STATIC_LIBRARY`, `SHARED_LIBRARY`, `MODULE_LIBRARY` and `OBJECT_LIBRARY` targets are included.
> 
> `labels`
> The [`LABELS`](https://cmake.org/cmake/help/latest/prop_tgt/LABELS.html#prop_tgt:LABELS "LABELS") property of the target.

### [Google Trace File](https://cmake.org/cmake/help/latest/manual/cmake-instrumentation.7.html#id16)[¶](https://cmake.org/cmake/help/latest/manual/cmake-instrumentation.7.html#google-trace-file "Link to this heading")

Trace files follow the [Google Trace Event Format](https://docs.google.com/document/d/1CvAClvFfyA5R-PhYUmn5OOQtYMH4h6I0nSsKchNAySU/preview). They include data from all [v1 Snippet Files](https://cmake.org/cmake/help/latest/manual/cmake-instrumentation.7.html#v1-snippet-file) listed in the current index file. These files remain in the build tree even after [Indexing](https://cmake.org/cmake/help/latest/manual/cmake-instrumentation.7.html#indexing) occurs and all [Callbacks](https://cmake.org/cmake/help/latest/manual/cmake-instrumentation.7.html#callbacks) are executed, until the next time [Indexing](https://cmake.org/cmake/help/latest/manual/cmake-instrumentation.7.html#indexing) occurs.

Trace files are stored in the `JSON Array Format`, where each [v1 Snippet File](https://cmake.org/cmake/help/latest/manual/cmake-instrumentation.7.html#v1-snippet-file) corresponds to a single trace event object. Each trace event contains the following data:

`name`
A descriptive name generated by CMake based on the given snippet data.

`cat`
The `role` from the [v1 Snippet File](https://cmake.org/cmake/help/latest/manual/cmake-instrumentation.7.html#v1-snippet-file).

`ph`
Currently, always `"X"` to represent "Complete Events".

`ts`
The `timeStart` from the [v1 Snippet File](https://cmake.org/cmake/help/latest/manual/cmake-instrumentation.7.html#v1-snippet-file), converted from milliseconds to microseconds.

`dur`
The `duration` from the [v1 Snippet File](https://cmake.org/cmake/help/latest/manual/cmake-instrumentation.7.html#v1-snippet-file), converted from milliseconds to microseconds.

`pid`
Unused (always zero).

`tid`
An integer ranging from zero to the number of concurrent jobs with which the processes being indexed ran. This is a synthetic ID calculated by CMake based on the `ts` and `dur` of all snippet files being indexed in order to produce a more useful visualization of the process concurrency.

`args`
Contains all data from the [v1 Snippet File](https://cmake.org/cmake/help/latest/manual/cmake-instrumentation.7.html#v1-snippet-file) corresponding to this trace event.
