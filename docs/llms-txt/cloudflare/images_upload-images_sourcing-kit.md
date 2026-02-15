# Source: https://developers.cloudflare.com/images/upload-images/sourcing-kit/index.md

---

title: Upload via Sourcing Kit · Cloudflare Images docs
description: With Sourcing Kit you can define one or multiple repositories of
  images to bulk import from Amazon S3. Once you have these set up, you can
  reuse those sources and import only new images to your Cloudflare Images
  account. This helps you make sure that only usable images are imported, and
  skip any other objects or files that might exist in that source.
lastUpdated: 2025-10-30T17:09:11.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/images/upload-images/sourcing-kit/
  md: https://developers.cloudflare.com/images/upload-images/sourcing-kit/index.md
---

With Sourcing Kit you can define one or multiple repositories of images to bulk import from Amazon S3. Once you have these set up, you can reuse those sources and import only new images to your Cloudflare Images account. This helps you make sure that only usable images are imported, and skip any other objects or files that might exist in that source.

Sourcing Kit also lets you target paths, define prefixes for imported images, and obtain error logs for bulk operations.

## When to use Sourcing Kit

Sourcing Kit can be a good choice if the Amazon S3 bucket you are importing consists primarily of images stored using non-archival storage classes, as images stored using [archival storage classes](https://aws.amazon.com/s3/storage-classes/#Archive) will be skipped and need to be imported separately. Specifically:

* Images stored using S3 Glacier tiers (not including Glacier Instant Retrieval) will be skipped and logged in the migration log.
* Images stored using S3 Intelligent Tiering and placed in Deep Archive tier will be skipped and logged in the migration log.
