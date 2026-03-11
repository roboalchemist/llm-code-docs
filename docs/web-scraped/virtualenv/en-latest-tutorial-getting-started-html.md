# Source: https://virtualenv.pypa.io/en/latest/tutorial/getting-started.html

Title: Getting started - virtualenv

URL Source: https://virtualenv.pypa.io/en/latest/tutorial/getting-started.html

Markdown Content:
This tutorial will teach you the basics of virtualenv through hands-on practice. You’ll create your first virtual environment, install packages, and learn how to manage project dependencies.

Prerequisites[¶](https://virtualenv.pypa.io/en/latest/tutorial/getting-started.html#prerequisites "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------

Before starting this tutorial, you need:

* Python 3.8 or later installed on your system. If you use a version manager like [pyenv](https://github.com/pyenv/pyenv), [mise](https://mise.jdx.dev/), or [asdf](https://asdf-vm.com/), virtualenv will automatically discover the Python version they manage.

* virtualenv installed (see [Install virtualenv](https://virtualenv.pypa.io/en/latest/how-to/install.html)).

Create your first virtual environment[¶](https://virtualenv.pypa.io/en/latest/tutorial/getting-started.html#create-your-first-virtual-environment "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Let’s create a virtual environment called `myproject`:

$ virtualenv myproject
created virtual environment CPython3.13.2.final.0-64 in 200ms
 creator CPython3Posix(dest=/home/user/myproject, clear=False, no_vcs_ignore=False, global=False)
 seeder FromAppData(download=False, pip=bundle, setuptools=bundle, via=copy, app_data_dir=/home/user/.cache/virtualenv)
 activators BashActivator,CShellActivator,FishActivator,NushellActivator,PowerShellActivator,PythonActivator

This creates a new directory called `myproject` containing a complete, isolated Python environment with its own copy of Python, pip, and other tools.

Activate the environment[¶](https://virtualenv.pypa.io/en/latest/tutorial/getting-started.html#activate-the-environment "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------

To use your virtual environment, you can activate it. The activation command differs by platform:

Linux/macOS

$ source myproject/bin/activate

Windows (PowerShell)

PS> .\myproject\Scripts\Activate.ps1

Windows (CMD)

C:\> .\myproject\Scripts\activate.bat

After activation, your prompt changes to show the active environment:

(myproject) $

You can verify that Python is now running from inside the virtual environment:

Linux/macOS

(myproject) $ which python
/home/user/myproject/bin/python

Windows (PowerShell)

(myproject) PS> where.exe python
C:\Users\user\myproject\Scripts\python.exe

Windows (CMD)

(myproject) C:\> where.exe python
C:\Users\user\myproject\Scripts\python.exe

Install a package[¶](https://virtualenv.pypa.io/en/latest/tutorial/getting-started.html#install-a-package "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------

With the environment activated, install a package using pip:

(myproject) $ pip install requests
Collecting requests
 Using cached requests-2.32.3-py3-none-any.whl (64 kB)
Installing collected packages: requests
Successfully installed requests-2.32.3

Verify that the package is installed only inside your virtual environment:

(myproject) $ python -c "import requests; print(requests.__file__)"
/home/user/myproject/lib/python3.13/site-packages/requests/__init__.py

The path shows that `requests` is installed in the virtual environment, not in your system Python.

Deactivate[¶](https://virtualenv.pypa.io/en/latest/tutorial/getting-started.html#deactivate "Link to this heading")
-------------------------------------------------------------------------------------------------------------------

When you’re done working in the virtual environment, deactivate it:

(myproject) $ deactivate
$

The prompt returns to normal, and Python commands now use your system Python again.

Use without activation[¶](https://virtualenv.pypa.io/en/latest/tutorial/getting-started.html#use-without-activation "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------------

Activation is a convenience, not a requirement. You can run any executable from the virtual environment directly by using its full path:

Linux/macOS

$ myproject/bin/python -c "import sys; print(sys.prefix)"
/home/user/myproject

$ myproject/bin/pip install httpx

Windows (PowerShell)

PS> .\myproject\Scripts\python.exe -c "import sys; print(sys.prefix)"
C:\Users\user\myproject

PS> .\myproject\Scripts\pip.exe install httpx

Windows (CMD)

C:\> .\myproject\Scripts\python.exe -c "import sys; print(sys.prefix)"
C:\Users\user\myproject

C:\> .\myproject\Scripts\pip.exe install httpx

This is especially useful in scripts, CI pipelines, and automation where modifying the shell environment is unnecessary.

Set up a real project[¶](https://virtualenv.pypa.io/en/latest/tutorial/getting-started.html#set-up-a-real-project "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------

Now let’s apply what you’ve learned to a real project workflow:

$ mkdir myapp && cd myapp
$ virtualenv venv
$ source venv/bin/activate # or use the appropriate command for your platform
(venv) $ pip install flask requests
(venv) $ pip freeze > requirements.txt

The `requirements.txt` file now contains your project’s dependencies:

blinker==1.9.0
certifi==2025.1.31
charset-normalizer==3.4.1
click==8.1.8
flask==3.1.0
idna==3.10
itsdangerous==2.2.0
Jinja2==3.1.5
MarkupSafe==3.0.2
requests==2.32.3
urllib3==2.3.0
werkzeug==3.1.3

This file lets you recreate the exact environment later. Let’s test this:

(venv) $ deactivate
$ rm -rf venv
$ virtualenv venv
$ source venv/bin/activate
(venv) $ pip install -r requirements.txt

All packages are reinstalled exactly as before. Here’s the complete workflow:

What you learned[¶](https://virtualenv.pypa.io/en/latest/tutorial/getting-started.html#what-you-learned "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------

In this tutorial, you learned how to:

* Create a virtual environment with `virtualenv`.

* Activate and deactivate virtual environments on different platforms.

* Install packages in isolation from your system Python.

* Save project dependencies with `pip freeze`.

* Reproduce environments using `requirements.txt`.

Next steps[¶](https://virtualenv.pypa.io/en/latest/tutorial/getting-started.html#next-steps "Link to this heading")
-------------------------------------------------------------------------------------------------------------------

Now that you understand the basics, explore these topics:

* [Use virtualenv](https://virtualenv.pypa.io/en/latest/how-to/usage.html) for selecting specific Python versions, configuring defaults, and advanced usage patterns.

* [Explanation](https://virtualenv.pypa.io/en/latest/explanation.html) for understanding how virtualenv works under the hood and how it compares to `venv`.

* [Command line](https://virtualenv.pypa.io/en/latest/reference/cli.html) for all available command line options and flags.
