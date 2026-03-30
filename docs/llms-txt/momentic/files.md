# Source: https://momentic.ai/docs/files.md

> ## Documentation Index
> Fetch the complete documentation index at: https://momentic.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Files

## File upload

<Warning>
  The [File upload](/steps/file-upload) step registers an event listener to
  automatically upload a file when the native file picker dialog is opened. This
  step must be executed **before** the file picker dialog is opened, otherwise
  it will not work.
</Warning>

<Frame>
  <img src="https://mintcdn.com/momentic-docs/N47HcAM-4dLVFPuL/images/files/file-upload-step.png?fit=max&auto=format&n=N47HcAM-4dLVFPuL&q=85&s=18a263636ff01ebc54472f31b6a0a1e2" width="1248" height="1528" data-path="images/files/file-upload-step.png" />
</Frame>

### Cloud-hosted files

You can upload files to Momentic that are private and not accessible to the
public.

Select **Files** on the left sidebar and click on the **Upload file** button in
the top-right corner. You can upload any file type, including images, documents,
and more.

<Frame>
  <img src="https://mintcdn.com/momentic-docs/N47HcAM-4dLVFPuL/images/files/files-page.png?fit=max&auto=format&n=N47HcAM-4dLVFPuL&q=85&s=433eff2ccd3c2889efdc2ba77459306b" width="3620" height="2436" data-path="images/files/files-page.png" />
</Frame>

### Public files

<Info>
  Make sure the URL you provide is a direct link to the file. For example, if
  you want to upload an image, the URL should end with `.jpg`, `.png`, or
  another image file extension. If the URL does not point directly to a file,
  Momentic will not be able to access it.
</Info>

You can upload any files that has a publicly accessible URL. For example, this
is a URL for a `README.md` file of a public repository on GitHub:

[https://raw.githubusercontent.com/momentic-ai/momentic/main/README.md](https://raw.githubusercontent.com/momentic-ai/momentic/main/README.md)

### Local files

If you're using the Momentic CLI, you can also upload files from your local
machine.

Local files can be referenced by path. The path must be absolute or relative the
the root `momentic.config.yaml`.

## File download

You can download a file in a Momentic test by using a [Click](/steps/click) step
and configuring the **Wait for download** option. This will wait for the file to
be downloaded before proceeding to the next step. The default download timeout
is 10 seconds.

<Frame>
  <img src="https://mintcdn.com/momentic-docs/N47HcAM-4dLVFPuL/images/files/download.png?fit=max&auto=format&n=N47HcAM-4dLVFPuL&q=85&s=e2a980070a0d6983196be82b2f3488fd" width="1252" height="1592" data-path="images/files/download.png" />
</Frame>

Current limitations:

* Only one file can be downloaded per step.
* The maximum supported size is 50mb.
* Direct file manipulation (e.g., checking file names or formats) is not
  supported.


Built with [Mintlify](https://mintlify.com).