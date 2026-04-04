# Create and manage vault secrets

[Add vault secrets](#add-sensitive-data-as-vault-secrets) to your Postman Vault and reuse them in your local instance of Postman. Then you can [reference vault secrets](#use-vault-secrets) in your HTTP collections and requests, variables, and the Collection Runner. Only you can access and use values associated with your encrypted vault secrets, and vault secrets aren't synced to the Postman cloud.

You can also [use Guided Auth to add vault secrets](/docs/sending-requests/postman-vault/manage-vault-secrets-using-guided-auth/) that have authentication credentials for public APIs, and reference them in your HTTP requests.

## Add sensitive data as vault secrets

After you [save your vault key](/docs/sending-requests/postman-vault/postman-vault-key/), you can add sensitive data, such as API keys and passwords, to your Postman Vault and reuse them in your local instance of Postman. From the HTTP request builder, you can [set existing data as a vault secret](#set-data-as-a-vault-secret). You can also set a value for a [vault secret that doesn't exist](#set-a-value-for-a-vault-secret-that-doesnt-exist) in your Postman Vault, and later [add the vault secret reference to your Postman Vault](#add-a-vault-secret-reference-to-your-postman-vault). Then you can [use vault secrets](#use-vault-secrets) in your local instance of Postman.

You can [set vault secrets in scripts](/docs/tests-and-scripts/write-scripts/postman-sandbox-reference/pm-vault/). Make sure you enable scripts to access your vault secrets. Otherwise, you'll receive an error in the Postman Console.

You can also [create an integration](/docs/sending-requests/postman-vault/postman-vault-integrations/) ([Enterprise teams only](https://www.postman.com/pricing/)) that connects your Postman Vault with external vaults, such as Azure Key Vault. This enables you to link vault secrets with sensitive data stored in external vaults, and reuse it in your local instance of Postman.

Vault secrets are deleted from your Postman Vault after signing out of Postman. Existing references to vault secrets will be empty when you sign in to Postman. You can [add your vault secrets to your Postman Vault](#add-a-vault-secret-reference-to-your-postman-vault) after you sign in to Postman.

To add secrets to your Postman Vault, do the following:

1. [Open your Postman Vault](/docs/sending-requests/postman-vault/postman-vault-secrets/#access-your-postman-vault).
1. Enter the following values in an empty row:
   
   * **Key** - The name of the vault secret. Use the name to [reference the secret](#use-vault-secrets).
   * **Value** - The value used when sending requests in your local instance of Postman. It's never synced to your account or shared with your team.
   
     To show or hide a vault secret's value, hover over the secret and click ![Image 1: View icon](https://assets.postman.com/postman-docs/aether-icons/action-view-stroke.svg#icon) **View** or ![Image 2: Hide icon](https://assets.postman.com/postman-docs/aether-icons/action-hide-stroke.svg#icon) **Hide**.
   
   * **Allowed domains** - The comma-separated list of domains and subdomains you're allowed to send requests to with the vault secret. This enables you to prevent unintentional disclosure of sensitive data in your vault secret. By default, you can include vault secrets in requests to any domain and subdomain.
   
     If you specify allowed domains or subdomains for a vault secret, you can only reference it at the request level.
   
     To allow sending requests to any subdomain of an allowed domain, use `*` to represent any subdomain. For example, add `*.example.com` to allow sending requests to any subdomain of `example.com`.
   
   ![Add secrets to Postman Vault](https://assets.postman.com/postman-docs/v11/add-postman-vault-secrets-v11-1.jpg)
   
   Changes are automatically saved to your Postman Vault.

### Set data as a vault secret

You can select data from the **URL builder**, **Params** tab, **Authorization** tab, or **Headers** tab and set the data as a vault secret. You can also enter a value with sensitive data in the **Authorization** tab and add it directly to your Postman Vault as a vault secret.

To select data and set it as a vault secret, do the following:

1. [Open your Postman Vault](/docs/sending-requests/postman-vault/postman-vault-secrets/#access-your-postman-vault).
1. Select the data you need. You can select data from the **URL builder**, **Params** tab, **Authorization** tab, or **Headers** tab.
1. Right-click the selected data and click **Set as variable**.
1. Click ![Image 3: Add icon](https://assets.postman.com/postman-docs/aether-icons/action-add-stroke.svg#icon) **Set as new variable**.
   
   ![Set as new variable](https://assets.postman.com/postman-docs/v11/set-data-as-new-vault-secret-v11-14.jpg)
   
1. Enter the **Name** of the vault secret, confirm that the **Value** is correct, and select **Vault** as the scope.
1. Click **Set Variable**.

To add sensitive data as a vault secret from the **Authorization** tab, do the following:

1. [Open your Postman Vault](/docs/sending-requests/postman-vault/postman-vault-secrets/#access-your-postman-vault).
1. Click the **Authorization** tab.
1. Click the **Auth type** dropdown list, then select an authorization.
1. Enter a value in a field that holds sensitive data, such as a password or token.
1. Hover over ![Image 4: Secret warning icon](https://assets.postman.com/postman-docs/aether-icons/state-secretWarning-stroke.svg#icon) **Sensitive value**, then click **Set as Variable**.
   
   ![Set as new variable](https://assets.postman.com/postman-docs/v11/set-sensitive-value-as-vault-secret-v11-39.jpg)
   
1. Enter a name for the vault secret.
1. Select **Local Vault**.

### Set a value for a vault secret that doesn't exist

Vault secrets that aren't added to your Postman Vault are useful for trying out a value. If the value works as expected, you can [add the vault secret to your Postman Vault](#add-a-vault-secret-reference-to-your-postman-vault). You can also create placeholder vault secrets to share with your API consumers. Your consumers can use the placeholder vault secret to add their own sensitive data to their Postman Vault.

You can create a vault secret reference in an HTTP request without adding the vault secret to your Postman Vault. The value you enter for this vault secret is stored locally and is only available in the request it's set in. In the [variables pane](/docs/getting-started/basics/navigating-postman/#environment-selector-and-variables-pane) under **Variables in request**, the vault secret isn't associated with your Postman Vault.

To create a vault secret reference that isn't added to your Postman Vault, [open your Postman Vault](/docs/sending-requests/postman-vault/postman-vault-secrets/#access-your-postman-vault), then enter a name that doesn't exist using the following syntax: `{{vault:secret-name}}`. You can enter a name in the **URL builder**, the **Params** tab, the **Authorization** tab, and the **Headers** tab.

![Set as new vault secret](https://assets.postman.com/postman-docs/v11/reference-and-create-new-vault-secret-v11-18.jpg)

To set a value for a vault secret that isn't added to your Postman Vault, hover over it, click **Enter value**, then enter a value. You can also click ![Image 5: Variable list icon](https://assets.postman.com/postman-docs/aether-icons/descriptive-variableList-stroke.svg#icon) **Variables** to open the variables pane, click **Enter value** next to a vault secret, then enter a value under **Variables in request**.

Values for vault secrets not added to your Postman Vault are stored locally in a request until you close its tab or sign out of Postman. When you open the request again, the vault secret's value will be empty. Optionally, you can [add the vault secret and its value to your Postman Vault](#add-a-vault-secret-reference-to-your-postman-vault).

### Add a vault secret reference to your Postman Vault

From a Postman element, such as a request or collection, you can create a vault secret and add it to your Postman Vault. This also enables you to define a default value for a [vault secret that's not added to your Postman Vault](#set-a-value-for-a-vault-secret-that-doesnt-exist). From the element, you can add a value that's stored in your Postman Vault that only you can access and use.

[Open your Postman Vault](/docs/sending-requests/postman-vault/postman-vault-secrets/#access-your-postman-vault), then enter a name for a vault secret that doesn't exist in your Postman Vault using the following syntax: `{{vault:secret-name}}`. Hover over the reference to the vault secret, click **Enter value**, enter the value, then click ![Image 6: Add icon](https://assets.postman.com/postman-docs/aether-icons/action-add-stroke.svg#icon) **Add to Vault**.

![Add secret to Postman Vault](https://assets.postman.com/postman-docs/v11/add-vault-secret-to-postman-vault-v11-18.jpg)

You can also click ![Image 7: Variable list icon](https://assets.postman.com/postman-docs/aether-icons/descriptive-variableList-stroke.svg#icon) **Variables** in the [workbench](/docs/getting-started/basics/navigating-postman/#environment-selector-and-variables-pane) to open the variables pane and view the vault secrets used in your request. Click **Enter value** next to the vault secret, enter a value, then click ![Image 8: Add icon](https://assets.postman.com/postman-docs/aether-icons/action-add-stroke.svg#icon) **Add to Vault**.

If you would like to store the value as a variable instead, remove the `vault:` prefix, then follow the instructions to [add the variable to a scope](/docs/sending-requests/variables/variables/#adding-variables-to-a-scope).

## Use vault secrets

You can reference vault secrets in your HTTP collections and requests from the **URL builder**, the **Params** tab, the **Authorization** tab, the **Headers** tab, and the **Body** tab. You can use the Collection Runner to [manually run collections](/docs/collections/running-collections/intro-to-collection-runs/) and [run performance tests](/docs/collections/performance-testing/performance-test-configuration/) that reference vault secrets. Scheduled collection runs, monitors, the Postman CLI, and Newman don't support vault secrets.

You can [access vault secrets in scripts](/docs/tests-and-scripts/write-scripts/postman-sandbox-reference/pm-vault/). Make sure you enable scripts to access your vault secrets. Otherwise, you'll receive an error in the Postman Console.

If you're using the Postman web app to send requests with references to vault secrets, use the [Postman Desktop Agent](/docs/getting-started/basics/about-postman-agent/#postman-desktop-agent). Postman recommends you [use the latest version](/docs/getting-started/basics/about-postman-agent/#update-the-postman-desktop-agent) of the Postman Desktop Agent to receive recent changes and improvements. You can also use the [Postman Browser Agent](/docs/getting-started/basics/about-postman-agent/#postman-browser-agent), but you may experience the CORS limitations of browsers.

If you're referencing vault secrets linked from an external vault, you must use the Postman desktop app. Learn about [external vault integrations](/docs/sending-requests/postman-vault/postman-vault-integrations/).

Put the vault secret inside double curly braces (`{{ }}`) and append the prefix `vault:` to the vault secret's name, enabling you to reference it throughout your workspaces. For example, to reference a vault secret named "postman-api-key", use the following syntax:

```txt
{{vault:postman-api-key}}
```

![Reference vault secrets in Postman](https://assets.postman.com/postman-docs/v11/use-postman-vault-secrets-v11-12.jpg)

To learn how to troubleshoot empty or unresolved vault secrets, see [Troubleshoot vault secrets](/docs/sending-requests/postman-vault/troubleshoot-vault-secrets/).

If you specified an allowed domain for a vault secret and you're sending a request to the domain, you can select a vault secret from the **Authorization** tab. Note that you can only add a vault secret this way from the request level. Select an authorization from the **Auth type** dropdown list, click a field that holds sensitive data, then select a vault secret from the dropdown list. You can click ![Image 9: View icon](https://assets.postman.com/postman-docs/aether-icons/action-view-stroke.svg#icon) **View secret value** to show the vault secret's value in the dropdown list.

![Select vault secret](https://assets.postman.com/postman-docs/v11/select-sensitive-value-vault-secret-v11-39.jpg)

From the variables pane, you can view vault secrets referenced in an HTTP request and available from a Postman element. Click ![Image 10: Variable list icon](https://assets.postman.com/postman-docs/aether-icons/descriptive-variableList-stroke.svg#icon) **Variables** in the workbench to open the variables pane. Review the vault secrets referenced in a request under **Variables in request**. If the request auth is set to [**Inherit auth from parent**](/docs/sending-requests/authorization/specifying-authorization-details/#inherit-authorization), you can view vault secrets referenced in the **Authorization** tab of the request's parent collection or folder. Under **All variables**, you can view vault secrets that can be referenced and resolved in the Postman element that's open. For requests that reference a variable or vault secret, click **All variables** to display all vault secrets a request can access.

![Vault secrets used in a request](https://assets.postman.com/postman-docs/v11/vault-secrets-used-in-a-request-v11-18.jpg)

Vault secrets stored in your Postman Vault are masked by default when they're logged to the [Postman Console](/docs/sending-requests/response-data/troubleshooting-api-requests/). To edit whether vault secrets are masked in the Postman Console, click ![Image 11: Setting icon](https://assets.postman.com/postman-docs/aether-icons/descriptive-setting-stroke.svg#icon) **Settings**, then turn the toggle on or off next to **Mask vault secrets** from the **Settings** tab.

If you're using the Postman web app with Safari as your web browser, it deletes vault secrets from your local instance of Postman after seven days of inactivity.

Use a different web browser if you want your vault secrets available for more than seven days without activity in the Postman web app.

Learn about the [browser requirements](/docs/getting-started/installation/system-requirements/#browser-requirements) for the Postman web app.

## Edit vault secrets

Edit vault secrets stored in your Postman Vault by updating them and their allowed domains, changing a vault secret's name, making vault secrets unavailable, or deleting vault secrets. You can also edit the value of vault secrets directly from requests that references it or can access it.

To edit vault secrets, [open your Postman Vault](/docs/sending-requests/postman-vault/postman-vault-secrets/#access-your-postman-vault). You can take the following actions:

* To filter the list of vault secrets by name, enter text in the **Filter secrets** box.
* To sort the list of vault secrets, click a column header. You can toggle between ascending and descending order.
* To add a new vault secret, click **Add new secret** in the bottom row of the table.
* To update the key or value for the vault secret, click the relevant cell.
* To delete a vault secret, hover over a secret and click ![Image 12: Delete icon](https://assets.postman.com/postman-docs/aether-icons/action-delete-stroke.svg#icon) **Delete**.
* To update the list of allowed domains, click the empty cell or list of domains.
* To make a vault secret unavailable without deleting it, clear the checkbox next to the secret. Any references to the secret will be unresolved. To make the secret available again, select the checkbox.
* To [link a different secret from an external vault](/docs/sending-requests/postman-vault/manage-postman-vault-integrations/#link-a-different-secret-from-an-external-vault), click ![Image 13: Setting icon](https://assets.postman.com/postman-docs/aether-icons/descriptive-setting-stroke.svg#icon) **Configure vault** next to the vault secret you want to update, then click ![Image 14: Edit icon](https://assets.postman.com/postman-docs/aether-icons/action-edit-stroke.svg#icon) **Edit**.

Changes are automatically saved to your Postman Vault.

You can also edit the value of a vault secret from the variables pane or the request builder. Click ![Image 15: Variable list icon](https://assets.postman.com/postman-docs/aether-icons/descriptive-variableList-stroke.svg#icon) **Variables** in the workbench to open the variables pane. You can edit vault secrets referenced in an HTTP request under **Variables in request** and vault secrets available from a Postman element under **All variables**. In the variables pane, delete the existing value next to a vault secret, then enter a new value. You can also hover over the reference to the vault secret in the request builder, delete the existing value, then enter a new value.

From the variables pane, you can't edit the value of a vault secret that's linked to an external vault.