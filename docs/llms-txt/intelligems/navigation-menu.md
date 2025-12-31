# Source: https://docs.intelligems.io/getting-started/common-use-cases/content-test-common-use-cases/navigation-menu.md

# Navigation Menu

## Introduction

Testing your navigation menu is a great strategy that can significantly enhance the user experience and drive sales. As one of the primary ways customers interact with your site, the navigation menu plays a crucial role in how they discover products and navigate your offerings. Given its presence on every page, any adjustments can lead to substantial changes in customer behavior and satisfaction. Here are a few aspects you can explore through A/B testing your menu:

* **Layout**: Experiment with different structures to see which is more intuitive for users.
* **Organization**: Test how grouping products affects discoverability and ease of use.
* **Presentation**: Vary the visual design to identify what draws attention and enhances usability.
* **Styles**: Try different color schemes and fonts to see what resonates best with your audience.
* **Wording**: Analyze the effects of different labels and calls to action on customer engagement.

By fine-tuning these elements, you can optimize your navigation menu for better performance and improved customer experience. There are a few different ways you can test your navigation menu. The examples below show how to do this with a [Theme Test](#option-1-theme-test), or through our [Onsite Edits](#option-2-onsite-edits) capabilities.

{% hint style="info" %}
Once you have finished setting up your test, we recommend going through our suggested [Content Test QA Checklist](https://docs.intelligems.io/content-testing/content-test-qa-checklist) before you turn it on.
{% endhint %}

***

## Setting the Test Up

### Option 1: Theme Test

A Theme Test allows you to test a completely new design for your site, as you can make use of a new Shopify theme you're already working on, making it the easiest way to test bigger modifications. Your new theme may contain all sorts of changes, including a new navigation menu, and when a visitor comes to your site, Intelligems will automatically randomize them into one of the themes you've picked for your test.

You can test any of the aspects listed above, as you'll be setting up a new theme with your alternative navigation menu, so the sky is the limit!

To test a new navigation menu through a Theme Test:

1. **Create the new version of the menu you want to test**. Set it up as you normally would on Shopify, creating a new Shopify theme (it may be a copy of your existing theme) in which the new menu will be used.
2. **Follow the steps on** [**How to Set Up a Theme Test**](https://docs.intelligems.io/content-testing/content-testing-getting-started/how-to-set-up-a-theme-test) to create a new Theme Test. When selecting the themes that will be part of the test, choose your current theme for the control , and the theme containing your new navigation menu as the test.
3. You should be all set to launch your test!

***

### Option 2: Onsite Edits

Intelligems' Onsite Editor is a dynamic and versatile tool that enables you to creatively interact with and test various elements of your Shopify theme. When experimenting with a new navigation menu, you have numerous options depending on the specific aspects you wish to explore. Here, we’ll delve into ideas for enhancing your menu through a fresh [Layout and Organization](#layout-and-organization), reimagining its [Presentation and Styles](#presentation-and-styles), or experimenting with innovative [Wording](#wording).

#### Layout and Organization

If you're looking to test two different menus — one that directs visitors to all your collections through a single link and another that lists each collection individually — a great approach is to set up all the options you want to test on Shopify. Then, you can use our Onsite Editor to hide or show each option based on the menu you are evaluating.

Here's how you can achieve this:

1. On Shopify, go to **Online Store > Navigation**, and create a new menu through the **Add menu** option.
2. Create a menu containing all the sections that will be presented to both groups A and B:

   <figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-3eaf81f4184ca485f9a7794b9fd01099657318c5%2Fimage.png?alt=media" alt="" width="563"><figcaption></figcaption></figure>
3. Go to **Online Store > Themes**, and duplicate your current theme. We don't want to set up your live theme with the new menu quite yet, as all those options would be visible, so we will set everything up using a duplicate theme, which you can then publish when you turn on your test.
4. Next to the newly created theme, click on **Customize** to access the Theme Editor. Click on your theme's header, and change the current menu by the one you just created:

   <figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-c60fc2cf6cc327285ebfcc500aaf7dfbdd591382%2Fimg2.gif?alt=media" alt=""><figcaption></figcaption></figure>
5. On Intelligems, create a new Content Test, selecting the type Onsite Edits (see [How to Set Up an Onsite Edits Test](https://docs.intelligems.io/content-testing/content-testing-getting-started/how-to-set-up-an-onsite-edits-test)). When you get to the final step, click on **Edit** next to **Content Edits**, then **Add & Edit Changes in Visual Editor**, and select the duplicate theme you created:

   <figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-df2bb3d334a21d06a7bcb2fd9af1c32e2c219152%2Fimg3.gif?alt=media" alt=""><figcaption></figcaption></figure>
6. With Group A selected, enable the element selecting tool, then select each menu element that needs to be hidden for Group A, creating a replacement for each one. When selecting each menu element, make sure you're selecting the most outer portion of it, as this will ensure that we are targeting the correct portion of the menu that needs to be hidden. You'll hide each of these elements for Group A, while leaving them as originally set for Group B:

   <figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-ae35deeb102686fe0782599913630e344e074db0%2Fimg4.gif?alt=media" alt=""><figcaption></figcaption></figure>
7. Repeat this for the elements that won't be visible to Group B, this time leaving them as originally set for Group A, and hiding them only for Group B. Make sure to **Save** your changes before closing the editor:

   <figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-bc9bd9bee1d041ffb266fec19ecbe1f6facb57d8%2Fimg5.gif?alt=media" alt=""><figcaption></figcaption></figure>
8. As you switch between groups A and B in preview mode, you'll notice that the right menu elements are displayed for each test group.
9. Once you are ready to start your test, simply publish the duplicate theme that has the test menu in it, or set your live theme with that menu, then start the test on Intelligems. You'll want to make sure to keep the interval between these two actions as minimal as possible, so your visitors don't see all the menu options once the test menu is set on your live theme.

{% hint style="info" %}
If you are using [Audience Targeting](https://docs.intelligems.io/general-features/targeting/audience-targeting) to run this test only for a subset of visitors, make sure you use **Advanced Targeting**, setting up a condition so, if the visitor doesn't meet the audience's criteria, they get assigned to your control group, and select the option to exclude them from Analytics. This will ensure that they see your default menu instead of all the menu items. For example, if you wanted to target Desktop visitors only, this is how you would set this up:

<img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-7dbd6c40925730bbd2260eea249d029a354e88f9%2Fimage.png?alt=media" alt="" data-size="original">
{% endhint %}

#### Presentation and Styles

Perhaps you are happy with the options presented on your menu, but you want to test the ways your visitors perceive it. You can easily inject custom styles into your test, having an alternative presentation for your test group, without needing to make any theme modifications, as outlined below:

1. On Intelligems, create a new Content Test, selecting the type Onsite Edits (see [How to Set Up an Onsite Edits Test](https://docs.intelligems.io/content-testing/content-testing-getting-started/how-to-set-up-an-onsite-edits-test)).
2. Load your test's preview, access the Onsite Editor, and go into editing mode.
3. Click on the "\</>" icon to open the Global CSS / JS editor:

   <figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-ca1d8dde20e4e1253882b337488b228d007719d5%2Fimg6.png?alt=media" alt=""><figcaption></figcaption></figure>
4. In the Group selector, switch to your test group, then add in your custom CSS that targets and modifies the elements on your navigation menu. This will be CSS that you've written yourself, with the help of a theme developer, or an AI generating tool, for example:

   <figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-fce57191c17e8410ac36e2397bea5e28e33e5748%2Fimg7.png?alt=media" alt=""><figcaption></figcaption></figure>
5. Make sure you click **Apply** on the editor, and then **Save** on our widget.

#### Wording

Changing labels can often enhance the understanding of the underlying content and boost client engagement with specific sections of your menu. Here's how you can test simple text adjustments to your existing menu items:

1. On Intelligems, create a new Content Test, selecting the type Onsite Edits (see [How to Set Up an Onsite Edits Test](https://docs.intelligems.io/content-testing/content-testing-getting-started/how-to-set-up-an-onsite-edits-test)).
2. Load your test's preview, access the Onsite Editor, and go into editing mode.
3. Click the button on the bottom-left to **enable element selecting**:

   <figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-9bc2af2a8b7ba94a743d366446d2ad08ecef9538%2Fimg8.png?alt=media" alt=""><figcaption></figcaption></figure>
4. Click on the menu item you wish to test, then **Edit Text**:

   <figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-f215f64838d2b574cae527962af9c3d27a76344b%2Fimg9.png?alt=media" alt=""><figcaption></figcaption></figure>
5. Make no changes for Group A (Leave as is). For Group B, add in the text that should replace the original text:

   <figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-419a708652b2abd012d160e324795320044ae699%2Fimg10.png?alt=media" alt=""><figcaption></figcaption></figure>
6. Make sure you click **Done** on the editor, and then **Save** on our widget.

***

## Additional Suggestions

The methods for testing a navigation menu aren't limited to those mentioned above. With the various resources available through Intelligems, there are several other ways you can set up your test, depending on the specific changes you want to evaluate:

* If you want to redirect visitors to certain pages when they click on a given menu link, you can create a [Split URL Test](https://docs.intelligems.io/content-testing/content-testing-getting-started/how-to-set-up-a-split-url-test) rather than make changes directly to your menu.
* If you want to modify your menu without creating new menu items on Shopify, and you have a developer to assist you with front-end coding, you can use our [JavaScript injection capabilities](https://docs.intelligems.io/general-features/css-and-javascript-injection), adding custom JavaScript to the test group to programmatically modify your menu.
