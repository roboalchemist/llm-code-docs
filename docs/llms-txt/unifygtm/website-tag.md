# Source: https://docs.unifygtm.com/developers/intent-client/website-tag.md

# Website Tag

> Quickly set up the Unify Intent client on a static marketing website.

## Installation

You can automatically load and install the client by placing a `<script>` tag in the `<head>` or `<body>` of your website's HTML. The minified script can be found [here](https://app.unifygtm.com/dashboard/settings/integrations/unify-intent-client) in Unify.

### HTML Example

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <!-- Your Unify JavaScript tag here -->
  </head>
  <body>
    <!-- Or here... -->
  </body>
</html>
```

Once added, there's nothing else you need to do to start collecting intent data. The website tag will automatically start collecting both page views and user identifications.

> Be sure to only initialize the client one time on your website.

If you'd like to manually trigger events in specific places on your website, you can do so by calling the client directly. When you include the tag in your HTML, you will immediately be able to access the client at `window.unify` (or simply `unify` since `window` is global).

```js
// Trigger a `page` event
window.unify.page();
unify.page();

// Trigger an `identify` event
window.unify.identify("user@email.com");
unify.identify("user@email.com");
```

## Additional Instructions

If you're using one of the tools below, you can follow the provider-specific instructions for that tool to install the website tag.

### Google Tag Manager

The Unify Intent website tag can be added using Google Tag Manager. This can be useful in certain situations, such as if you have lots of scripts on your website and prefer to manage them all in one place.

Start by opening the Google Tag Manager console. Add a new tag by selecting **Tags -> New**. Click on the **Tag Configuration** section and choose the **Custom HTML** tag type.

Copy the website tag script from the Unify settings page [here](https://app.unifygtm.com/dashboard/settings/integrations/unify-intent-client) and paste it into the HTML field. Once it's added, click **Save**.

![Google Tag Manager Install](https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/developers/intent-client/google-tag-manager-install.png?fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=70b042e703a2fa60a96e4ab8ec8389c7)

Lastly, be sure to enable support for `document.write` in the tag settings. This is required for the website tag to work correctly.

For more information, see the official Google Tag Manager support docs [here](https://support.google.com/tagmanager/answer/6107167).

### Webflow

Webflow has a dedicated section for adding custom code to your website. From the Webflow dashboard, navigate to the settings for your website and then select the **Custom code** tab in the sidebar.

Under **Head code**, paste the website tag script from the Unify settings page [here](https://app.unifygtm.com/dashboard/settings/integrations/unify-intent-client) in the text area. Be sure to create a new line between any existing code and the Unify script.

![Webflow Install](https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/developers/intent-client/webflow-install.png?fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=52a753bc219787d46885e76a5f54b326)

When you're done, click **Save** and then publish your changes by selecting **Publish -> Publish to selected domains** in the top right corner.