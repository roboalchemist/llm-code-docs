# Source: https://developers.make.com/custom-apps-documentation/app-maintenance/updating-your-app/approved-apps/managing-breaking-changes.md

# Manage breaking changes

Ideally, the removal of the connections, modules, and fields should be announced to the users in advance.

Contact the [help desk](https://www.make.com/en/ticket) with a request for email notification to users.

## Common breaking changes

<table><thead><tr><th width="234.629638671875" valign="top">App's Element or Block</th><th valign="top">Breaking Changes</th></tr></thead><tbody><tr><td valign="top"><strong>Base</strong></td><td valign="top">Any changes might break scenarios.</td></tr><tr><td valign="top"><strong>Connection</strong></td><td valign="top">Changing the <code>refresh</code> call for OAuth connection.</td></tr><tr><td valign="top"><strong>Module's Communication</strong></td><td valign="top"><p>Changing <code>response.output</code>.</p><p>Changing <code>response.type</code>.</p><p>Adding <code>response.valid</code> for <code>2xx</code> response.</p><p>Changing <code>response.trigger</code>.</p><p>Adding a <code>condition</code>.</p><p>Adding an additional call (chaining request).</p><p>Changing a linked connection.</p></td></tr><tr><td valign="top"><strong>Module's Parameters</strong></td><td valign="top"><p>Adding a new <code>required</code> parameter.</p><p>Changing <code>required</code> from <code>false</code> to <code>true</code>.</p><p>Removing a parameter.</p><p>Changing <code>type</code> (If the original type can be coerced to the new type, it’s fine. e.g. number -> text. See <a href="https://help.make.com/type-coercion">type coercions</a>.</p><p>Adding <code>validate</code>.</p><p>Setting the select parameter <code>mappable</code> to <code>false</code>.</p><p>Setting the select parameter <code>dynamic</code> to <code>false</code>.<br>Removing or changing items in a list or dropdown.</p></td></tr><tr><td valign="top"><strong>Webhook's Communication</strong></td><td valign="top">Any changes might break scenarios.</td></tr><tr><td valign="top"><strong>RPC</strong></td><td valign="top"><p>Changing parameter <code>required</code> from <code>false</code> to <code>true</code>.</p><p>Changing RPCs building dynamic parameters.</p></td></tr><tr><td valign="top"><strong>Custom Functions</strong></td><td valign="top">Any changes might break scenarios.</td></tr></tbody></table>

## Remove a parameter from a module

It's important to avoid removing mappable parameters from a module without a clear indication or notification to the user. Even if it doesn't immediately cause a scenario to fail, it could still impact its functionality or disrupt the underlying process. Therefore, it's best to communicate any changes to the user. Also, the user should be able to see and work with the original input in the deprecated parameter/s.

In situations where a mappable parameter needs to be removed, there are several ways to handle the deprecation. The appropriate approach depends on the specific circumstances and how the API manages parameter deprecation in its endpoint.

Below, are methods ranked in order of least to greatest impact:

1. **Add the \[Deprecated] string to the module's label**

The parameter should be put into advanced parameters and the `[Deprecated]` string should be attached to the label. Additionally, you can add instructions to the help.

{% tabs %}
{% tab title="Occurrence in a module" %}

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-6d21473af5e08d4bdaa5b25ce166f421dd20e88a%2Fdeprecated_tag.png?alt=media" alt="" width="563"><figcaption></figcaption></figure></div>
{% endtab %}

{% tab title="Code in mappable parameters" %}

```json
[
    {
        "name": "firstName",
        "type": "text",
        "label": "First Name",
	"help":  "This field is a replacement for the deprecated `Name` field."
    },
	{
        "name": "lastName",
        "type": "text",
        "label": "Last Name",
	"help":  "This field is a replacement for the deprecated `Name` field."
    }, 
    {
        "name": "email",
        "type": "email",
        "label": "Email"
    },
    {
        "name": "name",
        "type": "text",
        "label": "Name [Deprecated]",
	"advanced": true,
	"help": "This field has been deprecated and divided into `First Name` and `Last Name` parameters."
    }
]
```

{% endtab %}
{% endtabs %}

2. **Add a banner**

If you need to make sure that the user notices the deprecated parameters, you can use the banner element.

There are three distinct message types available, each with a specific icon and guidelines for appropriate use. The **recommended length** of the message is **50 to 300 characters**.

{% tabs %}
{% tab title="Occurrence in a module" %}

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-437bccd9830dd0d61fdbca7fe7e17a19de437d29%2Fcustomapps_newinfobanner_blueexample.png?alt=media" alt="" width="470"><figcaption></figcaption></figure></div>
{% endtab %}

{% tab title="Code" %}

```json
{
    "type": "banner",
    "title": "This is an info",
    "text": "Here is a description of info.",
    "theme": "info"
}
```

{% endtab %}
{% endtabs %}

{% tabs %}
{% tab title="Occurrence in a module" %}

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-dc7e51385fce2c9e764a3a67ad400d8030db2bb9%2Fcustomapps_newinfobanner_yellowexample.png?alt=media" alt="" width="475"><figcaption></figcaption></figure></div>
{% endtab %}

{% tab title="Code" %}

```json
{
	"type": "banner",
	"title": "This is a warning",
	"text": "Here is a description of warning.",
	"theme": "warning"
}
```

{% endtab %}
{% endtabs %}

{% tabs %}
{% tab title="Occurrence in a module" %}

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-fe865fbdb68643adea945147df1a22c59ede286c%2Fbanner_warning.png?alt=media" alt="" width="563"><figcaption></figcaption></figure></div>
{% endtab %}

{% tab title="Code" %}

```json
{
	"type": "banner",
	"title": "Headline, if needed...",
	"text": "Minimum recommended length of message text. (50 characters)",
	"theme": "danger"
}
```

{% endtab %}
{% endtabs %}

3. **Perform an additional check before the request is sent and throw an error if the deprecated parameter is present in the payload**

If the called API service is too strict about using the deprecated parameters, you can do the error execution on the app's side.

{% tabs %}
{% tab title="Occurrence in a module" %}

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-bd28338a8018f2ec692f47a9e8417da321969a83%2Fdeprecated_showerror.png?alt=media" alt="" width="563"><figcaption></figcaption></figure></div>
{% endtab %}

{% tab title="Code in communication" %}

```json
[
	{ // when parameter name exists
	"condition": "{{parameters.name}}", 
        "response": {
            "valid": {
                "condition": false, //to throw response as error
		"type": "DataError",
                "message": "You can't use the parameter 'name' as it has been removed.\nPlease read the module's note message."
            }
        }  
    },
    { // when parameter name doesn't exist
	"condition": "{{!parameters.name}}",
        "url": "/api/users",
        "method": "POST",
	"body": "{{omit(parameters, 'name')}}",
        "response": {
			"output": "{{body}}"
		}
	}
       
]
```

{% endtab %}
{% endtabs %}

## Shut down a module

If you need to make sure that the module is not used anymore, you can throw an error whenever the module is executed.

{% tabs %}
{% tab title="Occurrence in a module" %}

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-bd28338a8018f2ec692f47a9e8417da321969a83%2Fdeprecated_showerror.png?alt=media" alt="" width="563"><figcaption></figcaption></figure></div>
{% endtab %}

{% tab title="Code in communication" %}

```json
{
        "response": {
            "valid": {
                "condition": "{{'a' === 'b'}}",
                "message": "You can't use this module anymore as it has been shut down.\nPlease read the module's note message."
            }
        }
  }
```

{% endtab %}
{% endtabs %}

## Deprecate a connection

If you need to deprecate a connection, create a new connection to use as the functional alternative and rename the now-deprecated connection so it contains the `(deprecated)` string.

Then, do the following:

{% stepper %}
{% step %}
Remove the current primary connection.
{% endstep %}

{% step %}
Map the new connection as the primary connection.
{% endstep %}

{% step %}
Map the deprecated connection as the alternative connection.
{% endstep %}
{% endstepper %}
