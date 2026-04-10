# Source: https://developers.kit.com/kit-app-store/app-versioning.md

> ## Documentation Index
> Fetch the complete documentation index at: https://developers.kit.com/llms.txt
> Use this file to discover all available pages before exploring further.

# App versioning

> Ensure creators have access to your latest functionality through app versioning

App versioning in Kit ensures smooth transitions when authentication requirements change, protecting both creators and developers by maintaining compatibility while apps evolve. This guide explains how versioning works, what triggers new versions, and the implications for both creators using your app and developers maintaining it.

## Understanding app versions

App versions are automatically created by Kit when certain changes to your app's authentication or scope requirements occur. These versions help manage the authentication lifecycle and ensure creators maintain proper access to your app's functionality.

Kit automatically creates new app versions in the following scenarios:

* Initial publication (v1)
* Authentication changes

When installing an app, a creator will always authenticate with the latest available version.

### Initial publication

The first version is created when your app is initially published to the Kit App Store. This establishes the baseline authentication and scope requirements for your app going forwards.

### Authentication changes

A new version is triggered when your app authentication requirements change after it is released. This ensures that creators are prompted to reauthenticate to gain access to any new features and functionality reliant on the new authentication method or scopes attached.

The specific scenarios are:

* **Access types change** - When you modify which Kit resources your app can access (API access, plugin access, or both) in your app's *Authentication* settings tab
* **Authorization strategy changes** - When your plugin provider's authentication method changes (for example, switching from "No authorization" to "OAuth) in your app's *Authentication* settings tab
* **Plugin scopes change** - When the cumulative scope requirements across all your plugins are modified - more details on this can be found below.

## Understanding scope changes

Scopes define the specific permissions your plugins require to access data from your service. Kit tracks scopes cumulatively across all plugins in your app, and version changes occur when:

* A new plugin is created with a scope that none of your other plugins currently use
* A scope is added to an existing plugin that wasn't previously required by any plugin
* A scope is removed from a plugin and is not used by any other plugins in your app

Scopes allow you to gate access to plugins to only work for creators that have installed the correct version of your app.

