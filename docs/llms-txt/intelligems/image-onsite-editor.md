# Source: https://docs.intelligems.io/general-features/image-onsite-editor.md

# Image Onsite Editor

## What is the Image Onsite Editor?

The Intelligems Image Onsite Editor allows you to adjust the images featured on your site based on a visitor's test group. You will select where you want to update images and what the image should be for each group.

## Why would I need to use the Image Onsite Editor?

The Image Onsite Editor is a lightweight tool that makes it easy to show specific images per test group. Image replacements are set up directly through Intelligems, without the need to edit any HTML!

## Image Replacement Methods

Intelligems offers two ways to replace images in your tests.

### URL-based replacement (recommended)

Replace images site-wide using their source URL. When you use URL based image replacement, we'll replace every image on the page that has a matching source URL with your provided replacement. This enables you to seamlessly replace an image across collection pages, product thumbnails, mobile and desktop views, and more.

{% hint style="info" %}
This method works best when you use consistent image URLs across your site.
{% endhint %}

### Query selector replacement

Target a specific image on a specific page or position on a page using CSS selectors. This gives you precise control over which images change, but requires more technical setup.

### Making a choice

Use URL-based replacements if:

* you want to change an image across your entire site.
* you want to change an image across a set of pages or on a single page.

{% hint style="info" %}
Use Page Targeting to choose which pages show your replacement image.
{% endhint %}

Use Query selector replacements if

* your image shows up multiple times on a page and you want to replace only one of those.

{% hint style="info" %}
Query selectors were our original method for image replacement. URL-based replacements are now the default because they are simpler and work across multiple locations automatically.
{% endhint %}

## How to Set Up an Image Onsite Edit

1. Click the `Edit` button and Select the Image icon in the bottom left of the widget.

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-5e54bb1fe6616e7e3a4cef03654c0ad16cad1ddd%2FScreenshot%202025-10-07%20at%2013.14.09.png?alt=media" alt=""><figcaption></figcaption></figure>

2. Hover over images to indicate which image you want to replace and click on it. If there are multiple images that could be replaced, you will see a dialog prompting you to select the specific image you want to replace.

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-cc0a4fe51da1e8cca03924bcba28f4c8775a5590%2F2025-10-07%2018.34.40.gif?alt=media" alt=""><figcaption></figcaption></figure>

You can temporarily disable the highlighting if you need to interact with the page by using the spacebar. When you are ready to select your image, press the spacebar again to reactivate the selection mode.

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-daa862b52ec952aee820d2db99916e0436993133%2F2025-10-07%2018.32.20.gif?alt=media" alt=""><figcaption></figcaption></figure>

3. Once you have selected an image, a modal will pop down from our widget. This modal allows you to configure which images should be presented for each of your test groups.

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-7f1b471cd5ffbdc3ee98665e6355044af9507f5a%2F%202025-10-27%20at%2014.56.51.png?alt=media" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Note the checkboxes at the bottom of each image. Neither of these need to be checked for this feature to work.
{% endhint %}

4. To use an image URL from the web, you can copy and paste that url directly into the text input box. If you want to upload a photo from your Shopify account, you can click the button labeled `Select Image from Library`. This will reveal a modal that contains all images you have uploaded to your Shopify account. Click any image that you would like to upload.

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-3d0002cb2846304ff54185d4894451eed25a40c3%2FScreenshot%202023-09-20%20at%202.55.03%20PM.png?alt=media" alt="" width="375"><figcaption></figcaption></figure>

5. Make sure to hit the Save button on the widget to apply your changes to the page.
