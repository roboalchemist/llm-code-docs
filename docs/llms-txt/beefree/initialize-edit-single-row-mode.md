# Source: https://docs.beefree.io/beefree-sdk/rows/reusable-content/sync/initialize-edit-single-row-mode.md

# Initialize Edit Single Row Mode

{% hint style="info" %}
This feature is available on Beefree SDK [Core plan](https://developers.beefree.io/pricing-plans) and above. Upgrade a [development application](https://docs.beefree.io/beefree-sdk/getting-started/readme/development-applications) at no extra charge to explore features from higher plan tiers. **Note:** Usage on a development application still counts toward [usage-based fees](https://devportal.beefree.io/hc/en-us/articles/4403095825042-Usage-based-fees) and limits.
{% endhint %}

## How it works <a href="#how-it-works" id="how-it-works"></a>

Our builders offer ready-to-go rows to your end-users, which provide both structure and content to create contents faster. With Edit Single Row mode you can offer an easier way for your users to modify a single row with a tailored UI built to edit the row structure, content, and style settings without worrying about messing up with the overall design of the email campaign, landing page, or pop-up.

Edit Single Row mode complements the [Saved Rows](https://docs.beefree.io/beefree-sdk/rows/storage/self-hosted-saved-rows) as it allows a complete control over the content of individual rows (e.g. the footer that requires to be updated) without the need to intervene into a full template, this will help you in implementing a more effective way to manage libraries of Saved Rows with a streamlined design process.

### **Initializing the editor in Edit Single Row Mode**

```javascript

type ClientConfig = {
  workspace?: {
    editSingleRow?: boolean
    // ....
  }
  // ....
}

const beeConfig: ClientConfig = {
  workspace:{
    editSingleRow: true
    // ....
  }
  // ....
}


// Create the instance 
function BeePlugin.create(token, beeConfig, (beePluginInstance) => { 
  //.... 

  beePluginInstance.start(template, { shared: false })
}

```

When a builder application is initialized with this mode enabled the UI will show to the user only properties that pertain to editing a single row, therefore:

* the options to insert custom rows, saved rows, or new default rows are disabled,
* the **Settings tab** is unavailable, as those properties are specific to the entire document,
* when a row is selected on the editing stage, the action to **Delete**, **Duplicate**, **Comment**, **Save** are not available.

<figure><img src="https://806400411-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F8c7XIQHfAtM23Dp3ozIC%2Fuploads%2Fa2HyhoPzTONDU4AyYLZV%2Fimage1%20(1).png?alt=media&#x26;token=7583f7e7-9ffb-4dac-a589-259ba840f384" alt=""><figcaption></figcaption></figure>

## Implementing the Save action <a href="#implementing-the-save-action" id="implementing-the-save-action"></a>

The following describes the recommended workflow to implement the Save action in your host SaaS application when the Single Edit Row mode is enabled.

In case your application uses the default [Toolbar](https://docs.beefree.io/beefree-sdk/server-side-configurations/server-side-options/toolbar-options), you can leverage the save button to trigger the sequence of action to correctly save the row, the workflow is the same as the one documented in [saving-rows-workflow-for-developers](https://github.com/BeefreeSDK/beefree-sdk-docs/blob/main/rows/reusable-content/sync/broken-reference/README.md), in short :

1. The user clicks on the save button
2. A contentDialog of type saveRow will be triggered.

In case your application doesn’t use the default Toolbar you will need to handle the row saving in a different way, following a couple of examples:

* Calling the [save method](https://docs.beefree.io/beefree-sdk/getting-started/readme/installation/methods-and-events). It will trigger the on [onSave](https://docs.beefree.io/beefree-sdk/getting-started/readme/installation/methods-and-events) event with two arguments, one of them is the full message JSON that can be saved as a Saved Row (it’s the same JSON returned by the [onSaveRow](https://docs.beefree.io/beefree-sdk/getting-started/readme/installation/methods-and-events) event).

### Example:

```javascript

myCustomToolbarButton.onClick(() => beePluginInstance.save())
...

onSave: function (json, html) {
	myCustomApi.saveRow(json)
},

```

* Listening to the [onChange](https://docs.beefree.io/beefree-sdk/getting-started/readme/installation/methods-and-events) event. It will receive the updated full message JSON which again can be saved as a Saved Row.

### Example:

```javascript

onChange: function (json, response) {
	myCustomApi.saveRow(json)
},

```

## **Merging saved rows in existing messages**

An effective way to update saved rows across multiple templates is by [implementing the save action](https://docs.beefree.io/beefree-sdk/rows/reusable-content/create/save/implement-self-hosted-saved-rows) in combination with the [Content Services API](https://docs.beefree.io/beefree-sdk/apis/content-services-api), to handle a row update across multiple existing templates.