<Note>
  For example, if you have two plugins:

  * Plugin A uses scopes: `read:products`, `read:inventory`
  * Plugin B uses scopes: `read:products`, `read:customers`

  Your app's cumulative scopes are: `read:products`, `read:inventory`, `read:customers`

  Adding `write:orders` to either plugin would trigger a new version, while adding `read:products` to a third plugin would not (since it's already in the cumulative scope set).
</Note>

### Adding scopes to a plugin

Scopes can be added to plugins using the *Scopes* field found when editing a plugin. A plugin can have any number of scopes attached, with previously used scopes available for selection automatically from the field. When creating a new scope, press return upon completion of typing for it to be added to the plugin. Click save to publish this change and prompt upgrade for creators with the app installed.

<img width="800" alt="plugin scopes" src="https://mintcdn.com/kit-314e57c1/ohR8KbVxvspIDffR/images/kit_app_store/plugin-scopes.png?fit=max&auto=format&n=ohR8KbVxvspIDffR&q=85&s=2ff7dd7081f88530615c80ccf92ac3d8" data-path="images/kit_app_store/plugin-scopes.png" />

<Warning>
  Using spaces in scope names can cause serialization issues when processed as arrays or comma-separated strings. We recommend using a combination of `action:resource`, such as `read:data` (opposed to `read data`) and hyphens/underscores/snake-case/camel-case for multi-word scopes, such as `read:customer_data`.
</Warning>

## Impact on creators

When a new app version is created, the experience varies depending on the type of change:

### Re-authentication requirements

Creators will be prompted to re-authenticate your app when:

* **New access types are added** - For example, if your app previously only used plugins but now also requires API access
* **Authorization strategy changes to OAuth** - When moving from no authentication to OAuth authentication
* **New scopes are added** - When your plugins require additional permissions not previously granted

When re-authentication is required, creators will be notified of updates required, through:

* An icon on the [*Manage tab of the Kit App Store*](https://app.kit.com/apps):

<img width="800" alt="kit app store browse tab updates required" src="https://mintcdn.com/kit-314e57c1/dSCrspkEWxNDV3Va/images/kit_app_store/browse-tab-updates.png?fit=max&auto=format&n=dSCrspkEWxNDV3Va&q=85&s=17e186ec421d0098dac0224633a8ea68" data-path="images/kit_app_store/browse-tab-updates.png" />

* All *Install* buttons will change to *Update* for all app cards across the Kit App Store, as well as an update icon in the top right corner:

<img width="300" alt="app update example" src="https://mintcdn.com/kit-314e57c1/ohR8KbVxvspIDffR/images/kit_app_store/shopify-app-update.png?fit=max&auto=format&n=ohR8KbVxvspIDffR&q=85&s=36b8ec2719d20d92a62ba014d3673f57" data-path="images/kit_app_store/shopify-app-update.png" />

* A separate section for apps requiring updates at the top of [*Manage tab of the Kit App Store*](https://app.kit.com/apps?is=installed):

<img width="800" alt="app update section on manage tab" src="https://mintcdn.com/kit-314e57c1/dSCrspkEWxNDV3Va/images/kit_app_store/manage-tab-updates.png?fit=max&auto=format&n=dSCrspkEWxNDV3Va&q=85&s=4c4fa6e71061fdeb15defb0509df766e" data-path="images/kit_app_store/manage-tab-updates.png" />

Upon clicking the *Update* button for any apps requiring updates, the creator is guided through the authentication flow to grant all new necessary permissions.

<Note>
  When the update is tied to authentication strategy changes, an additional banner will be shown on the *Authentication* settings page for your app to help you know when an update will be required from creators.

  <img width="800" alt="app update warning in authentication settings page for an app" src="https://mintcdn.com/kit-314e57c1/dSCrspkEWxNDV3Va/images/kit_app_store/authentication-change-warning.png?fit=max&auto=format&n=dSCrspkEWxNDV3Va&q=85&s=e0da4ce8cc5b3f2779fb47ccce66f79d" data-path="images/kit_app_store/authentication-change-warning.png" />
</Note>

### Seamless updates

Some version changes don't require creator action:

* **Scope removals** - When permissions are removed, creators maintain their existing authentication
* **Access type removals** - When reducing the app's access requirements

## Impact on developers

As a developer, understanding app versioning helps you plan updates strategically and minimize disruption for your users. It allows you to gate plugins, to only be accessible when a certain version of your authentication strategy is installed, as well as build your apps iteratively - perhaps launching with API access only, before adding plugins at a later date.

Below are a few best practices & common scenarios to ensure you are making the most out of app versioning, to make future app updates as seamless as possible.

### Best practices

* **Testing plugins with new scopes before launch** - When plugins are inactive but require new scopes, ensure you re-authenticate the app in the [*Build tab of the Kit App Store\_*](https://app.kit.com/apps?is=created) to test the new functionality before launch. This allows you to verify the authentication flow works as expected before affecting production users. Other creators won't see these changes until you publish the plugin.
* **Plan your scopes carefully** - Define comprehensive scopes during initial development to minimize future version changes.
* **Group related functionality** - Consider future features when establishing initial scope requirements
* **Avoid problematic scope formats** - Never use spaces in scope names and use consistent naming conventions for ease of management (recommended: `action:resource` format)
* **Test thoroughly before publishing** - Use test mode to verify all scope changes work correctly. Ensure your OAuth server properly handles the new scope requests and validate that the re-authentication flow provides clear information to creators
* **Managing version transitions** - When planning changes that will trigger a new version:
  * Communicate with your users - If possible, notify creators about upcoming changes through your app's channels
  * Bundle related changes - Group authentication changes together to minimize the number of versions
  * Maintain backwards compatibility - Ensure your endpoints can handle both old and new authentication tokens during transition periods
  * Update your documentation - Keep your app's description and support resources current with the new requirements
* **Track your app's version history** - While Kit manages version creation automatically, we recommend maintaining your own changelog documenting what changed in each version. This should include the date and reason for authentication changes & which features correspond to which version requirements

### Common scenarios and solutions

**Scenario: Adding a new feature**
If you're adding a new plugin that requires additional scopes:

1. Consider whether the feature could work with existing scopes
2. If new scopes are necessary, plan the rollout carefully
3. Test thoroughly in development mode first
4. Communicate the value of the new feature to encourage re-authentication

**Scenario: Improving security**
When updating from no authentication to OAuth:

1. Implement your OAuth server following Kit's requirements
2. Test the complete flow in development
3. Prepare clear documentation for creators about why authentication is now required
4. Consider providing a grace period where both methods work if technically feasible

**Scenario: Reducing permissions**
If you're optimizing your app to require fewer scopes:

1. This won't require creator re-authentication
2. Update your code to work with reduced permissions
3. Remove unnecessary scope requests from your OAuth flow
4. This is generally seamless for users but improves security and trust

## Technical considerations

### OAuth server requirements

When implementing scope changes, ensure your OAuth server:

* Properly validates and returns the requested scopes
* Handles incremental authorization if scopes are added over time
* Provides clear scope descriptions in the consent screen
* Maintains tokens that accurately reflect granted scopes

### Error handling

Implement robust error handling for version-related scenarios:

* Detect when a creator hasn't granted new required scopes
* Provide clear messages about what permissions are needed and why
* Guide users to re-authenticate when necessary
* Gracefully degrade functionality if optional scopes aren't granted


Built with [Mintlify](https://mintlify.com).