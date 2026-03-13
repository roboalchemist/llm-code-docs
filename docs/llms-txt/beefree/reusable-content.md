# Source: https://docs.beefree.io/beefree-sdk/rows/reusable-content.md

# Reusable Content

{% hint style="info" %}
This feature is available on Beefree SDK [Core plan](https://developers.beefree.io/pricing-plans) and above. Upgrade a [development application](https://docs.beefree.io/beefree-sdk/getting-started/readme/development-applications) at no extra charge to explore features from higher plan tiers. **Note:** Usage on a development application still counts toward [usage-based fees](https://devportal.beefree.io/hc/en-us/articles/4403095825042-Usage-based-fees) and limits.
{% endhint %}

Beefree SDK offers a comprehensive suite of features that enable your application's end users to save and manage reusable content. Rows are a core feature of the visual builders within Beefree SDK that provide end users with an intuitive avenue for saving and reusing content throughout their design creation workflows. They provide a structured method to house various types of content such as headers, paragraphs, images, and buttons.

Rows are also a fundamental part of how designs are built and structured within the visual builders. In the following GIF, you can see how each row functions as a component of a continuous design.

<figure><img src="https://806400411-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F8c7XIQHfAtM23Dp3ozIC%2Fuploads%2FGjsrzTtyIj8iNe9D7y5s%2FCleanShot%202024-12-03%20at%2017.29.14.gif?alt=media&#x26;token=31207a27-bc67-4232-9a7d-534b165a1aaa" alt=""><figcaption></figcaption></figure>

Rows allow end users to add multiples types of content to a section of a design. End users can either create their own rows from scratch (and save them for reuse on a later day), or they can use pre-designed rows that are pre-loaded into the host application and ready for use. Pre-loaded rows are helpful when providing a template structure that end users can customize as they build their designs.

Providing end users with the option to easily reuse content comes with a host of benefits, including:

* **Pre-designed and customizable content**: End users can select from rows that already contain content, which they can then customize for their specific needs.
* **Flexible structure**: Rows help organize different content types in a structured layout, which promotes a clean and efficient design.
* **Drag-and-drop functionality**: Rows can easily be dragged and dropped onto the stage.
* **Continuity with current user experience**: End users can add empty structures, which preserves creativity and allows them to build and design from scratch.
* **Option to disable empty rows**: If preferred, end users can opt to work solely with pre-made rows, focusing on content customization without the need to build layouts from the ground up.

In addition to rows offering a variety of benefits for end users, there are also clear benefits for the host application, including:

* **Ready-to-go content delivery**: The host application can pass pre-built, ready-to-go rows directly into the builder, reducing the need for end users to create content from scratch.
* **Customization control**: Host applications can offer a variety of customizable rows, ensuring users follow design guidelines while still providing creative freedom.
* **Improved user experience**: Pre-designed rows simplify the user interface, making the builder more intuitive and less complex for users.
* **Optional removal of empty structures**: Host applications can disable empty row options if desired, encouraging users to focus on modifying pre-existing content.
* **Efficient content management**: Rows enable the host to provide consistent, reusable content blocks that can be updated globally, streamlining content management and maintaining design consistency across the platform.

### Understanding the Different Types of Rows in Beefree SDK

This section outlines the different row-related features available within Beefree SDK. Throughout the following pages of the Rows section, we will discuss each of these different row-related features in depth, including what they are, how they look, and how to implement them if they are a good fit for your application and end users.

#### Custom Rows

The purpose of Custom Rows is to provide pre-configured rows that your end users can drag-and-drop into the builder and start customizing.

The following GIF provides a visual of how Custom Rows look to end users:

<figure><img src="https://806400411-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F8c7XIQHfAtM23Dp3ozIC%2Fuploads%2FA8V5ujJWJZExILbP45xA%2FCleanShot%202024-12-03%20at%2017.53.35.gif?alt=media&#x26;token=08c84742-2a2d-48fa-ac7e-2aabdf232f58" alt=""><figcaption></figcaption></figure>

Custom Rows are integrated by adding the `rowsConfiguration` parameter to your [`beeConfig`](https://docs.beefree.io/beefree-sdk/getting-started/readme/installation/configuration-parameters). The following code snippet is the one used to configure the row in the GIF above.

```json
rowsConfiguration : {
 "externalContentURLs": [
  {
   "name": "External resource",
   "value": "https://bee-playground-backend.getbee.io/api/customrows?ids=1,2,3,4"
  }
 ]
}
```

Visit the [Beefree SDK playground](https://developers.beefree.io/playground) to experiment more with the Custom Rows configuration, and visit the [Implement Custom Rows page](https://docs.beefree.io/beefree-sdk/rows/reusable-content/create/pre-build/implement-custom-rows) to learn more about integrating this feature within your application.

#### Hosted Saved Rows

Hosted Saved Rows allow your end users to save and manage their own rows. This supports them in saving the content they've created and reusing it again at a later date.

Hosted Saved Rows provides both a storage solution and user interface your end users can engage with to save and manage their rows.

The following GIF shows an example user interface displaying how Hosted Saved Rows will appear to your end users on the frontend of your application.

<figure><img src="https://806400411-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F8c7XIQHfAtM23Dp3ozIC%2Fuploads%2F3i8oQ6gwSbZy09wUlzhD%2FCleanShot%202024-12-03%20at%2018.22.16.gif?alt=media&#x26;token=343c0373-62df-4664-83fd-69873d58682f" alt=""><figcaption></figcaption></figure>

Hosted Saved Rows are enabled by default. The following image shows how the toggle looks like in the [Developer Console](https://developers.beefree.io/login?from=website_menu).

<figure><img src="https://806400411-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F8c7XIQHfAtM23Dp3ozIC%2Fuploads%2FDxokUNScP9W6wAsxUPaV%2FCleanShot%202024-12-03%20at%2018.26.16.png?alt=media&#x26;token=4f6c1ab4-1026-496e-946b-8618124d3641" alt=""><figcaption></figcaption></figure>

Visit the [Implement Hosted Saved Rows](https://docs.beefree.io/beefree-sdk/rows/reusable-content/create/save/implement-hosted-saved-rows) page to learn more about customization options and integration details.

#### Self-hosted Saved Rows

[Self-hosted Saved Rows](https://docs.beefree.io/beefree-sdk/rows/reusable-content/create/save/implement-self-hosted-saved-rows) are similar to Hosted Saved Rows on the frontend, but require you to connect your own database on the backend. This feature also provides you with more customization options on the frontend if you'd more granular control over customizing your end user's experience saving and managing rows.

The following GIF shows an example of a customized modal for saving a row within an application. This modal uses both [saved rows](#hosted-saved-rows) and [content dialog](https://docs.beefree.io/beefree-sdk/other-customizations/advanced-options/content-dialog) for the customized experience.

<figure><img src="https://806400411-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F8c7XIQHfAtM23Dp3ozIC%2Fuploads%2FRGahp1J2cERkHkLpkO6s%2FCleanShot%202024-12-03%20at%2018.45.20.gif?alt=media&#x26;token=baf17914-631e-4d77-9dd9-358b3473102d" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
**Note:** Unlike Hosted Saved Rows, Self-hosted Saved Rows does require development.
{% endhint %}

#### Synced Rows

The purpose of [Synced Rows](https://docs.beefree.io/beefree-sdk/rows/reusable-content/sync/implement-synced-rows) is to maintain consistency by synchronizing row updates across multiple designs. A synced row can be reused across multiple designs and each design is updated whenever a synced row is updated. When you edit a synced row, you are redirected to [Edit Single Row Mode](https://docs.beefree.io/beefree-sdk/rows/reusable-content/sync/initialize-edit-single-row-mode).

<figure><img src="https://806400411-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F8c7XIQHfAtM23Dp3ozIC%2Fuploads%2FYiQ764sn5WhsuMkxrGcH%2FCleanShot%202024-12-03%20at%2018.57.13.gif?alt=media&#x26;token=59c74b2b-67fe-42a1-9710-76462d0e13e7" alt=""><figcaption></figcaption></figure>

#### Edit Single Row Mode

The purpose of Edit Single Row Mode is to allow precise editing of rows inside of a dedicated row builder. The GIF above displays an example of Edit Single Row Mode. Visit [Initialize Edit Single Row Mode](https://docs.beefree.io/beefree-sdk/rows/reusable-content/sync/initialize-edit-single-row-mode) to learn more about how to implement this feature.
