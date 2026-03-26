# Source: https://docs.socket.dev/reference/api-lifecycle-and-deprecation-process.md

# API Lifecycle and Deprecation Process

Socket sometimes needs to deprecate or replace API endpoints with new ones. We offer a number of tools and channels to help notify and migrate customers to new endpoints.

## Deprecation Process

When Socket deprecates an API endpoint, you'll be notified through multiple channels:

### API Documentation Updates

* Deprecated endpoints are marked with a `deprecated` tag in our API documentation
* Documentation includes links to the replacement endpoint
* Deprecation headers are sent to clients making requests to deprecated endpoints
* These may also be supplemented with email notifications, blog posts or account manager outreach.

### HTTP Response Headers

All requests to deprecated endpoints include standard HTTP headers:

* **Deprecation** (per [RFC 8594](https://www.rfc-editor.org/rfc/rfc8594.html)): Indicates the endpoint is deprecated
* **Link Headers** (per [RFC 8288](https://www.rfc-editor.org/rfc/rfc8288.html)):
  * `deprecation`: Links to deprecation information
  * `successor-version`: Links to the replacement endpoint
  * `alternate`: Links to alternative endpoints

These headers allow your application to programmatically detect deprecated endpoints and plan migrations accordingly.

### Socket SDK Updates

Socket's official SDKs and libraries are updated to use new endpoints after deprecation, ensuring you benefit from the latest API improvements when you upgrade. Updating to the latest SDK will sometimes offer migration paths to the new endpoints, though sometimes it will require changes on your part as well.

## Endpoint Sunset

Before an endpoint is fully decommissioned, Socket adds the **Sunset header** per [RFC 8594](https://www.rfc-editor.org/rfc/rfc8594.html) to all responses. This header indicates the date when the endpoint will stop functioning, giving you time to complete your migration.

### Migration Timeline

Sunset timelines are determined based on:

* Customer impact and migration readiness
* Complexity of the migration path
* Infrastructure considerations

Socket strives to provide adequate notice before sunsetting endpoints to minimize disruption to your integrations.

## Best Practices for API Consumers

To stay ahead of API changes:

1. **Monitor HTTP headers**: Check for `Deprecation` and `Sunset` headers in API responses
2. **Review API documentation regularly**: Stay informed about deprecated and new endpoints
3. **Keep SDKs updated**: Use the latest versions of Socket's official SDKs
4. **Plan migrations early**: Don't wait until an endpoint is sunset to begin migration

## Standards Compliance

Socket follows these RFCs for API lifecycle management:

* [RFC 8594](https://www.rfc-editor.org/rfc/rfc8594.html) - Sunset HTTP Header (for endpoint decommissioning dates)
* [RFC 8594](https://www.rfc-editor.org/rfc/rfc8594.html) - Deprecation HTTP Header (for deprecated endpoints)

This ensures compatibility with industry-standard API lifecycle tools and practices.

## Support

If you have questions about API deprecations or need migration assistance, please contact Socket support.