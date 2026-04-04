# Source: https://clickwrap-developer.ironcladapp.com/docs/authentication-2.md

# Authentication (Activity API)

Learn about how authentication works with the Activity API.

Our Activity API does not utilize your REST API Access Token. Instead, it utilizes your Site **Access ID**, which is located within your [Site Settings](https://app.pactsafe.com/settings/account). Your Site Access ID should be added as a URL parameter on every API call to the Activity API.

The site access ID is unique to your Ironclad Clickwrap site and is meant only to help identify your implementation with Ironclad Clickwrap. This means that it can safely be used in client-side implementations and mobile applications.