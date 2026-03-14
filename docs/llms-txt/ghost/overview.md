# Source: https://docs.ghost.org/admin-api/webhooks/overview.md

# Source: https://docs.ghost.org/admin-api/users/overview.md

# Source: https://docs.ghost.org/admin-api/tiers/overview.md

# Source: https://docs.ghost.org/admin-api/themes/overview.md

# Source: https://docs.ghost.org/admin-api/posts/overview.md

# Source: https://docs.ghost.org/admin-api/pages/overview.md

# Source: https://docs.ghost.org/admin-api/offers/overview.md

# Source: https://docs.ghost.org/admin-api/newsletters/overview.md

# Source: https://docs.ghost.org/admin-api/members/overview.md

# Source: https://docs.ghost.org/admin-api/images/overview.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.ghost.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Overview

Sending images to Ghost via the API allows you to upload images one at a time, and store them with a [storage adapter](https://ghost.org/integrations/?tag=storage). The default adapter stores files locally in /content/images/ without making any modifications, except for sanitising the filename.

```js  theme={"dark"}
POST /admin/images/upload/
```

### The image object

Images can be uploaded to, and fetched from storage. When an image is uploaded, the response is an image object that contains the new URL for the image - the location from which the image can be fetched.

`url`: *URI* The newly created URL for the image.

`ref`: *String (optional)* The reference for the image, if one was provided with the upload.

```json  theme={"dark"}
// POST /admin/images/upload/

{
    "images": [
        {
            "url": "https://demo.ghost.io/content/images/2019/02/ghost-logo.png",
            "ref": "ghost-logo.png"
        }
    ]
}
```


Built with [Mintlify](https://mintlify.com).