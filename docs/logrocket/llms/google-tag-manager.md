# Source: https://docs.logrocket.com/docs/google-tag-manager.md

# Google Tag Manager

Initialize the LogRocket JavaScript SDK with Google Tag Manager

If you use Google Tag Manager to manage third party scripts, you can use it to initialize LogRocket in your application. You will need to create a Custom HTML Tag for the LogRocket script and select a trigger for it. We recommend using the Window Loaded trigger.

To get started, create a new Custom HTML Tag in your Google Tag Manager instance and add both lines of the LogRocket script tag:

```html Script Tag
Add to your HTML:

<script src="https://cdn.logr-in.com/LogRocket.min.js"></script>
<script>window.LogRocket && window.LogRocket.init(YOUR_APP_ID);</script>
```

See example screenshot below. Note that the script tag is specific to your account, so we recommend copying directly from the [*Project Setup* section of the LogRocket *Settings*](https://app.logrocket.com/r/settings/setup):

<Image align="center" src="https://files.readme.io/a0eb2f363bcf727125f5d25ea67acd0a591c55a02a7fa9b11afcecb223f6fefe-image.png" />

<br />

If you don't already have an app ID, visit [https://app.logrocket.com](https://app.logrocket.com) to get one.

Next, select a trigger for the tag. We recommend Window Loaded, but you can also use Page View.

![](https://files.readme.io/90b8e57-Screen_Shot_2023-02-03_at_12.31.45_PM.png "Screen Shot 2023-02-03 at 12.31.45 PM.png")

> 📘 Gathering more data with LogRocket in GTM
>
> All methods available with the LogRocket JavaScript SDK are available when initializing via Google Tag Manager. These include [user identification](https://docs.logrocket.com/reference/identify), [DOM sanitization](https://docs.logrocket.com/reference/dom) and [network sanitization](https://docs.logrocket.com/reference/network), along with [custom events](https://docs.logrocket.com/reference/track).