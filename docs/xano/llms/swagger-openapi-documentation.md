# Source: https://docs.xano.com/the-function-stack/building-with-visual-development/swagger-openapi-documentation.md

# Source: https://docs.xano.com/the-function-stack/building-with-visual-development/apis/swagger-openapi-documentation.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Swagger/OpenAPI Docs

> Using Swagger/OpenAPI to document your Xano APIs for easy integration.

Xano automatically generates **Swagger/OpenAPI** documentation for your APIs, making it easy to share your endpoints with frontend developers, AI copilots, or third-party services. It's also a quick way to visualize and test your API endpoints.

The API documentation is accessible via a unique URL for each API group, or for an entire workspace. This URL can be shared with anyone who needs to understand or interact with your API. The URLs can also be protected with a token, or disabled entirely.

## Group Level Documentation

From inside of an API group, click <span class="ui-bubble">{ } Swagger Documentation</span> in the top right to access the Swagger/OpenAPI documentation for that specific group.
<img src="https://mintcdn.com/xano-997cb9ee/AXl-sU83thfbeKWS/images/swagger-openapi-documentation-20251208-100959.png?fit=max&auto=format&n=AXl-sU83thfbeKWS&q=85&s=2bb884c0528d42bad2be26f345274f4b" alt="swagger-openapi-documentation-20251208-100959" width="1426" height="203" data-path="images/swagger-openapi-documentation-20251208-100959.png" />

This will open a new tab with the Swagger UI, displaying all the endpoints in that API group, along with details about request parameters, responses, and authentication.
<img src="https://mintcdn.com/xano-997cb9ee/AXl-sU83thfbeKWS/images/swagger-openapi-documentation-20251208-101019.png?fit=max&auto=format&n=AXl-sU83thfbeKWS&q=85&s=ca7c9075043904a7df241c2a027fd120" alt="swagger-openapi-documentation-20251208-101019" width="1403" height="750" data-path="images/swagger-openapi-documentation-20251208-101019.png" />

You can access a downloadable version of your OpenAPI specification in JSON format by selecting the link under the title of the page.
<img src="https://mintcdn.com/xano-997cb9ee/AXl-sU83thfbeKWS/images/swagger-openapi-documentation-20251208-101116.png?fit=max&auto=format&n=AXl-sU83thfbeKWS&q=85&s=bb3fffc320aa72c38b886e93e7b935d9" alt="swagger-openapi-documentation-20251208-101116" width="674" height="274" data-path="images/swagger-openapi-documentation-20251208-101116.png" />

### Documentation settings

From the API group settings, you can configure whether or not the Swagger documentation is enabled, and whether it requires a token to access.
<img src="https://mintcdn.com/xano-997cb9ee/AXl-sU83thfbeKWS/images/swagger-openapi-documentation-20251208-101219.png?fit=max&auto=format&n=AXl-sU83thfbeKWS&q=85&s=3c0a401e315926d929dda2e6f7e9bd62" alt="swagger-openapi-documentation-20251208-101219" width="1429" height="828" data-path="images/swagger-openapi-documentation-20251208-101219.png" />

## Workspace Level Documentation

### First Time Setup

From the API Groups page, click <span class="ui-bubble"><Icon icon="ban" /> Swagger Documentation Disabled</span> in the top right to access the settings. You'll need to select which API groups you want to be made available in your workspace-level documentation.
<img src="https://mintcdn.com/xano-997cb9ee/AXl-sU83thfbeKWS/images/swagger-openapi-documentation-20251208-101351.png?fit=max&auto=format&n=AXl-sU83thfbeKWS&q=85&s=828935223e27569d122aeb90fa72a3ee" alt="swagger-openapi-documentation-20251208-101351" width="1434" height="402" data-path="images/swagger-openapi-documentation-20251208-101351.png" />

At the bottom of the panel, select the desired option to enable the documentation (public or requires token), and use the check boxes to select which API groups to include.
<img src="https://mintcdn.com/xano-997cb9ee/AXl-sU83thfbeKWS/images/swagger-openapi-documentation-20251208-101457.png?fit=max&auto=format&n=AXl-sU83thfbeKWS&q=85&s=dcb539a138b0e3b9d9cedd3b11b7bb49" alt="swagger-openapi-documentation-20251208-101457" width="1198" height="558" data-path="images/swagger-openapi-documentation-20251208-101457.png" />

### Accessing the Documentation

