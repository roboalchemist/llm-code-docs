# Media & Attachments

Source: https://docs.perplexity.ai/docs/sonar/media

Send and receive images, videos, and files with the Sonar API

## Overview

The Sonar API supports comprehensive media handling: send images and files for analysis, and receive images and videos in responses. This guide covers all media functionality in one place.

## Sending Images

Send images to the API for analysis using either base64 encoding or HTTPS URLs. Images are embedded in the `messages` array alongside text content.

<Warning>
  * Base64 images: Maximum 50 MB per image. Supported formats: PNG, JPEG, WEBP, GIF
  * HTTPS URLs: Must be publicly accessible and point directly to the image file
</Warning>

### Base64 Encoded Images

Use base64 encoding when you have the image file locally:

```python Python SDK theme={null}
from perplexity import Perplexity
import base64

client = Perplexity()
