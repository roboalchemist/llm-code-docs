# Source: https://smartcar.com/docs/connect/connect-sdks.md

> ## Documentation Index
> Fetch the complete documentation index at: https://smartcar.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# SDKs for Connect

> Our SDKs make integrating Smartcar fast and easy in different languages and frameworks.

For mobile or single page web apps, you can use one of our frontend SDKs. Please note that our frontend SDKs only handle
integrating Connect into your application. You will still need to use a [backend SDK](/api-reference/api-sdks) to manage tokens and make API requests to vehicles.

<Snippet file="sdks/connect-sdk-card-group.mdx" />

<Note>**Note:** In addition to using a frontend SDK to integrate with Smartcar Connect, a backend SDK is strongly recommended to securely manage tokens, receive data from Smartcar, and make API requests to issue commands to vehicles. The backend SDK facilitates authentication, token exchange, and all communication with Smartcar’s APIs.</Note>

For server-side rendered applications, you can use one of our backend SDKs:

<Snippet file="sdks/api-sdk-card-group.mdx" />

<br />

<Tip>
  Don't see an SDK for your language? No problem!
  As long as you can build a URL and handle HTTP requests, you're good to go.
</Tip>
