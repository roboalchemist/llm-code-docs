# Source: https://docs.logrocket.com/reference/roothostname.md

# Track Sessions Across Subdomains

Control how LogRocket records across subdomains of your website

## Capture traffic from all subdomains under one session

#### `rootHostname` - String

##### optional (default - `null`)

Use this option to control whether sessions that traverse different subdomains on your site are kept intact or broken up into sessions specific to each subdomain. Set this to the highest-level hostname sessions should be shared across (e.g., `example.com` or `shared.example.com`). Leave it unspecified if you want a different session per subdomain. A leading period is required.

```javascript Specify the root hostname
LogRocket.init(YOUR_APP_ID, {
  rootHostname: '.example.com',
});
```