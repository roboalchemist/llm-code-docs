# Source: https://www.nutrient.io/guides/dws-processor/getting-started/postman-collection/

---
description: Use Nutrient DWS Processor API’s official Postman collection to test Processor API requests with preconfigured examples and hosted sample files.
title: Postman collection for Nutrient DWS Processor API
image: https://cdn.prod.website-files.com/65fdb7696055f07a05048833/6717c1324bc009b855df63a7_Nutrient.jpg
---

# Postman collection

Copy page 

[ Copy pageCopy page as Markdown for LLMs ](#) [ View as MarkdownView this page as plain text ](#) [ Open with ChatGPTExplain the page with ChatGPT ](#) [ Open with ClaudeExplain the page with Claude ](#) [ Open with GrokExplain the page with Grok ](#) 

[Postman(opens in a new tab)](https://www.postman.com/) is a cross-platform graphical user interface (GUI) application for interacting with APIs. You can use our official [Postman collection(opens in a new tab)](https://www.postman.com/nutrient-dws-api/nutrient-dws-api/overview) to get started with Nutrient DWS Processor API with the click of a button.

Use this guide when you want the official Postman collection for Nutrient Processor API, need the fastest path from API key to a working request, or want to explore multiple Processor API task endpoints before writing integration code.

If you need broader DWS context while testing requests, continue to the [Processor API overview](https://www.nutrient.io/api/processor-api/), the [REST API reference](https://www.nutrient.io/api/reference/public/) for endpoint documentation, the [dashboard getting-started guide](https://www.nutrient.io/guides/dws-processor/getting-started/), or [Processor API pricing](https://www.nutrient.io/api/pricing/processor-api/).

Alternatively, you can [download the collection as a zip file](https://www.nutrient.io/assets/guides/dws-processor/dws-processor-api-postman-1de21c03234faf2e4a3d4762f4606913.zip) to import it locally into Postman.

## [ ](#get-started) Get started 

1. Create an account in [Nutrient DWS API dashboard(opens in a new tab)](https://dashboard.nutrient.io/sign%5Fup/?product=processor) and receive 200 free credits to start testing.
2. In Postman, create a `variable` named `DWS_PROCESSOR_API_KEY` and paste your key as its value.  
![Screen capture of the Postman window with the Variables section open](https://www.nutrient.io/_astro/variable.CFPobznF_1OzH6D.png)
3. In the **Authorization** tab, set the type to **Bearer Token** and enter `{{DWS_PROCESSOR_API_KEY}}` as the token.  
![Screen capture of the Postman window with the Authorization section open](https://www.nutrient.io/_astro/auth.9E8m_Ld4_163Mpb.png)  
    
Make sure each request includes the following header: `Authorization: Bearer {{DWS_PROCESSOR_API_KEY}}`. For more information, refer to the [variables in Postman(opens in a new tab)](https://learning.postman.com/docs/sending-requests/variables/variables/) guide.
4. Choose a request and click **Send** to get started.  
> We include example files with the collection so that you can try different examples right away. All files are already hosted and accessible via public URLs.  
![Screenshot of the Postman interface with a merge request example selected and the rendered PDF preview displayed in the response panel](https://www.nutrient.io/_astro/result.DgOQ4NWe_2vkDUQ.png)

## [ ](#key-features-and-tools) Key features and tools 

### [ ](#pdf-editing-tools) PDF editing tools 

* [Merge PDFs(opens in a new tab)](https://www.postman.com/nutrient-dws-api/nutrient-dws-api/request/edvzwp4/merge?tab=body)
* [Split PDFs(opens in a new tab)](https://www.postman.com/nutrient-dws-api/nutrient-dws-api/request/am144rs/split?tab=body)
* [Delete pages(opens in a new tab)](https://www.postman.com/nutrient-dws-api/nutrient-dws-api/request/0u4d2wt/delete?tab=body)
* [Flatten PDFs(opens in a new tab)](https://www.postman.com/nutrient-dws-api/nutrient-dws-api/request/0ip4ydp/flatten?tab=body)
* [Duplicate pages(opens in a new tab)](https://www.postman.com/nutrient-dws-api/nutrient-dws-api/request/07ea627/duplicate?tab=body)

### [ ](#ocr-operations) OCR operations 

* [Basic OCR(opens in a new tab)](https://www.postman.com/nutrient-dws-api/nutrient-dws-api/request/9x0zszy/basic?tab=body)
* [Merge and OCR combined workflows(opens in a new tab)](https://www.postman.com/nutrient-dws-api/nutrient-dws-api/request/whrrc16/merge-and-ocr?tab=body)

### [ ](#watermarking) Watermarking 

* [Text and image watermarking(opens in a new tab)](https://www.postman.com/nutrient-dws-api/nutrient-dws-api/request/0crycw8/text-watermark?tab=body)
* [Multiple overlay support(opens in a new tab)](https://www.postman.com/nutrient-dws-api/nutrient-dws-api/request/cur65dl/multiple-watermarks?tab=body)

### [ ](#file-conversion) File conversion 

* [HTML to PDF(opens in a new tab)](https://www.postman.com/nutrient-dws-api/nutrient-dws-api/request/yg94vz9/html-to-pdf-basic?tab=body)
* [Office to PDF (Word, Excel, PowerPoint)(opens in a new tab)](https://www.postman.com/nutrient-dws-api/nutrient-dws-api/request/a6wda5f/docx-to-pdf?tab=body)
* [Image to PDF(opens in a new tab)](https://www.postman.com/nutrient-dws-api/nutrient-dws-api/request/nfs2lwj/png-to-pdf?tab=body)
* [PDF to image(opens in a new tab)](https://www.postman.com/nutrient-dws-api/nutrient-dws-api/request/y1eu1x8/pdf-to-png?tab=body)
* [Office to image(opens in a new tab)](https://www.postman.com/nutrient-dws-api/nutrient-dws-api/request/2qy3fs1/office-to-png?tab=body)
* [HTML to image(opens in a new tab)](https://www.postman.com/nutrient-dws-api/nutrient-dws-api/request/4n67ig0/html-to-png?tab=body)

[Sign up and get started today(opens in a new tab)](https://dashboard.nutrient.io/sign%5Fup/?product=processor)!

---

### Was this helpful?

YES 

NO 

### Help us improve

0 / 2000 characters

Cancel Send 

### Thank you for your feedback!

### Something went wrong. Please try again or let us know.

Try Again [Contact Us](https://www.nutrient.io/company/contact/) 

---

 On this page 

## On this page

ASK AI 

```json
{
  "@context": "https://schema.org",
  "@type": "TechArticle",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://www.nutrient.io/guides/dws-processor/getting-started/postman-collection/"
  },
  "headline": "Postman collection",
  "description": "Use Nutrient DWS Processor API’s official Postman collection to test Processor API requests with preconfigured examples and hosted sample files.",
  "inLanguage": "en-US",
  "articleSection": "Getting Started",
  "wordCount": 442,
  "publisher": {
    "@type": "Organization",
    "name": "Nutrient",
    "logo": {
      "@type": "ImageObject",
      "url": "https://www.nutrient.io/_astro/nutrient-logo.CJxiofUP_19DKCs.svg"
    },
    "sameAs": [
      "https://www.nutrient.io/company/about",
      "https://www.linkedin.com/company/nutrientdocs",
      "https://www.facebook.com/nutrientdocs/",
      "https://x.com/nutrientdocs"
    ]
  },
  "author": {
    "@type": "Organization",
    "name": "Nutrient Documentation Team"
  }
}
```
