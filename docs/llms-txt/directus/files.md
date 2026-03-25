# Source: https://directus.io/docs/raw/configuration/files.md

# Files

> Configuration for storage locations, metadata, upload limits, and transformations.

<partial content="config-env-vars">



</partial>

By default, Directus stores all uploaded files locally on the file system or can also configure Directus to use external storage services. You can also configure *multiple* storage adapters at the same time which allows you to choose where files are being uploaded on a file-by-file basis.

In the Data Studio, files will automatically be uploaded to the first configured storage location (in this case `local`). The used storage location is saved under `storage` in the `directus_files` collection.

## Storage Locations

<table>
<thead>
  <tr>
    <th>
      Variable
    </th>
    
    <th>
      Description
    </th>
    
    <th>
      Default Value
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <code>
        STORAGE_LOCATIONS
      </code>
    </td>
    
    <td>
      A comma separated list of storage locations. You can use any names you'd like for these keys.
    </td>
    
    <td>
      <code>
        local
      </code>
    </td>
  </tr>
</tbody>
</table>

For each of the storage locations listed, you must provide the following configuration (variable name must be uppercase in these options):

<table>
<thead>
  <tr>
    <th>
      Variable
    </th>
    
    <th>
      Description
    </th>
    
    <th>
      Default Value
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <code>
        STORAGE_<LOCATION>_DRIVER
      </code>
    </td>
    
    <td>
      Which driver to use, either <code>
        local
      </code>
      
      , <code>
        s3
      </code>
      
      , <code>
        gcs
      </code>
      
      , <code>
        azure
      </code>
      
      , <code>
        cloudinary
      </code>
      
      , <code>
        supabase
      </code>
      
      .
    </td>
    
    <td>
      
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        STORAGE_<LOCATION>_ROOT
      </code>
    </td>
    
    <td>
      Where to store the files on disk.
    </td>
    
    <td>
      <code>
        ''
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        STORAGE_<LOCATION>_HEALTHCHECK_THRESHOLD
      </code>
    </td>
    
    <td>
      Healthcheck timeout threshold in ms.
    </td>
    
    <td>
      <code>
        750
      </code>
    </td>
  </tr>
</tbody>
</table>

Based on your configured drivers, you must also provide additional variables, where `<LOCATION>` is the capitalized name of the item in the `STORAGE_LOCATIONS` value.

### Local (`local`)

<table>
<thead>
  <tr>
    <th>
      Variable
    </th>
    
    <th>
      Description
    </th>
    
    <th>
      Default Value
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <code>
        STORAGE_<LOCATION>_ROOT
      </code>
    </td>
    
    <td>
      Where to store the files on disk.
    </td>
    
    <td>
      
    </td>
  </tr>
</tbody>
</table>

### S3 (`s3`)

