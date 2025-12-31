# Source: https://typer.tiangolo.com/environment-variables/

# Environment Variables[¶](#environment-variables "Permanent link")

Before we jump into **Typer** code, let\'s cover a bit some of the **basics** that we\'ll need to understand how to work with Python (and programming) in general. Let\'s check a bit about **environment variables**.

Tip

If you already know what \"environment variables\" are and how to use them, feel free to skip this.

An environment variable (also known as \"**env var**\") is a variable that lives **outside** of the Python code, in the **operating system**, and could be read by your Python code (or by other programs as well).

Environment variables could be useful for handling application **settings**, as part of the **installation** of Python, etc.

## Create and Use Env Vars[¶](#create-and-use-env-vars "Permanent link")

You can **create** and use environment variables in the **shell (terminal)**, without needing Python:

Linux, macOS, Windows BashWindows PowerShell

## Read env vars in Python[¶](#read-env-vars-in-python "Permanent link")

You could also create environment variables **outside** of Python, in the terminal (or with any other method), and then **read them in Python**.

For example you could have a file `main.py` with:

    import os

    name = os.getenv("MY_NAME", "World")
    print(f"Hello  from Python")

Tip

The second argument to [`os.getenv()`](https://docs.python.org/3.8/library/os.html#os.getenv) is the default value to return.

If not provided, it\'s `None` by default, here we provide `"World"` as the default value to use.

Then you could call that Python program:

Linux, macOS, Windows BashWindows PowerShell

As environment variables can be set outside of the code, but can be read by the code, and don\'t have to be stored (committed to `git`) with the rest of the files, it\'s common to use them for configurations or **settings**.

You can also create an environment variable only for a **specific program invocation**, that is only available to that program, and only for its duration.

To do that, create it right before the program itself, on the same line:

    // Create an env var MY_NAME in line for this program call
    $ MY_NAME="Wade Wilson" python main.py

    // Now it can read the environment variable

    Hello Wade Wilson from Python

    // The env var no longer exists afterwards
    $ python main.py

    Hello World from Python

Tip

You can read more about it at [The Twelve-Factor App: Config](https://12factor.net/config).

## Types and Validation[¶](#types-and-validation "Permanent link")

These environment variables can only handle **text strings**, as they are external to Python and have to be compatible with other programs and the rest of the system (and even with different operating systems, as Linux, Windows, macOS).

That means that **any value** read in Python from an environment variable **will be a `str`**, and any conversion to a different type or any validation has to be done in code.

You will learn more about using environment variables for your CLI applications later in the section about [CLI Arguments with Environment Variables](../tutorial/arguments/envvar/).

## `PATH` Environment Variable[¶](#path-environment-variable "Permanent link")

There is a **special** environment variable called **`PATH`** that is used by the operating systems (Linux, macOS, Windows) to find programs to run.

The value of the variable `PATH` is a long string that is made of directories separated by a colon `:` on Linux and macOS, and by a semicolon `;` on Windows.

For example, the `PATH` environment variable could look like this:

Linux, macOSWindows

This means that the system should look for programs in the directories:

-   `/usr/local/bin`
-   `/usr/bin`
-   `/bin`
-   `/usr/sbin`
-   `/sbin`

This means that the system should look for programs in the directories:

-   `C:\Program Files\Python312\Scripts`
-   `C:\Program Files\Python312`
-   `C:\Windows\System32`

When you type a **command** in the terminal, the operating system **looks for** the program in **each of those directories** listed in the `PATH` environment variable.

For example, when you type `python` in the terminal, the operating system looks for a program called `python` in the **first directory** in that list.

If it finds it, then it will **use it**. Otherwise it keeps looking in the **other directories**.

### Installing Python and Updating the `PATH`[¶](#installing-python-and-updating-the-path "Permanent link")

When you install Python, you might be asked if you want to update the `PATH` environment variable.

Linux, macOSWindows

So, if you type:

    $ python

Linux, macOSWindows

This information will be useful when learning about [Virtual Environments](../virtual-environments/).

It will also be useful when you **create your own CLI programs** as, for them to be available for your users, they will need to be somewhere in the `PATH` environment variable.

## Conclusion[¶](#conclusion "Permanent link")

With this you should have a basic understanding of what **environment variables** are and how to use them in Python.

You can also read more about them in the [Wikipedia for Environment Variable](https://en.wikipedia.org/wiki/Environment_variable).

In many cases it\'s not very obvious how environment variables would be useful and applicable right away. But they keep showing up in many different scenarios when you are developing, so it\'s good to know about them.

For example, you will need this information in the next section, about [Virtual Environments](../virtual-environments/).