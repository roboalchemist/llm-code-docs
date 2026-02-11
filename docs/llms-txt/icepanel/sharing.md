# Source: https://docs.icepanel.io/collaboration/sharing.md

# Share links & embeds

Sharing knowledge is critical to everyone being on the same page about how your system works and what is being built. IcePanel Share links make this easy, allowing a read-only and up-to-date version of your design to be shared with a URL. Share links can also be protected with passwords or SSO so only the right people can access your diagrams.

In addition to links, landscapes and diagrams can be embedded in the following collaboration tools:

* Confluence
* Notion
* Miro
* Microsoft Sharepoint

{% hint style="success" %}
Viewers are free on all IcePanel plans. Only admins and editors in a landscape can create share links.
{% endhint %}

## Share link types

### Creating a public share link

Public share links are accessible to anyone with the URL and are read-only. You can share a link to your landscape or a diagram at any level.

To create a public share link:

1. Click on the `Share` button on the top right of the navigation (in a landscape or diagram)
2. Click on the `Share link` tab
3. Turn on the `Share link for latest version` toggle
4. Click on the `Copy link` button

{% hint style="info" %}
**Tip:** When you share a link, viewers will be put exactly where you are when creating your link with the same zoom level, selected objects, and tag groups displayed. You can also have viewers enter a specific flow directly by opening it and sharing a link.
{% endhint %}

<figure><img src="https://4065434276-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FOHewp5hylgOsOa0VDOBo%2Fuploads%2FAgdeMtatbxKS84LxeJ0i%2FShare-Diagram-Public.gif?alt=media&#x26;token=a6262a6d-9619-4b5f-aecf-f2bff6b9ffa4" alt=""><figcaption><p>Creating a public share link for a diagram</p></figcaption></figure>

### Creating a private share link

{% hint style="info" %}
Password and SSO-protected links are only available on Growth and Isolation plans.
{% endhint %}

Share links can be password-protected for an additional layer of security.

To turn on password protection on links:

1. Click on the `Share` button on the top right of the navigation (in a landscape or diagram)
2. Click on the `Share link` tab
3. With the Share link toggle on, click on the `Password protect` toggle
4. Enter the password (must be at least 8 characters)

