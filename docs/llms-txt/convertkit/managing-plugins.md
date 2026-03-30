# Source: https://developers.kit.com/plugins/managing-plugins.md

> ## Documentation Index
> Fetch the complete documentation index at: https://developers.kit.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Managing plugins

> Creating and configuring your app's plugins

This guide helps you through the process of managing your plugins, from starting out, to testing all the way through to release. This guide is split out to help guide you through a number of key concepts:

* Creating your plugins
* Configuring plugin authentication
* Testing your plugins
* Activating your plugins
* Managing your existing plugins

## Configuring plugin authentication

Before you can start creating plugins, you need to select and set up your authorization strategy for your plugins to let Kit know how to fetch the content needed to let creators use your apps.

We currently offer 2 options:

<AccordionGroup>
  <Accordion title="OAuth">
    If you require linking of third-party accounts or are sharing sensitive information, we currently only support OAuth authentication. This option will likely be the default for most applications, needing to pull data from a third-party account for the creator in a vast number of use cases. More details on OAuth authorization for plugins can be found in the [dedicated OAuth guide](/plugins/oauth-authorization).
  </Accordion>

  <Accordion title="No authorization">
    If you are working with public APIs, don’t need to pull any confidential information and are happy to have the content endpoints open, you can select “No authorization”. This can also be used temporarily to test our functionality before committing development time into building out an OAuth flow.
  </Accordion>
</AccordionGroup>

<img width="800" alt="plugin authentication strategies" src="https://mintcdn.com/kit-314e57c1/ohR8KbVxvspIDffR/images/plugins/plugin-authentication-strategies.png?fit=max&auto=format&n=ohR8KbVxvspIDffR&q=85&s=d4deba45766b48e762d4ef1e177b1794" data-path="images/plugins/plugin-authentication-strategies.png" />

If you try to create a plugin without setting your authentication strategy, you will be prompted to set this up, with 2 options; selecting:

* "Continue without authentication" sets your strategy to "No authorization", or
* "Configure Authentication" takes you to the Authentication tab to set this up

<img width="400" alt="plugin authentication modal" src="https://mintcdn.com/kit-314e57c1/ohR8KbVxvspIDffR/images/plugins/configure-plugin-authentication-modal.png?fit=max&auto=format&n=ohR8KbVxvspIDffR&q=85&s=d6ed15b53d84e5ea26a3995be3909a42" data-path="images/plugins/configure-plugin-authentication-modal.png" />

<Note> If you disable plugin authentication on the Authentication tab, you'll see a warning when you return to the Plugins tab. This warning indicates that you need to update authentication settings before your plugins can be active. Click the prompt to go directly to the Authentication tab and make the necessary changes. <br /><img width="600" alt="disabled plugin authentication modal" src="https://mintcdn.com/kit-314e57c1/ohR8KbVxvspIDffR/images/plugins/disabled-plugin-authentication.png?fit=max&auto=format&n=ohR8KbVxvspIDffR&q=85&s=9ee53cdbf89d49ce4f9149985deb431d" data-path="images/plugins/disabled-plugin-authentication.png" /></Note>

## Create a new plugin

Once you have selected your authentication method, you'll be able to create your first plugin! To do this, click on the "Plugins" tab in the sidebar menu when editing your app. When here, click on the "+ New plugin" button to start the process.

<img width="800" alt="creating your first plugin" src="https://mintcdn.com/kit-314e57c1/ohR8KbVxvspIDffR/images/plugins/creating-your-first-plugin.png?fit=max&auto=format&n=ohR8KbVxvspIDffR&q=85&s=ddb77b54b207d7d2fc7d8e71693afb84" data-path="images/plugins/creating-your-first-plugin.png" />

<Note> If this is your second app, the "+ New plugin" button will be located to the right of the Plugin title:<br /><img width="800" alt="creating your first plugin" src="https://mintcdn.com/kit-314e57c1/ohR8KbVxvspIDffR/images/plugins/creating-your-second-plugin.png?fit=max&auto=format&n=ohR8KbVxvspIDffR&q=85&s=592411e17da732169a6ba090577b78a2" data-path="images/plugins/creating-your-second-plugin.png" /></Note>

From here, a modal will appear asking for a name and plugin type. The name can be updated later and should be unique for the app you are creating. On overview for the available plugin types [can be found here](/plugins/overview), with more detail found in their dedicated sections in the Environments section below.