Once first-time setup is complete, you can access the workspace-level Swagger/OpenAPI documentation by clicking <span class="ui-bubble">{ } Swagger Documentation</span> in the top right of the API Groups page.
<img src="https://mintcdn.com/xano-997cb9ee/AXl-sU83thfbeKWS/images/swagger-openapi-documentation-20251208-101526.png?fit=max&auto=format&n=AXl-sU83thfbeKWS&q=85&s=95bd08cd6bc6476f155fa7dd31b7e372" alt="swagger-openapi-documentation-20251208-101526" width="1423" height="1188" data-path="images/swagger-openapi-documentation-20251208-101526.png" />

## API Level Documentation

You can also access Swagger/OpenAPI documentation for individual API endpoints. From inside an API, click the <span class="ui-bubble">{ }</span> icon to view documentation specific to that endpoint.
<img src="https://mintcdn.com/xano-997cb9ee/AXl-sU83thfbeKWS/images/swagger-openapi-documentation-20251208-101625.png?fit=max&auto=format&n=AXl-sU83thfbeKWS&q=85&s=ad9f87e0a0c9aa3e45696ac686071f2e" alt="swagger-openapi-documentation-20251208-101625" width="1427" height="354" data-path="images/swagger-openapi-documentation-20251208-101625.png" />

## Using the Documentation

<Frame>
  <iframe src="https://demo.arcade.software/QDBGCvxr0Jf6Fq6Uqtar?embed" title="https://demo.arcade.software/QDBGCvxr0Jf6Fq6Uqtar?embed" allowFullScreen allow="clipboard-write" class="contentkit-webframe" />
</Frame>

<Steps>
  <Step title="Review the API information shown.">
    Each API will show you the method, the API name, and the description on the left side.

    <Frame>
      <img src="https://mintcdn.com/xano-997cb9ee/rOuOq7qlTNyaIMAW/images/574845da-image.jpeg?fit=max&auto=format&n=rOuOq7qlTNyaIMAW&q=85&s=6847a24a0aeb88c40e36d1ac319c8984" width="431" height="62" data-path="images/574845da-image.jpeg" />
    </Frame>

    On the right, you'll see a 🔓 icon if that API requires authentication.

    <Frame>
      <img src="https://mintcdn.com/xano-997cb9ee/dC3SQWgPCF_-1qn6/images/2bacfc4a-image.jpeg?fit=max&auto=format&n=dC3SQWgPCF_-1qn6&q=85&s=8afdac45d3ea2f248333084b860eba5c" width="403" height="67" data-path="images/2bacfc4a-image.jpeg" />
    </Frame>

    Click the `V` to interact with your API of choice.
  </Step>

  <Step title="Sending Authenticated Requests">
    If any of the API(s) you want to interact with require authentication, click <img src="https://mintcdn.com/xano-997cb9ee/rOuOq7qlTNyaIMAW/images/5c797444-image.jpeg?fit=max&auto=format&n=rOuOq7qlTNyaIMAW&q=85&s=12848d510dffaa1d9d66e7294bf33b54" width="197" height="49" data-path="images/5c797444-image.jpeg" /> at the top of the page to supply an authentication token.
  </Step>

  <Step title="Click 'Try it out' to send a request to that API.">
    <Frame>
      <img src="https://mintcdn.com/xano-997cb9ee/p57kHPQ04p_0aEqF/images/b502df4b-image.jpeg?fit=max&auto=format&n=p57kHPQ04p_0aEqF&q=85&s=eba21ba620620ba4ab4b2dda7689fa3d" width="198" height="46" data-path="images/b502df4b-image.jpeg" />
    </Frame>
  </Step>

  <Step title="Fill in any request body values or parameters necessary.">
    <Frame>
      <img src="https://mintcdn.com/xano-997cb9ee/ClU5W_-qt6GI3QWZ/images/459c1ff9-image.jpeg?fit=max&auto=format&n=ClU5W_-qt6GI3QWZ&q=85&s=6ea7b0815c9e87c2348b22c2eb1254c6" width="624" height="536" data-path="images/459c1ff9-image.jpeg" />
    </Frame>
  </Step>

  <Step title="Click 'Execute' to send the test request.">
    <Frame>
      <img src="https://mintcdn.com/xano-997cb9ee/o7zunZFYmjx8RZ8N/images/f44d5d22-image.jpeg?fit=max&auto=format&n=o7zunZFYmjx8RZ8N&q=85&s=969bd1fbc3e1a7ae0e8dc93a634a881f" width="129" height="34" data-path="images/f44d5d22-image.jpeg" />
    </Frame>

    You can review the response given below.

    <Frame>
      <img src="https://mintcdn.com/xano-997cb9ee/-vy8_DWVOwkWo8Bt/images/7f1c00b4-image.jpeg?fit=max&auto=format&n=-vy8_DWVOwkWo8Bt&q=85&s=512c0b54f09e29a2effd4300e5a4e81b" width="1753" height="593" data-path="images/7f1c00b4-image.jpeg" />
    </Frame>
  </Step>
