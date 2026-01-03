::: redirect-from
/users/installing
:::

::: redirect-from
/users/installing/index
:::

# Installation

::: {.tab-set .sd-width-content-min}
::: tab-item
pip

``` bash
pip install matplotlib
```
:::

::: tab-item
conda

``` bash
conda install -c conda-forge matplotlib
```
:::

::: tab-item
pixi

``` bash
pixi add matplotlib
```
:::

::: tab-item
uv

``` bash
uv add matplotlib
```

::: warning
::: title
Warning
:::

uv usually installs its own versions of Python from the
python-build-standalone project, and only recent versions of those
Python builds (August 2025) work properly with the `tkagg` backend for
displaying plots in a window. Please make sure you are using uv 0.8.7 or
newer (update with e.g. `uv self update`) and that your bundled Python
installs are up to date (with `uv python upgrade --reinstall`).
Alternatively, you can use one of the other
`supported GUI frameworks <optional_dependencies>`{.interpreted-text
role="ref"}, e.g.

``` bash
uv add matplotlib pyside6
```
:::
:::

::: tab-item
other

`install-official`{.interpreted-text role="ref"}

`install-third-party`{.interpreted-text role="ref"}

`install-nightly-build`{.interpreted-text role="ref"}

`install-source`{.interpreted-text role="ref"}
:::
:::

## Install an official release {#install-official}

