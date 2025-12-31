# Source: https://gitbook.com/docs/documentation/zh/creating-content/blocks/insert-files.md

# Source: https://gitbook.com/docs/documentation/fr/creating-content/blocks/insert-files.md

# Source: https://gitbook.com/docs/creating-content/blocks/insert-files.md

# Source: https://gitbook.com/docs/documentation/zh/creating-content/blocks/insert-files.md

# Source: https://gitbook.com/docs/documentation/fr/creating-content/blocks/insert-files.md

# Source: https://gitbook.com/docs/creating-content/blocks/insert-files.md

# Files

You can upload files to your GitBook space and add them to your page for people to view or download.

You can show some files, such as images and OpenAPI files, on the page itself for people to see without clicking anything. For others, such as PDFs, users will have to click to view or download it.

You can also optionally add a caption below any file you insert into your page to add more information if needed.

### Example of a file <a href="#example-of-a-file" id="example-of-a-file"></a>

{% file src="<https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2Fgit-blob-9ff1c1eef1d9ee1744295e274d3ee01fae848a20%2Fexample.pdf?alt=media>" %}
This is a caption on a file.
{% endfile %}

### Uploading a file

You can manage uploaded files in the Files side panel of your space. You can find the Files panel at the top of your space’s table of contents.

To upload a file, drag and drop it into the **Drop your file or browse** section, or select it and use your system file dialog to select the file you want to upload.

{% hint style="warning" %}
GitBook allows you to upload files up to 100MB per file.
{% endhint %}

You can also add files to your space when you add an [image block](https://gitbook.com/docs/creating-content/blocks/insert-images) or an [OpenAPI block](https://gitbook.com/docs/api-references/openapi). When you create one of these blocks, the Files panel will open, so you can either select a file, or upload a new file.

{% hint style="info" %}
**Tip:** You can also drag and drop images from your file system directly into the editor — or paste a copied image into your content. GitBook will automatically add them to the Files side panel for the respective space, so you can view and manage them later.
{% endhint %}

### Renaming a file

To rename a file, open the **Actions menu** <picture><source srcset="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FQ4IsWwmEEi5QM7PSXNsN%2Factions%20-%20dark.svg?alt=media&#x26;token=ebff54f4-9825-4ab0-99bc-633e1c449371" media="(prefers-color-scheme: dark)"><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2F89MTSo5XRpPMVr1T0rxS%2Factions.svg?alt=media&#x26;token=2b5d001e-560a-4f29-8d22-de8163725ca1" alt="The Actions menu icon in GitBook"></picture> for the file, and click **Edit**. In the dialog prompt, enter the new name of your file.

### Deleting a file

To delete a file, open the **Actions menu** <picture><source srcset="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FQ4IsWwmEEi5QM7PSXNsN%2Factions%20-%20dark.svg?alt=media&#x26;token=ebff54f4-9825-4ab0-99bc-633e1c449371" media="(prefers-color-scheme: dark)"><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2F89MTSo5XRpPMVr1T0rxS%2Factions.svg?alt=media&#x26;token=2b5d001e-560a-4f29-8d22-de8163725ca1" alt="The Actions menu icon in GitBook"></picture> for the file and click **Delete**. After confirming in the dialog that you’re sure you want to delete the file, your file will be deleted.

{% hint style="warning" %}
**Note:** Make sure you update any pages that included your deleted file! File blocks that reference a deleted file will show an empty block, or *Could not load image* error.
{% endhint %}

### Replacing a file

If you have a file that simply needs updating to a new version, you can replace it. This will swap out the old file and put the new file in its place. Any blocks that previously referred to the old file will then refer to the new file.

To replace a file, open the **Actions menu** <picture><source srcset="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FQ4IsWwmEEi5QM7PSXNsN%2Factions%20-%20dark.svg?alt=media&#x26;token=ebff54f4-9825-4ab0-99bc-633e1c449371" media="(prefers-color-scheme: dark)"><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2F89MTSo5XRpPMVr1T0rxS%2Factions.svg?alt=media&#x26;token=2b5d001e-560a-4f29-8d22-de8163725ca1" alt="The Actions menu icon in GitBook"></picture> for the file and click **Replace**. In the file replacement dialog that appears, select the new file and wait for the upload indicator to complete. Your file will automatically update everywhere it appeared in your space.

This can be helpful if, for example, you’ve had a major product redesign and need to update outdated UI screenshots that appear on multiple pages. Replacing the original file would update the screenshot everywhere in your space, saving you time and effort.

{% hint style="info" %}
**Tip:** Once you’ve uploaded an image or a file, you can reference it anywhere in your space by creating an image or a file block and selecting it from the **Files** side panel.

We recommend you do this rather than uploading the image again every time you want to include it, to make it easier to replace images later and to avoid having multiple files with the same name.
{% endhint %}

### Representation in Markdown

```markdown
{% file src="https://example.com/example.pdf" %}
    This is a caption for the example file.
{% endfile %}
```
