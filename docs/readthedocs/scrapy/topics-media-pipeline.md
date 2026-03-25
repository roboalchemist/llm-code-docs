# Downloading and processing files and images

Scrapy provides reusable item pipelines for
downloading files attached to a particular item (for example, when you scrape
products and also want to download their images locally). These pipelines share
a bit of functionality and structure (we refer to them as media pipelines), but
typically you’ll either use the Files Pipeline or the Images Pipeline.

Both pipelines implement these features:

- 

Avoid re-downloading media that was downloaded recently

- 

Specifying where to store the media (filesystem directory, FTP server, Amazon S3 bucket,
Google Cloud Storage bucket)

The Images Pipeline has a few extra functions for processing images:

- 

Convert all downloaded images to a common format (JPG) and mode (RGB)

- 

Thumbnail generation

- 

Check images width/height to make sure they meet a minimum constraint

The pipelines also keep an internal queue of those media URLs which are currently
being scheduled for download, and connect those responses that arrive containing
the same media to that queue. This avoids downloading the same media more than
once when it’s shared by several items.

## Using the Files Pipeline

The typical workflow, when using the `FilesPipeline` goes like
this:

- 

In a Spider, you scrape an item and put the URLs of the desired into a
`file_urls` field.

- 

The item is returned from the spider and goes to the item pipeline.

- 

When the item reaches the `FilesPipeline`, the URLs in the
`file_urls` field are scheduled for download using the standard
Scrapy scheduler and downloader (which means the scheduler and downloader
middlewares are reused), but with a higher priority, processing them before other
pages are scraped. The item remains “locked” at that particular pipeline stage
until the files have finish downloading (or fail for some reason).

- 

When the files are downloaded, another field (`files`) will be populated
with the results. This field will contain a list of dicts with information
about the downloaded files, such as the downloaded path, the original
scraped url (taken from the `file_urls` field), the file checksum and the file status.
The files in the list of the `files` field will retain the same order of
the original `file_urls` field. If some file failed downloading, an
error will be logged and the file won’t be present in the `files` field.

## Using the Images Pipeline

Using the `ImagesPipeline` is a lot like using the `FilesPipeline`,
except the default field names used are different: you use `image_urls` for
the image URLs of an item and it will populate an `images` field for the information
about the downloaded images.

The advantage of using the `ImagesPipeline` for image files is that you
can configure some extra functions like generating thumbnails and filtering
the images based on their size.

The Images Pipeline requires Pillow [https://github.com/python-pillow/Pillow] 8.3.2 or greater. It is used for
thumbnailing and normalizing images to JPEG/RGB format.

## Enabling your Media Pipeline

To enable your media pipeline you must first add it to your project
`ITEM_PIPELINES` setting.

For Images Pipeline, use:

```
ITEM_PIPELINES = {"scrapy.pipelines.images.ImagesPipeline": 1}

```