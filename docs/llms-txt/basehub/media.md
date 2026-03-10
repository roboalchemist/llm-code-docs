# Media

> All kind of assets in one block. Comes with some constraints that can make your media uploads more reliable.

## Features

*   ✅ Supports traditional image, video and audio formats
    
*   ✅ Allows you to add custom mimeTypes
    
*   ✅ Supports AI Chat (with image generation)
    
*   ✅ Auto generated alt text for images
    

## Constraints

\[data-radix-scroll-area-viewport\]{scrollbar-width:none;-ms-overflow-style:none;-webkit-overflow-scrolling:touch;}\[data-radix-scroll-area-viewport\]::-webkit-scrollbar{display:none}

Contraint

Description

Is required

Validates the input is filled.

Max size

Limit the max size for the assets that can be uploaded to this block.

Allowed formats

Select from every format category available to limit which ones you will allow.

**Important:** When only one category is enabled, the API will return that single type. (e.g: A media block that only allows image formats, will be exposed as a `BlockImage` type in graphQL.)

## Media Block Union

When dealing with Media blocks in the API, you will encounter that if accepts more than one format category (image, video, audio or file) it will appear as a Union of these types. To fetch the url of a media block you would need to do the following:

```
{
  doc {
    media {
      __typename
      ...on BlockImage {
        url
        width
        height
        altText
      }
      ...on BlockVideo {
        url
      }
      ...on BlockAudio {
        url
      }
      ...on BlockFile {
        url
      }
    }
  }
}
```

Yes, it doesn’t look pretty, but it’s a GraphQL rule for unions. On the other hand, with this query format setup, you can query each type specifics easily. For example, you could fetch audio durations or image altText when possible.

## Adding new formats

If by any chance, you want to upload a file that’s not allowed by default in the media block, you can add it to the constraints following this example: