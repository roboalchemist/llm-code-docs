# Source: https://developers.notion.com/reference/get-self

Retrieves the bot [User](/reference/user) associated with the API token provided in the authorization header. The bot will have an `owner` field with information about the person who authorized the integration.
### Errors
Each Public API endpoint can return several possible error codes. See the [Error codes section](/reference/status-codes#error-codes) of the Status codes documentation for more information.
> ##
>
> Integration capabilities
>
> This endpoint is accessible from by integrations with any level of capabilities. The [user object](/reference/user) returned will adhere to the limitations of the integration's capabilities. For more information on integration capabilities, see the [capabilities guide](/reference/capabilities).