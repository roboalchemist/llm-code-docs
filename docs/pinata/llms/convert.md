# Source: https://docs.pinata.cloud/sdk/gateways/public/convert.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.pinata.cloud/llms.txt
> Use this file to discover all available pages before exploring further.

# convert

Convert an IPFS link into one that uses your Dedicated Gateway

## Usage

```typescript  theme={null}
import { PinataSDK } from "pinata-web3";

const pinata = new PinataSDK({
  pinataJwt: process.env.PINATA_JWT!,
  pinataGateway: "example-gateway.mypinata.cloud",
});

const url = await pinata.gateways.convert(
  "ipfs://QmVLwvmGehsrNEvhcCnnsw5RQNseohgEkFNN1848zNzdng"
);
```

## Returns

```typescript  theme={null}
string
```

## Parameters

### url

* Type: `string`

Accepts CID or IPFS gateway link.

```typescript  theme={null}
const url = await pinata.gateways.convert(
	"bafybeibo5zcqeorhqxczodrx52rn7byyrwfvwthz5dspnjlbkd7zkugefi/hello-1.txt",
);

const url = await pinata.gateways.convert(
	"https://ipfs.io/ipfs/bafybeibo5zcqeorhqxczodrx52rn7byyrwfvwthz5dspnjlbkd7zkugefi/hello-1.txt",
);

const url = await pinata.gateways.convert(
	"https://bafyreibroegmxohcbvvs3rziqsp3osyn7t5rzot34y6pn5xtewffhtsl4e.ipfs.nftstorage.link/metadata.json",
);
```

### prefix (Optional)

* Type: `string`

Use a different gateway prefix than the config default

```typescript  theme={null}
const url = await pinata.gateways.convert(
	"QmVLwvmGehsrNEvhcCnnsw5RQNseohgEkFNN1848zNzdng",
	"https://ipfs.io"
);
```
