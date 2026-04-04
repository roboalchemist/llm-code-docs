# Source: https://docs.intelligems.io/personalizations/targeting-personalizations.md

# Adding Targeting to a Personalization

## **Audience Targeting**

Intelligems offers three ways of picking an audience for an Personalization.

* **Common Audience:** limit to users on certain devices, new or returning, channels, or countries. You can read about this in depth [**here**](https://docs.intelligems.io/content-testing/targeting/audience-targeting).
* **Custom Audiences:** use additional conditions such as cookie, landing page, custom javascript, and define complex logic to combine them. You can read about this in depth [here](https://docs.intelligems.io/general-features/targeting/audience-targeting#custom-audiences).
* **Link-based:** This option is used if you would prefer for the Personalization to only be accessible for a link. Intelligems will create a custom link for you, which you will then need to use in the locations you wish to drive traffic from. \*\*\*\*To use this option, select "Link" and input what page you'd like visitors to land on - if not just the homepage. After saving your Personalization, your unique link will be accessible here or from the Personalization list. You can change this link at any time if you’d prefer to have some people land on a different page. The Intelligems link builder simply appends a special parameter to whatever URL you specify, which ensures that a visitor coming through that link is assigned that Personalization going forward as long as it’s active - regardless of the presence of the link on subsequent visits.

{% hint style="info" %}
**Audiences ignored in Tests:** Intelligems allows you to test Offers against each other to see which one is more effective before activating it. Note that the audience targeting rules of individual Personalizations are ignored when testing in lieu of test-wide audience targeting settings. [Learn more about testing Offers](https://docs.intelligems.io/offer-personalizations/testing-offer-personalizations).
{% endhint %}

## **Currency Targeting**

You can also show Personalizations only to users shopping in a certain currency if your site supports multiple currencies. This can be combined with any of the audience targeting settings.

Read more about currency targeting in the context of tests [here](https://docs.intelligems.io/general-features/targeting/currency-targeting).

## **Page Targeting**

By default, your modifications apply to all site pages. But you may for example decide that a certain popup or javascript button behavior should be limited only to one or more product pages. Use Page Targeting to limit which pages your modifications apply to.

Page targeting can be used if your Modifications are limited to Template Changes, Content Edits, CSS/JS, and Offers.

Note that the same targeting applies to all modifications in the Personalization. There is currently no way to limit some Modifications to one page and others to another. Here is how page targeting acts for each modification:

* Template change, Onsite Edits, CSS/JS: the changes are only shown on selected page(s)
* Offers: popup components only display on selected page(s). There is no way to hide updated prices, progress bar components, or quantity buttons from the cart and checkout pages.

## Next Steps

Once you’ve set up your Targeting, you can go on to:

* **Preview:** Make sure everything looks and functions correctly on your site before activating the Personalization. Click [here](https://docs.intelligems.io/personalizations/previewing-personalizations) to read our Preview guide.
* **Activate the** **Personalization:** You can pause and resume as many times as you need, which helps with recurring promotions.
