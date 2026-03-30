# Source: https://docs.redwoodjs.com/docs/typescript/introduction

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [Reference](/docs/index)
-   [TypeScript](/docs/typescript/index)
-   [Introduction]

[Version: 8.8]

On this page

<div>

# TypeScript in Redwood

</div>

Redwood comes with full TypeScript support, and you don\'t have to give up any of the conveniences that Redwood offers to enjoy all the benefits of a type-safe codebase.

## Getting Started[​](#getting-started "Direct link to Getting Started") 

### Starting a Redwood Project in TypeScript[​](#starting-a-redwood-project-in-typescript "Direct link to Starting a Redwood Project in TypeScript") 

You can use the `--typescript` option on `yarn create redwood-app` to use TypeScript from the start:

``` 
yarn create redwood-app my-redwood-app --typescript
```

### Converting a JavaScript Project to TypeScript[​](#converting-a-javascript-project-to-typescript "Direct link to Converting a JavaScript Project to TypeScript") 

Started your project in JavaScript but want to switch to TypeScript? Start by using the `tsconfig` setup command:

``` 
yarn rw setup tsconfig
```

This adds `tsconfig.json` files to both the web and the api side, telling VSCode that this\'s a TypeScript project. (You can go ahead and remove the `jsconfig.json` files from both sides now.)

You don\'t need to convert all your JavaScript files to TypeScript right away. In fact, you probably shouldn\'t. Do it incrementally. Start by renaming your files from `.js` to `.ts`. (Or, if they have a React component, `.tsx`.)

## Core Concepts[​](#core-concepts "Direct link to Core Concepts") 

### 1. Automatic types[​](#1-automatic-types "Direct link to 1. Automatic types") 

When you\'re developing in TypeScript, the Redwood CLI is your trusted companion---focus on writing code and it\'ll generate as many of the types as it can. When you run `yarn rw dev`, the CLI watches files for changes so that it can generate types. (More on this in the [Generated Types](/docs/typescript/generated-types) doc.)

But let\'s say that you don\'t have the dev server running, and are just coding and notice missing types. You can always run `yarn rw g types` to make sure you have all the types you need.

### 2. Use generators to learn about available utility types[​](#2-use-generators-to-learn-about-available-utility-types "Direct link to 2. Use generators to learn about available utility types") 

Let\'s say you generate a Cell using the command `yarn rw g cell Post`. If your project is in TypeScript, the generated files will contain a bunch of utility types (imported from `@redwoodjs/web`), as well as types specific to your project (imported from `types/graphql`). You don\'t need to learn all the utility types up front, but they\'re documented in detail in the [Utility Types](/docs/typescript/utility-types) doc when you\'re ready.

### 3. Redwood won\'t force you to type everything[​](#3-redwood-wont-force-you-to-type-everything "Direct link to 3. Redwood won't force you to type everything") 

The Redwood philosophy is to keep things as simple as possible at first. Redwood generates as much as possible, avoids forcing you to type every little detail, and doesn\'t have [strict mode](https://www.typescriptlang.org/tsconfig#strict) on by default. Where needed (e.g. the [`DbAuthHandler`](/docs/typescript/utility-types#dbauthhandleroptions)) you can make use of generics to be more specific with your types.

But if you\'re comfortable with TypeScript and want that extra level of safety, take a look at our [Strict Mode](/docs/typescript/strict-mode) doc.

## A Few Useful Tips[​](#a-few-useful-tips "Direct link to A Few Useful Tips") 

### Sharing Types between Sides[​](#sharing-types-between-sides "Direct link to Sharing Types between Sides") 

To share types between sides:

1.  Put them in a directory called `types` at the root of your project (you may have to create this directory)
2.  Restart your editor\'s TypeScript server. In VSCode, you can do this by running the \"TypeScript: Restart TS server\" command via the command palette (make sure you\'re in a `.js` or `.ts` file)

### Running Type Checks[​](#running-type-checks "Direct link to Running Type Checks") 

Behind the scenes, Redwood actually uses Babel to transpile TypeScript. This\'s why you\'re able to convert your project from JavaScript to TypeScript incrementally, but it also means that, strictly speaking, dev and build don\'t care about what the TypeScript compiler has to say.

That\'s where the `type-check` command comes in:

``` 
yarn rw type-check
```

This runs `tsc` on your project and ensures that all the necessary generated types are generated first. Checkout the [CLI reference for type-check](/docs/cli-commands#type-check)

### Using Alias Paths[​](#using-alias-paths "Direct link to Using Alias Paths") 

Alias paths are a mechanism that allows you to define custom shortcuts or aliases for import statements in your code. Instead of using relative or absolute paths to import modules or files, you can use these aliases to make your imports cleaner and more concise.

Redwood comes with a great starting point by aliasing the `src` directory, but you can take this further by configuring your `tsconfig.json` file, your import paths could go from:

``` 
// this really long path
import  from 'src/components/modules/admin/common/ui/CustomModal'

// to this nicer one!
import  from '@adminUI/CustomModal'
```

Add you custom `@adminUI` alias to your `tsconfig.json` file:

``` 

  }
...
}
```

You might have noticed the `"../.redwood/types/mirror/web/src/components/modules/admin/common/ui/*"` path. I\'m glad you did!

When you build your project redwood will create a set of directories or a virtual directory called`.redwood`, [read more about this typescript feature here](https://www.typescriptlang.org/docs/handbook/module-resolution.html#virtual-directories-with-rootdirs). This directory contains types for te Cells, so there is no need for us to specify an index file.

When you combine those two paths `.src/...` and `./.redwood/...` under an alias you can have shorter and cleaner import paths:

``` 
// Instead of this 🥵
import  from 'src/components/modules/admin/common/ui/CustomModal/CustomModal'

// they could look like this ✨
import  from '@adminUI/CustomModal'
```

#### Some benefits of using alias paths are[​](#some-benefits-of-using-alias-paths-are "Direct link to Some benefits of using alias paths are") 

1.  **Improved code readability**, by abstracting complex directory hierarchies, and having meaningful names for your imports.
2.  **Code maintainability**, aliases allow you to decouple your code from the file structure and more easily move files around, as they are not tied to the longer path.
3.  **Reduce boilerplate**, no more `../../src/components/modules/admin/common/ui/` 😮‍💨

When you start writing tests for components that contain alias paths, you will need to add the following to your Jest configuration in `jest.config.js`:

``` 
const config = ,
}

module.exports = config
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTcgMi4zYzMuMTQgMCA1LjcgMi41NiA1LjcgNS43cy0yLjU2IDUuNy01LjcgNS43QTUuNzEgNS43MSAwIDAgMSAxLjMgOGMwLTMuMTQgMi41Ni01LjcgNS43LTUuN3pNNyAxQzMuMTQgMSAwIDQuMTQgMCA4czMuMTQgNyA3IDcgNy0zLjE0IDctNy0zLjE0LTctNy03em0xIDNINnY1aDJWNHptMCA2SDZ2Mmgydi0yeiI+PC9wYXRoPjwvc3ZnPg==)]info

There are 3 `jest.config.js` files within a Redwood project. There\'s one inside the `web` directory, one inside the `api` directory, and one at the root of the project. Since the alias I created is used within the `web` directory, I added the `moduleNameMapper` to the `jest.config.js` file within the `web` directory.

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6Ij48L3BhdGg+PC9nPjwvc3ZnPg==)Edit the latest version of this page](https://github.com/redwoodjs/graphql/blob/main/docs/docs/typescript/introduction.md)