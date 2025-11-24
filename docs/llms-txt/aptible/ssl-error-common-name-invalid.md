# Source: https://www.aptible.com/docs/how-to-guides/troubleshooting/common-errors-issues/ssl-error-common-name-invalid.md

# SSL error ERR_CERT_COMMON_NAME_INVALID

## Cause and Resolution

This error usually indicates one of two things:

* You created a CNAME to an [Endpoint](/core-concepts/apps/connecting-to-apps/app-endpoints/overview) configured to use a [Default Domain](/core-concepts/apps/connecting-to-apps/app-endpoints/default-domain). That won't work; use a [Custom Domain](/core-concepts/apps/connecting-to-apps/app-endpoints/custom-domain) instead.

* The [Custom Certificate](/core-concepts/apps/connecting-to-apps/app-endpoints/custom-certificate) you provided for your Endpoint is not valid for the [Custom Domain](/core-concepts/apps/connecting-to-apps/app-endpoints/custom-domain) you're using. Get a valid certificate for the domain.
