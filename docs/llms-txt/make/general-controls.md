# Source: https://developers.make.com/custom-apps-documentation/get-started/make-apps-editor/apps-sdk/general-controls.md

# Use general controls

The following are basic controls in VS Code.

## Add a new item

To add a new item such as a module, connection, or webhook, right-click the corresponding folder and click the **New \<item>** option.

<div align="left"><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-fa9c986be97acd5bad9b374497cf6a615c2a8945%2FScreen%20Shot%202022-08-22%20at%2013.51.12.png?alt=media" alt="" width="563"></div>

Each time the prompt appears, you are asked to fill in information about the newly created item. Follow the indicated prompts to create an item. Your new item appears under the corresponding folder.

<div align="left"><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-2e3fad6a5d2903ded25b32fd33d74543ab90c277%2FScreen%20Shot%202022-08-22%20at%2013.54.01.png?alt=media" alt="" width="563"></div>

## Edit the source code

To start editing the source code, find the item to edit in the left menu and click it.

A new editor will appear and the current source will be downloaded from Make.

You can edit it as a normal file. If your app contains some RPCs or IML functions, you will see auto-complete suggestions for them.

<div align="left"><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-3f3dca0a995aac9066868d1de372a3cd12c99684%2Fctrl_src_01.png?alt=media" alt="" width="563"></div>

{% hint style="info" %}
Use the shortcut `CTRL+S` to upload the source code back to Make.
{% endhint %}

## Edit metadata

To edit metadata (for example, to change the label of a module), right-click the desired item and select the **Edit metadata** option from the menu.

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-82c6d496bacad985b4c521ce66a00bd5f4d164c8%2FScreenshot%202024-05-09%20at%206.10.18.png?alt=media" alt="" width="563"><figcaption></figcaption></figure></div>

In the prompt, change allowed values. If you don't want to change a value, skip the field by pressing the **Enter** key.

## Change the connection or webhook

To change the attached connection or webhook of an item, right-click the item and select the **Change connection (or webhook)** option from the menu.

<div align="left"><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-eb1c0b0dcaddee0aed059688398815a542f69875%2FScreen%20Shot%202022-08-22%20at%2013.56.39.png?alt=media" alt="" width="563"></div>

In the prompt, change the connection or webhook. If possible, there will also be an option to unassign the current connection without assigning a new one.

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-283631c92a064e4877e9e2a8d930eb3bac713ce8%2FScreenshot%202024-05-09%20at%206.16.57.png?alt=media" alt="" width="563"><figcaption></figcaption></figure></div>

You will also see a prompt to assign an alternative (secondary) connection. The alternative connection should not be the same as the main connection. You can leave it empty.

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-70117cf44f4eac8cee9bd3de1eadaf46072e058f%2FScreenshot%202024-05-09%20at%206.18.28.png?alt=media" alt="" width="563"><figcaption></figcaption></figure></div>

## Delete an item

To delete an item, right-click it and select **Delete**.

<div align="left"><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-f195d5f80cea9a464f69d7a5a8ebe8b7e3a4f199%2FScreen%20Shot%202022-08-22%20at%2014.08.27.png?alt=media" alt="" width="563"></div>

You will be asked to confirm the deletion. If you answer **Yes**, the item will be deleted from the app.

<div align="left"><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-bf0bd9902233bd770429ca7f28f03655bd361982%2FScreen%20Shot%202022-08-22%20at%2014.14.26.png?alt=media" alt="" width="563"></div>

{% hint style="warning" %}
Deleting items is only possible in private apps. Once an app is published, the capability to delete items within the app is disabled. Learn more about [your apps' visibility](https://github.com/integromat/make-apps-sdk-docs/blob/master/get-started/make-apps-editor/apps-sdk/broken-reference/README.md) and the deletion of items.
{% endhint %}

## Generate the interface code

Use the [Interface Generator](https://developers.make.com/custom-apps-documentation/component-blocks/interface#interface-generator) to generate an interface.
