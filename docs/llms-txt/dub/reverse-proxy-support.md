# Source: https://dub.co/docs/sdks/client-side/features/reverse-proxy-support.md

# Reverse-proxy support

> Track clicks on the client-side using a reverse proxy

## Tracking clicks via a reverse proxy

To avoid ad-blockers from blocking your click-tracking requests, we recommend setting up a reverse proxy.

Depending on which backend framework you're using, there are a few different ways to do this:

<CodeGroup>
  ```javascript Next.js theme={null}
  // next.config.js
  module.exports = {
    async rewrites() {
      return [
        {
          source: "/_proxy/dub/track/:path",
          destination: "https://api.dub.co/track/:path",
        },
      ];
    },
  };
  ```

  ```json Vercel theme={null}
  // vercel.json
  {
    "rewrites": [
      {
        "source": "/_proxy/dub/track/:path",
        "destination": "https://api.dub.co/track/:path"
      }
    ]
  }
  ```
</CodeGroup>

Once you've set up your reverse proxy, don't forget to update the `apiHost` parameter in the `<Analytics />` component to point to your proxy URL.

<CodeGroup>
  ```typescript React/Next.js theme={null}
  import { Analytics as DubAnalytics } from "@dub/analytics/react";

  export default function App() {
    return (
      <Layout>
        <DubAnalytics
          apiHost="/_proxy/dub" // the URL of your reverse proxy
          domainsConfig={{
            refer: "go.example.com", // the custom domain you're using on Dub for your short links
          }}
        />
        {/* Your app code here */}
      </Layout>
    );
  }
  ```

  ```javascript Other Frameworks theme={null}
  // include this script tag in your HTML Head tag
  <script
    src="https://www.dubcdn.com/analytics/script.js"
    data-api-host="/_proxy/dub"
    data-domains='{"refer": "go.example.com"}'
    defer
  ></script>
  ```
</CodeGroup>

## Loading the script via a reverse proxy

To avoid ad-blockers from blocking the `@dub/analytics` script, it is recommended to use a reverse proxy.

Depending on which backend framework you're using, there are a few different ways to do this:

<CodeGroup>
  ```javascript Next.js theme={null}
  // next.config.js
  module.exports = {
    async rewrites() {
      return [
        {
          source: "/_proxy/dub/script.js",
          destination: "https://www.dubcdn.com/analytics/script.js",
        },
      ];
    },
  };
  ```

  ```json Vercel theme={null}
  // vercel.json
  {
    "rewrites": [
      {
        "source": "/_proxy/dub/script.js",
        "destination": "https://www.dubcdn.com/analytics/script.js"
      }
    ]
  }
  ```
</CodeGroup>

Once you've set up your reverse proxy, don't forget to update the `scriptProps.src` parameter in the `<Analytics />` component to point to your proxy URL.

<CodeGroup>
  ```typescript React/Next.js theme={null}
  import { Analytics as DubAnalytics } from "@dub/analytics/react";

  export default function App() {
    return (
      <Layout>
        <DubAnalytics
          scriptProps={{
            src: "/_proxy/dub/script.js", // pointing to your reverse proxy
          }}
        />
        {/* Your app code here */}
      </Layout>
    );
  }
  ```

  ```javascript Other Frameworks theme={null}
  // include this script tag in your HTML Head tag
  <script
    src="/_proxy/dub/script.js" // pointing to your reverse proxy
    defer
  ></script>
  ```
</CodeGroup>
