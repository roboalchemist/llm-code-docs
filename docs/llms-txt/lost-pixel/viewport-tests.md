# Source: https://docs.lost-pixel.com/docs/recipes/general-recipes/viewport-tests.md

# Viewport tests

Lost Pixel supports testing different viewports. You can use the **breakpoints** option in the config. Page/story level breakpoints will override the top-level breakpoints.

{% hint style="info" %}
Breakpoint tests are supported in both OSS and Platform versions of Lost Pixel
{% endhint %}

{% code title="lostpixel.config.ts" %}

```typescript

import { CustomProjectConfig } from 'lost-pixel';

export const config: CustomProjectConfig = {
    pageShots: {
        pages: [
            { path: '/', name: 'landing' },
            {
                path: '/blog',
                name: 'blog',
                breakpoints: [800, 1400],
            },
        ],
        baseUrl: 'http://172.17.0.1:3000',
        breakpoints: [640, 1024],
    },
    waitBeforeScreenshot: 3500,
    lostPixelProjectId: 'YOUR_PROJECT_ID',
    apiKey: process.env.LOST_PIXEL_API_KEY,
};
```

{% endcode %}

<figure><img src="https://354517992-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2tpFIKHmNw4YdppgU75t%2Fuploads%2Fgit-blob-f4061f0efddbd9c09881399fa14a6411adc7e7f3%2FScreenshot%202023-10-26%20at%2014.51.55.png?alt=media" alt=""><figcaption></figcaption></figure>
