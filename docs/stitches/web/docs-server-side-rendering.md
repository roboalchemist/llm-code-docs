# Source: https://stitches.dev/docs/server-side-rendering

Title: Server-Side Rendering — Stitches

URL Source: https://stitches.dev/docs/server-side-rendering

Markdown Content:
How to configure server-side rendering.

You can get access to the CSS string by using the `getCssText` function. This function is made available by the `createStitches` function.

```
import { createStitches } from '@stitches/react';
export const { getCssText } = createStitches();
```

The `getCssText` will give you all the CSS you need to server-side render it.

For a better hydration strategy, we highly recommend adding an `id="stitches"` to your `style` tag.

Here's an example of SSR with Next.js

```
import React from 'react';
import NextDocument, { Html, Head, Main, NextScript } from 'next/document';
import { getCssText } from 'path-to/stitches.config';
export default class Document extends NextDocument {
render() {
return (
<Html lang="en">
        <Head>
          <style id="stitches" dangerouslySetInnerHTML={{ __html: getCssText() }} />
        </Head>
        <body>
          <Main />
          <NextScript />
        </body>
      </Html>
);
}
}
```

Note: If using React, make sure to add your styles in `dangerouslySetInnerHTML`.