<table>
<thead>
  <tr>
    <th>
      Variable
    </th>
    
    <th>
      Description
    </th>
    
    <th>
      Default Value
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <code>
        STORAGE_<LOCATION>_KEY
      </code>
    </td>
    
    <td>
      User key.
    </td>
    
    <td>
      
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        STORAGE_<LOCATION>_SECRET
      </code>
    </td>
    
    <td>
      User secret.
    </td>
    
    <td>
      
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        STORAGE_<LOCATION>_BUCKET
      </code>
    </td>
    
    <td>
      S3 bucket.
    </td>
    
    <td>
      
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        STORAGE_<LOCATION>_REGION
      </code>
    </td>
    
    <td>
      S3 region.
    </td>
    
    <td>
      
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        STORAGE_<LOCATION>_ENDPOINT
      </code>
      
      <sup>
        <span>
          1
        </span>
      </sup>
    </td>
    
    <td>
      S3 endpoint.
    </td>
    
    <td>
      <code>
        s3.amazonaws.com
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        STORAGE_<LOCATION>_ACL
      </code>
    </td>
    
    <td>
      S3 ACL.
    </td>
    
    <td>
      
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        STORAGE_<LOCATION>_SERVER_SIDE_ENCRYPTION
      </code>
    </td>
    
    <td>
      S3 server side encryption.
    </td>
    
    <td>
      
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        STORAGE_<LOCATION>_SERVER_SIDE_ENCRYPTION_KMS_KEY_ID
      </code>
    </td>
    
    <td>
      S3 server side encryption kms id.
    </td>
    
    <td>
      
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        STORAGE_<LOCATION>_FORCE_PATH_STYLE
      </code>
    </td>
    
    <td>
      S3 force path style.
    </td>
    
    <td>
      false
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        STORAGE_<LOCATION>_CONNECTION_TIMEOUT
      </code>
    </td>
    
    <td>
      S3 connection timeout (ms).
    </td>
    
    <td>
      5000
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        STORAGE_<LOCATION>_SOCKET_TIMEOUT
      </code>
    </td>
    
    <td>
      S3 socket timeout (ms).
    </td>
    
    <td>
      120000
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        STORAGE_<LOCATION>_MAX_SOCKETS
      </code>
    </td>
    
    <td>
      S3 max sockets.
    </td>
    
    <td>
      500
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        STORAGE_<LOCATION>_KEEP_ALIVE
      </code>
    </td>
    
    <td>
      S3 keep alive.
    </td>
    
    <td>
      true
    </td>
  </tr>
</tbody>
</table>

<sup>
<span>

1

</span>
</sup>

 When overriding this variable for S3, make sure to add your bucket's region in the endpoint: `s3.{region}.amazonaws.com`.

### Google Cloud Storage (`gcs`)

<table>
<thead>
  <tr>
    <th>
      Variable
    </th>
    
    <th>
      Description
    </th>
    
    <th>
      Default Value
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <code>
        STORAGE_<LOCATION>_KEY_FILENAME
      </code>
    </td>
    
    <td>
      Path to key file on disk.
    </td>
    
    <td>
      
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        STORAGE_<LOCATION>_BUCKET
      </code>
    </td>
    
    <td>
      Google Cloud Storage bucket.
    </td>
    
    <td>
      
    </td>
  </tr>
</tbody>
</table>

### Azure (`azure`)

<table>
<thead>
  <tr>
    <th>
      Variable
    </th>
    
    <th>
      Description
    </th>
    
    <th>
      Default Value
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <code>
        STORAGE_<LOCATION>_CONTAINER_NAME
      </code>
    </td>
    
    <td>
      Azure Storage container.
    </td>
    
    <td>
      
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        STORAGE_<LOCATION>_ACCOUNT_NAME
      </code>
    </td>
    
    <td>
      Azure Storage account name.
    </td>
    
    <td>
      
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        STORAGE_<LOCATION>_ACCOUNT_KEY
      </code>
    </td>
    
    <td>
      Azure Storage key.
    </td>
    
    <td>
      
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        STORAGE_<LOCATION>_ENDPOINT
      </code>
    </td>
    
    <td>
      Azure URL.
    </td>
    
    <td>
      <code>
        https://{ACCOUNT_NAME}.blob.core.windows.net
      </code>
    </td>
  </tr>
</tbody>
</table>

### Cloudinary (`cloudinary`)

<table>
<thead>
  <tr>
    <th>
      Variable
    </th>
    
    <th>
      Description
    </th>
    
    <th>
      Default Value
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <code>
        STORAGE_<LOCATION>_CLOUD_NAME
      </code>
    </td>
    
    <td>
      Cloudinary cloud name.
    </td>
    
    <td>
      
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        STORAGE_<LOCATION>_API_KEY
      </code>
    </td>
    
    <td>
      Cloudinary API key.
    </td>
    
    <td>
      
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        STORAGE_<LOCATION>_API_SECRET
      </code>
    </td>
    
    <td>
      Cloudinary API secret.
    </td>
    
    <td>
      
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        STORAGE_<LOCATION>_ACCESS_MODE
      </code>
    </td>
    
    <td>
      Default access mode for the file. One of <code>
        public
      </code>
      
      , <code>
        authenticated
      </code>
      
      .
    </td>
    
    <td>
      
    </td>
  </tr>
