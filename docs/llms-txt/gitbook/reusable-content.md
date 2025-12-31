# Source: https://gitbook.com/docs/documentation/zh/creating-content/reusable-content.md

# Source: https://gitbook.com/docs/documentation/fr/creating-content/reusable-content.md

# Source: https://gitbook.com/docs/creating-content/reusable-content.md

# Source: https://gitbook.com/docs/documentation/zh/creating-content/reusable-content.md

# Source: https://gitbook.com/docs/documentation/fr/creating-content/reusable-content.md

# Source: https://gitbook.com/docs/creating-content/reusable-content.md

# Reusable content

{% hint style="info" %}
This feature is available on [Pro and Enterprise plans](https://www.gitbook.com/pricing).
{% endhint %}

Reusable content lets you sync content across multiple pages and spaces, so you can edit all instances of the block at the same time.

<figure><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2F21nR8UJaA970B2iHPCWL%2Fcreating-content-reusable-content%402x.png?alt=media&#x26;token=ec03b404-3254-485c-bbee-9d4864cf3aac" alt="A GitBook screenshot showing reusable content"><figcaption><p>Create reusable content within a space.</p></figcaption></figure>

## Fundamentals

Reusable content works just like any other content—you can modify it via change requests, include it in review workflows, and it will render correctly on any published site.

While reusable content can be referenced across multiple spaces, it belongs to a single *parent space*.

### The "parent space" concept

The parent space is the space that owns the reusable content. It’s the only place where that content can be edited.

Even though updates to reusable content will appear instantly in all instances, all changes must originate from the parent space—either as a direct edit or through a change request.

Spaces are a core concept in GitBook, supporting both editorial workflows and security. Because GitBook enforces permission-based editing, reusable content can only be changed from its parent space. This ensures that editing rights are respected, even when the content is reused across the organization.

### Known limitations

#### Integrations

Blocks provided by integrations are not supported in reusable content. This is because integrations in GitBook are installed per space, and limiting access ensures that third-party integrations only have the permissions you grant. Referencing reusable content across spaces would break this security boundary.

#### Search

Currently, reusable content only appears in search results within its parent space. We’re actively working to remove this limitation so that reusable content shows up in search results wherever it’s referenced.

## In the app

### **Create reusable content**

To create reusable content, [select one or more blocks](https://gitbook.com/docs/blocks#selecting-blocks-and-interacting-with-selected-blocks), then open the **Actions menu** <picture><source srcset="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FQ4IsWwmEEi5QM7PSXNsN%2Factions%20-%20dark.svg?alt=media&#x26;token=ebff54f4-9825-4ab0-99bc-633e1c449371" media="(prefers-color-scheme: dark)"><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2F89MTSo5XRpPMVr1T0rxS%2Factions.svg?alt=media&#x26;token=2b5d001e-560a-4f29-8d22-de8163725ca1" alt="The Actions menu icon in GitBook"></picture> , select **Turn into**, and choose **Reusable content**. You can also give your block a name to make it easier to find and reuse later.

Alternatively, you can select one or more blocks and then hit **Cmd + C** to open a prompt asking if you want to create reusable content.

### **Insert reusable content**

You can insert reusable content as you would with any other block. Hit `/` on an empty line to open the **Insert palette** and search for your content by its name or simply searching for “reusable”. Alternatively, click the `+` on the left of any block or empty line.

You will also find the reusable content panel in the pages sidebar, where you can find a list of previously created content blocks in your current space.

### **Edit reusable content**

Reusable content is like any other content — you can edit any instance directly if [live edits](https://gitbook.com/docs/collaboration/live-edits) are enabled, or through [a change request](https://gitbook.com/docs/collaboration/change-requests) if not. Any changes you make will be synced everywhere the content is used.

If you’re making changes inside a change request, the content will be synced to all other instances once that change request is merged.

### **Detach reusable content**

You can detach reusable content by opening the **Actions menu** <picture><source srcset="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FQ4IsWwmEEi5QM7PSXNsN%2Factions%20-%20dark.svg?alt=media&#x26;token=ebff54f4-9825-4ab0-99bc-633e1c449371" media="(prefers-color-scheme: dark)"><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2F89MTSo5XRpPMVr1T0rxS%2Factions.svg?alt=media&#x26;token=2b5d001e-560a-4f29-8d22-de8163725ca1" alt="The Actions menu icon in GitBook"></picture> and selecting **Detach**. Detaching will convert the content back to regular blocks.

Once detached, any changes you make to the block(s) will not be reflected across the other instances, and changes you make in those instances will not be reflected in the detached block(s). All other instances of the reusable content remain synced together.

### Delete reusable content

You can delete reusable content from your space entirely, if you wish. Find the reusable content in the page’s table of contents, then open the **Actions menu** <picture><source srcset="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FQ4IsWwmEEi5QM7PSXNsN%2Factions%20-%20dark.svg?alt=media&#x26;token=ebff54f4-9825-4ab0-99bc-633e1c449371" media="(prefers-color-scheme: dark)"><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2F89MTSo5XRpPMVr1T0rxS%2Factions.svg?alt=media&#x26;token=2b5d001e-560a-4f29-8d22-de8163725ca1" alt="The Actions menu icon in GitBook"></picture> next to the content you’d like to delete, and select **Delete**.

Deleting reusable content will **delete it from all pages it is used in**. This action cannot be undone.

## Syncing with GitHub & GitLab

Reusable content is fully supported when syncing to GitHub & GitLab. Your reusable content will be exported to a dedicated `includes` folder, each content being a separate Markdown file.

Your content is then referenced in your other pages using the `includes` directive.

{% hint style="info" %}
When syncing, the `.gitbook/includes` directory is created in the root of each synced space (which may not be the root of the whole repository). If your `.gitbook/includes` folder or its files appear in your space’s table of contents, you may need to hide them manually from the TOC.
{% endhint %}

#### Example

{% hint style="success" %}
If you're writing on the GitHub side, ensure the path to the include is relative to the file containing the reference (not the root of the repository).
{% endhint %}

```markdown
{% include "../../.gitbook/includes/reusable-block.md" %}
```
