# Source: https://www.aptible.com/docs/how-to-guides/troubleshooting/common-errors-issues/ssl-error-auth-invalid.md

# SSL error ERR_CERT_AUTHORITY_INVALID

## Cause

This error is usually caused by neglecting to include CA intermediate certificates when you upload a [Custom Certificate](/core-concepts/apps/connecting-to-apps/app-endpoints/custom-certificate) to Aptible.

## Resolution

Include CA intermediate certificate in your certificate bundle. See [Custom Certificate](/core-concepts/apps/connecting-to-apps/app-endpoints/custom-certificate) for instructions.
