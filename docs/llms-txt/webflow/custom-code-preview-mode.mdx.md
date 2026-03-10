# Source: https://developers.webflow.com/data/docs/custom-code-preview-mode.mdx

***

title: Supporting custom code in preview mode
slug: data/docs/custom-code-preview-mode
description: Configure your app's hosted resources to work with Webflow's preview mode
'og:title': Supporting Custom Code in Preview Mode
'og:description': Enable your app's resources to work in Webflow's preview mode
-------------------------------------------------------------------------------

Users can preview sites with custom code before publishing. When users add your app's scripts or resources as custom code, these resources need to be accessible from Webflow's preview domain.

## How preview mode works

When a user enables [preview](https://webflow.com/glossary/preview-mode) or [comment](https://help.webflow.com/hc/en-us/articles/33961339882131-Comments) mode, their site renders on a new subdomain:

```
{shortName}.canvas.webflow.com
```

This creates a secure, isolated environment that closely mirrors the published site experience, where custom code scripts can execute safely.

## Important considerations for custom code

If your custom code scripts implement specific security controls, they may need modification to work in preview and comment modes.

### What needs to be updated?

Your custom code scripts may need updates if they implement any of the following security controls:

* [Content-Security-Policy (CSP)](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Content-Security-Policy) restrictions
* [Domain-based script or stylesheet restrictions](https://developer.mozilla.org/en-US/docs/Web/Security/Same-origin_policy)
* [Origin or Referrer header validation](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Referrer-Policy)

### Required modifications

#### For scripts with domain restrictions

If your scripts check for specific domains or origins, update domain validation to include preview domains:

```javascript
// Update domain validation to include preview domains
const isAllowedDomain = (domain) => {
    return domain.endsWith('.webflow.io') ||
           domain.endsWith('.canvas.webflow.com');
}
```

#### For scripts that validate origins

If your scripts validate request origins, update origin validation to include preview domains:

```javascript
// Example of updated origin validation
const validateOrigin = (origin) => {
    return origin.includes('.webflow.io') ||
           origin.includes('.canvas.webflow.com');
}
```

#### For dynamic domain detection

If your scripts need to detect the current environment, update domain detection to include preview domains:

```javascript
const shortName = window.location.hostname.split('.')[0];
const isPreviewMode = window.location.hostname.includes('canvas.webflow.com');
```

### Testing your custom code

To ensure your custom code works correctly:

1. Add your custom code to a site or page
2. Enter preview mode to test functionality
3. Verify that all interactive elements work as expected
4. Check that any external service connections still function properly

## Support resources

For implementation assistance or questions, please contact us at [developers@webflow.com](mailto:developers@webflow.com?subject=Support:%20Custom%20Code%20-%20Preview%20and%20Comment%20mode).
