# Source: https://docs.intelligems.io/personalizations/personalizations-faqs.md

# Experiences FAQs

<details>

<summary>Checklist: What to consider before activating a Experience</summary>

* **Unforeseen combinations:** Because a visitor can be subject to multiple Experiences at the same time, you should be careful when designing and targeting your Experiences to make sure that you don't create conflicts or unpredictable states for users. For example, you wouldn't want the same visitor to be redirected from page A to B but also from A to C. Likewise, you don't want a visitor experiencing a theme change as well as a template change where the new theme doesn't actually contain the new template. Try to avoid having too many broadly-targeted Experiences active at the same time and take stock of your Experiences regularly. Make sure you [follow the precautions ](https://docs.intelligems.io/personalizations/theme-personalization-precautions)when using theme changes.
* **Interactions with tests:** You should also be careful to make sure your active Experiences don't conflict with any active tests.
* **Performance of non-native changes:** While Experiences can help you enact quick site changes without the need to go into Shopify, some changes will likely perform better and more safely if they are implemented 'natively' in Shopify. For example, URL redirects, price changes, and theme changes targeting all visitors (rather than a specific audience) should ideally be done in Shopify. If you have the option, consider minimizing how many of these types of Experiences you run.

</details>

<details>

<summary>When does a visitor start seeing my Experience? And what happens if I stop it?</summary>

A site visitor starts seeing a Personalization the moment they become eligible for it, according to its targeting criteria. Even if they are not eligible on their first site visit or the first few pages they browse on your site, they still remain eligible.

The moment you stop a Personalization, visitors who saw the Personalization will cease to see it. This is critical for time-limited sales and events.

</details>

<details>

<summary>Do I need to be on a certain plan to use Experiences?</summary>

You can create and launch Experiences on any of our plans.

* The use of Content modifications (URL Redirect, Content Edit, Styles & JS, theme change, and template change) is available on all plans.
* The ability to test Offers requires the Plus or Blue plan.

When editing an active Experience you will not be able to add these types of modifications without the corresponding plan unless you first stop the Experience.

The Intelligems free trial will allow you to activate Experiences with all of the above modifications during your trial period.

[See our Pricing Page for more information](https://www.intelligems.io/pricing).

</details>

<details>

<summary>Why am I not able to Preview or why is Preview unavailable?</summary>

It may be that you are not in the target audience of the Experience, so Intelligems is effectively showing you what a visitor sees when they are outside the target audience. To "force" yourself into the Experience, click the "Include" button at the bottom right of the blue Preview widget in the Full Screen preview.

It may also be that you have paused an Experience that was once active but is now stopped. Intelligems currently does not support the preview of such Experiences. To get around this, you can duplicate the Experience and preview its duplicate, or stop the Experience temporarily.

It may also be that you have not yet saved your most recent changes in this Experience. The Preview shows only saved changes. Save your changes and then click Preview again. Read more on the [Previews](https://docs.intelligems.io/previewing-personalizations#tip-in-full-screen-preview-make-sure-to-include-yourself) page.

</details>

<details>

<summary>Can the same visitor be exposed to multiple Experiences at once?</summary>

Yes, absolutely! For example, a new visitor on a mobile device may be exposed to a "New Visitors" Experience with a "20% off" offer, and a "Mobile" Experience that moves the Call to Action button higher up on the page.

You should be careful when designing and targeting your Experiences to make sure that you don't create conflicts or unpredictable states for users. For example, you wouldn't want the same visitor to be redirected from page A to B but also from A to C. Likewise you don't want a visitor experiencing a theme change as well as a template change where the new theme doesn't actually contain the new template. You should try to avoid having too many broadly-targeted Experiences active at the same time.

You should make sure your active Experiences don't conflict with any active *tests*.

Experiences cannot be made mutually exclusive the way that tests can, but this feature is coming soon.

</details>

<details>

<summary>What happens if two Experiences seen by a visitor are in 'conflict'?</summary>

You should aim to avoid scenarios where the same visitor is exposed to two active Experiences that both use a theme change, a Template change on the same origin template, or similar. Intelligems will break the tie at random, potentially leading to unpredictable experiences.

</details>

<details>

<summary>When using a popup component in an Offer Experience, how can I prevent the pop-up from displaying on a specific page of my site?</summary>

On any page you want to remove the pop-up, add the following snippet. For example, to remove on the home page, add this snippet to `templates/index.liquid`

```
<style>
  #ig-discount-message-box {
    display: none;
  }
</style>
```

</details>

<details>

<summary>Can I make price changes to subscription products?</summary>

At this time, price changes are only supported for non-subscription products.

</details>

<details>

<summary>Can I use Experiences to serve different prices to different customer segments?</summary>

Intelligems allows you price products differently based on the customer, but you cannot raise prices over the Shopify list price for technical reasons.

</details>

<details>

<summary>What does Discount Synchronization Error mean and how do I fix it?</summary>

You may see a "Discount Synchronization Error" when you create, edit, start, or pause an offer. This means that Intelligems received an error from Shopify when updating your discounts in Shopify.

⚠️ **This may be affecting live Intelligems offers and your customers' ability to redeem them.**

The limitation is that you can only have 5 Automatic Discounts active in Shopify at any given time (see [Shopify docs](https://community.shopify.com/c/shopify-functions/app-automatic-discount-limitation/m-p/1966961/highlight/true#M349)). Intelligems does its best to combine all of the offers you create in the platform into as few discounts in Shopify.

You may have other apps or automatic discounts active that also count towards the limit. To check, navigate to Shopify Admin > Discounts and then add a filter for Status = Active and Method = Automatic.

To resolve this error, you can either:

* [Archive](https://docs.intelligems.io/offer-experiences/offers-limits#archiving-offers) existing Intelligems offers that you're no longer using within Intelligems
* Deactivate or delete non-Intelligems discounts that are currently active in Shopify

If neither of these actions resolve the error, please [reach out to our support team](https://portal.usepylon.com/intelligems/forms/intelligems-support-request) and we'd be glad to help!

</details>
