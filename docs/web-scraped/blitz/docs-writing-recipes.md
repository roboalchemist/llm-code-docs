# Source: https://blitzjs.com/docs/writing-recipes

Title: Writing Your Own Recipes - Blitz.js

URL Source: https://blitzjs.com/docs/writing-recipes

Markdown Content:
The incredible power of Blitz Recipes isn't limited to the official recipes in the Blitz repo. The API for building recipes is a public API (although one that is subject to change) exposed via the [`blitz`](https://npm.im/blitz) package from `blitz/installer`, which can be installed into your own scripts to write a completely custom recipe. Combined with the power of [`jscodeshift`](https://github.com/facebook/jscodeshift) for transforming existing files, fully automated code migrations are first-class citizens in the Blitz ecosystem.

### [](https://blitzjs.com/docs/writing-recipes#setup)Setup

To author your own recipe, you'll want to create a new package and install a couple of dependencies. You'll only need the `jscodeshift` dependencies if you're using a **transform** step to modify an existing file. If you're only creating new files or adding dependencies you'll only need `blitz`.

If you're going to be writing tests for your recipe you'll need a build and test setup. We recommend [`tsdx`](https://github.com/jaredpalmer/tsdx) and Vitest for building and running tests.

The Recipe API all revolves around the `RecipeBuilder` factory. Blitz assumes that the file referenced in the `main` field of your `package.json` has a recipe as its default export, so we can go ahead and set that up.

### [](https://blitzjs.com/docs/writing-recipes#adding-metadata)Adding Metadata

In addition to the actual steps of the recipe, we require that the developer supply metadata about the recipe. This allows us to display some information to the user about what they're installing, as well as where they can look for support if they need it.

This is a pretty good start, and is actually all we need to create an executable recipe that a user can run via `blitz install`. However, it's not very useful because we don't actually have any steps for the installer framework to execute. Keep reading to learn about the different actions we can execute.

### [](https://blitzjs.com/docs/writing-recipes#common-api)Common API

Each action type has a shared interface for defining a "step" in the recipe. This ensures consistency in the user experience and enables us to provide a pleasant installation experience. Each step that gets added must have a string ID that's used to internally track the progress of the installation, a display name, and an explanation for what the step is doing.

Eventually we expect to provide hooks into the recipe lifecycle, making some of the metadata like `stepId` critical.

### [](https://blitzjs.com/docs/writing-recipes#adding-dependencies)Adding Dependencies

The first action we can take is adding dependencies to the user's application. This step type will automatically detect whether the user is using `yarn` or `npm` and use the proper tool. The configuration is very straightforward — it accepts a list of packages, their versions, and whether or not they should be installed as a `devDependency`.

### [](https://blitzjs.com/docs/writing-recipes#adding-files)Adding files

One incredibly powerful part of recipes is the ability to generate files from templates.

We use a custom templating language that's natural to both read and write. [Read our template documentation to learn how to write templates](https://blitzjs.com/docs/templates).

By supplying the `templateValues` configuration, you can either supply a hard-coded object for values to interpolate in the template or a function that returns an object. The function will be passed any additional arguments passed to `blitz install` (e.g. `blitz install myrecipe --someConfig=false`). The template files can go anywhere in your recipe's file structure, you supply the path as a part of the recipe definition.

### [](https://blitzjs.com/docs/writing-recipes#modifying-existing-files)Modifying existing files

Arguably the most powerful part of Blitz recipes, using JSCodeShift you can write a transform that will modify an existing file. The transform function is passed the AST representing the selected file, an object for building new nodes, and an object to assist with typechecking and assertions on nodes. [ASTExplorer](https://astexplorer.net/) is a great place to get familiar with the AST structures and to play around with transforms. For best results, use the `@babel/parser` for the parser setting, and `jscodeshift` for the transform setting.

Blitz supplies some predefined transforms for you for the most common cases, but you can always write a custom transform to modify any JavaScript file you want. We also provide a convenience utility for accessing common files like `_app.tsx` or `next.config.js`. If the file path is a glob pattern, the installer process will prompt the user to select a file matching the pattern.

Because transforms are self-contained functions that execute on ASTs, you can actually unit test this part of your installer, which is incredibly helpful for reliability. Using `jscodeshift` directly along with snapshot testing, the tests are quick to write:

#### Modifying Non-JS files

Not all modifications can be performed using `jscodeshift`. For any other transformations, you can use `transformPlain`:

This step would append "Paul Plain was here!" to the user's README.md

#### Creating a custom message

Sometimes you need to print a simple message, or give some instructions, you can achieve that with `printMessage`

This step would print "If you like this recipe, consider helping out!" to terminal and wait for the user to go to the next step.

#### Custom step icons

If you want to customize your recipe even further, you can pass an optional `successIcon` param to your steps.

#### Modifying Prisma schemas

A lot of recipes may need to add or modify models in the schema.prisma file in order to apply the recipe's effects. You can attempt to manipulate the schema using plain string transformations in `transformPlain`, but a lot of recipes may require the ability to query something about the schema first. For example, to determine the model on the other end of a [Relation](https://www.prisma.io/docs/concepts/components/prisma-schema/relations/), or to detect if a field already exists.

For your convenience, there are several pre-written utilities for common schema modifications:

##### Create an Enum

##### Add a Field to a Model

##### Create a Generator

##### Create a Model

##### Add an Attribute such as an Index to a Model

##### Set the schema's Datasource

Since a prisma schema can only have one data source, there is no "add" utility, this will replace the schema's current data source.

##### Custom Schema Transformations with produceSchema

If the provided helpers aren't flexible enough for your recipe, you can use the `produceSchema` utility function to parse the prisma schema file and apply custom transformations. It will convert the schema into a JSON object format that you can modify using JavaScript, then print the schema (with your changes applied) back out to a string. All of the above helpers are implemented using `produceSchema`.

It is a best practice for schema transformations to be idempotent, meaning that the function should not attempt to make a change to the schema if that change already has been made. For instance, do not add a field to a model if that field already exists.

To see how the schema file is parsed, [click here](https://github.com/MrLeebo/prisma-ast).

### [](https://blitzjs.com/docs/writing-recipes#modifying-next-config)Modifying Next config

Some recipes may require modifying an existing Next.js config file. We are fortunate enough to be able to use the `paths` provided by the `blitz/installer` module. You can pass this into your `singleFileSearch` and use `jscodeshift` to modify it.

#### Transforming the config

The `transformNextConfig` function can be imported from the `blitz/installer` module. It looks for the configuration object and lets you modify it. It takes a `program` as an argument, and returns helper functions to use.

#### Wrapping the config

There are cases when you want to wrap the configuration object with another function, like this:

The `wrapConfig` function can be accessed from `transformNextConfig()`. It looks for `withBlitz()` and wraps whatever's inside with the name of the function you supply. Note that you still need to create the require statement - you can use `transformNextConfig(program).addRequireStatement(identifier, packageName)` for this.

#### [](https://blitzjs.com/docs/writing-recipes#adding-blitz-middleware)Adding a middleware

Using the transform function `addBlitzMiddleware` you can add new middleware from a recipe.

The `addBlitzMiddleware` function can be imported from the `blitzjs/installer` module.

This function takes two arguments `program` and `middleware`. `program` being the jscodeshift object we are modifying, and `middleware` being a function we want to add as middleware.

Using a transformation step, we can take advantage of `singleFileSearch`, construct our middleware, and add it.

In this case, the resulting middleware is added to your blitz server file:

### [](https://blitzjs.com/docs/writing-recipes#wrap-app-with-provider)Wrap _app with a provider component

You may want to modify the user's `_app` page and wrap whatever is in the return statement:

`wrapAppWithProvider` is exported from `blitz/installer` and requires `program`&`element` (being the name of the jsx component). The function searches for `MyApp` then wraps whatever is returned with a JSX component identified by the element string passed.

### [](https://blitzjs.com/docs/writing-recipes#modifying-babel-config)Modifying Babel config

Some recipes may require modifying the existing Babel config file. We are fortunate enough to be able to use the `paths` provided by the `blitz/installer`. You can pass this into your `singleFileSearch` and use `jscodeshift` to modify it.

`blitz/installer` provides two transformers: `addBabelPlugin` and `addBabelPreset`. Both take the `program` and the plugin/preset. You don't need to worry about jscodeshift stuff, you only need to provide a valid JSON object and it will be transformed. This argument has to be either the name of the plugin/preset (as a string) or a array with two elements: the name of the plugin/preset and its configuration.

### [](https://blitzjs.com/docs/writing-recipes#running-an-external-command)Running an external command

In case you have a recipe which should run an external command like `blitz prisma generate`, you can use `addRunCommandStep`.

Example usage:

### [](https://blitzjs.com/docs/writing-recipes#publishing)Publishing

That's all you need to build a recipe! At this point, you can commit and push up to GitHub, and your recipe is available to the world. Users can install your recipe by passing your full repository name to `blitz install` - for example:

### [](https://blitzjs.com/docs/writing-recipes#testing-locally)Testing locally

To test your recipe locally without publishing it you can run
