# How to Embed a Notion Page Into Your Website

Recently, it's become very easy to embed a Notion page into your website.

Instead of copy and paste, you can link your Notion page directly to your website.

## Option 1: Use a basic Notion iframe

![The Notion embed interface showing iframe code to copy](https://framerusercontent.com/images/buhh1FslueKgZbxt5pnFKvTK8k.png)

First, unlock your page for the world to see:

- Open your Notion page.
- Click the "Share" button in the top-right corner.
- Click on "Publish."
- Snag the public URL by copying it.
- Click on "Embed this page" and copy the iframe code.

Alternatively, swap out `YOUR_NOTION_PUBLIC_URL` with your copied link:

```html
<iframe src="YOUR_NOTION_PUBLIC_URL" style="width:100%; height:600px; border:none;">
</iframe>
```

## Option 2: Use a customized iframe

![Using EmbedNotionPages to generate a styled iframe](https://framerusercontent.com/images/I7kXhsAEgf3c4tLBQlsZzOc.png)

The Notion iframe works but it's basicâyou can't customize it or define who can access it.

This is solved with [EmbedNotionPages](https://www.embednotionpages.com/), a simple tool to create highly customized Notion iframes.

- Sign up.
- Add your Notion page to the tool.
- Paste your Notion link into the tool.
- Customize the look and feel and access control.
- Copy the iframe code.

## Add the iframe to your site

Now you just need to paste the iframe HTML code into the website page of your choice.

- **For HTML sites:** Paste the iframe code right into your page.
- **For WordPress, Webflow, Squarespace, or Framer:** Drop it into a custom HTML block.

## Things to watch out for

- **Privacy first:** Make sure you're not sharing anything sensitive.
- **Performance check:** Embeds can slow pages slightlyâalways test after adding.

## Frequently asked questions

### Can I embed a private Notion page?

No â you must publish your Notion page to the web to embed it.

### Will updates in Notion show up automatically on my site?

Yes â any edits you make in Notion will reflect live on your website.

### Can I change the size of the embedded page?

Yes â you can adjust the width and height in the iframe code to fit your design.

### Is using a tool like EmbedNotionPages secure?

EmbedNotionPages uses secure methods to display your page, but always review privacy settings before embedding.