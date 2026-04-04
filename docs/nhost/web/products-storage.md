# Source: https://docs.nhost.io/products/storage/

Title: Overview

URL Source: https://docs.nhost.io/products/storage/

Markdown Content:
Overview | Nhost Documentation
===============
[Skip to content](https://docs.nhost.io/products/storage/#_top)

[![Image 1](https://docs.nhost.io/_astro/dark.BjDa9aYk.svg)![Image 2](https://docs.nhost.io/_astro/light.BLb3wxKz.svg) Nhost Documentation](https://docs.nhost.io/)

Search Ctrl K

 Cancel 

[Twitter](https://twitter.com/nhost)[GitHub](https://github.com/nhost)[LinkedIn](https://www.linkedin.com/company/nhost)

[](https://discord.com/invite/nhost)[](https://github.com/nhost/nhost)[](https://x.com/nhost)[Support](https://app.nhost.io/support)[Dashboard](https://app.nhost.io/)

Products

Sections

[Welcome](https://docs.nhost.io/)[Getting Started](https://docs.nhost.io/getting-started/)[Platform](https://docs.nhost.io/platform/)[Reference](https://docs.nhost.io/reference/)[Blog](https://nhost.io/blog)

Products

[Overview](https://docs.nhost.io/products/)[Database](https://docs.nhost.io/products/database/)[GraphQL](https://docs.nhost.io/products/graphql/)[Auth](https://docs.nhost.io/products/auth/)[Storage](https://docs.nhost.io/products/storage/)[Run](https://docs.nhost.io/products/run/)[Functions](https://docs.nhost.io/products/functions/)[AI](https://docs.nhost.io/products/ai/)

[Support](https://app.nhost.io/support)[Dashboard](https://app.nhost.io/)

[Welcome](https://docs.nhost.io/)[Getting Started](https://docs.nhost.io/getting-started/)

 Products 

[Overview](https://docs.nhost.io/products/)[Database](https://docs.nhost.io/products/database/)[GraphQL](https://docs.nhost.io/products/graphql/)[Auth](https://docs.nhost.io/products/auth/)[Storage](https://docs.nhost.io/products/storage/)[Run](https://docs.nhost.io/products/run/)[Functions](https://docs.nhost.io/products/functions/)[AI](https://docs.nhost.io/products/ai/)

[Platform](https://docs.nhost.io/platform/)[Reference](https://docs.nhost.io/reference/)[Blog](https://nhost.io/blog)

*   [Getting Started](https://docs.nhost.io/getting-started/)
*   [Products](https://docs.nhost.io/products/)
*   [Database](https://docs.nhost.io/products/database/)
*   [GraphQL](https://docs.nhost.io/products/graphql/)
*   [Auth](https://docs.nhost.io/products/auth/)
*   [Storage](https://docs.nhost.io/products/storage/)
*   [Run](https://docs.nhost.io/products/run/)
*   [Functions](https://docs.nhost.io/products/functions/)
*   [AI](https://docs.nhost.io/products/ai/)
*   [Platform](https://docs.nhost.io/platform/)
*   [Reference](https://docs.nhost.io/reference/)

*   [Storage](https://docs.nhost.io/products/storage/)
*   
Concepts
    *   [Architecture](https://docs.nhost.io/products/storage/architecture/)
    *   [Buckets](https://docs.nhost.io/products/storage/buckets/)
    *   [Permissions](https://docs.nhost.io/products/storage/permissions/)
    *   [Image Transformation](https://docs.nhost.io/products/storage/image-transformation/)

*   
Guides
    *   [File Operations](https://docs.nhost.io/products/storage/guides/file-operations/)
    *   [Pre-signed URLs](https://docs.nhost.io/products/storage/guides/presigned-urls/)
    *   [Display Images](https://docs.nhost.io/products/storage/guides/display-images/)
    *   [Permissions and Relationships](https://docs.nhost.io/products/storage/guides/permissions-and-relationships/)

*   
Platform
    *   [CDN](https://docs.nhost.io/products/storage/cdn/)
    *   [Antivirus](https://docs.nhost.io/products/storage/antivirus/)

[Twitter](https://twitter.com/nhost)[GitHub](https://github.com/nhost)[LinkedIn](https://www.linkedin.com/company/nhost)

On this page

*   [Overview](https://docs.nhost.io/products/storage/#_top)
*   [How Storage Works](https://docs.nhost.io/products/storage/#how-storage-works)
*   [Buckets](https://docs.nhost.io/products/storage/#buckets)
*   [Permissions](https://docs.nhost.io/products/storage/#permissions)
*   [Image Transformation](https://docs.nhost.io/products/storage/#image-transformation)
*   [Concepts](https://docs.nhost.io/products/storage/#concepts)
*   [Guides](https://docs.nhost.io/products/storage/#guides)
*   [Platform](https://docs.nhost.io/products/storage/#platform)

On this page
------------

*   [Overview](https://docs.nhost.io/products/storage/#_top)
*   [How Storage Works](https://docs.nhost.io/products/storage/#how-storage-works)
*   [Buckets](https://docs.nhost.io/products/storage/#buckets)
*   [Permissions](https://docs.nhost.io/products/storage/#permissions)
*   [Image Transformation](https://docs.nhost.io/products/storage/#image-transformation)
*   [Concepts](https://docs.nhost.io/products/storage/#concepts)
*   [Guides](https://docs.nhost.io/products/storage/#guides)
*   [Platform](https://docs.nhost.io/products/storage/#platform)

Overview
========

storage file upload file download S3 CDN images files media blob storage

Nhost Storage is a file storage service seamlessly integrated with the [GraphQL API](https://docs.nhost.io/products/graphql) and its [Permission System](https://docs.nhost.io/products/graphql/permissions). Files are stored on an S3-compatible backend, metadata is managed through GraphQL, and access control is handled by the same Hasura permission system used for the rest of your data. Files are served through a [CDN](https://docs.nhost.io/products/storage/cdn) for optimal performance.

How Storage Works
-----------------

[Section titled “How Storage Works”](https://docs.nhost.io/products/storage/#how-storage-works)

When you upload a file, the Storage service validates the user’s JWT, checks permissions via Hasura, stores the file content in S3, and records metadata in the `storage.files` table. Downloads follow the same path in reverse — permissions are checked before the file is served. See [Architecture](https://docs.nhost.io/products/storage/architecture) for the full request flow.

`// Upload a fileconst response = await nhost.storage.uploadFiles({  'bucket-id': 'default',  'file[]': [file],})`

`// Download a fileconst { body } = await nhost.storage.getFile(fileId)const url = URL.createObjectURL(body)`

Buckets
-------

[Section titled “Buckets”](https://docs.nhost.io/products/storage/#buckets)

[Buckets](https://docs.nhost.io/products/storage/buckets) are containers that organize files and group configuration. Each bucket can have its own size limits, cache settings, and pre-signed URL configuration. Every project includes a `default` bucket; you can create additional buckets for different use cases (e.g., `avatars`, `documents`, `communities`).

Permissions
-----------

[Section titled “Permissions”](https://docs.nhost.io/products/storage/#permissions)

[Permissions](https://docs.nhost.io/products/storage/permissions) follow a **Zero Trust** model — no role has access by default. You grant access by configuring `insert`, `select`, and `delete` permissions on the `storage.files` table in Hasura. The same session variables (`X-Hasura-User-Id`, `X-Hasura-Role`, custom claims) available in your GraphQL permissions also work for storage.

Image Transformation
--------------------

[Section titled “Image Transformation”](https://docs.nhost.io/products/storage/#image-transformation)

Images can be [transformed on-the-fly](https://docs.nhost.io/products/storage/image-transformation) by adding query parameters to file URLs. Resize, change format (WebP, AVIF), adjust quality, and apply blur — all cached at the CDN layer.

`// Fetch a 100x100 WebP thumbnailconst { body } = await nhost.storage.getFile(fileId, {  w: 100,  h: 100,  f: 'webp',})const url = URL.createObjectURL(body)`

Concepts
--------

[Section titled “Concepts”](https://docs.nhost.io/products/storage/#concepts)

[### Architecture How Storage integrates with Auth, GraphQL, and S3](https://docs.nhost.io/products/storage/architecture)

[### Buckets Organize files with configurable containers](https://docs.nhost.io/products/storage/buckets)

[### Permissions Control access with Hasura’s permission system](https://docs.nhost.io/products/storage/permissions)

[### Image Transformation Resize, convert, and optimize images on-the-fly](https://docs.nhost.io/products/storage/image-transformation)

Guides
------

[Section titled “Guides”](https://docs.nhost.io/products/storage/#guides)

[### File Operations Upload, download, replace, and delete files](https://docs.nhost.io/products/storage/guides/file-operations)

[### Pre-signed URLs Generate temporary secure URLs for file access](https://docs.nhost.io/products/storage/guides/presigned-urls)

[### Display Images Fetch authenticated images and render them in the browser](https://docs.nhost.io/products/storage/guides/display-images)

[### Permissions and Relationships Set up user files, department files, and GraphQL relationships](https://docs.nhost.io/products/storage/guides/permissions-and-relationships)

Platform
--------

[Section titled “Platform”](https://docs.nhost.io/products/storage/#platform)

[### CDN Global content delivery and caching](https://docs.nhost.io/products/storage/cdn)

[### Antivirus Scan uploads with ClamAV integration](https://docs.nhost.io/products/storage/antivirus)

[Next Architecture](https://docs.nhost.io/products/storage/architecture/)
