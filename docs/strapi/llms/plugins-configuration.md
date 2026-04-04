# Plugins configuration

Plugin configurations are stored in `/config/plugins.js|ts` (see [project structure](/cms/project-structure)). Each plugin can be configured with the following available parameters:

| Parameter                  | Description                                                                                                                                                            | Type    |
| -------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| `enabled`                  | Enable (`true`) or disable (`false`) an installed plugin                                                                                                               | Boolean |
| `config`<br/><br/>_Optional_ | Used to override default plugin configuration ([defined in strapi-server.js](/cms/plugins-development/server-api#configuration)) | Object  |
| `resolve`<br/> _Optional, only required for local plugins_             | Path to the plugin's folder                                                                                                                                            | String  |

:::note
Some features of Strapi are provided by plugins and the following plugins can also have specific configuration options: the [GraphQL](/cms/plugins/graphql#code-based-configuration) plugin, the [Upload](/cms/features/media-library#available-options) package which powers the Media Library, and [Users & Permissions](/cms/features/users-permissions#code-based-configuration).
:::

**Basic example custom configuration for plugins:**

</Tabs>

:::tip
If no specific configuration is required, a plugin can also be declared with the shorthand syntax `'plugin-name': true`.
:::