{% hint style="warning" %}
To set up SSO links, you need to have SSO enabled. See [sso-saml](https://docs.icepanel.io/other-information/sso-saml "mention")
{% endhint %}

<figure><img src="https://4065434276-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FOHewp5hylgOsOa0VDOBo%2Fuploads%2FfQUjyphH0uVut3tA0dza%2FShare-Diagram-Private.gif?alt=media&#x26;token=6fd20980-4121-4cc9-9366-7c0858b9287d" alt=""><figcaption><p>Creating a password protected share link</p></figcaption></figure>

## Sharing versions

By default, your share links will be from the latest version of your landscape or diagrams.

To share previous versions:

1. Click on the `Latest` dropdown. This is located below the landscape dropdown in the top navigation in a landscape or the top left of the screen beside the object name in a diagram
2. Select the version you want to share
3. Click on the `Share link` tab
4. Turn on the `Share link for latest version` toggle
5. Click on the `Copy link` button

For more information on versioning, see [versioning](https://docs.icepanel.io/future-state-design/versioning "mention")

## Share link settings

### Resetting a share link

You can reset a link to remove access to an existing link and create a new one.

To reset a share link:

1. Click on the `Share` button on the top right of the navigation (in a landscape or diagram)
2. Click on the `Share link` tab
3. With the Share link toggle on, click on `Reset` to the right

{% hint style="warning" %}
Resetting the link will remove access to **all active** share links in the landscape's version.
{% endhint %}

<figure><img src="https://4065434276-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FOHewp5hylgOsOa0VDOBo%2Fuploads%2FIyxQjTVZIvoEuGnZUsA7%2FScreenshot%202024-10-02%20at%201.46.05%E2%80%AFPM.png?alt=media&#x26;token=ca6a1e24-02f2-4a50-9323-758c5ad2091e" alt=""><figcaption><p>Resetting a share link</p></figcaption></figure>

### Preventing navigation in a link

When you share a link to a diagram, viewers can navigate between the different levels.&#x20;

To disable this:

1. Click on the `Share` button on the top right of the navigation in a diagram
2. Click on the `Share link` tab
3. Turn on the `Prevent navigation` toggle

<figure><img src="https://4065434276-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FOHewp5hylgOsOa0VDOBo%2Fuploads%2F88oKgCdViYPhFHqgShd9%2FScreenshot%202024-10-02%20at%201.52.15%E2%80%AFPM.png?alt=media&#x26;token=a5f181af-dc9f-451e-9853-b79042410d65" alt=""><figcaption><p>Preventing navigation in a share link</p></figcaption></figure>

### Disabling share links

Only admins and editors can create shared links for landscapes and diagrams by default.

To disable share links globally in the organization:

1. Open the Organization dropdown and click on `Manage` (only visible to Admins)
2. Go to Sharing
3. Turn off the `Share links` toggle

<figure><img src="https://4065434276-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FOHewp5hylgOsOa0VDOBo%2Fuploads%2F6w9NJH0buxBQbduElt7L%2Fimage.png?alt=media&#x26;token=08334628-237a-491a-a56f-fd8e0c9c7615" alt=""><figcaption><p>Disabling share links in an organization</p></figcaption></figure>

{% hint style="info" %}
If you disable global share links, users will still be able to toggle share links on in the app (but they won't be accessible).
{% endhint %}

## Embedding share links

Landscapes and diagrams can be embedded via iFrames in other tools. If you share the latest version, these links will also remain up-to-date.

To embed a landscape or diagram:

1. Click on the `Share` button on the top right of the navigation (in a landscape or diagram)
2. Click on the `Share link` tab
3. With Share links enabled, select the tool in the embed list
4. Copy the share link or the iFrame code

### Embed in Notion

1. In a Notion page, paste your IcePanel share link
2. Select the `Create embed` option in the dropdown
3. Resize the embedded URL to max width and height so it's readable by your viewers

<div data-full-width="false"><figure><img src="https://4065434276-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FOHewp5hylgOsOa0VDOBo%2Fuploads%2Fn6bQSUf58xB9w8T4uDOI%2FEmbed-Notion.gif?alt=media&#x26;token=689b72c1-20a3-43f1-a81a-63392d8bc3c4" alt=""><figcaption><p>Embedding a diagram in Notion</p></figcaption></figure></div>

### Embed in Miro

1. In a Miro board, click on the `More apps` button and select `Embed iFrame code`
2. Copy the iFrame code from IcePanel with your share link
3. Paste the iFrame code in Miro's text field and click `Embed`

Viewers must click on the iFrame image to load and interact with the landscape or diagram.

We recommend adding a link to the up-to-date share link by:

1. Selecting the iFrame
2. Add a link by using hotkey `Cmd + K` or `Ctrl + K` or by selecting the 3 dots menu on the image and then selecting `Link to`
3. Paste in the share link

<figure><img src="https://4065434276-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FOHewp5hylgOsOa0VDOBo%2Fuploads%2FChIfe2y6WCSv9jDyWVku%2FEmbed-Miro.gif?alt=media&#x26;token=737ffdbb-4e17-4ea9-9593-92f13e44bb7d" alt=""><figcaption><p>Embedding a diagram in Miro</p></figcaption></figure>

### Embed in Confluence

1. Insert an iFrame macro with the + icon from the toolbar
2. Copy your IcePanel share link
3. Paste the share link in the URL field
4. Set the width to 100% and height to 800
5. If your Confluence page is set to a fixed width, set “Go full width” under iFrame *(optional)*
6. Add your share link under the iFrame for a direct link *(optional)*

<figure><img src="https://4065434276-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FOHewp5hylgOsOa0VDOBo%2Fuploads%2FHZVnirYUrNuCd7GZS5s2%2FEmbed-Confluence.gif?alt=media&#x26;token=5f599712-8241-41a4-8779-dde9425032d5" alt=""><figcaption><p>Embedding a diagram in Confluence</p></figcaption></figure>

### Embed in SharePoint

**Using URL:**

1. Insert an embed web part from the + list
2. Paste your IcePanel share link
3. Click "resize to fit the page"

**Using embed code:**

1. Insert an embed web part from the + list
2. Paste your IcePanel share link in this format: `<iframe src="s.icepanel.io/____" height="800" width="1200" title="Your landscape / diagram name"></iframe>`
3. We recommend using a maximum height and width or a minimum Height=800, Width=1200