</Steps>

## Additional Features

### Defining Sample Inputs and Responses

<Tip>
  **Note**

  We're currently rolling out this feature to all users as part of our next release. If you don't have it yet, you will soon! Hang tight.
</Tip>

When [testing your function stacks](/testing-debugging/testing-and-debugging-function-stacks) in Xano, you can define sample input and output examples for your Swagger documentation.

It is important that you do this to ensure that your documentation is as effective as possible, as well as for helping AI models understand what's expected when interacting with your APIs.

<Steps>
  <Step title="In the 'response' section of the Run panel, click Set As Example">
    <Frame>
      <img src="https://mintcdn.com/xano-997cb9ee/kBkSb_XZ48XRxJA_/images/a3c4ebc7-image.jpeg?fit=max&auto=format&n=kBkSb_XZ48XRxJA_&q=85&s=8d8e78274928ca9c7cd09a8b5ca37975" width="642" height="312" data-path="images/a3c4ebc7-image.jpeg" />
    </Frame>
  </Step>

  <Step title="Review the sample input and response, and make any necessary adjustments">
    <Warning>
      Make sure these do not include any sensitive information.
    </Warning>

    <Frame>
      <img src="https://mintcdn.com/xano-997cb9ee/_FyaEhYRFYQZinJ0/images/df1910c3-image.jpeg?fit=max&auto=format&n=_FyaEhYRFYQZinJ0&q=85&s=fd42faaa2cc429800cd1ea1dfeb5cc53" width="774" height="908" data-path="images/df1910c3-image.jpeg" />
    </Frame>
  </Step>

  <Step title="Click Save and you will see these defined in your Swagger documentation.">
    <Frame>
      <img src="https://mintcdn.com/xano-997cb9ee/_Sd90ZcMa6hsPScv/images/d3752a34-image.jpeg?fit=max&auto=format&n=_Sd90ZcMa6hsPScv&q=85&s=a04294b4063e73fb62b3f37222f2abf7" width="1426" height="995" data-path="images/d3752a34-image.jpeg" />
    </Frame>

    If you need to make adjustments later, you can do so from the settings menu.

    <Frame>
      <img src="https://mintcdn.com/xano-997cb9ee/rOuOq7qlTNyaIMAW/images/58f13ba2-image.jpeg?fit=max&auto=format&n=rOuOq7qlTNyaIMAW&q=85&s=7a0c09cd20fe99036fd1fe2920772911" width="586" height="364" data-path="images/58f13ba2-image.jpeg" />
    </Frame>
  </Step>
</Steps>

### Copy / Copy as cURL

Throughout the documentation, you'll see <img src="https://mintcdn.com/xano-997cb9ee/Zmn_DUDgqMkazo6J/images/e5eabd60-image.jpeg?fit=max&auto=format&n=Zmn_DUDgqMkazo6J&q=85&s=b0a4f5816ea2da2ad4e5c0176c6a9464" className="inline m-0" width="27" height="29" data-path="images/e5eabd60-image.jpeg" /> icons. These will let you quickly copy the contents of that element, and in the presence of a cURL command, copy that command to quickly paste into a terminal or other API / testing platform of choice, such as [Postman](https://www.postman.com/).

### JSON OpenAPI Spec

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/WBQXG-4Ngk82eYAW/images/ff9c8a88-image.jpeg?fit=max&auto=format&n=WBQXG-4Ngk82eYAW&q=85&s=67801506f4eb3d61fa6899475d2003d1" width="290" height="114" data-path="images/ff9c8a88-image.jpeg" />
</Frame>

You can click the link at the top of the page to access a JSON-formatted version of your API spec. This is useful for other external platforms that rely on this type of standardized information about your APIs or providing to AI chatbots / LLMs.


Built with [Mintlify](https://mintlify.com).