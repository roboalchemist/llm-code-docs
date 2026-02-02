# Source: https://dub.co/docs/sdks/client-side/installation-guides/react.md

## React

How to add the @dub/analytics client-side script to your React website

With Dub Analytics, you can track lead and sale conversions on your website, enabling you to measure the effectiveness of your marketing campaigns.

## Quickstart

This quick start guide will show you how to get started with Dub Analytics on your website.

### Install package

Using the package manager of your choice, add the `@dub/analytics` to your project.

```bash
# npm
npm install @dub/analytics

# pnpm
pnpm add @dub/analytics

# yarn
yarn add @dub/analytics

# bun
bun add @dub/analytics
```

### Initialize package in your code

If you are using a React framework, you can use the `<Analytics />` component to track conversions on your website.

E.g., if you're using Next.js, you can add the `<Analytics />` component to your root layout component or any other pages where you want to track conversions.

```jsx
import { Analytics as DubAnalytics } from '@dub/analytics/react';

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body>{children}</body>
      <DubAnalytics />
    </html>
  );
}
```

### Optional: Set up client-side click tracking

If you're using [Dub Partners](/partners/quickstart) for affiliate management, you will also need to set up the `domainsConfig.refer` property to enable [client-side click-tracking](/sdks/client-side/features/click-tracking).

```jsx
import { Analytics as DubAnalytics } from '@dub/analytics/react';

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body>{children}</body>
      <DubAnalytics domainsConfig={{
        refer: "yourcompany.link"
      }}>
    </html>
  );
}
```

Read the [client-side click-tracking guide](/sdks/client-side/features/click-tracking) for more information.

You can **verify the installation** with the following tests:

1. Open the browser console and type in `_dubAnalytics` – if the script is installed correctly, you should see the `_dubAnalytics` object in the console.
2. Add the `?dub_id=test` query parameter to your website URL and make sure that the `dub_id` cookie is being set in your browser.

If both of these checks pass, the script is installed correctly. Otherwise, please make sure:

- The analytics script was added to the `<head>` section of the page
- If you're using a content delivery network (CDN), make sure to purge any cached content

## Concepts

You can pass the following props to the `<Analytics />` component to customize its behavior:

- **Api Host**: The base URL for the Dub API. This is useful for [setting up reverse proxies](/sdks/client-side/features/reverse-proxy-support) to avoid adblockers.

- **Attribution Model**: The attribution model to use for the analytics event. The following attribution models are available:
  - `First Click`: Gives all the credit to the first touchpoint in the customer journey.
  - `Last Click`: Gives all the credit to the last touchpoint in the customer journey.

- **Cookie Options**:
  - **Domain**: Specifies the value for the `Domain` Set-Cookie attribute. This is useful for cross-domain tracking. Example: `.example.com`
  - **Expires**: Specifies the `Date` object to be the value for the `Expires` Set-Cookie attribute. Example: `new Date('2024-12-31')`
  - **Expires In Days**: Specifies the number (in days) to be the value for the `Expires` Set-Cookie attribute. Example: `90`
  - **Path**: Specifies the value for the `Path` Set-Cookie attribute. By default, the path is considered the "default path". Example: `/`

- **Domains Config**: Configure the domains that Dub will track. The following properties are available:
  - **Refer**: The Dub custom domain for [referral program client-side click tracking](http://d.to/clicks/refer) (previously `shortDomain`). Example: `refer.dub.co`
  - **Site**: The Dub short domain for tracking site visits. Example: `site.dub.co`
  - **Outbound**: An array of domains for cross-domain tracking. When configured, the existing `dub_id` cookie will be automatically appended to all outbound links targeting these domains to enable cross-domain tracking across different applications. Example: `["dub.sh", "git.new"]`

- **QueryParams**: Configure the query parameters to listen to for client-side click-tracking (e.g., `?via=abc123`).

- **Script Props**: Custom properties to pass to the script tag. Refer to [MDN](https://developer.mozilla.org/en-US/docs/Web/API/HTMLScriptElement) for all available options.