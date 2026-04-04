# Source: https://gitbook.com/docs/documentation/ja-gitbook-documentation/creating-content/blocks/heading.md

# Source: https://gitbook.com/docs/documentation/zh/creating-content/blocks/heading.md

# Source: https://gitbook.com/docs/documentation/fr/creating-content/blocks/heading.md

# Source: https://gitbook.com/docs/creating-content/blocks/heading.md

# Headings

Headings help give your documents structure — and using keywords in headings will also help search engines understand that structure, which can help your page rank higher in search results.

GitBook offers three levels of headings. Heading levels 1 (H1) and 2 (H2) will appear in the [page outline](https://gitbook.com/docs/resources/gitbook-ui#page-outline).

### Anchor links

When you add a heading to a page, it creates an anchor link. You can then link directly to these specific sections, to point people to relevant information.

#### Link to an anchor

You can see anchor links in public content, or private content in read-only mode, by hovering over the title and clicking the `#` that appears next to it. This will update the URL in your browser’s top bar, so you can copy it to use elsewhere.

If you want to link to a particular anchor from a page within your GitBook space, you can use a [relative link](https://gitbook.com/docs/formatting/inline#relative-links), which will update if you change the heading to prevent the link from breaking.

#### Edit an anchor

By default, the anchor link will be identical to the text in your header. If you plan to link to that URL outside of GitBook, changing the header in future will break the anchor link. The link will then take visitors to the top of the page, rather than the anchor location.

To avoid this, you can manually set the anchor link by opening the **Options menu** <picture><source srcset="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FjYRg42UtM4u1pHmJl4Ln%2Fdrag%20-%20dark.svg?alt=media&#x26;token=4c219b2b-37d2-449e-9130-19b6ba3d38d2" media="(prefers-color-scheme: dark)"><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FaS1QvPIBVYwhpFTGcPBN%2Foptions-menu.svg?alt=media&#x26;token=3ee40bbf-f4fb-41fa-aa30-306b559cbe88" alt="The Options menu icon in GitBook"></picture> for the header, then choosing **Edit anchor**. You can then enter the anchor link you wish to use — this will remain the anchor even if you change the header itself.

### Representation in Markdown

GitBook generates SEO optimized pages, meaning page titles in GitBook are automatically represented in markdown as a first level heading:

```markdown
# I'm a page title
```

This means that if you [sync your content with Git](https://gitbook.com/docs/getting-started/git-sync), page headers added through the editor will be represented as one level lower:

{% code overflow="wrap" %}

```markdown
## My heading 1
### My heading 2
#### My heading 3
```

{% endcode %}

### Heading examples <a href="#example-of-a-heading" id="example-of-a-heading"></a>

## My heading 1

### My heading 2

#### My heading 3
