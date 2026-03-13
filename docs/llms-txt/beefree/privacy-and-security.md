# Source: https://docs.beefree.io/beefree-sdk/server-side-configurations/server-side-options/privacy-and-security.md

# Privacy and Security

{% hint style="info" %}
Every Beefree SDK plan includes privacy and security customization options, with additional advanced features available on paid plans.
{% endhint %}

## Overview

In the [Beefree SDK Developer Console](https://developers.beefree.io/), you'll find categories of **Application Configurations** you can customize to personalize your application. This page discusses the customization options available under the **Privacy and Security** section.&#x20;

This category of Application Configurations enable you to customize the following:

* Anonymous error logging
* Custom limitation for the [File Manager](https://docs.beefree.io/beefree-sdk/file-manager)
* [HTML sanitizer](https://docs.beefree.io/beefree-sdk/custom-head-html#the-sanitizer-and-adding-custom-html) for the HTML content block and [Custom Head HTML](https://docs.beefree.io/beefree-sdk/server-side-configurations/custom-head-html)

The following image shows how these options appear within the Developer Console.&#x20;

<figure><img src="https://806400411-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F8c7XIQHfAtM23Dp3ozIC%2Fuploads%2F2r5Q1QnzS6OW9gv1RuH6%2FCleanShot%202025-11-04%20at%2010.23.08.png?alt=media&#x26;token=d71a15d8-c4ff-4bc0-a65c-f367a9b9eb7e" alt=""><figcaption></figcaption></figure>

### Customizing Privacy and Security

This section defines what each customization option under **Privacy and Security** is. It also explains how to edit an existing configuration.

#### Edit an Existing Configuration

Take the following steps to edit an existing configuration:

1. Log in to the [Beefree SDK Developer Console](https://developers.beefree.io/).
2. Navigate to the application you'd like to edit a configuration for.
3. Click on **Details**.
4. Navigate to **Application Configuration** and click **Configure Application**.
5. Scroll down to the **Privacy and Security** section.
6. Select or deselect the configuration using the checkbox.
7. Click the purple **Save changes** button to apply the updated configuration to your application.

The following image shows an example of selecting the **Disable anonymous error logging** option with the Developer Console.

<figure><img src="https://806400411-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F8c7XIQHfAtM23Dp3ozIC%2Fuploads%2FPpPpNTTftnV8md91BiyO%2FCleanShot%202025-11-04%20at%2011.39.17.png?alt=media&#x26;token=4f211f1a-60fd-452b-a55b-a06146f9fbfe" alt=""><figcaption></figcaption></figure>

#### Anonymous Error Logging

We use third-party tools to aggregate anonymous usage data. It helps us develop a better product by assessing locations, devices, browsers, etc. This can be turned off if necessary.

#### HTML Sanitizer Service

* When you disable the HTML sanitization service, you’re removing all restrictions on what users of the builder can add inside the Custom HTML content block.
* The sanitize service checks and cleans up custom HTML, which can prevent the introduction of unsafe content or tags that might impact deliverability. However, disabling it can be useful if the host application needs custom HTML tags or attributes.
* If disabled, you should implement an alternative code review process, such as using the `onChange` or `onSave` [events](https://docs.beefree.io/beefree-sdk/getting-started/readme/installation/methods-and-events) to review content.
* The [client-side configuration](https://docs.beefree.io/beefree-sdk/getting-started/readme/installation/configuration-parameters) allows enabling (`forceSanitizeHTML: true`) per user, but cannot disable sanitization for security reasons.

Learn more about [Custom HTML](https://docs.beefree.io/end-user-guide/content-blocks/custom-html#html-tag-restrictions-in-emails) and [Custom Head HTML](https://docs.beefree.io/end-user-guide/design-tools/add-custom-head-html).

#### Custom Limitations on the File Manager

In this section, you can manage the restrictions for the [file manager](https://github.com/BeefreeSDK/beefree-sdk-docs/blob/main/server-side-configurations/server-side-options/services-options/broken-reference/README.md):

* Specify which file formats your users can upload.
* Set a maximum file size (limit: 20MB).

Instead of file extensions, categories such as image, video, or text are shown, mapped to [MIME types](https://docs.beefree.io/beefree-sdk/file-manager/file-manager-application-overview/file-extensions-and-groups).

The following image shows how you can manage the limitations to the File Manager.

<figure><img src="https://806400411-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F8c7XIQHfAtM23Dp3ozIC%2Fuploads%2F5bDoECzorstOgVbQndcB%2FCleanShot%202025-11-04%20at%2011.47.31.png?alt=media&#x26;token=ba28c17c-681f-4eab-9f2d-48728fcf8727" alt=""><figcaption></figcaption></figure>

#### File Type Limitations

The following table details which files are available for each Beefree SDK plan type.&#x20;

<table><thead><tr><th width="139">Plan type</th><th width="300">Default-allowed file types</th><th width="300">Configurable file types</th></tr></thead><tbody><tr><td>Free plans</td><td>Image, video, and PDF </td><td>No other file types can be added</td></tr><tr><td>Paid plans</td><td>Image, video, and PDF </td><td>Text, audio, office, xml, zip, epub, postscript, and font MIME types</td></tr></tbody></table>

If you’d like to allow your users to upload additional file types, you’ll need to explicitly enable those specific MIME types in the Custom Limitations section of your SDK Console.

#### Potentially Harmful Content Blocking

The system prevents harmful uploads by enforcing:

* Automatic blocking for all users of potentially dangerous file extensions such as exe, msi, bat, iso, jar, apk, SVGs containing JavaScript, HTML with redirects and more. These files can never be uploaded even if the custom limitations on the File Manager are removed.
* Antivirus scanning that targets malicious files.
