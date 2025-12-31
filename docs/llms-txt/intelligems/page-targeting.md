# Source: https://docs.intelligems.io/general-features/targeting/page-targeting.md

# Page Targeting

## What is Intelligems Page Targeting?

By default, all pages on your site are included in a test. Intelligems page targeting allows you to limit your test to specific pages of your website.

## How does Intelligems Page Targeting work?

When you set up page targeting, site visitors will only be included in the test when they navigate to a page whose URL is included in the page targeting criteria. If a site visitor is on a page that is not included in the page targeting, they will be excluded from the test until they navigate to an included page.

Once a site visitor visits a targeted page, they will be assigned to a test group and remain in that test group for the remainder of the test, even if they navigate to pages that are not included in page targeting.

That said, modifications, such as Onsite Edits or Template Redirects, will only execute on the pages specified in your page targeting criteria. Visitors in your test will not see the modifications when they navigate to non-targeted pages.

## What about Query Parameters?

We match targeting based on the content **after your store URL** and **before any query parameters**. Because of this, you should not include the ? or any query parameters in your page targeting criteria. See below for an image further illustrating this:

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-7241feb90a87335d4c0d021e1fc5898a575bf667%2FScreenshot%202025-10-17%20at%201.53.32%E2%80%AFPM.png?alt=media" alt=""><figcaption></figcaption></figure>

### Examples:

* `https://ovenspring-cookware.myshopify.com/collections`
* `https://ovenspring-cookware.com/collections`
* `https://ovenspring-cookware.com/collections?utm_source=facebook`

will all correctly match the condition:

URL Path equals `/collections`

Because we match targeting based on the content after your store URL, you cannot set up page targeting for different domains simply using the URL. This means:

* `https://ovenspring-cookware.myshopify.com`
* `https://ovenspring-cookware.myshopify.fr`

will both correctly match your homepage. It is possible to target different domains using Custom JavaScript targeting.

## What about URLs with Trailing Slashes?

Similar to Shopify's routing rules, Intelligems will not evaluate a trailing slash at the end of a URL, for example:

`https://example.com/collections/`

will be evaluated the same as

`https://example.com/collections` (no trailing slash).

## What types of tests can I use Intelligems Page Targeting for?

Page targeting is available only for Content Tests that are created using Onsite Edits, as a Template Test or as an Advanced Test. Page Targeting is not available for Theme Tests, Split URL Tests, Shipping Tests or Price Tests. Split URL Test analytics already include only visitors who reached one of the redirect pages.

## How does Page Targeting impact experiment analytics?

Experiment analytics for experiments that use page targeting show visitors who were exposed to the test (that is, they reached a targeted page while the experiment was live). Any order made by these visitors while the experiment was live (but after the visitor entered it) is attributed to the experiment, even if the visitor did not add to cart on a targeted page.

## Examples of Intelligems Page Targeting

### **Including traffic on a specific product page**

You can select a single page to target in your test.

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-d2048dcebbb08c95545f4c67b39cac2a80257a6f%2FScreenshot%202025-05-06%20at%2011.09.16.png?alt=media" alt=""><figcaption></figcaption></figure>

### **Including traffic on specific product pages**

You can select multiple pages to target in your test using `OR` criteria. When multiple conditions are set, Intelligems will **include** a user if they meet **any** of the conditions set.

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-1b5970353edc2c4dfe9e4d6f01649a50c2897ee4%2FScreenshot%202025-05-06%20at%2011.11.57.png?alt=media" alt=""><figcaption></figcaption></figure>

### **Including traffic for pages contained inside certain collections**

You can set more general inclusion rules by setting a broader URL. In this example, all URLs that start with "collection-a" or "collection-b" **will be included,** but URLs that start with a different URL, e.g. "collection-c" **will not be included**.

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-a4c3cc22c2e1cd1544c76fb73bfa81da6e51175c%2FScreenshot%202025-05-06%20at%2011.15.08.png?alt=media" alt=""><figcaption></figcaption></figure>

### Targeting the homepage

To target the homepage, simply use `/`

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-e08cb00e0d79780ca35c0cc55a3babf02a9109e2%2Fpage_targeting_homepage.png?alt=media" alt=""><figcaption></figcaption></figure>

## Page Targeting Tester

Use our Page targeting tester to check whether an example URL matches your configured targeting criteria. Here is an example of testing whether URL visits to certain collections will or will not be included in your test.

In this image, we are testing whether `https://ovenspring-cookware.myshopify.com/collection-c` matches the configured criteria.

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-642f79286168aa03bfb25c513315abf913cad8d2%2FScreenshot%202025-05-06%20at%2011.19.16.png?alt=media" alt=""><figcaption><p>Proposed URL failed to match configured criteria.</p></figcaption></figure>

In this image, we are testing whether `https://ovenspring-cookware.myshopify.com/collection-a` matches the configured criteria.

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-9369be52988327b68eef52d7c56045070976b6f5%2FScreenshot%202025-05-06%20at%2011.19.30.png?alt=media" alt=""><figcaption><p>Proposed URL matches configured criteria</p></figcaption></figure>
