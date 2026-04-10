# Source: https://dub.co/docs/sdks/client-side/features/cross-domain-tracking.md

> ## Documentation Index
> Fetch the complete documentation index at: https://dub.co/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Cross-domain tracking

> Track conversions across domains

By default, the script already sets the `dub_id` cookie on a **cross-domain level**.

This means that if you have the script installed on your marketing site (e.g. **example.com**), the cookie will also be accessible when your user signs up for your app (e.g. **app.example.com**).

However, if you are installing the script on a subdomain (e.g. **app.example.com**), you will need to set the following option to make sure the cookie is accessible on the apex domain as well (e.g. **example.com**):

<CodeGroup>
  ```typescript React theme={null}
  <DubAnalytics
    cookieOptions={{
      domain: ".example.com",
    }}
  />
  ```

  ```html Other theme={null}
  <script
    src="https://www.dubcdn.com/analytics/script.js"
    data-cookie-options='{"domain": ".example.com"}'
  ></script>
  ```
</CodeGroup>

The script also supports conversion tracking across *entirely different domains*.

This means that if you have the script installed on a separate domain (e.g. **example.sh**), you can use the `outboundDomains` prop to ensure that the `dub_id` cookie value is automatically appended to all outbound links targeting your main domain (e.g. **example.com**).

<CodeGroup>
  ```typescript React theme={null}
  // install this script on both domains
  <DubAnalytics
    domainsConfig={{
      outbound: ["example.com", "example.sh"],
    }}
  />
  ```

  ```html Other theme={null}
  <script
    src="https://www.dubcdn.com/analytics/script.outbound-domains.js"
    data-domains="{'outbound': ['example.com', 'example.sh']}"
  ></script>
  ```
</CodeGroup>

<Tip>
  For outbound-domains support, you'll need to use the
  [`script.outbound-domains.js`](/sdks/client-side/variants#outbound-domains-variant-script-outbound-domains-js)
  variant of the script. Learn more about [how script variants
  work](/sdks/client-side/variants).
</Tip>
