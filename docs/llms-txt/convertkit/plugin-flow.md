# Source: https://developers.kit.com/plugins/media-source/plugin-flow.md

# Source: https://developers.kit.com/plugins/content-blocks/plugin-flow.md

> ## Documentation Index
> Fetch the complete documentation index at: https://developers.kit.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Content blocks plugin flow

> Example flow for the content block plugin

Let’s say you were developing an integration that allowed users to embed “Products” from your app inside the Kit editor. The full flow would look like this:

<Steps>
  <Step title="Create the HTML URL">
    You create a POST endpoint on your server to generate the HTML for your Product embed. *Details on configuring the `HMTL URL` [can be found here](/plugins/content-blocks/plugin-configuration#html-url).*
  </Step>

  <Step title="Create the search products endpoint">
    *Optional* - You create a POST endpoint on your server to allow users to search for products. This is only necessary if you add a [search input](/plugins/content-blocks/plugin-settings#search-input), because we need to retrieve the results from somewhere.
  </Step>

  <Step title="Create & publish your app">
    You [create your app within Kit](https://app.kit.com/apps?is=created) and configure the Products plugin. Once your app and plugin are ready, you submit your app for approval and publish.
  </Step>

  <Step title="Creator installs your app">
    A Kit user installs your app, triggering and completing your plugin's OAuth authentication flow.
  </Step>

  <Step title="Creator searches for your Product plugin and adds to their email">
    The Kit user navigates to an email and searches for your Product plugin from the content block menu, or by using the `/Products` quick command. They select it from the menu to add it.
  </Step>

  <Step title="Kit notifies you on add and edit">
    Upon adding the plugin to the email, and upon all subsequent interactions with the plugin settings, Kit will make a request to the endpoint found in step 1 along with the values from the configuration settings selected by the creator - along with their access tokens to ensure authentication with your servers.
  </Step>

  <Step title="Return the HTML">
    You will respond to the request, returning HTML for the Product that adheres to all of the setting values selected by the creator - which we'll insert into our editor, ready to send.
  </Step>
</Steps>


Built with [Mintlify](https://mintlify.com).