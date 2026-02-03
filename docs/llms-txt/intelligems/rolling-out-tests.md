# Source: https://docs.intelligems.io/personalizations/rolling-out-tests.md

# Rolling Out Tests

## Why Roll out tests?

When viewing the results of your Intelligems experiment, you may find that one variant performed better than others across all audiences, or only for a limited audience.

* **If one variant performed better across all audiences:** you’ll want to end the test and show the winning variant to all visitors. Replicating the changes in Shopify takes time, is error-prone, and may require developer support. With Intelligems Rollouts you can apply your changes in a few clicks - optimizing your site as quickly as possible.
* **If a variant performed better across a specific audience only**: it may be impossible to deploy this change in Shopify. With Intelligems Rollouts you can apply these changes to one or more specific audiences in a few clicks.

{% hint style="success" %}
**One test, multiple rollouts:** You may find that you want several rollouts from a single test. For instance if your group 1 performs better for audience A while group 2 performs better for audience B, you can roll out group 1 only to audience A and separately roll out group 2 to audience B.
{% endhint %}

## How do Rollouts work?

Rolling out a winning test variant **ends the test and creates a Personalization** with the same site modifications as the variant. You can [learn more about Personalizations here](https://docs.intelligems.io/personalizations/personalizations-getting-started) but in general, you can

* **Limit the audience:** configure the Personalization to target all site visitors or a particular audience, including only visitors holding a special link.
* **Start whenever:** turn it on immediately or only once you’re ready.
* **Stop or resume any time:** for example, you may roll out a test variant just for a few days while you work on implementing your changes natively in Shopify and once you’re ready, you can turn off the resulting Personalization.

**What kinds of tests can you roll out?**

A test can be rolled out if it is active, paused, or ended.

* CONTENT TESTS: can be rolled out
* OFFER TESTS: can be rolled out
* PRICE TESTS: a particular variant in a price test can be rolled out to all Visitors on your site, but it can not be rolled out to a specific audience only. Additionally, price tests can only be rolled out *once*, the moment you end them.
* SHIPPING TESTS: cannot be rolled out due to technical limitations

**Native Rollouts:** There are two situations in which Intelligems, for technical and safety reasons, rolls out changes *“natively”* - meaning directly to Shopify rather than to a Personalization. This occurs when

* You choose to roll out a **theme test** to All Visitors: It’s much safer and more performant for Intelligems to change the Shopify theme directly.
* You roll out a Price test: for technical reasons Intelligems must update your Shopify prices directly.

## How to roll out a test

**Step 1: Open the Rollout Wizard**

The Rollout Wizard guides you through a few steps to roll out a test variant into a single Personalization. If you are rolling out more than once from the same test, you'll need to go through the wizard multiple times. When you complete the Rollout Wizard you'll still have a chance to review and modify the resulting Personalization before activating it.

There are several ways to reach the Rollout Wizard.

* FROM THE TESTS LIST: click the Stop Test button or the Roll Out button
* FROM THE ANALYTICS PAGE: The same two buttons are available at the top of a test’s Analytics page

  <figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-a55c1389f50238d7540d1694036805c1a16a3bd1%2Fimage.png?alt=media" alt=""><figcaption><p>Rolling out a test group from the top of the test's Analytics page</p></figcaption></figure>
* FROM THE ANALYTICS AUDIENCES TABLE:
  * In the All Visitors tab at the bottom of the Analytics Overview page, click the name of the variant you’d like to roll out
  * From one of the Audience tabs of this table, you can roll out a variant to a specific audience that it performed best for

    <figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-27b832972046936e0196dbb5f3e0bbea9fe8e585%2Fimage.png?alt=media" alt=""><figcaption><p>Rolling out a test group to a particular audience from the Audiences Table in Analytics</p></figcaption></figure>

**Step 2: Choose the group you want to roll out**

This is usually the winner, based on your primary goal. If you’re reached the wizard from the Audiences table, a group will be pre-selected for you.

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-bcd481552da1622cef273dca078d39022ca2f46c%2Fimage.png?alt=media" alt=""><figcaption><p>Selecting a test group to roll out</p></figcaption></figure>

{% hint style="info" %}
**Price Tests:** If you’re rolling out a Price test, this is as far as the wizard goes. You can now click Roll Out. Intelligems will apply your prices directly to Shopify, for all visitors.

**Warning:** If your test contained any additional on-site edits such as text changes, those will ***not*** be rolled out. You can either apply those in Shopify yourself or create a Personalization from scratch with those changes.
{% endhint %}

**Step 3: Choose the audience you’d like to roll this variant out to**

You can build an audience of your choosing using our robust audience targeting conditions and combination logic. You can also show the resulting Personalization only to visitors with a special link, which is handy for rolling out offers.

Intelligems will automatically suggest an audience for you depending on your test settings and how you entered the Rollout Wizard. You can change or clear this if you wish.

* If your test is targeted to a specific audience, we’ll copy that audience over
* If you come in from Analytics and you had filters active, we’ll copy those filters
* If you come from an audience in the Analytics table, we’ll copy that as well.

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-a6c1a28fe5be9856b57604d6c0697e89ee889ca9%2Fimage.png?alt=media" alt=""><figcaption><p>Selecting an audience for your roll out</p></figcaption></figure>

If your test made use of Advanced Targeting, we will not be able to auto-suggest an audience for the Personalization but you should be able to build it yourself if needed.

{% hint style="info" %}
**Other types of targeting:** The test you’re rolling out may have used additional types of targeting:

* **Currency or Page Targeting** will be copied into the resulting Personalization but you should check to make sure before activating the Personalization. This does not apply when rolling out price tests or rolling out theme tests to all visitors, since these kinds of changes are applied directly to Shopify.
* **Mutually exclusive behavior** will not be rolled out. If your test was in a Mutual Exclusion Group (meaning visitors cannot see it and another test at the same time), the resulting Personalization will have no such limitations.
  {% endhint %}

**Step 3.5: Additional step for theme rollouts**

If you are rolling out a Theme test to all visitors, Intelligems will roll out natively - meaning it will apply the new theme directly to your Shopify store rather than creating a Personalization. However, if your test also contained additional changes such as onsite edits - for example text, colors, CSS, javascript - you'll be asked whether you want to discard those changes or roll them out separately as a Personalization.

{% hint style="warning" %}
If you do choose to roll them out as a Personalization, you should activate the resulting Personalization as soon as possible, since the Theme change will be applied to Shopify as soon as you finish the Rollout Wizard.
{% endhint %}

**Step 4: Confirm the changes and roll out**

Look over the summary of your Rollout, fixing anything if needed. If everything looks good, click Roll Out and End Test (or “Roll Out” if your test has already ended).

Your test will end if it’s not already ended and you will be taken to a draft of your resulting Personalization where you can

* give it a more descriptive name
* check to make sure everything looks okay and make any changes
* click the “Activate” button whenever you’re ready to activate your Rollout Personalization

{% hint style="info" %}
**Cleaning up after Offer Rollouts:** Offer tests can be created by choosing one or more already-existing Offer Personalizations and testing them against each other. When you roll out a winning group in an Offer Test, Intelligems creates a new Personalization from the winning group. At this point you may want to do some tidying up in your Personalizations list to:

* remove the Offer Personalization that gave rise to your winning group
* remove the other Offer Personalizations that gave rise to your non-winning groups, if you’re not planning on using them or testing them again
  {% endhint %}
