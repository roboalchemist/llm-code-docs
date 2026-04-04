# Source: https://developers.cloudflare.com/images/manage-images/enable-flexible-variants/index.md

---

title: Enable flexible variants · Cloudflare Images docs
description: Flexible variants allow you to create variants with dynamic
  resizing which can provide more options than regular variants allow. This
  option is not enabled by default.
lastUpdated: 2025-12-15T15:19:35.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/images/manage-images/enable-flexible-variants/
  md: https://developers.cloudflare.com/images/manage-images/enable-flexible-variants/index.md
---

Flexible variants allow you to create variants with dynamic resizing which can provide more options than regular variants allow. This option is not enabled by default.

## Enable flexible variants via the Cloudflare dashboard

1. In the Cloudflare dashboard, got to the **Hosted Images** page.

   [Go to **Hosted images**](https://dash.cloudflare.com/?to=/:account/images/hosted)

2. Select the **Delivery** tab.

3. Enable **Flexible variants**.

## Enable flexible variants via the API

Make a `PATCH` request to the [Update a variant endpoint](https://developers.cloudflare.com/api/resources/images/subresources/v1/subresources/variants/methods/edit/).

```bash
curl --request PATCH https://api.cloudflare.com/client/v4/accounts/{account_id}/images/v1/config \
--header "Authorization: Bearer <API_TOKEN>" \
--header "Content-Type: application/json" \
--data '{"flexible_variants": true}'
```

After activation, you can use [transformation parameters](https://developers.cloudflare.com/images/transform-images/transform-via-url/#options) on any Cloudflare image. For example,

`https://imagedelivery.net/{account_hash}/{image_id}/w=400,sharpen=3`

Note

Flexible variants cannot be used for images that require a [signed delivery URL](https://developers.cloudflare.com/images/manage-images/serve-images/serve-private-images).
