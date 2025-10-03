# Source: https://developers.notion.com/reference/get-users

Returns a paginated list of [Users](https://developers.notion.com/reference/user) for the workspace. The response may contain fewer than `page_size` of results.
Guests are not included in the response.
See [Pagination](https://developers.notion.com/reference/intro#pagination) for details about how to use a cursor to iterate through the list.
### [](https://developers.notion.com/reference/get-users#errors)
Each Public API endpoint can return several possible error codes. See the [Error codes section](https://developers.notion.com/reference/status-codes#error-codes) of the Status codes documentation for more information.
> ## 📘
> The API does not currently support filtering users by their email and/or name.
> ## 📘
> Integration capabilities
> This endpoint requires an integration to have user information capabilities. Attempting to call this API without user information capabilities will return an HTTP response with a 403 status code. For more information on integration capabilities, see the [capabilities guide](https://developers.notion.com/reference/capabilities).
