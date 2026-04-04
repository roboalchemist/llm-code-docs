# Create and manage vault secrets using Guided Auth

[Use Guided Auth to add vault secrets](#add-authorization-as-vault-secrets-using-guided-auth) to your Postman Vault, enabling you to store authentication credentials for public APIs that set up Guided Auth. You can use vault secrets added using Guided Auth in your Postman team. Then you can [reference vault secrets added using Guided Auth](#use-vault-secrets-added-using-guided-auth) in new HTTP requests to the same public APIs. Only you can access and use values associated with your encrypted vault secrets, and vault secrets aren't synced to the Postman cloud.

Guided Auth enables you to set up authentication credentials for public APIs by following steps set up by API publishers. Once you set up your authentication credentials using Guided Auth, you can store them in your Postman Vault and reuse them throughout your workspaces.

Learn how to [explore public APIs](/docs/postman-api-network/explore/overview/) on the Postman API Network. If you're an API publisher, learn how to [set up Guided Auth for your public APIs in Postman](/docs/publishing-your-api/setting-up-authentication-for-public-apis/).

Guided Auth supports public APIs that require bearer, basic, API key, or OAuth 2.0 authentication credentials. If an API supports token refresh, Postman automatically refreshes OAuth 2.0 tokens that were stored in your Postman Vault using Guided Auth.

Vault secrets are deleted from your Postman Vault after signing out of Postman. Existing references to vault secrets are empty when you sign in to Postman. You can add your vault secrets to your Postman Vault using Guided Auth after you sign in to Postman.

To add authentication credentials as vault secrets using Guided Auth, do the following:

1. Open an HTTP request, and enter the URL for a public API that has Guided Auth set up, such as `https://api.getpostman.com/`.
    
    Learn how to [explore public APIs](/docs/postman-api-network/explore/overview/) on the Postman API Network.
    
2. Click the **Authorization** tab, click the **Auth Type** dropdown list, then select the authentication option you'd like to use under **Recommended setup**.
    
    If the public API has only one API authentication configured, you can click **Set up new authorization** when you enter the URL. This takes you directly to the instructions for getting your credentials.
    
    ![Set up new auth using Guided Auth](https://assets.postman.com/postman-docs/v11/set-up-new-auth-v11-16.jpg)
    
    ![Add credentials using Guided Auth](https://assets.postman.com/postman-docs/v11/guided-setup-add-credentials-v11-16.jpg)
    
3. Generate and enter your authentication credentials:
    
    * For APIs that require authentication credentials like tokens or API keys, follow the instructions to get your credentials. Then enter them in the field under **Auth credentials**.
    * For APIs that support OAuth 2.0, select **Authorize** to get your credentials and automatically enter the access token in the field under **Auth credentials**.
    
4. Click **Store Auth in Vault**.
    
    ![Store auth in Postman Vault](https://assets.postman.com/postman-docs/v11/store-auth-in-postman-vault-v11-16.jpg)
    
    If you haven't entered your vault key since signing in to Postman, you're asked to enter it.
    
5. Enter the **Auth method name** for the authentication credentials. By default, the auth method name is the public API's name, such as "Postman API", but you can use a different name if you'd like.
    
    The auth method name is used to categorize the vault secret in your Postman Vault. The auth method name is also used to generate the vault secret's key. For example, if you enter "Postman API Key" as the auth method name for an API key, the vault secret's key would be `postman-api-key:value`.
    
    If you use an auth method name that already exists in your Postman Vault, the existing auth method is overwritten.
    
6. Click **Store**. In the **Auth Type** dropdown list of the request, the auth method name is selected under **Stored in vault**.
    
    ![Stored credentials in Auth Type list](https://assets.postman.com/postman-docs/v11/auth-credentials-stored-in-postman-vault-v11-16.jpg)
    
To view your authentication credentials in your Postman Vault, select the created auth method name as the auth type, then click **View in vault**. You can also click ![Vault icon](https://assets.postman.com/postman-docs/aether-icons/descriptive-vault-stroke.svg#icon) **Vault** from the Postman footer. Learn more about [opening your Postman Vault](/docs/sending-requests/postman-vault/postman-vault-secrets/#access-your-postman-vault).
    
In your Postman Vault, vault secrets added using Guided Auth are stored under **Created with guided auth**, and they're categorized by the auth method name. Each vault secret's key name is automatically appended with a suffix, which you shouldn't edit:
    
* For APIs that require authentication credentials like tokens or API keys, the suffix represents the authentication type, such as `:token`.
* For APIs that support OAuth 2.0, multiple vault secrets are added to your Postman Vault, including the access token and other properties returned by the public API (like the token type). Each vault secret has a suffix that represents the value, such as `:accessToken` and `:tokenType`.

![Vault secret created with Guided Auth](https://assets.postman.com/postman-docs/v11/postman-vault-guided-auth-v11-60.jpg)

The allowed domains for the vault secret are autofilled with the domains and subdomains for the public API. This is a comma-separated list of domains and subdomains you're allowed to send requests to with the vault secret. This enables you to prevent unintentional disclosure of sensitive data in your vault secret. Postman uses this information to suggest [using saved authorization](#use-vault-secrets-added-using-guided-auth) in future HTTP requests to the domain or subdomain.

If allowed domains or subdomains are specified for a vault secret, you can only reference it at the request level.

## Use vault secrets added using Guided Auth

You can reference vault secrets that were added using Guided Auth from the **Authorization** tab of your HTTP requests. You can also use the Collection Runner to [manually run collections](/docs/collections/running-collections/intro-to-collection-runs/) and [run performance tests](/docs/collections/performance-testing/performance-test-configuration/) that reference vault secrets added using Guided Auth. Scheduled collection runs, monitors, the Postman CLI, and Newman don't support vault secrets added using Guided Auth.

You can [access vault secrets added using Guided Auth in scripts](/docs/tests-and-scripts/write-scripts/postman-sandbox-reference/pm-vault/). Make sure you enable scripts to access your vault secrets. Otherwise, you'll receive an error in the Postman Console.

If you're using Guided Auth from the Postman web app, use the [Postman Desktop Agent](/docs/getting-started/basics/about-postman-agent/#postman-desktop-agent). Postman recommends you [use the latest version](/docs/getting-started/basics/about-postman-agent/#update-the-postman-desktop-agent) of the Postman Desktop Agent to receive recent changes and improvements.

Click the **Authorization** tab of an HTTP request, and click the **Auth Type** dropdown list. Under **Stored in vault**, select the auth method name that has the stored authentication credentials you want to reference.

![Guided Auth credentials](https://assets.postman.com/postman-docs/v11/guided-auth-stored-in-vault-list-v11-16.jpg)

If the public API has only one API authentication configured, you can click **Use Saved Authorization** in the **URL builder**. This enables you to reference the vault secret with the authentication you generated using Guided Auth.

![Used saved Guided Auth credentials](https://assets.postman.com/postman-docs/v11/guided-auth-use-saved-auth-v11-16.jpg)

Vault secrets added using Guided Auth are inside double curly braces (`{{ }}`). The prefix `vault:` is appended to the vault secret's name, and a suffix is automatically appended with the authentication type. For example, a vault secret that stores an API key named "postman-api-key" uses the following syntax:

```txt
{{vault:postman-api-key:value}}
```

![Use vault secret stored using Guided Auth](https://assets.postman.com/postman-docs/v11/use-guided-auth-vault-secrets-v11-16.jpg)

To learn how to troubleshoot empty or unresolved vault secrets, see [Troubleshoot vault secrets](/docs/sending-requests/postman-vault/troubleshoot-vault-secrets/).

From the variables pane, you can view vault secrets that are referenced in an HTTP request and available from a Postman element. Click ![Variable list icon](https://assets.postman.com/postman-docs/aether-icons/descriptive-variableList-stroke.svg#icon) **Variables** in the workbench to open the variables pane. Review the vault secrets referenced in a request under **Variables in request**. Under **All variables**, you can view vault secrets that can be referenced and resolved in the Postman element that's open. For requests that reference a variable or vault secret, click **All variables** to display all vault secrets a request can access.

![View Guided Auth vault secret used in a request](https://assets.postman.com/postman-docs/v11/guided-auth-vault-secrets-used-in-a-request-v11-18.jpg)

Vault secrets in your Postman Vault added using Guided Auth are masked by default when they're logged to the [Postman Console](/docs/sending-requests/response-data/troubleshooting-api-requests/). To edit whether vault secrets are masked in the Postman Console, click ![Setting icon](https://assets.postman.com/postman-docs/aether-icons/descriptive-setting-stroke.svg#icon) **Settings**, then turn the toggle on or off next to **Mask vault secrets**.

If you're using the Postman web app with Safari as your web browser, it deletes vault secrets from your Postman Vault after seven days of inactivity. Use a different web browser if you want your vault secrets available for more than seven days without activity in the Postman web app. Learn about the [browser requirements](/docs/getting-started/installation/system-requirements/#browser-requirements) for the Postman web app.

## Edit vault secrets added using Guided Auth

You can edit vault secrets stored in your Postman Vault that were added using Guided Auth. Update the auth method name, update allowed domains, make vault secrets unavailable, and delete vault secrets. You can also edit the value of vault secrets added using Guided Auth from requests that reference it or can access it.

Be careful when editing vault secrets added using Guided Auth. This might cause your authentication credentials stored as vault secrets to not work as expected. Learn how to [troubleshoot vault secrets](/docs/sending-requests/postman-vault/troubleshoot-vault-secrets/).

To edit vault secrets added using Guided Auth, [open your Postman Vault](/docs/sending-requests/postman-vault/postman-vault-secrets/#access-your-postman-vault). You can take the following actions:

1. To filter the list of vault secrets by name, enter text in the **Filter secrets** box under **Created with guided auth**.
2. To sort the list of vault secrets, click a column header. You can toggle between ascending and descending order.
3. To update the key or value for the vault secret, click the relevant cell. Existing references to the vault secret are empty, meaning they won't have a value. Learn how to [add a value to an empty vault secret](/docs/sending-requests/postman-vault/manage-vault-secrets/#add-a-vault-secret-reference-to-your-postman-vault).
    
    Don't remove or change the suffix associated with each vault secret's key name.
    
4. To delete a vault secret, hover over a secret and click ![Delete icon](https://assets.postman.com/postman-docs/aether-icons/action-delete-stroke.svg#icon) **Delete**. This will remove the vault secret reference from requests that were using the auth method.
5. To update the list of allowed domains, click the empty cell or list of domains.
6. To make a vault secret unavailable without deleting it, clear the checkbox next to the secret. Any references to the secret are unresolved. To make the secret available again, select the checkbox.

Changes are automatically saved to your Postman Vault.

You can also edit the value of a vault secret from the variables pane or the request builder. Click ![Variable list icon](https://assets.postman.com/postman-docs/aether-icons/descriptive-variableList-stroke.svg#icon) **Variables** in the workbench to open the variables pane. You can edit vault secrets referenced in an HTTP request under **Variables in request** and vault secrets available from a Postman element under **All variables**. In the variables pane, delete the existing value next to a vault secret, then enter a new value. You can also hover over the reference to the vault secret in the request builder, delete the existing value, then enter a new value.