# Source: https://docs.redwoodjs.com/docs/project-configuration-dev-test-build

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [Reference](/docs/index)
-   [Project Configuration]

[Version: 8.8]

On this page

<div>

# Project Configuration: Dev, Test, Build

</div>

## Babel[​](#babel "Direct link to Babel") 

Out of the box Redwood configures [Babel](https://babeljs.io/) so that you can write modern JavaScript and TypeScript without needing to worry about transpilation at all. GraphQL tags, JSX, SVG imports---all of it\'s handled for you.

For those well-versed in Babel config, you can find Redwood\'s in [\@redwoodjs/internal](https://github.com/redwoodjs/redwood/tree/main/packages/internal/src/build/babel).

### Configuring Babel[​](#configuring-babel "Direct link to Configuring Babel") 

For most projects, you won\'t need to configure Babel at all, but if you need to you can configure each side (web, api) individually using side-specific `babel.config.js` files.

> **Heads up**
>
> `.babelrc` files are ignored. You have to put your custom config in the appropriate side\'s `babel.config.js`: `web/babel.config.js` for web and `api/babel.config.js` for api.

Let\'s go over an example.

#### Example: Adding Emotion[​](#example-adding-emotion "Direct link to Example: Adding Emotion") 

Let\'s say we want to add the styling library [emotion](https://emotion.sh), which requires adding a Babel plugin.

1.  Create a `babel.config.js` file in `web`:

``` 
touch web/babel.config.js
```

\

2.  Add the `@emotion/babel-plugin` as a dependency:

``` 
yarn workspace web add --dev @emotion/babel-plugin
```

\

3.  Add the plugin to `web/babel.config.js`:

web/babel.config.js

``` 
module.exports = 

// ℹ️ Notice how we don't need the `extends` property
```

That\'s it! Now your custom web-side Babel config will be merged with Redwood\'s.

## Jest[​](#jest "Direct link to Jest") 

Redwood uses [Jest](https://jestjs.io/) for testing. Let\'s take a peek at how it\'s all configured.

At the root of your project is `jest.config.js`. It should look like this:

jest.config.js

``` 
module.exports = /jest.config.js'],
}
```

This just tells Jest that the actual config files sit in each side, allowing Jest to pick up the individual settings for each. `rootDir` also makes sure that if you\'re running Jest with the `--collectCoverage` flag, it\'ll produce the report in the root directory.

#### Web Jest Config[​](#web-jest-config "Direct link to Web Jest Config") 

The web side\'s configuration sits in `./web/jest.config.js`

``` 
const config = 

module.exports = config
```

> You can always see Redwood\'s latest configuration templates in the [create-redwood-app package](https://github.com/redwoodjs/redwood/blob/main/packages/create-redwood-app/templates/ts/web/jest.config.js).

The preset includes all the setup required to test everything that\'s going on in web: rendering React components and transforming JSX, automatically mocking Cells, transpiling with Babel, mocking the Router and the GraphQL client---the list goes on! You can find all the details in the [source](https://github.com/redwoodjs/redwood/blob/main/packages/testing/config/jest/web/jest-preset.js).

#### Api Side Config[​](#api-side-config "Direct link to Api Side Config") 

The api side is configured similarly, with the configuration sitting in `./api/jest.config.js`. But the api preset is slightly different in that:

-   it\'s configured to run tests serially (because Scenarios seed your test database)
-   it has setup code to make sure your database is 1) seeded before running tests 2) reset between Scenarios

You can find all the details in the [source](https://github.com/redwoodjs/redwood/blob/main/packages/testing/config/jest/api/jest-preset.js).

## GraphQL Codegen[​](#graphql-codegen "Direct link to GraphQL Codegen") 

You can customize the types that Redwood generates from your project too! This is documented in a bit more detail in the [Generated Types](/docs/typescript/generated-types#customising-codegen-config) doc.

## Debug configurations[​](#debug-configurations "Direct link to Debug configurations") 

### Dev Server[​](#dev-server "Direct link to Dev Server") 

The `yarn rw dev` command is configured by default to open a browser and a debugger on the port `18911` and your redwood app ships with several default configurations to debug with VSCode.

#### Customizing the configuration[​](#customizing-the-configuration "Direct link to Customizing the configuration") 

**a) Using the redwood.toml**

Add/change the `debugPort` or `open` under your api settings

redwood.toml

``` 
[web]
  # .
[api]
  # .
  debugPort = 18911 # change me!
[browser]
  open = true # change me!
```

**b) Pass a flag to `rw dev` command**

You can also pass a flag when you launch your dev servers, for example:

