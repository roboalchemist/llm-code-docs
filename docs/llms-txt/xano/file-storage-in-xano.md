# Source: https://docs.xano.com/file-storage/file-storage-in-xano.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# File Storage In Xano

## How does file storage work?

In Xano, you are provided a separate "bucket" that can hold all of your files, whether these are files you are providing to your users, or files they are uploading to your application.

You can upload almost anything, from images, to documents and PDFs, and even audio / video.

File storage has two essential components:

* The files themselves

* Database records with metadata

While the files themselves are not stored in your database, if you choose to reference a file in a database record, it will be storing the **metadata**, or general information about the file, such as the filename, size, file type, and a URL to access the file.

<Tip>
  **Review all of the available functions for working with files&#x20;**[**here**](/the-function-stack/functions/file-storage)**.**
</Tip>

## Public vs Private Storage

It's important to note that files uploaded to Xano have static URLs — this means that once a user has a URL to a file stored in your Xano backend, that URL will always be accessible without any kind of authentication or other checks to determine if it should be accessed.

If you have files that you need to restrict access to, you should be utilizing [private file storage](/file-storage/private-file-storage) instead.

You can review all of your public and private files from the <img src="https://mintcdn.com/xano-997cb9ee/SGxJ0muPK3um9hNH/images/7a688f00-image.jpeg?fit=max&auto=format&n=SGxJ0muPK3um9hNH&q=85&s=228620bebc1f3bcd74ac6b71955b7ae8" className="inline m-0" width="92" height="36" data-path="images/7a688f00-image.jpeg" /> section in the left-side navigation menu.

## File Management

The File section enables you to view and manage all of the files (images, videos, audio files, and attachments) in your workspace. You can easily see and search the files of your workspace and see the file name, mime type, size, and date it was created.

<Frame>
  <iframe src="https://demo.arcade.software/rn7KwVPLzSWaIwKSn4Lp?embed" title="https://demo.arcade.software/rn7KwVPLzSWaIwKSn4Lp?embed" allowFullScreen allow="clipboard-write" class="contentkit-webframe" width="1000" height="500" />
</Frame>

If a file appears in this section, then it is included in the overall media storage of your plan. Files will be added here once one of the following happens:

1. Uploading a file directly to the database.
2. Uploading a file directly to the File page.
3. Creating Metadata for any type of file in the function stack.

<Warning>
  Files do not need to be added to your database to be a file of your workspace. Creating the metadata of a file through the function stack associates that file with your workspace - even if you do not add it to a record in one of your database tables.
</Warning>


Built with [Mintlify](https://mintlify.com).