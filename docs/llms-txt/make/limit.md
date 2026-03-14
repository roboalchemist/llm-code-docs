# Source: https://developers.make.com/custom-apps-documentation/component-blocks/api/handling-responses/limit.md

# Limit

**Required**: no\
**Default**: unlimited

This directive specifies the maximum number of items that are returned by the module. In a multi-request configuration only the limit of the last request is used, even if it is not specified, because the limit has a default value.

The `limit` directive is also used by pagination logic to determine whether to fetch the next page or not.
