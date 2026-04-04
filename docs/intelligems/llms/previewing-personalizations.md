# Source: https://docs.intelligems.io/personalizations/previewing-personalizations.md

# Previewing Personalizations

## How does Preview help?

* Before you’ve ever activated a Personalization, preview to make sure everything looks good
* While a Personalization is active, preview to see what it looks like for its target audience

{% hint style="info" %}
At the moment you cannot preview a Personalization that has been previously active but is now stopped. To work around this, you can either re-activate the Personalization, or you can duplicate it and preview the duplicated version.
{% endhint %}

## How to preview your Personalization

In a Personalization, go to the Preview tab.

#### **STEP 1: Save your changes**

The Intelligems preview (screenshots and full screen) will only show what’s already saved in your Personalization. If you’ve made additional changes since your last save, you should save the Personalization to see them in the Preview.

If you are editing an active Personalization, you may not feel comfortable saving your changes just to preview, since saving would automatically apply these changes to visitors. To work around this, you should *either re-activate the Personalization, or you can duplicate it and preview the duplicated version.*

#### **STEP 2: Optionally adjust which page you want to see**

To save you time, Intelligems automatically determines which site page our preview should ‘center’ on. This means which page is shown in screenshots and as the first page when you open full screen preview. The automated logic works as follows:

* By default the home page of your site is shown.
* If you have page targeting set up to a single page, that page will be used. This is useful, for instance, when personalizing a particular PDP for a given audience.
* If you have a single redirect modification, the target URL of that redirect will be used.
* If you have both of the above, the page targeting will be used.

If you prefer to override this and always see previews beginning on a particular page, whether it’s the home page or another, simply choose Custom URL in the top left picker, type in a URL, and save. Intelligems will continue showing previews of this URL until you choose another URL or reset it to automatic mode.

#### **STEP 3: View screenshots and Full Screen Preview**

* **Screenshots:** Have a look at the screenshots for a rough at-a-glance view of your site. These should never be used as a substitute for a full screen preview.
* **Full Screen Preview:** Click the “Full Screen Preview” button to view your site in the browser as visitors in the Personalization would see it. Or click the “Mobile Preview” button to get a link for your mobile device.

#### **TIP: In full screen preview, make sure to “include” yourself:**

If your Personalization is targeted to a Particular audience, it may be that your own circumstances (location, device, etc) make you ineligible for the Personalization. To account for this, full screen preview allows you to view the site in two ways:

* **As yourself:** If you do not match the Personalization audience, you will receive a message like the one below. This helps you confirm that the targeting is excluding people correctly. Click the “Include” button to force yourself into the audience of the Personalization - this will allow you to see what it will look like for those visitors.

  <figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-e84786a6cb41e4e73fbfcd765d9e0bea44b90f19%2Fimage.png?alt=media" alt=""><figcaption></figcaption></figure>
* **As a member of the audience**: once you click “Include” you will see the site as it appears for the Personalization's audience. This is the mode you should spend most of your time in.

Other buttons in this blue banner that you may find useful are:

* **The refresh icon:** This resets the preview so that your site appears the way it did when you first previewed it. This can be handy when using a URL Redirect modification that's set to only redirect from Page A to Page B *a single time*. Clicking refresh will allow you to test the redirect more than once.
* **Highlight Replaces:** If you have used Content Edits in your Personalization, this toggle will show which elements on each page have been affected.

## Next Steps

Once you’ve previewed your Personalization, you can go on to:

* **Fine tune your modifications:** Click [here](https://docs.intelligems.io/personalizations/personalization-modifications) to read our Modifications guide.
* **Activate the Experience**: If everything looks good, activate your Personalization or leave it pending until ready. You can pause and resume as many times as you need, which helps with recurring promotions.
