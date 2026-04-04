# Plugin creation

There are many ways to create a Strapi 5 plugin, but the fastest and recommended way is to use the Plugin SDK.

The Plugin SDK is a set of commands orientated around developing plugins to use them as local plugins or to publish them on NPM and/or submit them to the Marketplace.

With the Plugin SDK, you do not need to set up a Strapi project before creating a plugin.

The present guide covers creating a plugin from scratch, linking it to an existing Strapi project, and publishing the plugin. If you already have an existing plugin, you can instead retrofit the plugin setup to utilise the Plugin SDK commands (please refer to the [Plugin SDK reference](/cms/plugins-development/plugin-sdk) for a full list of available commands).

:::note
This guide assumes you want to develop a plugin external to your Strapi project. However, the steps largely remain the same if you want to develop a plugin within your existing project. If you are not [using a monorepo](#monorepo) the steps are exactly the same.
:::

:::prerequisites

</Tabs>

The path `my-strapi-plugin` can be replaced with whatever you want to call your plugin, including the path to where it should be created (e.g., `code/strapi-plugins/my-new-strapi-plugin`).

You will be ran through a series of prompts to help you setup your plugin. If you selected yes to all options the final structure will be similar to the default [plugin structure](/cms/plugins-development/plugin-structure).

### Linking the plugin to your project

In order to test your plugin during its development, the recommended approach is to link it to a Strapi project.

Linking your plugin to a project is done with the `watch:link` command. The command will output explanations on how to link your plugin to a Strapi project.

In a new terminal window, run the following commands:

</Tabs>

:::note
In the above examples we use the name of the plugin (`my-strapi-plugin`) when linking it to the project. This is the name of the package, not the name of the folder.
:::

Because this plugin is installed via `node_modules` you won't need to explicity add it to your `plugins` [configuration file](/cms/configurations/plugins), so running the [`develop command`](/cms/cli#strapi-develop) to start your Strapi project will automatically pick up your plugin.

Now that your plugin is linked to a project, run `yarn develop` or `npm run develop` to start the Strapi application.

You are now ready to develop your plugin how you see fit! If you are making server changes, you will need to restart your server for them to take effect.

### Building the plugin for publishing

When you are ready to publish your plugin, you will need to build it. To do this, run the following command:

</Tabs>

The above commands will not only build the plugin, but also verify that the output is valid and ready to be published. You can then publish your plugin to NPM as you would any other package.

## Working with the Plugin SDK in a monorepo environment {#monorepo}

If you are working with a monorepo environment to develop your plugin, you don't need to use the `watch:link` command because the monorepo workspace setup will handle the symlink. You can use the `watch` command instead.

However, if you are writing admin code, you might add an `alias` that targets the source code of your plugin to make it easier to work with within the context of the admin panel:

```ts

  config.resolve.alias = {
    ...config.resolve.alias,
    'my-strapi-plugin': path.resolve(
      __dirname,
      // We've assumed the plugin is local.
      '../plugins/my-strapi-plugin/admin/src'
    ),
  };

  return config;
};
```

:::caution
Because the server looks at the `server/src/index.ts|js` file to import your plugin code, you must use the `watch` command otherwise the code will not be transpiled and the server will not be able to find your plugin.
:::

### Configuration with a local plugin

Since the Plugin SDK is primarily designed for developing plugins, not locally, the configuration needs to be adjusted manually for local plugins.

When developing your plugin locally (using `@strapi/sdk-plugin`), your plugins configuration file looks like in the following example:

```js title="/config/plugins.js|ts"
myplugin: {
  enabled: true,
  resolve: `./src/plugins/local-plugin`,
},
```

However, this setup can sometimes lead to errors such as the following:

```js
Error: 'X must be used within StrapiApp';
```

This error often occurs when your plugin attempts to import core Strapi functionality, for example using:

```js

```

To resolve the issue, remove `@strapi/strapi` as a dev dependency from your plugin. This ensures that your plugin uses the same instance of Strapi’s core modules as the main application, preventing conflicts and the associated errors.

## Setting a local plugin in a monorepo environment without the Plugin SDK

In a monorepo, you can configure your local plugin without using the Plugin SDK by adding 2 entry point files at the root of your plugin:

- server entry point: `strapi-server.js|ts`
- admin entry point: `strapi-admin.js|ts`

### Server entry point

The server entry point file initializes your plugin’s server-side functionalities. The expected structure for `strapi-server.js` (or its TypeScript variant) is:

```js
module.exports = () => {
  return {
    register,
    config,
    controllers,
    contentTypes,
    routes,
  };
};
```

Here, you export a function that returns your plugin's core components such as controllers, routes, and configuration. For more details, please refer to the [Server API reference](/cms/plugins-development/server-api).

### Admin entry point

The admin entry point file sets up your plugin within the Strapi admin panel. The expected structure for `strapi-admin.js` (or its TypeScript variant) is:

```js

  register(app) {},
  bootstrap() {},
  registerTrads({ locales }) {},
};
```

This object includes methods to register your plugin with the admin application, perform bootstrapping actions, and handle translations. For more details, please refer to the [Admin Panel API reference](/cms/plugins-development/admin-panel-api).

:::tip
For a complete example of how to structure your local plugin in a monorepo environment, please check out our .
:::