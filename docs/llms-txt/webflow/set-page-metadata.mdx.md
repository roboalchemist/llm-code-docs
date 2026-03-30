# Source: https://developers.webflow.com/designer/set-page-metadata.mdx

***

title: Set page metadata
slug: set-page-metadata
description: Set the metadata of a page.
hidden: false
'og:title': Set page metadata
'og:description': Set the metadata of a page.
---------------------------------------------

## `page.setMetadata(parameters)`

Updates the metadata of a page, including SEO-related properties, OpenGraph settings, and search configurations. For more information on the information and properties, see all methods in the Managing Pages section of the API Reference.

### Syntax

```typescript
page.setMetadata(metadata: PageMetadata): void

type PageMetadata = {
  name: string;
  slug: string;
  title: string;
  description: string;
  isDraft: boolean;
  usesTitleAsOpenGraphTitle: boolean;
  openGraphTitle: string;
  usesDescriptionAsOpenGraphDescription: boolean;
  openGraphDescription: string;
  openGraphImage: string;
  isExcludedFromSearch: boolean;
  usesTitleAsSearchTitle: boolean;
  searchTitle: string;
  usesDescriptionAsSearchDescription: boolean;
  searchDescription: string;
  usesOpenGraphImageAsSearchImage: boolean;
  searchImage: string;
}
```

### Parameters

* **metadata**: *PageMetadata* - An object containing the page metadata properties:
  * **name**: *string* - The name of the page
  * **slug**: *string* - The URL-friendly identifier for the page
  * **title**: *string* - The page title
  * **description**: *string* - The page description
  * **isDraft**: *boolean* - Whether the page is in draft status
  * **usesTitleAsOpenGraphTitle**: *boolean* - Whether to use the page title as the OpenGraph title
  * **openGraphTitle**: *string* - Custom OpenGraph title
  * **usesDescriptionAsOpenGraphDescription**: *boolean* - Whether to use the page description as the OpenGraph description
  * **openGraphDescription**: *string* - Custom OpenGraph description
  * **openGraphImage**: *string* - URL of the OpenGraph image
  * **isExcludedFromSearch**: *boolean* - Whether to exclude the page from search results
  * **usesTitleAsSearchTitle**: *boolean* - Whether to use the page title as the search title
  * **searchTitle**: *string* - Custom search title
  * **usesDescriptionAsSearchDescription**: *boolean* - Whether to use the page description as the search description
  * **searchDescription**: *string* - Custom search description
  * **usesOpenGraphImageAsSearchImage**: *boolean* - Whether to use the OpenGraph image as the search image
  * **searchImage**: *string* - Custom search image URL

### Returns

**Promise\<`null`>**

A promise that resolves to `null`.

### Example

```typescript
// Update page metadata
page.setMetadata({
  name: "Product Features",
  slug: "product-features",
  title: "Awesome Product Features",
  description: "Discover our product's amazing features",
  isDraft: false,
  usesTitleAsOpenGraphTitle: true,
  openGraphTitle: "",
  usesDescriptionAsOpenGraphDescription: true,
  openGraphDescription: "",
  openGraphImage: "https://example.com/og-image.jpg",
  isExcludedFromSearch: false,
  usesTitleAsSearchTitle: true,
  searchTitle: "",
  usesDescriptionAsSearchDescription: true,
  searchDescription: "",
  usesOpenGraphImageAsSearchImage: true,
  searchImage: ""
});
```

<div>
  <a href="https://webflow.com/oauth/authorize?response_type=code&client_id=19511de1ec410f9228d8dcbc9420e67916dea80d86d18f0c9a533eb475ea0f62">
    Try this example
  </a>
</div>

### Designer Ability

| Designer Ability      | Locale | Branch | Workflow | Sitemode |
| :-------------------- | :----- | :----- | :------- | :------- |
| canManagePageSettings | Any    | Any    | Any      | Any      |
