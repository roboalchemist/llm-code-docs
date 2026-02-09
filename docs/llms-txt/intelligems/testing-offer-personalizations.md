# Source: https://docs.intelligems.io/offer-personalizations/testing-offer-personalizations.md

# Testing Offers

Intelligems enables your org to run real-time split tests on different Offers. This article will walk you through how to run an Offers Test with Intelligems and some best practices.\
\
Watch the Looms or follow the steps below.\
\
Let's get started!

## Setting Up an Offer Test from Offer Creation Flow

{% embed url="<https://www.loom.com/share/3c872bdb406c4355a3785c1ee0f966fa>" %}

## Setting Up an Offer Test from Test Creation Flow

{% embed url="<https://www.loom.com/share/402158d0b8c845c39e07477e3b401e84?sid=73395dbc-8880-48dd-ba0d-dd94abcddadc>" %}

If you'd rather follow written steps, read below.

## Step 1: Create a new test

Navigate to the "A/B Tests" tab in the menu on the left-hand side of the Intelligems app. Once you're there, click 'Create New Test' above the experiments table. Select "Offers Test" and then "Create Test".

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-8e4eb709d4625c2cc600818b00fa6fad8120a7f1%2FScreenshot%202024-07-22%20at%2010.20.49%E2%80%AFAM.png?alt=media" alt="" width="563"><figcaption></figcaption></figure>

## Step 2: Enter the test details

Fill in the Test Name and Test Description for the experiment you are creating. This information is all internal; the more detail you include here the better! Tests can be live for several weeks, and your future self will thank you for including the details here.

You will also select your primary goal. This will not affect what data is tracked or available to view, but will allow Intelligems to display analytics so that the most important information is surfaced first.

## Step 3: Create your test groups

Create between two and five groups to include in the test by clicking on the ‘+’ button. Name the groups for the experiment and use the slider at the bottom of the page to allocate what percentage of traffic will go to each group.

{% hint style="info" %}
The more groups you have, the longer it will take to get statistically significant results. You’ll need about 300 orders for each group in the test to detect a 10% change in conversion with 90% confidence.
{% endhint %}

## Step 4: Select which Offer each group will be exposed to

Once you've created your groups, go to the Modifications step. Here, you will choose what kind of Offers you're testing for each group. You can:

* Leave a group untouched, as a no-offer group
* Build an offer by choosing an offer type and other optional modifications
* Or start by copying the contents of a Experience that contains an Offer. See more [here](https://docs.intelligems.io/personalizations/personalizations-getting-started) on how to set up a new Experience.

These details can be modified anytime during test setup and while the test is live.

{% hint style="info" %}
Your chosen Experience will remain untouched. It was simply used as a 'starting point' to copy Offer details from. We recommend you don’t activate it while the test is running in order to avoid overlapping Offers on your site.
{% endhint %}

## Step 5: Set up targeting if needed

Targeting is an optional step. By default, a visitor will be immediately assigned to one of the test groups using its random split-test mechanism. This assignment is determined at the first visit and is stored via a first‐party cookie, ensuring that the visitor remains in the same group on subsequent visits during the offers test period.

The targeting tool allows you to apply specific conditions to certain site visitors. There are a few different ways you can do this:

* **Audience Targeting:** limit your users based on their device, country, UTM parameters, landing page URL, new/returning, cookies, and much more.
* **Currency Targeting:** Limit your test to a single currency and/or a list of specific countries.
* **Mutual Exclusion:** Prevent users from being targeted by related experiments to reduce undesired interactions under the [Mutually Exclusive Tests](https://docs.intelligems.io/general-features/targeting/mutually-exclusive-experiments) option.

You can learn more about targeting [here](https://docs.intelligems.io/general-features/targeting).

{% hint style="warning" %}
**A note on targeting: If you had any targeting options set on the Offer Personalizations you used to define your test groups, these will be ignored in lieu of test-level targeting.**

* Personalization-level audience targeting is ignored. The audience targeting used on the test (or lack thereof) is used in its place.
* Personalization-level currency targeting is ignored. The currency targeting used on the test (or lack thereof) is used in its place.
* Personalization-level page targeting is ignored. The page targeting used on the test (or lack thereof) is used in its place.
  {% endhint %}

## Step 6: Save your test and start it

Once you have completed all the steps, you'll be able to save your test with the button in the bottom right. You can then start it whenever you're ready.

{% hint style="success" %}
Don’t worry, this won’t set the test live yet and you can come back and edit if you need to make changes!
{% endhint %}
