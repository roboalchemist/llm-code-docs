# Source: https://help.cloudsmith.io/docs/nuget-symbol-server.md

# NuGet Symbol Server

Cloudsmith provides public & private symbol server support for NuGet

The NuGet Symbol Server is a repository that stores and serves debugging symbols (PDB files) and source files for packages published.

By using the Symbol Server, developers can step through and debug their code more easily, even when working with compiled libraries or packages, as it provides access to the necessary debugging information.

For more information on Symbol Server, please see:

* [NuGet](https://docs.microsoft.com/en-us/nuget/): The official website for NuGet Documentation
* [Symbols for Windows Debugging](https://learn.microsoft.com/en-us/windows-hardware/drivers/debugger/symbols): Official documentation on Symbols for windows
* [Symbols in the Visual Studio Debugger](https://docs.microsoft.com/en-us/visualstudio/debugger/specify-symbol-dot-pdb-and-source-files-in-the-visual-studio-debugger): Official guide on configuring a Symbol Server on Visual Studio

In the following examples:

| Identifier    | Description                                                                               |
| :------------ | :---------------------------------------------------------------------------------------- |
| OWNER         | Your Cloudsmith account name or organization name (namespace)                             |
| REPOSITORY    | Your Cloudsmith Repository name (also called "slug")                                      |
| TOKEN         | Your Cloudsmith Entitlement Token (see [Entitlements](https://help.cloudsmith.io/docs/entitlements) for more details) |
| USERNAME      | Your Cloudsmith username                                                                  |
| PASSWORD      | Your Cloudsmith password                                                                  |
| API-KEY       | Your Cloudsmith API Key                                                                   |
| PACKAGE\_NAME | The name of your package                                                                  |

## Configuring Cloudsmith Repository as Symbol Server

> 📘
>
> Private Cloudsmith repositories require authentication.  You can choose between two types of authentication, Entitlement Token Authentication or HTTP Basic Authentication.

Each individual repository in Cloudsmith can be configured as a Symbol Server in Visual Studio. Only symbols within that repository will be served back to the debugger.

In Visual Studio, go to `Tools > Options`

![](https://files.readme.io/07b2a66-image.png)

Inside Options, on the menu to the left navigate to `Debugging > Symbols`, using the plus icon on the top-right, enter the URL of your repository, as follows:

```Text Nuget - Symbol Server URL
https://nuget.cloudsmith.io/OWNER/REPOSITORY/download/symbols
```

![](https://files.readme.io/dfb62d0-image.png)

If your repository is private, at this stage you might be asked for credentials, you can use either an entitlement token or your personal api key.

```Text Entitlement Token
Username: token
Password: TOKEN
```

```Text Api Key
Username: USERNAME
Password: API-KEY
```

By default the debugger will only display and step into user code only, ignoring system code and other code that is optimized or does not have debugging symbols available locally. To allow Visual Studio to go fetch PDB symbols for imported nuget packages, the `Just My Code` option has to be disabled.

For this in the same Options screen, navigate to `Debugging > General` and disable `Just My Code`

![](https://files.readme.io/c2be6aa-image.png)

You can now start a debug session, the first time you do it Visual Studio, if your repository is private, it will prompt you for credentials:

![](https://files.readme.io/0c35b25-image.png)

You can use either an entitlement token or your personal api key.

```Text Entitlement Token
Username: token
Password: TOKEN
```

```Text Api Key
Username: USERNAME
Password: API-KEY
```

## Troubleshooting

### I have snupkg symbols in my repository but Visual Studio can't find them

If you had `snupkg` symbols uploaded from before this feature was released, it's possible that the `pdb` files are not indexed. Check in the UI in the `Files` tab if you see `pdb` files attached to your package

![](https://files.readme.io/99638c2-image.png)

If you don't see one or more `pdb` files here, then do a `Resync` of your package to force a re-index.

If you do see `pdb` files then it's possible that Visual Studio is configured to not load the module you want to debug. To fix this in Visual Studio, head to `Tools > Options`, and navigate to `Debugging > Symbols`, on the bottom of the screen there's an option titled `Automatic symbol loading preference`

![](https://files.readme.io/ef4d04b-image.png)

Set this to `Load all modules, unless excluded`