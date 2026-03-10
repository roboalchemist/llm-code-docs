# Source: https://screenshotone.com/docs/guides/how-to-screenshot-an-area-of-a-site/

# How to screenshot an area of a site

import Alert from "@/components/Alert.astro";

When rendering website screenshots with the ScreenshotOne Screenshot API, you can specify [clip options](https://screenshotone.com/docs/options/#clip) to render only a specific area of the website.

<Alert>You must specify all clip options, otherwise, it won't work.</Alert>

For example, let's clip a square of the ScreenshotOne landing page:

```
https://api.screenshotone.com/take?access_key=<your api key>&url=https://screenshotone.com&clip_x=100&clip_y=100&clip_width=500&clip_height=500
```

The resulting image will be:

![A clip example](./clip_example.png)

In case you can rely on a selector, it is better to use [the selector option](https://screenshotone.com/docs/options/#selector) than precise coordinates. It will allow you to produce more stable results. But in case you know what you do and prefer to rely on specific coordinates, it is OK to use clip options.

A few typical uses of the feature:

1. **Content Monitoring**. Businesses can use this feature to monitor their website's content regularly, ensuring that updates are correctly deployed and that there are no visual anomalies or layout issues.

2. **Competitor Analysis**. Companies can clip and analyze key sections of competitors' websites, such as product pages or promotional banners, to stay informed about market trends and competitor strategies.

3. **QA Testing**. Web developers and QA teams can automate the process of taking screenshots of different sections of a webpage across various devices and browsers for testing purposes, ensuring consistency and identifying layout issues.

Enjoy it. If you have any questions, please, feel free to send an email to `support.screenshotone.com`.