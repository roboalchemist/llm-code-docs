# Source: https://developers.make.com/custom-apps-documentation/app-components/base.md

# Source: https://developers.make.com/custom-apps-documentation/best-practices/base.md

# Source: https://developers.make.com/custom-apps-documentation/create-your-first-app/apps-environment/base.md

# Base

The Base component contains the common settings of the app that are inherited by all modules.

The common settings include:

* **Base URL**: The API base URL used as the main address for all requests to the API.
* **Authorization**: Authentication information and credentials.
* **Error Handling and Sanitization**: Same as the Connections component.

**If a module doesn’t define a setting, it follows what’s in the Base**. However, if a module specifies a different value for the same setting, for example a different error handling directive, this overrides what's present in the Base.

The Base component is the code where you specify the common directives and the common data if needed. When you create a new app, the Base is filled in with default code.

<figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-65ad94244aa82a44f463d2e9c3051f4066966e2b%2Fbase_defaultcode.png?alt=media" alt="" width="563"><figcaption></figcaption></figure>

## Set up Base for your Geocodify custom app

To set up the Base for your custom app:

{% stepper %}
{% step %}
Remove the default code that is present.
{% endstep %}

{% step %}
Copy and paste the following code:

```json
{
	// Default request configuration
	"baseUrl": "https://api.geocodify.com/v2", // Default base URL for all modules and RPCs.
	"qs": { // Default query parameters for all modules.
		"api_key": "{{connection.apiKey}}" // API key, which user will provide in the connection as parameter.
	},

	// Default response handling
	"response": {
		"error": { // Error handling
			"message": "[{{body.meta.code}}] {{body.meta.error_detail}}" // On error, returns error detail
		}
	},

	"log": {
		"sanitize": [ // Excludes sensitive parameters from logs.
			"request.qs.api_key" // remove api_key query param from logs.
		]
	}
}
```

<table><thead><tr><th width="382" valign="top">Code</th><th valign="top">Description</th></tr></thead><tbody><tr><td valign="top"><code>"baseUrl": "https://api.geocodify.com/v2",</code></td><td valign="top">Contains the base URL of the API. Note that it contains the API version.</td></tr><tr><td valign="top"><code>"api_key": "{{connection.apiKey}}"</code></td><td valign="top">Contains the query parameter for authentication.<br><br>Note that the apiKey parameter is taken from the Connections component and accessed using connecotin.apiKey.</td></tr><tr><td valign="top"><code>"response": {</code><br><code>"error": { // Error handling</code><br><code>"message": "[{{body.meta.code}}] {{body.meta.error_detail}}"</code><br><code>}</code><br><code>},</code></td><td valign="top">Instructions on how to handle errors.<br><br>Note that in this case the code is the same as in the Connections component.</td></tr><tr><td valign="top"><code>"log": {</code><br><code>"sanitize": [</code><br><code>"request.qs.api_key"</code><br><code>]</code><br><code>}</code></td><td valign="top"><p>Instructions on the information that is saved in the logs.<br></p><p><strong>sanitize</strong> specifies what needs to be omitted.</p><p><br>Note that in this case the code is the same as in the <strong>Connections</strong> component.</p></td></tr></tbody></table>
{% endstep %}

{% step %}
Click **Save changes**.
{% endstep %}
{% endstepper %}

Continue to set up the [module](https://developers.make.com/custom-apps-documentation/create-your-first-app/apps-environment/module).
