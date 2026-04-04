::: {#environment-variables}
::: redirect-from
/faq/installing_faq
:::
:::

::: redirect-from
/users/faq/installing_faq
:::

::: redirect-from
/users/installing/environment_variables_faq
:::

# Environment variables

::: envvar
HOME

The user\'s home directory. On Linux, `~ <HOME>`{.interpreted-text
role="envvar"} is shorthand for `HOME`{.interpreted-text role="envvar"}.
:::

::: envvar
MPLBACKEND

This optional variable can be set to choose the Matplotlib backend. See
`what-is-a-backend`{.interpreted-text role="ref"}.
:::

::: envvar
MPLCONFIGDIR

This is the directory used to store user customizations to Matplotlib,
as well as some caches to improve performance. If
`MPLCONFIGDIR`{.interpreted-text role="envvar"} is not defined,
`{HOME}/.config/matplotlib`{.interpreted-text role="file"} and
`{HOME}/.cache/matplotlib`{.interpreted-text role="file"} are used on
Linux, and `{HOME}/.matplotlib`{.interpreted-text role="file"} on other
platforms, if they are writable. Otherwise, the Python standard
library\'s [tempfile.gettempdir]{.title-ref} is used to find a base
directory in which the `matplotlib`{.interpreted-text role="file"}
subdirectory is created.
:::

::: envvar
PATH

The list of directories searched to find executable programs.
:::

::: envvar
PYTHONPATH

The list of directories that are added to Python\'s standard search list
when importing packages and modules.
:::

::: envvar
QT_API

The Python Qt wrapper to prefer when using Qt-based backends. See `the
entry in the usage guide <QT_bindings>`{.interpreted-text role="ref"}
for more information.
:::

## Setting environment variables in Linux and macOS {#setting-linux-macos-environment-variables}

To list the current value of `PYTHONPATH`{.interpreted-text
role="envvar"}, which may be empty, try:

    echo $PYTHONPATH

The procedure for setting environment variables in depends on what your
default shell is. Common shells include `bash`{.interpreted-text
role="program"} and `csh`{.interpreted-text role="program"}. You should
be able to determine which by running at the command prompt:

    echo $SHELL

To create a new environment variable:

    export PYTHONPATH=~/Python  # bash/ksh
    setenv PYTHONPATH ~/Python  # csh/tcsh

To prepend to an existing environment variable:

    export PATH=~/bin:${PATH}  # bash/ksh
    setenv PATH ~/bin:${PATH}  # csh/tcsh

The search order may be important to you, do you want
`~/bin`{.interpreted-text role="file"} to be searched first or last? To
append to an existing environment variable:

    export PATH=${PATH}:~/bin  # bash/ksh
    setenv PATH ${PATH}:~/bin  # csh/tcsh

To make your changes available in the future, add the commands to your
`~/.bashrc`{.interpreted-text role="file"} or
`~/.cshrc`{.interpreted-text role="file"} file.

## Setting environment variables in Windows {#setting-windows-environment-variables}

Open the `Control Panel`{.interpreted-text role="program"}
(`Start --> Control Panel`{.interpreted-text role="menuselection"}),
start the `System`{.interpreted-text role="program"} program. Click the
`Advanced`{.interpreted-text role="guilabel"} tab and select the
`Environment Variables`{.interpreted-text role="guilabel"} button. You
can edit or add to the `User Variables`{.interpreted-text
role="guilabel"}.
