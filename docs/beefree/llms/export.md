# Source: https://docs.beefree.io/beefree-sdk/apis/content-services-api/export.md

# Export

{% hint style="info" %}
Export endpoints are part of the [Content Services API](https://docs.beefree.io/beefree-sdk/apis/content-services-api). The Content Services API is available on [Beefree SDK plans that are Essentials or above](https://developers.beefree.io/pricing-plans).
{% endhint %}

## Overview

The Export category is one of the most common uses of the Content Services API. After creating a design in the no-code builder, end users often need to export and share it. These endpoints let you offer multiple export options—including HTML, plain text, PDF, and image formats—so your users can easily distribute their finished designs.

### Available Collection Values for Export Endpoints

The following table lists the collection values available in this category of endpoints, and their corresponding collection options.

Prior to referencing the table, the following example shows how you can replace the **{collection}** placeholder based on the type of content you'd like to export.

#### How to Replace the {collection} Placeholder

The following example URL has a **{collection}** placeholder. This placeholder needs to be filled in with a **Collection Option** prior to making an API call.

`https://api.getbee.io/v1/{collection}/html`

As an example, if you'd like to export an email's HTML using this endpoint, replace **{collection}** with **message**.

The final URL to make the API call will be:

`https://api.getbee.io/v1/message/html`

The following table provides a comprehensive reference of all available options based on what you'd like to export.

| Resource      | Collection Options                                                                                                       |
| ------------- | ------------------------------------------------------------------------------------------------------------------------ |
| `/html`       | <ul><li><code>/message</code></li><li><code>/page</code></li><li><code>/popup</code></li><li><code>/amp</code></li></ul> |
| `/plain-text` | <ul><li><code>/message</code></li></ul>                                                                                  |
| `/pdf`        | <ul><li><code>/message</code></li><li><code>/page</code></li></ul>                                                       |
| `/image`      | <ul><li><code>/message</code></li><li><code>/page</code></li></ul>                                                       |

## HTML <a href="#html" id="html"></a>

**URL:** `https://api.getbee.io/v1/{collection}/html`

This endpoint allows you to retrieve the full or partial HTML output of a template (email, page, or popup).

{% hint style="info" %}
**Important:** `collection` is a placeholder within the URL. This placeholder can be replaced with any of the `collection` options available for the HTML resource. Reference the [Export Resource and Collection Options table](https://docs.beefree.io/beefree-sdk/apis/content-services-api/..#export) for a list of available option.
{% endhint %}

#### How It Works

To generate HTML from a template's JSON:

1. Capture or store the latest JSON output from the builder using [callbacks](https://docs.beefree.io/beefree-sdk/getting-started/readme/installation/methods-and-events) such as `onChange` or `autosave`.
2. Send this JSON payload to the HTML endpoint.
3. Receive the HTML string as the response.

#### Required Request Payload

```json
{
  "page": {
    "body": { ... },
    ...
  }
}
```

* `page` (object, required): The full template structure in Beefree JSON format. This is the same structure returned by the builder or captured from its callbacks.

#### Notes

* This endpoint bypasses the need for the `onSave` callback and can be used at any time post-editing.
* Partial HTML rendering is also supported for specific components or modules (if required by your use case).
* The output HTML reflects the current rendering engine used by Beefree, ensuring up-to-date compatibility.

{% openapi src="<https://806400411-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F8c7XIQHfAtM23Dp3ozIC%2Fuploads%2Fa3lSukpFEcbPYPVzjVIz%2Fhtml_endpoint.yaml?alt=media&token=f7b58600-763b-45ab-98c8-1877a24bd4c0>" path="/v1/{collection}/html" method="post" %}
[html\_endpoint.yaml](https://806400411-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F8c7XIQHfAtM23Dp3ozIC%2Fuploads%2Fa3lSukpFEcbPYPVzjVIz%2Fhtml_endpoint.yaml?alt=media\&token=f7b58600-763b-45ab-98c8-1877a24bd4c0)
{% endopenapi %}

## Plain Text

**URL:** `https://api.getbee.io/v1/{collection}/html`

This endpoint allows you to retrieve the plain text version of an email.

{% hint style="info" %}
**Important:** `collection` is a placeholder within the URL. This placeholder can be replaces with any of the `collection` options available for the Plain Text resource. Reference the [Export Resource and Collection Options table](https://docs.beefree.io/beefree-sdk/apis/content-services-api/..#export) for a list of available option.
{% endhint %}

#### How It Works

To generate plain text from a template's JSON:

1. Capture or store the latest JSON output from the builder using [callbacks](https://docs.beefree.io/beefree-sdk/getting-started/readme/installation/methods-and-events) such as `onChange` or `autosave`.
2. Send this JSON payload to the `/plain-text` endpoint.
3. Receive the plain text as the response.

{% openapi src="<https://806400411-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F8c7XIQHfAtM23Dp3ozIC%2Fuploads%2FEDXE2wtfc77B5cWtzADx%2Fplain_text_endpoint.yaml?alt=media&token=4639676b-5852-4b66-a690-470489969e67>" path="/v1/{collection}/plain-text" method="post" %}
[plain\_text\_endpoint.yaml](https://806400411-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F8c7XIQHfAtM23Dp3ozIC%2Fuploads%2FEDXE2wtfc77B5cWtzADx%2Fplain_text_endpoint.yaml?alt=media\&token=4639676b-5852-4b66-a690-470489969e67)
{% endopenapi %}

## PDF <a href="#pdf" id="pdf"></a>

**URL:** `https://api.getbee.io/v1/{collection}/pdf`

You can generate a PDF file from valid HTML content using the dedicated PDF generation endpoint. This operation requires a JSON payload with specific fields to configure the output.

{% hint style="info" %}
**Important:** `collection` is a placeholder within the URL. This placeholder can be replaces with any of the `collection` options available for the PDF resource. Reference the [Export Resource and Collection Options table](https://docs.beefree.io/beefree-sdk/apis/content-services-api/..#export) for a list of available option.
{% endhint %}

#### Required Request Payload

```json
{
  "page_size": "Full",
  "page_orientation": "landscape",
  "html": "<!DOCTYPE html>...</html>"
}
```

**Field Descriptions**

* **`html`** (string, required): The full HTML content to convert to a PDF. You can obtain the HTML output of a template by calling the [`/html` endpoint](#html) and copying its response into this field.
* **`page_orientation`** (string, required): Sets the orientation of the generated PDF pages.\
  Accepted values:
  * `"portrait"`: vertical layout.
  * `"landscape"`: horizontal layout.
* **`page_size`** (string, required): Defines the dimensions of the PDF output.\
  Accepted values:
  * `"Letter"`: US Letter format.
  * `"A4"`: A4 paper size.
  * `"A3"`: A3 paper size.
  * `"Full"`: a single continuous page with fixed width (900px) and height determined proportionally to the content.

{% hint style="warning" %}
When using `"Letter"`, `"A4"`, or `"A3"`, the content is automatically split across multiple pages.\
Using `"Full"` produces a single, unpaginated scrollable PDF.
{% endhint %}

#### Steps to generate a PDF

To generate a PDF from a template:

1. Call the `/html` endpoint to retrieve the template's HTML.
2. Insert that HTML into the `"html"` field of the request payload.
3. Set your preferred `"page_orientation"` and `"page_size"`.
4. Send the payload to the PDF generation endpoint.

{% openapi src="<https://806400411-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F8c7XIQHfAtM23Dp3ozIC%2Fuploads%2FnlGD61dWKnS9Kptefein%2Fpdf_endpoint.yaml?alt=media&token=7fb49d6c-8b0a-4e25-ab88-6526989d3c97>" path="/v1/{collection}/pdf" method="post" %}
[pdf\_endpoint.yaml](https://806400411-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F8c7XIQHfAtM23Dp3ozIC%2Fuploads%2FnlGD61dWKnS9Kptefein%2Fpdf_endpoint.yaml?alt=media\&token=7fb49d6c-8b0a-4e25-ab88-6526989d3c97)
{% endopenapi %}

{% hint style="info" %}
**Note:** The response is a JSON string that will contain the URL of the temporary location of the PDF document. The file is available for 24 hours.
{% endhint %}

#### Sample code: Exporting PDFs prototype <a href="#image" id="image"></a>

Curious to see what an implementation of the PDF export API could look like? [This example](https://github.com/BeefreeSDK/beefree-sdk-examples/tree/main/template-export-pdf-example) demonstrates advanced PDF export functionality for the Beefree SDK using a modern React + TypeScript architecture. It showcases how to export templates as high-quality PDFs with comprehensive export options, progress tracking, and export history management.

{% embed url="<https://github.com/BeefreeSDK/beefree-sdk-examples/tree/main/template-export-pdf-example>" %}

## Image <a href="#image" id="image"></a>

**URL:** `https://api.getbee.io/v1/{collection}/image`

This endpoint allows you to generate an image file (for example, PNG) from a template's HTML. You can control the image output by specifying the dimensions.

{% hint style="info" %}
**Important:** `collection` is a placeholder within the URL. This placeholder can be replaces with any of the `collection` options available for the Image resource. Reference the [Export Resource and Collection Options table](https://docs.beefree.io/beefree-sdk/apis/content-services-api/..#export) for a list of available option.
{% endhint %}

#### Required Request Payload

```json
{
  "html": "<!DOCTYPE html>...</html>",
  "width": 800,
  "height": 600
}
```

{% hint style="info" %}
Note: As an alternative to providing `width` and `height`, you can also provide `size`.
{% endhint %}

#### Rendering

The HTML is rendered using a fixed-size browser window to simulate a real-world preview. Here are the key rendering parameters:

* **Window Size**: `1920 x 1080` pixels (used for clipping/screenshot area)
* **Default Viewports**:
  * Mobile: `320px` width
  * Desktop: `1024px` width
* **Clipping Region**: defaults to `1920 x 1080` pixels
* **Scale Factor**: Automatically calculated to match viewport and clipping dimensions.

You may override the clipping size if your layout requires a custom viewport. If your content exceeds the clipping area, it may be cropped. For improved results, using auto height with the size parameter is recommended.

#### Steps to perform an Image API call

1. Use the [`/html` endpoint](#html) to generate the HTML version of your template.
2. Set the `html` field in your image request payload to the HTML generated.
3. Provide a `width` and `height` values, or a `size` value.
4. Send the payload to the image endpoint.

| Name         | Type    | Description                                                                                                                                                                                                                                                                                                                        |
| ------------ | ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| html\*       | String  | A Beefree HTML message.                                                                                                                                                                                                                                                                                                            |
| size         | String  | Use “size” instead of “width” and “height” when you only know the width and want the height automatically calculated. **Required** if width and height are not defined.                                                                                                                                                            |
| width        | Integer | The image width in pixels. **Required** if size is not defined.                                                                                                                                                                                                                                                                    |
| height       | Integer | The image height in pixels. Default applies a proportional value based on the given width, keeping the image aspect ratio. When the value is not proportional to the given width, either will occur: If it’s higher, the proportional value applies, or, if it’s lower, the image is cropped. **Required** if size is not defined. |
| file\_type\* | String  | Accepts jpg or png.                                                                                                                                                                                                                                                                                                                |

## Transform HTML into an Image

> Use this endpoint to transform a design's HTML into an Image, which can be used for thumbnails and  similar purposes. Compatible with Email and Page builder.

```json
{"openapi":"3.0.0","info":{"title":"Transform HTML into an Image","version":"1.0.0"},"servers":[{"url":"https://api.getbee.io","description":"Base URL for the API"}],"security":[{"bearerAuth":[]}],"components":{"securitySchemes":{"bearerAuth":{"type":"http","scheme":"bearer","bearerFormat":"Enter Dev Console API Key as Bearer token"}}},"paths":{"/v1/{collection}/image":{"post":{"summary":"Transform HTML into an Image","description":"Use this endpoint to transform a design's HTML into an Image, which can be used for thumbnails and  similar purposes. Compatible with Email and Page builder.","parameters":[{"name":"collection","in":"path","required":true,"description":"The collection ID or name","schema":{"type":"string"}}],"requestBody":{"required":true,"description":"Request body for the endpoint","content":{"application/json":{"schema":{"type":"object","properties":{"file_type":{"type":"string","description":"A string field for file_type"},"size":{"type":"string","description":"A string field for size"},"html":{"type":"string","description":"A string field for html"}},"required":["file_type","size","html"]}}}},"responses":{"200":{"description":"Successful response","content":{"image/png":{"schema":{"type":"string","format":"binary"},"description":"The response is binary data representing a PNG image. \nYou need to write code to convert the binary response to a PNG image file in your application.\n"}}},"400":{"description":"Bad request"},"401":{"description":"Unauthorized"},"403":{"description":"Forbidden"},"500":{"description":"Internal Server Error"}}}}}}
```
