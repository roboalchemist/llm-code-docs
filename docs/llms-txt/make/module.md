# Source: https://developers.make.com/custom-apps-documentation/create-your-first-app/apps-environment/module.md

# Modules

In Make, you can set up [six different types of modules](https://developers.make.com/custom-apps-documentation/app-components/modules), each with a specific function.

In this tutorial, you will set up a Search module to retrieve the coordinates of an address.

The **Search module sends a request and returns multiple results**. Use this module when you want to let users search for records.

Inside the **Search module** component there are five tabs:

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-0af8add9b393414b328ff48e932c30bad30c55de%2Fmodule_tabs.png?alt=media" alt="" width="530"><figcaption></figcaption></figure></div>

<details>

<summary>Communication</summary>

Information on what the engine needs to do to manage the API call (call the endpoint, process the response, pagination, etc). Remember that the following elements are **inherited from the Base**: **base URL**, **error handling**, **log sanitize**. If something needs to be changed, you can write it here, and it will override the settings of the Base component.

</details>

<details>

<summary>Static parameters</summary>

Input parameters that the user cannot map from other modules. They are only used for polling triggers, which don't have mappable parameters.

</details>

<details>

<summary>Mappable parameters</summary>

Input parameters in the interface that the user can either enter manually or map from the output of other modules.

</details>

<details>

<summary>Interface</summary>

Labels of the module's output added to make the output more straightforward and easy to interpret. By specifying it, there’s no need to first run the module in your scenario to get the output structure for mapping the elements.

</details>

<details>

<summary>Samples</summary>

Examples of data to help the users set up the module.

</details>

## Create a Search module

To create a new module for your Geocodify app:

{% stepper %}
{% step %}
In the **Modules** tab, click **Create Module**.
{% endstep %}

{% step %}
In the pop-up window, fill in the module details. The chart below contains the values to use for your Geocodify app.

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-1c7a12913686cd077a6a3ef817570b6834573f97%2Fcreatemodule_newpopup.png?alt=media" alt="" width="362"><figcaption></figcaption></figure></div>

<table><thead><tr><th width="163" valign="top">Field</th><th valign="top">Values</th></tr></thead><tbody><tr><td valign="top"><strong>Template</strong></td><td valign="top">Blank module (you will set it up from scratch)</td></tr><tr><td valign="top"><strong>Type</strong></td><td valign="top">Search (to retrieve geolocation details)</td></tr><tr><td valign="top"><strong>Connection</strong></td><td valign="top">Geocodify API Key (the connection you have created earlier)</td></tr><tr><td valign="top"><strong>Name</strong></td><td valign="top">geocode</td></tr><tr><td valign="top"><strong>Label</strong></td><td valign="top">Search geolocation</td></tr><tr><td valign="top"><strong>Description</strong></td><td valign="top">Provides longitude, latitude, and place details of a location (address, name of a place, or location).</td></tr></tbody></table>
{% endstep %}

{% step %}
Click **Save**.
{% endstep %}

{% step %}
Click the Mappable Parameters tab for your new search module.
{% endstep %}

{% step %}
Copy and paste the following code:

```json
/// Defines "location" as module input parameters.
[
    {
        "name": "location_info", // Makes value accesible via "{{parameters.location_info}}".
        "label": "Location", // Sets the user friendly label visible in the module
        "type": "text", // Sets the type to text.
        "help": "Type the location you want to geolocate", // Sets the help text with an example under input field in the module.
        "required": true // Indicates this parameter is mandatory.
    }
]
```

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-fe17b595e9f24ace62dd02bbe24761baaa41d05b%2Fmappable_parameters_newapp.png?alt=media" alt="" width="563"><figcaption></figcaption></figure></div>

<table><thead><tr><th width="193" valign="top">Mappable parameters</th><th valign="top">Description</th></tr></thead><tbody><tr><td valign="top"><strong>name</strong></td><td valign="top">Required. Internal name of the parameter. Use it when you want to access the parameter using <code>{{parameters.name}}</code>.</td></tr><tr><td valign="top"><strong>label</strong></td><td valign="top">Parameter name displayed in the module setup.</td></tr><tr><td valign="top"><strong>type</strong></td><td valign="top">Required. Type of the parameter.</td></tr><tr><td valign="top"><strong>help</strong></td><td valign="top">Instructions for the user displayed in the module setup. It supports Markdown for text formatting.</td></tr><tr><td valign="top"><strong>required</strong></td><td valign="top">Specifies if the parameter is required.</td></tr></tbody></table>
{% endstep %}

{% step %}
Click **Save changes**.
{% endstep %}

{% step %}
Click the Communications tab for your new search module.
{% endstep %}

{% step %}
Copy and paste the following code:

```json
{
	// Request to API endpoint.
	"url": "/geocode", // Endpoint relative to base URL
	"method": "GET",
	"qs": {
		"q": "{{parameters.location_info}}" // Required query parameter. Parameter "location_info" is defined in Mappable parameters. 
	},

	// Response handling
	"response": {
		"output": "{{body}}" // Return the body of the response
	}
}
```

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-d3abbc240380b1c3727fbb93a438b5be9d24367f%2Fcommunication_newapp.png?alt=media" alt="" width="563"><figcaption></figcaption></figure></div>

<table><thead><tr><th width="169">Specification</th><th>Description</th></tr></thead><tbody><tr><td><strong>url</strong></td><td>The API endpoint. Since it starts with <code>/</code>, it is joined to the base URL. Note that if the URL starts with <code>https://</code>, it will override the base URL.</td></tr><tr><td><strong>method</strong></td><td>The default method is GET, so it could have been omitted in this case.</td></tr><tr><td><strong>qs</strong></td><td>Query parameter containing the location to geolocate. Note that you access it by using <code>parameters.location_info</code>.</td></tr><tr><td><strong>response</strong></td><td>Defines the output returned, which in this case is the whole body of the response.</td></tr></tbody></table>
{% endstep %}

{% step %}
Click **Save changes**.
{% endstep %}
{% endstepper %}

Leave all the other tabs as they are, including the **Interface**. This means that you won't apply any filtering or customization to the output, but all the information from the API will be returned as is.

Now you are ready to [test your app](https://developers.make.com/custom-apps-documentation/create-your-first-app/test-your-app).
