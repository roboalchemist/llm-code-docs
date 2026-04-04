# Source: https://cmake.org/cmake/help/latest/manual/cmake-env-variables.7.html

Title: cmake-env-variables(7) — CMake 4.3.0-rc3 Documentation

URL Source: https://cmake.org/cmake/help/latest/manual/cmake-env-variables.7.html

Markdown Content:
Contents

*   [cmake-env-variables(7)](https://cmake.org/cmake/help/latest/manual/cmake-env-variables.7.html#cmake-env-variables-7)

    *   [Environment Variables that Change Behavior](https://cmake.org/cmake/help/latest/manual/cmake-env-variables.7.html#environment-variables-that-change-behavior)

    *   [Environment Variables that Control the Build](https://cmake.org/cmake/help/latest/manual/cmake-env-variables.7.html#environment-variables-that-control-the-build)

    *   [Environment Variables for Languages](https://cmake.org/cmake/help/latest/manual/cmake-env-variables.7.html#environment-variables-for-languages)

    *   [Environment Variables for CTest](https://cmake.org/cmake/help/latest/manual/cmake-env-variables.7.html#environment-variables-for-ctest)

    *   [Environment Variables for the CMake curses interface](https://cmake.org/cmake/help/latest/manual/cmake-env-variables.7.html#environment-variables-for-the-cmake-curses-interface)

This page lists environment variables that have special meaning to CMake.

For general information on environment variables, see the [Environment Variables](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#cmake-language-environment-variables) section in the cmake-language manual.

[Environment Variables that Change Behavior](https://cmake.org/cmake/help/latest/manual/cmake-env-variables.7.html#id2)[¶](https://cmake.org/cmake/help/latest/manual/cmake-env-variables.7.html#environment-variables-that-change-behavior "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

*   [CLICOLOR](https://cmake.org/cmake/help/latest/envvar/CLICOLOR.html)
*   [CLICOLOR_FORCE](https://cmake.org/cmake/help/latest/envvar/CLICOLOR_FORCE.html)
*   [CMAKE_APPBUNDLE_PATH](https://cmake.org/cmake/help/latest/envvar/CMAKE_APPBUNDLE_PATH.html)
*   [CMAKE_FRAMEWORK_PATH](https://cmake.org/cmake/help/latest/envvar/CMAKE_FRAMEWORK_PATH.html)
*   [CMAKE_INCLUDE_PATH](https://cmake.org/cmake/help/latest/envvar/CMAKE_INCLUDE_PATH.html)
*   [CMAKE_LIBRARY_PATH](https://cmake.org/cmake/help/latest/envvar/CMAKE_LIBRARY_PATH.html)
*   [CMAKE_MAXIMUM_RECURSION_DEPTH](https://cmake.org/cmake/help/latest/envvar/CMAKE_MAXIMUM_RECURSION_DEPTH.html)
*   [CMAKE_POLICY_VERSION_MINIMUM](https://cmake.org/cmake/help/latest/envvar/CMAKE_POLICY_VERSION_MINIMUM.html)
*   [CMAKE_PREFIX_PATH](https://cmake.org/cmake/help/latest/envvar/CMAKE_PREFIX_PATH.html)
*   [CMAKE_PROGRAM_PATH](https://cmake.org/cmake/help/latest/envvar/CMAKE_PROGRAM_PATH.html)
*   [CMAKE_TLS_VERIFY](https://cmake.org/cmake/help/latest/envvar/CMAKE_TLS_VERIFY.html)
*   [CMAKE_TLS_VERSION](https://cmake.org/cmake/help/latest/envvar/CMAKE_TLS_VERSION.html)
*   [NO_COLOR](https://cmake.org/cmake/help/latest/envvar/NO_COLOR.html)
*   [SSL_CERT_DIR](https://cmake.org/cmake/help/latest/envvar/SSL_CERT_DIR.html)
*   [SSL_CERT_FILE](https://cmake.org/cmake/help/latest/envvar/SSL_CERT_FILE.html)

[Environment Variables that Control the Build](https://cmake.org/cmake/help/latest/manual/cmake-env-variables.7.html#id3)[¶](https://cmake.org/cmake/help/latest/manual/cmake-env-variables.7.html#environment-variables-that-control-the-build "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

*   [ADSP_ROOT](https://cmake.org/cmake/help/latest/envvar/ADSP_ROOT.html)
*   [CMAKE_APPLE_SILICON_PROCESSOR](https://cmake.org/cmake/help/latest/envvar/CMAKE_APPLE_SILICON_PROCESSOR.html)
*   [CMAKE_AUTOGEN_INTERMEDIATE_DIR_STRATEGY](https://cmake.org/cmake/help/latest/envvar/CMAKE_AUTOGEN_INTERMEDIATE_DIR_STRATEGY.html)
*   [CMAKE_BUILD_PARALLEL_LEVEL](https://cmake.org/cmake/help/latest/envvar/CMAKE_BUILD_PARALLEL_LEVEL.html)
*   [CMAKE_BUILD_TYPE](https://cmake.org/cmake/help/latest/envvar/CMAKE_BUILD_TYPE.html)
*   [CMAKE_COLOR_DIAGNOSTICS](https://cmake.org/cmake/help/latest/envvar/CMAKE_COLOR_DIAGNOSTICS.html)
*   [CMAKE_CONFIG_DIR](https://cmake.org/cmake/help/latest/envvar/CMAKE_CONFIG_DIR.html)
*   [CMAKE_CONFIG_TYPE](https://cmake.org/cmake/help/latest/envvar/CMAKE_CONFIG_TYPE.html)
*   [CMAKE_CONFIGURATION_TYPES](https://cmake.org/cmake/help/latest/envvar/CMAKE_CONFIGURATION_TYPES.html)
*   [CMAKE_CROSSCOMPILING_EMULATOR](https://cmake.org/cmake/help/latest/envvar/CMAKE_CROSSCOMPILING_EMULATOR.html)
*   [CMAKE_EXPORT_BUILD_DATABASE](https://cmake.org/cmake/help/latest/envvar/CMAKE_EXPORT_BUILD_DATABASE.html)
*   [CMAKE_EXPORT_COMPILE_COMMANDS](https://cmake.org/cmake/help/latest/envvar/CMAKE_EXPORT_COMPILE_COMMANDS.html)
*   [CMAKE_FASTBUILD_VERBOSE_GENERATOR](https://cmake.org/cmake/help/latest/envvar/CMAKE_FASTBUILD_VERBOSE_GENERATOR.html)
*   [CMAKE_GENERATOR](https://cmake.org/cmake/help/latest/envvar/CMAKE_GENERATOR.html)
*   [CMAKE_GENERATOR_INSTANCE](https://cmake.org/cmake/help/latest/envvar/CMAKE_GENERATOR_INSTANCE.html)
*   [CMAKE_GENERATOR_PLATFORM](https://cmake.org/cmake/help/latest/envvar/CMAKE_GENERATOR_PLATFORM.html)
*   [CMAKE_GENERATOR_TOOLSET](https://cmake.org/cmake/help/latest/envvar/CMAKE_GENERATOR_TOOLSET.html)
*   [CMAKE_INSTALL_MODE](https://cmake.org/cmake/help/latest/envvar/CMAKE_INSTALL_MODE.html)
*   [CMAKE_INSTALL_PARALLEL_LEVEL](https://cmake.org/cmake/help/latest/envvar/CMAKE_INSTALL_PARALLEL_LEVEL.html)
*   [CMAKE_INSTALL_PREFIX](https://cmake.org/cmake/help/latest/envvar/CMAKE_INSTALL_PREFIX.html)
*   [CMAKE_INTERMEDIATE_DIR_STRATEGY](https://cmake.org/cmake/help/latest/envvar/CMAKE_INTERMEDIATE_DIR_STRATEGY.html)
*   [CMAKE_<LANG>_COMPILER_LAUNCHER](https://cmake.org/cmake/help/latest/envvar/CMAKE_LANG_COMPILER_LAUNCHER.html)
*   [CMAKE_<LANG>_IMPLICIT_LINK_DIRECTORIES_EXCLUDE](https://cmake.org/cmake/help/latest/envvar/CMAKE_LANG_IMPLICIT_LINK_DIRECTORIES_EXCLUDE.html)
*   [CMAKE_<LANG>_IMPLICIT_LINK_LIBRARIES_EXCLUDE](https://cmake.org/cmake/help/latest/envvar/CMAKE_LANG_IMPLICIT_LINK_LIBRARIES_EXCLUDE.html)
*   [CMAKE_<LANG>_LINKER_LAUNCHER](https://cmake.org/cmake/help/latest/envvar/CMAKE_LANG_LINKER_LAUNCHER.html)
*   [CMAKE_MSVCIDE_RUN_PATH](https://cmake.org/cmake/help/latest/envvar/CMAKE_MSVCIDE_RUN_PATH.html)
*   [CMAKE_NO_VERBOSE](https://cmake.org/cmake/help/latest/envvar/CMAKE_NO_VERBOSE.html)
*   [CMAKE_OSX_ARCHITECTURES](https://cmake.org/cmake/help/latest/envvar/CMAKE_OSX_ARCHITECTURES.html)
*   [CMAKE_TEST_LAUNCHER](https://cmake.org/cmake/help/latest/envvar/CMAKE_TEST_LAUNCHER.html)
*   [CMAKE_TOOLCHAIN_FILE](https://cmake.org/cmake/help/latest/envvar/CMAKE_TOOLCHAIN_FILE.html)
*   [DESTDIR](https://cmake.org/cmake/help/latest/envvar/DESTDIR.html)
*   [LDFLAGS](https://cmake.org/cmake/help/latest/envvar/LDFLAGS.html)
*   [MACOSX_DEPLOYMENT_TARGET](https://cmake.org/cmake/help/latest/envvar/MACOSX_DEPLOYMENT_TARGET.html)
*   [<PackageName>_ROOT](https://cmake.org/cmake/help/latest/envvar/PackageName_ROOT.html)
*   [VERBOSE](https://cmake.org/cmake/help/latest/envvar/VERBOSE.html)

[Environment Variables for Languages](https://cmake.org/cmake/help/latest/manual/cmake-env-variables.7.html#id4)[¶](https://cmake.org/cmake/help/latest/manual/cmake-env-variables.7.html#environment-variables-for-languages "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

*   [ASM<DIALECT>](https://cmake.org/cmake/help/latest/envvar/ASM_DIALECT.html)
*   [ASM<DIALECT>FLAGS](https://cmake.org/cmake/help/latest/envvar/ASM_DIALECTFLAGS.html)
*   [CC](https://cmake.org/cmake/help/latest/envvar/CC.html)
*   [CFLAGS](https://cmake.org/cmake/help/latest/envvar/CFLAGS.html)
*   [CSFLAGS](https://cmake.org/cmake/help/latest/envvar/CSFLAGS.html)
*   [CUDAARCHS](https://cmake.org/cmake/help/latest/envvar/CUDAARCHS.html)
*   [CUDACXX](https://cmake.org/cmake/help/latest/envvar/CUDACXX.html)
*   [CUDAFLAGS](https://cmake.org/cmake/help/latest/envvar/CUDAFLAGS.html)
*   [CUDAHOSTCXX](https://cmake.org/cmake/help/latest/envvar/CUDAHOSTCXX.html)
*   [CXX](https://cmake.org/cmake/help/latest/envvar/CXX.html)
*   [CXXFLAGS](https://cmake.org/cmake/help/latest/envvar/CXXFLAGS.html)
*   [FC](https://cmake.org/cmake/help/latest/envvar/FC.html)
*   [FFLAGS](https://cmake.org/cmake/help/latest/envvar/FFLAGS.html)
*   [HIPCXX](https://cmake.org/cmake/help/latest/envvar/HIPCXX.html)
*   [HIPFLAGS](https://cmake.org/cmake/help/latest/envvar/HIPFLAGS.html)
*   [HIPHOSTCXX](https://cmake.org/cmake/help/latest/envvar/HIPHOSTCXX.html)
*   [ISPC](https://cmake.org/cmake/help/latest/envvar/ISPC.html)
*   [ISPCFLAGS](https://cmake.org/cmake/help/latest/envvar/ISPCFLAGS.html)
*   [OBJC](https://cmake.org/cmake/help/latest/envvar/OBJC.html)
*   [OBJCFLAGS](https://cmake.org/cmake/help/latest/envvar/OBJCFLAGS.html)
*   [OBJCXX](https://cmake.org/cmake/help/latest/envvar/OBJCXX.html)
*   [OBJCXXFLAGS](https://cmake.org/cmake/help/latest/envvar/OBJCXXFLAGS.html)
*   [RC](https://cmake.org/cmake/help/latest/envvar/RC.html)
*   [RCFLAGS](https://cmake.org/cmake/help/latest/envvar/RCFLAGS.html)
*   [SWIFTC](https://cmake.org/cmake/help/latest/envvar/SWIFTC.html)

[Environment Variables for CTest](https://cmake.org/cmake/help/latest/manual/cmake-env-variables.7.html#id5)[¶](https://cmake.org/cmake/help/latest/manual/cmake-env-variables.7.html#environment-variables-for-ctest "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

*   [CMAKE_CONFIG_TYPE](https://cmake.org/cmake/help/latest/envvar/CMAKE_CONFIG_TYPE.html)
*   [CTEST_INTERACTIVE_DEBUG_MODE](https://cmake.org/cmake/help/latest/envvar/CTEST_INTERACTIVE_DEBUG_MODE.html)
*   [CTEST_NO_TESTS_ACTION](https://cmake.org/cmake/help/latest/envvar/CTEST_NO_TESTS_ACTION.html)
*   [CTEST_OUTPUT_ON_FAILURE](https://cmake.org/cmake/help/latest/envvar/CTEST_OUTPUT_ON_FAILURE.html)
*   [CTEST_PARALLEL_LEVEL](https://cmake.org/cmake/help/latest/envvar/CTEST_PARALLEL_LEVEL.html)
*   [CTEST_PROGRESS_OUTPUT](https://cmake.org/cmake/help/latest/envvar/CTEST_PROGRESS_OUTPUT.html)
*   [CTEST_USE_INSTRUMENTATION](https://cmake.org/cmake/help/latest/envvar/CTEST_USE_INSTRUMENTATION.html)
*   [CTEST_USE_LAUNCHERS_DEFAULT](https://cmake.org/cmake/help/latest/envvar/CTEST_USE_LAUNCHERS_DEFAULT.html)
*   [CTEST_USE_VERBOSE_INSTRUMENTATION](https://cmake.org/cmake/help/latest/envvar/CTEST_USE_VERBOSE_INSTRUMENTATION.html)
*   [DASHBOARD_TEST_FROM_CTEST](https://cmake.org/cmake/help/latest/envvar/DASHBOARD_TEST_FROM_CTEST.html)

[Environment Variables for the CMake curses interface](https://cmake.org/cmake/help/latest/manual/cmake-env-variables.7.html#id6)[¶](https://cmake.org/cmake/help/latest/manual/cmake-env-variables.7.html#environment-variables-for-the-cmake-curses-interface "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

*   [CCMAKE_COLORS](https://cmake.org/cmake/help/latest/envvar/CCMAKE_COLORS.html)
