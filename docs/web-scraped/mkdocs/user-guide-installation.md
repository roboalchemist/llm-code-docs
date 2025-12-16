# Source: https://www.mkdocs.org/user-guide/installation/

[MkDocs](../..)

[]

-   [Home](../..)
-   [Getting Started](../../getting-started/)
-   [User Guide ](#)
    -   [User Guide](../)
    -   [Installation](./)
    -   [Writing Your Docs](../writing-your-docs/)
    -   [Choosing Your Theme](../choosing-your-theme/)
    -   [Customizing Your Theme](../customizing-your-theme/)
    -   [Localizing Your Theme](../localizing-your-theme/)
    -   [Configuration](../configuration/)
    -   [Command Line Interface](../cli/)
    -   [Deploying Your Docs](../deploying-your-docs/)
-   [Developer Guide ](#)
    -   [Developer Guide](../../dev-guide/)
    -   [Themes](../../dev-guide/themes/)
    -   [Translations](../../dev-guide/translations/)
    -   [Plugins](../../dev-guide/plugins/)
    -   [API Reference](../../dev-guide/api/)
-   [About ](#)
    -   [Release Notes](../../about/release-notes/)
    -   [Contributing](../../about/contributing/)
    -   [License](../../about/license/)

```
<!-- -->
```
-   [ Search](#)
-   [ Previous](../)
-   [Next ](../writing-your-docs/)
-   [ Edit on GitHub](https://github.com/mkdocs/mkdocs/blob/master/docs/user-guide/installation.md)

[]

-   [MkDocs Installation](#mkdocs-installation)
    -   [Requirements](#requirements)
    -   [Installing MkDocs](#installing-mkdocs)

# MkDocs Installation[](#mkdocs-installation "Permanent link")

A detailed guide.

------------------------------------------------------------------------

## Requirements[](#requirements "Permanent link")

MkDocs requires a recent version of [Python](https://www.python.org/) and the Python package manager, [pip](https://pip.readthedocs.io/en/stable/installing/), to be installed on your system.

You can check if you already have these installed from the command line:

``` highlight
$ python --version
Python 3.8.2
$ pip --version
pip 20.0.2 from /usr/local/lib/python3.8/site-packages/pip (python 3.8)
```

If you already have those packages installed, you may skip down to [Installing MkDocs](#installing-mkdocs).

### Installing Python[](#installing-python "Permanent link")

Install [Python](https://www.python.org/) using your package manager of choice, or by downloading an installer appropriate for your system from [python.org](https://www.python.org/downloads/) and running it.

Note

If you are installing Python on Windows, be sure to check the box to have Python added to your PATH if the installer offers such an option (it\'s normally off by default).

![Add Python to PATH](../../img/win-py-install.png)

### Installing pip[](#installing-pip "Permanent link")

If you\'re using a recent version of Python, the Python package manager, [pip](https://pip.readthedocs.io/en/stable/installing/), is most likely installed by default. However, you may need to upgrade pip to the lasted version:

``` highlight
pip install --upgrade pip
```

If you need to install pip for the first time, download [get-pip.py](https://bootstrap.pypa.io/get-pip.py). Then run the following command to install it:

``` highlight
python get-pip.py
```

## Installing MkDocs[](#installing-mkdocs "Permanent link")

Install the `mkdocs` package using pip:

``` highlight
pip install mkdocs
```

You should now have the `mkdocs` command installed on your system. Run `mkdocs --version` to check that everything worked okay.

``` highlight
$ mkdocs --version
mkdocs, version 1.2.0 from /usr/local/lib/python3.8/site-packages/mkdocs (Python 3.8)
```

Note

If you would like manpages installed for MkDocs, the [click-man](https://github.com/click-contrib/click-man) tool can generate and install them for you. Simply run the following two commands:

``` highlight
pip install click-man
click-man --target path/to/man/pages mkdocs
```

See the [click-man documentation](https://github.com/click-contrib/click-man#automatic-man-page-installation-with-setuptools-and-pip) for an explanation of why manpages are not automatically generated and installed by pip.

Note

If you are using Windows, some of the above commands may not work out-of-the-box.

A quick solution may be to preface every Python command with `python -m` like this:

``` highlight
python -m pip install mkdocs
python -m mkdocs
```

For a more permanent solution, you may need to edit your `PATH` environment variable to include the `Scripts` directory of your Python installation. Recent versions of Python include a script to do this for you. Navigate to your Python installation directory (for example `C:\Python38\`), open the `Tools`, then `Scripts` folder, and run the `win_add2path.py` file by double clicking on it. Alternatively, you can download the [script](https://github.com/python/cpython/blob/master/Tools/scripts/win_add2path.py) and run it (`python win_add2path.py`).

------------------------------------------------------------------------

Copyright © 2014 [Tom Christie](https://twitter.com/starletdreaming), Maintained by the [MkDocs Team](/about/release-notes/#maintenance-team).

Documentation built with [MkDocs](https://www.mkdocs.org/).

#### Search 

[×][Close]

From here you can search these documents. Enter your search terms below.

#### Keyboard Shortcuts 

[×][Close]

  Keys        Action
  ----------- ----------------
  [?]   Open this help
  [n]   Next page
  [p]   Previous page
  [s]   Search