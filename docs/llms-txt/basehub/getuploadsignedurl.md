# getUploadSignedURL

> A helper to upload assets to our database.

This is useful for example, when we have a PNG on our machine that we want to use in a BaseHub Image block. In order to use it, you should:

### Call the `getUploadSignedURL` mutation

You will need to retrieve both the `signedURL` and the `uploadURL`.

### Do a PUT request to the `signedURL`

The `signedURL` is an authorized endpoint that allows you to send any allowed asset through it. You’ll use it to upload the files you want to use in your BaseHub blocks.

### Consume the uploaded data from `uploadURL`

The `uploadURL` is the path to the uploaded file. After sending the asset data to the `signedURL`, you will be able to see the file in this URL. You will use it in the block value when running a transaction mutation.

## Example

On this example we’re uploading a new image file to BaseHub assets pool.

You can explore the full code for this example in [Github](https://github.com/basehub-ai/mutations-api-example/blob/c4d1ccd2609598f707d58204ade29134fd283d8f/lib/mutate-action.ts#L16-L40).

```
export const uploadImageToBaseHub = async (imageInput: File) => {
  const { getUploadSignedURL } = await basehub().mutation({
    getUploadSignedURL: {
      __args: {
        fileName: imageInput.name,
      },
      signedURL: true,
      uploadURL: true,
    },
  });

  const uploadStatus = await fetch(getUploadSignedURL.signedURL, {
    method: "PUT",
    body: imageInput,
    headers: {
      "Content-Type": imageInput.type,
    },
  });

  if (uploadStatus.ok) {
    return getUploadSignedURL.uploadURL;
  }

  return null;
};
```