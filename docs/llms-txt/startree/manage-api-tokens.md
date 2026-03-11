# Source: https://docs.startree.ai/corecapabilities/security/manage-api-tokens.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# API Token Management

This page describes how to create and manage API tokens within the StarTree environment. API tokens provide programmatic access to StarTree resources through role-based permissions.
They consist of an access key and a secret key, formatted as `st-<accessKey>-<secretKey>`.

## Generating an API token

1. Navigate to the Security Manager by browsing to [https://dp.your\_environment\_id.startree.cloud/security-manager](https://dp.your_environment_id.startree.cloud/security-manager).
2. Click **API Tokens** in the left navigation menu.
3. Click **Generate API token**.
4. Select the desired role for the token. This will determine the permissions that will be granted to the token.
   * For more information on roles and how they are defined, refer to the [Manage Access](manage-access) page.
5. Provide a description for the token. This will help you identify the token going forward.
6. Click **Generate API token** to generate the new token.
7. Copy the token and store it someplace safe.

<Warning>Copy the generated token immediately. This token will only be displayed once.</Warning>

## Managing API tokens

* **View Existing Tokens:** The API Tokens screen displays a list of all existing tokens, including their description, creation date, and their assigned role.
* **Delete a Token:** To delete an API token, locate the token in the API Tokens list, click the actions menu (three vertical dots to the right of the token description) and click **Delete**.

## Security considerations

* **Treat API tokens like passwords:** Store API tokens securely and never share them with unauthorized individuals.
* **Use strong security practices:** Implement appropriate security measures to protect your API tokens, such as:
  * **Assign least privilege:** Grant only the minimal necessary permissions to API tokens.
  * **Ensure regular rotation:** Regularly rotate API tokens to minimize the risk of unauthorized access.
  * **Use secure storage:** Store API tokens securely and avoid hardcoding them directly into applications.

## Important notes

* API tokens provide programmatic access to StarTree resources. Exercise caution when granting permissions to API tokens.
* Revoking an API token will immediately disable its access to StarTree resources.

## Test the API token

You can test the token using one of the following methods:

### Using CURL

To test the API token using CURL, include the token in the `--header` (`-H`) authorization parameter.

```
curl --location --request GET 'https://pinot.<your url>.cloud/appconfigs' \
--header 'Authorization: Bearer st-XkQBXKr652MV1VF9-5gkhGWNaGAdA1NU5yrHXRSPKMCcNRlRg'
```

### Using the Swagger API

1. In Pinot UI, click on **Swagger REST API**.
2. Click **Authorize**.
3. In the "Available authorizations" dialog, scroll up to see the `oauth` authorization option.
4. Enter `Bearer` (including the space), followed by the token in the **Value** textbox.

   <img width="610" alt="image" src="https://mintcdn.com/startree/xe5mTwlEdZc68KYh/corecapabilities/security/images/swagger_ui_authorize_dialog.png?fit=max&auto=format&n=xe5mTwlEdZc68KYh&q=85&s=5dfa2f76cb91b283d3d6ebcebba4353c" title="Swagger UI Authorize dialog" data-path="corecapabilities/security/images/swagger_ui_authorize_dialog.png" />
5. Click **Authorize**.
6. Find the API call you want to try and click the related **Try it out** button.

   <img width="610" alt="image" src="https://mintcdn.com/startree/xe5mTwlEdZc68KYh/corecapabilities/security/images/swagger_try_it_out.png?fit=max&auto=format&n=xe5mTwlEdZc68KYh&q=85&s=6a66ff834fd54406bbc764cad276b1cd" title="Swagger API screen" data-path="corecapabilities/security/images/swagger_try_it_out.png" />

## Extracting Username and Password from a StarTree Bearer Token

Certain integrations or tools require basic authentication (username and password) rather than bearer token authentication. In such cases, you can extract the equivalent username and password from your StarTree bearer token.

StarTree bearer tokens are formatted as `st-<accessKey>-<secretKey>`.

To extract the username and password:

1. Remove the `st-` prefix from the token.
2. The 16 characters immediately following the prefix (before the hyphen) constitute the username.
3. The 32 characters after the hyphen constitute the password.

**Example:**

Given the bearer token: `st-XkQBXKr652MV1VF9-5gkhGWNaGAdA1NU5yrHXRSPKMCcNRlRg`

* Username: `XkQBXKr652MV1VF9`
* Password: `5gkhGWNaGAdA1NU5yrHXRSPKMCcNRlRg`
  Use these credentials where basic username/password authentication is required for your Pinot connection.

Built with [Mintlify](https://mintlify.com).
