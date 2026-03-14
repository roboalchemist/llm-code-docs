# Source: https://docs.beefree.io/beefree-sdk/other-customizations/mobile-design-mode.md

# Mobile Design Mode

{% hint style="info" %}
Mobile Design Mode is available on all [Beefree SDK plan types](https://developers.beefree.io/pricing-plans). Important: While Mobile Design Mode is available on all plan types, there associated advanced features (such as Stack on Mobile) that are only available on [Beefree SDK paid plans](https://developers.beefree.io/pricing-plans). This page outlines which Mobile Design Mode features correspond with each plan type.
{% endhint %}

## Overview <a href="#overview" id="overview"></a>

Your customers can easily design responsive emails, pages, and popups for mobile using **Mobile Design Mode**. When enabled, your customers will be able to:

* Easily switch between desktop and mobile view to access and edit content;
* Edit padding, text alignment, and font size optimized for Mobile;
* Instantly display the results of [mobile optimization options](https://devportal.beefree.io/hc/en-us/articles/4408466433938) – such as *do not stack/reverse stack/hide on mobile*;
* Extend Beefree SDK’s design flexibility and build mobile-first campaigns.

### Use cases

* **Mobile-first design**: Start the builder in Mobile view, and let the user switch as needed.
* **Mobile-only editing**: Start the builder in Mobile view, and hide the widget to switch views.
* **Control hidden elements visibility**: Remove the “Visibility” toggle and decide if elements with a “hide on” property can be visible with the blur effect or are not visible during editing.
* **Custom UI controls**: start the builder in a predefined mode and offer your UI controls to switch between views and hidden elements visualization. To do so, you can use the loadStageMode method to trigger a change from your application.

```javascript

bee.loadStageMode({
  mode: 'mobile',
  display: 'hide',
})

```

You can also use the `loadStageMode` method to disable Mobile editing mode.

```javascript

bee.loadStageMode({
  mode: 'global',
})

```

## Demo <a href="#demo" id="demo"></a>

Here is a video explaining **why we built Mobile design mode** and how it **enhances the design UX** of Beefree SDK.

{% embed url="<https://youtu.be/1hP83GPcue8>" %}

## How to enable Mobile Design Mode <a href="#how-to-enable-mobile-design-mode" id="how-to-enable-mobile-design-mode"></a>

Take the following steps to enable Mobile Design Mode within your application:

1. Log in to the [Beefree SDK Developer Console](https://developers.beefree.io/login?from=website_menu).
2. Navigate to the application you want to configure **Mobile Design Mode** for.
3. Click the application's **Details** button.

   **Note:** We recommend testing the feature first with a DEV or QA application
4. On the next page, navigate to the **Application Configuration** section and click **View More**.
5. Go to the **Services** section and toggle **Enable mobile design mode** on. ![](https://806400411-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F8c7XIQHfAtM23Dp3ozIC%2Fuploads%2F9Cp0jzaftupLbyIQh2ga%2FCleanShot%202025-06-27%20at%2015.27.36.png?alt=media\&token=843beb8f-5e6b-490c-9326-59a663d44cd2)
6. Click **Save** on the top-right corner of the page to save the server-side configuration.

## How it works in the user Interface <a href="#how-it-works" id="how-it-works"></a>

When Mobile Design Mode is enabled for an application at [developers.beefree.io](https://devportal.beefree.io/hc/en-us), the builder will display two new icons in the upper-left corner of the content area, as highlighted below.

<figure><img src="https://806400411-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F8c7XIQHfAtM23Dp3ozIC%2Fuploads%2FJgBkeSfUAT87UnLQZH95%2Fnew-mobile-design-mode-icons.png?alt=media&#x26;token=0d414669-8b90-4cf3-9a79-19d30c46c3fa" alt=""><figcaption></figcaption></figure>

The *desktop view (screen icon on the left)* will leverage your browser’s full width.

The *mobile view* (mobile icon on the right) will resize the work area width to 320px to simulate a mobile screen.

<figure><img src="https://806400411-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F8c7XIQHfAtM23Dp3ozIC%2Fuploads%2Fpx2dhWRPVepW5YPVuBR3%2F2Going-from-desktop-to-mobile_450.gif?alt=media&#x26;token=05b90387-15e1-40bc-9878-0b6ff4bcf810" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
**Note:** When Mobile design mode is enabled, users will work on a single template that will include both the desktop design and the mobile one. The template doesn’t require any duplicates. The mobile edits will be automatically saved and reflected in the templates.
{% endhint %}

## Builder limitations in mobile view

When a user is working in the Mobile stage, the features available are the same as in the desktop stage, with a few exceptions:

* The content area width cannot be scaled – it can only be changed in the desktop view;
* Users can add or delete columns within a row, but they won’t be able to resize them.

## Designing content for Mobile <a href="#designing-content-for-mobile" id="designing-content-for-mobile"></a>

When designing content for Mobile, users may require more flexibility in the way they arrange or format elements to fit a smaller screen.

Thanks to the latest Mobile Design Mode updates, users can now control individual elements straight from the mobile stage without the need to duplicate them.

Users can optimize the design of the following content properties by switching to the Mobile Design Stage:

* Padding
* Alignment
* Font size

It is now possible to style these elements for Mobile or Desktop.

These three mobile-optimized properties are available for the following content type modules:

* Title
* Paragraph
* List
* Form
* Icons
* Menu
* Button

To edit a specific parameter for mobile, users must switch to the Mobile stage and select the content element they want to edit.

They will find the Mobile-optimized properties in the sidebar menu, under the “Content Properties” tab.

Mobile-optimized elements are flagged with a clickable “Mobile” pill, as shown in the image below:

<figure><img src="https://806400411-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F8c7XIQHfAtM23Dp3ozIC%2Fuploads%2FjaMABKan0FW66zbZnJrE%2F6Screenshot-2022-07-04-at-15.35.39.png?alt=media&#x26;token=d3c47bd0-c723-427e-a68c-3c93fa27187c" alt=""><figcaption></figcaption></figure>

When the pill is highlighted in light blue, it means the property has been edited and applied in the mobile stage. The mobile pill can be styled using [Custom CSS](https://docs.beefree.io/beefree-sdk/other-customizations/appearance/custom-css) if covered by your [subscription plan](https://beefree.io/bee-plugin/pricing/).

<figure><img src="https://806400411-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F8c7XIQHfAtM23Dp3ozIC%2Fuploads%2FkJO0W1TubflU4tD1LnHY%2F7Screenshot-2022-07-04-at-15.34.30.png?alt=media&#x26;token=a356cc62-c0e9-4238-8e44-3a99dca4fa4e" alt=""><figcaption></figcaption></figure>

Users can click on the x to revert the property back to the desktop.

## Editing Font Size on Mobile

We have also improved the user experience by moving the Font Size Controls, previously displayed in the formatting tiny menu available in the content area, to the Content Properties Tab in the sidebar menu.

<figure><img src="https://806400411-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F8c7XIQHfAtM23Dp3ozIC%2Fuploads%2FxhjTGQ6mkQYSTbWVNHvP%2F8Screenshot-2022-07-04-at-16.47.57.png?alt=media&#x26;token=83f43018-1f8f-4f37-8da3-9b2b4013e77d" alt=""><figcaption></figcaption></figure>

<figure><img src="https://806400411-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F8c7XIQHfAtM23Dp3ozIC%2Fuploads%2F0lPuMcj84RUMMN7IEtfr%2F9Screenshot-2022-07-04-at-15.35.39.png?alt=media&#x26;token=8eb90f4f-fce6-479d-a702-c2fd511d0c09" alt=""><figcaption></figcaption></figure>

## Tracking changes in the history

All the edits performed in the Mobile Stage are tracked and flagged in the history as *(Mobile)* edits.

<figure><img src="https://806400411-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F8c7XIQHfAtM23Dp3ozIC%2Fuploads%2FouKNuwCwLxtIdguQ4AUe%2F10Screenshot-2022-07-04-at-11.15.20.png?alt=media&#x26;token=3f7f8e18-614b-46a9-bff2-f3a3cb830446" alt=""><figcaption></figcaption></figure>

## Customization options <a href="#customization-options" id="customization-options"></a>

Mobile Design Mode can be considered a “plug-and-play” feature because it just needs to be enabled on the [Beefree SDK Console](http://developers.beefree.io/) and can be used by your users out of the box.

If you want to customize the user experience, Beefree SDK allows you to configure a few client-side options to control permissions and styles. Take a look at the code snippet below to see how to load these settings into the initial configuration as part of the workspace section.

```javascript

workspace: {
  type: 'default', // default, mixed, amp_only, html_only
  stage: 'desktop', // desktop, mobile, global
  displayHidden: 'blur', // blur, hide
  hideStageToggle: true, // default = false
}

```

Here is a brief description of the parameters and their options. They are all optional.

<table><thead><tr><th width="209">Parameter</th><th width="197">Description</th><th width="154">Values</th><th>Default</th></tr></thead><tbody><tr><td><code>type</code></td><td>loads different workspace types (currently used to handle <a href="amp-for-email">AMP content visibility</a>).</td><td>default, mixed, amp_only, html_only</td><td><code>default</code></td></tr><tr><td><code>stage</code></td><td>Define if the builder starts in desktop view, mobile view, or global (i.e. without desktop/mobile views.)</td><td>desktop, mobile, global</td><td>inherits Developer account configuration</td></tr><tr><td><code>displayHidden</code></td><td>if defined, hidden elements will behave based on the parameter value.</td><td>blur, hide</td><td><code>blur</code></td></tr><tr><td><code>hideStageToggle</code></td><td>if true, the mobile/desktop icons to switch view are not visible</td><td>true, false</td><td><code>false</code></td></tr></tbody></table>

## Mobile optimization settings

{% hint style="info" %}
**Important:** The **Mobile Optimization Settings** listed in this section are available on [Beefree SDK paid plans](https://developers.beefree.io/pricing-plans).
{% endhint %}

Beefree SDK provides addition mobile optimization settings both for rows and content blocks. These are available on [paid plans](https://developers.beefree.io/pricing-plans).

To change how content behaves on mobile and create a mobile version of an email, page, or popup, you can add the following enhancements to your application:

* **Hide on mobile/Hide on desktop:** A content property to hide a block when displaying the email/page on a specific device.
  * **Server-side configuration:** ![](https://806400411-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F8c7XIQHfAtM23Dp3ozIC%2Fuploads%2FO71qDT1DwPCSyOSCsGQ8%2FCleanShot%202025-06-27%20at%2015.31.57.png?alt=media\&token=c031fa6e-93a4-48c5-813f-8c1629fd0be3)
  * **User interface:** ![](https://806400411-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F8c7XIQHfAtM23Dp3ozIC%2Fuploads%2FoqobPsi1QBXtqOoQS4Lf%2FCleanShot%202025-06-27%20at%2015.33.03.png?alt=media\&token=af5f18b3-ced2-4788-aece-8b9d80b93ca6)
* **Do not stack on mobile:** When this option is enabled for a row, adjacent columns will not be stacked on mobile devices. The columns will stay side-by-side, as in the desktop view.
  * **Server-side configuration:** ![](https://806400411-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F8c7XIQHfAtM23Dp3ozIC%2Fuploads%2FPkvzSiUyEMRCzNidS8k9%2FCleanShot%202025-06-27%20at%2015.34.42.png?alt=media\&token=5707da0d-7f66-438e-a868-44a12535917c)
  * **User interface:** ![](https://806400411-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F8c7XIQHfAtM23Dp3ozIC%2Fuploads%2FIB9cTF9lj9AnlpbsW7hT%2FCleanShot%202025-06-27%20at%2015.35.10.png?alt=media\&token=27895f44-e2ed-490f-a356-70ac42696ddd)
* **Reverse stacking on mobile:** When turned on for a row, columns for that row will stack in reverse order, i.e., from the rightmost to the leftmost.
  * **Server-side configuration:** ![](https://806400411-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F8c7XIQHfAtM23Dp3ozIC%2Fuploads%2Fa3Ex89KSZGXgxTIXJvHR%2FCleanShot%202025-06-27%20at%2015.35.39.png?alt=media\&token=08f6f004-08da-4378-a775-0155cd78d339)
  * **User interface:** ![](https://806400411-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F8c7XIQHfAtM23Dp3ozIC%2Fuploads%2FjrnPZmAc6U8QYjkX0Nmt%2FCleanShot%202025-06-27%20at%2015.36.13.png?alt=media\&token=e29bf85f-c065-467f-928f-b9ccdaddfe5d)

These settings enhance Mobile Design Mode by allowing end users to immediately view desktop vs. mobile designs.

### Displaying hidden elements

There is an additional setting to preview hidden elements included in a template. With the Hide-on enabled a “Visibility” icon will appear next to the Desktop vs. Mobile stage icons.

<figure><img src="https://806400411-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F8c7XIQHfAtM23Dp3ozIC%2Fuploads%2FZSLFcxAkKuDoM151cGif%2F3visibility-icon.png?alt=media&#x26;token=88589cd0-6661-4f0b-9d80-87bf672bfae6" alt=""><figcaption></figcaption></figure>

When the Visibility button is ON (default behavior):

* The builder will display content blocks set as hidden for the current device;
* Hidden elements will be blurred out;
* A small icon in the outline of the block will appear whenever hovering with the mouse on the hidden element.

<figure><img src="https://806400411-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F8c7XIQHfAtM23Dp3ozIC%2Fuploads%2FDzjSXqXXUcDfch6qqqA6%2F4hidden-element.png?alt=media&#x26;token=1b7bdd72-636d-4740-9a33-8c55609d695b" alt=""><figcaption></figcaption></figure>

When Visibility is OFF:

* Hidden elements won’t be visible in the content area;
* The template will be available as it is;

Here is how the Visibility toggle changes the experience when editing a recent Beefree SDK newsletter.

<figure><img src="https://806400411-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F8c7XIQHfAtM23Dp3ozIC%2Fuploads%2F8xHu9jdWklKNoGrTTyp6%2F5Visibility-icon-in-a-newsletter.gif?alt=media&#x26;token=d4b83717-86bc-4539-9235-6fd77e10d5eb" alt=""><figcaption></figcaption></figure>

The device preview matches the stage selected when accessing the design preview. This doesn’t apply if you have implemented a custom-built preview.
