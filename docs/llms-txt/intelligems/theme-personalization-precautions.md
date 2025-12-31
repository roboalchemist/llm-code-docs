# Source: https://docs.intelligems.io/personalizations/theme-personalization-precautions.md

# Theme Experience Precautions

## Setting up Experiences involving a Theme Change

A few reminders to make sure your Theme Experiences runs smoothly:

* Make sure the [Intelligems script is installed](https://docs.intelligems.io/getting-started/adding-intelligems-script-to-your-theme) in all themes that you're testing! This is how we will hide the preview bar at the bottom of the theme. If you have checkout.liquid file, ensure you have installed the Intelligems script on this page as well, so that the preview bar is hidden at checkout. If you do not have checkout.liquid, the bar will be hidden automatically.
* Product page templates are set at the product level, and the template name must be available in the live theme. When testing two different themes, make sure the template names match, so that the templates you've chosen for each product exist in both themes. If the product pages look correct when previewing the test theme(s), then you're good to go!

## Ending Experiences involving a Theme Change

{% hint style="warning" %}
After ending a Theme Experience, we recommend you do not delete the theme that was present in the Experience for at least a month.
{% endhint %}

While the Experience is active, visitors are sent to draft themes, and their browser will "remember" which theme to open the next time they visit your store via a session cookie. Once the Experience is stopped, if a visitor who was exposed to the Experience re-visits your store and the cookie is still active, Shopify will load the draft theme, and Intelligems will then immediately reset them back to the live theme.

However, if the draft theme that was in the Experience has since been deleted, Intelligems won't be loaded and won't have the opportunity to reset the visitor's theme. Instead, the visitor sees an error from Shopify, since they're trying to load a theme that does not exist. So, its important to leave any themes that were in a Experience in draft mode (rather than deleting them) for at least 30 days after the Experience has been stopped, to ensure any returning visitors are reset back to the live theme correctly.