``` 
yarn rw dev --debugPort 75028
```

The flag passed in the CLI will always take precedence over your setting in the `redwood.toml`

Just remember to also change the port you are attaching to in your `./vscode/launch.json`

### API and Web Debuggers[​](#api-and-web-debuggers "Direct link to API and Web Debuggers") 

Simply run your dev server, then attach the debugger from the \"run and debug\" panel. Quick demo below:

### Compound Debugger[​](#compound-debugger "Direct link to Compound Debugger") 

The compound configuration is a combination of the dev, api and web configurations. It allows you to start all debugging configurations at once, facilitating simultaneous debugging of server and client-side code.

\

> **ℹ️ Tip: Can\'t see the debug configurations?** In VSCode
>
> You can grab the latest launch.json from the Redwood template [here](https://github.com/redwoodjs/redwood/blob/main/packages/create-redwood-app/templates/ts/.vscode/launch.json). Copy the contents into your project\'s `.vscode/launch.json`

## Ignoring the `.yarn` folder[​](#ignoring-the-yarn-folder "Direct link to ignoring-the-yarn-folder") 

The `.yarn` folder contains the most recent Yarn executable that Redwood supports which is the [recommended way](https://github.com/yarnpkg/yarn/issues/7741) to ensure things run smoothly for everyone. From VSCode\'s perspective, this of course is just another folder containing code, so it will

1.  include its contents in project-wide, full-text searches
2.  display it in the file browser
3.  watch its contents for changes

... which, depending on your personal preference, is something you may not need or want.

Fortunately, all these aspects are configurable via VSCode\'s `settings.json`. You have the choice of making these changes to your local Redwood project\'s configuration found in `.vscode/settings.json` or globally (so they apply to other projects as well). For global changes, hit [F1] or [Ctrl]+[Shift]+[P] (that\'s [⌘]+[Shift]+[P] if you\'re on Mac) and search for \"Preferences: Open User Settings (JSON)\".

Note that the local workspace configuration always overrules your user settings. The VSCode website [provides an extensive explanation](https://code.visualstudio.com/docs/getstarted/settings#_settings-precedence) on how its config inheritance works. It also has a complete reference of [all available settings and their defaults](https://code.visualstudio.com/docs/getstarted/settings#_default-settings).

### Excluding a folder from search results only[​](#excluding-a-folder-from-search-results-only "Direct link to Excluding a folder from search results only") 

Adding the following would exclude any `.yarn` folder encountered anywhere in the project (that\'s what the `**` [glob pattern](https://code.visualstudio.com/docs/editor/codebasics#_advanced-search-options) does) from search results:

``` 
  "search.exclude": 
```

### Excluding a folder from the file browser and searching[​](#excluding-a-folder-from-the-file-browser-and-searching "Direct link to Excluding a folder from the file browser and searching") 

``` 
  "files.exclude": 
```

This setting also excludes all matching folders and files from search results, so there\'s no point in adding a `search.exclude` setting separately.

Don\'t worry: this setting won\'t influence change detection in your \"Source Control\" tab---that would be managed via `.gitignore`.

### Excluding a folder from watching[​](#excluding-a-folder-from-watching "Direct link to Excluding a folder from watching") 

``` 
  "files.watcherExclude": 
```

This setting works independently of the ones above and so it needs to be added separately. It\'s important to note that files or folders matched by this setting will no longer immediately appear (or disappear):

-   from existing search results (but as soon as you search again or change the search term, they\'ll be discovered)
-   in your \"Source Control\" tab, unless you hit the \"Refresh\" button

Admittedly, the `.yarn` folder won\'t change that often, so this may not be the best example. But we thought we\'d share this technique with you so that you\'d know how to apply it to any folders that you know change very often, and how to tell VSCode not to bother wasting any CPU cycles on them.

## Trailing whitespace[​](#trailing-whitespace "Direct link to Trailing whitespace") 

If you\'re using VS Code, or another editor that supports [EditorConfig](https://editorconfig.org), trailing whitespace will be trimmed in source files, but preserved in html, markdown and mjml files when saving.

This behavior is controlled by `.vscode/settings` or `.editorconfig` depending on your editor.

In JavaScript and TypeScript files trailing whitespace has no significance, but for html, markdown and mjml it does. That\'s why the behavior is different for those files. If you don\'t like the default behavior Redwood has configured for you, you\'re free to change the settings in those two files.

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6Ij48L3BhdGg+PC9nPjwvc3ZnPg==)Edit the latest version of this page](https://github.com/redwoodjs/graphql/blob/main/docs/docs/project-configuration-dev-test-build.mdx)