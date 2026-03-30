# Source: https://virtualenv.pypa.io/en/latest/reference/compatibility.html

Title: Compatibility - virtualenv

URL Source: https://virtualenv.pypa.io/en/latest/reference/compatibility.html

Markdown Content:
Supported Python implementations[¶](https://virtualenv.pypa.io/en/latest/reference/compatibility.html#supported-python-implementations "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------------------------

`virtualenv` works with the following Python interpreter implementations. Only the latest patch version of each minor version is fully supported; previous patch versions work on a best effort basis.

### CPython[¶](https://virtualenv.pypa.io/en/latest/reference/compatibility.html#cpython "Link to this heading")

`3.14 >= python_version >= 3.8`

### PyPy[¶](https://virtualenv.pypa.io/en/latest/reference/compatibility.html#pypy "Link to this heading")

`3.11 >= python_version >= 3.8`

### GraalPy[¶](https://virtualenv.pypa.io/en/latest/reference/compatibility.html#graalpy "Link to this heading")

`24.1` and later (Linux and macOS only).

### RustPython[¶](https://virtualenv.pypa.io/en/latest/reference/compatibility.html#rustpython "Link to this heading")

Experimental support (Linux, macOS, and Windows). [RustPython](https://github.com/RustPython/RustPython) implements Python 3.14.

Support policy[¶](https://virtualenv.pypa.io/en/latest/reference/compatibility.html#support-policy "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------

* **New versions** are added close to their release date, typically during the beta phase.

* **Old versions** are dropped 18 months after [CPython EOL](https://devguide.python.org/versions/), giving users plenty of time to migrate.

Version support timeline[¶](https://virtualenv.pypa.io/en/latest/reference/compatibility.html#version-support-timeline "Link to this heading")
----------------------------------------------------------------------------------------------------------------------------------------------

Major version support changes:

* **20.27.0** (2024-10-17): dropped support for running under Python 3.7 and earlier.

* **20.22.0** (2023-04-19): dropped support for creating environments for Python 3.6 and earlier.

* **20.18.0** (2023-02-06): dropped support for running under Python 3.6 and earlier.

Supported operating systems[¶](https://virtualenv.pypa.io/en/latest/reference/compatibility.html#supported-operating-systems "Link to this heading")
----------------------------------------------------------------------------------------------------------------------------------------------------

CPython is shipped in multiple forms, and each OS repackages it, often applying some customization. The platforms listed below are tested. Unlisted platforms may work but are not explicitly supported. If you encounter issues on unlisted platforms, please open a feature request.

### Cross-platform[¶](https://virtualenv.pypa.io/en/latest/reference/compatibility.html#cross-platform "Link to this heading")

These Python distributions work on Linux, macOS, and Windows:

* Installations from [python.org](https://www.python.org/downloads/)

* [python-build-standalone](https://github.com/astral-sh/python-build-standalone) builds (used by [uv](https://docs.astral.sh/uv/) and [mise](https://mise.jdx.dev/))

* Python versions managed by [pyenv](https://github.com/pyenv/pyenv), [mise](https://mise.jdx.dev/), or [asdf](https://asdf-vm.com/) (shims are automatically resolved to the real binary)

### Linux[¶](https://virtualenv.pypa.io/en/latest/reference/compatibility.html#linux "Link to this heading")

* Ubuntu 16.04 and later (both upstream and [deadsnakes](https://launchpad.net/~deadsnakes/+archive/ubuntu/ppa) builds)

* Fedora

* RHEL and CentOS

* OpenSuse

* Arch Linux

### macOS[¶](https://virtualenv.pypa.io/en/latest/reference/compatibility.html#macos "Link to this heading")

* Python versions installed via [Homebrew](https://docs.brew.sh/Homebrew-and-Python) (works, but [not recommended](https://justinmayer.com/posts/homebrew-python-is-not-for-you/) – Homebrew may upgrade or remove Python versions without warning, breaking existing virtual environments)

* Python 3 part of XCode (Python framework builds at `/Library/Frameworks/Python3.framework/`)

Note

Framework builds do not support copy-based virtual environments. Use symlink or hardlink creation methods instead.

### Windows[¶](https://virtualenv.pypa.io/en/latest/reference/compatibility.html#windows "Link to this heading")

* [Windows Store](https://apps.microsoft.com/search?query=python) Python 3.8 and later
