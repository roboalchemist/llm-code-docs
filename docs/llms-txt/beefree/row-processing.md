# Source: https://docs.beefree.io/beefree-sdk/apis/content-services-api/row-processing.md

# Row Processing

{% hint style="info" %}
Row Processing endpoints are part of the [Content Services API](https://docs.beefree.io/beefree-sdk/apis/content-services-api). The Content Services API is available on [Beefree SDK plans that are Essentials or above](https://developers.beefree.io/pricing-plans).
{% endhint %}

## Overview

The Rows endpoints help you keep templates consistent and avoid redundancy. Use them to list [saved rows](https://docs.beefree.io/beefree-sdk/rows/reusable-content/create/save), apply updates across multiple templates, or retrieve [synced rows](#merge-2).

### Available Collection Values for Row Processing Endpoints

The following table lists the collection values available in this category of endpoints, and their corresponding collection options.

Prior to referencing the table, the following example shows how you can replace the **{collection}** placeholder.

#### How to Replace the {collection} Placeholder

The following example URL has a **{collection}** placeholder. This placeholder needs to be filled in with a **Collection Option** prior to making an API call.

`https://api.getbee.io/v1/{collection}/merge-rows`

As an example, if you'd like to merge rows for emails using this endpoint, replace **{collection}** with **message**.

The final URL to make the API call will be:

`https://api.getbee.io/v1/message/merge-rows`

The following table provides a comprehensive reference of all available options.

| Resource       | Collection Options                                                 |
| -------------- | ------------------------------------------------------------------ |
| `/merge`       | <ul><li><code>/message</code></li><li><code>/page</code></li></ul> |
| `/merge-rows`  | <ul><li><code>/message</code></li><li><code>/page</code></li></ul> |
| `/synced-rows` | <ul><li><code>/message</code></li><li><code>/page</code></li></ul> |
| `/merge-index` | <ul><li><code>/message</code></li><li><code>/page</code></li></ul> |

## Merge <a href="#merge" id="merge"></a>

The `merge` method allows you to update a row across multiple templates. Specifically, it enables the host application to modify an element within an existing JSON document. This means you can implement a feature that updates templates in the background—without requiring any action from your users. It's ideal for merging shared content ([saved rows](https://docs.beefree.io/beefree-sdk/rows/reusable-content/create/save)) into templates that use it—for example, updating the same footer across 30 different email or page templates.

{% hint style="info" %}
**Important:** `collection` is a placeholder within the URL. This placeholder can be replaces with any of the `collection` options available for the Row Processing resource. Reference the [Row Processing Resource and Collection Options table](https://docs.beefree.io/beefree-sdk/apis/content-services-api/..#row-processing) for a list of available option.
{% endhint %}

**URL:** `https://api.getbee.io/v1/{collection}/merge`

{% openapi src="<https://806400411-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F8c7XIQHfAtM23Dp3ozIC%2Fuploads%2FFA32TtishOt1zMRnLqON%2Fmerge_endpoint.yaml?alt=media&token=e11047bd-52db-43ba-885f-20eb08f3d4f9>" path="/v1/{collection}/merge" method="post" %}
[merge\_endpoint.yaml](https://806400411-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F8c7XIQHfAtM23Dp3ozIC%2Fuploads%2FFA32TtishOt1zMRnLqON%2Fmerge_endpoint.yaml?alt=media\&token=e11047bd-52db-43ba-885f-20eb08f3d4f9)
{% endopenapi %}

## Merge Rows <a href="#merge" id="merge"></a>

**URL:** `https://api.getbee.io/v1/{collection}/merge-rows`

{% openapi src="<https://806400411-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F8c7XIQHfAtM23Dp3ozIC%2Fuploads%2FO7XIH833WreYXAXzYGOA%2Fmerge_rows_endpoint.yaml?alt=media&token=e5aa840d-5710-4854-a581-adc16f4303e2>" path="/v1/{collection}/merge-rows" method="post" %}
[merge\_rows\_endpoint.yaml](https://806400411-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F8c7XIQHfAtM23Dp3ozIC%2Fuploads%2FO7XIH833WreYXAXzYGOA%2Fmerge_rows_endpoint.yaml?alt=media\&token=e5aa840d-5710-4854-a581-adc16f4303e2)
{% endopenapi %}

{% hint style="info" %}
When utilizing this feature, it's important to consider adding a handle to the metadata. This handle serves a crucial role in functions such as `onDeleteRow` and `onEditRow`. In our provided example, we use a handle named `guid`. However, users have the flexibility to choose their own handle name according to their preferences and requirements. When selecting a handle name, we recommend you choose something descriptive and meaningful for ease of identification and management within your workflow.
{% endhint %}

## Synced Rows <a href="#merge" id="merge"></a>

**URL:** `https://api.getbee.io/v1/{collection}/synced-rows`

What if a footer is shared by 10 messages and needs to be updated in all of them? The [Synced Rows](https://docs.beefree.io/beefree-sdk/rows/reusable-content/sync/implement-synced-rows) feature was created precisely to address the scenario of content that is shared across multiple emails, pages, or popups, and it is used in conjunction with the Content Services API.

{% openapi src="<https://806400411-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F8c7XIQHfAtM23Dp3ozIC%2Fuploads%2FE0VkdcfuvZbbmAFdQybV%2Fsynced_rows_endpoint.yaml?alt=media&token=b7b2da65-0055-45ce-a888-44ce835e56e4>" path="/v1/{collection}/synced-rows" method="post" %}
[synced\_rows\_endpoint.yaml](https://806400411-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F8c7XIQHfAtM23Dp3ozIC%2Fuploads%2FE0VkdcfuvZbbmAFdQybV%2Fsynced_rows_endpoint.yaml?alt=media\&token=b7b2da65-0055-45ce-a888-44ce835e56e4)
{% endopenapi %}

## Index <a href="#index" id="index"></a>

The `index` method in the Content Services API lets you retrieve a list of assets that include a specific saved row. This method is essential for determining which assets need to be updated using the `merge` method.

**Typical Use Cases**

* Updating shared headers or footers across multiple templates
* Modifying expiration dates in seasonal campaigns
* Applying price or link changes to reused promotional content
* Making any update to shared blocks without manually editing each message

Use the `index` method first to locate all impacted assets, then apply changes with the `merge` method to ensure content is updated consistently.

## Index

> Reference an array of metadata objects from a Beefree template in JSON format.

```json
{"openapi":"3.0.0","info":{"title":"Index","version":"1.0.0"},"servers":[{"url":"https://api.getbee.io","description":"Base URL for the API"}],"security":[{"bearerAuth":[]}],"components":{"securitySchemes":{"bearerAuth":{"type":"http","scheme":"bearer","bearerFormat":"Enter Dev Console API Key as Bearer token"}}},"paths":{"/v1/{collection}/merge/index":{"post":{"summary":"Index","description":"Reference an array of metadata objects from a Beefree template in JSON format.","parameters":[{"name":"collection","in":"path","required":true,"description":"The collection ID or name","schema":{"type":"string"}}],"requestBody":{"required":true,"description":"Request body for the endpoint","content":{"application/json":{"schema":{"type":"object","properties":{"source":{"type":"object","description":"An object field for source","properties":{"page":{"type":"object","description":"An object field for page","properties":{"body":{"type":"object","description":"An object field for body","properties":{"container":{"type":"object","description":"An object field for container","properties":{"style":{"type":"object","description":"An object field for style","properties":{"background-color":{"type":"string","description":"A string field for background-color"}}}}},"content":{"type":"object","description":"An object field for content","properties":{"computedStyle":{"type":"object","description":"An object field for computedStyle","properties":{"linkColor":{"type":"string","description":"A string field for linkColor"},"messageBackgroundColor":{"type":"string","description":"A string field for messageBackgroundColor"},"messageWidth":{"type":"string","description":"A string field for messageWidth"}}},"style":{"type":"object","description":"An object field for style","properties":{"color":{"type":"string","description":"A string field for color"},"font-family":{"type":"string","description":"A string field for font-family"}}}}},"type":{"type":"string","description":"A string field for type"},"webFonts":{"type":"array","description":"An array of objects for webFonts","items":{"type":"object","properties":{"name":{"type":"string","description":"A string field for name"},"fontFamily":{"type":"string","description":"A string field for fontFamily"},"url":{"type":"string","description":"A string field for url"}}}}}},"description":{"type":"string","description":"A string field for description"},"rows":{"type":"array","description":"An array of objects for rows","items":{"type":"object","properties":{"metadata":{"type":"object","description":"An object field for metadata","properties":{"name":{"type":"string","description":"A string field for name"},"guid":{"type":"string","description":"A string field for guid"}}},"columns":{"type":"array","description":"An array of objects for columns","items":{"type":"object","properties":{"grid-columns":{"type":"integer","description":"An integer field for grid-columns"},"modules":{"type":"array","description":"An array of objects for modules","items":{"type":"object","properties":{"descriptor":{"type":"object","description":"An object field for descriptor","properties":{"computedStyle":{"type":"object","description":"An object field for computedStyle","properties":{"class":{"type":"string","description":"A string field for class"},"width":{"type":"integer","description":"An integer field for width"}}},"image":{"type":"object","description":"An object field for image","properties":{"alt":{"type":"string","description":"A string field for alt"},"href":{"type":"string","description":"A string field for href"},"src":{"type":"string","description":"A string field for src"}}},"style":{"type":"object","description":"An object field for style","properties":{"padding-bottom":{"type":"string","description":"A string field for padding-bottom"},"padding-left":{"type":"string","description":"A string field for padding-left"},"padding-right":{"type":"string","description":"A string field for padding-right"},"padding-top":{"type":"string","description":"A string field for padding-top"},"width":{"type":"string","description":"A string field for width"}}}}},"locked":{"type":"integer","description":"An integer field for locked"},"type":{"type":"string","description":"A string field for type"}}}},"style":{"type":"object","description":"An object field for style","properties":{"background-color":{"type":"string","description":"A string field for background-color"},"border-bottom":{"type":"string","description":"A string field for border-bottom"},"border-left":{"type":"string","description":"A string field for border-left"},"border-right":{"type":"string","description":"A string field for border-right"},"border-top":{"type":"string","description":"A string field for border-top"},"padding-bottom":{"type":"string","description":"A string field for padding-bottom"},"padding-left":{"type":"string","description":"A string field for padding-left"},"padding-right":{"type":"string","description":"A string field for padding-right"},"padding-top":{"type":"string","description":"A string field for padding-top"}}}}}},"container":{"type":"object","description":"An object field for container","properties":{"style":{"type":"object","description":"An object field for style","properties":{"background-color":{"type":"string","description":"A string field for background-color"},"background-image":{"type":"string","description":"A string field for background-image"},"background-position":{"type":"string","description":"A string field for background-position"},"background-repeat":{"type":"string","description":"A string field for background-repeat"}}}}},"content":{"type":"object","description":"An object field for content","properties":{"computedStyle":{"type":"object","description":"An object field for computedStyle","properties":{"hideContentOnDesktop":{"type":"integer","description":"An integer field for hideContentOnDesktop"},"hideContentOnMobile":{"type":"integer","description":"An integer field for hideContentOnMobile"},"rowColStackOnMobile":{"type":"integer","description":"An integer field for rowColStackOnMobile"}}},"style":{"type":"object","description":"An object field for style","properties":{"background-color":{"type":"string","description":"A string field for background-color"},"background-image":{"type":"string","description":"A string field for background-image"},"background-position":{"type":"string","description":"A string field for background-position"},"background-repeat":{"type":"string","description":"A string field for background-repeat"},"color":{"type":"string","description":"A string field for color"},"width":{"type":"string","description":"A string field for width"}}}}},"locked":{"type":"integer","description":"An integer field for locked"},"type":{"type":"string","description":"A string field for type"}}}},"template":{"type":"object","description":"An object field for template","properties":{"name":{"type":"string","description":"A string field for name"},"type":{"type":"string","description":"A string field for type"},"version":{"type":"string","description":"A string field for version"}}},"title":{"type":"string","description":"A string field for title"}}}}}}}}}},"responses":{"200":{"description":"Successful response","content":{"application/json":{"schema":{"type":"object"}}}},"400":{"description":"Bad request"},"401":{"description":"Unauthorized"},"403":{"description":"Forbidden"},"500":{"description":"Internal Server Error"}}}}}}
```