<img width="600" alt="OAuth authorization strategy UI" src="https://mintcdn.com/kit-314e57c1/ohR8KbVxvspIDffR/images/plugins/create-a-new-plugin-modal.png?fit=max&auto=format&n=ohR8KbVxvspIDffR&q=85&s=bb4ddcb80db1d4bd5a260426825093c0" data-path="images/plugins/create-a-new-plugin-modal.png" />

After completing this step, you'll land on a dedicated setup page where you can configure your plugin settings.

<Accordion title="Example plugin configuration for content blocks">
  <img width="600" alt="example plugin configuration" src="https://mintcdn.com/kit-314e57c1/ohR8KbVxvspIDffR/images/plugins/plugin-configuration-example.png?fit=max&auto=format&n=ohR8KbVxvspIDffR&q=85&s=ed70cfe2e283cdd2e89f677f2bb99dd9" data-path="images/plugins/plugin-configuration-example.png" />

  <Note>Details on the JSON required to set plugins up can be found in the plugin configuration documentation for the respective plugin environment.</Note>
</Accordion>

## Testing your plugins

So that new plugins can be tested for apps that have already been published, the developer account for an app is able to see all plugins set up for an app within their account *regardless of whether they are active or not*. This allows you to utilize your production system and your app authentication to test changes in a live system without worrying about other accounts accessing your plugins before they are ready.

If you haven't yet gone live with your app and you want to envision what your plugins will look like for creators, you can start building out your plugins with public API endpoints and the "no authorization" authentication strategy, allowing you to tweak your content before finalising your OAuth authentication flows.

## Activating your plugin

When you first create your plugin it will be inactive. While inactive it will only be available to test for your developer account, but once activated, the plugin will be visible to any user who has installed the app.

<Note>You must install your app from the Kit App Store to see your plugins in the editor. To do this, go to the ["Build" tab in the Kit App Store](https://app.kit.com/apps?is=created), click on "Preview" and install your app.</Note>

In order to activate your plugin for Kit-wide usage, simply click the "Active" toggle and confirm that you want to set it live by clicking "Activate" in the resulting modal.

<img width="800" alt="activating your plugin" src="https://mintcdn.com/kit-314e57c1/ohR8KbVxvspIDffR/images/plugins/activating-your-plugin.png?fit=max&auto=format&n=ohR8KbVxvspIDffR&q=85&s=4d4871dbc22df618dc4da7f22d087c75" data-path="images/plugins/activating-your-plugin.png" />activating-your-plugin

At this point, the plugin will be available for all accounts that have installed your app.

## Managing your plugins

Once you have created plugins within your app, you'll see your complete plugin list in the "Plugin" tab of your app, with options to:

* Activate or deactivate plugins using toggles
* Edit plugin settings

<img width="800" alt="plugin list" src="https://mintcdn.com/kit-314e57c1/ohR8KbVxvspIDffR/images/plugins/plugin-list.png?fit=max&auto=format&n=ohR8KbVxvspIDffR&q=85&s=e5e63dd2e36eee70c3efb4db8b5bef78" data-path="images/plugins/plugin-list.png" />

<Warning>If a plugin is already active on a published app, we don’t recommend editing it until your changes have been thouroughly tested, as all updates to your plugins will take effect immediately, for accounts that have your app installed. Instead, create a new plugin and keep it inactive to test your changes. Once your tests are successful, you can update the original plugin with the new functionality.</Warning>

### Deleting plugins

You can also delete your unwanted plugins. In order to do this, simply edit the plugin you want to delete, and select the `Delete Plugin` button in the bottom left corner.

<img width="800" alt="delete plugin" src="https://mintcdn.com/kit-314e57c1/ohR8KbVxvspIDffR/images/plugins/delete-plugin.png?fit=max&auto=format&n=ohR8KbVxvspIDffR&q=85&s=924ea844d5d11c7c2474079a9765b3c9" data-path="images/plugins/delete-plugin.png" />

Once you click this, a confirmation modal will appear, click `Delete` and the plugin will be deleted from the app.

<img width="800" alt="delete plugin confirmation" src="https://mintcdn.com/kit-314e57c1/ohR8KbVxvspIDffR/images/plugins/delete-plugin-confirmation.png?fit=max&auto=format&n=ohR8KbVxvspIDffR&q=85&s=4bbb6f0089ac1a1ecb5bd99ab7396f93" data-path="images/plugins/delete-plugin-confirmation.png" />

<Note>This will stop creators from being able to add new instances of this plugin, but won't remove previously added instances to reduce the chance of broken content. This will allow creators to make the decision themselves on how they want to manage the plugin - by deleting it from their content or using the last valid state they saw.</Note>


Built with [Mintlify](https://mintlify.com).