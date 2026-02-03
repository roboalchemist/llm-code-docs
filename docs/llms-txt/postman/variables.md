# variables

_Store and reuse values using variables_

_By storing a value as a variable, you can reference it throughout your collections, environments, requests, and scripts. Variables help you work efficiently, collaborate with teammates, and set up dynamic workflows._

## Understanding variables

A variable is a symbolic representation of data that enables you to access a value without having to enter it manually wherever you need it. This can be useful if you're using the same values in multiple places. Variables make your requests more flexible and readable by abstracting the detail away.

For example, if you have the same URL in more than one request, but the URL might change, you can store it in a "base_url" variable. Then, use "{{base_url}}" to reference the variable in your requests. If the URL changes, you can change the variable value and it'll be reflected throughout your collection wherever you've used the variable name.

The same principle applies to any part of your request where data is repeated. Whatever value is stored in the variable will be included wherever you've referenced the variable when your requests run. If the variable value is `https://postman-echo.com` and the request uses the `{{base_url}}/get` URL, then Postman sends the request to `https://postman-echo.com/get`.

![Environment editor](https://assets.postman.com/postman-docs/v11/environment-editor-v11-60-4.jpg)
![Reference variable](https://assets.postman.com/postman-docs/v11/reference-var-v11-18.jpg)

Variables in Postman are key-value pairs. Each variable name represents its key, so referencing the variable name enables you to access its value. You can use variables to pass data between requests and tests. For example, if you are [chaining requests](https://www.postman.com/postman/postman-team-collections/collection/fa2fdwg/extract-data-to-chain-requests) in a collection.

Use your [Postman Vault](/docs/sending-requests/postman-vault/postman-vault-secrets/) to store sensitive data as vault secrets and reuse them in your local instance of Postman. Only you can access and use values associated with your vault secrets and secrets aren't synced to the Postman cloud.

Use environments to group sets of variables together and share them with collaborators. For example, if you use one set of config details for your production server and another for testing. See [Group sets of variables in Postman using environments](/docs/sending-requests/variables/managing-environments/) for more on how you can incorporate environments into your team workflows.

## Variable scopes

Postman supports variables at different scopes, allowing you to tailor your processing to a variety of development, testing, and collaboration tasks. Scopes in Postman relate to the different contexts that your requests run in, and different variable scopes are suited to different tasks.

You can create a variable without a variable scope if it isn't meant to hold a default value. You can also create a variable without a scope to try out the value before adding it to a scope. Learn more about [creating variables without a scope](#setting-values-for-variables-without-a-scope).

In order from broadest to narrowest, these scopes are: _global_, _collection_, _environment_, _data_, and _local_.

* **Global variables** enable you to access data between collections, requests, scripts, and environments. Global variables are available throughout a [workspace](/docs/collaborating-in-postman/using-workspaces/create-workspaces/). Since global variables have the broadest scope available in Postman, they're well-suited for testing and prototyping. In later development phases, use more specific scopes.
* **Collection variables** are available throughout the requests in a collection and are independent of environments. Collection variables don't change based on the selected environment. Collection variables are suitable if you're using a single environment, such as auth or URL details.
* **Environment variables** enable you to scope your work to different environments, such as local development versus testing or production environments. One environment can be active at a time. If you have a single environment, using collection variables can be more efficient, but environments enable you to specify [role-based access levels](/docs/sending-requests/variables/team-environments/#share-an-environment).
* **Data variables** come from external CSV and JSON files to define data sets you can use when running collections with the [Collection Runner](/docs/collections/running-collections/intro-to-collection-runs/), the [Postman CLI](/docs/postman-cli/postman-cli-overview/), or [Newman](/docs/collections/using-newman-cli/command-line-integration-with-newman/). Data variables have local values, which don't persist beyond request or collection runs.
* **Local variables** are temporary variables that are accessed in your request scripts. Local variables are scoped to a single request or collection run, and are no longer available when the run is complete. Local variables are suitable if you need a value to override all other variable scopes but don't want the value to persist once the run ends.

![Variable scope](https://assets.postman.com/postman-docs/v10/var-scope-v10.jpg)

If a variable with the same name is declared in two different scopes, the value stored in the variable with narrowest scope will be used. For example, if there is a "username" global variable and a "username" local variable, the local value is used when the request runs.

Postman stores variables as strings. If you store objects or arrays, remember to `JSON.stringify()` them before storing, and `JSON.parse()` them when you retrieve them.

## Variable values

By default, collection, environment, and global variable values are only available locally in your instance of Postman. The local value is used when sending requests, and it isn't synced to the Postman cloud. Update your local value as you'd like, without sharing it with your teammates. Learn how to [define a local value for your variables](#defining-variables).

If you have Editor access to the element, you can [share a variable's value](#share-variable-values), syncing it's value to the Postman cloud. Share a variable's value to provide your teammates with a default value they can use to begin making requests to your API. Your teammates can continue to update their local value without sharing it. They can also reset their local value back to the shared value at any time.

Some Postman features that run on the Postman cloud also use the shared value when sending requests. These features include scheduled collection runs, monitors, the Postman CLI, and Newman.

If you're more familiar with current and initial values, learn more about the [previous way of defining variables](#previous-way-of-defining-variables).

### Previous way of defining variables

Postman no longer supports maintaining multiple independent values for your collection, environment, and global variables. Previously, you could provide a _current value_ (local) and _initial value_ (shared) for your variables and update them separately.

Initial and current values are supported in the Postman VS Code extension. Learn more about [variables in the VS Code extension](/docs/developer/vs-code-extension/send-requests/#store-variables).

With this change, you only need to provide a single value for your variables that's local by default (previously the current value). Learn how to [define a local value for your variables](#defining-variables).

You can choose to [share a variable's value](#share-variable-values) with your teammates (previously the initial value), based on the local value at the time of sharing. You can continue to update and use your local value without sharing it. Updates to your local value are only shared with your teammates if you intentionally choose to share the new value.

## Defining variables

Variable values are local by default and only available to you in your instance of Postman. These values aren't synced to the Postman cloud. Once you've defined a local value, you can optionally [share variable values](#share-variable-values), syncing the value to the Postman cloud.

Remember to delete variables you're no longer using.

To define variables at any scope in the request builder, do the following:

1. Select the data you need, for example in the address, parameters, headers, or body.
1. Right-click the selection and click **Set as variable**.

![Set as variable](https://assets.postman.com/postman-docs/v11/set-as-var-prompt-v11-3.jpg)

1. Click ![Add icon](https://assets.postman.com/postman-docs/aether-icons/action-add-stroke.svg#icon) **Set as new variable**.

![Set as variable](https://assets.postman.com/postman-docs/v11/set-as-a-new-var-v11-25.jpg)

1. Enter a **Name**, confirm the **Value** is correct, and select a **Scope**. Then click **Set Variable**.

![Set as variable](https://assets.postman.com/postman-docs/v11/set-as-var-modal-v11-25.jpg)

You can also define variables in the following ways:

* [Try out a variable locally without a scope](#setting-values-for-variables-without-a-scope), then [add the variable to a scope](#adding-variables-to-a-scope).
* [Set a response body value as a variable](#setting-response-body-values-as-variables) (_Desktop app only_)
* Define a variable in the [global](#defining-global-variables), [environment](#defining-environment-variables), or [collection](#defining-collection-variables) scope.
* [Define variables using scripts](#defining-variables-in-scripts).

Learn more about [variable scopes](#variable-scopes) in Postman.

You can also learn how to [define variables from the VS Code extension](/docs/developer/vs-code-extension/send-requests/#store-variables).

### Setting values for variables without a scope

Variables without a [variable scope](#variable-scopes) are useful for trying out the value before [adding the variable to a scope](#adding-variables-to-a-scope). This is also useful for sending data with requests that isn't meant to hold a default value. For example, a variable without a scope might send user-specific information that changes each time you send the request. Variables without a scope also enable you to create a placeholder variable to share with your API consumers, without having to define the variable at a specific scope.

In the request builder, you can create a variable without adding it to a variable scope. The value you enter for this variable is stored locally and is only available in the request it's set in. When you click ![Variable list icon](https://assets.postman.com/postman-docs/aether-icons/descriptive-variableList-stroke.svg#icon) **Variables**, the variable isn't associated with a scope (highlighted by color) in the variables pane under **Variables in request**.

To create a variable from the request builder, [use double curly braces (\"{{\" and \"}}\") to reference a variable](#using-variables) that doesn't exist or isn't available from the request. For example, enter "{{username}}" to create a username variable that doesn't have a scope.

![Set a value for variable without a scope](https://assets.postman.com/postman-docs/v11/variables-used-temporary-value-v11-18.jpg)

To set a value for a variable without a scope, hover over it, click the text box, then enter a value. You can also click ![Variable list icon](https://assets.postman.com/postman-docs/aether-icons/descriptive-variableList-stroke.svg#icon) **Variables** in the [workbench](/docs/getting-started/basics/navigating-postman/#environment-selector-and-variables-pane) to open the variables pane. Click **Enter value** next to the variable, then enter a value.

You can use `pm.variables.get(variableName)` to access variables without a scope in scripts. Learn more about [using variables in scripts](/docs/tests-and-scripts/write-scripts/postman-sandbox-reference/pm-variables/).

Values for variables without a scope are stored locally in a request until you close its tab or sign out of Postman. When you open the request again, the variable's value will be empty. If you'd like to store and reuse the value in your requests, you can [add the variable and its value to a scope](#adding-variables-to-a-scope).

You can also create a vault secret without adding it to your Postman Vault. [Open your Postman Vault](/docs/sending-requests/postman-vault/postman-vault-secrets/#access-your-postman-vault), then use the "{{vault:secret-name}}" syntax. When you're ready, you can add the vault secret to your Postman Vault. Learn how to [create](/docs/sending-requests/postman-vault/manage-vault-secrets/#set-a-value-for-a-vault-secret-that-doesnt-exist) and [add](/docs/sending-requests/postman-vault/manage-vault-secrets/#add-a-vault-secret-reference-to-your-postman-vault) a vault secret from the request builder.

### Adding variables to a scope

From a Postman element, such as a request or collection, you can create a variable and add it to a specific [variable scope](#variable-scopes) to reuse it across your requests. You can also add a [variable without a scope](#setting-values-for-variables-without-a-scope) to a specific variable scope in your team. From the element, you can add a value that's stored locally for the variable.

You need Editor access to an environment or collection to add variables to it.

[Use double curly braces (\"{{\" and \"}}\") to reference a variable](#using-variables) that doesn't exist or isn't available from the element. Hover over the reference to the variable, click the text box, then enter a value if you haven't already. Select the **Add to** dropdown list, then select the scope you'd like to add the variable to.

![Add unresolved variable to a scope](https://assets.postman.com/postman-docs/v11/variables-used-define-unresolved-v11-18.jpg)

You can define variables at any scope from the **Authorization** tab. Select the **Auth Type** dropdown list, select an authorization, then enter a value in a field that holds sensitive data, such as a password or token. Hover over ![Secret warning icon](https://assets.postman.com/postman-docs/aether-icons/state-secretWarning-stroke.svg#icon) **Sensitive value**, click **Set as Variable**, enter a name for the variable, then select the scope you'd like to add it to.

![Set as new variable](https://assets.postman.com/postman-docs/v11/set-sensitive-value-as-vault-secret-v11-39.jpg)

You can also click ![Variable list icon](https://assets.postman.com/postman-docs/aether-icons/descriptive-variableList-stroke.svg#icon) **Variables** in the workbench to view the variables and vault secrets used in your request. Click the text box, enter a value for the variable without a scope, click ![Add icon](https://assets.postman.com/postman-docs/aether-icons/action-add-stroke.svg#icon) **Add to**, then select the scope you'd like to add it to.

![Define a value for an unresolved variable](https://assets.postman.com/postman-docs/v11/variables-used-define-variable-pane-v11-18.jpg)

You can also choose to add sensitive data as a vault secret in your Postman Vault. To add it as a vault secret in your Postman Vault, first [open your Postman Vault](/docs/sending-requests/postman-vault/postman-vault-secrets/#access-your-postman-vault).

The environment you want to add a variable to must be active in the environment selector. If an environment isn't active, you can add a variable to an environment using one of the following options in the dropdown list:

* **Select an existing environment** - Click **Select**, then choose an environment to make it active. The variable is added to the selected environment.
* **Create a new environment** - Click **Create One**, enter a name for the environment, then select **Create**. The variable is created and added to the new environment.

Note that you can [set global and environment variables as sensitive data](#set-a-value-as-sensitive-data), masking the values in the Postman app.

![Choose or create an environment for unresolved variables](https://assets.postman.com/postman-docs/v11/variables-used-choose-active-environment-v11-18.jpg)

If the variable without a scope has the "vault:" prefix (for example, "vault:postman-api-key"), you can only add it to your Postman Vault as a vault secret.

To add a local value to a variable that you can shared with collaborators, learn how to edit variables directly in the [global](#defining-global-variables), [environment](#defining-environment-variables), and [collection](#defining-collection-variables) scope.

### Setting response body values as variables

Setting response body values as variables is only available in the [Postman desktop app](/docs/getting-started/installation/installation-and-updates/).

To define variables at any scope from a request's response body, do the following:

1. (Optional) If you're setting the value for an environment variable, [select the variable's environment](/docs/sending-requests/variables/managing-environments/#switch-between-environments) from the dropdown list located in the top right of the workbench.
1. In the response, right-click the selection and click **Set as variable**.
1. Click ![Add icon](https://assets.postman.com/postman-docs/aether-icons/action-add-stroke.svg#icon) **Set as new variable**.
1. Enter a **Name**, confirm the **Value** is correct, and select a **Scope**. Then click **Set Variable**.

![Set as new variable](https://assets.postman.com/postman-docs/v11/set-sensitive-value-as-vault-secret-v11-39.jpg)

You can also define variables in the following ways:

* [Try out a variable locally without a scope](#setting-values-for-variables-without-a-scope), then [add the variable to a scope](#adding-variables-to-a-scope).
* [Set a response body value as a variable](#setting-response-body-values-as-variables) (_Desktop app only_)
* Define a variable in the [global](#defining-global-variables), [environment](#defining-environment-variables), or [collection](#defining-collection-variables) scope.
* [Define variables using scripts](#defining-variables-in-scripts).

Learn more about [variable scopes](#variable-scopes) in Postman.

You can also learn how to [set a value as sensitive data from the VS Code extension](/docs/developer/vs-code-extension/send-requests/#store-variables).

### Defining global variables

To view global variables, click **Environments** in the sidebar and select **Globals**.

To add a new global variable, do the following:

1. Click the **Add variable** text box and enter a variable name.
1. (Optional) Click ![Key icon](https://assets.postman.com/postman-docs/aether-icons/descriptive-key-stroke.svg#icon) **Mark as sensitive** next to the variable name to set the variable as sensitive data, masking the value in Postman. Learn more about [setting a variable as sensitive data](#set-a-value-as-sensitive-data).
1. Enter the variable's value.
1. (Optional) Click ![Edit description icon](https://assets.postman.com/postman-docs/v11/icons/icon-edit-description-v11.jpg#icon) **Add description** next to the variable name and enter a description of the variable. To display the description in a separate column, click ![Options icon](https://assets.postman.com/postman-docs/aether-icons/action-options-stroke.svg#icon) **More** and select **Description**.
1. (Optional) Click ![Share icon](https://assets.postman.com/postman-docs/v11/icons/icon-cloud-v11.svg#icon) **Share** next to the value to share it with teammates and use it with monitors and scheduled runs. To display the shared value in its own column, click ![Options icon](https://assets.postman.com/postman-docs/aether-icons/action-options-stroke.svg#icon) **More** and select **Shared Value**.

To download global variables, click ![Export icon](https://assets.postman.com/postman-docs/aether-icons/action-export-stroke.svg#icon) **Export** in the upper right of the workbench.

To edit an existing global variable, change the desired variable name, value, or description. To search for a global variable by name or value, click ![Search icon](https://assets.postman.com/postman-docs/aether-icons/action-search-stroke.svg#icon) **Search**, and enter your search.

You can also learn about [defining global variables in scripts](#defining-variables-in-scripts) and [viewing and editing variables](#viewing-and-editing-variables-in-an-element) directly from a Postman element.

Changes to your variables are automatically saved.

### Defining environment variables

To view environment variables, click **Environments** in the sidebar and select the environment you want to view.

To add a new environment variable, do the following:

1. Click the **Add variable** text box and enter a variable name.
1. (Optional) Click ![Key icon](https://assets.postman.com/postman-docs/aether-icons/descriptive-key-stroke.svg#icon) **Mark as sensitive** next to the variable name to set the variable as sensitive data, masking the value in Postman. Learn more about [setting a variable as sensitive data](#set-a-value-as-sensitive-data).
1. Enter the variable's value.
1. (Optional) Click ![Edit description icon](https://assets.postman.com/postman-docs/v11/icons/icon-edit-description-v11.jpg#icon) **Add description** next to the variable name and enter a description of the variable. To display the description in a separate column, click ![Options icon](https://assets.postman.com/postman-docs/aether-icons/action-options-stroke.svg#icon) **More** and select **Description**.
1. (Optional) Click ![Share icon](https://assets.postman.com/postman-docs/v11/icons/icon-cloud-v11.svg#icon) **Share** next to the value to share it with teammates and use it with monitors and scheduled runs. To display the shared value in its own column, click ![Options icon](https://assets.postman.com/postman-docs/aether-icons/action-options-stroke.svg#icon) **More** and select **Shared Value**.

To download environment variables, click ![Options icon](https://assets.postman.com/postman-docs/aether-icons/action-options-stroke.svg#icon) **View more actions** next to an environment and select **Export**.

To edit an existing environment variable, change the desired variable name, value, or description. To search for an environment variable by name or value, click ![Search icon](https://assets.postman.com/postman-docs/aether-icons/action-search-stroke.svg#icon) **Search**, and enter your search.

You can add and edit variables if you have Editor access to an environment. If you have Viewer access, you're restricted to updating the local value of existing variables. Any variables you edit are available to you, but not to collaborators in your [workspace](/docs/collaborating-in-postman/using-workspaces/create-workspaces/). Learn about [working with environments](/docs/sending-requests/variables/managing-environments/) in your team and [defining environment variables in scripts](#defining-variables-in-scripts).

You can also learn about [viewing and editing variables](#viewing-and-editing-variables-in-an-element) directly from a Postman element.

Changes to your variables are automatically saved.

### Defining collection variables

To view collection variables, click **Collections** in the sidebar, select a collection you want to view, then select **Variables**.

To add a new collection variable, do the following:

1. Click the **Add variable** text box and enter a variable name.
1. Enter the variable's value.
1. (Optional) Click ![Edit description icon](https://assets.postman.com/postman-docs/v11/icons/icon-edit-description-v11.jpg#icon) **Add description** next to the variable name and enter a description of the variable. To display the description in a separate column, click ![Options icon](https://assets.postman.com/postman-docs/aether-icons/action-options-stroke.svg#icon) **More** and select **Description**.
1. (Optional) Click ![Share icon](https://assets.postman.com/postman-docs/v11/icons/icon-cloud-v11.svg#icon) **Share** next to the value to share it with teammates and use it with monitors and scheduled runs. To display the shared value in its own column, click ![Options icon](https://assets.postman.com/postman-docs/aether-icons/action-options-stroke.svg#icon) **More** and select **Shared Value**.

To download collection variables, click ![Options icon](https://assets.postman.com/postman-docs/aether-icons/action-options-stroke.svg#icon) **View more actions** next to a collection, then click **More** and select **Export**. Learn more about [exporting a collection](/docs/getting-started/importing-and-exporting/exporting-data/).

To edit an existing collection variable, change the desired variable name, value, or description. To search for a collection variable by name or value, click ![Search icon](https://assets.postman.com/postman-docs/aether-icons/action-search-stroke.svg#icon) **Search**, and enter your search.

With Editor access to a collection, you can add new collection variables, share values with your teammates, and update shared values. You can also [define collection variables in scripts](#defining-variables-in-scripts). If you have Viewer access to a collection, you can only update the local value of existing collection variables. Learn how to [request Editor access to a collection](/docs/collaborating-in-postman/requesting-access-to-elements/#request-editor-access).

You can also learn about [viewing and editing variables](#viewing-and-editing-variables-in-an-element) directly from a Postman element.

Changes to your variables are automatically saved.

### Defining variables in scripts

You can set variables and vault secrets programmatically in your request scripts.

Method | Use case | Example
--- | --- | ---
`pm.globals` | Define a global variable. | `pm.globals.set("variable_key", "variable_value")`
`pm.collectionVariables` | Define a collection variable. | `pm.collectionVariables.set("variable_key", "variable_value")`
`pm.environment` | Define an environment variable in the current environment. | `pm.environment.set("variable_key", "variable_value")`
`pm.variables` | Define a local variable. | `pm.variables.set("variable_key", "variable_value")`
`pm.vault` | Define a vault secret in your Postman Vault. | `await pm.vault.set("secret_key", "secret_value")`
`unset` | Remove a variable. | `pm.environment.unset("variable_key")`

If you don't have Editor access to an environment, your script code will affect the local value but won't be synced or shared with your team.

Make sure you [enable scripts to access your vault secrets](/docs/tests-and-scripts/write-scripts/postman-sandbox-reference/pm-vault/). Otherwise, you'll receive an error in the Postman Console, and any code that comes after the method won't run. Also, you must use the `await` operator before each `pm.vault` method for it to run in your script.

For instructions on how to use variables in pre-request or post-response scripts, see [Using variables in scripts](#using-variables-in-scripts).

## Set a value as sensitive data

With [Editor](/docs/administration/roles-and-permissions/) access, you can set a global or environment variable as sensitive data. This masks the value, helping you avoid unintentionally sharing sensitive tokens, for example, to an unintended audience during screen sharing or live streaming. Postman stores variables as strings on the cloud. To learn about how Postman keeps your data safe, see [Security at Postman](https://www.postman.com/trust/security/).

Postman recommends that you use your [Postman Vault](/docs/sending-requests/postman-vault/postman-vault-secrets/) to store sensitive data, such as API keys, as encrypted vault secrets. Only you can access and use values associated with your vault secrets, and they aren't synced to the Postman cloud.

To set a variable value as sensitive data, do the following:

1. Open a [global](#defining-global-variables) or [environment](#defining-environment-variables) variable.
1. Click ![Key icon](https://assets.postman.com/postman-docs/aether-icons/descriptive-key-stroke.svg#icon) **Mark as sensitive** next to the variable name.

    ![Set environment variable as sensitive data](https://assets.postman.com/postman-docs/v11/environment-variable-sensitive-data-v11-60-4.jpg)

To set all variable values as sensitive data, click ![Options icon](https://assets.postman.com/postman-docs/aether-icons/action-options-stroke.svg#icon) **More** and select **Mark all sensitive**.

If you [share a value](#share-variable-values) that's set as sensitive data, Postman warns you about the outcome of sharing a sensitive value.

Your teammates can view the value of a variable set as sensitive data by clicking ![View icon](https://assets.postman.com/postman-docs/aether-icons/action-view-stroke.svg#icon) **Show** next to the variable's value.

To unset a variable value as sensitive data, do the following:

1. Open a [global](#defining-global-variables) or [environment](#defining-environment-variables) variable.
1. Click ![Key icon](https://assets.postman.com/postman-docs/aether-icons/descriptive-key-stroke.svg#icon) **Remove sensitive mark** next to the variable name. The value is no longer masked.

To unset all variable values as sensitive data, click ![Options icon](https://assets.postman.com/postman-docs/aether-icons/action-options-stroke.svg#icon) **More** and select **Unmark all sensitive**.

You can also learn how to [set a value as sensitive data from the VS Code extension](/docs/developer/vs-code-extension/send-requests/#store-variables).

## Using variables

You can use double curly braces (\"{{\" and \"}}\") to reference variables throughout Postman. For example, to reference a \"username\" variable in your request's authorization settings, use the following syntax:

```js
{{username}}
```

When you run a request, Postman resolves the variable and replaces it with your value. For example, you could have a request URL referencing a variable:

```js
https://postman-echo.com/get?customer_id={{cust_id}}
```

Postman sends the value stored for the "cust_id" variable when the request runs. If "cust_id" has a "3" value, the request is sent to the following URL with the query parameter:

```js
https://postman-echo.com/get?customer_id=3
```

If you want to access a variable from within a request body, wrap its reference in double-quotes:

```js
{ "customer_id" : "{{cust_id}}" }
```

You can use variables in request URLs, parameters, headers, authorization, body, and header presets.

When you hover over a variable, Postman shows its value and its scope. As you add variables to your requests, Postman displays any existing variables.

![Variable prompt](https://assets.postman.com/postman-docs/v11/var-prompt-v11-60.jpg)

The prompt indicates the local value, scope (highlighted by color), and ![Warning icon](https://assets.postman.com/postman-docs/aether-icons/state-warning-stroke.svg#icon) **Overridden** status where relevant. If a global or environment variable is set as [sensitive data](#set-a-value-as-sensitive-data), you can hover over the variable and click ![View icon](https://assets.postman.com/postman-docs/aether-icons/action-view-stroke.svg#icon) **Reveal** to show its value. You can also press and hold **â** or **Ctrl** to show the values for all variables set as sensitive data.

If a variable doesn't have a value, Postman highlights it in red. Also, a red exclamation point displays on ![Variable list icon](https://assets.postman.com/postman-docs/aether-icons/descriptive-variableList-stroke.svg#icon) **Variables** in the upper-right of the workbench. For information on how to fix this, see [Fixing empty variables](#fixing-empty-variables).

![Unresolved variable](https://assets.postman.com/postman-docs/v11/unresolved-variable-v11-18.jpg)

### Using dynamic variables

Postman provides dynamic variables you can use in your requests. Examples of dynamic variables include:

* `$guid` - A v4-style GUID.
* `$timestamp` - The current Unix timestamp, in seconds.
* `$randomInt` - A random integer between 0 and 1000.

See the [Use dynamic variables to return randomly generated data](/docs/tests-and-scripts/write-scripts/variables-list/) section for a full list.

### Using variables in scripts

You can retrieve your local value of a variable in your scripts using the object representing the scope level and the `.get` method:

```js
//access a variable at any scope including local
pm.variables.get("variable_key");
//access a global variable
pm.globals.get("variable_key");
//access a collection variable
pm.collectionVariables.get("variable_key");
//access an environment variable
pm.environment.get("variable_key");
//access a vault secret
await pm.vault.get("secret_key")
```

Using `pm.variables.get()` to access variables in your scripts gives you the option to change variable scope without affecting your script functionality. This method returns the variable that has the highest precedence (or narrowest scope).

Postman doesn't support using `pm.variables` to access and manipulate vault secrets.

To use [dynamic variables](#using-dynamic-variables) in pre-request or post-response scripts, use `pm.variables.replaceIn()`. For example:

```js
pm.variables.replaceIn('{{$randomFirstName}}')
```

See [Postman Sandbox API reference](/docs/tests-and-scripts/write-scripts/postman-sandbox-reference/overview/) for more details about scripting with variables.

#### Logging variables

You can log variable values to the [Postman Console](/docs/sending-requests/response-data/troubleshooting-api-requests/) while your requests run. Use the following syntax in your script to log the value of a variable:

```js
console.log(pm.variables.get("variable_key"));
```

To view the results, click ![Console icon](https://assets.postman.com/postman-docs/aether-icons/descriptive-console-stroke.svg#icon) **Console** in the footer. You can also access the Console by selecting **View > Show Postman Console**.

### Using data variables

The Collection Runner lets you import a CSV or a JSON file and use the values from the data file inside requests and scripts. You can't set a data variable inside Postman because it's pulled from the data file, but you can access data variables inside scripts, for example using `pm.iterationData.get("variable_name")`.

For more details, see [working with data files](/docs/collections/running-collections/working-with-data-files/) and the [Postman Sandbox API reference](/docs/tests-and-scripts/write-scripts/postman-sandbox-reference/overview/).

## Share variable values

You can choose to share global, environment, and collection variables, syncing the values with the Postman cloud. By default, variables have a local value that only you can access in your instance of Postman. [Share a variable value](#create-a-shared-value) to create a separate, shared value your teammates can access. You can also [update a shared value](#update-a-shared-value) and [stop sharing a value](#stop-sharing-a-shared-value).

Shared values are also used with Postman features that run on the Postman cloud, like scheduled collection runs, monitors, the Postman CLI, and Newman.

Once the value is shared, you and your teammates can continue to [work with your own local values](#work-with-shared-values) during development and testing, without affecting the shared value. You can reset your local value back to the shared value, if you'd like.

For more information on working with variables as a team, see [Work with environments as a team in Postman](/docs/sending-requests/variables/team-environments/).

You can also learn how to [share variable values from the VS Code extension](/docs/developer/vs-code-extension/send-requests/#store-variables).

### Create a shared value

You can create a shared value for a variable with Editor access to the element.

Be aware that the shared values of all variables are [published with your documentation](/docs/publishing-your-api/publishing-your-docs/). Make sure your shared values don't contain sensitive information such as passwords or tokens.

To share a variable with your teammates, do the following:

1. Create a [global](#defining-global-variables), [environment](#defining-environment-variables), or [collection](#defining-collection-variables) variable.
1. Click ![Share icon](https://assets.postman.com/postman-docs/v11/icons/icon-cloud-v11.svg#icon) **Share** next to the variable's value you'd like to share.

    If you've selected the ![Options icon](https://assets.postman.com/postman-docs/aether-icons/action-options-stroke.svg#icon) **More > Shared Value** view option, enter a value. The shared values automatically update.

    ![Share environment variable](