# Source: https://docs.beefree.io/beefree-sdk/server-side-configurations/server-side-options/content-options.md

# Content options

In this box, you can enable additional content blocks that will appear in the Content panel inside the editor.

<figure><img src="https://806400411-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F8c7XIQHfAtM23Dp3ozIC%2Fuploads%2F7mIitPvTUPQpPs2UQZDl%2FCleanShot%202024-03-12%20at%2011.48.22%402x.png?alt=media&#x26;token=d164f247-2f11-49fb-a2cb-987b7a7c9d66" alt=""><figcaption></figcaption></figure>

Currently, you can manage these content blocks:

## Available Content Blocks

| Block         | Description                                                                                                                     | Availability              | User guide |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------- | ------------------------- | ---------- |
| **HTML**      | Allows your users to include their own HTML code                                                                                | Paid plans only           | More info  |
| **Menu**      | Allows users to create simple, text-based navigation elements                                                                   | All plans, including free | More info  |
| **Title**     | Allows users to add text with H1,H2,H3 tags, for email and web accessibility, and for SEO on web pages.                         | All plans, including free | More info  |
| **List**      | Allows users to create easy numbered and bullet lists with Paragraph's upgrades and list type, spacing, and identation support. | All plans, including free | More info  |
| **Paragraph** | Allows users to write text with support for multiple font weights, copy/paste support, easier reformatting, and more.           | All plans, including free | More info  |
| **Text**      | Legacy text block. Please refer to title, paragraph and list.                                                                   | All plans, including free | More info  |
| **Video**     | Helps users include a visual link to video content                                                                              | Paid plans only           | More info  |
| **Icons**     | Enables users to create icon-based layouts, such as *star ratings, bullet lists, properties*                                    | All plans, including free | More info  |
| **Spacer**    | Allows users to add a space between content                                                                                     | All plans, including free | More info  |
| **Table**     | Allows users to add a table to their design                                                                                     | All plans                 | More info  |

## **Content options in Page Builder**

If you’re configuring a Page Builder application, there are a few differences in what these blocks allow:

* the **HTML Block** also allows **script and iframe tags;**
* the **Video block** allows for video playback, either embedding a YouTube, YouTube Shorts, or Vimeo video or pointing to a hosted video ([read more](https://docs.beefree.io/beefree-sdk/visual-builders/page-builder/embedding-videos-in-a-page)). Supported video formats are:
  * YouTube (16:9 aspect ratio)
    * Public Videos
    * Unlisted Videos
    * Videos starting at a certain time
  * YouTube Shorts (16:9 aspect ratio)
  * Vimeo
    * Public Videos
    * Unlisted Videos
    * Cinemascope (21:9 aspect ratio)
* the **Menu block** allows menu items to be set as “internal links,” pointing to any content block in the page that is configured as a “block identifier.”

There is also an additional option for turning on the **Form block**.

Please note that you need to implement one of the two methods indicated in this article for the Form tile to appear in the Content tab of the editor:

* The [default form](https://docs.beefree.io/beefree-sdk/forms/integrating-and-using-the-form-block/passing-forms-to-the-builder) method is available for all plans, including free
* The [content dialog](https://docs.beefree.io/beefree-sdk/other-customizations/advanced-options/content-dialog) method is available for paid plans only.

## AMP Content <a href="#amp-content" id="amp-content"></a>

You can enable AMP blocks that will become available in the “Content” tab of your application's Email Builder. To enable this feature, toggle on **Enable AMP Carousel** in the **AMP Content** section of your application's configuration options.

<figure><img src="https://806400411-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F8c7XIQHfAtM23Dp3ozIC%2Fuploads%2FLIGlzVDyumEhWq0TQI7T%2FCleanShot%202024-03-12%20at%2012.23.01%402x.png?alt=media&#x26;token=7eb177c8-357c-4148-bbd6-b1fbf0290669" alt=""><figcaption></figcaption></figure>

We currently provide an [AMP Carousel](https://docs.beefree.io/beefree-sdk/other-customizations/amp-for-email) content block. After enabling the toggle, you will need to configure an [AMP-compatible workspace](https://docs.beefree.io/beefree-sdk/other-customizations/amp-for-email).

Please note that AMP content is not available for Page Builder.