Matplotlib releases are available as wheel packages for macOS, Windows
and Linux on [PyPI](https://pypi.org/project/matplotlib/). Install it
using `pip`:

``` sh
python -m pip install -U pip
python -m pip install -U matplotlib
```

If this command results in Matplotlib being compiled from source and
there\'s trouble with the compilation, you can add `--prefer-binary` to
select the newest version of Matplotlib for which there is a precompiled
wheel for your OS and Python.

::: note
::: title
Note
:::

The following non-interactive backends work out of the box: Agg, ps,
pdf, svg

The TkAgg interactive backend also typically works out of the box. It
requires Tk bindings, which are usually provided via the Python standard
library\'s `tkinter` module. On some OSes, you may need to install a
separate package like `python3-tk` to add this component of the standard
library.

Some tools like `uv` make use of Python builds from the
python-build-standalone project, which only gained usable Tk bindings
recently (August 2025). If you are having trouble with the TkAgg
backend, ensure you have an up-to-date build, e.g.
`uv self update && uv python upgrade --reinstall`.

For support of other GUI frameworks, LaTeX rendering, saving animations
and a larger selection of file formats, you can install
`optional dependencies <optional_dependencies>`{.interpreted-text
role="ref"}.
:::

## Third-party distributions {#install-third-party}

Various third-parties provide Matplotlib for their environments.

### Conda packages

Matplotlib is available both via the *anaconda main channel* :

``` sh
conda install matplotlib
```

as well as via the *conda-forge community channel* :

``` sh
conda install -c conda-forge matplotlib
```

### Python distributions

Matplotlib is part of major Python distributions:

-   [Anaconda](https://www.anaconda.com/)
-   [ActiveState
    ActivePython](https://www.activestate.com/products/python/downloads/)
-   [WinPython](https://winpython.github.io/)

### Linux package manager

If you are using the Python version that comes with your Linux
distribution, you can install Matplotlib via your package manager, e.g.:

-   Debian / Ubuntu: `sudo apt-get install python3-matplotlib`
-   Fedora: `sudo dnf install python3-matplotlib`
-   Red Hat: `sudo yum install python3-matplotlib`
-   Arch: `sudo pacman -S python-matplotlib`

::: redirect-from
/users/installing/installing_source
:::

## Install a nightly build {#install-nightly-build}

Matplotlib makes nightly development build wheels available on the
[scientific-python-nightly-wheels Anaconda Cloud
organization](https://anaconda.org/scientific-python-nightly-wheels).
These wheels can be installed with `pip` by specifying
scientific-python-nightly-wheels as the package index to query:

``` sh
python -m pip install \
  --upgrade \
  --pre \
  --index-url https://pypi.anaconda.org/scientific-python-nightly-wheels/simple \
  --extra-index-url https://pypi.org/simple \
  matplotlib
```

## Install from source {#install-source}

::: {.admonition .important}
Installing for Development

If you would like to contribute to Matplotlib or otherwise need to
install the latest development code, please follow the instructions in
`installing_for_devs`{.interpreted-text role="ref"}.
:::

The following instructions are for installing from source for production
use. This is generally *not* recommended; please use prebuilt packages
when possible. Proceed with caution because these instructions may
result in your build producing unexpected behavior and/or causing local
testing to fail.

Before trying to install Matplotlib, please install the
`dependencies`{.interpreted-text role="ref"}.

To build from a tarball, download the latest *tar.gz* release file from
[the PyPI files page](https://pypi.org/project/matplotlib/).

If you are building your own Matplotlib wheels (or sdists) on Windows,
note that any DLLs that you copy into the source tree will be packaged
too.

## Configure build and behavior defaults

We provide a
[meson.options](https://github.com/matplotlib/matplotlib/blob/main/meson.options)
file containing options with which you can use to customize the build
process. For example, which default backend to use, whether some of the
optional libraries that Matplotlib ships with are installed, and so on.
These options will be particularly useful to those packaging Matplotlib.

Aspects of some behavioral defaults of the library can be configured
via:

::: {.toctree maxdepth="2"}
environment_variables_faq.rst
:::

Default plotting appearance and behavior can be configured via the
`rcParams file <customizing-with-matplotlibrc-files>`{.interpreted-text
role="ref"}.

## Dependencies

Mandatory dependencies should be installed automatically if you install
Matplotlib using a package manager such as `pip` or `conda`; therefore
this list is primarily for reference and troubleshooting.

::: {.toctree maxdepth="2"}
dependencies
:::

## Frequently asked questions {#installing-faq}

### Report a compilation problem

See `reporting-problems`{.interpreted-text role="ref"}.

### Matplotlib compiled fine, but nothing shows up when I use it

The first thing to try is a
`clean install <clean-install>`{.interpreted-text role="ref"} and see if
that helps. If not, the best way to test your install is by running a
script, rather than working interactively from a python shell or an
integrated development environment such as `IDLE`{.interpreted-text
role="program"} which add additional complexities. Open up a UNIX shell
or a DOS command prompt and run, for example:

``` sh
python -c "from pylab import *; set_loglevel('DEBUG'); plot(); show()"
```

This will give you additional information about which backends
Matplotlib is loading, version information, and more. At this point you
might want to make sure you understand Matplotlib\'s
`configuration <customizing>`{.interpreted-text role="ref"} process,
governed by the `matplotlibrc`{.interpreted-text role="file"}
configuration file which contains instructions within and the concept of
the Matplotlib backend.

If you are still having trouble, see
`reporting-problems`{.interpreted-text role="ref"}.

### How to completely remove Matplotlib {#clean-install}

Occasionally, problems with Matplotlib can be solved with a clean
installation of the package. In order to fully remove an installed
Matplotlib:

1.  Delete the caches from your `Matplotlib configuration directory
    <locating-matplotlib-config-dir>`{.interpreted-text role="ref"}.
2.  Delete any Matplotlib directories or eggs from your `installation
    directory <locating-matplotlib-install>`{.interpreted-text
    role="ref"}.

### macOS Notes

#### Which python for macOS?

Apple ships macOS with its own Python, in `/usr/bin/python`, and its own
copy of Matplotlib. Unfortunately, the way Apple currently installs its
own copies of NumPy, Scipy and Matplotlib means that these packages are
difficult to upgrade (see [system python
packages](https://github.com/MacPython/wiki/wiki/Which-Python#system-python-and-extra-python-packages)).
For that reason we strongly suggest that you install a fresh version of
Python and use that as the basis for installing libraries such as NumPy
and Matplotlib. One convenient way to install Matplotlib with other
useful Python software is to use the
[Anaconda](https://www.anaconda.com/) Python scientific software
collection, which includes Python itself and a wide range of libraries;
if you need a library that is not available from the collection, you can
install it yourself using standard methods such as *pip*. See the
Anaconda web page for installation support.

Other options for a fresh Python install are the standard installer from
[python.org](https://www.python.org/downloads/macos/), or installing
Python using a general macOS package management system such as
[homebrew](https://brew.sh/) or [macports](https://www.macports.org).
Power users on macOS will likely want one of homebrew or macports on
their system to install open source software packages, but it is
perfectly possible to use these systems with another source for your
Python binary, such as Anaconda or Python.org Python.

#### Installing macOS binary wheels {#install_macos_binaries}

If you are using Python from <https://www.python.org>, Homebrew, or
Macports, then you can use the standard pip installer to install
Matplotlib binaries in the form of wheels.

pip is installed by default with python.org and Homebrew Python, but
needs to be manually installed on Macports with :

``` sh
sudo port install py38-pip
```

Once pip is installed, you can install Matplotlib and all its
dependencies with from the Terminal.app command line:

``` sh
python3 -m pip install matplotlib
```

You might also want to install IPython or the Jupyter notebook
(`python3 -m pip install ipython notebook`).

#### Checking your installation

The new version of Matplotlib should now be on your Python \"path\".
Check this at the Terminal.app command line:

``` sh
python3 -c 'import matplotlib; print(matplotlib.__version__, matplotlib.__file__)'
```

You should see something like

``` none
3.10.0 /Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages/matplotlib/__init__.py
```

where `3.10.0` is the Matplotlib version you just installed, and the
path following depends on whether you are using Python.org Python,
Homebrew or Macports. If you see another version, or you get an error
like

``` none
Traceback (most recent call last):
  File "<string>", line 1, in <module>
ImportError: No module named matplotlib
```

then check that the Python binary is the one you expected by running :

``` sh
which python3
```

If you get a result like `/usr/bin/python...`, then you are getting the
Python installed with macOS, which is probably not what you want. Try
closing and restarting Terminal.app before running the check again. If
that doesn\'t fix the problem, depending on which Python you wanted to
use, consider reinstalling Python.org Python, or check your homebrew or
macports setup. Remember that the disk image installer only works for
Python.org Python, and will not get picked up by other Pythons. If all
these fail, please `let us know
<reporting-problems>`{.interpreted-text role="ref"}.

::: {#troubleshooting-install}
::: redirect-from
/users/installing/troubleshooting_faq
:::
:::

## Troubleshooting

### Obtaining Matplotlib version {#matplotlib-version}

To find out your Matplotlib version number, import it and print the
`__version__` attribute:

\>\>\> import matplotlib \>\>\> matplotlib.\_\_version\_\_ \'0.98.0\'

### `matplotlib`{.interpreted-text role="file"} install location {#locating-matplotlib-install}

You can find what directory Matplotlib is installed in by importing it
and printing the `__file__` attribute:

\>\>\> import matplotlib \>\>\> matplotlib.\_\_file\_\_
\'/home/jdhunter/dev/lib64/python2.5/site-packages/matplotlib/\_\_init\_\_.pyc\'

### `matplotlib`{.interpreted-text role="file"} configuration and cache directory locations {#locating-matplotlib-config-dir}

Each user has a Matplotlib configuration directory which may contain a
`matplotlibrc <customizing-with-matplotlibrc-files>`{.interpreted-text
role="ref"} file. To locate your `matplotlib/`{.interpreted-text
role="file"} configuration directory, use
`matplotlib.get_configdir`{.interpreted-text role="func"}:

\>\>\> import matplotlib as mpl \>\>\> mpl.get_configdir()
\'/home/darren/.config/matplotlib\'

On Unix-like systems, this directory is generally located in your
`HOME`{.interpreted-text role="envvar"} directory under the
`.config/`{.interpreted-text role="file"} directory.

In addition, users have a cache directory. On Unix-like systems, this is
separate from the configuration directory by default. To locate your
`.cache/`{.interpreted-text role="file"} directory, use
`matplotlib.get_cachedir`{.interpreted-text role="func"}:

\>\>\> import matplotlib as mpl \>\>\> mpl.get_cachedir()
\'/home/darren/.cache/matplotlib\'

On Windows, both the config directory and the cache directory are the
same and are in your `Documents and Settings`{.interpreted-text
role="file"} or `Users`{.interpreted-text role="file"} directory by
default:

\>\>\> import matplotlib as mpl \>\>\> mpl.get_configdir()
\'C:\\Documents and Settings\\jdhunter\\.matplotlib\' \>\>\>
mpl.get_cachedir() \'C:\\Documents and Settings\\jdhunter\\.matplotlib\'

If you would like to use a different configuration directory, you can do
so by specifying the location in your `MPLCONFIGDIR`{.interpreted-text
role="envvar"} environment variable \-- see
`setting-linux-macos-environment-variables`{.interpreted-text
role="ref"}. Note that `MPLCONFIGDIR`{.interpreted-text role="envvar"}
sets the location of both the configuration directory and the cache
directory.
