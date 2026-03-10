# Remember to also add this ^ env var in your deployment platform
```

### Configure Node Scripts

In order to generate the BaseHub SDK, we recommend running `basehub dev` in parallel to running the development server, and `basehub` right before building the app.

package.json

```
"scripts": {
  "dev": "basehub dev & vite dev",
  "build": "basehub && vite build",
  "preview": "vite preview",
  ... rest scripts
},
```

### Start the Dev Server

Give it a go to make sure the set up went correctly.

npm

```
npm run dev
```

## Your First Query

Now, let’s go ahead and query some content!

+page.server.ts

```
import type { PageServerLoad } from "./$types"
import { basehub } from "basehub"
import { BASEHUB_TOKEN } from "$env/static/private"

export const load: PageServerLoad = async () => {
  const data = await basehub({ token: BASEHUB_TOKEN }).query({
    __typename: true,
    _sys: {
      id: true,
    },
  })
  return data
}
```

## Support Table

While you can query BaseHub content from SvelteKit, there are some DX features that are not supported.

\[data-radix-scroll-area-viewport\]{scrollbar-width:none;-ms-overflow-style:none;-webkit-overflow-scrolling:touch;}\[data-radix-scroll-area-viewport\]::-webkit-scrollbar{display:none}

Feature

Supported

`basehub()`

✅

`<Pump />`

❌

`<RichText />`

❌

Analytics

✅

Search

✅ (just the client, not the UI helpers)