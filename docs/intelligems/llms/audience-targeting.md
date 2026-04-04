# Source: https://docs.intelligems.io/general-features/targeting/audience-targeting.md

# Audience Targeting

## What is Intelligems Audience Targeting?

Limit and customize the audience of your tests to specific segments based on device, URL parameters, traffic source, and more.

By default, a test is shown to all visitors accessing your site. You may, however, choose to limit which visitors are exposed to a test. For example, you may wish to

* Test several treatments of a “welcome back” banner for **returning visitors only**
* Show a landing page test only to visitors arriving from a **social campaign**
* Include only visitors from **a specific country** or place them in a specific test group

Intelligems allows you to limit which visitors should be exposed to a test based on specific criteria. It also allows you to control which particular test group a visitor should be placed into. When setting up and modifying any type of test, you may choose from three different options to limit who should see your test:

* **Target by Common Audience:** limit based on common criteria such as new/returning, device, traffic source (ex: email vs social), and country
* **Target by Custom Audience:** limit by mixing any type of condition, including device, cookie, UTM parameters, and others into logical statements
* **Advanced Targeting:** specify which audiences should be assigned to which groups in the test and more

{% hint style="info" %}
**A note on how targeting works:**

Once a visitor matches the audience criteria, Intelligems assigns them to a test group and keeps them in that test group going forward. They will remain in that test group until the test or personalization is over (an exception is if you choose [Temporary Targeting](https://docs.intelligems.io/personalizations/targeting-personalizations/targeting-modes-for-personalizations#temporary-audience)).

If they don’t match an audience, Intelligems will check again on the next page load and every page after that. This is handy when you’re targeting only logged-in visitors, for example, since they may not be logged in the moment they arrive.

If the audience targeting rules change mid-test and a visitor has already been assigned to a group, they remain in that group even if they no longer match the audience. This ensures a consistent user experience.

You can use Advanced Targeting to change this behavior.
{% endhint %}

## Common Audiences

Common audiences allow you to target your test based one or more common criteria (called **“Conditions”**).

* **Device Type:** Target only users coming from desktop or mobile devices (tablet traffic is included with mobile traffic)
* **New or Returning Visitors**: Target only users who have visited your site before, or who are brand new

{% hint style="info" %}
We can only track if a visitor has been to your site since you installed Intelligems, but not before. We assign every visitor an Intelligems ID when they come to your website once our JavaScript is live in the site. We assign the Intelligems ID to the user's cookie. If a visitor has an Intelligems ID already, they are returning, and if we are assigning them an ID on that visit, they are new.
{% endhint %}

* **Source Sites:** target users from *one or more* common site sources, such as email, SMS, social, and others, without having to define your own detailed targeting conditions. These can be divided into two categories
  * **Common Categories:** Direct, Email, Referral, Organic Social, Paid Social, Organic Search, Paid Search, SMS. Site traffic is classified using the same [industry standard rules used by Google Analytics](https://support.google.com/analytics/answer/9756891?hl=en#list), mostly via combination of UTM parameters and referring domain.
  * **Common Sources:** Google, Facebook, Instagram, TikTok, Twitter. Intelligems classifies traffic using a combination of referring domain, UTM source, and user agent to capture traffic from all possible entry points including in-app browsers, websites, and more.
* **Country:** Target one or more countries.

{% hint style="info" %}
The source site logic is an approximation that may not perfectly classify all traffic. When using the traffic source feature to target tests or filter results, you may want to do a quick spot check to test that traffic is being directed as you expect. If you need more precision, you can always set up your own Custom Audience using UTM parameters and referring domain conditions. See the next section to find out more.
{% endhint %}

You may choose a single condition or a combination of conditions. If you combine conditions, a visitor must match ALL conditions to be included in your test. However, you may select multiple allowable values for country and source site. For example, you may limit a test to:

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-c43b876d234ab3c3487e280d25f85dfc2941971a%2FScreenshot%202025-04-07%20at%2010.56.40%E2%80%AFAM.png?alt=media" alt=""><figcaption><p><em>New visitors, on a mobile device, in any of the following countries: USA, Mexico, or Canada.</em></p></figcaption></figure>

## Custom Audiences

When Common audiences don’t suffice, Custom audiences allow you to define a very specific combination of criteria that a visitor must meet in order to be included in a test.

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-03797f04cb9a82935f9429e356f4eb22202bafd5%2FUntitled%20(1).png?alt=media" alt=""><figcaption><p>Here is an example of a Custom audience used to target a test to only mobile visitors in the USA that come from one of three social campaigns.</p></figcaption></figure>

**Structure**

You may be familiar with the structure of custom audiences from other e-commerce tools:

* A custom audience contains one or more **clauses.**
* Every clause contains one or more **conditions.**
* The conditions in a clause are OR-ed together. This means that if at least one of the conditions in a clause is met by a visitor, the clause is satisfied.
* The clauses are AND-ed together. This means that if there is more than one clause, all clauses must be satisfied.

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-3fe6f58e62ae726bf5cbaf92daaa5968ed4715f8%2FUntitled%20(2).png?alt=media" alt=""><figcaption><p>This one-clause audience targets anyone coming from Klaviyo marketing</p></figcaption></figure>

**Available Audience Conditions**

* **Device Type:** desktop or mobile devices (tablet traffic is included with mobile traffic)
* **New or Returning:** new or returning visitors
* **Source Sites:** common traffic sources
* **Country:** specific countries
* **URL Parameter:** check if a particular URL parameter is defined or matches a value or pattern. Out of box UTM parameters such as campaign, medium, and source are commonly used for targeting traffic from a particular campaign or platform.
* **Landing Page URL:** target only visitors who entered your site through a specific page or pages. If you frequently create ad campaigns that point to the same landing page, this can be an efficient way to target only visitors from these campaigns, rather than targeting by UTM parameters and frequently updating the test with new campaign UTM parameters.

{% hint style="info" %}
Landing Page URL conditions will consider the whole URL (`window.location.href`) when checking for filter equality.
{% endhint %}

{% hint style="info" %}
**Combining with Page Targeting:** You can use page targeting on a test with a Landing Page audience condition but users will not be placed into the test unless / until they visit the page specified in page targeting.
{% endhint %}

* **Referring Domain:** check if visitor arrived via link from a particular domain, such as Google, LinkedIn, Amazon, or other. Often used in combination with URL Parameters.
* **JavaScript Expression:** check if an arbitrary javascript expression of your choice evaluates to true. This is handy for many specialized scenarios: including only people that arrived via a particular landing page, excluding people arriving on any page that contains a certain element, excluding developers, and more. One example use case for this would be targeting Klaviyo subscribers. In order to do this, you could add the below to your theme code, and add localStorage.getItem('klaviyoIdentified') === 'true' to ur JavaScript targeting.

```
window.klaviyo.isIdentified((e) => {
    localStorage.setItem('klaviyoIdentified', e);
})
```

* **Cookie:** check if a particular cookie is set or matches a value or pattern. This is useful for targeting based on Shopify visitor characteristics, cart information, and previous behavior on the site.

{% hint style="info" %}
For security reasons, Intelligems can only identify first party cookies accessible by Javascript (not marked as “Secure”). Most cookies used for targeting should fall into this category. For example, when Klaviyo and Google Analytics are integrated with your site, their cookies are considered first party so can be used for targeting.
{% endhint %}

{% hint style="info" %}
**City & State Targeting:** This feature is coming soon. In the meantime you can target your tests to specific cities and states by using our Cookie-based targeting. Simply check to see if the "ig-location" cookie contains or does not contain a certain city, state, or international region/province (ex: Quebec) using capital letters. The example test below targets anyone in Oregon outside of Eugene.

<img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-5c41acc4fff950fcf6325f90f09599fd02b715b6%2Fimage.png?alt=media" alt="" data-size="original">
{% endhint %}

## Advanced Targeting

Rather than just identifying which visitors should be exposed to a test, Advanced Targeting additionally allows you to assign particular audiences to specific groups in the test, or to permanently exclude them.

This is done by creating multiple if-then clauses, where each clause allows you to build an audience (Common or Custom) and then choose how that audience should be treated by the test.

For each audience you define, Intelligems can take one of the following actions:

* **Assign it to a specific test group:** include the visitor in the test and assign a specific group. For example, to reach statistical significance faster you may want to place all international visitors in the Control Group (rather than excluding them), and distribute everyone else across several treatment groups.
* **Assign it a test group randomly:** include the visitor in the test and assign a test group as usual based on the %s defined in the test setup.
* **Exclude it from the test:** exclude the visitor from this test permanently. Intelligems will no longer assess whether they match the audience or not on subsequent page loads.
* **Do not assign it:** visitor will not be placed in the test but will also not be permanently excluded. Intelligems will re-assess every time they visit a new page.

You might use Advanced Audiences to allocate specific ad campaigns to specific groups. For example: if `utm_campaign = fb_123abc` then assign to `Group A`, else if `utm_campaign = fb_456xyz` then assign to `Group B`, else leave unassigned. This will put all traffic from the first campaign into Group A and the second campaign into Group B, but leave everyone else out of the test. This way you can make sure your ads match each website experience you’re testing.

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-3233c1ef809889696fc49d15bad8fef83acccb22%2FUntitled%201.png?alt=media" alt=""><figcaption></figcaption></figure>
