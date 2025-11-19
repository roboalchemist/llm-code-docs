# Source: https://docs.unifygtm.com/developers/intent-client/website-tag.md

# Website Tag

> Quickly set up the Unify Intent client on a static marketing website.

# Installation

You can automatically load and install the client by placing a `<script>` tag in the `<head>`
or `<body>` of your website's HTML. The minified script can be found [here](https://app.unifygtm.com/dashboard/settings/integrations/unify-intent-client)
in Unify.

```html index.html theme={null}
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

Once added, there's nothing else you need to do to start collecting intent data.
The website tag will automatically start collecting both page views and user
identifications.

<Warning>
  Be sure to only initialize the client one time on your website.
</Warning>

If you'd like to manually trigger events in specific places on your website, you
can do so by calling the client directly. When you include the tag in your HTML,
you will immediately be able to access the client at `window.unify` (or simply
`unify` since `window` is global).

```js Console theme={null}
// Trigger a `page` event
window.unify.page();
unify.page();

// Trigger an `identify` event
window.unify.identify("user@email.com");
unify.identify("user@email.com");
```

## Additional instructions

If you're using one of the tools below, you can follow the provider-specific
instructions for that tool to install the website tag.

<AccordionGroup>
  <Accordion title="Google Tag Manager">
    The Unify Intent website tag can be added using Google Tag Manager. This can
    be useful in certain situations, such as if you have lots of scripts on your
    website and prefer to manage them all in one place.

    Start by opening the Google Tag Manager console. Add a new tag by selecting
    **Tags -> New**. Click on the **Tag Configuration** section and choose the
    **Custom HTML** tag type.

    Copy the website tag script from the Unify settings page [here](https://app.unifygtm.com/dashboard/settings/integrations/unify-intent-client)
    and paste it into the HTML field. Once it's added, click **Save**.

    <Frame>
      <img src="https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/developers/intent-client/google-tag-manager-install.png?fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=70b042e703a2fa60a96e4ab8ec8389c7" data-og-width="3456" width="3456" data-og-height="1818" height="1818" data-path="images/developers/intent-client/google-tag-manager-install.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/developers/intent-client/google-tag-manager-install.png?w=280&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=eeaef22dd75d0290b76f5e161add140c 280w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/developers/intent-client/google-tag-manager-install.png?w=560&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=11a5630d0ff610dcb5fcd63dd408a888 560w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/developers/intent-client/google-tag-manager-install.png?w=840&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=f134f061fbf6d9d70e633b0527db859e 840w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/developers/intent-client/google-tag-manager-install.png?w=1100&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=9e4238c61c0c94f853e5743cd2976021 1100w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/developers/intent-client/google-tag-manager-install.png?w=1650&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=4dc9d6fc34d853bc86653669d5a3cef1 1650w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/developers/intent-client/google-tag-manager-install.png?w=2500&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=b93d87253807815c6abd22f1e30ff0cc 2500w" />
    </Frame>

    Lastly, be sure to enable support for `document.write` in the tag settings.
    This is required for the website tag to work correctly.

    For more information, see the official Google Tag Manager support docs
    [here](https://support.google.com/tagmanager/answer/6107167).
  </Accordion>

  <Accordion title="Webflow">
    Webflow has a dedicated section for adding custom code to your website. From
    the Webflow dashboard, navigate to the settings for your website and then
    select the **Custom code** tab in the sidebar.

    Under **Head code**, paste the website tag script from the Unify settings
    page [here](https://app.unifygtm.com/dashboard/settings/integrations/unify-intent-client)
    in the text area. Be sure to create a new line between any existing code and
    the Unify script.

    <Frame>
      <img src="https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/developers/intent-client/webflow-install.png?fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=52a753bc219787d46885e76a5f54b326" data-og-width="1858" width="1858" data-og-height="410" height="410" data-path="images/developers/intent-client/webflow-install.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/developers/intent-client/webflow-install.png?w=280&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=5d153df10eca89128e98dae41ff107fe 280w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/developers/intent-client/webflow-install.png?w=560&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=05f704ddbba9207397c81d161c71c891 560w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/developers/intent-client/webflow-install.png?w=840&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=5b6b3735a1ba5b3f03e7420836a669ce 840w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/developers/intent-client/webflow-install.png?w=1100&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=85e7c9f271aede29cf1fca684eeccf79 1100w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/developers/intent-client/webflow-install.png?w=1650&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=3c8d2905d30c80a4b7b30dfa9fd85d4f 1650w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/developers/intent-client/webflow-install.png?w=2500&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=32f69b885ca1475ee8aa59e6d85b23eb 2500w" />
    </Frame>

    When you're done, click **Save** and then publish your changes by selecting
    **Publish -> Publish to selected domains** in the top right corner.
  </Accordion>
</AccordionGroup>

# Usage

Once the website tag is installed, the Unify Intent client will automatically
start collecting events on your website. Most of the time, there is nothing else
you need to do.

For details on how this works and the available options, see [Configuration](/developers/intent-client/client-spec#configuration).
