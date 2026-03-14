# Source: https://docs.ghost.org/admin-api/themes/uploading-a-theme.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.ghost.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Uploading a theme

To upload a theme ZIP archive, send a multipart formdata request by providing the `'Content-Type': 'multipart/form-data;'` header, along with the following field encoded as [FormData](https://developer.mozilla.org/en-US/docs/Web/API/FormData/FormData):

`file`: *[Blob](https://developer.mozilla.org/en-US/docs/Web/API/Blob) or [File](https://developer.mozilla.org/en-US/docs/Web/API/File)* The theme archive that you want to upload.

<RequestExample>
  ```bash  theme={"dark"}
  curl -X POST -F 'file=@/path/to/themes/my-theme.zip' -H "Authorization: Ghost $token" -H "Accept-Version: $version" https://{admin_domain}/ghost/api/admin/themes/upload
  ```
</RequestExample>


Built with [Mintlify](https://mintlify.com).