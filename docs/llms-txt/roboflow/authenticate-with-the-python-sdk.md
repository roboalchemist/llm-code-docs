# Source: https://docs.roboflow.com/developer/python-sdk/authenticate-with-the-python-sdk.md

# Authenticate with the Python SDK

You can authenticate with the Python package using:

* A command, or;
* A `login()` method.

### Authenticate with the CLI

To authenticate with the Python SDK using the command line, run:

```
roboflow login
```

You will then be given a URL to which you can go to issue a Token.

You will be asked to select a workspace, then given a token for use in the Python package or CLI.

This Token will then be used to saved to your computer for use in authenticating with the Roboflow API through the Python Package.

To reauthenticate, run `roboflow login` again.

### Authenticate with the SDK

You can also authenticate with the SDK using the `roboflow.login()` method.

To authenticate with this method, add the following line of code after you import the `roboflow` Python package into a script:

```
roboflow.login()
```

You will then be given a URL to which you can go to issue a Token.

You will be asked to select a workspace, then given a token for use in the Python package or CLI.

This Token will then be used to saved to your computer for use in authenticating with the Roboflow API through the Python Package.

If you want to change accounts, you will need to reauthenticate. You can reauthenticate using the following command:

```
roboflow.login(force=True)
```
