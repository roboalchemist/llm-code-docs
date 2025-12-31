# Source: https://docs.redwoodjs.com/docs/seo-head

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [Reference](/docs/index)
-   [SEO & \<meta\> tags]

[Version: 8.8]

On this page

<div>

# SEO & `<meta>` tags

</div>

Search Engine Optimization is a dark art that some folks dedicate their entire lives to. We\'ve add a couple of features to Redwood to make HTML-based SEO fairly simple.

## Adding a Title[​](#adding-a-title "Direct link to Adding a Title") 

You certainly want to change the title of your Redwood app from the default of \"Redwood App.\" You can start by adding or modifying `title` inside of `/redwood.toml`

``` 
[web]
- title = "Redwood App"
+ title = "My Cool App"
  port = 8910
  apiUrl = "/.redwood/functions"
```

This title (the app title) is used by default for all your pages if you don\'t define another one. It will also be used for the title template.

### Title Template[​](#title-template "Direct link to Title Template") 

Now that you have the app title set, you probably want some consistence with the page title, that\'s what the title template is for.

Add `titleTemplate` as a prop for `RedwoodProvider` to have a title template for every page.

``` 
-  <RedwoodProvider>
+  <RedwoodProvider titleTemplate="%PageTitle | %AppTitle">
    /* ... */
  <RedwoodProvider />
```

You can use whatever formatting you\'d like in here. Some examples:

``` 
"%PageTitle | %AppTitle" => "Home Page | Redwood App"

"%AppTitle · %PageTitle" => "Redwood App · Home Page"

"%PageTitle : %AppTitle" => "Home Page : Redwood App"
```

## Adding to Page `<head>`[​](#adding-to-page-head "Direct link to adding-to-page-head") 

So you want to change the title of your page, or add elements to the `<head>` of the page? We\'ve got you!

Let\'s say you want to change the title of your About page, Redwood provides a built-in `<Head>` component, which you can use like this:

``` 
+import  from '@redwoodjs/web'

const AboutPage = () => `<MetaTags>` Deprecation

Prior to Redwood 6.6.0 this component was called `<MetaTags>` and had several special hard-coded props like `ogContentUrl`, which didn\'t properly map to the OpenGraph spec. We\'ll still render `<MetaTags>` for the foreseeable future, but it\'s deprecated and you should migrate to `<Metadata>` if you have an existing app.

### What About Nested Tags?[​](#what-about-nested-tags "Direct link to What About Nested Tags?") 

Redwood uses [react-helmet-async](https://github.com/staylor/react-helmet-async) underneath, which will use the tags furthest down your component tree.

For example, if you set title in your Layout, and a title in your Page, it\'ll render the one in Page - this way you can override the tags you wish, while sharing the tags defined in Layout.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTcgMi4zYzMuMTQgMCA1LjcgMi41NiA1LjcgNS43cy0yLjU2IDUuNy01LjcgNS43QTUuNzEgNS43MSAwIDAgMSAxLjMgOGMwLTMuMTQgMi41Ni01LjcgNS43LTUuN3pNNyAxQzMuMTQgMSAwIDQuMTQgMCA4czMuMTQgNyA3IDcgNy0zLjE0IDctNy0zLjE0LTctNy03em0xIDNINnY1aDJWNHptMCA2SDZ2Mmgydi0yeiI+PC9wYXRoPjwvc3ZnPg==)]Bots & `<meta>` Tags

For these headers to appear to bots and scrapers e.g. for twitter to show your title, you have to make sure your page is prerendered. If your content is static you can use Redwood\'s built-in [Prerender](/docs/prerender). For dynamic tags, check the [Dynamic head tags](#dynamic-tags)

## Setting `<meta>` Tags and OpenGraph Directives with `<Metadata>`[​](#setting-meta-tags-and-opengraph-directives-with-metadata "Direct link to setting-meta-tags-and-opengraph-directives-with-metadata") 

Often we want to set more than just the title and description of the page -- most commonly [OpenGraph](https://ogp.me/) headers.

Redwood provides a convenience component `<Metadata>` to help you create most of these `<meta>` tags for you with a more concise syntax. But, you can also pass children and define any custom content that you want.

Here\'s an example setting some common meta, including a page title, description, `og:image` and an `http-equiv`:

``` 
import  from '@redwoodjs/web'

