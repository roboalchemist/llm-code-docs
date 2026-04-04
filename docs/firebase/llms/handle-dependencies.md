# Source: https://firebase.google.com/docs/functions/handle-dependencies.md.txt

<br />

Node.jsPython  

<br />

There are two ways to specify dependencies forCloud Functionswritten in Python: using the[pip](https://pip.pypa.io/en/stable/)package manager's`requirements.txt`file or packaging local dependencies alongside your function.

Dependency specification using the Pipfile/Pipfile.lock standard is not supported. Your project should not include these files.

## Specifying dependencies with pip

Dependencies in Python are managed with pip and expressed in a metadata file called[`requirements.txt`](https://pip.pypa.io/en/stable/user_guide/#requirements-files). This file must be in the same directory as the`main.py`file that contains your function code.

When you deploy or redeploy your function, Cloud Functions uses pip to download and install the latest version of your dependencies as declared in the`requirements.txt`file. The`requirements.txt`file contains one line per package. Each line contains the package name, and optionally, the requested version. For more details, see the[`requirements.txt`reference](https://pip.pypa.io/en/stable/user_guide/#requirements-files).

To prevent your build from being affected by dependency version changes, consider pinning your dependency packages to a specific version.

The following is an example`requirements.txt`file:  

```
functions-framework
requests==2.20.0
numpy
```

## Packaging local dependencies

You can also package and deploy dependencies alongside your function. This approach is useful if your dependency is not available via the pip package manager or if your Cloud Functions environment's internet access is restricted.
| **Note:** You can still use a`requirements.txt`file to specify additional dependencies you haven't packaged alongside your function.

For example, you might use a directory structure such as the following:  

```
myfunction/
âââ main.py
âââ localpackage/
    âââ __init__.py
    âââ script.py
```

You can then import the code as usual from`localpackage`using the following`import`statement.  

```py
# Code in main.py
from localpackage import script
```

Note that this approach will*not* run any`setup.py`files. Packages with those files can still be bundled, but may not run correctly onCloud Functions.