# Source: https://docs.redwoodjs.com/docs/assets-and-files

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [Reference](/docs/index)
-   [Assets and Files]

[Version: 8.8]

On this page

<div>

# Assets and Files

</div>

There are two ways to add an asset to your Redwood app:

1.  co-locate it with the component using it and import it into the component as if it were code
2.  add it to the `web/public` directory and reference it relative to your site\'s root

Where possible, prefer the first strategy.

It lets Vite include the asset in the bundle when the file is small enough.

### Co-locating and Importing Assets[​](#co-locating-and-importing-assets "Direct link to Co-locating and Importing Assets") 

Let\'s say you want to show your app\'s logo in your `Header` component. First, add your logo to the `Header` component\'s directory:

``` 
web/src/components/Header/
├── logo.png
├── Header.js
├── Header.stories.js
└── Header.test.js
```

Then, in the `Header` component, import your logo as if it were code:

web/src/components/Header/Header.js

``` 
import logo from './logo.png'

const Header = () => 
      <img src= alt="Logo" />
    </header>
  )
}

export default Header
```

If you\'re curious how this works, see the Vite docs on [static asset handling](https://vitejs.dev/guide/assets.html).

## Adding to the `web/public` Directory[​](#adding-to-the-webpublic-directory "Direct link to adding-to-the-webpublic-directory") 

You can also add assets to the `web/public` directory, effectively adding static files to your app. During dev and build, Redwood copies `web/public`\'s contents into `web/dist`.

> Changes to `web/public` don\'t hot-reload.

Again, because assets in this directory don\'t go through Vite, **use this strategy sparingly**, and mainly for assets like favicons, manifests, `robots.txt`, libraries incompatible with Vite, etc.

### Example: Adding Your Logo and Favicon to `web/public`[​](#example-adding-your-logo-and-favicon-to-webpublic "Direct link to example-adding-your-logo-and-favicon-to-webpublic") 

Let\'s say that you\'ve added your logo and favicon to `web/public`:

``` 
web/public/
├── img/
│  └── logo.png
└── favicon.png
```

When you run `yarn rw dev` and `yarn rw build`, Redwood copies `web/public/img/logo.png` to `web/dist/img/logo.png` and `web/public/favicon.png` to `web/dist/favicon.png`:

``` 
web/dist/
├── static/
│  ├── js/
│  └── css/
├── img/
│  └── logo.png
└── favicon.png
```

You can reference these files in your code without any special handling:

web/src/components/Header/Header.js

``` 
import  from '@redwoodjs/web'

const Header = () => 

export default Header
```

## Styling SVGs: The special type of image[​](#styling-svgs-the-special-type-of-image "Direct link to Styling SVGs: The special type of image") 

By default you can import and use SVG images like any other image asset.

web/src/components/Example.jsx

``` 
import svgIconSrc from '../mySvg.svg'

const Example = () =>  alt="Logo" />
    </>
  )
}

export default Example
```

Sometimes however, you might want more control over styling your SVGs - maybe you want to modify the `stroke-width` or `fill` color.

The easiest way to achieve this, is to make your SVGs a React component. Open up your SVG file, and drop in its contents into a component -- for example:

web/src/components/icons/CarIcon.tsx

``` 
import type  from "react"

export const CarIcon = (props: SVGProps) =>  // or adjust properties directly
    // ...
```

If you needed to convert a whole library of SVGs into stylable (or animatable!) components, one easy way would be to use the [SVGR cli](https://react-svgr.com/docs/cli/)

## Custom fonts[​](#custom-fonts "Direct link to Custom fonts") 

There are many different ways to peel this potato -- it\'s all a search away -- but if you\'re using the CSS `@font-face` rule, we have a quick tip for you:

1.  Place your fonts in the public folder, so it gets carried across
2.  In your CSS, use absolute paths - the public folder being your root - to point to the font file (same as the [Vite docs](https://vitejs.dev/guide/assets.html#the-public-directory)), for example:

``` 
web/
├── src
├── App.tsx
├── entry.client.tsx
├── index.css
├── ...
├── public
│ ├── favicon.png
│ ├── fonts
│ │ └── RedwoodNeue.woff2
```

``` 
/* in e.g. index.css */
@font-face 
```

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6Ij48L3BhdGg+PC9nPjwvc3ZnPg==)Edit the latest version of this page](https://github.com/redwoodjs/graphql/blob/main/docs/docs/assets-and-files.md)