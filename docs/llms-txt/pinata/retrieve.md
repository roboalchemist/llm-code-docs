# Source: https://docs.pinata.cloud/api-reference/endpoint/x402/retrieve.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.pinata.cloud/llms.txt
> Use this file to discover all available pages before exploring further.

# Retrieve a Private File

> Retrieves a private file from IPFS by its CID

## Cost

| Price    | Duration    |
| -------- | ----------- |
| \$0.0001 | Per request |

## Example Usage

If you upload a file as `private` then it will not be accessible on public IPFS, so in order to access it you need to create a temporary access URL. This flow is similar to the previous one, except you would provide the CID that you uploded previously that you would like to access. After a successful payment the server will return a URL you can access the file with.

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

````yaml pinata-x402-api-v1.yaml get /retrieve/private/{cid}
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
  /retrieve/private/{cid}:
    get:
      summary: Retrieve private file
      description: Retrieves a private file from IPFS by its CID
      operationId: retrievePrivateFile
      parameters:
        - name: cid
          in: path
          required: true
          schema:
            type: string
          description: Content Identifier (CID) of the file
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
                    description: URL to access the private file
        '400':
          description: Bad request
        '401':
          description: Unauthorized
        '500':
          description: Server error
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