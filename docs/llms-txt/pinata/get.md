# Source: https://docs.pinata.cloud/sdk/signatures/public/get.md

# Source: https://docs.pinata.cloud/sdk/signatures/private/get.md

# Source: https://docs.pinata.cloud/sdk/groups/public/get.md

# Source: https://docs.pinata.cloud/sdk/groups/private/get.md

# Source: https://docs.pinata.cloud/sdk/gateways/public/get.md

# Source: https://docs.pinata.cloud/sdk/gateways/private/get.md

# get

> `org:files:write`

Retrieve a file through the config's `pinataGateway`

## Usage

```typescript  theme={null}
import { PinataSDK } from "pinata";

const pinata = new PinataSDK({
  pinataJwt: process.env.PINATA_JWT!,
  pinataGateway: "example-gateway.mypinata.cloud",
});

const file = await pinata.gateways.private.get("bafkreih5aznjvttude6c3wbvqeebb6rlx5wkbzyppv7garjiubll2ceym4")
```

## Returns

Returns the data in the form of `JSON`, `string`, or `Blob` as well as the `ContentType`

```typescript  theme={null}
type GetCIDResponse = {
  data?: JSON | string | Blob | null;
  contentType: ContentType;
};

type ContentType =
  | "application/json"
  | "application/xml"
  | "text/plain"
  | "text/html"
  | "text/css"
  | "text/javascript"
  | "application/javascript"
  | "image/jpeg"
  | "image/png"
  | "image/gif"
  | "image/svg+xml"
  | "audio/mpeg"
  | "audio/ogg"
  | "video/mp4"
  | "application/pdf"
  | "application/octet-stream"
  | string;
```

## Parameters

### cid

* Type: `string`

Accepts CID of the file you are trying to fetch

```typescript  theme={null}
const data = await pinata.gateways.private.get(
	"bafybeibo5zcqeorhqxczodrx52rn7byyrwfvwthz5dspnjlbkd7zkugefi",
);
```

### optimizeImage (Optional)

* Type: [OptimizeImageOptions](/sdk/types#optimizeimageoptions)

```typescript  theme={null}
type OptimizeImageOptions = {
  width?: number;
  height?: number;
  dpr?: number;
  fit?: "scaleDown" | "contain" | "cover" | "crop" | "pad";
  gravity?: "auto" | "side" | string;
  quality?: number;
  format?: "auto" | "webp";
  animation?: boolean;
  sharpen?: number;
  onError?: boolean;
  metadata?: "keep" | "copyright" | "none";
};
```

If the content being fetched is an image you can apply image optimizations to the image.

```typescript {3-7} theme={null}
const data = await pinata.gateways.private
  .get("bafkreih5aznjvttude6c3wbvqeebb6rlx5wkbzyppv7garjiubll2ceym4")
  .optimizeImage({
    width: 500,
    height: 500,
    format: "webp"
  })
```
