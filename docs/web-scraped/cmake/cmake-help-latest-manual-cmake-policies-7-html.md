# Source: https://cmake.org/cmake/help/latest/manual/cmake-policies.7.html

Title: cmake-policies(7) — CMake 4.3.0-rc3 Documentation

URL Source: https://cmake.org/cmake/help/latest/manual/cmake-policies.7.html

Markdown Content:
Contents

*   [cmake-policies(7)](https://cmake.org/cmake/help/latest/manual/cmake-policies.7.html#cmake-policies-7)

    *   [Introduction](https://cmake.org/cmake/help/latest/manual/cmake-policies.7.html#introduction)

        *   [Updating Projects](https://cmake.org/cmake/help/latest/manual/cmake-policies.7.html#updating-projects)

        *   [Transition Schedule](https://cmake.org/cmake/help/latest/manual/cmake-policies.7.html#transition-schedule)

    *   [Supported Policies](https://cmake.org/cmake/help/latest/manual/cmake-policies.7.html#supported-policies)

        *   [Policies Introduced by CMake 4.3](https://cmake.org/cmake/help/latest/manual/cmake-policies.7.html#policies-introduced-by-cmake-4-3)

        *   [Policies Introduced by CMake 4.2](https://cmake.org/cmake/help/latest/manual/cmake-policies.7.html#policies-introduced-by-cmake-4-2)

        *   [Policies Introduced by CMake 4.1](https://cmake.org/cmake/help/latest/manual/cmake-policies.7.html#policies-introduced-by-cmake-4-1)

        *   [Policies Introduced by CMake 4.0](https://cmake.org/cmake/help/latest/manual/cmake-policies.7.html#policies-introduced-by-cmake-4-0)

        *   [Policies Introduced by CMake 3.31](https://cmake.org/cmake/help/latest/manual/cmake-policies.7.html#policies-introduced-by-cmake-3-31)

        *   [Policies Introduced by CMake 3.30](https://cmake.org/cmake/help/latest/manual/cmake-policies.7.html#policies-introduced-by-cmake-3-30)

        *   [Policies Introduced by CMake 3.29](https://cmake.org/cmake/help/latest/manual/cmake-policies.7.html#policies-introduced-by-cmake-3-29)

        *   [Policies Introduced by CMake 3.28](https://cmake.org/cmake/help/latest/manual/cmake-policies.7.html#policies-introduced-by-cmake-3-28)

        *   [Policies Introduced by CMake 3.27](https://cmake.org/cmake/help/latest/manual/cmake-policies.7.html#policies-introduced-by-cmake-3-27)

        *   [Policies Introduced by CMake 3.26](https://cmake.org/cmake/help/latest/manual/cmake-policies.7.html#policies-introduced-by-cmake-3-26)

        *   [Policies Introduced by CMake 3.25](https://cmake.org/cmake/help/latest/manual/cmake-policies.7.html#policies-introduced-by-cmake-3-25)

        *   [Policies Introduced by CMake 3.24](https://cmake.org/cmake/help/latest/manual/cmake-policies.7.html#policies-introduced-by-cmake-3-24)

        *   [Policies Introduced by CMake 3.23](https://cmake.org/cmake/help/latest/manual/cmake-policies.7.html#policies-introduced-by-cmake-3-23)

        *   [Policies Introduced by CMake 3.22](https://cmake.org/cmake/help/latest/manual/cmake-policies.7.html#policies-introduced-by-cmake-3-22)

        *   [Policies Introduced by CMake 3.21](https://cmake.org/cmake/help/latest/manual/cmake-policies.7.html#policies-introduced-by-cmake-3-21)

        *   [Policies Introduced by CMake 3.20](https://cmake.org/cmake/help/latest/manual/cmake-policies.7.html#policies-introduced-by-cmake-3-20)

        *   [Policies Introduced by CMake 3.19](https://cmake.org/cmake/help/latest/manual/cmake-policies.7.html#policies-introduced-by-cmake-3-19)

        *   [Policies Introduced by CMake 3.18](https://cmake.org/cmake/help/latest/manual/cmake-policies.7.html#policies-introduced-by-cmake-3-18)

        *   [Policies Introduced by CMake 3.17](https://cmake.org/cmake/help/latest/manual/cmake-policies.7.html#policies-introduced-by-cmake-3-17)

        *   [Policies Introduced by CMake 3.16](https://cmake.org/cmake/help/latest/manual/cmake-policies.7.html#policies-introduced-by-cmake-3-16)

        *   [Policies Introduced by CMake 3.15](https://cmake.org/cmake/help/latest/manual/cmake-policies.7.html#policies-introduced-by-cmake-3-15)

        *   [Policies Introduced by CMake 3.14](https://cmake.org/cmake/help/latest/manual/cmake-policies.7.html#policies-introduced-by-cmake-3-14)

        *   [Policies Introduced by CMake 3.13](https://cmake.org/cmake/help/latest/manual/cmake-policies.7.html#policies-introduced-by-cmake-3-13)

        *   [Policies Introduced by CMake 3.12](https://cmake.org/cmake/help/latest/manual/cmake-policies.7.html#policies-introduced-by-cmake-3-12)

        *   [Policies Introduced by CMake 3.11](https://cmake.org/cmake/help/latest/manual/cmake-policies.7.html#policies-introduced-by-cmake-3-11)

        *   [Policies Introduced by CMake 3.10](https://cmake.org/cmake/help/latest/manual/cmake-policies.7.html#policies-introduced-by-cmake-3-10)

        *   [Policies Introduced by CMake 3.9](https://cmake.org/cmake/help/latest/manual/cmake-policies.7.html#policies-introduced-by-cmake-3-9)

        *   [Policies Introduced by CMake 3.8](https://cmake.org/cmake/help/latest/manual/cmake-policies.7.html#policies-introduced-by-cmake-3-8)

        *   [Policies Introduced by CMake 3.7](https://cmake.org/cmake/help/latest/manual/cmake-policies.7.html#policies-introduced-by-cmake-3-7)

    *   [Unsupported Policies](https://cmake.org/cmake/help/latest/manual/cmake-policies.7.html#unsupported-policies)

        *   [Policies Introduced by CMake 3.4, Removed by CMake 4.0](https://cmake.org/cmake/help/latest/manual/cmake-policies.7.html#policies-introduced-by-cmake-3-4-removed-by-cmake-4-0)

        *   [Policies Introduced by CMake 3.3, Removed by CMake 4.0](https://cmake.org/cmake/help/latest/manual/cmake-policies.7.html#policies-introduced-by-cmake-3-3-removed-by-cmake-4-0)

        *   [Policies Introduced by CMake 3.2, Removed by CMake 4.0](https://cmake.org/cmake/help/latest/manual/cmake-policies.7.html#policies-introduced-by-cmake-3-2-removed-by-cmake-4-0)

        *   [Policies Introduced by CMake 3.1, Removed by CMake 4.0](https://cmake.org/cmake/help/latest/manual/cmake-policies.7.html#policies-introduced-by-cmake-3-1-removed-by-cmake-4-0)

        *   [Policies Introduced by CMake 3.0, Removed by CMake 4.0](https://cmake.org/cmake/help/latest/manual/cmake-policies.7.html#policies-introduced-by-cmake-3-0-removed-by-cmake-4-0)

        *   [Policies Introduced by CMake 2.8, Removed by CMake 4.0](https://cmake.org/cmake/help/latest/manual/cmake-policies.7.html#policies-introduced-by-cmake-2-8-removed-by-cmake-4-0)

        *   [Policies Introduced by CMake 2.6, Removed by CMake 4.0](https://cmake.org/cmake/help/latest/manual/cmake-policies.7.html#policies-introduced-by-cmake-2-6-removed-by-cmake-4-0)

[Introduction](https://cmake.org/cmake/help/latest/manual/cmake-policies.7.html#id2)[¶](https://cmake.org/cmake/help/latest/manual/cmake-policies.7.html#introduction "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

CMake policies introduce behavior changes while preserving compatibility for existing project releases. Policies are deprecation mechanisms, not feature toggles. Each policy documents a deprecated `OLD` behavior and a preferred `NEW` behavior. Projects must be updated over time to use the `NEW` behavior, but their existing releases will continue to work with the `OLD` behavior.

### [Updating Projects](https://cmake.org/cmake/help/latest/manual/cmake-policies.7.html#id3)[¶](https://cmake.org/cmake/help/latest/manual/cmake-policies.7.html#updating-projects "Link to this heading")

When policies are newly introduced by a version of CMake, their `OLD` behaviors are immediately deprecated by that version of CMake and later. Projects should be updated to use the `NEW` behaviors of the policies as soon as possible.

Use the [`cmake_minimum_required()`](https://cmake.org/cmake/help/latest/command/cmake_minimum_required.html#command:cmake_minimum_required "cmake_minimum_required") command to record the latest version of CMake for which a project has been updated. For example:

cmake_minimum_required(VERSION 3.10...4.2)

This uses the `<min>...<policy_max>` syntax to enable the `NEW` behaviors of policies introduced in CMake 4.2 and earlier while only requiring a minimum version of CMake 3.10. The project is expected to work with both the `OLD` and `NEW` behaviors of policies introduced between those versions.

### [Transition Schedule](https://cmake.org/cmake/help/latest/manual/cmake-policies.7.html#id4)[¶](https://cmake.org/cmake/help/latest/manual/cmake-policies.7.html#transition-schedule "Link to this heading")

To help projects port to the `NEW` behaviors of policies on their own schedule, CMake offers a transition period:

*   If a policy is not set by a project, CMake uses its `OLD` behavior, but may warn that the policy has not been set.

    *   Users running CMake may silence the warning without modifying a project by setting the [`CMAKE_POLICY_DEFAULT_CMP<NNNN>`](https://cmake.org/cmake/help/latest/variable/CMAKE_POLICY_DEFAULT_CMPNNNN.html#variable:CMAKE_POLICY_DEFAULT_CMP%3CNNNN%3E "CMAKE_POLICY_DEFAULT_CMP<NNNN>") variable as a cache entry on the [`cmake(1)`](https://cmake.org/cmake/help/latest/manual/cmake.1.html#manual:cmake(1) "cmake(1)") command line:

cmake -DCMAKE_POLICY_DEFAULT_CMP0990=OLD ... 
    *   Projects may silence the warning by using the [`cmake_policy()`](https://cmake.org/cmake/help/latest/command/cmake_policy.html#command:cmake_policy "cmake_policy") command to explicitly set the policy to `OLD` or `NEW` behavior:

if(POLICY CMP0990)
 cmake_policy(SET CMP0990 NEW)
endif() Note

A policy should almost never be set to `OLD`, except to silence warnings in an otherwise frozen or stable codebase, or temporarily as part of a larger migration path. 

*   If a policy is set to `OLD` by a project, CMake versions released at least 2 years after the version that introduced a policy may issue a warning that the policy's `OLD` behavior will be removed from a future version of CMake.

*   If a policy is not set to `NEW` by a project, CMake versions released at least 6 years after the version that introduced a policy, and whose major version number is higher, may issue an error that the policy's `OLD` behavior has been removed.

[Supported Policies](https://cmake.org/cmake/help/latest/manual/cmake-policies.7.html#id5)[¶](https://cmake.org/cmake/help/latest/manual/cmake-policies.7.html#supported-policies "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The following policies are supported.

### [Policies Introduced by CMake 4.3](https://cmake.org/cmake/help/latest/manual/cmake-policies.7.html#id6)[¶](https://cmake.org/cmake/help/latest/manual/cmake-policies.7.html#policies-introduced-by-cmake-4-3 "Link to this heading")

*   [CMP0210: CMAKE_<LANG>_LINK_FLAGS adds link flags to all target types.](https://cmake.org/cmake/help/latest/policy/CMP0210.html)
*   [CMP0209: Verify interface header sets checks executables without exports.](https://cmake.org/cmake/help/latest/policy/CMP0209.html)
*   [CMP0208: export(EXPORT) does not allow empty arguments.](https://cmake.org/cmake/help/latest/policy/CMP0208.html)
*   [CMP0207: file(GET_RUNTIME_DEPENDENCIES) normalizes paths before matching.](https://cmake.org/cmake/help/latest/policy/CMP0207.html)
*   [CMP0206: The CPack Archive Generator defaults to UID 0 and GID 0.](https://cmake.org/cmake/help/latest/policy/CMP0206.html)
*   [CMP0205: file(CREATE_LINK) with COPY_ON_ERROR copies directory content.](https://cmake.org/cmake/help/latest/policy/CMP0205.html)

### [Policies Introduced by CMake 4.2](https://cmake.org/cmake/help/latest/manual/cmake-policies.7.html#id7)[¶](https://cmake.org/cmake/help/latest/manual/cmake-policies.7.html#policies-introduced-by-cmake-4-2 "Link to this heading")

*   [CMP0204: A character set is always defined when targeting the MSVC ABI.](https://cmake.org/cmake/help/latest/policy/CMP0204.html)
*   [CMP0203: _WINDLL is defined for shared libraries targeting the MSVC ABI.](https://cmake.org/cmake/help/latest/policy/CMP0203.html)
*   [CMP0202: PDB file names always include their target's per-config POSTFIX.](https://cmake.org/cmake/help/latest/policy/CMP0202.html)
*   [CMP0201: Python::NumPy does not depend on Python::Development.Module.](https://cmake.org/cmake/help/latest/policy/CMP0201.html)
*   [CMP0200: Location and configuration selection for imported targets is more consistent.](https://cmake.org/cmake/help/latest/policy/CMP0200.html)
*   [CMP0199: $<CONFIG> does not match mapped configurations that are not selected.](https://cmake.org/cmake/help/latest/policy/CMP0199.html)
*   [CMP0198: CMAKE_PARENT_LIST_FILE is not defined in CMakeLists.txt.](https://cmake.org/cmake/help/latest/policy/CMP0198.html)

### [Policies Introduced by CMake 4.1](https://cmake.org/cmake/help/latest/manual/cmake-policies.7.html#id8)[¶](https://cmake.org/cmake/help/latest/manual/cmake-policies.7.html#policies-introduced-by-cmake-4-1 "Link to this heading")

*   [CMP0197: MSVC link -machine: flag is not in CMAKE_*_LINKER_FLAGS.](https://cmake.org/cmake/help/latest/policy/CMP0197.html)
*   [CMP0196: The CMakeDetermineVSServicePack module is removed.](https://cmake.org/cmake/help/latest/policy/CMP0196.html)
*   [CMP0195: Swift modules in build trees use the Swift module directory structure.](https://cmake.org/cmake/help/latest/policy/CMP0195.html)
*   [CMP0194: MSVC is not an assembler for language ASM.](https://cmake.org/cmake/help/latest/policy/CMP0194.html)
*   [CMP0193: GNUInstallDirs caches CMAKE_INSTALL_* with leading 'usr/' for install prefix '/'.](https://cmake.org/cmake/help/latest/policy/CMP0193.html)
*   [CMP0192: GNUInstallDirs uses absolute SYSCONFDIR, LOCALSTATEDIR, and RUNSTATEDIR in special prefixes.](https://cmake.org/cmake/help/latest/policy/CMP0192.html)
*   [CMP0191: The FindCABLE module is removed.](https://cmake.org/cmake/help/latest/policy/CMP0191.html)
*   [CMP0190: FindPython enforce consistency in cross-compiling mode.](https://cmake.org/cmake/help/latest/policy/CMP0190.html)
*   [CMP0189: TARGET_PROPERTY evaluates LINK_LIBRARIES properties transitively.](https://cmake.org/cmake/help/latest/policy/CMP0189.html)
*   [CMP0188: The FindGCCXML module is removed.](https://cmake.org/cmake/help/latest/policy/CMP0188.html)
*   [CMP0187: Include source file without an extension after the same name with an extension.](https://cmake.org/cmake/help/latest/policy/CMP0187.html)
*   [CMP0186: Regular expressions match ^ at most once in repeated searches.](https://cmake.org/cmake/help/latest/policy/CMP0186.html)

### [Policies Introduced by CMake 4.0](https://cmake.org/cmake/help/latest/manual/cmake-policies.7.html#id9)[¶](https://cmake.org/cmake/help/latest/manual/cmake-policies.7.html#policies-introduced-by-cmake-4-0 "Link to this heading")

*   [CMP0185: FindRuby no longer provides upper-case RUBY_* variables.](https://cmake.org/cmake/help/latest/policy/CMP0185.html)
*   [CMP0184: MSVC runtime checks flags are selected by an abstraction.](https://cmake.org/cmake/help/latest/policy/CMP0184.html)
*   [CMP0183: add_feature_info() supports full Condition Syntax.](https://cmake.org/cmake/help/latest/policy/CMP0183.html)
*   [CMP0182: Create shared library archives by default on AIX.](https://cmake.org/cmake/help/latest/policy/CMP0182.html)
*   [CMP0181: Link command-line fragment variables are parsed and re-quoted.](https://cmake.org/cmake/help/latest/policy/CMP0181.html)

### [Policies Introduced by CMake 3.31](https://cmake.org/cmake/help/latest/manual/cmake-policies.7.html#id10)[¶](https://cmake.org/cmake/help/latest/manual/cmake-policies.7.html#policies-introduced-by-cmake-3-31 "Link to this heading")

*   [CMP0180: project() always sets <PROJECT-NAME>_* as normal variables.](https://cmake.org/cmake/help/latest/policy/CMP0180.html)
*   [CMP0179: De-duplication of static libraries on link lines keeps first occurrence.](https://cmake.org/cmake/help/latest/policy/CMP0179.html)
*   [CMP0178: Test command lines preserve empty arguments.](https://cmake.org/cmake/help/latest/policy/CMP0178.html)
*   [CMP0177: install() DESTINATION paths are normalized.](https://cmake.org/cmake/help/latest/policy/CMP0177.html)
*   [CMP0176: execute_process() ENCODING is UTF-8 by default.](https://cmake.org/cmake/help/latest/policy/CMP0176.html)
*   [CMP0175: add_custom_command() rejects invalid arguments.](https://cmake.org/cmake/help/latest/policy/CMP0175.html)
*   [CMP0174: cmake_parse_arguments(PARSE_ARGV) defines a variable for an empty string after a single-value keyword.](https://cmake.org/cmake/help/latest/policy/CMP0174.html)
*   [CMP0173: The CMakeFindFrameworks module is removed.](https://cmake.org/cmake/help/latest/policy/CMP0173.html)
*   [CMP0172: The CPack module enables per-machine installation by default in the CPack WIX Generator.](https://cmake.org/cmake/help/latest/policy/CMP0172.html)
*   [CMP0171: 'codegen' is a reserved target name.](https://cmake.org/cmake/help/latest/policy/CMP0171.html)

### [Policies Introduced by CMake 3.30](https://cmake.org/cmake/help/latest/manual/cmake-policies.7.html#id11)[¶](https://cmake.org/cmake/help/latest/manual/cmake-policies.7.html#policies-introduced-by-cmake-3-30 "Link to this heading")

*   [CMP0170: FETCHCONTENT_FULLY_DISCONNECTED requirements are enforced.](https://cmake.org/cmake/help/latest/policy/CMP0170.html)
*   [CMP0169: FetchContent_Populate(depName) single-argument signature is deprecated.](https://cmake.org/cmake/help/latest/policy/CMP0169.html)
*   [CMP0168: FetchContent implements steps directly instead of through a sub-build.](https://cmake.org/cmake/help/latest/policy/CMP0168.html)
*   [CMP0167: The FindBoost module is removed.](https://cmake.org/cmake/help/latest/policy/CMP0167.html)
*   [CMP0166: TARGET_PROPERTY evaluates link properties transitively over private dependencies of static libraries.](https://cmake.org/cmake/help/latest/policy/CMP0166.html)
*   [CMP0165: enable_language() must not be called before project().](https://cmake.org/cmake/help/latest/policy/CMP0165.html)
*   [CMP0164: add_library() rejects SHARED libraries when not supported by the platform.](https://cmake.org/cmake/help/latest/policy/CMP0164.html)
*   [CMP0163: The GENERATED source file property is now visible in all directories.](https://cmake.org/cmake/help/latest/policy/CMP0163.html)
*   [CMP0162: Visual Studio generators add UseDebugLibraries indicators by default.](https://cmake.org/cmake/help/latest/policy/CMP0162.html)

### [Policies Introduced by CMake 3.29](https://cmake.org/cmake/help/latest/manual/cmake-policies.7.html#id12)[¶](https://cmake.org/cmake/help/latest/manual/cmake-policies.7.html#policies-introduced-by-cmake-3-29 "Link to this heading")

*   [CMP0161: CPACK_PRODUCTBUILD_DOMAINS defaults to true.](https://cmake.org/cmake/help/latest/policy/CMP0161.html)
*   [CMP0160: More read-only target properties now error when trying to set them.](https://cmake.org/cmake/help/latest/policy/CMP0160.html)
*   [CMP0159: file(STRINGS) with REGEX updates CMAKE_MATCH_<n>.](https://cmake.org/cmake/help/latest/policy/CMP0159.html)
*   [CMP0158: add_test() honors CMAKE_CROSSCOMPILING_EMULATOR only when cross-compiling.](https://cmake.org/cmake/help/latest/policy/CMP0158.html)
*   [CMP0157: Swift compilation mode is selected by an abstraction.](https://cmake.org/cmake/help/latest/policy/CMP0157.html)
*   [CMP0156: De-duplicate libraries on link lines based on linker capabilities.](https://cmake.org/cmake/help/latest/policy/CMP0156.html)

### [Policies Introduced by CMake 3.28](https://cmake.org/cmake/help/latest/manual/cmake-policies.7.html#id13)[¶](https://cmake.org/cmake/help/latest/manual/cmake-policies.7.html#policies-introduced-by-cmake-3-28 "Link to this heading")

*   [CMP0155: C++ sources in targets with at least C++20 are scanned for imports when supported.](https://cmake.org/cmake/help/latest/policy/CMP0155.html)
*   [CMP0154: Generated files are private by default in targets using file sets.](https://cmake.org/cmake/help/latest/policy/CMP0154.html)
*   [CMP0153: The exec_program command should not be called.](https://cmake.org/cmake/help/latest/policy/CMP0153.html)
*   [CMP0152: file(REAL_PATH) resolves symlinks before collapsing ../ components.](https://cmake.org/cmake/help/latest/policy/CMP0152.html)

### [Policies Introduced by CMake 3.27](https://cmake.org/cmake/help/latest/manual/cmake-policies.7.html#id14)[¶](https://cmake.org/cmake/help/latest/manual/cmake-policies.7.html#policies-introduced-by-cmake-3-27 "Link to this heading")

*   [CMP0151: AUTOMOC include directory is a system include directory by default.](https://cmake.org/cmake/help/latest/policy/CMP0151.html)
*   [CMP0150: ExternalProject_Add and FetchContent_Declare treat relative git repository paths as being relative to parent project's remote.](https://cmake.org/cmake/help/latest/policy/CMP0150.html)
*   [CMP0149: Visual Studio generators select latest Windows SDK by default.](https://cmake.org/cmake/help/latest/policy/CMP0149.html)
*   [CMP0148: The FindPythonInterp and FindPythonLibs modules are removed.](https://cmake.org/cmake/help/latest/policy/CMP0148.html)
*   [CMP0147: Visual Studio generators build custom commands in parallel.](https://cmake.org/cmake/help/latest/policy/CMP0147.html)
*   [CMP0146: The FindCUDA module is removed.](https://cmake.org/cmake/help/latest/policy/CMP0146.html)
*   [CMP0145: The Dart and FindDart modules are removed.](https://cmake.org/cmake/help/latest/policy/CMP0145.html)
*   [CMP0144: find_package uses upper-case PACKAGENAME_ROOT variables.](https://cmake.org/cmake/help/latest/policy/CMP0144.html)

### [Policies Introduced by CMake 3.26](https://cmake.org/cmake/help/latest/manual/cmake-policies.7.html#id15)[¶](https://cmake.org/cmake/help/latest/manual/cmake-policies.7.html#policies-introduced-by-cmake-3-26 "Link to this heading")

*   [CMP0143: USE_FOLDERS global property is treated as ON by default.](https://cmake.org/cmake/help/latest/policy/CMP0143.html)

### [Policies Introduced by CMake 3.25](https://cmake.org/cmake/help/latest/manual/cmake-policies.7.html#id16)[¶](https://cmake.org/cmake/help/latest/manual/cmake-policies.7.html#policies-introduced-by-cmake-3-25 "Link to this heading")

*   [CMP0142: The Xcode generator does not append per-config suffixes to library search paths.](https://cmake.org/cmake/help/latest/policy/CMP0142.html)
*   [CMP0141: MSVC debug information format flags are selected by an abstraction.](https://cmake.org/cmake/help/latest/policy/CMP0141.html)
*   [CMP0140: The return() command checks its arguments.](https://cmake.org/cmake/help/latest/policy/CMP0140.html)

### [Policies Introduced by CMake 3.24](https://cmake.org/cmake/help/latest/manual/cmake-policies.7.html#id17)[¶](https://cmake.org/cmake/help/latest/manual/cmake-policies.7.html#policies-introduced-by-cmake-3-24 "Link to this heading")

*   [CMP0139: The if() command supports path comparisons using PATH_EQUAL operator.](https://cmake.org/cmake/help/latest/policy/CMP0139.html)
*   [CMP0138: CheckIPOSupported uses flags from calling project.](https://cmake.org/cmake/help/latest/policy/CMP0138.html)
*   [CMP0137: try_compile() passes platform variables in project mode.](https://cmake.org/cmake/help/latest/policy/CMP0137.html)
*   [CMP0136: Watcom runtime library flags are selected by an abstraction.](https://cmake.org/cmake/help/latest/policy/CMP0136.html)
*   [CMP0135: ExternalProject and FetchContent ignore timestamps in archives by default for the URL download method.](https://cmake.org/cmake/help/latest/policy/CMP0135.html)
*   [CMP0134: Fallback to "HOST" Windows registry view when "TARGET" view is not usable.](https://cmake.org/cmake/help/latest/policy/CMP0134.html)
*   [CMP0133: The CPack module disables SLA by default in the CPack DragNDrop Generator.](https://cmake.org/cmake/help/latest/policy/CMP0133.html)
*   [CMP0132: Do not set compiler environment variables on first run.](https://cmake.org/cmake/help/latest/policy/CMP0132.html)
*   [CMP0131: LINK_LIBRARIES supports the LINK_ONLY generator expression.](https://cmake.org/cmake/help/latest/policy/CMP0131.html)
*   [CMP0130: while() diagnoses condition evaluation errors.](https://cmake.org/cmake/help/latest/policy/CMP0130.html)

### [Policies Introduced by CMake 3.23](https://cmake.org/cmake/help/latest/manual/cmake-policies.7.html#id18)[¶](https://cmake.org/cmake/help/latest/manual/cmake-policies.7.html#policies-introduced-by-cmake-3-23 "Link to this heading")

*   [CMP0129: Compiler id for MCST LCC compilers is now LCC, not GNU.](https://cmake.org/cmake/help/latest/policy/CMP0129.html)

### [Policies Introduced by CMake 3.22](https://cmake.org/cmake/help/latest/manual/cmake-policies.7.html#id19)[¶](https://cmake.org/cmake/help/latest/manual/cmake-policies.7.html#policies-introduced-by-cmake-3-22 "Link to this heading")

*   [CMP0128: Selection of language standard and extension flags improved.](https://cmake.org/cmake/help/latest/policy/CMP0128.html)
*   [CMP0127: cmake_dependent_option() supports full Condition Syntax.](https://cmake.org/cmake/help/latest/policy/CMP0127.html)

### [Policies Introduced by CMake 3.21](https://cmake.org/cmake/help/latest/manual/cmake-policies.7.html#id20)[¶](https://cmake.org/cmake/help/latest/manual/cmake-policies.7.html#policies-introduced-by-cmake-3-21 "Link to this heading")

*   [CMP0126: set(CACHE) does not remove a normal variable of the same name.](https://cmake.org/cmake/help/latest/policy/CMP0126.html)
*   [CMP0125: find_(path|file|library|program) have consistent behavior for cache variables.](https://cmake.org/cmake/help/latest/policy/CMP0125.html)
*   [CMP0124: foreach() loop variables are only available in the loop scope.](https://cmake.org/cmake/help/latest/policy/CMP0124.html)
*   [CMP0123: ARMClang cpu/arch compile and link flags must be set explicitly.](https://cmake.org/cmake/help/latest/policy/CMP0123.html)
*   [CMP0122: UseSWIG use standard library name conventions for csharp language.](https://cmake.org/cmake/help/latest/policy/CMP0122.html)
*   [CMP0121: The list command detects invalid indices.](https://cmake.org/cmake/help/latest/policy/CMP0121.html)

### [Policies Introduced by CMake 3.20](https://cmake.org/cmake/help/latest/manual/cmake-policies.7.html#id21)[¶](https://cmake.org/cmake/help/latest/manual/cmake-policies.7.html#policies-introduced-by-cmake-3-20 "Link to this heading")

*   [CMP0120: The WriteCompilerDetectionHeader module is removed.](https://cmake.org/cmake/help/latest/policy/CMP0120.html)
*   [CMP0119: LANGUAGE source file property explicitly compiles as language.](https://cmake.org/cmake/help/latest/policy/CMP0119.html)
*   [CMP0118: GENERATED sources may be used across directories without manual marking.](https://cmake.org/cmake/help/latest/policy/CMP0118.html)
*   [CMP0117: MSVC RTTI flag /GR is not added to CMAKE_CXX_FLAGS by default.](https://cmake.org/cmake/help/latest/policy/CMP0117.html)
*   [CMP0116: Ninja generators transform DEPFILEs from add_custom_command().](https://cmake.org/cmake/help/latest/policy/CMP0116.html)
*   [CMP0115: Source file extensions must be explicit.](https://cmake.org/cmake/help/latest/policy/CMP0115.html)

### [Policies Introduced by CMake 3.19](https://cmake.org/cmake/help/latest/manual/cmake-policies.7.html#id22)[¶](https://cmake.org/cmake/help/latest/manual/cmake-policies.7.html#policies-introduced-by-cmake-3-19 "Link to this heading")

*   [CMP0114: ExternalProject step targets fully adopt their steps.](https://cmake.org/cmake/help/latest/policy/CMP0114.html)
*   [CMP0113: Makefile generators do not repeat custom commands from target dependencies.](https://cmake.org/cmake/help/latest/policy/CMP0113.html)
*   [CMP0112: Target file component generator expressions do not add target dependencies.](https://cmake.org/cmake/help/latest/policy/CMP0112.html)
*   [CMP0111: An imported target missing its location property fails during generation.](https://cmake.org/cmake/help/latest/policy/CMP0111.html)
*   [CMP0110: add_test() supports arbitrary characters in test names.](https://cmake.org/cmake/help/latest/policy/CMP0110.html)
*   [CMP0109: find_program() requires permission to execute but not to read.](https://cmake.org/cmake/help/latest/policy/CMP0109.html)

### [Policies Introduced by CMake 3.18](https://cmake.org/cmake/help/latest/manual/cmake-policies.7.html#id23)[¶](https://cmake.org/cmake/help/latest/manual/cmake-policies.7.html#policies-introduced-by-cmake-3-18 "Link to this heading")

*   [CMP0108: A target cannot link to itself through an alias.](https://cmake.org/cmake/help/latest/policy/CMP0108.html)
*   [CMP0107: An ALIAS target cannot overwrite another target.](https://cmake.org/cmake/help/latest/policy/CMP0107.html)
*   [CMP0106: The Documentation module is removed.](https://cmake.org/cmake/help/latest/policy/CMP0106.html)
*   [CMP0105: Device link step uses the link options.](https://cmake.org/cmake/help/latest/policy/CMP0105.html)
*   [CMP0104: CMAKE_CUDA_ARCHITECTURES now detected for NVCC, empty CUDA_ARCHITECTURES not allowed.](https://cmake.org/cmake/help/latest/policy/CMP0104.html)
*   [CMP0103: Multiple export() with same FILE without APPEND is not allowed.](https://cmake.org/cmake/help/latest/policy/CMP0103.html)

### [Policies Introduced by CMake 3.17](https://cmake.org/cmake/help/latest/manual/cmake-policies.7.html#id24)[¶](https://cmake.org/cmake/help/latest/manual/cmake-policies.7.html#policies-introduced-by-cmake-3-17 "Link to this heading")

*   [CMP0102: mark_as_advanced() does nothing if a cache entry does not exist.](https://cmake.org/cmake/help/latest/policy/CMP0102.html)
*   [CMP0101: target_compile_options honors BEFORE keyword in all scopes.](https://cmake.org/cmake/help/latest/policy/CMP0101.html)
*   [CMP0100: Let AUTOMOC and AUTOUIC process .hh header files.](https://cmake.org/cmake/help/latest/policy/CMP0100.html)
*   [CMP0099: Link properties are transitive over private dependencies of static libraries.](https://cmake.org/cmake/help/latest/policy/CMP0099.html)
*   [CMP0098: FindFLEX runs flex in CMAKE_CURRENT_BINARY_DIR when executing.](https://cmake.org/cmake/help/latest/policy/CMP0098.html)

### [Policies Introduced by CMake 3.16](https://cmake.org/cmake/help/latest/manual/cmake-policies.7.html#id25)[¶](https://cmake.org/cmake/help/latest/manual/cmake-policies.7.html#policies-introduced-by-cmake-3-16 "Link to this heading")

*   [CMP0097: ExternalProject_Add with GIT_SUBMODULES "" initializes no submodules.](https://cmake.org/cmake/help/latest/policy/CMP0097.html)
*   [CMP0096: project() preserves leading zeros in version components.](https://cmake.org/cmake/help/latest/policy/CMP0096.html)
*   [CMP0095: RPATH entries are properly escaped in the intermediary CMake install script.](https://cmake.org/cmake/help/latest/policy/CMP0095.html)

### [Policies Introduced by CMake 3.15](https://cmake.org/cmake/help/latest/manual/cmake-policies.7.html#id26)[¶](https://cmake.org/cmake/help/latest/manual/cmake-policies.7.html#policies-introduced-by-cmake-3-15 "Link to this heading")

*   [CMP0094: FindPython3, FindPython2 and FindPython use LOCATION for lookup strategy.](https://cmake.org/cmake/help/latest/policy/CMP0094.html)
*   [CMP0093: FindBoost reports Boost_VERSION in x.y.z format.](https://cmake.org/cmake/help/latest/policy/CMP0093.html)
*   [CMP0092: MSVC warning flags are not in CMAKE_{C,CXX}_FLAGS by default.](https://cmake.org/cmake/help/latest/policy/CMP0092.html)
*   [CMP0091: MSVC runtime library flags are selected by an abstraction.](https://cmake.org/cmake/help/latest/policy/CMP0091.html)
*   [CMP0090: export(PACKAGE) does not populate package registry by default.](https://cmake.org/cmake/help/latest/policy/CMP0090.html)
*   [CMP0089: Compiler id for IBM Clang-based XL compilers is now XLClang.](https://cmake.org/cmake/help/latest/policy/CMP0089.html)

### [Policies Introduced by CMake 3.14](https://cmake.org/cmake/help/latest/manual/cmake-policies.7.html#id27)[¶](https://cmake.org/cmake/help/latest/manual/cmake-policies.7.html#policies-introduced-by-cmake-3-14 "Link to this heading")

*   [CMP0088: FindBISON runs bison in CMAKE_CURRENT_BINARY_DIR when executing.](https://cmake.org/cmake/help/latest/policy/CMP0088.html)
*   [CMP0087: install(SCRIPT | CODE) supports generator expressions.](https://cmake.org/cmake/help/latest/policy/CMP0087.html)
*   [CMP0086: UseSWIG honors SWIG_MODULE_NAME via -module flag.](https://cmake.org/cmake/help/latest/policy/CMP0086.html)
*   [CMP0085: IN_LIST generator expression handles empty list items.](https://cmake.org/cmake/help/latest/policy/CMP0085.html)
*   [CMP0084: The FindQt module does not exist for find_package().](https://cmake.org/cmake/help/latest/policy/CMP0084.html)
*   [CMP0083: Add PIE options when linking executable.](https://cmake.org/cmake/help/latest/policy/CMP0083.html)
*   [CMP0082: Install rules from add_subdirectory() are interleaved with those in caller.](https://cmake.org/cmake/help/latest/policy/CMP0082.html)

### [Policies Introduced by CMake 3.13](https://cmake.org/cmake/help/latest/manual/cmake-policies.7.html#id28)[¶](https://cmake.org/cmake/help/latest/manual/cmake-policies.7.html#policies-introduced-by-cmake-3-13 "Link to this heading")

*   [CMP0081: Relative paths not allowed in LINK_DIRECTORIES target property.](https://cmake.org/cmake/help/latest/policy/CMP0081.html)
*   [CMP0080: BundleUtilities cannot be included at configure time.](https://cmake.org/cmake/help/latest/policy/CMP0080.html)
*   [CMP0079: target_link_libraries allows use with targets in other directories.](https://cmake.org/cmake/help/latest/policy/CMP0079.html)
*   [CMP0078: UseSWIG generates standard target names.](https://cmake.org/cmake/help/latest/policy/CMP0078.html)
*   [CMP0077: option() honors normal variables.](https://cmake.org/cmake/help/latest/policy/CMP0077.html)
*   [CMP0076: target_sources() command converts relative paths to absolute.](https://cmake.org/cmake/help/latest/policy/CMP0076.html)

### [Policies Introduced by CMake 3.12](https://cmake.org/cmake/help/latest/manual/cmake-policies.7.html#id29)[¶](https://cmake.org/cmake/help/latest/manual/cmake-policies.7.html#policies-introduced-by-cmake-3-12 "Link to this heading")

*   [CMP0075: Include file check macros honor CMAKE_REQUIRED_LIBRARIES.](https://cmake.org/cmake/help/latest/policy/CMP0075.html)
*   [CMP0074: find_package uses PackageName_ROOT variables.](https://cmake.org/cmake/help/latest/policy/CMP0074.html)
*   [CMP0073: Do not produce legacy _LIB_DEPENDS cache entries.](https://cmake.org/cmake/help/latest/policy/CMP0073.html)

### [Policies Introduced by CMake 3.11](https://cmake.org/cmake/help/latest/manual/cmake-policies.7.html#id30)[¶](https://cmake.org/cmake/help/latest/manual/cmake-policies.7.html#policies-introduced-by-cmake-3-11 "Link to this heading")

*   [CMP0072: FindOpenGL prefers GLVND by default when available.](https://cmake.org/cmake/help/latest/policy/CMP0072.html)

### [Policies Introduced by CMake 3.10](https://cmake.org/cmake/help/latest/manual/cmake-policies.7.html#id31)[¶](https://cmake.org/cmake/help/latest/manual/cmake-policies.7.html#policies-introduced-by-cmake-3-10 "Link to this heading")

*   [CMP0071: Let AUTOMOC and AUTOUIC process GENERATED files.](https://cmake.org/cmake/help/latest/policy/CMP0071.html)
*   [CMP0070: Define file(GENERATE) behavior for relative paths.](https://cmake.org/cmake/help/latest/policy/CMP0070.html)

### [Policies Introduced by CMake 3.9](https://cmake.org/cmake/help/latest/manual/cmake-policies.7.html#id32)[¶](https://cmake.org/cmake/help/latest/manual/cmake-policies.7.html#policies-introduced-by-cmake-3-9 "Link to this heading")

*   [CMP0069: INTERPROCEDURAL_OPTIMIZATION is enforced when enabled.](https://cmake.org/cmake/help/latest/policy/CMP0069.html)
*   [CMP0068: RPATH settings on macOS do not affect install_name.](https://cmake.org/cmake/help/latest/policy/CMP0068.html)

### [Policies Introduced by CMake 3.8](https://cmake.org/cmake/help/latest/manual/cmake-policies.7.html#id33)[¶](https://cmake.org/cmake/help/latest/manual/cmake-policies.7.html#policies-introduced-by-cmake-3-8 "Link to this heading")

*   [CMP0067: Honor language standard in try_compile() source-file signature.](https://cmake.org/cmake/help/latest/policy/CMP0067.html)

### [Policies Introduced by CMake 3.7](https://cmake.org/cmake/help/latest/manual/cmake-policies.7.html#id34)[¶](https://cmake.org/cmake/help/latest/manual/cmake-policies.7.html#policies-introduced-by-cmake-3-7 "Link to this heading")

*   [CMP0066: Honor per-config flags in try_compile() source-file signature.](https://cmake.org/cmake/help/latest/policy/CMP0066.html)

[Unsupported Policies](https://cmake.org/cmake/help/latest/manual/cmake-policies.7.html#id35)[¶](https://cmake.org/cmake/help/latest/manual/cmake-policies.7.html#unsupported-policies "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The following policies are no longer supported. Projects' calls to [`cmake_minimum_required(VERSION)`](https://cmake.org/cmake/help/latest/command/cmake_minimum_required.html#command:cmake_minimum_required "cmake_minimum_required(version)") or [`cmake_policy(VERSION)`](https://cmake.org/cmake/help/latest/command/cmake_policy.html#version "cmake_policy(version)") must set them to `NEW`. Their `OLD` behaviors have been removed from CMake.

### [Policies Introduced by CMake 3.4, Removed by CMake 4.0](https://cmake.org/cmake/help/latest/manual/cmake-policies.7.html#id36)[¶](https://cmake.org/cmake/help/latest/manual/cmake-policies.7.html#policies-introduced-by-cmake-3-4-removed-by-cmake-4-0 "Link to this heading")

*   [CMP0065: Do not add flags to export symbols from executables without the ENABLE_EXPORTS target property.](https://cmake.org/cmake/help/latest/policy/CMP0065.html)
*   [CMP0064: Support new TEST if() operator.](https://cmake.org/cmake/help/latest/policy/CMP0064.html)

### [Policies Introduced by CMake 3.3, Removed by CMake 4.0](https://cmake.org/cmake/help/latest/manual/cmake-policies.7.html#id37)[¶](https://cmake.org/cmake/help/latest/manual/cmake-policies.7.html#policies-introduced-by-cmake-3-3-removed-by-cmake-4-0 "Link to this heading")

*   [CMP0063: Honor visibility properties for all target types.](https://cmake.org/cmake/help/latest/policy/CMP0063.html)
*   [CMP0062: Disallow install() of export() result.](https://cmake.org/cmake/help/latest/policy/CMP0062.html)
*   [CMP0061: CTest does not by default tell make to ignore errors (-i).](https://cmake.org/cmake/help/latest/policy/CMP0061.html)
*   [CMP0060: Link libraries by full path even in implicit directories.](https://cmake.org/cmake/help/latest/policy/CMP0060.html)
*   [CMP0059: Do not treat DEFINITIONS as a built-in directory property.](https://cmake.org/cmake/help/latest/policy/CMP0059.html)
*   [CMP0058: Ninja requires custom command byproducts to be explicit.](https://cmake.org/cmake/help/latest/policy/CMP0058.html)
*   [CMP0057: Support new IN_LIST if() operator.](https://cmake.org/cmake/help/latest/policy/CMP0057.html)

### [Policies Introduced by CMake 3.2, Removed by CMake 4.0](https://cmake.org/cmake/help/latest/manual/cmake-policies.7.html#id38)[¶](https://cmake.org/cmake/help/latest/manual/cmake-policies.7.html#policies-introduced-by-cmake-3-2-removed-by-cmake-4-0 "Link to this heading")

*   [CMP0056: Honor link flags in try_compile() source-file signature.](https://cmake.org/cmake/help/latest/policy/CMP0056.html)
*   [CMP0055: Strict checking for break() command.](https://cmake.org/cmake/help/latest/policy/CMP0055.html)

### [Policies Introduced by CMake 3.1, Removed by CMake 4.0](https://cmake.org/cmake/help/latest/manual/cmake-policies.7.html#id39)[¶](https://cmake.org/cmake/help/latest/manual/cmake-policies.7.html#policies-introduced-by-cmake-3-1-removed-by-cmake-4-0 "Link to this heading")

*   [CMP0054: Only interpret if() arguments as variables or keywords when unquoted.](https://cmake.org/cmake/help/latest/policy/CMP0054.html)
*   [CMP0053: Simplify variable reference and escape sequence evaluation.](https://cmake.org/cmake/help/latest/policy/CMP0053.html)
*   [CMP0052: Reject source and build dirs in installed INTERFACE_INCLUDE_DIRECTORIES.](https://cmake.org/cmake/help/latest/policy/CMP0052.html)
*   [CMP0051: List TARGET_OBJECTS in SOURCES target property.](https://cmake.org/cmake/help/latest/policy/CMP0051.html)

### [Policies Introduced by CMake 3.0, Removed by CMake 4.0](https://cmake.org/cmake/help/latest/manual/cmake-policies.7.html#id40)[¶](https://cmake.org/cmake/help/latest/manual/cmake-policies.7.html#policies-introduced-by-cmake-3-0-removed-by-cmake-4-0 "Link to this heading")

*   [CMP0050: Disallow add_custom_command SOURCE signatures.](https://cmake.org/cmake/help/latest/policy/CMP0050.html)
*   [CMP0049: Do not expand variables in target source entries.](https://cmake.org/cmake/help/latest/policy/CMP0049.html)
*   [CMP0048: project() command manages VERSION variables.](https://cmake.org/cmake/help/latest/policy/CMP0048.html)
*   [CMP0047: Use QCC compiler id for the qcc drivers on QNX.](https://cmake.org/cmake/help/latest/policy/CMP0047.html)
*   [CMP0046: Error on non-existent dependency in add_dependencies.](https://cmake.org/cmake/help/latest/policy/CMP0046.html)
*   [CMP0045: Error on non-existent target in get_target_property.](https://cmake.org/cmake/help/latest/policy/CMP0045.html)
*   [CMP0044: Case sensitive Lang_COMPILER_ID generator expressions.](https://cmake.org/cmake/help/latest/policy/CMP0044.html)
*   [CMP0043: Ignore COMPILE_DEFINITIONS_Config properties.](https://cmake.org/cmake/help/latest/policy/CMP0043.html)
*   [CMP0042: MACOSX_RPATH is enabled by default.](https://cmake.org/cmake/help/latest/policy/CMP0042.html)
*   [CMP0041: Error on relative include with generator expression.](https://cmake.org/cmake/help/latest/policy/CMP0041.html)
*   [CMP0040: The target in the TARGET signature of add_custom_command() must exist.](https://cmake.org/cmake/help/latest/policy/CMP0040.html)
*   [CMP0039: Utility targets may not have link dependencies.](https://cmake.org/cmake/help/latest/policy/CMP0039.html)
*   [CMP0038: Targets may not link directly to themselves.](https://cmake.org/cmake/help/latest/policy/CMP0038.html)
*   [CMP0037: Target names should not be reserved and should match a validity pattern.](https://cmake.org/cmake/help/latest/policy/CMP0037.html)
*   [CMP0036: The build_name command should not be called.](https://cmake.org/cmake/help/latest/policy/CMP0036.html)
*   [CMP0035: The variable_requires command should not be called.](https://cmake.org/cmake/help/latest/policy/CMP0035.html)
*   [CMP0034: The utility_source command should not be called.](https://cmake.org/cmake/help/latest/policy/CMP0034.html)
*   [CMP0033: The export_library_dependencies command should not be called.](https://cmake.org/cmake/help/latest/policy/CMP0033.html)
*   [CMP0032: The output_required_files command should not be called.](https://cmake.org/cmake/help/latest/policy/CMP0032.html)
*   [CMP0031: The load_command command should not be called.](https://cmake.org/cmake/help/latest/policy/CMP0031.html)
*   [CMP0030: The use_mangled_mesa command should not be called.](https://cmake.org/cmake/help/latest/policy/CMP0030.html)
*   [CMP0029: The subdir_depends command should not be called.](https://cmake.org/cmake/help/latest/policy/CMP0029.html)
*   [CMP0028: Double colon in target name means ALIAS or IMPORTED target.](https://cmake.org/cmake/help/latest/policy/CMP0028.html)
*   [CMP0027: Conditionally linked imported targets with missing include directories.](https://cmake.org/cmake/help/latest/policy/CMP0027.html)
*   [CMP0026: Disallow use of the LOCATION target property.](https://cmake.org/cmake/help/latest/policy/CMP0026.html)
*   [CMP0025: Compiler id for Apple Clang is now AppleClang.](https://cmake.org/cmake/help/latest/policy/CMP0025.html)
*   [CMP0024: Disallow include export result.](https://cmake.org/cmake/help/latest/policy/CMP0024.html)

### [Policies Introduced by CMake 2.8, Removed by CMake 4.0](https://cmake.org/cmake/help/latest/manual/cmake-policies.7.html#id41)[¶](https://cmake.org/cmake/help/latest/manual/cmake-policies.7.html#policies-introduced-by-cmake-2-8-removed-by-cmake-4-0 "Link to this heading")

*   [CMP0023: Plain and keyword target_link_libraries signatures cannot be mixed.](https://cmake.org/cmake/help/latest/policy/CMP0023.html)
*   [CMP0022: INTERFACE_LINK_LIBRARIES defines the link interface.](https://cmake.org/cmake/help/latest/policy/CMP0022.html)
*   [CMP0021: Fatal error on relative paths in INCLUDE_DIRECTORIES target property.](https://cmake.org/cmake/help/latest/policy/CMP0021.html)
*   [CMP0020: Automatically link Qt executables to qtmain target on Windows.](https://cmake.org/cmake/help/latest/policy/CMP0020.html)
*   [CMP0019: Do not re-expand variables in include and link information.](https://cmake.org/cmake/help/latest/policy/CMP0019.html)
*   [CMP0018: Ignore CMAKE_SHARED_LIBRARY_Lang_FLAGS variable.](https://cmake.org/cmake/help/latest/policy/CMP0018.html)
*   [CMP0017: Prefer files from the CMake module directory when including from there.](https://cmake.org/cmake/help/latest/policy/CMP0017.html)
*   [CMP0016: target_link_libraries() reports error if its only argument is not a target.](https://cmake.org/cmake/help/latest/policy/CMP0016.html)
*   [CMP0015: link_directories() treats paths relative to the source dir.](https://cmake.org/cmake/help/latest/policy/CMP0015.html)
*   [CMP0014: Input directories must have CMakeLists.txt.](https://cmake.org/cmake/help/latest/policy/CMP0014.html)
*   [CMP0013: Duplicate binary directories are not allowed.](https://cmake.org/cmake/help/latest/policy/CMP0013.html)
*   [CMP0012: if() recognizes numbers and boolean constants.](https://cmake.org/cmake/help/latest/policy/CMP0012.html)

### [Policies Introduced by CMake 2.6, Removed by CMake 4.0](https://cmake.org/cmake/help/latest/manual/cmake-policies.7.html#id42)[¶](https://cmake.org/cmake/help/latest/manual/cmake-policies.7.html#policies-introduced-by-cmake-2-6-removed-by-cmake-4-0 "Link to this heading")

*   [CMP0011: Included scripts do automatic cmake_policy PUSH and POP.](https://cmake.org/cmake/help/latest/policy/CMP0011.html)
*   [CMP0010: Bad variable reference syntax is an error.](https://cmake.org/cmake/help/latest/policy/CMP0010.html)
*   [CMP0009: FILE GLOB_RECURSE calls should not follow symlinks by default.](https://cmake.org/cmake/help/latest/policy/CMP0009.html)
*   [CMP0008: Libraries linked by full-path must have a valid library file name.](https://cmake.org/cmake/help/latest/policy/CMP0008.html)
*   [CMP0007: list command no longer ignores empty elements.](https://cmake.org/cmake/help/latest/policy/CMP0007.html)
*   [CMP0006: Installing MACOSX_BUNDLE targets requires a BUNDLE DESTINATION.](https://cmake.org/cmake/help/latest/policy/CMP0006.html)
*   [CMP0005: Preprocessor definition values are now escaped automatically.](https://cmake.org/cmake/help/latest/policy/CMP0005.html)
*   [CMP0004: Libraries linked may not have leading or trailing whitespace.](https://cmake.org/cmake/help/latest/policy/CMP0004.html)
*   [CMP0003: Libraries linked via full path no longer produce linker search paths.](https://cmake.org/cmake/help/latest/policy/CMP0003.html)
*   [CMP0002: Logical target names must be globally unique.](https://cmake.org/cmake/help/latest/policy/CMP0002.html)
*   [CMP0001: CMAKE_BACKWARDS_COMPATIBILITY should no longer be used.](https://cmake.org/cmake/help/latest/policy/CMP0001.html)
*   [CMP0000: A minimum required CMake version must be specified.](https://cmake.org/cmake/help/latest/policy/CMP0000.html)
