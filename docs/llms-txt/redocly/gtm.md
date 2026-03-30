# Source: https://redocly.com/docs/realm/config/analytics/gtm.md

# Google Tag Manager analytics

Integrate Google Tag Manager into Redocly project.

## Configuration

| Option | Type | Description |
|  --- | --- | --- |
| includeInDevelopment | boolean | Set this option to `true` to enable GTM Analytics in development mode and preview builds.
Default is `false`. |
| trackingId | string | **REQUIRED**GTM tracking ID |
| gtmAuth | string | GTM environment auth string |
| gtmPreview | string | GTM environment preview name |
| defaultDataLayer | object | Arbitrary datalayer object to be set before GTM is loaded |
| dataLayerName | string | Name of GTM datalayer |
| enableWebVitalsTracking | boolean | Enable web vitals tracking |
| selfHostedOrigin | string | Set this for custom GTM server hosting |
| pageViewEventName | String | Set this option to change the event name for page views.
Default is `pageView`. |


## Example


```yaml
analytics:
  gtm:
    includeInDevelopment: true
    trackingId: my-tracking-id
    gtmAuth: my-gtm-auth-string
    gtmPreview: my-gtm-preview-name
    defaultDataLayer:
      platform: redocly
    dataLayerName: my-data-layer-name
    enableWebVitalsTracking: true
    selfHostedOrigin: http://my-gtm-server-host.com
    pageViewEventName: routeChange
```