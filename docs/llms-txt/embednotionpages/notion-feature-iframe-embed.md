# The New Notion Embed & iFrame Feature

In February 2025, Notion launched a new feature: you can now embed Notion pages and forms into websites using iframes.

![Copying the iframe embed code](https://framerusercontent.com/images/irMRmugKI0NNSC7lUf4CrxvtQ4I.png)

## How Notion iframe works

Here's what you can now do in Notion:

- Get an iframe embed code from any public Notion page.
- Show Notion pages on your own site.
- Share live-updating content without extra tools.

Now, visitors can view and use your Notion content—like a portfolio or feedback form—without leaving your website.

## How to use Notion iframe

Follow these steps:

### Make Your Notion Page Public

Click “Share” in the top right corner of Notion, then “Publish” twice.

![Publishing a Notion page for embed](https://framerusercontent.com/images/jvxSXQjtmMt3z6zTUr95ecZxhbE.png)

### Get the Embed Code

Click “Embed this page,” then “Copy code” to get the iframe code.

![Getting the iframe embed code](https://framerusercontent.com/images/USDJoQaEeS3FfWtEfp3dgQ5DyZE.png)

### Add to Your Website

Paste it into your HTML where you want it (this is an example in Framer).

![Framer HTML block showing embedded iframe code](https://framerusercontent.com/images/wRaupWDDvv4Va5KCD5WrBJdOK2s.png)

Or create the iframe manually:

```html
<iframe src="NOTION_PUBLIC_PAGE_URL" style="width:100%; height:600px; border:none;" />
```

Replace `NOTION_PUBLIC_PAGE_URL` with your Notion page link.

## Why embed Notion pages?

Embedding can help in many ways:

- **Portfolios**: Show your work in style.
- **Docs**: Share guides or notes that auto-update.
- **Forms**: Gather feedback right from your site.
- **Dashboards**: Display real-time updates.

## Things to remember

- **Public pages only**: The page must be set to “Share to web.”
- **Responsive design**: Make sure it looks good on desktops and phones.
- **Auto updates**: Any changes to the Notion page will show up live.

## Limitation to Notion iframe features

This new embed feature is handy, but there are a few things to watch out for:

- **You can’t customise much**: What you see is pretty much what you get. You can't change how it looks beyond basic size settings.
- **No control over who sees it**: If the page is public, anyone with the link or iframe can view it. There’s no way to restrict access.
- **No way to hide parts of the page**: Once it’s embedded, everything is visible. You can’t limit what people interact with.
- **It relies on Notion**: If your Notion page isn’t live and working, the embed on your site won’t work.

If you’re looking for more customisation & access control, you can use [EmbedNotionPages](https://embednotionpages.com/). With it, you can create more ‘advanced’ Notion iframes that you can embed on any website.