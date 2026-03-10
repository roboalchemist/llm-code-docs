# Source: https://screenshotone.com/docs/errors/resulting-image-too-large/

# Resulting Image Too Large

It is an API error returned when the resulting image is too large for the specified format.

```json
{
    "is_successful": false,
    "error_message": "The resulting image is too large for the specified format.",
    "error_code": "resulting_image_too_large",
    "documentation_url": "https://screenshotone.com/docs/errors/resulting-image-too-large/"
}
```

## Reasons and how to fix

### Using image formats with size limits for full-page screenshots

The JPEG format has a height limit of 65,535 pixels, WebP format has a height limit of 16,383 pixels.

Full-page screenshots that don't fit the size limits will trigger the error `resulting_image_too_large`. 

A solution would be is to choose the format that fits your use case better. E.g. if you use WebP, try to use JPEG. Or maybe try PNG. 

### Limiting the height of the full-page screenshot

If it happens for full-page screenshots, you can set the `full_page_max_height` option to make sure the height of the resulting image always fits the specified format, e.g. set it to 16000 for WebP format or 60000 for JPEG format. 


### Reducing the device scale factor

If the issue is with the size of the page, you can try to reduce the device scale factor by setting the `device_scale_factor` option to a lower value, e.g. `1` instead of `2`.

## Combining the options

You can try to combine all the options above to find the best solution for your use case. 

Or you can even send API requests as-is, but when you encounter the error, just perform a retry with the limited full page height or lower device scale factor, or even a different format.

## Reach out to support

If you continue to face issues, please reach out to `support@screenshotone.com`, and we will assist you as soon as possible.