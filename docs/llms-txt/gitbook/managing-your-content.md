# Source: https://gitbook.com/docs/help-center/editing-content/managing-your-content.md

# Moving your content

## Is there a limit on the content import size?

The best way to import content into GitBook is via [GitSync](https://www.gitbook.com/solutions/git-sync). This allows you to upload up to 5000 markdown pages.

We do support other [import formats](https://gitbook.com/docs/content-editor/import) but the functionality is more limited. Currently we have the following limits for imported content:

* The import feature allows a maximum of 20 pages to be uploaded simultaneously.
* The maximum number of files that can be uploaded in a single import is limited to 20.

### **Can I request an increase in the import limit?**

Currently, we’re unable to provide increases in import limits.

***

## How can I export my content?

You can export your GitBook content:

* in Markdown format by enabling GitHub or GitLab sync
* as a PDF (you may encounter limits when exporting very large spaces)

### How to export content in Markdown format

You cannot export pages as Markdown directly within the GitBook app, but you can use GitHub or GitLab sync to sync your space with a Git repository and generate a Markdown export this way.

You’ll need to synchronize the space containing the content you want to export with an empty repository. Read our documentation on [setting up the GitHub or GitLab sync](https://gitbook.com/docs/integrations/git-sync) to get started.

{% hint style="info" %}
Some custom blocks do not have a representation in Markdown, therefore they will appear as HTML in your export.
{% endhint %}

***

## Can I move a page between spaces?

We do not currently support moving individual pages between spaces in the app.

To move the content of a page from one space to another, you can use one of the options below.

### Copy and paste&#x20;

To move a one or a few pages we recommend selecting the content using the `Esc`  key and copying and pasting it to your new destination. This is a manual process, but the most efficient one for smaller content changes.

{% hint style="info" %}
**Note:** Some blocks may need to be reconfigured during this process. \
Comments and page history will not be copied and you will need to re-upload your images to the new space.
{% endhint %}

### Use Git Sync to move pages

This approach is beneficial if you already have [Git Sync](https://gitbook.com/docs/integrations/git-sync) enabled in your space.

You first need two repositories — your main one with the content you want to **copy the content from** and a new one that you’re **copying the pages into**.

1. Enable Git Sync in both spaces and make sure they sync the correct repositories as mentioned above.
2. Clone both repositories to your local machine/computer
3. Open both cloned copies of your repositories in a text editor of choice
4. Add the space page titles from the current space to SUMMARY.md in the new space
5. Copy the files from the original space to the new one
6. Commit the changes in the new repository
7. Wait for GitBook to sync and import the changes

Here's a video showing the same process outlined above:

{% embed url="<https://www.loom.com/share/76b8f3dc5ff542f18cf034c26c94fe2b?sid=00cbea46-9fb2-46ba-9c75-e9e8cf7df36e>" %}

***

## Can I move a space between organizations?

We do not currently support moving spaces between organizations, even if you are an admin in both of them.

We'd recommend you either:

* [Export your content and import it back to GitBook ](#how-to-export-content-in-markdown-format)
* [Use Git Sync to move pages](#use-git-sync-to-move-pages)
