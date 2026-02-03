# Source: https://gitbook.com/docs/documentation/ja-gitbook-documentation/getting-started/import.md

# Source: https://gitbook.com/docs/documentation/zh/getting-started/import.md

# Source: https://gitbook.com/docs/documentation/fr/getting-started/import.md

# Source: https://gitbook.com/docs/getting-started/import.md

# Migrate to GitBook

You can migrate and unify existing documentation in GitBook using the import tool.

You have the option to import single or multiple pages using our built-in import tool — or [an entire Git repository using Git Sync](#import-using-git-sync).

## Using the Import panel

The Import panel makes it easy to migrate your content into your GitBook organization from another documentation website or from existing files.

When you choose to import from another online documentation site, all you have to do is add the URL of the site and GitBook will handle the rest.

By default, GitBook uses AI to streamline the import process. This will intelligently refine and clean up imported content that doesn’t perfectly match GitBook’s formats — meaning the output will be more polished and use GitBook’s blocks more effectively. You can disable this from the menu.

### Supported import formats

GitBook supports imports from docs websites or files in the following formats:

* Markdown (`.md` or `.markdown`)
* HTML (`.html`)
* Microsoft Word (`.docx`)

GitBook also support imports from:

* Confluence
* Notion
* GitHub Wiki
* Quip
* Dropbox Paper
* Google Docs

If you want to **import multiple pages**, you can upload a ZIP file containing HTML or Markdown files, or use the **Online docs** import option.

{% hint style="info" %}
GitBook is Markdown-based, so importing content in Markdown format will yield the best results. If your current tools support exporting in Markdown, we recommend using that format for a smoother import process.
{% endhint %}

### The Import panel

<figure><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2F8omDHqTDwNkvdG6Hv81q%2FImport%402x%20(1).png?alt=media&#x26;token=a5c0993c-f49a-4911-8297-6e76f0435bcb" alt="A GitBook screenshot showing the import panel"><figcaption><p>The import panel in GitBook.</p></figcaption></figure>

When you create a new space, you’ll have the option to import content in the modal that appears. If you create an empty space, you can also import using the **Quickstart** section at the bottom of the new empty page when you click **Edit**.

Alternatively, you can always import a page or subpage by selecting **Add new** > **Import pages** at the bottom of the [table of contents](https://gitbook.com/docs/resources/gitbook-ui#table-of-contents), or by opening the **Actions menu** <picture><source srcset="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FQ4IsWwmEEi5QM7PSXNsN%2Factions%20-%20dark.svg?alt=media&#x26;token=ebff54f4-9825-4ab0-99bc-633e1c449371" media="(prefers-color-scheme: dark)"><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2F89MTSo5XRpPMVr1T0rxS%2Factions.svg?alt=media&#x26;token=2b5d001e-560a-4f29-8d22-de8163725ca1" alt="The Actions menu icon in GitBook"></picture> for a page and choosing **Import subpages**.

After choosing an input source, you can select the file you’d like to import.

{% hint style="warning" %}
GitBook imports content from various sources, but differences in product features and document formats may cause variations in the imported content compared to the original source.
{% endhint %}

### Limitations

GitBook currently has the following limits for imported content:

* The maximum number of pages that can be uploaded in a single import is **20**.
* The maximum number of files (images etc.) that can be uploaded in a single import is **20**.

***

## Import from a GitHub or GitLab repo using Git Sync <a href="#import-using-git-sync" id="import-using-git-sync"></a>

When importing large volumes of content into GitBook, we recommend using [Git Sync](https://gitbook.com/docs/getting-started/git-sync). While our built-in migration tool can handle most imports, Git Sync is better suited for handling larger migrations efficiently.

{% hint style="info" %}
You’ll find the essential steps to import your content below. For more detailed steps and a video demo, head over to our dedicated guide for [importing content into GitBook using Git Sync](https://app.gitbook.com/s/LBGJKQic7BQYBXmVSjy0/editing-and-publishing-documentation/import-or-migrate-your-content-to-gitbook-with-git-sync).
{% endhint %}

{% stepper %}
{% step %}
**Convert your content into Markdown**

GitBook is Markdown-based, so importing content in Markdown format will yield the best results. If your current tools support exporting in Markdown, we recommend using that format for a smoother import process.

If your content isn’t already in Markdown files, we recommend using a script (like [Markitdown](https://github.com/microsoft/markitdown)) or an online tool to convert your content.
{% endstep %}

{% step %}
**Organize your content in GitHub or GitLab**

When setting up your GitBook site, it’s crucial to organize your content in your GitHub or GitLab repository efficiently. Since Git Sync occurs at the space level, carefully plan how to group your content. Create multiple repositories or folders, ensuring the necessary Markdown files are in the correct locations.
{% endstep %}

{% step %}
**Set up spaces and configure Git Sync**

To organize your content, create one or more spaces in GitBook as needed. Install the [GitHub Sync](https://www.gitbook.com/integrations/github-sync) or [GitLab Sync](https://www.gitbook.com/integrations/gitlab-sync) integrations in your organization and configure it for those spaces. You’ll need to synchronize your space with the folder or repository you set up in the previous step.
{% endstep %}

{% step %}
**Run Git Sync in the direction GitHub → GitBook**

When following the configuration process, make sure you select the direction of GitHub → GitBook. This will result in the contents of your folder or repository being pulled from GitHub or GitLab into GitBook.
{% endstep %}
{% endstepper %}
