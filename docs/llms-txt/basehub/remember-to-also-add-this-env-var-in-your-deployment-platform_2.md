# Remember to also add this ^ env var in your deployment platform
```

### Configure Node Scripts

In order to generate the BaseHub SDK, we recommend running `basehub dev` in parallel to running the development server, and `basehub` right before building the app.

package.json

```
"scripts": {
  "dev": "basehub dev & astro dev",
  "start": "basehub dev & astro dev",
  "build": "basehub && astro check && astro build",
  "preview": "astro preview",
  "astro": "astro"
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

src/pages/index.astro

```
---
import { basehub } from 'basehub'

const data = await basehub({
	token: import.meta.env.BASEHUB_TOKEN
}).query({
	__typename: true,
	_sys: {
        id: true
	}
})
---

<html lang="en">
	<head>
		<meta charset="utf-8" />
		<link rel="icon" type="image/svg+xml" href="/favicon.svg" />
		<meta name="viewport" content="width=device-width" />
		<meta name="generator" content={Astro.generator} />
		<title>Astro</title>
	</head>
	<body>
		<pre><code>{JSON.stringify(data, null, 2)}</code></pre>
	</body>
</html>
```

## Support Table

While you can query BaseHub content from Astro, there are some DX features that are not supported.

\[data-radix-scroll-area-viewport\]{scrollbar-width:none;-ms-overflow-style:none;-webkit-overflow-scrolling:touch;}\[data-radix-scroll-area-viewport\]::-webkit-scrollbar{display:none}

Feature

Supported

`basehub()`

✅

`<Pump />`

❌

`<RichText />`

✅ (with React)

Analytics

✅

Search

✅ (with React)