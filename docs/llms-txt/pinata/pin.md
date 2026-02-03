# Source: https://docs.pinata.cloud/api-reference/endpoint/x402/pin.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.pinata.cloud/llms.txt
> Use this file to discover all available pages before exploring further.

# Upload a File

> Uploads a file to Pinata's public IPFS network

## Cost

| Price           | Duration           |
| --------------- | ------------------ |
| \$0.10/GB \* 12 | Pins for 12 months |

## Example Usage

In order to access these endpoints you will need to use either [`@x402/axios`](https://www.npmjs.com/package/@x402/axios) or [`@x402/fetch`](https://www.npmjs.com/package/@x402/fetch). Once installed you will also need either [Viem](https://viem.sh) or a Coinbase developer account. From there you can create an `account` locally or through the CDP Wallet API.

When you make a request to one of the Pinata x402 endpoints it will return a 402 error saying payment is required. Then the `fetchWithPayment` method from the fetch or axios library will make a second requst for the requested payment amount. After payment is settled then you can use the returned presigned URL to upload the file to Pinata.

```typescript  theme={null}
import { wrapFetchWithPayment, decodeXPaymentResponse } from "@x402/fetch";
import { account } from "./viem";

const fetchWithPayment = wrapFetchWithPayment(fetch, account);

const url = "https://402.pinata.cloud/v1/pin/public";

fetchWithPayment(url, {
  method: "POST",
  body: JSON.stringify({
    fileSize: 5000000,
  }),
})
  .then(async (response) => {
    const body = (await response.json()) as { url: string };
    console.log(body);

    const uuid = crypto.randomUUID();

    const file = new File([`Paid and pinned by 402.pinata.cloud: ${uuid}`], "file.txt");

    const data = new FormData();
    data.append("network", "public");
    data.append("file", file);

    const uploadReq = await fetch(body.url, {
      method: "POST",
      body: data,
    });

    const uploadRes = await uploadReq.json();
    console.log(uploadRes);
  })
  .catch((error) => {
    console.error(error.response?.data?.error);
  });
```

Uploading files to Public IPFS means you can access them through a gateway like `https://ipfs.io/ipfs/:CID`. If you upload a file as `private` then it will not be accessible on public IPFS, so in order to access it you need to create a temporary access URL. This flow is similar to the previous one, except you would provide the CID that you uploded previously that you would like to access. After a successful payment the server will return a URL you can access the file with.

```typescript  theme={null}
import { wrapFetchWithPayment, decodeXPaymentResponse } from "@x402/fetch";
import { account } from "./viem";

const fetchWithPayment = wrapFetchWithPayment(fetch, account);

const url =
  "https://402.pinata.cloud/v1/retrieve/private/bafkreih5aznjvttude6c3wbvqeebb6rlx5wkbzyppv7garjiubll2ceym4";

fetchWithPayment(url, {
  method: "GET",
})
  .then(async (response) => {
    const body = (await response.json()) as { url: string };
    console.log(body);
  })
  .catch((error) => {
    console.error(error.response?.data?.error);
  });
```


## OpenAPI

````yaml pinata-x402-api-v1.yaml post /pin/{network}
openapi: 3.0.0
info:
  title: Pinata x402
  description: x402 compatible endpoints for uploading and retrieving files on IPFS
  version: 1.0.0
servers:
  - url: https://402.pinata.cloud/v1
    description: Production server
security: []
paths:
  /pin/{network}:
    post:
      summary: Upload a file to Public or Private IPFS
      description: Uploads a file to Pinata's public IPFS network
      parameters:
        - name: network
          description: Upload to either public or private IPFS network
          in: path
          schema:
            type: string
            enum:
              - public
              - private
          required: true
          example: public
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required:
                - fileSize
              properties:
                fileSize:
                  type: integer
                  description: Size of the file to be uploaded in bytes
      responses:
        '200':
          description: Successful operation
          content:
            application/json:
              schema:
                type: object
                properties:
                  url:
                    type: string
                    description: The signed URL for file upload
        '400':
          description: Bad request
      security:
        - x402Payment: []
components:
  securitySchemes:
    x402Payment:
      type: apiKey
      name: X-PAYMENT
      in: header
      description: Base64 encoded x402 payment payload

````