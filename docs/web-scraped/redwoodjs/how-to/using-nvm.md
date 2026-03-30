# Source: https://docs.redwoodjs.com/docs/how-to/using-nvm

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [How To](/docs/how-to/index)
-   [Using nvm]

[Version: 8.8]

On this page

<div>

# Using nvm

</div>

## What is nvm?[​](#what-is-nvm "Direct link to What is nvm?") 

[nvm](https://github.com/nvm-sh/nvm) is a Node Version Manager. It\'s perfect for running multiple versions of Node.js on the same machine.

## Installing nvm[​](#installing-nvm "Direct link to Installing nvm") 

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTguODkzIDEuNWMtLjE4My0uMzEtLjUyLS41LS44ODctLjVzLS43MDMuMTktLjg4Ni41TC4xMzggMTMuNDk5YS45OC45OCAwIDAgMCAwIDEuMDAxYy4xOTMuMzEuNTMuNTAxLjg4Ni41MDFoMTMuOTY0Yy4zNjcgMCAuNzA0LS4xOS44NzctLjVhMS4wMyAxLjAzIDAgMCAwIC4wMS0xLjAwMkw4Ljg5MyAxLjV6bS4xMzMgMTEuNDk3SDYuOTg3di0yLjAwM2gyLjAzOXYyLjAwM3ptMC0zLjAwNEg2Ljk4N1Y1Ljk4N2gyLjAzOXY0LjAwNnoiPjwvcGF0aD48L3N2Zz4=)]warning

If you\'ve already installed Node.js on your machine, uninstall Node.js before installing nvm. This will prevent any conflicts between the Node.js and nvm.

### If you\'re on a Mac[​](#if-youre-on-a-mac "Direct link to If you're on a Mac") 

You can uninstall by running the following command in your terminal:

``` 
brew uninstall --force node
```

Once that\'s finished, run the following command to remove unused folders and dependencies:

``` 
brew cleanup
```

### If you\'re on Windows[​](#if-youre-on-windows "Direct link to If you're on Windows") 

-   Go to the start menu, search and go to **Settings**
-   Click on the **Apps** section
-   In the search box under **Apps & Features** section, search for **Nodejs**
-   Click on **Nodejs** and click on **Uninstall**
-   We recommend restarting your machine, even if you\'re not prompted to do so

### If you\'re on a Mac[​](#if-youre-on-a-mac-1 "Direct link to If you're on a Mac") 

You can install `nvm` using [Homebrew](https://brew.sh/):

``` 
brew install nvm
```

### If you\'re on Windows[​](#if-youre-on-windows-1 "Direct link to If you're on Windows") 

Reference the [nvm-windows](https://github.com/coreybutler/nvm-windows) repo.

-   Download the [latest installer](https://github.com/coreybutler/nvm-windows/releases) (nvm-setup.zip)
-   Locate your zip file (should be in your downloads or wherever you\'ve configured your downloads to be saved) and unzip/extract its contents
-   Now, you should have a file called **nvm-setup.exe**. Double click on it to run the installer.
-   Follow the instructions in the installer

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTcgMi4zYzMuMTQgMCA1LjcgMi41NiA1LjcgNS43cy0yLjU2IDUuNy01LjcgNS43QTUuNzEgNS43MSAwIDAgMSAxLjMgOGMwLTMuMTQgMi41Ni01LjcgNS43LTUuN3pNNyAxQzMuMTQgMSAwIDQuMTQgMCA4czMuMTQgNyA3IDcgNy0zLjE0IDctNy0zLjE0LTctNy03em0xIDNINnY1aDJWNHptMCA2SDZ2Mmgydi0yeiI+PC9wYXRoPjwvc3ZnPg==)]info

We have a specific doc for [Windows Development Setup.](/docs/how-to/windows-development-setup)

## How to use nvm[​](#how-to-use-nvm "Direct link to How to use nvm") 

To confirm that `nvm` was installed correctly, run the following command in your terminal:

``` 
nvm --version
```

You should see the version number of `nvm` printed to your terminal.

### To install the latest version of Node.js[​](#to-install-the-latest-version-of-nodejs "Direct link to To install the latest version of Node.js") 

``` 
nvm install latest
```

### To install a specific version of Node.js[​](#to-install-a-specific-version-of-nodejs "Direct link to To install a specific version of Node.js") 

``` 
nvm install <version number>
```

To see all the versions of Node that you can install, run the following command:

``` 
nvm ls-remote
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTguODkzIDEuNWMtLjE4My0uMzEtLjUyLS41LS44ODctLjVzLS43MDMuMTktLjg4Ni41TC4xMzggMTMuNDk5YS45OC45OCAwIDAgMCAwIDEuMDAxYy4xOTMuMzEuNTMuNTAxLjg4Ni41MDFoMTMuOTY0Yy4zNjcgMCAuNzA0LS4xOS44NzctLjVhMS4wMyAxLjAzIDAgMCAwIC4wMS0xLjAwMkw4Ljg5MyAxLjV6bS4xMzMgMTEuNDk3SDYuOTg3di0yLjAwM2gyLjAzOXYyLjAwM3ptMC0zLjAwNEg2Ljk4N1Y1Ljk4N2gyLjAzOXY0LjAwNnoiPjwvcGF0aD48L3N2Zz4=)]warning

You\'ll need to [install yarn](https://yarnpkg.com/getting-started/install) **for each version of Node that you install.**

[Corepack](https://nodejs.org/dist/latest/docs/api/corepack.html) is included with all Node.js \>=16.10 installs, but you must opt-in. To enable it, run the following command:

``` 
corepack enable
```

We also have a doc specifically for [working with yarn](/docs/how-to/using-yarn).

### To use a specific version of Node.js[​](#to-use-a-specific-version-of-nodejs "Direct link to To use a specific version of Node.js") 

``` 
nvm use <version number>
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTcgMi4zYzMuMTQgMCA1LjcgMi41NiA1LjcgNS43cy0yLjU2IDUuNy01LjcgNS43QTUuNzEgNS43MSAwIDAgMSAxLjMgOGMwLTMuMTQgMi41Ni01LjcgNS43LTUuN3pNNyAxQzMuMTQgMSAwIDQuMTQgMCA4czMuMTQgNyA3IDcgNy0zLjE0IDctNy0zLjE0LTctNy03em0xIDNINnY1aDJWNHptMCA2SDZ2Mmgydi0yeiI+PC9wYXRoPjwvc3ZnPg==)]info

Remember: [Redwood has specific Node.js version requirements.](/docs/tutorial/chapter1/prerequisites#nodejs-and-yarn-versions)

### To see all the versions of Node.js that you have installed[​](#to-see-all-the-versions-of-nodejs-that-you-have-installed "Direct link to To see all the versions of Node.js that you have installed") 

``` 
nvm ls
```

### To set the default version of Node.js[​](#to-set-the-default-version-of-nodejs "Direct link to To set the default version of Node.js") 

``` 
nvm alias default <<version number>>
```

### To uninstall a specific version of Node.js[​](#to-uninstall-a-specific-version-of-nodejs "Direct link to To uninstall a specific version of Node.js") 

``` 
nvm uninstall <<version number>>
```

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6Ij48L3BhdGg+PC9nPjwvc3ZnPg==)Edit the latest version of this page](https://github.com/redwoodjs/graphql/blob/main/docs/docs/how-to/using-nvm.md)