# Source: https://docs.redwoodjs.com/docs/create-redwood-app

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [Reference](/docs/index)
-   [Create Redwood App]

[Version: 8.8]

On this page

<div>

# Create Redwood App

</div>

To get up and running with Redwood, you can use Create Redwood App:

``` 
yarn create redwood-app <your-app-name>
```

## Set up for success[​](#set-up-for-success "Direct link to Set up for success") 

Redwood requires that you\'re running Node version 20 or higher.

If you\'re running Node version 21.0.0 or higher, you can still use Create Redwood App, but it may make your project incompatible with some deploy targets, such as AWS Lambdas.

To see what version of Node you\'re running, you can run the following command in your terminal:

``` 
node -v
```

If you need to update your version of Node or run multiple versions of Node, we recommend installing nvm and have [documentation about how to get up and running.](/docs/how-to/using-nvm)

You also need to have yarn version 1.22.21 or higher installed. To see what version of yarn you\'re running, you can run the following command in your terminal:

``` 
yarn -v
```

To upgrade your version of yarn, [you can refer to the yarn documentation](https://yarnpkg.com/getting-started/install).

## What you can expect[​](#what-you-can-expect "Direct link to What you can expect") 

### Select your preferred language[​](#select-your-preferred-language "Direct link to Select your preferred language") 

Options: TypeScript (default) or JavaScript

If you choose JavaScript, you can always [add TypeScript later](/docs/typescript/introduction#converting-a-javascript-project-to-typescript).

### Do you want to initialize a git repo?[​](#do-you-want-to-initialize-a-git-repo "Direct link to Do you want to initialize a git repo?") 

Options: yes (default) or no

If you mark \"yes\", then it will ask you to **Enter a commit message**. The default message is \"Initial commit.\"

You can always initialize a git repo later and add a commit message by running the following commands in your terminal:

``` 
cd <your-app-name>
git init
git add .
git commit -m "Initial commit"
```

If you\'re new to git, here\'s a recommended playlist on YouTube: [git for Beginners](https://www.youtube.com/playlist?list=PLrz61zkUHJJFmfTgOVL1mBw_NZcgGe882)

### Do you want to run `yarn install`?[​](#do-you-want-to-run-yarn-install "Direct link to do-you-want-to-run-yarn-install") 

Options: yes (default) or no

*NOTE: This prompt will only display if you\'re running yarn, version 1.*

This command will download all of your project\'s dependencies.

If you mark \"no\", you can always run this command later:

``` 
cd <your-app-name>
yarn install
```

## Running the development server[​](#running-the-development-server "Direct link to Running the development server") 

Once the Create Redwood app has finished running, you can start your development server by running the following command:

``` 
cd <your-app-name>
yarn rw dev
```

-   This will start your development server at `http://localhost:8910`.
-   Your API will be available at `http://localhost:8911`.
-   You can visit the Redwood GraphQL Playground at `http://localhost:8911/graphql`.

## Flags[​](#flags "Direct link to Flags") 

You can by pass these prompts by using the following flags:

Flag

Alias

What it does

`--yarn-install`

Run `yarn install`

`--typescript`

`ts`

Set TypeScript as the preferred language (pass `--no-typescript` to use JavaScript)

`--overwrite`

Overwrites the existing directory, if it has the same name

`--git-init`

`git`

Initializes a git repository

`--commit-message "Initial commit"`

`m`

Specifies the initial git commit message

`--yes`

`y`

Automatically select all defaults

For example, here\'s the project with all flags enabled:

``` 
yarn create redwood-app <your-app-name> --typescript --git-init --commit-message "Initial commit" --yarn-install
```

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6Ij48L3BhdGg+PC9nPjwvc3ZnPg==)Edit the latest version of this page](https://github.com/redwoodjs/graphql/blob/main/docs/docs/create-redwood-app.md)