::: redirect-from
/devel/gitwash/configure_git
:::

::: redirect-from
/devel/gitwash/dot2_dot3
:::

::: redirect-from
/devel/gitwash/following_latest
:::

::: redirect-from
/devel/gitwash/forking_hell
:::

::: redirect-from
/devel/gitwash/git_development
:::

::: redirect-from
/devel/gitwash/git_install
:::

::: redirect-from
/devel/gitwash/git_intro
:::

::: redirect-from
/devel/gitwash/git_resources
:::

::: redirect-from
/devel/gitwash/patching
:::

::: redirect-from
/devel/gitwash/set_up_fork
:::

::: redirect-from
/devel/gitwash/index
:::

# Setting up Matplotlib for development {#installing_for_devs}

To set up Matplotlib for development follow these steps:

::: {.contents local=""}
:::

## Fork the Matplotlib repository

Matplotlib is hosted at <https://github.com/matplotlib/matplotlib.git>.
If you plan on solving issues or submitting pull requests to the main
Matplotlib repository, you should first fork this repository by
*clicking* the `repo-forked`{.interpreted-text role="octicon"} **Fork**
button near the top of the [project
repository](https://github.com/matplotlib/matplotlib) page.

This creates a copy of the code under your account on the GitHub server.
See [the GitHub
documentation](https://docs.github.com/get-started/quickstart/fork-a-repo)
for more details.

## Set up development environment

You can either work locally on your machine, or online in [GitHub
Codespaces](https://docs.github.com/codespaces), a cloud-based
in-browser development environment.

local

:   If you are making extensive or frequent contributions to Matplotlib
    then it is probably worth taking the time to set up on your local
    machine: As well as having the convenience of your local familiar
    tools, you will not need to worry about Codespace\'s monthly usage
    limits.

codespaces

:   If you are making a one-off, relatively simple, change then working
    in GitHub Codespaces can be a good option because most of the
    setting up is done for you and you can skip the next few sections.

If you want to use Codespaces, skip to
`development-codespaces`{.interpreted-text role="ref"}, otherwise,
continue with the next section.

### Create local environment

#### Get most recent code

Now that your fork of the repository lives under your GitHub username,
you can retrieve the most recent version of the source code with one of
the following commands (replace `<your-username>` with your GitHub
username):

::: tab-set
::: tab-item
https

``` bash
git clone https://github.com/<your-username>/matplotlib.git
```
:::

::: tab-item
ssh

``` bash
git clone git@github.com:<your-username>/matplotlib.git
```

This requires you to setup an [SSH key]() in advance, but saves you from
typing your password at every connection.
:::
:::

This will place the sources in a directory
`matplotlib`{.interpreted-text role="file"} below your current working
directory and set the remote name `origin` to point to your fork. Change
into this directory before continuing:

``` bash
cd matplotlib
```

Now set the remote name `upstream` to point to the Matplotlib main
repository:

::: tab-set
::: tab-item
https

``` bash
git remote add upstream https://github.com/matplotlib/matplotlib.git
```
:::

::: tab-item
ssh

``` bash
git remote add upstream git@github.com:matplotlib/matplotlib.git
```
:::
:::

You can now use `upstream` to retrieve the most current snapshot of the
source code, as described in `development-workflow`{.interpreted-text
role="ref"}.

::: {.dropdown color="info" open=""}
Additional `git` and `GitHub` resources

For more information on `git` and `GitHub`, see:

-   [Git documentation](https://git-scm.com/doc)
-   [GitHub-Contributing to a
    Project](https://git-scm.com/book/en/v2/GitHub-Contributing-to-a-Project)
-   [GitHub Skills](https://skills.github.com/)
-   `using-git`{.interpreted-text role="external+scipy:ref"}
-   `git-resources`{.interpreted-text role="external+scipy:ref"}
-   [Installing
    git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
-   [Managing remote
    repositories](https://docs.github.com/en/get-started/getting-started-with-git/managing-remote-repositories)
-   <https://tacaswell.github.io/think-like-git.html>
-   <https://tom.preston-werner.com/2009/05/19/the-git-parable.html>
:::

#### Create a dedicated environment {#dev-environment}

You should set up a dedicated environment to decouple your Matplotlib
development from other Python and Matplotlib installations on your
system.

We recommend using one of the following options for a dedicated
development environment because these options are configured to install
the Python dependencies as part of their setup.

::: tab-set
::: tab-item
venv environment

Create a new [venv](https://docs.python.org/3/library/venv.html)
environment with :

``` bash
python -m venv <file folder location>
```

and activate it with one of the following :

::: tab-set
::: tab-item
Linux and macOS

``` bash
source <file folder location>/bin/activate  # Linux/macOS
```
:::

::: tab-item
Windows cmd.exe

``` bat
<file folder location>\Scripts\activate.bat
```
:::

::: tab-item
Windows PowerShell

``` ps1con
<file folder location>\Scripts\Activate.ps1
```
:::
:::

On some systems, you may need to type `python3` instead of `python`. For
a discussion of the technical reasons, see
[PEP-394](https://peps.python.org/pep-0394).

Install the Python dependencies with :

``` bash
pip install -r requirements/dev/dev-requirements.txt
```

Remember to activate the environment whenever you start working on
Matplotlib!
:::

::: tab-item
conda environment

Create a new
[conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)
environment and install the Python dependencies with :

``` bash
conda env create -f environment.yml
```

You can use `mamba` instead of `conda` in the above command if you have
[mamba]() installed.

Activate the environment using :

``` bash
conda activate mpl-dev
```

Remember to activate the environment whenever you start working on
Matplotlib!
:::
:::

#### Install external dependencies

Python dependencies were installed as part of
`setting up the environment <dev-environment>`{.interpreted-text
role="ref"}. Additionally, the following non-Python dependencies must
also be installed locally:

::: rst-class
checklist
:::

-   `compile-build-dependencies`{.interpreted-text role="ref"}
-   `external tools used by the documentation build <doc-dependencies-external>`{.interpreted-text
    role="ref"}

For a full list of dependencies, see `dependencies`{.interpreted-text
role="ref"}. External dependencies do not need to be installed when
working in codespaces.

### Create GitHub Codespace `codespaces`{.interpreted-text role="octicon"} {#development-codespaces}

[GitHub Codespaces](https://docs.github.com/codespaces) is a cloud-based
in-browser development environment that comes with the appropriate setup
to contribute to Matplotlib.

1.  Open codespaces on your fork by clicking on the green
    `code`{.interpreted-text role="octicon"} `Code` button on the GitHub
    web interface and selecting the `Codespaces` tab.

2.  Next, click on \"Open codespaces on \<your branch name\>\". You will
    be able to change branches later, so you can select the default
    `main` branch.

3.  After the codespace is created, you will be taken to a new browser
    tab where you can use the terminal to activate a pre-defined conda
    environment called `mpl-dev`:

    ``` bash
    conda activate mpl-dev
    ```

Remember to activate the *mpl-dev* environment whenever you start
working on Matplotlib.

If you need to open a GUI window with Matplotlib output on Codespaces,
our configuration includes a [light-weight Fluxbox-based
desktop](https://github.com/devcontainers/features/tree/main/src/desktop-lite).
You can use it by connecting to this desktop via your web browser. To do
this:

1.  Press `F1` or `Ctrl/Cmd+Shift+P` and select
    `Ports: Focus on Ports View` in the VSCode session to bring it into
    focus. Open the ports view in your tool, select the `noVNC` port,
    and click the Globe icon.
2.  In the browser that appears, click the Connect button and enter the
    desktop password (`vscode` by default).

Check the [GitHub
instructions](https://github.com/devcontainers/features/tree/main/src/desktop-lite#connecting-to-the-desktop)
for more details on connecting to the desktop.

If you also built the documentation pages, you can view them using
Codespaces. Use the \"Extensions\" icon in the activity bar to install
the \"Live Server\" extension. Locate the `doc/build/html` folder in the
Explorer, right click the file you want to open and select \"Open with
Live Server.\"

## Install Matplotlib in editable mode {#development-install}

Install Matplotlib in editable mode from the
`matplotlib`{.interpreted-text role="file"} directory using the command
:

``` bash
python -m pip install --verbose --no-build-isolation --editable ".[dev]"
```

The \'editable/develop mode\' builds everything and places links in your
Python environment so that Python will be able to import Matplotlib from
your development source directory. This allows you to import your
modified version of Matplotlib without having to re-install after
changing a `.py` or compiled extension file.

When working on a branch that does not have Meson enabled, meaning it
does not have `26621`{.interpreted-text role="ghpull"} in its history
(log), you will have to reinstall from source each time you change any
compiled extension code.

If the installation is not working, please consult the
`troubleshooting guide <troubleshooting-faq>`{.interpreted-text
role="ref"}. If the guide does not offer a solution, please reach out
via [chat](https://gitter.im/matplotlib/matplotlib) or
`open an issue <submitting-a-bug-report>`{.interpreted-text role="ref"}.

### Build options

If you are working heavily with files that need to be compiled, you may
want to inspect the compilation log. This can be enabled by setting the
environment variable `MESONPY_EDITABLE_VERBOSE`{.interpreted-text
role="envvar"} or by setting the `editable-verbose` config during
installation :

``` bash
python -m pip install --no-build-isolation --config-settings=editable-verbose=true --editable .
```

For more information on installation and other configuration options,
see the Meson Python
`editable installs guide <how-to-guides-editable-installs>`{.interpreted-text
role="external+meson-python:ref"}.

For a list of the other environment variables you can set before
install, see `environment-variables`{.interpreted-text role="ref"}.

## Verify the Installation

Run the following command to make sure you have correctly installed
Matplotlib in editable mode. The command should be run when the virtual
environment is activated:

``` bash
python -c "import matplotlib; print(matplotlib.__file__)"
```

This command should return :
`<matplotlib_local_repo>\lib\matplotlib\__init__.py`

We encourage you to run tests and build docs to verify that the code
installed correctly and that the docs build cleanly, so that when you
make code or document related changes you are aware of the existing
issues beforehand.

-   Run test cases to verify installation `testing`{.interpreted-text
    role="ref"}
-   Verify documentation build
    `documenting-matplotlib`{.interpreted-text role="ref"}

## Install pre-commit hooks {#pre-commit-hooks}

[pre-commit](https://pre-commit.com/) hooks save time in the review
process by identifying issues with the code before a pull request is
formally opened. Most hooks can also aide in fixing the errors, and the
checks should have corresponding
`development workflow <development-workflow>`{.interpreted-text
role="ref"} and `pull request <pr-guidelines>`{.interpreted-text
role="ref"} guidelines. Hooks are configured in
[.pre-commit-config.yaml](https://github.com/matplotlib/matplotlib/blob/main/.pre-commit-config.yaml?)
and include checks for spelling and formatting, flake 8 conformity,
accidentally committed files, import order, and incorrect branching.

Install pre-commit hooks :

``` bash
python -m pip install pre-commit
pre-commit install
```

Hooks are run automatically after the `git commit` stage of the
`editing workflow<edit-flow>`{.interpreted-text role="ref"}. When a hook
has found and fixed an error in a file, that file must be *staged and
committed* again.

Hooks can also be run manually. All the hooks can be run, in order as
listed in `.pre-commit-config.yaml`, against the full codebase with :

``` bash
pre-commit run --all-files
```

To run a particular hook manually, run `pre-commit run` with the hook id
:

``` bash
pre-commit run <hook id> --all-files
```

Please note that the `mypy` pre-commit hook cannot check the
`type-hints`{.interpreted-text role="ref"} for new functions; instead
the stubs for new functions are checked using the `stubtest`
`CI check <automated-tests>`{.interpreted-text role="ref"} and can be
checked locally using `tox -e stubtest`.
