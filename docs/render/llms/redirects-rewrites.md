# Source: https://render.com/docs/redirects-rewrites.md

# Static Site Redirects and Rewrites

You can add *redirect and rewrite rules* to your static sites in the [Render Dashboard](https://dashboard.render.com):

[image: Setting redirect and rewrite rules in the Render Dashboard]

When the path of an incoming request matches a rule's *Source*, Render automatically redirects or rewrites the request to the corresponding *Destination*. For details, see [Rule matching and ordering](#rule-matching-and-ordering).

> *You can't apply redirect/rewrite rules to your domain root.*
>
> Each *Source* requires at least one URL path component (such as `/blog`, or even `/`).

## Which action to use?

Set each rule's Action to *Redirect* or *Rewrite* according to your needs:

------

###### Action

*Redirect*

###### Description

Instructs the browser (or any other client) to *switch URLs* to the rule's destination via a `301 Moved Permanently` response code. Create a redirect rule if you're moving an existing resource from one path to another (for example, if you move your site's documentation content from `/documentation` to `/docs`).

---

###### Action

*Rewrite*

###### Description

*Does not redirect the browser.* Instead, your site serves the content from the rule's destination at the original path. The browser can't detect that content was served from a different path or URL. Create a rewrite rule if:

- You want to serve the same content from multiple paths.
- Your static site uses a framework with [client-side routing](https://facebook.github.io/create-react-app/docs/deployment#serving-apps-with-client-side-routing) (such as [react-router](https://github.com/ReactTraining/react-router) or [Vue Router](https://router.vuejs.org/)), and you'll handle all requests from a single path like `/index.html`.

------

## Rule matching and ordering

*Render does not apply redirect or rewrite rules to a path if a resource exists at that path.* Instead, Render simply serves the resource at that path. This protects against overwriting valid paths with a rule, especially when using [wildcards](#wildcards).

Here's what the full path-matching process looks like:

[diagram]

If this process results in a redirect to another site path, the process repeats with the new path.

## Rule syntax

- *Source* must be a path (not a full URL). This is matched against the path of the incoming request.
- *Destination* can be either a path or a full, publicly accessible URL.

### Basic examples

| Source | Destination |
| --- | --- |
| `/home` | `/` |
| `/blog/index.html` | `/blog` |
| `/web-host` | `https://render.com` |

### Wildcards

Use a *wildcard* (`*`) to match arbitrary strings in a path.

- In *Source*, `*` matches _any_ string that appears starting at that position in the path.
  - Specify `/*` to match _all_ paths.
- In *Destination*, `*` applies the _entire string_ captured by the wildcard in *Source*.

| Source | Destination   | Example Effect                            |
| ------ | ------------- | ----------------------------------------- |
| `/*`   | `/blog/*`     | `/path1/path2` &rarr; `/blog/path1/path2` |
| `/*`   | `/index.html` | All requests &rarr; `/index.html`         |

### Placeholders

Use *placeholders* to include specific path components from *Source* in *Destination*:

| Source                  | Destination               | Example Effect                                 |
| ----------------------- | ------------------------- | ---------------------------------------------- |
| `/blog/posts/:postid`   | `/blog/:postid`           | `/blog/posts/my-post` &rarr; `/blog/my-post`   |
| `/updates/:month/:year` | `/changelog/:year/:month` | `/updates/03/2024` &rarr; `/changelog/2024/03` |

---

##### Appendix: Glossary definitions

###### static site

Deploy this *service type* to host a static website (HTML/CSS/JS) over a global CDN at a public URL.

Related article: https://render.com/docs/static-sites.md