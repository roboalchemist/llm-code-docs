# Source: https://docs.xano.com/the-function-stack/functions/apis-and-lambdas/external-api-request.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# External API Request

## What is an external API request?

The External API Request function is used to send requests to external APIs. You'll use this anytime you want to interact with a third party service, such as a payment platform or email provider.

## Using the External API Request Function

<Steps>
  <Step title="Add an External API Request function">
    &#x9;
  </Step>

  <Step title="Use the AI Assistant to help you build your API request">
    <Steps>
      <Step title="Add an External API Request function to your function stack.">
        This is located inside of the **APIs & Lambdas** category.
      </Step>

      <Step title="Click 'API Request Assistant' from the panel that opens.">
        <Frame>
          <img src="https://mintcdn.com/xano-997cb9ee/Zmn_DUDgqMkazo6J/images/e9d0ad4f-image.jpeg?fit=max&auto=format&n=Zmn_DUDgqMkazo6J&q=85&s=673f8fb2b0902db6b156f379995fa141" width="185" height="34" data-path="images/e9d0ad4f-image.jpeg" />
        </Frame>
      </Step>

      <Step title="Tell the AI Assistant about the API you want to access, and any specifics about the request you want to make.">
        <Frame>
          <img src="https://mintcdn.com/xano-997cb9ee/Zmn_DUDgqMkazo6J/images/e59451d4-image.jpeg?fit=max&auto=format&n=Zmn_DUDgqMkazo6J&q=85&s=2b9fc51f3d81279dd33bccf98576da80" width="594" height="269" data-path="images/e59451d4-image.jpeg" />
        </Frame>
      </Step>

      <Step title="You can either choose to apply the AI's suggestion, or continue to converse with the AI to iterate or make changes.">
        <Frame>
          <img src="https://mintcdn.com/xano-997cb9ee/WBQXG-4Ngk82eYAW/images/fd7abad4-image.jpeg?fit=max&auto=format&n=WBQXG-4Ngk82eYAW&q=85&s=518bca61d0f08a2b3f8b984fd9e67cd7" width="580" height="297" data-path="images/fd7abad4-image.jpeg" />
        </Frame>
      </Step>

      <Step title="For things like API keys, you can either pass them to the AI or fill them in manually after you've applied the suggestion.">
        <Frame>
          <img src="https://mintcdn.com/xano-997cb9ee/dyVYERTquSXdpw_-/images/CleanShot%202025-04-02%20at%2016.00.32.gif?s=7c3138bdf22346262da6577a4a422b66" width="530" height="800" data-path="images/CleanShot 2025-04-02 at 16.00.32.gif" />
        </Frame>
      </Step>
    </Steps>
  </Step>

  <Step title="Or, build the request manually or with a cURL command">
    You can copy cURL commands from API documentation, and paste them using <img src="https://mintcdn.com/xano-997cb9ee/-vy8_DWVOwkWo8Bt/images/861703c7-image.jpeg?fit=max&auto=format&n=-vy8_DWVOwkWo8Bt&q=85&s=bd8f5ca3db5e0a670db1149652683c3b" className="inline m-0" width="131" height="37" data-path="images/861703c7-image.jpeg" />. Xano will build the request for you.

    | Option           | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
    | ---------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | url              | The URL of the API you're calling, such as: `https://api.service.com/send_message`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
    | method           | The verb the API is designed to respond to, such as GET, POST, DELETE, etc...                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
    | params           | Also known as "query parameters", these are options sent along with the request, such as searching and filtering options, or other data that the request needs to execute.<br /><br />You may also see this referred to as **request body**.<br /><br />Hover over the params value space and click **set** to add a new parameter. <img src="https://mintcdn.com/xano-997cb9ee/Zmn_DUDgqMkazo6J/images/ee31cee9-image.jpeg?fit=max&auto=format&n=Zmn_DUDgqMkazo6J&q=85&s=c522baf9e027dfbf8ac8f4ae6c24d91b" width="534" height="91" data-path="images/ee31cee9-image.jpeg" /> |
    | headers          | Any headers you need to send with the request, such as authentication.<br /><br />Add headers by hovering over the value space and click **push**<br /><br /><img src="https://mintcdn.com/xano-997cb9ee/RVHCrB1RJjFkWEmQ/images/0fbdf4f9-image.jpeg?fit=max&auto=format&n=RVHCrB1RJjFkWEmQ&q=85&s=3dfdfeeb69f0a7f7a711ad0b7f43e936" width="529" height="86" data-path="images/0fbdf4f9-image.jpeg" />                                                                                                                                                                        |
    | timeout          | How long Xano should allow the request to take before considering it timed out (failed)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
    | follow\_location | Determines if you wish to automatically follow the redirects (if there are any) in the API call.An example of this would be an API that generates a file for you, then gives you a redirect to get that file.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
  </Step>
</Steps>

## Understanding API Documentation

