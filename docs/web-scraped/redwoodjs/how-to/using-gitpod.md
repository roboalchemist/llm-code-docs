# Source: https://docs.redwoodjs.com/docs/how-to/using-gitpod

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [How To](/docs/how-to/index)
-   [Using GitPod]

[Version: 8.8]

On this page

<div>

# Using GitPod

</div>

## What is GitPod?[​](#what-is-gitpod "Direct link to What is GitPod?") 

GitPod is a cloud development environment with all the necessary tools and dependencies, allowing you to focus on building your RedwoodJS application without worrying about the setup. Get started quickly and efficiently by launching RedwoodJS inside GitPod!

## Getting Started[​](#getting-started "Direct link to Getting Started") 

Click on the Open in GitPod button:

[![Open in GitPod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/redwoodjs/starter)

# An error occurred. 

Unable to execute JavaScript.

This will launch GitPod and ask you to configure a new workspace. Click continue.

![GitPod Onboarding Screen](https://github.com/redwoodjs/starter/raw/main/images/gitpod-new-workspace.png)

GitPod will then begin to build your workspace. This may take several minutes.

What\'s going on behind the scenes:

-   GitPod is setting up the workspace
-   It installs our recommended VS Code plugins:
    -   [ESLint](https://github.com/redwoodjs/starter/blob/main)
    -   [Git Lens](https://github.com/redwoodjs/starter/blob/main)
    -   [VS Code Language - Babel](https://github.com/redwoodjs/starter/blob/main)
    -   [VS Code Version Lens](https://github.com/redwoodjs/starter#:~:text=VS%20Code%20Version%20Lens)
    -   [Editor Config](https://github.com/redwoodjs/starter#:~:text=Code%20Version%20Lens-,Editor%20Config,-Prisma)
    -   [Prisma](https://github.com/redwoodjs/starter/blob/main)
    -   [VS Code GraphQL](https://github.com/redwoodjs/starter/blob/main)
-   It runs our **Create Redwood App** which will install the latest stable version of Redwood. We\'re setting this project to use TypeScript, however, you can [change it to JavaScript](https://github.com/redwoodjs/starter/blob/main) if you prefer.
-   It runs `yarn install`, adding all the dependencies for the project
-   Changes the database over to Postgres

Once everything is up and running, you can click on the Ports tab:

![GitPod Ports Tab](https://github.com/redwoodjs/starter/raw/main/images/gitpod-ports.png)

You can click on the address or the globe icon to open that particular port in a new tab.

-   Port 5432 is the database. So, if you click on that port, you\'ll probably see a \"Port 5432 Not Found\" error, but it is working! ![GitPod on Port 5432](https://github.com/redwoodjs/starter/raw/main/images/gitpod-port-5432.png)

-   Port 8910 is your frontend ![Port 8910 frontend](https://github.com/redwoodjs/starter/raw/main/images/gitpod-port-8910.png)

-   Port 8911 is your backend and will show you a list of all available functions. If you add `/graphql` to the end of the URL, you should see the GraphQL Playground ![Port 8911 GraphQL Playground](https://github.com/redwoodjs/starter/raw/main/images/gitpod-graphql.png)

## How to Use GitPod[​](#how-to-use-gitpod "Direct link to How to Use GitPod") 

# An error occurred. 

Unable to execute JavaScript.

If you have an existing project, you can still use GitPod:

1.  Take any repository within GitHub and append `gitpod.io/#` to the URL. This will quickly launch a GitPod workspace.
2.  Within the Terminal, run `yarn install` to install all the dependencies

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6Ij48L3BhdGg+PC9nPjwvc3ZnPg==)Edit the latest version of this page](https://github.com/redwoodjs/graphql/blob/main/docs/docs/how-to/using-gitpod.md)