</tbody>
</table>

Cloudinary is supported only as a storage driver. Changes made on Cloudinary are not synced back to Directus, and Directus won't rely on Cloudinary's asset transformations in the `/assets` endpoint.

### Supabase (`supabase`)

<table>
<thead>
  <tr>
    <th>
      Variable
    </th>
    
    <th>
      Description
    </th>
    
    <th>
      Default Value
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <code>
        STORAGE_<LOCATION>_SERVICE_ROLE
      </code>
    </td>
    
    <td>
      The admin service role JWT.
    </td>
    
    <td>
      
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        STORAGE_<LOCATION>_BUCKET
      </code>
    </td>
    
    <td>
      Storage bucket.
    </td>
    
    <td>
      
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        STORAGE_<LOCATION>_PROJECT_ID
      </code>
    </td>
    
    <td>
      Project ID.
    </td>
    
    <td>
      
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        STORAGE_<LOCATION>_ENDPOINT
      </code>
    </td>
    
    <td>
      Optional custom endpoint.
    </td>
    
    <td>
      
    </td>
  </tr>
</tbody>
</table>

## Metadata

When uploading an image, Directus persists the `description`, `title`, and `tags` from available Exif metadata. For security purposes, collection of additional metadata must be configured:

<table>
<thead>
  <tr>
    <th>
      Variable
    </th>
    
    <th>
      Description
    </th>
    
    <th>
      Default Value
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <code>
        FILE_METADATA_ALLOW_LIST
      </code>
    </td>
    
    <td>
      A comma-separated list of metadata keys to collect during file upload. Use <code>
        *
      </code>
      
       for all<sup>
        <span>
          1
        </span>
      </sup>
      
      .
    </td>
    
    <td>
      ifd0.Make,ifd0.Model,exif.FNumber,exif.ExposureTime,exif.FocalLength,exif.ISOSpeedRatings
    </td>
  </tr>
</tbody>
</table>

<sup>
<span>

1

</span>
</sup>

: Extracting all metadata might cause memory issues when the file has an unusually large set of metadata

## Upload Limits