<Steps>
  <Step title="Start by evaluating the four key sections that almost every API documentation has.">
    The Getting Started guide is your entry point - it typically covers the basics of authentication, shows a simple example request, and helps you make your first API call successfully.

    The Authentication section explains how to get your API keys and how to include them in your requests. This is crucial since you'll need this working before you can try anything else.

    The API Reference details every possible endpoint and operation. Don't try to read this cover-to-cover. Instead, find the specific endpoint that matches what you're trying to do, then study its parameters, required headers, and example responses.

    The Examples/Tutorials section often has complete code snippets showing common use cases. These are invaluable for seeing how different API calls work together to accomplish a task.
  </Step>

  <Step title="Finding the endpoint(s) you need">
    When you find the endpoint you need, focus on three things:

    1. What URL you'll be calling

    2. What parameters or data you need to send

    3. What the response will look like

    Most API documentation also includes **cURL commands**, which you can copy and paste right into Xano by clicking <img src="https://mintcdn.com/xano-997cb9ee/-vy8_DWVOwkWo8Bt/images/861703c7-image.jpeg?fit=max&auto=format&n=-vy8_DWVOwkWo8Bt&q=85&s=bd8f5ca3db5e0a670db1149652683c3b" className="inline m-0" width="131" height="37" data-path="images/861703c7-image.jpeg" /> on the External API Request function panel. This is the optimal way to create external API request in Xano, as it ensures consistency with what the API requires and is much faster.

    <Info>
      **Tip**

      Most API documentation has a "try it out" or interactive portion that allows you to experiment with the API — it's the fastest way to understand how everything works.
    </Info>
  </Step>
</Steps>

## Multipart (File) Support

### Sending a single image as the whole request body

To send a single image as a part of a whole request body, send a file resource via the 'params' option. You may also need to set the Content-Type in the headers to the type of file you're sending, depending on the API.

<Frame caption="In this example, we've built an API request to send a single image as the entire request body.">
    <img src="https://mintcdn.com/xano-997cb9ee/ZIaZLN54BVGHJVWU/images/external-api-request-20251212-145901.png?fit=max&auto=format&n=ZIaZLN54BVGHJVWU&q=85&s=f0a3aed8b413f1306a45820e718fdb34" alt="external-api-request-20251212-145901" width="2455" height="961" data-path="images/external-api-request-20251212-145901.png" />
</Frame>

### Sending mixed data (files and text)

Some APIs will ask for mixed content, such as a file plus a text field with a description. In this case, you can use the 'set' filter to add multiple key:value pairs to the params, with the file resource as the value for the file field, and text for the other fields.

<Frame caption="In this example, we've built an API request to send an image file along with a text description.">
    <img src="https://mintcdn.com/xano-997cb9ee/ZIaZLN54BVGHJVWU/images/external-api-request-20251212-145955.png?fit=max&auto=format&n=ZIaZLN54BVGHJVWU&q=85&s=a17cb50a28ecca10ad7abaeca35aa8d2" alt="external-api-request-20251212-145955" width="2463" height="954" data-path="images/external-api-request-20251212-145955.png" />
</Frame>

### Sending multiple images as the whole request body

To send multiple images as part of the request body, you can send an array of file resources via the 'params' option. You may also need to set the Content-Type in the headers to the type of files you're sending, depending on the API.

<Frame caption="In this example, we've built an API request to send multiple image files as the entire request body.">
    <img src="https://mintcdn.com/xano-997cb9ee/ZIaZLN54BVGHJVWU/images/external-api-request-20251212-150050.png?fit=max&auto=format&n=ZIaZLN54BVGHJVWU&q=85&s=d60a560ac62f5a48f3ea1376bb035a89" alt="external-api-request-20251212-150050" width="2459" height="1040" data-path="images/external-api-request-20251212-150050.png" />
</Frame>

## Security Settings

### Host Verification

When an API request is sent to a secure server (you'll know if it's a secure request if the URL starts with https — most requests will), the domain's secure connection is verified using a certificate. Enabling host verification checks the certificate to make sure that it matches the domain you're sending the request to.

This value can be `true` or `false`

**Recommended Setting:** `true`

You might want to set Host Verification to 'false' in a few specific scenarios:

1. **Development and Testing Environments**: When working with development servers that use self-signed certificates or have hostnames that don't match their certificates
2. **Internal Services with Misconfigured Certificates**: In corporate environments where internal services may have certificates that don't exactly match the hostnames used to access them, especially in legacy systems.
3. **Troubleshooting SSL Issues**: To isolate whether hostname verification is causing connection problems when debugging API connectivity issues.

### Peer Verification

Secure certificates are usually issued by certain trusted authorities, such as [LetsEncrypt](https://letsencrypt.org/). Peer Verification enables checking whether or not the certificate is issued by one of these known trusted authorities, validating its authenticity.

This value can be `true` or `false`

**Recommended Setting:** `true`

You might want to set this to false if the server you're sending the request to falls under one of the scenarios outlined above under **Host Verification**.

### SSL Authentication

This is a set of additional options you can use to validate the security of the request being made. The provider of the service you're calling should be able to provide these for you, if necessary.

* `certificate`: The content of the client certificate file. Usually, you'd be provided with a .crt or a .pem file — just open it up in your text editor of choice and paste the contents here.
* `certificate_pass`: Password for the certificate if it's password-protected
* `private_key`: The contents of the private key file. Usually, you'd be provided with a .pem file for this — just open it up in your text editor of choice and paste the contents here.
* `private_key_pass`: Password for the private key if it's password-protected

### CA Certificate

Custom CA certificates allow you to specify your own trusted Certificate Authority for peer verification. This is an advanced option that is useful when connecting to servers that use certificates signed by private or internal CAs — as in, a CA that is not listed as a known trusted authority.

A custom certificate is usually provided as a file that you'd just open up in a text editor and paste here. It will look something like this:

```
-----BEGIN CERTIFICATE-----
MIIDITCCAgmgAwIBAgIUJqrGM2rS34H8YryJJLAMarvab8AwDQYJKoZIhvcNAQEL
BQAwIDEeMBwGA1UEAwwVbXlDdXN0b21DZXJ0aWZpY2F0ZUNKX...
-----END CERTIFICATE-----
```


Built with [Mintlify](https://mintlify.com).