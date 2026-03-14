# Source: https://scons.org/doc/latest/HTML/scons-api/index.html

Title: SCons API Documentation — SCons 4.10.1 documentation

URL Source: https://scons.org/doc/latest/HTML/scons-api/index.html

Markdown Content:
SCons API Documentation — SCons 4.10.1 documentation
===============

[Skip to main content](https://scons.org/doc/latest/HTML/scons-api/index.html#main-content)

Back to top- [x] - [x]

Ctrl+K

[SCons 4.10.1 documentation](https://scons.org/doc/latest/HTML/scons-api/index.html#)

Search Ctrl+K

Contents:

* [SCons package](https://scons.org/doc/latest/HTML/scons-api/SCons/)
* [SCons.compat package](https://scons.org/doc/latest/HTML/scons-api/SCons.compat/)
* [SCons.Node package](https://scons.org/doc/latest/HTML/scons-api/SCons.Node/)
* [SCons.Platform package](https://scons.org/doc/latest/HTML/scons-api/SCons.Platform/)
* [SCons.Scanner package](https://scons.org/doc/latest/HTML/scons-api/SCons.Scanner/)
* [SCons.Script package](https://scons.org/doc/latest/HTML/scons-api/SCons.Script/)
* [SCons.Taskmaster package](https://scons.org/doc/latest/HTML/scons-api/SCons.Taskmaster/)
* [SCons.Tool package](https://scons.org/doc/latest/HTML/scons-api/SCons.Tool/)
* [SCons.Util package](https://scons.org/doc/latest/HTML/scons-api/SCons.Util/)
* [SCons.Variables package](https://scons.org/doc/latest/HTML/scons-api/SCons.Variables/)

* [.rst](https://scons.org/doc/latest/HTML/scons-api/_sources/index.rst "Download source file")
* .pdf

SCons API Documentation
=======================

Contents
--------

* [SCons API Documentation](https://scons.org/doc/latest/HTML/scons-api/index.html#)
* [Indices and Tables](https://scons.org/doc/latest/HTML/scons-api/index.html#indices-and-tables)

SCons API Documentation[#](https://scons.org/doc/latest/HTML/scons-api/index.html#scons-api-documentation "Link to this heading")
=================================================================================================================================

Attention

This is the **internal** API Documentation for SCons. It is generated automatically from code docstrings using the [Sphinx](https://www.sphinx-doc.org/) documentation generator, and covers much more than the Public API. If you were looking for the Public API - the interfaces that have long-term consistency guarantees, which you can reliably use when writing a build system for a project - see the [SCons Reference Manual](https://scons.org/doc/production/HTML/scons-man.html). Note that what is Public API and what is not is often not clearly delineated in these API Docs.

The target audience is developers contributing to SCons itself, and those writing external Tools, Builders, and other related functionality for their project, who may need to reach beyond the Public API to accomplish their tasks. Reaching into internals is fine, but comes with the usual risks of “things here could change, it’s up to you to keep your code working”.

Any missing/incomplete information is due to shortcomings in the docstrings in the code. Without being flippant, filling in all the docstrings has not always been a priority across the two-plus decades SCons has been in existence. Contributions improving the docstring front are welcome. It is often useful when making some larger change to fill in docstrings and suitable type annotations in the code being modified, “leaving the world a better place”, as it were.

Note that the Sphinx configuration is limited, still a work in progress. SCons classes which inherit from Python standard library classes (e.g. `UserList`, `UserDict`, `UserString`), may be allowed to show inherited mmembers; the Python standard library occasionally has little to no helpful docstring information. Inherited interfaces from outside SCons code can be identified by the lack of a `[source]` button to the right of the method signature. Such classes should be evaluated case-by-case and possibly switched to not show inherited members, depending on which way seems to provide the more useful result.

Contents:

* [SCons package](https://scons.org/doc/latest/HTML/scons-api/SCons/)
  * [Module contents](https://scons.org/doc/latest/HTML/scons-api/SCons/#module-SCons)
  * [Submodules](https://scons.org/doc/latest/HTML/scons-api/SCons/#submodules)
  * [SCons.Action module](https://scons.org/doc/latest/HTML/scons-api/SCons/#module-SCons.Action)
  * [SCons.Builder module](https://scons.org/doc/latest/HTML/scons-api/SCons/#module-SCons.Builder)
  * [SCons.CacheDir module](https://scons.org/doc/latest/HTML/scons-api/SCons/#module-SCons.CacheDir)
  * [SCons.Conftest module](https://scons.org/doc/latest/HTML/scons-api/SCons/#module-SCons.Conftest)
  * [SCons.Debug module](https://scons.org/doc/latest/HTML/scons-api/SCons/#module-SCons.Debug)
  * [SCons.Defaults module](https://scons.org/doc/latest/HTML/scons-api/SCons/#module-SCons.Defaults)
  * [SCons.Environment module](https://scons.org/doc/latest/HTML/scons-api/SCons/#module-SCons.Environment)
  * [SCons.Errors module](https://scons.org/doc/latest/HTML/scons-api/SCons/#scons-errors-module)
  * [SCons.Executor module](https://scons.org/doc/latest/HTML/scons-api/SCons/#module-SCons.Executor)
  * [SCons.Memoize module](https://scons.org/doc/latest/HTML/scons-api/SCons/#module-SCons.Memoize)
  * [SCons.PathList module](https://scons.org/doc/latest/HTML/scons-api/SCons/#module-SCons.PathList)
  * [SCons.SConf module](https://scons.org/doc/latest/HTML/scons-api/SCons/#module-SCons.SConf)
  * [SCons.SConsign module](https://scons.org/doc/latest/HTML/scons-api/SCons/#module-SCons.SConsign)
  * [SCons.Subst module](https://scons.org/doc/latest/HTML/scons-api/SCons/#module-SCons.Subst)
  * [SCons.Warnings module](https://scons.org/doc/latest/HTML/scons-api/SCons/#scons-warnings-module)
  * [SCons.cpp module](https://scons.org/doc/latest/HTML/scons-api/SCons/#module-SCons.cpp)
  * [SCons.dblite module](https://scons.org/doc/latest/HTML/scons-api/SCons/#module-SCons.dblite)
  * [SCons.exitfuncs module](https://scons.org/doc/latest/HTML/scons-api/SCons/#module-SCons.exitfuncs)
  * [SConsDoc documentation module](https://scons.org/doc/latest/HTML/scons-api/SCons/#sconsdoc-documentation-module)
  * [SConsExamples documentation module](https://scons.org/doc/latest/HTML/scons-api/SCons/#sconsexamples-documentation-module)

* [SCons.compat package](https://scons.org/doc/latest/HTML/scons-api/SCons.compat/)
  * [Module contents](https://scons.org/doc/latest/HTML/scons-api/SCons.compat/#module-SCons.compat)

* [SCons.Node package](https://scons.org/doc/latest/HTML/scons-api/SCons.Node/)
  * [Module contents](https://scons.org/doc/latest/HTML/scons-api/SCons.Node/#module-SCons.Node)
  * [Submodules](https://scons.org/doc/latest/HTML/scons-api/SCons.Node/#submodules)
  * [SCons.Node.Alias module](https://scons.org/doc/latest/HTML/scons-api/SCons.Node/#module-SCons.Node.Alias)
  * [SCons.Node.FS module](https://scons.org/doc/latest/HTML/scons-api/SCons.Node/#module-SCons.Node.FS)
  * [SCons.Node.Python module](https://scons.org/doc/latest/HTML/scons-api/SCons.Node/#module-SCons.Node.Python)

* [SCons.Platform package](https://scons.org/doc/latest/HTML/scons-api/SCons.Platform/)
  * [Module contents](https://scons.org/doc/latest/HTML/scons-api/SCons.Platform/#module-SCons.Platform)
  * [Submodules](https://scons.org/doc/latest/HTML/scons-api/SCons.Platform/#submodules)
  * [SCons.Platform.aix module](https://scons.org/doc/latest/HTML/scons-api/SCons.Platform/#module-SCons.Platform.aix)
  * [SCons.Platform.cygwin module](https://scons.org/doc/latest/HTML/scons-api/SCons.Platform/#module-SCons.Platform.cygwin)
  * [SCons.Platform.darwin module](https://scons.org/doc/latest/HTML/scons-api/SCons.Platform/#module-SCons.Platform.darwin)
  * [SCons.Platform.hpux module](https://scons.org/doc/latest/HTML/scons-api/SCons.Platform/#module-SCons.Platform.hpux)
  * [SCons.Platform.irix module](https://scons.org/doc/latest/HTML/scons-api/SCons.Platform/#module-SCons.Platform.irix)
  * [SCons.Platform.mingw module](https://scons.org/doc/latest/HTML/scons-api/SCons.Platform/#module-SCons.Platform.mingw)
  * [SCons.Platform.os2 module](https://scons.org/doc/latest/HTML/scons-api/SCons.Platform/#module-SCons.Platform.os2)
  * [SCons.Platform.posix module](https://scons.org/doc/latest/HTML/scons-api/SCons.Platform/#module-SCons.Platform.posix)
  * [SCons.Platform.sunos module](https://scons.org/doc/latest/HTML/scons-api/SCons.Platform/#module-SCons.Platform.sunos)
  * [SCons.Platform.virtualenv module](https://scons.org/doc/latest/HTML/scons-api/SCons.Platform/#module-SCons.Platform.virtualenv)
  * [SCons.Platform.win32 module](https://scons.org/doc/latest/HTML/scons-api/SCons.Platform/#module-SCons.Platform.win32)

* [SCons.Scanner package](https://scons.org/doc/latest/HTML/scons-api/SCons.Scanner/)
  * [Module contents](https://scons.org/doc/latest/HTML/scons-api/SCons.Scanner/#module-SCons.Scanner)
  * [Submodules](https://scons.org/doc/latest/HTML/scons-api/SCons.Scanner/#submodules)
  * [SCons.Scanner.C module](https://scons.org/doc/latest/HTML/scons-api/SCons.Scanner/#module-SCons.Scanner.C)
  * [SCons.Scanner.D module](https://scons.org/doc/latest/HTML/scons-api/SCons.Scanner/#module-SCons.Scanner.D)
  * [SCons.Scanner.Dir module](https://scons.org/doc/latest/HTML/scons-api/SCons.Scanner/#module-SCons.Scanner.Dir)
  * [SCons.Scanner.Fortran module](https://scons.org/doc/latest/HTML/scons-api/SCons.Scanner/#module-SCons.Scanner.Fortran)
  * [SCons.Scanner.IDL module](https://scons.org/doc/latest/HTML/scons-api/SCons.Scanner/#module-SCons.Scanner.IDL)
  * [SCons.Scanner.Java module](https://scons.org/doc/latest/HTML/scons-api/SCons.Scanner/#module-SCons.Scanner.Java)
  * [SCons.Scanner.LaTeX module](https://scons.org/doc/latest/HTML/scons-api/SCons.Scanner/#module-SCons.Scanner.LaTeX)
  * [SCons.Scanner.Prog module](https://scons.org/doc/latest/HTML/scons-api/SCons.Scanner/#module-SCons.Scanner.Prog)
  * [SCons.Scanner.RC module](https://scons.org/doc/latest/HTML/scons-api/SCons.Scanner/#module-SCons.Scanner.RC)
  * [SCons.Scanner.SWIG module](https://scons.org/doc/latest/HTML/scons-api/SCons.Scanner/#module-SCons.Scanner.SWIG)

* [SCons.Script package](https://scons.org/doc/latest/HTML/scons-api/SCons.Script/)
  * [Module contents](https://scons.org/doc/latest/HTML/scons-api/SCons.Script/#module-SCons.Script)
  * [Submodules](https://scons.org/doc/latest/HTML/scons-api/SCons.Script/#submodules)
  * [SCons.Script.Interactive module](https://scons.org/doc/latest/HTML/scons-api/SCons.Script/#module-SCons.Script.Interactive)
  * [SCons.Script.Main module](https://scons.org/doc/latest/HTML/scons-api/SCons.Script/#module-SCons.Script.Main)
  * [SCons.Script.SConsOptions module](https://scons.org/doc/latest/HTML/scons-api/SCons.Script/#module-SCons.Script.SConsOptions)
  * [SCons.Script.SConscript module](https://scons.org/doc/latest/HTML/scons-api/SCons.Script/#module-SCons.Script.SConscript)

* [SCons.Taskmaster package](https://scons.org/doc/latest/HTML/scons-api/SCons.Taskmaster/)
  * [Module contents](https://scons.org/doc/latest/HTML/scons-api/SCons.Taskmaster/#module-SCons.Taskmaster)
  * [Submodules](https://scons.org/doc/latest/HTML/scons-api/SCons.Taskmaster/#submodules)
  * [SCons.Taskmaster.Job module](https://scons.org/doc/latest/HTML/scons-api/SCons.Taskmaster/#module-SCons.Taskmaster.Job)

* [SCons.Tool package](https://scons.org/doc/latest/HTML/scons-api/SCons.Tool/)
  * [Module contents](https://scons.org/doc/latest/HTML/scons-api/SCons.Tool/#module-SCons.Tool)

* [SCons.Util package](https://scons.org/doc/latest/HTML/scons-api/SCons.Util/)
  * [Module contents](https://scons.org/doc/latest/HTML/scons-api/SCons.Util/#module-SCons.Util)
  * [Submodules](https://scons.org/doc/latest/HTML/scons-api/SCons.Util/#submodules)
  * [SCons.Util.envs module](https://scons.org/doc/latest/HTML/scons-api/SCons.Util/#module-SCons.Util.envs)
  * [SCons.Util.filelock module](https://scons.org/doc/latest/HTML/scons-api/SCons.Util/#module-SCons.Util.filelock)
  * [SCons.Util.hashes module](https://scons.org/doc/latest/HTML/scons-api/SCons.Util/#module-SCons.Util.hashes)
  * [SCons.Util.sctypes module](https://scons.org/doc/latest/HTML/scons-api/SCons.Util/#module-SCons.Util.sctypes)
  * [SCons.Util.stats module](https://scons.org/doc/latest/HTML/scons-api/SCons.Util/#module-SCons.Util.stats)

* [SCons.Variables package](https://scons.org/doc/latest/HTML/scons-api/SCons.Variables/)
  * [Module contents](https://scons.org/doc/latest/HTML/scons-api/SCons.Variables/#module-SCons.Variables)
  * [Submodules](https://scons.org/doc/latest/HTML/scons-api/SCons.Variables/#submodules)
  * [SCons.Variables.BoolVariable module](https://scons.org/doc/latest/HTML/scons-api/SCons.Variables/#module-SCons.Variables.BoolVariable)
  * [SCons.Variables.EnumVariable module](https://scons.org/doc/latest/HTML/scons-api/SCons.Variables/#module-SCons.Variables.EnumVariable)
  * [SCons.Variables.ListVariable module](https://scons.org/doc/latest/HTML/scons-api/SCons.Variables/#module-SCons.Variables.ListVariable)
  * [SCons.Variables.PackageVariable module](https://scons.org/doc/latest/HTML/scons-api/SCons.Variables/#module-SCons.Variables.PackageVariable)
  * [SCons.Variables.PathVariable module](https://scons.org/doc/latest/HTML/scons-api/SCons.Variables/#module-SCons.Variables.PathVariable)

Indices and Tables[#](https://scons.org/doc/latest/HTML/scons-api/index.html#indices-and-tables "Link to this heading")
=======================================================================================================================

* [Index](https://scons.org/doc/latest/HTML/scons-api/genindex/)

* [Module Index](https://scons.org/doc/latest/HTML/scons-api/py-modindex/)

* [Search Page](https://scons.org/doc/latest/HTML/scons-api/search/)

[next SCons package](https://scons.org/doc/latest/HTML/scons-api/SCons/ "next page")

 Contents

* [SCons API Documentation](https://scons.org/doc/latest/HTML/scons-api/index.html#)
* [Indices and Tables](https://scons.org/doc/latest/HTML/scons-api/index.html#indices-and-tables)

By SCons Project Team

© Copyright Copyright (c) 2001 - 2025 The SCons Foundation.