const AboutPage = () => }
        robots="nofollow"
      >
        <meta httpEquiv="content-type" content="text/html; charset=UTF-8" />
      </Metadata>

      <h2>About Page</h2>
      <p className="font-light">This is the about page!</p>
    </div>
  )
}

export default AboutPage
```

This code would be transformed into this HTML and injected into the `<head>` tag:

``` 
<title>About page</title>
<meta name="title" content="About page" />
<meta name="description" content="About the awesome team" />
<meta name="robots" content="nofollow" />
<meta property="og:title" content="About page" />
<meta property="og:description" content="About the awesome team" />
<meta property="og:image" content="https://example.com/images/og.png" />
<meta property="og:url" content="https://example.com/start" />
<meta property="og:type" content="website" />
<meta http-equiv="content-type" content="text/html; charset=UTF-8" />
```

Setting an `og:image` is how sites like Facebook and Slack can show a preview of a URL when pasted into a post (also known as \"unfurling\"):

![Typical URL unfurl](/assets/images/facebook_unfurl-da4e2ed64b0cd12e85aa39cacd723082.png)

Sites like GitHub go a step farther than a generic image by actually creating an image for a repo on the fly, including details about the repo itself:

![GitHub\'s og for the redwood repo](https://opengraph.githubassets.com/322ce8081bb85a86397a59494eab1c0fbe942b5104461f625e2c973c46ae4179/redwoodjs/redwood)

If you want to write your own `<meta>` tags, skipping the interpolation that `<Metadata>` does for you, you can pass them as children to `<Metadata>` or just write them into the `<head>` tag as normal.

### `<Metadata>` Props[​](#metadata-props "Direct link to metadata-props") 

For the most part `<Metadata>` creates simple `<meta>` tags based on the structure of the props you pass in. There are a couple of special behaviors described below.

#### Plain Key/Value Props[​](#plain-keyvalue-props "Direct link to Plain Key/Value Props") 

Any \"plain\" key/value prop will be turned into a `<meta>` tag with `name` and `content` attributes:

``` 
<Metadata description="Lorem ipsum dolar sit amet..." />
// generates
<meta name="description" content="Lorem ipsum dolar sit amet..." />
```

Child elements are just copied 1:1 to the resulting output:

``` 
<Metadata description="Lorem ipsum dolar sit amet...">
  <meta httpEquiv="refresh" content="30" />
</Metadata>
// generates
<meta name="description" content="Lorem ipsum dolar sit amet..." />
<meta http-equiv="refresh" content="30" />
```

#### Passing Objects to Props[​](#passing-objects-to-props "Direct link to Passing Objects to Props") 

Any props that contain an object will create a `<meta>` tag with `property` and `content` attributes, and the `property` being the names of the nested keys with a `:` between each:

``` 
<Metadata music= }}/>
// generates
<meta property="music:album:track" content="12" />
```

This is most commonly used to create the \"nested\" structure that a spec like OpenGraph uses:

``` 
<Metadata og=
<Metadata og=
<Metadata
  og=,
      'http://host.test/image2.jpg',
      'http://host.test/image3.jpg',
      ,
      ,
    ],
  }}
