# Source: https://docs.lost-pixel.com/docs/recipes/general-recipes/masking-page-elements.md

# Masking page elements

Lost Pixel supports masking elements that can be flaky during visual tests. Lazy-loaded images, animated components, and other parts of pages are all good candidates for masking them out.

You can use any selectors to mask the elements on the page. Refer to api reference for more details:

[mask](https://docs.lost-pixel.com/docs/api-reference/mask "mention")

{% code title="lostpixel.config.ts" %}

```typescript

import { CustomProjectConfig } from 'lost-pixel';

export const config: CustomProjectConfig = {
  pageShots: {
    pages: [
      { path: '/app', name: 'app' },
      {
        path: '/app',
        name: 'app-masked',
        mask: [{ selector: 'code' }, { selector: 'h2' }],
        breakpoints: [360, 500],
      },
      { path: '/next-app', name: 'next-app' },
    ],
    baseUrl: 'http://127.0.0.1:3000',
  },
  generateOnly: true,
  failOnDifference: true,
};
```

{% endcode %}

<figure><img src="https://354517992-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2tpFIKHmNw4YdppgU75t%2Fuploads%2Fgit-blob-355b49ec61e455df23673c376d6f4bca722bc6c3%2Fapp-masked__%5Bw500px%5D.png?alt=media" alt="" width="250"><figcaption></figcaption></figure>
