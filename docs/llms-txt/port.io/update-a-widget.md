# Source: https://docs.port.io/api-reference/update-a-widget.md

# Update a widget

```
PATCH 
/v1/pages/:page_identifier/widgets/:widget_id
```

**The Pages API is currently in beta, in its current form it lacks certain validations and protections and it could render your portal unusable if used incorrectly.<br /><br />Please refer to the [Pages overview](/api-reference/pages.md) before using this endpoint.<br /><br />**&#x54;his route allows you to update a specific widget in your portal.<br /><br />To learn more about pages, checkout the [documentation](https://docs.port.io/customize-pages-dashboards-and-plugins/page/catalog-page).

## Request[â](#request "Direct link to Request")

## Responses[â](#responses "Direct link to Responses")

* 200
* 401
* 404
* 413
* 422

Updated successfully

Default Response

A resource with the provided identifier was not found

Request body is too large (limit is 1MiB)

The json provided does not match the route's schema
