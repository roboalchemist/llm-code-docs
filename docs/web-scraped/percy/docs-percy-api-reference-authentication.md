# Source: https://www.browserstack.com/docs/percy/api-reference/authentication

# Authentication
The Percy API is based on theJSONAPI standard and organized around theRESTdesign.

[JSON](https://jsonapi.org/)[REST](https://developer.mozilla.org/en-US/docs/Glossary/REST)Note:API base URLhttps://percy.io/api/v1

`https://percy.io/api/v1`The Percy API uses API tokens to authenticate. They are passed in asHTTPAuthorizationrequest headers.

[HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Authorization)`Authorization`Note:Authorization header formatAuthorization: Token ${PERCY_TOKEN}

`Authorization: Token ${PERCY_TOKEN}`Percy currently authenticates with three project token types:

| Write-only | Read-only | Full-access |
| Create builds | Read builds |  |
| Create snapshots | Download snapshots | All project read and write functions |
| SDK use | API use |  |

[SDK use](https://www.browserstack.com/docs/percy/integrate/overview)The tokens for a particular project can be found on its Project Settings page.

#### We're sorry to hear that. Please share your feedback so we can do better
Contact ourSupport teamfor immediate help while we work on improving our docs.

[Support team](https://www.browserstack.com/support)
#### We're continuously improving our docs. We'd love to know what you liked
- This page has exactly what I am looking for
- This content & code samples are accurate and up-to-date
- The content on this page is easy to understand
- Other (please tell us more below)
Thank you for your valuable feedback