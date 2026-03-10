# Source: https://firebase.google.com/docs/hosting/full-config.md.txt

With Firebase Hosting, you can configure customized hosting behavior for
requests to your site.

#### What can you configure for Hosting?

- Specify which files in your local project directory you want to deploy to
  Firebase Hosting. [Learn how.](https://firebase.google.com/docs/hosting/full-config#specify-files-to-deply)

- Serve a customized 404/Not Found page. [Learn how.](https://firebase.google.com/docs/hosting/full-config#404)

- Set up `redirects` for pages that you've moved or deleted.
  [Learn how.](https://firebase.google.com/docs/hosting/full-config#redirects)

- Set up `rewrites` for any of these purposes:

  - Show the same content for multiple URLs. [Learn how.](https://firebase.google.com/docs/hosting/full-config#rewrites)

  - Serve a function or access a Cloud Run container from a Hosting
    URL. Learn how: [function](https://firebase.google.com/docs/hosting/full-config#rewrite-function) or
    [container](https://firebase.google.com/docs/hosting/full-config#rewrite-cloud-run-container).

  - Create a custom domain Dynamic Link. [Learn how.](https://firebase.google.com/docs/hosting/full-config#rewrite-dynamic-links)

- Add `headers` to pass along additional information about a request or a
  response, such as how browsers should handle the page and its content
  (authentication, caching, encoding, etc.). [Learn how.](https://firebase.google.com/docs/hosting/full-config#headers)

- Set up internationalization (i18n) rewrites to serve specific content based
  on a user's language preference and/or country.
  [Learn how](https://firebase.google.com/docs/hosting/i18n-rewrites) (different page).

#### Where do you define your Hosting configuration?

You define your Firebase Hosting configuration in your
[`firebase.json`](https://firebase.google.com/docs/cli#the_firebasejson_file) file. Firebase
automatically creates your `firebase.json` file at the root of your project
directory when you run the
[`firebase init`](https://firebase.google.com/docs/hosting/quickstart#initialize) command.

> [!CAUTION]
> **Caution:** If you run `firebase init` again and select Hosting, the command will overwrite the `hosting` section of the `firebase.json` file back to the default configuration.

You can find a
[full `firebase.json` configuration example](https://firebase.google.com/docs/hosting/full-config#firebase-json_example)
(covering only Firebase Hosting) at the bottom of this page. Note that a
`firebase.json` file can also contain
[configurations for other Firebase services](https://firebase.google.com/docs/cli#the_firebasejson_file).

You can check the deployed `firebase.json` content using the
[Hosting REST API](https://firebase.google.com/docs/reference/hosting/rest/v1beta1/sites.releases/list?apix_params=%7B%22parent%22:%22sites/%3Cyour-site-name%3E%22,%22pageSize%22:1%7D).

## Priority order of Hosting responses

The different Firebase Hosting configuration options described on this page
can sometimes overlap. If there is a conflict, Hosting determines its
response using the following priority order:

1. Reserved namespaces that begin with a `/__/*` path segment
2. Configured [redirects](https://firebase.google.com/docs/hosting/full-config#redirects)
3. Exact-match static content
4. Configured [rewrites](https://firebase.google.com/docs/hosting/full-config#rewrites)
5. [Custom 404](https://firebase.google.com/docs/hosting/full-config#404) page
6. Default 404 page

> [!IMPORTANT]
> **Important:** Within each of the `redirects` and `rewrites` attributes, Hosting applies the redirect or rewrite defined by the *first* rule with a URL pattern that matches the requested path. So, you need to deliberately order the rules within each of the `redirects` and `rewrites` attributes. Configured `redirects` still take precedence over `rewrites`.

If you're using [i18n rewrites](https://firebase.google.com/docs/hosting/i18n-rewrites), the exact-match
and 404 handling priority order are expanded in scope to accommodate your "i18n
content".

## Specify which files to deploy

The default attributes --- [`public`](https://firebase.google.com/docs/hosting/full-config#public) and [`ignore`](https://firebase.google.com/docs/hosting/full-config#ignore) --- included
in the default `firebase.json` file define which files in your project directory
should be deployed to your Firebase project.

The default `hosting` configuration in a `firebase.json` file looks like this:

    "hosting": {
      "public": "public",  // the only required attribute for Hosting
      "ignore": [
        "firebase.json",
        "**/.*",
        "**/node_modules/**"
      ]
    }

### public

***Required***   

The `public` attribute specifies which directory to deploy to
Firebase Hosting. The default value is a directory named `public`, but you
can specify any directory's path, as long as it exists in your project
directory.

The following is the default specified name of the directory to deploy:

    "hosting": {
      "public": "public"

      // ...
    }

You can change the default value to the directory that you want to deploy:

    "hosting": {
      "public": "dist/app"

      // ...
    }

### ignore

***Optional***   

The `ignore` attribute specifies the files to ignore on deploy. It can take
[globs](https://firebase.google.com/docs/hosting/full-config#glob_pattern_matching) the same way that
[Git](https://en.wikipedia.org/wiki/Git_(software)) handles `.gitignore`.

The following are the default values for the files to ignore:

    "hosting": {
      // ...

      "ignore": [
        "firebase.json",  // the Firebase configuration file (the file described on this page)
        "**/.*",  // files with a leading period should be hidden from the system
        "**/node_modules/**"  // contains dependencies used to create your site but not run it
      ]
    }

## Customize a 404/Not Found page

***Optional***   

You can serve a custom `404 Not Found` error when a user tries to access a page
that doesn't exist.

Create a new file in your project's [`public` directory](https://firebase.google.com/docs/hosting/full-config#public), name it
`404.html`, then add your custom `404 Not Found` content to the file.

Firebase Hosting will display the content of this custom `404.html` page if
a browser triggers a `404 Not Found` error on your domain or subdomain.

## Configure redirects

***Optional***   

Use a URL redirect to prevent broken links if you've moved a page
or to shorten URLs. For example, you could redirect a browser from
`example.com/team` to `example.com/about.html`.

Specify URL redirects by creating a `redirects` attribute that contains an array
of objects (called "redirect rules"). In each rule, specify a URL pattern that,
if matched to the request URL path, triggers Hosting to respond with a redirect
to the specified destination URL.

Here's the basic structure for a `redirects` attribute. This example redirects
requests to `/foo` by making a new request to `/bar`.

    "hosting": {
      // ...

      // Returns a permanent redirect to "/bar" for requests to "/foo" (but not "/foo/**")
      "redirects": [ {
        "source": "/foo",
        "destination": "/bar",
        "type": 301
      } ]
    }

<br />

**View a more detailed example for a `redirects` attribute**

<br />

    "hosting": {
      // ...

      // Add the "redirects" attribute within "hosting"
      "redirects": [ {
        // Returns a permanent redirect to "/bar" for requests to "/foo" (but not "/foo/**")
        "source": "/foo",
        "destination": "/bar",
        "type": 301
      }, {
        // Returns a permanent redirect to "/bar" for requests to both "/foo" and "/foo/**"
        "source": "/foo{,/**}"
        "destination": "/bar"
        "type": 301
      }, {
        // Returns a temporary redirect for all requests to files or directories in the "firebase" directory
        "source": "/firebase/**",
        "destination": "https://firebase.google.com/",
        "type": 302
      }, {
        // A regular expression-based redirect equivalent to the above behavior
        "regex": "/firebase/.*",
        "destination": "https://firebase.google.com/",
        "type": 302
      } ]
    }

<br />

<br />

The `redirects` attribute contains an array of redirect rules, where each rule
must include the fields in the table below.

Firebase Hosting compares the `source` or `regex` value against all URL
paths at the start of every request (before the browser determines whether a
file or folder exists at that path). If a match is found, then the
Firebase Hosting origin server sends an HTTPS redirect response telling the
browser to make a new request at the `destination` URL.

| Field || Description |
|---|---|---|
| `redirects` |||
|   | `source` *(recommended)* or `regex` | A URL pattern that, if matched to the initial request URL, triggers Hosting to apply the redirect - Use `source` to specify a [glob](https://firebase.google.com/docs/hosting/full-config#glob_pattern_matching) *(recommended)*. - Use `regex` to specify a [RE2 regular expression](https://github.com/google/re2/wiki/Syntax). |
|   | `destination` | A static URL where the browser should make a new request This URL can be a relative or an absolute path. |
|   | `type` | The HTTPS response code - Use a type of `301` for 'Moved Permanently' - Use a type of `302` for 'Found' (Temporary Redirect) |

> [!IMPORTANT]
> **Important:** Within the `redirects` attribute, Hosting applies the redirect defined by the *first* rule with a URL pattern that matches the requested path. So, you need to deliberately order the rules within the `redirects` attribute.

### Capture URL segments for redirects

***Optional***   

Sometimes, you might need to capture specific segments of a redirect rule's URL
pattern (`source` or `regex` value), then re-use these segments in the
rule's `destination` path.

<br />

**Capture URL segments when using globs**

<br />

If you're using a `source` field (that is, specifying a glob for your URL
pattern), you can capture segments by including a `:` prefix to identify the
segment. If you also need to capture the remaining URL path after the segment,
include a `*` immediately after the segment. For example:

```
"hosting": {
  // ...

  "redirects": [ {
    "source": "/blog/:post*",  // captures the entire URL segment beginning at "post"
    "destination": "https://blog.myapp.com/:post", // includes the entire URL segment identified and captured by the "source" value
    "type": 301
  }, {
    "source": "/users/:id/profile",  // captures only the URL segment "id", but nothing following
    "destination": "/users/:id/newProfile",  // includes the URL segment identified and captured by the "source" value
    "type": 301
  } ]
}
```

<br />

<br />

<br />

**Capture URL segments when using RE2 regular expressions**

<br />

If you're using a `regex` field (that is, specifying a RE2 regular expression
for your URL pattern), you can capture segments using either named or unnamed
RE2 capture groups. Named capture groups can be used in the `destination` field
with a `:` prefix, while unnamed capture groups can be referenced by their
numerical index in the `regex` value, indexed from 1. For example:

```
"hosting": {
  // ...

  "redirects": [ {
    "regex": "/blog/(?P<post>.+)",  // if you're familiar with PCRE, be aware that RE2 requires named capture groups to begin with ?P
    "destination": "https://blog.myapp.com/:post",  // includes the entire URL segment identified and captured by the `regex` value
    "type": 301
  }, {
    "regex": "/users/(\d+)/profile",  // uses the \d directive to only match numerical path segments
    "destination": "/users/:1/newProfile",  // the first capture group to be seen in the `regex` value is named 1, and so on
    "type": 301
  } ]
}
```

<br />

<br />

## Configure rewrites

***Optional***   

Use a rewrite to show the same content for multiple URLs. Rewrites are
particularly useful with pattern matching, as you can accept any URL that
matches the pattern and let the client-side code decide what to display.

You can also use rewrites to support apps that use
[HTML5 pushState](https://developer.mozilla.org/en-US/docs/Web/Guide/API/DOM/Manipulating_the_browser_history#The_pushState().C2.A0method)
for navigation. When a browser attempts to open a URL path that matches the
specified `source` or `regex` URL pattern, the browser will be given the
contents of the file at the `destination` URL instead.

Specify URL rewrites by creating a `rewrites` attribute that contains an array
of objects (called "rewrite rules"). In each rule, specify a URL pattern that,
if matched to the request URL path, triggers Hosting to respond as if the
service were given the specified destination URL.

Here's the basic structure for a `rewrites` attribute. This example serves
`index.html` for requests to files or directories that don't exist.

    "hosting": {
      // ...

      // Serves index.html for requests to files or directories that do not exist
      "rewrites": [ {
        "source": "**",
        "destination": "/index.html"
      } ]
    }

<br />

**View a more detailed example for a `rewrites` attribute**

<br />

```
"hosting": {
// ...

// Add the "rewrites" attribute within "hosting"
"rewrites": [ {
  // Serves index.html for requests to files or directories that do not exist
  "source": "**",
  "destination": "/index.html"
}, {
  // Serves index.html for requests to both "/foo" and "/foo/**"
  // Using "/foo/**" only matches paths like "/foo/xyz", but not "/foo"
  "source": "/foo{,/**}",
  "destination": "/index.html"
}, {
  // A regular expression-based rewrite equivalent to the above behavior
  "regex": "/foo(/.*)?",
  "destination": "/index.html"
}, {
  // Excludes specified pathways from rewrites
  "source": "!/@(js|css)/**",
  "destination": "/index.html"
} ]
}
```

<br />

<br />

The `rewrites` attribute contains an array of rewrite rules, where each rule
must include the fields in the table below.

Firebase Hosting only applies a rewrite rule if a file or directory does not
exist at a URL path that matches the specified `source` or `regex` URL pattern.
When a request triggers a rewrite rule, the browser returns the actual content
of the specified `destination` file instead of an HTTP redirect.

| Field || Description |
|---|---|---|
| `rewrites` |||
|   | `source` *(recommended)* or `regex` | A URL pattern that, if matched to the initial request URL, triggers Hosting to apply the rewrite - Use `source` to specify a [glob](https://firebase.google.com/docs/hosting/full-config#glob_pattern_matching) *(recommended)*. - Use `regex` to specify a [RE2 regular expression](https://github.com/google/re2/wiki/Syntax). |
|   | `destination` | A local file that must exist This URL can be a relative or an absolute path. |

> [!IMPORTANT]
> **Important:** Within the `rewrites` attribute, Hosting applies the rewrite defined by the *first* rule with a URL pattern that matches the requested path. So, you need to deliberately order the rules within the `rewrites` attribute.

### Direct requests to a function

You can use `rewrites` to serve a function from a Firebase Hosting URL. The
following example is an excerpt from
[serving dynamic content using Cloud Functions](https://firebase.google.com/docs/hosting/functions).

For example, to direct all requests from the page `/bigben` on your
Hosting site to execute the `bigben` function:

    "hosting": {
      // ...

      // Directs all requests from the page `/bigben` to execute the `bigben` function
      "rewrites": [ {
        "source": "/bigben",
        "function": {
          "functionId": "bigben",
          "region": "us-central1"  // optional (see note below)
          "pinTag": true           // optional (see note below)
        }
      } ]
    }

<br />

**How `region`
works within the `function` block**

<br />

> If `region` is omitted from a `function` block of the `hosting.rewrites`
> config, the Firebase CLI attempts to automatically detect the region from
> the function's source code which, if unspecified, defaults to `us-central1`.
> If the function's source code is unavailable, the CLI attempts to detect
> the region from the deployed function. If the function is in multiple regions,
> the CLI requires `region` to be specified in the `hosting.rewrites`
> config.

<br />

<br />

<br />

**How
`pinTag` works within the `function` block**

<br />

> The `pinTag` feature is only available in Cloud Functions for Firebase (2nd gen).
> With this feature, you can ensure that each function for generating your
> site's dynamic content is kept in sync with your static Hosting resources
> and Hosting config. Also, this feature allows you to preview your rewrites
> to functions on Hosting preview channels.
>
> If you add `"pinTag": true` to a `function` block of the `hosting.rewrites`
> config, then the "pinned" function will be deployed along with your static
> Hosting resources and configuration, even when running
> `firebase deploy --only hosting`. If you roll back a
> version of your site, the "pinned" function is also rolled back.
>
> > [!NOTE]
> > **Note:** If you add a `pinTag` to an *existing* rewrite, you must first deploy the updated rewrite to your "live" channel. After that deploy, you can then preview changes to your function's code in Hosting preview channels without affecting production.
>
> This feature relies on
> [Cloud Run tags](https://cloud.google.com/run/docs/rollouts-rollbacks-traffic-migration#tags),
> which have a limit of 1000 tags per service and 2000 tags per region. This
> means that after hundreds of deploys, the oldest versions of a site may stop
> working.

<br />

<br />

After adding this rewrite rule and deploying to Firebase (using
`firebase deploy`), your function is reachable via the following URLs:

- Your Firebase subdomains:  

  `PROJECT_ID.web.app/bigben` and
  `PROJECT_ID.firebaseapp.com/bigben`

- Any connected [custom domains](https://firebase.google.com/docs/hosting/custom-domain):  

  `CUSTOM_DOMAIN/bigben`

When Firebase Hosting forwards traffic to a function, the function receives the
full original request path and query string. For example, a request to
`/bigben/hello/world?foo=bar` on your Hosting site is passed to the function
with the complete path and query intact. Make sure your function handler is
written to handle the *entire absolute URL*, not just the base path defined in
the rewrite.

When redirecting requests to functions with Hosting, supported HTTP request
methods are `GET`, `POST`, `HEAD`, `PUT`, `DELETE`, `PATCH`, and `OPTIONS`.
Other methods like `REPORT` or `PROFIND` are not supported.

### Direct requests to a Cloud Run container

You can use `rewrites` to access a Cloud Run container from a
Firebase Hosting URL. The following example is an excerpt from
[serving dynamic content using Cloud Run](https://firebase.google.com/docs/hosting/cloud-run).

For example, to direct all requests from the page `/helloworld` on your
Hosting site to trigger the startup and running of a `helloworld` container
instance:

    "hosting": {
     // ...

     // Directs all requests from the page `/helloworld` to trigger and run a `helloworld` container
     "rewrites": [ {
       "source": "/helloworld",
       "run": {
         "serviceId": "helloworld",  // "service name" (from when you deployed the container image)
         "region": "us-central1"  // optional (if omitted, default is us-central1)
       }
     } ]
    }

<br />

**How `pinTag`
works within the `run` block**

<br />

> With this feature, you can ensure that the revision of your Cloud Run
> service for generating your site's dynamic content is kept in sync with your
> static Hosting resources and Hosting config. Also, this feature allows
> you to preview your rewrites to Cloud Run on Hosting preview
> channels.
>
> If you add `"pinTag": true` to a `run` block of the `hosting.rewrites`
> config, your static Hosting resources and configuration will be pinned to
> the most recent revision of the Cloud Run service, at the time of
> deploy. If you roll back a version of your site, the revision of the "pinned"
> Cloud Run service is also rolled back.
>
> This feature relies on
> [Cloud Run tags](https://cloud.google.com/run/docs/rollouts-rollbacks-traffic-migration#tags),
> which have a limit of 1000 tags per service and 2000 tags per region. This
> means that after hundreds of deploys, the oldest versions of a site may stop
> working.

<br />

<br />

After adding this rewrite rule and deploying to Firebase (using
`firebase deploy`), your container image is reachable via the following URLs:

- Your Firebase subdomains:  

  `PROJECT_ID.web.app/helloworld` and
  `PROJECT_ID.firebaseapp.com/helloworld`

- Any connected [custom domains](https://firebase.google.com/docs/hosting/custom-domain):  

  `CUSTOM_DOMAIN/helloworld`

When redirecting requests to Cloud Run containers with Hosting,
supported HTTP request methods are `GET`, `POST`, `HEAD`, `PUT`, `DELETE`,
`PATCH`, and `OPTIONS`. Other methods like `REPORT` or `PROFIND` are not
supported.

For the best performance, colocate your Cloud Run service with Hosting using the following regions:

- `us-west1`
- `us-central1`
- `us-east1`
- `europe-west1`
- `asia-east1`

Rewrites to Cloud Run from Hosting are supported in the
following regions:

- `asia-east1`
- `asia-east2`
- `asia-northeast1`
- `asia-northeast2`
- `asia-northeast3`
- `asia-south1`
- `asia-south2`
- `asia-southeast1`
- `asia-southeast2`
- `australia-southeast1`
- `australia-southeast2`
- `europe-central2`
- `europe-north1`
- `europe-southwest1`
- `europe-west1`
- `europe-west12`
- `europe-west2`
- `europe-west3`
- `europe-west4`
- `europe-west6`
- `europe-west8`
- `europe-west9`
- `me-central1`
- `me-west1`
- `northamerica-northeast1`
- `northamerica-northeast2`
- `southamerica-east1`
- `southamerica-west1`
- `us-central1`
- `us-east1`
- `us-east4`
- `us-east5`
- `us-south1`
- `us-west1`
- `us-west2`
- `us-west3`
- `us-west4`
- `us-west1`
- `us-central1`
- `us-east1`
- `europe-west1`
- `asia-east1`

### Create custom domain Dynamic Links

> [!NOTE]
> **Note:** Firebase Dynamic Links is *deprecated* and should not be used in new projects. The service will be shutting down soon. Follow the [migration guide](https://firebase.google.com/support/dynamic-links-faq#how_should_i_migrate_from_the_service) and see the [Dynamic Links Deprecation FAQ](https://firebase.google.com/support/dynamic-links-faq) for more information.

You can use `rewrites` to create custom domain Dynamic Links. Visit the Dynamic Links
documentation for detailed information about
[setting up a custom domain for Dynamic Links](https://firebase.google.com/docs/dynamic-links/custom-domains#priority_order).

- Use your custom domain *only* for Dynamic Links

  ```
  "hosting": {
    // ...

    "appAssociation": "AUTO",  // required for Dynamic Links (default is AUTO if not specified)

    // Add the "rewrites" attribute within "hosting"
    "rewrites": [ {
      "source": "/**",  // the Dynamic Links start with "https://CUSTOM_DOMAIN/"
      "dynamicLinks": true
    } ]
  }
  ```
- Specify custom domain path prefixes to use for Dynamic Links

  ```
  "hosting": {
    // ...

    "appAssociation": "AUTO",  // required for Dynamic Links (default is AUTO if not specified)

    // Add the "rewrites" attribute within "hosting"
    "rewrites": [ {
      "source": "/promos/**",  // the Dynamic Links start with "https://CUSTOM_DOMAIN/promos/"
      "dynamicLinks": true
    }, {
      "source": "/links/share/**",  // the Dynamic Links start with "https://CUSTOM_DOMAIN/links/share/"
      "dynamicLinks": true
    } ]
  }
  ```

Configuring Dynamic Links in your `firebase.json` file requires the following:

| Field || Description |
|---|---|---|
| `appAssociation` || Must be set to `AUTO` - If you don't include this attribute in your configuration, the default for `appAssociation` is `AUTO`. - By setting this attribute to `AUTO`, Hosting can dynamically generate `assetlinks.json` and `apple-app-site-association` files when they're requested. |
| `rewrites` |||
|   | `source` | A path that you want to use for Dynamic Links Unlike rules that rewrite paths to URLs, rewrite rules for Dynamic Links can't contain regular expressions. |
|   | `dynamicLinks` | Must be set to `true` |

> [!NOTE]
> **Important** : For Dynamic Links, be particularly aware of [hosting priority order](https://firebase.google.com/docs/hosting/full-config#hosting_priority_order).
>
> - Ensure that your Dynamic Links URL prefix doesn't conflict with higher priority hosting configurations (for example, hosted static content always has priority over rewrites).
> - Within each of the `redirects` and `rewrites` attributes, Hosting applies the redirect or rewrite defined by the *first* rule with a URL pattern that matches the requested path. So, you need to deliberately order the rules within each of the `redirects` and `rewrites` attributes.
>
> For detailed information, refer to the
> [Dynamic Links
> documentation](https://firebase.google.com/docs/dynamic-links/custom-domains#priority_order).

## Configure headers

***Optional***   

Headers allow the client and the server to pass additional information along
with a request or a response. Some sets of headers can affect how the browser
handles the page and its content, including access control, authentication,
caching, and encoding.

Specify custom, file-specific response headers by creating a `headers` attribute
that contains an array of header objects. In each object, specify a URL pattern
that, if matched to the request URL path, triggers Hosting to apply the
specified custom response headers.

Here's the basic structure for a `headers` attribute. This example applies a
CORS header for all font files.

    "hosting": {
      // ...

      // Applies a CORS header for all font files
      "headers": [ {
        "source": "**/*.@(eot|otf|ttf|ttc|woff|font.css)",
        "headers": [ {
          "key": "Access-Control-Allow-Origin",
          "value": "*"
        } ]
      } ]
    }

<br />

**View a more detailed example for a `headers` attribute**

<br />

```
"hosting": {
  // ...

  // Add the "headers" attribute within "hosting"
  "headers": [ {
    // Applies a CORS header for all font files
    "source": "**/*.@(eot|otf|ttf|ttc|woff|font.css)",
    "headers": [ {
      "key": "Access-Control-Allow-Origin",
      "value": "*"
    } ]
  }, {
    // Overrides the default 1 hour browser cache with a 2 hour cache for all image files
    "source": "**/*.@(jpg|jpeg|gif|png)",
    "headers": [ {
      "key": "Cache-Control",
      "value": "max-age=7200"
    } ]
  }, {
    // A regular expression-based rewrite equivalent to the above behavior
    "regex": ".+/\w+\.(jpg|jpeg|gif|png)$",
    "headers": [ {
      "key": "Cache-Control",
      "value": "max-age=7200"
    } ]
  }, {
    // Sets the cache header for 404 pages to cache for 5 minutes
    "source": "404.html",
    "headers": [ {
      "key": "Cache-Control",
      "value": "max-age=300"
    } ]
  } ]
}
```

<br />

<br />

The `headers` attribute contains an array of definitions, where each definition
must include the fields in the table below.

| Field ||| Description |
|---|---|---|---|
| `headers` ||||
|   | `source` *(recommended)* or `regex` || A URL pattern that, if matched to the initial request URL, triggers Hosting to apply the custom header - Use `source` to specify a [glob](https://firebase.google.com/docs/hosting/full-config#glob_pattern_matching) *(recommended)*. - Use `regex` to specify a [RE2 regular expression](https://github.com/google/re2/wiki/Syntax). To create a header to match against your [custom 404 page](https://firebase.google.com/docs/hosting/full-config#404), use `404.html` as your `source` or `regex` value. |
|   | array of (sub-)`headers` || The custom headers that Hosting applies to the request path Each sub-header must include a [`key` and `value` pair](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers) (see next two rows). |
|   |   | `key` | The name of the header, for example `Cache-Control` |
|   |   | `value` | The value for the header, for example `max-age=7200` |

> [!NOTE]
> **Note:** The URL pattern matching for custom headers is done *before* any [rewrite rules](https://firebase.google.com/docs/hosting/full-config#rewrites) are applied. Matching rules are applied in the order they are defined.

You can learn more about [`Cache-Control`](https://firebase.google.com/docs/hosting/manage-cache) in the
Hosting section that describes serving dynamic content and hosting
microservices. You can also learn more about
[CORS](https://en.wikipedia.org/wiki/Cross-origin_resource_sharing) headers.

> [!IMPORTANT]
> **Important:** Firebase Hosting overwrites the `Strict-Transport-Security` configuration on default Hosting subdomains (like `*.web.app`). However, any connected custom domains will serve the configured value.

## Control `.html` extensions

***Optional***   

The `cleanUrls` attribute allows you to control whether or not URLs
should include the `.html` extension.

When `true`, Hosting automatically drops the `.html` extension from uploaded
file URLs. If an `.html` extension is added in the request, Hosting performs
a `301` redirect to the same path but eliminates the `.html` extension.

Here's how to control the inclusion of `.html` in URLs by including a
`cleanUrls` attribute:

    "hosting": {
      // ...

      // Drops `.html` from uploaded URLs
      "cleanUrls": true
    }

## Control trailing slashes

***Optional***   

The `trailingSlash` attribute allows you to control whether or not static
content URLs should include trailing slashes.

- When `true`, Hosting redirects URLs to add a trailing slash.
- When `false`, Hosting redirects URLs to remove a trailing slash.
- When unspecified, Hosting only uses trailing slashes for directory index files (for example, `about/index.html`).

Here's how to control trailing slashes by adding a `trailingSlash` attribute:

    "hosting": {
      // ...

      // Removes trailing slashes from URLs
      "trailingSlash": false
    }

The `trailingSlash` attribute does not affect rewrites to dynamic content
served by Cloud Functions or Cloud Run.

## Glob pattern matching

Firebase Hosting configuration options make extensive use of the
[glob pattern matching](https://en.wikipedia.org/wiki/Glob_%28programming%29)
notation with extglob, similar to how Git handles
[`gitignore`](https://git-scm.com/docs/gitignore) rules and
[Bower](https://github.com/bower/bower) handles `ignore` rules.
[This wiki page](https://mywiki.wooledge.org/glob) is a more detailed reference,
but the following are explanations of examples used on this page:

- **`firebase.json`** --- Only matches the `firebase.json` file in the root
  of the [`public`](https://firebase.google.com/docs/hosting/full-config#public) directory

- **`**`** --- Matches any file or folder in an arbitrary sub-directory

- **`*`** --- Only matches files and folders in the root of the
  [`public`](https://firebase.google.com/docs/hosting/full-config#public) directory

- **`**/.*`** --- Matches any file beginning with `.` (usually hidden files,
  like in the `.git` folder) in an arbitrary sub-directory

- **`**/node_modules/**`** --- Matches any file or folder in an arbitrary
  sub-directory of a `node_modules` folder, which can itself be in an arbitrary
  sub-directory of the [`public`](https://firebase.google.com/docs/hosting/full-config#public) directory

- **`**/*.@(jpg|jpeg|gif|png)`** --- Matches any file in an arbitrary
  sub-directory that ends with exactly one of the following: `.jpg`, `.jpeg`,
  `.gif`, or `.png`

## Full Hosting configuration example

The following is a full `firebase.json` configuration example for
Firebase Hosting. Note that a `firebase.json` file can also contain
[configurations for other Firebase services](https://firebase.google.com/docs/cli#the_firebasejson_file).

    {
      "hosting": {

        "public": "dist/app",  // "public" is the only required attribute for Hosting

        "ignore": [
          "firebase.json",
          "**/.*",
          "**/node_modules/**"
        ],

        "redirects": [ {
          "source": "/foo",
          "destination": "/bar",
          "type": 301
        }, {
          "source": "/firebase/**",
          "destination": "https://www.firebase.com",
          "type": 302
        } ],

        "rewrites": [ {
          // Shows the same content for multiple URLs
          "source": "/app/**",
          "destination": "/app/index.html"
        }, {
          // Configures a custom domain for Dynamic Links
          "source": "/promos/**",
          "dynamicLinks": true
        }, {
          // Directs a request to Cloud Functions
          "source": "/bigben",
          "function": "bigben"
        }, {
          // Directs a request to a Cloud Run containerized app
          "source": "/helloworld",
          "run": {
            "serviceId": "helloworld",
            "region": "us-central1"
          }
        } ],

        "headers": [ {
          "source": "**/*.@(eot|otf|ttf|ttc|woff|font.css)",
          "headers": [ {
            "key": "Access-Control-Allow-Origin",
            "value": "*"
          } ]
        }, {
          "source": "**/*.@(jpg|jpeg|gif|png)",
          "headers": [ {
            "key": "Cache-Control",
            "value": "max-age=7200"
          } ]
        }, {
          "source": "404.html",
          "headers": [ {
            "key": "Cache-Control",
            "value": "max-age=300"
          } ]
        } ],

        "cleanUrls": true,

        "trailingSlash": false,

        // Required to configure custom domains for Dynamic Links
        "appAssociation": "AUTO",

      }
    }