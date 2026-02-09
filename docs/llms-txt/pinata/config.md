# Source: https://docs.pinata.cloud/sdk/types/config.md

# Source: https://docs.pinata.cloud/sdk/config.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.pinata.cloud/llms.txt
> Use this file to discover all available pages before exploring further.

# Config

Overview of the Private IPFS SDK Config

## Usage

```typescript  theme={null}
import { PinataSDK } from "pinata";

const pinata = new PinataSDK({
  pinataJwt: process.env.PINATA_JWT!,
  pinataGateway: "example-gateway.mypinata.cloud",
});
```

## Parameters

### pinataJwt (Optional)

* Type: `string`

The Pinata API JWT key that authorizes the SDK. [Read more about API Keys](/account-management/api-keys).

### pinataGateway (Optional)

* Type: `string`

The domain of the Gateway included with your account. [Read more about Gateways](/gateways/retrieving-files).

### pinataGatewayKey (Optional)

* Type: `string`

Optional [Gateway Access Control](/gateways/gateway-access-controls) key to authorize requests outside your account.