/>
// generates
<meta property="og:image" content="http://host.test/image1.jpg" />
<meta property="og:image:width" content="320" />
<meta property="og:image:height" content="240" />
<meta property="og:image" content="http://host.test/image2.jpg" />
<meta property="og:image" content="http://host.test/image3.jpg" />
<meta property="og:image:width" content="1024" />
<meta property="og:image:height" content="768" />
```

#### Special OpenGraph Helpers[​](#special-opengraph-helpers "Direct link to Special OpenGraph Helpers") 

If you define *any* `og` prop, we will copy any `title` and `description` to an `og:title` and `og:description`:

``` 
<Metadata title="My Website" og />
// generates
<meta name="title" content="My Website" />
<meta property="og:title" content="My Website" />
```

You can override this behavior by explicitly setting `og:title` or `og:description` to `null`:

``` 
<Metadata title="My Website" og=}/>
// generates
<meta name="title" content="My Website" />
```

Of course, if you don\'t want any auto-generated `og` tags, then don\'t include any `og` prop at all!

In addition to `og:title` and `og:description`, if you define *any* `og` prop we will generate an `og:type` set to `website`:

``` 
<Metadata og />
// generates
<meta property="og:type" content="website" />
```

You can override the `og:type` by setting it directly:

``` 
<Metadata og=}/>
// generates
<meta property="og:type" content="music:album" />
```

#### Other Special Cases[​](#other-special-cases "Direct link to Other Special Cases") 

If you define a `title` prop we will automatically prepend a `<title>` tag to the output:

``` 
<Metadata title="My Website" />
// generates
<title>My Website</title>
<meta name="title" content="My Website" />
```

If you define a `charSet` prop we will create a `<meta>` tag with the `charset` attribute:

``` 
<Metadata charSet="utf-8" />
// generates
<meta charset="utf-8" />
```

We simplified some of the examples above by excluding the generated `<title>` and `og:type` tags, so here\'s the real output if you included `title` and `og` props:

``` 
<Metadata title="My Website" og />
// generates
<title>My Website</title>
<meta name="title" content="My Website" />
<meta property="og:title" content="My Website" />
<meta property="og:type" content="website" />
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTcgMi4zYzMuMTQgMCA1LjcgMi41NiA1LjcgNS43cy0yLjU2IDUuNy01LjcgNS43QTUuNzEgNS43MSAwIDAgMSAxLjMgOGMwLTMuMTQgMi41Ni01LjcgNS43LTUuN3pNNyAxQzMuMTQgMSAwIDQuMTQgMCA4czMuMTQgNyA3IDcgNy0zLjE0IDctNy0zLjE0LTctNy03em0xIDNINnY1aDJWNHptMCA2SDZ2Mmgydi0yeiI+PC9wYXRoPjwvc3ZnPg==)]Do I need to apply these same tags over and over in every page?

Some `<meta>` tags, like `charset` or `locale` are probably applicable to the entire site, in which case it would be simpler to just include these once in your `index.html` instead of having to set them manually on each and every page/cell of your site.

This should allow you to create a fairly full-featured set of `<meta>` tags with minimal special syntax! A typical `<Metadata>` invocation could look like:

``` 
<Metadata
  title="My Website"
  description="An amazing website created with RedwoodJS"
  robots="noindex,nofollow"
  og=}
  twitter=}
/>
```

## Dynamic tags[​](#dynamic-tags "Direct link to Dynamic tags") 

Bots will pick up our tags if we\'ve prerendered the page, but what if we want to set the `<meta>` based on the output of the Cell?

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTcgMi4zYzMuMTQgMCA1LjcgMi41NiA1LjcgNS43cy0yLjU2IDUuNy01LjcgNS43QTUuNzEgNS43MSAwIDAgMSAxLjMgOGMwLTMuMTQgMi41Ni01LjcgNS43LTUuN3pNNyAxQzMuMTQgMSAwIDQuMTQgMCA4czMuMTQgNyA3IDcgNy0zLjE0IDctNy0zLjE0LTctNy03em0xIDNINnY1aDJWNHptMCA2SDZ2Mmgydi0yeiI+PC9wYXRoPjwvc3ZnPg==)]Prerendering

As of v3.x, Redwood supports prerendering your [Cells](https://redwoodjs.com/docs/cells) with the data you were querying. For more information please refer [to this section](https://redwoodjs.com/docs/prerender#cell-prerendering).

Let\'s say in our `PostCell`, we want to set the title to match the `Post`.

``` 
import  from '@redwoodjs/web'

import Post from 'src/components/Post/Post'

export const QUERY = gql`
  query FindPostById($id: Int!) 
    }
  }
`

export const Loading = /* ... */

export const Empty = /* ... */

export const Success = () => 
        author=
        description=
      />
      <Post post= />
    </>
  )
}
```

Once the `Success` component renders, it will update your page\'s `<title>` and set the relevant `<meta>` tags for you!

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6Ij48L3BhdGg+PC9nPjwvc3ZnPg==)Edit the latest version of this page](https://github.com/redwoodjs/graphql/blob/main/docs/docs/seo-head.md)