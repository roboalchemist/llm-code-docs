# Source: https://docs.upsun.com/environments/search-engine-visibility.md

# Set an environment's visibility to search engines

When you have preview environments,
you don't want search engines indexing them and diluting the SEO of your production site.

Search engine indexers are told to ignore all preview environments.
When you're ready to go live, give your production environment a [custom domain](https://docs.upsun.com../domains/steps.md)
and then set it to be visible to search engines.

To change your production environment's visibility to search engines, follow these steps:

 - Select the project where you want to change visibility.
 - From the **Environment** menu, select your production environment.
 - Click Settings **Settings**.
 - In the row with **Hide from search engines**, click **Edit **.
 - Select or clear the **Hide from search engines** checkbox.

Upsun can't guarantee that indexers follow the instructions.
If you're concerned about access, set up [HTTP access control](https://docs.upsun.com/environments/http-access-control.md).

## How it's done

When the **Hide from search engines** is activated,
search engines are turned away from environments by including a `X-Robots-Tag` header:

```txt
X-Robots-Tag: noindex, nofollow
```

That tells search engine indexers to not index these sites and not traverse links from these sites.
This helps keep non-Production sites out of search engine indexes.

It's automatically on for all `upsun.site` domains, and it's automatically off for production environments with a custom domain.

## Alternative method

You can also send instructions to search engine indexers using a `robots.txt` file.
Your app can serve this as a static file from its disk or as a dynamic response from its `passthru`.
Control either with the [`location` section of your app configuration](https://docs.upsun.com/create-apps/image-properties/web.md#locations).

If your `robots.txt` file includes instructions to ignore a page,
search engine indexers may ignore it even if you have configured Upsun to not send the header.

