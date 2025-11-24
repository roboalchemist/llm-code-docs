# Source: https://docs.anchorbrowser.io/advanced/extensions.md

# Browser Extensions

> Upload and use custom browser extensions in your sessions

Anchor allows you to upload and use Chrome extensions in your browser sessions. This lets you add ad blockers, privacy tools, or any other extension to enhance your browsing automation.

For uploading, listing, and managing extensions, see the [interactive API documentation](/api-reference/extensions).

## Getting Extensions from Chrome Web Store

To use extensions from the Chrome Web Store, you'll need to download and inspect their files:

### Download Extension Files

1. **Install CRX Extractor/Downloader** - Add this extension to your browser to download .zip files
2. **Navigate to the extension** you want on the Chrome Web Store
3. **Click the CRX Extractor icon** and download the .zip file
4. **Extract the ZIP** to inspect the contents

### Inspect Extension Contents

Once extracted, you'll see the extension's files:

* `manifest.json` - Contains extension metadata and permissions
* `background.js` or `service_worker.js` - Background scripts
* `content_scripts/` - Scripts that run on web pages
* `popup.html` - Extension popup interface
* `icons/` - Extension icons

### Repackage for Upload

After inspecting (and optionally modifying) the files:

1. **Select all files and folders** in the extracted directory
2. **Create a new ZIP file** containing all the extension files
3. **Upload this ZIP** to AnchorBrowser using the SDK

## Extension Requirements

Your extension ZIP file must contain a valid `manifest.json` with basic extension information like name and version.

### Example Manifest

```json  theme={null}
{
  "manifest_version": 3,
  "name": "My Extension",
  "version": "1.0.0",
  "description": "Extension description",
  "permissions": ["activeTab", "storage"],
  "background": {
    "service_worker": "background.js"
  },
  "content_scripts": [{
    "matches": ["<all_urls>"],
    "js": ["content.js"]
  }]
}
```

## Code Example

<CodeGroup>
  ```javascript node.js theme={null}
    import AnchorBrowser from 'anchorbrowser';
    import fs from 'fs';

    const anchor_client = new AnchorBrowser({apiKey: process.env.ANCHOR_API_KEY});

    const extension = await anchor_client.extensions.upload({
      file: fs.createReadStream('./my-extension.zip'),
      name: 'My Custom Extension'
    });
    const extensionId = extension.data.id;
    console.log("ExtensionId:", extensionId);

    const session = await anchor_client.sessions.create({
      browser: {
        extensions: [extensionId]
      }
    });
    console.log("Session:", session);
  ```

  ```python python theme={null}
    from anchorbrowser import Anchorbrowser
    import os

    anchor_client = Anchorbrowser(api_key=os.getenv("ANCHOR_API_KEY"))

    with open('./my-extension.zip', 'rb') as file:
      extension = anchor_client.extensions.upload(file=file,name='My Custom Extension')
    extensionId = extension.data.id
    print("ExtensionId:", extensionId)

    session = anchor_client.sessions.create(browser={
        "extensions": [extensionId]
      })
    print("Session:", session)
  ```
</CodeGroup>

## Limitations

* Maximum extension size: 50MB per ZIP file
* Extensions must be valid Chrome extensions
