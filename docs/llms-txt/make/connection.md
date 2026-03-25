# Source: https://developers.make.com/custom-apps-documentation/create-your-first-app/apps-environment/connection.md

# Connections

When building the Connections component, you will set up the form that appears when the user clicks **Create a connection** in a module.

You will define the parameters the user has to input and how these are handled by the apps engine to verify the authentication parameters.

The Connections component defines the details needed to authenticate with the API and ensures everything works when the user enters their credentials in the scenario editor.

It has three main jobs:

1. to get any relevant information from the user that adds the connection (credentials, API key, etc.)
2. to process the authentication
3. to check if the authentication works by making a test API call

You set this up in the **Communication** tab, while the **Parameters** tab holds the information the user needs to provide.

The code in the **Communication** tab is divided into three sections:

<details>

<summary>Request</summary>

The first part defines the **HTTP request** the app uses to validate the user's credentials.

This call happens when the user enters their credentials and clicks **Create a Connection**.

The usual way to validate credentials is to call an API endpoint that returns user details. If the API doesn't provide this, you can use a generic endpoint to validate the credentials by making a GET request to ensure that the authentication is correct. The default HTTP method is **GET**, so you don’t need to specify it.

Adding this validation call is a good practice to make sure the credentials are correct.

</details>

<details>

<summary>Response</summary>

The second part contains directives on how to handle the **response**:

* **metadata**: Stores the user details that are returned by the API call and displays them next to the connection in the **Connections** page, for ease of identification.
* **error**: Contains instructions on the information that is displayed when an error occurs to help the user understand the issue. Lets you set the type of error and the message that will appear if the API request fails.

</details>

<details>

<summary>Log</summary>

The third part contains instructions regarding the **log** and the information recorded in it:

* **sanitize**: specifies which information shouldn't be recorded in the logs for security reasons.

</details>

The code in the **Parameters** tab contains only one parameter: `apiKey`. This is the information the user has to provide in the scenario. Note that the parameter is used in the **Communication** tab using the notation `{{parameters.name}}`.

## Set up connections for your Geocodify custom app

To set up the connections for your custom app:

{% stepper %}
{% step %}
In the Connections component, click **Create Connection**.

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-57c7211de0a7ca40ad6b931ca4827a48ab365d91%2Fconnections_createnew.png?alt=media" alt="" width="440"><figcaption></figcaption></figure></div>
{% endstep %}

{% step %}
Fill in the details of your connection.

* **Label:** Geocodify API key
* **Type:** API Key

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-17b46b7fd1acf3894575df8d41580313081bdbae%2Fconnections_createnew2.png?alt=media" alt="" width="369"><figcaption></figcaption></figure></div>
{% endstep %}

{% step %}
Click **Save**.
{% endstep %}

{% step %}
Select the **Parameters** tab and remove the default parameter that is present.
{% endstep %}

{% step %}
Copy and paste the following code:

```json
[
    {
        "name": "apiKey",
        "label": "API Key",
        "type": "password",
        "help": "Enter the API Key provided by Geocodify. For details, see the  [Geocodify account documentation](https://geocodify.com/account).",
        "required": true,
        "editable": true
    }
]
```

<table><thead><tr><th width="194" valign="top">Parameter</th><th valign="top">Description</th></tr></thead><tbody><tr><td valign="top"><strong>name</strong></td><td valign="top">Required. Internal name of the parameter. Use it when you want to retrieve the parameter</td></tr><tr><td valign="top"><strong>label</strong></td><td valign="top">Parameter name as displayed in the module.</td></tr><tr><td valign="top"><strong>type</strong></td><td valign="top">Required. Data <a href="../../../block-elements/parameters#type">type</a> of the parameter.</td></tr><tr><td valign="top"><strong>help</strong></td><td valign="top">Instructions for the user displayed in the module setup. Supports Markdown for text formatting.</td></tr><tr><td valign="top"><strong>required</strong></td><td valign="top">Specifies if the parameter is required.</td></tr><tr><td valign="top"><strong>editable</strong></td><td valign="top">(Only for the connection) Specifies if the user can edit and modify the connection from the Connections page in Make.</td></tr></tbody></table>
{% endstep %}

{% step %}
Click **Save changes**.
{% endstep %}

{% step %}
In the **Communication** tab, remove the code present.
{% endstep %}

{% step %}
Copy and paste the following code:

```json
{
	// Request
	"url": "https://api.geocodify.com/v2/geocode", // Absolute URL to the API endpoint which validates credentials
	"qs": { // Query parameters
		"api_key": "{{parameters.apiKey}}" // Authorizes user by api key, provided by user during the connection creation.
	},
	"response": {

		"error": { // Error handling
			"message": "[{body.meta.code}}] {body.meta.error_detail}}" // On error, returns error details

		}
	},
	"log": {
		"sanitize": [ // Excludes sensitive parameters from logs.
			"request.qs.api_key" ] // Omit query string apy_key
	}
}
```

<table><thead><tr><th valign="top">Code</th><th valign="top">Description</th></tr></thead><tbody><tr><td valign="top"><code>"url": "https://api.geocodify.com/v2/geocode",</code><br><code>"qs": {</code><br><code>"api_key": "{{parameters.apiKey}}"</code><br><code>},</code></td><td valign="top"><p>Request that the apps engine makes to validate the credentials.</p><ul><li><strong>url</strong>: Absolute URL of the endpoint that is used for validation.</li><li><strong>qs</strong>: Query string.</li><li><strong>api_key</strong>: Key of the <strong>qs</strong> parameter as specified by the API docs. This means that it will use the apiKey that the user provides.</li></ul></td></tr><tr><td valign="top"><code>"response": {</code><br><code>"error": {</code><br><code>"message": "[{body.meta.code}}] {body.meta.error_detail}}"</code><br><code>}</code><br><code>},</code></td><td valign="top"><p>Instructions on how to display any error: <strong>[error code] error message</strong>.<br></p><p>This information is typically present in the API docs. Since it isn’t available in this case, you need to retrieve it manually.</p><p>Send a request with incorrect credentials in Postman, then check the response body to identify where the error code and message appear.</p><p><br>If available, it's good practice to include the status code in the error response.</p></td></tr><tr><td valign="top"><code>"log": {</code><br><code>"sanitize": [</code><br><code>"request.qs.api_key" ]</code><br><code>}</code></td><td valign="top">Indicates to omit the <strong>api_key</strong> parameter present in the query string of the request from the log.</td></tr></tbody></table>
{% endstep %}

{% step %}
Click **Save changes**.
{% endstep %}
{% endstepper %}

Continue to set up the [Base](https://developers.make.com/custom-apps-documentation/create-your-first-app/apps-environment/base).