<table>
<thead>
  <tr>
    <th>
      Variable
    </th>
    
    <th>
      Description
    </th>
    
    <th>
      Default Value
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <code>
        FILES_MAX_UPLOAD_SIZE
      </code>
    </td>
    
    <td>
      Maximum file upload size allowed. For example <code>
        10mb
      </code>
      
      , <code>
        1gb
      </code>
      
      , <code>
        10kb
      </code>
      
      .
    </td>
    
    <td>
      
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        FILES_MAX_UPLOAD_CONCURRENCY
      </code>
    </td>
    
    <td>
      Maximum files uploaded concurrently from the studio. Remaining files are sent in a sequential batch
    </td>
    
    <td>
      
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        FILES_MIME_TYPE_ALLOW_LIST
      </code>
    </td>
    
    <td>
      Allow list of mime types that are allowed to be uploaded. Supports <code>
        glob
      </code>
      
       syntax.
    </td>
    
    <td>
      <code>
        */*
      </code>
    </td>
  </tr>
</tbody>
</table>

## Chunked Uploads

Large files can be uploaded in chunks to improve reliability and efficiency, especially in scenarios with network instability or limited bandwidth. This is implemented using the [TUS protocol](https://tus.io/).

<table>
<thead>
  <tr>
    <th>
      Variable
    </th>
    
    <th>
      Description
    </th>
    
    <th>
      Default Value
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <code>
        TUS_ENABLED
      </code>
    </td>
    
    <td>
      Whether or not to enable the chunked uploads.
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        TUS_CHUNK_SIZE
      </code>
    </td>
    
    <td>
      The size of each file chunks. For example <code>
        10mb
      </code>
      
      , <code>
        1gb
      </code>
      
      , <code>
        10kb
      </code>
      
      .
    </td>
    
    <td>
      <code>
        10mb
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        TUS_UPLOAD_EXPIRATION
      </code>
    </td>
    
    <td>
      The expiry duration for uncompleted files with no upload activity.
    </td>
    
    <td>
      <code>
        10m
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        TUS_CLEANUP_SCHEDULE
      </code>
    </td>
    
    <td>
      Cron schedule to clean up the expired uncompleted uploads.
    </td>
    
    <td>
      <code>
        0 * * * *
      </code>
    </td>
  </tr>
</tbody>
</table>

<callout icon="material-symbols:info-outline">

This feature requires the `PUBLIC_URL` to be set correctly to [where your API is publicly accessible](https://directus.io/docs/configuration/general).

</callout>

<callout icon="material-symbols:warning-rounded" color="warning">

**Chunked Upload Restrictions**<br />



Some storage drivers have specific chunk size restrictions. The `TUS_CHUNK_SIZE` must meet the relevant restrictions for
the storage driver(s) being used.

<table>
<thead>
  <tr>
    <th>
      Storage Driver
    </th>
    
    <th>
      <code>
        TUS_CHUNK_SIZE
      </code>
      
       Restriction
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <code>
        storage-driver-gcs
      </code>
    </td>
    
    <td>
      Must be a power of 2 with a minimum of <code>
        256kb
      </code>
      
       (e.g. <code>
        256kb
      </code>
      
      , <code>
        512kb
      </code>
      
      , <code>
        1024kb
      </code>
      
      )
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        storage-driver-azure
      </code>
    </td>
    
    <td>
      Must not be larger than <code>
        100mb
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        storage-driver-cloudinary
      </code>
    </td>
    
    <td>
      Must not be smaller than <code>
        5mb
      </code>
    </td>
  </tr>
</tbody>
</table>
</callout>

## Assets

<table>
<thead>
  <tr>
    <th>
      Variable
    </th>
    
    <th>
      Description
    </th>
    
    <th>
      Default Value
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <code>
        ASSETS_CACHE_TTL
      </code>
    </td>
    
    <td>
      How long assets will be cached for in the browser. Sets the <code>
        max-age
      </code>
      
       value of the <code>
        Cache-Control
      </code>
      
       header.
    </td>
    
    <td>
      <code>
        30d
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        ASSETS_TRANSFORM_MAX_CONCURRENT
      </code>
    </td>
    
    <td>
      How many file transformations can be done simultaneously.
    </td>
    
    <td>
      <code>
        25
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        ASSETS_TRANSFORM_IMAGE_MAX_DIMENSION
      </code>
    </td>
    
    <td>
      The max pixel dimensions size (width/height) that is allowed to be transformed.
    </td>
    
    <td>
      <code>
        6000
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        ASSETS_TRANSFORM_TIMEOUT
      </code>
    </td>
    
    <td>
      Max time spent trying to transform an asset.
    </td>
    
    <td>
      <code>
        7500ms
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        ASSETS_TRANSFORM_MAX_OPERATIONS
      </code>
    </td>
    
    <td>
      The max number of transform operations that is allowed to be processed (excludes saved presets).
    </td>
    
    <td>
      <code>
        5
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        ASSETS_INVALID_IMAGE_SENSITIVITY_LEVEL
      </code>
    </td>
    
    <td>
      Level of sensitivity to invalid images. See the <a href="https://sharp.pixelplumbing.com/api-constructor#parameters" rel="nofollow">
        <code>
          sharp.failOn
        </code>
      </a>
      
       option.
    </td>
    
    <td>
      <code>
        warning
      </code>
    </td>
  </tr>
</tbody>
</table>

Image transformations can be heavy on memory usage. If you're using a system with 1GB or less available memory, we recommend lowering the allowed concurrent transformations to prevent you from overflowing your server.
