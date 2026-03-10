# Source: https://developers.webflow.com/designer/reference/create-an-asset.mdx

***

title: Create an Asset
slug: designer/reference/create-an-asset
description: Create a new asset on your Webflow site.
hidden: false
-------------

## `webflow.createAsset(fileBlob)`

Create a new asset on your Webflow site.

This method is specifically for creating new assets - if you need to update an existing asset, use the [set asset file](/designer/reference/set-asset-file) method instead. Be sure to review the [limits](#limits) and [MIME types](#mime-types) sections to ensure your files meet the requirements.

<Accordion title="Adding assets to pages">
  To add an asset to a page:

  1. Create an asset
  2. Create an [image element](/designer/reference/image-element)
  3. Use the [`element.setAsset(asset)`](/designer/reference/image-element/setAsset) method to set the asset
</Accordion>

### Syntax

```typescript
webflow.createAsset(fileBlob:File): Promise<Asset>
```

### Parameters

* **`fileBlob`**:`File` -  Represents a valid [File](https://developer.mozilla.org/en-US/docs/Web/API/File) to upload. Refer to the examples below for guidance on uploading an asset from a remote source and directly from a file picker.

### Returns

**Promise\<*Asset*>**

A Promise that resolves to the new Asset.

### Example

<Tabs>
  <Tab title="Remote File">
    ```typescript
    // Fetch image from remote source and build a Blob object
        const response = await fetch(url)
        const blob = await response.blob()
        const file = new File([blob], fileName, {
          type: 'image/png',
        })

        // Create and upload the asset to webflow
        const asset = await webflow.createAsset(file);
        console.log(asset)
    ```

    <div>
      <a href="https://webflow.com/oauth/authorize?response_type=code&client_id=19511de1ec410f9228d8dcbc9420e67916dea80d86d18f0c9a533eb475ea0f62">
        Try this example
      </a>
    </div>
  </Tab>

  <Tab title="Direct Upload">
    ```html HTML
    <!-- Add a file picker to your interface -->
    <input type="file" id="fileInput" />
    ```

    ```javascript
    // Reference the file input element
    const fileInput = document.getElementById('fileInput');

    // Add change event listener
    fileInput.addEventListener('change', async function () {
      try {
        // Check if the file input element is indeed an input element
        if (fileInput instanceof HTMLInputElement) {
          // Get the selected file from the file input
          const file = fileInput.files[0];

          // Check if a file is selected
          if (!file) {
            return; // Exit the function if no file is selected
          }

          // Upload the selected file and create an asset
          const asset = await webflow.createAsset(file);
        } else {
          console.error('Not an input element'); // Log an error if the file input is not an input element
        }
      } catch (err) {
        console.error('Something went wrong', err); // Log any errors that occur during the process
      }
    });
    ```
  </Tab>
</Tabs>

### Errors

If the method fails to create an asset, the method will return an error with the following cause and message.

| Tag                    | Message                                   |
| :--------------------- | :---------------------------------------- |
| ResourceCreationFailed | Failed to create asset for \$\{File.name} |

### Designer ability

| Designer Ability    | Locale | Branch | Workflow | Sitemode |
| :------------------ | :----- | :----- | :------- | :------- |
| **canManageAssets** | any    | any    | any      | any      |

## Limits

Uploaded assets must adhere to specific size limitations:

* Images must not exceed 4MB
* Documents must not exceed 10MB

## MIME types

Refer to the accepted MIME types listed below for compatibility. Pass Lottie files as `application/json` MIME types.

```Text MIME Types
'image/jpeg'
'image/jpg'
'image/png'
'image/gif'
'image/svg+xml'
'image/bmp'
'image/webp'
'application/pdf'
'application/msword'
'application/vnd.ms-excel'
'application/vnd.ms-powerpoint'
'application/vnd.openxmlformats-officedocument.wordprocessingml.document'
'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
'application/vnd.openxmlformats-officedocument.presentationml.presentation'
'text/plain'
'text/csv'
'application/vnd.oasis.opendocument.text'
'application/vnd.oasis.opendocument.spreadsheet'
'application/vnd.oasis.opendocument.presentation'
'application/json'
```
