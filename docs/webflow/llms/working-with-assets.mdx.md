# Source: https://developers.webflow.com/data/docs/working-with-assets.mdx

***

title: Working with Assets
slug: /data/docs/working-with-assets
description: How use the Webflow Data API to work with Assets
hidden: false
layout: overview
max-toc-depth: 2
'og:title': Working with Assets in the Webflow Data API
'og:description': How use the Webflow Data API to work with Assets
------------------------------------------------------------------

{/* Overview Section */}

Webflow's asset APIs enable apps to upload and manage a site's assets. Learn more about assets in Webflow in the [support documentation.](https://help.webflow.com/hc/en-us/articles/33961269934227-Assets-panel#supported-file-types)

{/* Why is this specifically helpful for developers/programmatically */}

These APIs enable developers to create integrations that sync with external file management systems like [Digital Asset Managers (DAMs)](https://www.bynder.com/en/what-is-digital-asset-management/). Keeping these systems in sync ensures that site designers and content managers have the assets they need when working in Webflow.

<Note title="Important">
  Files you upload to the assets panel aren't restricted — that is, they're
  publicly available and discoverable, but won’t necessarily be discovered or
  indexed by search engines if the file isn’t on a publicly viewable webpage
  or linked elsewhere. [Learn more about asset privacy in Webflow.](https://help.webflow.com/hc/en-us/articles/33961281837843)
</Note>

## FAQs

<Accordion title="Which file types are supported?">
  {/* <!-- vale off --> */}

  <Tabs>
    <Tab title="Images">
      * PNG
      * JPEG and JPG
      * GIF
      * SVG
      * WebP
      * AVIF
    </Tab>

    <Tab title="Documents">
      * PDF
      * DOC and DOCX
      * XLS and XLSX
      * PPT and PPTX
      * TXT
      * CSV
      * ODT
      * ODS
      * ODP
    </Tab>

    <Tab title="Lottie">
      * JSON (only Lottie type)
      * dotLottie
    </Tab>
  </Tabs>

  {/* <!-- vale on --> */}
</Accordion>

<Accordion title="Are there size limits for assets?">
  Yes, uploaded assets must adhere to specific size limitations:

  * Images must not exceed 4MB
  * Documents are capped at 10MB
</Accordion>

<Accordion title="Why do I need to include a file hash for asset uploads?">
  When uploading a file, Webflow requires an [MD5 hash](https://en.wikipedia.org/wiki/MD5) generated from the contents of the file to ensure data integrity and manage duplicate assets.

  {/* <!-- vale off --> */}

  ### What is a cryptographic hash?

  > A cryptographic hash, also often referred to as a “digest”, “fingerprint” or “signature”, is an almost perfectly unique string of characters that is generated from a separate piece of input text. --[boot.dev](https://blog.boot.dev/cryptography/how-sha-2-works-step-by-step-sha-256/)

  A cryptographic hash is the result of a hashing algorithm, which deterministically converts input data into an output of fixed length, regardless of input size.

  {/* <!-- vale on --> */}

  ### What are cryptographic hashes used for?

  Hashes serve a range of purposes, from verifying data integrity and enabling fast lookups in databases, to efficiently identifying duplicates.
  Let's break down what that looks like when uploading a file to Webflow and including an [MD5 hash](https://www.okta.com/identity-101/md5/):

  <Steps>
    ### Generate the file hash

    Before uploading, use the MD5 hashing algorithm to convert the binary contents of your file into a 128-bit hash. This hash will serve as the `fileHash` value.

    ### Provide the hash on upload

    When creating a new asset in Webflow, include this generated `fileHash` with a request to the [Create Asset Metadata](https://developers.webflow.com/data/reference/assets/assets/create) endpoint.

    ### Webflow uses the hash for de-duplication

    Webflow uses the `fileHash` as a unique identifier to prevent duplicate uploads. If a hash matches an existing file’s hash, Webflow avoids redundant storage, optimizing resources.

    ### Lookup and verification

    Webflow may use the `fileHash` as a lookup key to retrieve or verify file data, ensuring consistency across operations.
  </Steps>
</Accordion>

## What you'll build

In this tutorial, you'll build an example script that:

* Creates asset folders on a site
* Uploads a new image to an Webflow with a [MD5 hash](#cryptographic-hashing)
* Organizes the image within a site's asset folders

## Prerequisites

* A Webflow site in your development Workspace
* A Webflow App or site token with the following scopes: `assets:read`, `assets:write`
* Some knowledge of Node.js or Python

<br />

<iframe src="https://assets-data-api-guide.netlify.app/" width="100%" allow="clipboard-write; clipboard-read" />

## Conclusion

{/* Review what was accomplished, direct users to next steps that can be helpful - or examples */}

Congratulations! You've just programmatically created asset folders and uploaded assets to a Webflow site. These assets can now be organized and used across the site by designers and editors of Webflow projects.

Looking for more things to try with the API? Check out:

* [Working with Custom Code](/data/docs/custom-code)
* [Working with the CMS](/data/docs/working-with-the-cms)
* [Working with Webhooks](/data/docs/working-with-webhooks)
