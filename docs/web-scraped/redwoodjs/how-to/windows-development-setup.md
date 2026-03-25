# Source: https://docs.redwoodjs.com/docs/how-to/windows-development-setup

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [How To](/docs/how-to/index)
-   [Windows Development Setup]

[Version: 8.8]

On this page

<div>

# Windows Development Setup

</div>

This guide provides a simple setup to start developing a RedwoodJS project on Windows. Many setup options exist, but this aims to make getting started as easy as possible. This is the recommended setup unless you have experience with some other shell, like PowerShell.

> If you\'re interested in using the Windows Subsystem for Linux instead, there is a [community guide for that](https://community.redwoodjs.com/t/windows-subsystem-for-linux-setup/2439).

### Git Bash[​](#git-bash "Direct link to Git Bash") 

Download the latest release of [**Git for Windows**](https://git-scm.com/download/win) and install it. When installing Git, you can add the icon on the Desktop and add Git Bash profile to Windows Terminal if you use it, but it is optional.

![1-git_components.png](https://user-images.githubusercontent.com/18013532/146685298-b12ed1a5-fe99-4286-ab12-69cf0a7be139.png)

Next, set VS Code as Git default editor (or pick any other editor you\'re comfortable with).

![2-git_editor.png](https://user-images.githubusercontent.com/18013532/146685299-0e067554-a5a8-46b9-91ac-ffcd6f738b80.png)

For all other steps, we recommended keeping the default choices.

### Node.js environment (and npm)[​](#nodejs-environment-and-npm "Direct link to Node.js environment (and npm)") 

We recommend you install the latest `nvm-setup.zip` of [**nvm-windows**](https://github.com/coreybutler/nvm-windows/releases) to manage multiple version installations of Node.js. When the installation of nvm is complete, run Git Bash as administrator to install Node with npm.

![3-git_run_as_admin.png](https://user-images.githubusercontent.com/18013532/146685300-1762a00a-26cb-4f8b-b480-c6aba4e26b89.png)

Redwood uses the LTS version of Node. To install, run the following commands inside the terminal:

``` 
$ nvm install lts --latest-npm
// installs latest LTS and npm
e.g. 16.13.1 for the following examples
$ nvm use 16.13.1
```

### Yarn[​](#yarn "Direct link to Yarn") 

Now you have both Node and npm installed! Redwood also uses yarn, which you can now install using npm:

``` 
npm install -g yarn
```

*Example of Node.js, npm, and Yarn installation steps*

![4-install_yarn.png](https://user-images.githubusercontent.com/18013532/146685297-b361ebea-7229-4d8c-bc90-472773d06816.png)

## Congrats\![​](#congrats "Direct link to Congrats!") 

You now have everything ready to build your Redwood app.

Next, you should start the amazing [**Redwood Tutorial**](/docs/tutorial/chapter1/installation) to learn how to use the framework.

Or run `yarn create redwood-app myApp` to get started with a new project.

## Troubleshooting[​](#troubleshooting "Direct link to Troubleshooting") 

### Beware case-insensitivity[​](#beware-case-insensitivity "Direct link to Beware case-insensitivity") 

On Windows Git Bash, `cd myapp` and `cd myApp` will select the same directory because Windows is case-insensitive. But make sure you type the original capitalization to avoid strange errors in your Redwood project.

### Microsoft Visual C++ Redistributable[​](#microsoft-visual-c-redistributable "Direct link to Microsoft Visual C++ Redistributable") 

If your machine doesn\'t have Microsoft Visual C++ Redistributable, then you need to install it from [here](https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist?view=msvc-170#visual-studio-2015-2017-2019-and-2022).

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6Ij48L3BhdGg+PC9nPjwvc3ZnPg==)Edit the latest version of this page](https://github.com/redwoodjs/graphql/blob/main/docs/docs/how-to/windows-development-setup.md)