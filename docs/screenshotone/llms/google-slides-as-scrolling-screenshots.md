# Source: https://screenshotone.com/docs/guides/google-slides-as-scrolling-screenshots/

# How to render Google Slides as scrolling screenshots with ScreenshotOne

import Video from "@/components/Video.astro";

By default, you can not render Google Slides as scrolling screenshots with the ScreenshotOne API. But if you managed to export it as HTML, you can make it work.

## Make Google Slides available as HTML

To make Google Slides available as HTML, you need to export it as HTML from the Google Slides editor.

I created [a simple example Google Slides presentation](https://docs.google.com/presentation/d/1fsaM1LaLUEzNn9pTPRdY0XBz1WxaFcWBD2WY50SrqwY/edit?usp=sharing) to demonstrate how to do that.

(1) For you presentation, go to share settings: 

![The Google Slides share settings](./google-slides-share-settings.png)

(2) Change the settings to make the presentation public and shareable:

![The Google Slides share settings](./google-slides-share-settings-make-public.png)

After that you can use either Google Slides API or make the link shareable and public to everyone and then modify it to the link like:
`https://docs.google.com/presentation/d/<presentation id>/export/html`

## Render Google Slides as scrolling screenshots

Get your ScreenshotOne API key at the [ScreenshotOne dashboard](https://dashboard.screenshotone.com/).

And then implement the following example in TypeScript or any other language you want:

```typescript
// validate URL
const presentationUrl = new URL(url);
if (!presentationUrl.hostname.includes("docs.google.com")) {
    throw new Error("Invalid URL: Must be a Google Slides presentation URL");
}

// Extract presentation ID from the Google Slides URL
const match = presentationUrl.pathname.match(/presentation\/d\/([\w-]+)/);
if (!match) {
    throw new Error("Invalid Google Slides URL format");
}

const presentationId = match[1];
const exportUrl = `https://docs.google.com/presentation/d/${presentationId}/export/html`;
url = exportUrl;

// Prepare ScreenshotOne API parameters
const params: Record<string, string> = {
    url: url,
    access_key: SCREENSHOTONE_ACCESS_KEY as string,
    format: "mp4",
    scenario: "scroll",
    delay: "2", // wait for 2 seconds before starting to scroll
};

const apiUrl = `https://api.screenshotone.com/animate`;
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

// Process the video
```

Notice that we use a POST HTTP request to the `https://api.screenshotone.com/animate` endpoint. It is good if you want to send HTML yourself, but also works with URLs. Also, you can just send a regular GET request.

The resulting video will be something like: 

<Video url="/videos/google-slides-scrolling-screenshot.mp4" />

## Custom styles 

You can set custom styles via the `style` option:

```
style=<your CSS styles>
```

## A working example

You can find a fully working example (written in Node.js/TypeScript) in the [ScreenshoOne integration examples directory](https://github.com/screenshotone/examples/tree/main/nodejs/google-slides-scrolling-screenshots). However, it downloads HTML to render it with ScreenshotOne, but today you do not need that, you can render Google Documents and Slides directly with ScreenshotOne.

## Suggestions

1. If possible, use the official Google Slides API to get the HTML. It is more reliable and easier to use. 
2. If you build this solution for third-party use, consider if you can automate the processing of authentication with Google Slides and extract the HTML. 

## Google Documents

Check out [our guide on how to render Google Documents as screenshots](/docs/guides/screenshot-google-docs/).

## Support 

In case you have any questions or suggestions, feel free to reach out at `support@screenshotone.com`.