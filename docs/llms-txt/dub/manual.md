# Source: https://dub.co/docs/sdks/client-side/installation-guides/manual.md

# Manual Installation

> How to add the @dub/analytics client-side script to your website

With `@dub/analytics`, you can track lead and sale conversions on your website, enabling you to measure the effectiveness of your marketing campaigns.

You can add the `@dub/analytics` script to your website same way you would add Google Analytics script or any other JavaScript code – by adding the `@dub/analytics` script in the `<head>` section of your HTML file.

```html  theme={null}
<script src="https://www.dubcdn.com/analytics/script.js" defer></script>
```

If you're using [Dub Partners](/partners/quickstart) for affiliate management, you will also need to set up the `data-domains` property to enable [client-side click-tracking](/sdks/client-side/features/click-tracking).

```html  theme={null}
<script
  src="https://www.dubcdn.com/analytics/script.js"
  defer
  data-domains='{"refer":"yourcompany.link"}' // replace with your referral link domain on Dub
></script>
```

Read the [client-side click-tracking guide](/sdks/client-side/features/click-tracking) for more information.

<Check>
  You can **verify the installation** with the following tests:

  1. Open the browser console and type in `_dubAnalytics` – if the script is installed correctly, you should see the `_dubAnalytics` object in the console.
  2. Add the `?dub_id=test` query parameter to your website URL and make sure that the `dub_id` cookie is being set in your browser.

  If both of these checks pass, the script is installed correctly. Otherwise, please make sure:

  * The analytics script was added to the `<head>` section of the page
  * If you're using a content delivery network (CDN), make sure to purge any cached content
</Check>

## Concepts

You can pass the following props to the `@dub/analytics` script to customize its behavior:

<ParamField body="data-api-host" type="url" default="https://api.dub.co">
  The base URL for the Dub API. This is useful for [setting up reverse
  proxies](/sdks/client-side/features/reverse-proxy-support) to avoid
  adblockers.
</ParamField>

<ParamField body="data-attribution-model" type="first-click | last-click" default="last-click">
  The attribution model to use for the analytics event. The following
  attribution models are available:

  * `first-click`: The first click model
    gives all the credit to the first touchpoint in the customer journey.
  * `last-click`: The last click model gives all the credit to the last
    touchpoint in the customer journey.
</ParamField>

<ParamField body="data-cookie-options" type="JSON-stringified object">
  Custom properties to pass to the cookie. Refer to
  [MDN's Set-Cookie documentation](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie) for
  all available options.

  <Expandable title="properties">
    <ParamField body="domain" type="string">
      Specifies the value for the `Domain` Set-Cookie attribute. This is useful
      for cross-domain tracking. Example: `.example.com`
    </ParamField>

    <ParamField body="expires" type="integer" default="90">
      Specifies the `Date` object to be the value for the `Expires` Set-Cookie
      attribute. Example: `new Date('2024-12-31')`
    </ParamField>

    <ParamField body="expiresInDays" type="integer" default="90">
      Specifies the number (in days) to be the value for the `Expires`
      Set-Cookie attribute.

      For example, to set the cookie window to 60 days (instead of the default 90 days), you can add the following to your script:

      ```html  theme={null}
      <script
        src="https://www.dubcdn.com/analytics/script.js"
        defer
        data-cookie-options='{"expiresInDays": 60}'
      ></script>
      ```
    </ParamField>

    <ParamField body="path" type="string" default="/">
      Specifies the value for the `Path` Set-Cookie attribute. By default, the
      path is considered the "default path". Example: `/`
    </ParamField>
  </Expandable>
</ParamField>

<ParamField body="data-domains" type="JSON-stringified object">
  Configure the domains that Dub will track. The following properties are available:

  <Expandable title="properties">
    <ParamField body="refer" type="string">
      The Dub custom domain for [referral program client-side click tracking](http://d.to/clicks/refer) (previously `data-short-domain`).
      Example: `refer.dub.co`
    </ParamField>

    <ParamField body="site" type="string">
      The Dub short domain for tracking site visits.
      Example: `site.dub.co`
    </ParamField>

    <ParamField body="outbound" type="string | string[]">
      An array of domains for cross-domain tracking. When configured, the existing `dub_id` cookie
      will be automatically appended to all outbound links targeting these domains to enable
      cross-domain tracking across different applications.
      Example: `"dub.sh, git.new"`
    </ParamField>
  </Expandable>
</ParamField>

<ParamField body="data-query-params" type="string[]" default="[&#x22;via&#x22;]">
  An array of query parameters to listen to for client-side click-tracking (e.g.
  `?via=abc123`).
</ParamField>
