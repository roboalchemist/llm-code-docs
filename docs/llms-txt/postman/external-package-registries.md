# Import packages from external registries in Postman

You can [import public packages](#import-a-public-package) from external package registries into your scripts. Postman supports importing public packages from [npm](https://www.npmjs.com/) and [JSR](https://jsr.io/) registries. If you're on a Postman Professional or Enterprise plan, you can also [import private packages](#import-a-private-package) from npm that a Team Admin configured access to. You can import external packages in your internal, partner, and public workspaces. External packages are supported in HTTP, gRPC, and GraphQL requests.

## Import a public package

You can search for public external packages in npm and JSR and import them directly into your HTTP, gRPC, and GraphQL requests.

If you're on a Postman Enterprise plan, a Team Admin can [manage external packages](/docs/administration/managing-your-team/manage-team-workspaces/#allow-packages-from-external-package-registries) your team is allowed to use in scripts.

If you're on a Postman Enterprise plan, you can view external packages your Team Admin has allowed in scripts. Select **Team > Team Settings** in the Postman header, select **Team resources** in the sidebar, then select **External packages**.

To search and import a public external package, do the following:

1. Open an HTTP collection, folder, or request. You can also open a gRPC or GraphQL request.
2. Select the **Scripts** tab.
3. Select ![Image 1: Package icon](https://assets.postman.com/postman-docs/aether-icons/entity-package-stroke.svg#icon) **Packages** at the lower right of the code editor.
4. Search for a public package in npm or JSR. To filter your search results by package registry, select **npm**, **JSR**, or both. Search returns the top five results for each package registry. Learn about [supported public packages](#supported-external-packages) in Postman.
5. Select a package to import it into the code editor.

You can [view external packages in your script](#view-external-packages-in-your-script), including packages Postman was unable to import.

![Find and use public packages in external registries](https://assets.postman.com/postman-docs/v11/import-external-packages-v11-46.jpg)

When you select a public external package from search, a JavaScript variable is automatically declared in the code editor. Use the variable to call functions and objects in the package. By default, the variable identifier is based on the external package name. The variable's value is the `pm.require` method with the package registry, name, and latest version number as the argument in the `registry-name:package-name@version-number` format.

The script will always use the defined package version when the request runs. You can omit the version number (`@version-number`) from the argument to [use the latest package version](#use-the-latest-package-version) in all of your scripts.

You must use the exact version number in the argument. Postman doesn't support other ways to specify a version, such as version ranges or tags.

```js
// package imported from npm
const npmVariableName = pm.require('npm:package-name@version-number');
npmVariableName.functionName()

// package imported from jsr
const jsrVariableName = pm.require('jsr:package-name@version-number');
jsrVariableName.functionName()
```

## Import a private package

Private npm packages are supported on [Postman Professional and Enterprise plans](https://www.postman.com/pricing/).

You can import private external packages from npm if a Team Admin [configured access to the private package](/docs/administration/managing-your-team/manage-team-workspaces/#configure-access-to-private-packages) from your team's scripts. You can import private npm packages directly into your HTTP, gRPC, and GraphQL requests.

If you're on a Postman Enterprise plan, a Team Admin can [manage external packages](/docs/administration/managing-your-team/manage-team-workspaces/#allow-packages-from-external-package-registries) your team is allowed to use in scripts.

If you're on a Postman Professional or Enterprise plan, you can view external packages your Team Admin has allowed in scripts. Select **Team > Team Settings** in the Postman header, select **Team resources** in the sidebar, then select **External packages**.

To import a private external package, do the following:

1. Open an HTTP collection, folder, or request. You can also open a gRPC or GraphQL request.
2. Select the **Scripts** tab.
3. Declare a JavaScript variable in the code editor you can use to call functions and objects in the package. The variable's value must use the `pm.require` method with "npm", scope, package name, and latest version number as the argument in the `npm:@scope/package-name@version-number` format.

If you specified a version number, the script will always use the defined package version when the request runs. You can omit the version number (`@version-number`) from the argument to [use the latest package version](#use-the-latest-package-version) in all of your scripts.

```js
// package imported from npm
const npmVariableName = pm.require('npm:@scope/package-name@version-number');
npmVariableName.functionName()
```

You can [view external packages in your script](#view-external-packages-in-your-script), including packages Postman was unable to import.

## Use the latest package version

When you import an external package, you can configure the argument so the latest package version is used in all of your scripts. To do this, omit the version number (`@version-number`) from the `pm.require` method's argument. By default, scripts use the latest version number available when you first opened or ran the request.

Each script in your Postman app that imports the package without a version number will use the same version. The package version is specific to your Postman app, meaning the version may differ for your collaborators.

To update the package version number in your Postman app, do the following:

1. Open an HTTP collection, folder, or request. You can also open a gRPC or GraphQL request.
2. Select the **Scripts** tab.
3. Select ![Image 2: Package icon](https://assets.postman.com/postman-docs/aether-icons/entity-package-stroke.svg#icon) **Packages** at the lower right of the code editor.
4. Hover over the imported package, and select ![Image 3: Syncing icon](https://assets.postman.com/postman-docs/aether-icons/state-syncing-stroke.svg#icon) **Update to latest version**. The version number is updated in each of your scripts that import the package without specifying a version number.

## View external packages in your script

To view external packages in your request's script, select ![Image 4: Package icon](https://assets.postman.com/postman-docs/aether-icons/entity-package-stroke.svg#icon) **Packages** at the lower right of the code editor. To learn more about a package, hover over the package and select ![Image 5: Open in Postman icon](https://assets.postman.com/postman-docs/aether-icons/action-openInPostman-stroke.svg#icon) **View in npm** or ![Image 6: Open in Postman icon](https://assets.postman.com/postman-docs/aether-icons/action-openInPostman-stroke.svg#icon) **View in JSR**.

Use the following to troubleshoot external packages in your script:

* Packages with a blue checkmark were successfully imported in your script.
* Packages with a red exclamation point couldn't be imported in your script. For example, the version may not be valid or the package isn't allowed in your team. Hover over the exclamation point to view a tooltip about the issue.

## Supported external packages

Postman runs scripts in a sandbox environment that's secure by default. There are strict measures in place to ensure external code that runs inside the sandbox environment doesn't get extra privileges or access. Because of this, there may be some limitations when running the contents of external packages in the sandbox environment, depending on the package's dependencies.

Consider the following when importing external packages into Postman:

* Postman's sandbox environment runs code uniformly, regardless of whether the code runs on the browser or Node.js. External packages that use Nodes.js built-in modules may not work as expected in Postman because the modules aren't also available in the browser.
* Postman doesn't support all of JavaScript's [standard built-in objects](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects). Learn about the [JavaScript objects Postman supports](/docs/tests-and-scripts/write-scripts/postman-sandbox-reference/pm-require/#use-global-objects).
* Packages and their dependencies that exceed 50 MB aren't supported.
* Packages that use the [`await` keyword outside of an async function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/await#top_level_await) aren't supported.
* Packages that use both named and default exports must use specific syntax to access the default exports:

    ```js
    // access default exports
    const fooDefaultExport = pm.require("npm:foo").default
    
    // access named exports
    const { fooNamedExport } = pm.require("npm:foo")
    ```

## Troubleshoot vault secrets

You can reference vault secrets stored in your Postman Vault by adding the vault secret as a variable in your Postman Collection's or Environment's variables. For example, if you're using the `vault:postman-api-key` variable, you can use it in your API requests to retrieve the API key.

To reference a vault secret in your OpenAPI specifications using the URL to the component and its version. A component file must have a [published version](#version-and-publish-a-component-file) before you can reference its components in your specification.

To publish a new version of your component, select **Draft** in the version dropdown list. [Edit the component file](#edit-a-component-file) and then publish a new version.

## Sync components between collections and specifications

Consider the following behavior when syncing changes to reusable components between collections and OpenAPI specifications.

* When you [generate a collection from a specification](/docs/design-apis/specifications/generate-collections/), Postman uses referenced components from your team's component library to populate relevant parts of the collection.
* When you [sync changes](/docs/design-apis/specifications/generate-collections/#sync-changes-to-a-specification) from the collection back to the specification, Postman preserves the original reference URL if the values are unchanged. If you change values in the collection that originated from a referenced component, syncing those updates causes Postman to replace the reference URL with the updated inline values.

Learn more about:

* [Creating organization teams and workspaces](/docs/administration/organization/create/)
* [Organization roles](/docs/administration/organization/roles/)
* [Organization settings](/docs/administration/organization/settings/)

## Migrate your Enterprise team to an Organization

When you migrate your Enterprise team to an Organization, your Organization initially contains a single team that includes all the original teamâs shared workspaces.

These workspaces continue to be shared with the same users, and all members of the initial team become members of the migrated team.

This single team continues to function as it did before the migration, but Postman recommends that you break up your original, monolithic team into multiple Organization Teams, to take full advantage of Organization benefits.

To migrate your teams to Organizations, contact your Customer Success Manager. Your teams will be migrated to a single team that you can then reorganize and redistribute. Also see [Migrate your Enterprise team to an Organization](/docs/administration/organization/migrate/) for further steps.

Learn more about:

* [Creating organization teams and workspaces](/docs/administration/organization/create/)
* [Organization roles](/docs/administration/organization/roles/)
* [Organization settings](/docs/administration/organization/settings/)