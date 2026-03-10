# Source: https://screenshotone.com/docs/guides/screenshot-google-docs/

# How to render Google Documents as JPEG, PNG or WebP screenshots

import Video from "@/components/Video.astro";

By default, you can not render Google Docs as screenshots with the ScreenshotOne API. But if you managed to export it as HTML, you can make it work.

## Make Google Documents available as HTML

To make Google Documents available as HTML, you need to export it as HTML from the Google Docs editor.

I created [a simple Google Documents example](https://docs.google.com/document/d/1cY0QhA2GGCdhsoFCJYBCeCproSMzWwvUqkbnylwUGog/edit?usp=sharing) to demonstrate how to do that. 

(1) For document, go to share settings: 

![The Google Docs share settings](./google-docs-share-settings.png)

(2) Change the settings to make the document public and shareable:

![The Google Docs share settings](./google-docs-share-settings-make-public.png)

After that you can use either Google Docs API or make the link shareable and public to everyone and then modify it to the link like:
`https://docs.google.com/document/d/<document id>/export/html`.

## Render Google Documents as screenshots

Get your ScreenshotOne API key at the [ScreenshotOne dashboard](https://dashboard.screenshotone.com/).

And then implement the following example in TypeScript or any other language you want:

```typescript
// validate URL
const documentUrl = new URL(url);
if (!documentUrl.hostname.includes("docs.google.com")) {
    throw new Error("Invalid URL: Must be a Google Doc document URL");
}

// Extract document ID from the Google Doc URL
const match = documentUrl.pathname.match(/document\/d\/([\w-]+)/);
if (!match) {
    throw new Error("Invalid Google Docs URL format");
}

const documentId = match[1];
// for documents, change to "document"
const exportUrl = `https://docs.google.com/document/d/${documentId}/export/html`;
url = exportUrl;

// Prepare ScreenshotOne API parameters
const params: Record<string, string> = {
    url: url,
    access_key: SCREENSHOTONE_ACCESS_KEY as string,    
};

const apiUrl = `https://api.screenshotone.com/take`;
console.log("Making request to ScreenshotOne API...");

// Make request to ScreenshotOne API
const screenshotResponse = await axios({
    method: "post",
    url: apiUrl,
    data: params,
    headers: {
        "Content-Type": "application/json",
    },
    responseType: "stream",
    maxContentLength: Infinity,
    maxBodyLength: Infinity,
    timeout: 60000, // increase timeout to 60 seconds
});

// Process the image
```

Notice that we use a POST HTTP request to the `https://api.screenshotone.com/take` endpoint. It is good if you want to send HTML yourself, but also works with URLs. Also, you can just send a regular GET request.

The resulting video will be something like: 

## Set custom styles

In case, you do not like how Google Slides or Documents look like by default, you can set custom styles via the `style` option:

```
style=<your CSS styles>
```
Adding such a style option to Google Documents, will make look them differently. 

## A working example

You can find a fully working example (written in Node.js/TypeScript) in the [ScreenshoOne integration examples directory](https://github.com/screenshotone/examples/tree/main/nodejs/google-slides-scrolling-screenshots). However, it is for Google Slides
and downloads HTML to render it with ScreenshotOne, but today you do not need that, you can render Google Documents and Slides directly with ScreenshotOne.

## Suggestions

1. If possible, use the official Google Docs API to get the HTML. It is more reliable and easier to use. 
2. If you build this solution for third-party use, consider if you can automate the processing of authentication with Google Docs and extract the HTML. 

## Google Slides

Check out [our guide on how to render Google Slides as scrolling screenshots](/docs/guides/google-slides-as-scrolling-screenshots/).

## Support 

In case you have any questions or suggestions, feel free to reach out at `support@screenshotone.com`.