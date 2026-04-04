# Source: https://docs.logrocket.com/docs/proxying-traffic-through-your-own-domain.md

# Proxy traffic through your own domain

## Proxy Server

If your application runs in an environment where requests to our domain (lrkt-in.com) are blocked, you can set up traffic proxying through your own domain. You can do this with an existing service of your own that's equipped to handle external HTTP requests or by deploying a standalone proxy service that routes these requests to LogRocket.

A CNAME will not proxy traffic to our servers.  You also cannot use a CloudFlare proxy to forward to us at this time.

### CloudFront

We have [documentation available](https://docs.logrocket.com/docs/using-aws-cloudfront-as-a-proxy) for configuring CloudFront in a tested setup.

### Proxy CDN

The first step is to proxy GET requests to the LogRocket CDN. This allows browsers to download the scripts LogRocket needs to run. These GET requests are of the form `https://cdn.logrocket.com/*`. If your domain is `example.com`, you might pass these requests through `https://logrocket-cdn.example.com/*`.

Once your CDN proxy is deployed, use it as follows. If you're using the script version of LogRocket, change the script source as shown below so that it points to your proxy. This isn't necessary if you're using our npm package.

```html
<script src="https://logrocket-cdn.example.com/LogRocket.min.js" crossorigin="anonymous"></script>
```

Regardless of which version of LogRocket you're using (i.e., script or npm), you must tell LogRocket where to download the asynchronous portion of the LogRocket script from. If you're using the script version of LogRocket, this should be done **before** the script is imported. For example:

```html
<script>
  window._lrAsyncScript = 'https://logrocket-cdn.example.com/logger.min.js';
</script>
<script src="https://logrocket-cdn.example.com/LogRocket.min.js" crossorigin="anonymous"></script>
```

If you are using the npm version of LogRocket, this should be done **before** you import LogRocket for the first time. This involves setting a global variable and could be done in the first file that runs in your app.

```html
<head>
  <script>
    window._lrAsyncScript = 'https://logrocket-cdn.example.com/logger.min.js';
  </script>
</head>
```

Make sure import lines can't be hoisted above the variable declaration. For example, don't do this:

```javascript
window._lrAsyncScript = window._lrAsyncScript = 'https://logrocket-cdn.example.com/logger.min.js';

// this gets hoisted above the variable declaration on L1
import LogRocket from 'logrocket';
```

### Proxy Data Ingestion API

The second step is to proxy POST requests to the LogRocket data ingestion API. This allows LogRocket scripts running in the browser to send data back to LogRocket servers. These POST requests are of the form `https://r.logrocket.com/*`. If your domain is `example.com`, you might pass these requests through `https://logrocket-data.example.com/*`.

Once your data ingestion proxy is deployed, make sure it's used by adding the `serverURL` parameter to `LogRocket.init()`.

```javascript
LogRocket.init('YOUR_APPLICATION_ID',{
  serverURL: "https://logrocket-data.example.com/i",
});
```

Requests for LogRocket scripts and data should now be proxied through your backend.