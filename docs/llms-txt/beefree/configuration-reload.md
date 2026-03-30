# Source: https://docs.beefree.io/beefree-sdk/getting-started/readme/installation/configuration-parameters/configuration-reload.md

# Configuration Reload

## Overview <a href="#overview" id="overview"></a>

When you load a Beefree application inside the host application, you pass a [configuration object](https://docs.beefree.io/beefree-sdk/getting-started/readme/installation/configuration-parameters) with multiple sections that define the characteristics of the UI, UX, and available elements. However, there are cases when you may want to reload this configuration without the need to reload the Beefree application. In these cases, you can use a specific event to update the configuration while the editor is open.

## Use cases <a href="#use-cases" id="use-cases"></a>

With this event, you can make on-the-fly changes to the user experience. For example:

* Updating available categories for [Saved rows](https://docs.beefree.io/beefree-sdk/rows/storage/self-hosted-saved-rows)
* Refreshing a [Custom header](https://docs.beefree.io/beefree-sdk/other-customizations/advanced-options/custom-headers) for authorization
* Changing [Advanced permissions](https://docs.beefree.io/beefree-sdk/other-customizations/advanced-options/advanced-permissions) for the current user
* Updating settings for the editor’s [Content defaults](https://docs.beefree.io/beefree-sdk/other-customizations/appearance/content-defaults)

## How it works <a href="#how-it-works" id="how-it-works"></a>

You can load the configuration changes via a new instance event. Here’s an example:

```javascript

var newConfig = {
  advancedPermissions: {
    // new permissions
  }
}

bee.loadConfig(newConfig)

```
