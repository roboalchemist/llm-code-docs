# Server API for plugins

A Strapi plugin can interact with both the back end and the [front end](/cms/plugins-development/admin-panel-api) of a Strapi application. The Server API is about the back-end part, i.e. how the plugin interacts with the server part of a Strapi application.

:::prerequisites
You have [created a Strapi plugin](/cms/plugins-development/create-a-plugin).
:::

The Server API includes:

- an [entry file](#entry-file) which export the required interface,
- [lifecycle functions](#lifecycle-functions),
- a [configuration](#configuration) API,
- and the ability to [customize all elements of the back-end server](#backend-customization).

Once you have declared and exported the plugin interface, you will be able to [use the plugin interface](#usage).

:::note
The whole code for the server part of your plugin could live in the `/server/src/index.ts|js` file. However, it's recommended to split the code into different folders, just like the [structure](/cms/plugins-development/plugin-structure) created by the Plugin SDK.
:::

## Entry file

The `/src/server/index.js` file at the root of the plugin folder exports the required interface, with the following parameters available:

| Parameter type         | Available parameters                                                                                                                                                                                           |
| ---------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Lifecycle functions    | <ul><li> [register](#register)</li><li>[bootstrap](#bootstrap)</li><li>[destroy](#destroy)</li></ul>                                                                                                           |
| Configuration          | <ul><li>[config](#configuration) object   </li></ul>                                                                                                                                                                             |
| Backend customizations | <ul><li>[contentTypes](#content-types)</li><li>[routes](#routes)</li><li>[controllers](#controllers)</li><li>[services](#services)</li><li>[policies](#policies)</li><li>[middlewares](#middlewares)</li></ul> |

## Lifecycle functions

<br/>

### register()

This function is called to load the plugin, before the application is [bootstrapped](#bootstrap), in order to register [permissions](/cms/features/users-permissions), the server part of [custom fields](/cms/features/custom-fields#registering-a-custom-field-on-the-server), or database migrations.

**Type**: `Function`

**Example:**

</Tabs>

### bootstrap()

The [bootstrap](/cms/configurations/functions#bootstrap) function is called right after the plugin has [registered](#register).

**Type**: `Function`

**Example:**

</Tabs>

### destroy()

The [destroy](/cms/configurations/functions#destroy) lifecycle function is called to cleanup the plugin (close connections, remove listeners, etc.) when the Strapi instance is destroyed.

**Type**: `Function`

**Example:**

</Tabs>

## Configuration

`config` stores the default plugin configuration. It loads and validates the configuration inputted from the user within the [`./config/plugins.js` configuration file](/cms/configurations/plugins).

**Type**: `Object`

| Parameter   | Type                                           | Description                                                                                                                                              |
| ----------- | ---------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `default`   | Object, or Function that returns an Object | Default plugin configuration, merged with the user configuration                                                                                         |
| `validator` | Function                                       | <ul><li>Checks if the results of merging the default plugin configuration with the user configuration is valid</li><li>Throws errors when the resulting configuration is invalid</li></ul> |

**Example:**

</Tabs>

Once defined, the configuration can be accessed:

- with `strapi.plugin('plugin-name').config('some-key')` for a specific configuration property,
- or with `strapi.config.get('plugin::plugin-name')` for the whole configuration object.

:::tip
Run `yarn strapi console` or `npm run strapi console` to access the strapi object in a live console.
:::

## Backend customization

All elements of the back-end server of Strapi can be customized through a plugin using the Server API.

:::prerequisites
To better understand this section, ensure you have read through the [back-end customization](/cms/backend-customization) documentation of a Strapi application.
:::

### Content-types

An object with the [content-types](/cms/backend-customization/models) the plugin provides.

**Type**: `Object`

:::note
Content-Types keys in the `contentTypes` object should re-use the `singularName` defined in the [`info`](/cms/backend-customization/models#model-information) key of the schema.
:::

**Example:**

</Tabs>

### Routes

An array of [routes](/cms/backend-customization/routes) configuration.

**Type**: `Object[]`

**Examples:**

</Tabs>

</TabItem>

</Tabs>

</TabItem>
</Tabs>

### Controllers

An object with the [controllers](/cms/backend-customization/controllers) the plugin provides.

**Type**: `Object`

**Example:**

</Tabs>

### Services

An object with the [services](/cms/backend-customization/services) the plugin provides.

Services should be functions taking `strapi` as a parameter.

**Type**: `Object`

**Example:**

</Tabs>

### Policies

An object with the [policies](/cms/backend-customization/policies) the plugin provides.

**Type**: `Object`

**Example:**

</Tabs>

### Middlewares

An object with the [middlewares](/cms/configurations/middlewares) the plugin provides.

**Type**: `Object`

**Example:**

</Tabs>

## Usage

Once a plugin is exported and loaded into Strapi, its features are accessible in the code through getters. The Strapi instance (`strapi`) exposes both top-level getters and global getters:

- top-level getters imply chaining functions<br/>(e.g., `strapi.plugin('the-plugin-name').controller('the-controller-name'`),
- global getters are syntactic sugar that allows direct access using a feature's uid<br/>(e.g., `strapi.controller('plugin::plugin-name.controller-name')`).

```js
// Access an API or a plugin controller using a top-level getter 
strapi.api['api-name'].controller('controller-name')
strapi.plugin('plugin-name').controller('controller-name')

// Access an API or a plugin controller using a global getter
strapi.controller('api::api-name.controller-name')
strapi.controller('plugin::plugin-name.controller-name')
```

<details>
<summary> Top-level getter syntax examples</summary>

```js
strapi.plugin('plugin-name').config
strapi.plugin('plugin-name').routes
strapi.plugin('plugin-name').controller('controller-name')
strapi.plugin('plugin-name').service('service-name')
strapi.plugin('plugin-name').contentType('content-type-name')
strapi.plugin('plugin-name').policy('policy-name')
strapi.plugin('plugin-name').middleware('middleware-name')
```

</details>

<details>
<summary> Global getter syntax examples</summary>

```js
strapi.controller('plugin::plugin-name.controller-name');
strapi.service('plugin::plugin-name.service-name');
strapi.contentType('plugin::plugin-name.content-type-name');
strapi.policy('plugin::plugin-name.policy-name');
strapi.middleware('plugin::plugin-name.middleware-name');
```

</details>

:::strapi Document Service API
To interact with the content-types, use the [Document Service API](/cms/api/document-service).
:::