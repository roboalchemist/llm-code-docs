# Source: https://docs.api7.ai/enterprise/best-practices/custom-plugin.md

# Source: https://docs.api7.ai/enterprise/3.2.16.7/best-practices/custom-plugin.md

# Source: https://docs.api7.ai/enterprise/3.2.16.6/best-practices/custom-plugin.md

# Source: https://docs.api7.ai/enterprise/3.2.16.5/best-practices/custom-plugin.md

# Source: https://docs.api7.ai/enterprise/3.2.16.4.1/best-practices/custom-plugin.md

# Source: https://docs.api7.ai/enterprise/3.2.15.2.1/best-practices/custom-plugin.md

# Source: https://docs.api7.ai/enterprise/3.2.14.6/best-practices/custom-plugin.md

# Source: https://docs.api7.ai/enterprise/3.8.x/best-practices/custom-plugin.md

# Source: https://docs.api7.ai/enterprise/3.7.x/best-practices/custom-plugin.md

# Source: https://docs.api7.ai/enterprise/3.6.x/best-practices/custom-plugin.md

# Source: https://docs.api7.ai/enterprise/3.5.x/best-practices/custom-plugin.md

# Source: https://docs.api7.ai/enterprise/3.4.x/best-practices/custom-plugin.md

# Source: https://docs.api7.ai/enterprise/3.3.x/best-practices/custom-plugin.md

# Add Custom Plugin

One of the key features of API7 Gateway is its extensibility through plugins. In addition to a wide range of existing plugins, API7 Gateway also allows you to build custom plugins to add extra functionalities and manage API traffic with custom flow. Oftentimes, you use Lua programming language to implement new plugins. API7 Gateway processes requests in phases and the relevant plugin logics get executed in each phase during the routing of requests.

## Prerequisites[â](#prerequisites "Direct link to Prerequisites")

1. [Create a plugin in Lua](https://docs.api7.ai/apisix/how-to-guide/custom-plugins/create-plugin-in-lua).

## Add Custom Plugin[â](#add-custom-plugin "Direct link to Add Custom Plugin")

1. Select **Gateway Settings** from the side navigation bar, then select **Custom Plugin**.
2. Click **Add Custom Plugin**.
3. From the add custom plugin dialog box, do the following:

* **Plugin Source Code File**: Upload the source code of your custom plugin.
* **Plugin Catalog**: Select the catalog for the plugin, for example, `General`.
* **Plugin Description**: Fill out the plugin description, for example, `Replace the response body`.
* **Plugin Documentation Link**: Add the URL to your plugin documentation.
* **Plugin Author**: Fill out the name of the plugin author.
* Click **Add**.

4. Now your custom plugin is added to the plugin list. It can be selected by global rules of services/routes/consumers/plugins in the **Enable Plugin** dialog box.

Below is an interactive demo that provides a hands-on introduction to adding custom plugins. You will gain a better understanding of how to use it in API7 Enterprise by clicking and following the steps.

## Additional Resource(s)[â](#additional-resources "Direct link to Additional Resource(s)")

* Key Concepts

  <!-- -->

  * [Services](https://docs.api7.ai/enterprise/3.3.x/key-concepts/services.md)
  * [Routes](https://docs.api7.ai/enterprise/3.3.x/key-concepts/routes.md)
  * [Plugins](https://docs.api7.ai/enterprise/3.3.x/key-concepts/plugins.md)
