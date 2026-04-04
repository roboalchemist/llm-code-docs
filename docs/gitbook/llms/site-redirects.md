# Source: https://gitbook.com/docs/developers/gitbook-api/api-reference/docs-sites/site-redirects.md

# Source: https://gitbook.com/docs/documentation/ja-gitbook-documentation/publishing-documentation/site-redirects.md

# Source: https://gitbook.com/docs/documentation/zh/publishing-documentation/site-redirects.md

# Source: https://gitbook.com/docs/documentation/fr/publishing-documentation/site-redirects.md

# Source: https://gitbook.com/docs/publishing-documentation/site-redirects.md

# Site redirects

{% hint style="info" %}
This feature is available on [Premium and Ultimate site plans](https://www.gitbook.com/pricing).
{% endhint %}

<figure><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FSOD2dR0Bb3RtX6Avb7vg%2F26_01_06_redirects%402x.png?alt=media&#x26;token=7e2bf0a2-947c-46d7-96ff-a4e6b54e60b2" alt="A GitBook screenshot showing site redirects"><figcaption><p>Site redirects are useful when migrating documentation or restructuring content to avoid broken links, which can impact SEO.</p></figcaption></figure>

Redirects are commonly used when you are migrating your documentation from one provider to another — like when you just moved docs to GitBook. Broken links can impact SEO so we recommend setting up redirects where needed.

In addition to [automatic redirects created by GitBook](#about-automatic-redirects), you can create a redirect from any path in your site’s domain.

## Managing redirects on your site

To get started, view your site’s dashboard in GitBook and open the **Settings** tab, then click **Domain & redirects**.

### Creating redirects

Click **Add redirect** to begin. Fill in the source path — i.e. the URL slug that you wish to redirect somewhere else — and the destination content you wish to link to. You can pick any [section](https://gitbook.com/docs/publishing-documentation/site-structure/site-sections), [variant](https://gitbook.com/docs/publishing-documentation/site-structure/variants), or [page](https://gitbook.com/docs/creating-content/content-structure/page) on to your site. Click **Add** to create the redirect.

If you want to add another redirect to the same page, you can toggle the **Add another redirect** option on before you hit **Add**. When you add your redirect, the modal will remain open with the destination content set to the previous selection so you can add another URL slug immediately.

### Editing redirects

To edit a redirect, press the **Edit** <picture><source srcset="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2F8pD8Y2BfBxCEZoi99Pnk%2Fedit%20-%20dark.svg?alt=media&#x26;token=89496678-7347-4845-8c98-ee8dd9bedaec" media="(prefers-color-scheme: dark)"><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FA3OfGjPkE5GnOQvN36jN%2Fedit.svg?alt=media&#x26;token=6f70239f-d889-4e64-9ec6-4801df47a48d" alt="The Edit icon in GitBook"></picture> icon next to it in the list. Update the redirect and hit **Save**.

To delete a redirect, press the **Delete redirect** button and confirm.

## About automatic redirects

Whenever pages are moved or renamed, their canonical URL changes with them. In order to keep your content accessible, GitBook automatically creates a [HTTP 307](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status/307) redirect from the old URL to the new one.

Every time a URL is loaded, GitBook resolves it through the following steps:

1. Site content is resolved to its canonical URL by following any of the automatically created redirects.
2. If the URL cannot be resolved, the URL is checked against [space-level redirects](https://gitbook.com/docs/getting-started/git-sync/content-configuration#redirects), defined in your repository's `.gitbook.yaml` file.
3. Finally, the URL is checked against site-level redirects, created via [the process above](#creating-redirects).
