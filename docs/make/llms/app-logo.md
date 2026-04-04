# Source: https://developers.make.com/custom-apps-documentation/create-your-first-app/app-logo.md

# App logo

Every app in Make has its own logo and color. The combination of logo and color represents the app. With a distinct logo and color, the users quickly see which module belongs to which app.

<figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-3aed299ce29083b642a1f40ba41a5a820bc7552f%2FScreen%20Shot%202022-11-22%20at%2014.25.18%20(1).png?alt=media" alt="" width="563"><figcaption></figcaption></figure>

## App theme

The app theme is the module color in hexadecimal format. For example, the Make module's color is `#6e21cc`.

## App logo

To add a logo to your custom app, make sure your logo file meets these requirements:

* an image file in `.png` format
* square dimensions: minimum size 512 x 512 px and maximum size 2048 x 2048 px
* a maximum size of 500 kB

Make processes the logo file so that:

* Areas in the logo that are white or transparent will be displayed as the color specified in the **Theme** field.
* Areas in the logo that are black will be converted to full opacity and will be displayed as white.
* Areas in the logo that are in color or are semi-transparent will be displayed as the color between white and the color specified in the **Theme** field.

{% hint style="info" %}
If you don't have any tool to edit your file with the logo, you can use the [Lunapic](https://www9.lunapic.com/editor/) free editor.

For creating a transparent layer, you can use the [Transparent Background ](https://www9.lunapic.com/editor/?action=transparent)tool that is available in Lunapic.
{% endhint %}

## Examples of how logos are rendered

<figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-e0c01c285487e25d5bf4e83ce1e2a5aaf1eeb8e5%2Flogo_sample1.png?alt=media" alt=""><figcaption><p>Example of logos with one color</p></figcaption></figure>

<figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-6719da6b48fc353a6fbe7dd4dd88c34580070eb1%2Flogo_sample2.png?alt=media" alt=""><figcaption><p>Example of grayscale logos</p></figcaption></figure>

<figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-c82b739c92ef453380a34873b8fe70819ad91397%2Flogo_sample3.png?alt=media" alt=""><figcaption><p>Example of color logos</p></figcaption></figure>

## Work with semi-transparent pixels

An app can have only one theme color. You can use multiple transparency levels to give your logo multiple shades of the theme color. You can also create a 3D effect.

<figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-105f2232dd9988348ac5f99e2e8ca7089a97c343%2FScreen%20Shot%202022-11-22%20at%2016.49.05.png?alt=media" alt=""><figcaption><p>Example of apps with multiple transparency levels</p></figcaption></figure>

## Update the app's theme and/or logo

You can update the custom app's logo anytime. Navigate to your custom app settings and click **Options** > **Edit**.

{% hint style="warning" %}
If your app has been approved, the change of theme/logo needs to be approved by Make.
{% endhint %}

After you upload or update the logo or theme color, it may take up to 1 hour for the changes to be propagated across the Make platform.
