# Source: https://developers.notion.com/reference/create-a-token

> ## 📘
> For step-by-step instructions on how to use this endpoint to create a public integration, check out the [Authorization guide](https://developers.notion.com/docs/authorization#set-up-the-auth-flow-for-a-public-integration). To walkthrough how to create tokens for Link Previews, refer to the [Link Previews guide](https://developers.notion.com/docs/build-a-link-preview-integration).
> ## 🚧
> Redirect URI requirements for public integrations
> The `redirect_uri` is a _required_ field in the request body for this endpoint if:
>   * the `redirect_uri` query parameter was set in the [Authorization URL](https://developers.notion.com/docs/authorization#step-1-navigate-the-user-to-the-integrations-authorization-url) provided to users, _or_ ;
>   * there are more than one `redirect_uri`s included in the [integration’s settings](https://www.notion.so/my-integrations) under **OAuth Domain & URIs**. 
> 

> In most cases, the `redirect_uri` field is required.
> This field is not allowed in the request body if:
>   * there is one `redirect_uri` included in the [integration’s settings](https://www.notion.so/my-integrations) under **OAuth Domain & URIs**, _and_ the `redirect_uri` query parameter was not included in the Authorization URL.
> 

> Learn more in the public integration section of the [Authorization Guide](https://developers.notion.com/docs/authorization#public-integration-auth-flow-set-up).
_Note: Each Public API endpoint can return several possible error codes. To see a full description of each type of error code, see the[Error codes section](https://developers.notion.com/reference/status-codes#error-codes) of the Status codes documentation._
