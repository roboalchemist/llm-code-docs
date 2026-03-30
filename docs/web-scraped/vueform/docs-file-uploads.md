# Source: https://vueform.com/docs/file-uploads

Title: File Uploads | Vueform | Open-Source Form Framework for Vue

URL Source: https://vueform.com/docs/file-uploads

Markdown Content:
Learn how to upload files with Vueform.

Vueform's file upload can be configured in many ways in order to achieve different upload flows:

*   **[Upload temporary files](https://vueform.com/docs/file-uploads#uploading-files)** when the user selects them and only persist on form submit without having send over all the files again.
*   **[Upload files instantly](https://vueform.com/docs/file-uploads#skipping-temporary-upload-state)** and have them persist after the user selects them and issue a remove call to the backend if they choose to remove them later.
*   **[Upload files on form submit](https://vueform.com/docs/file-uploads#send-files-on-form-submit-only)** and have them sent along with form data.

Uploading Files [​](https://vueform.com/docs/file-uploads#uploading-files)
--------------------------------------------------------------------------

By default Vueform's `FileElement` will issue a request to `upload-temp-endpoint` when the user selects a file:

vue

`<FileElement upload-temp-endpoint="/store-temp-files" />`

### Disabling Auto-Uploading [​](https://vueform.com/docs/file-uploads#disabling-auto-uploading)

To disable issuing a request instantly on file select, we can set `auto` to `false`:

vue

```
<FileElement
  upload-temp-endpoint="/store-temp-files"
  :auto="false"
/>
```

In this case the user will have to press an `Upload` button to upload files. If files are not uploaded by the time the form is submitted, they will be force uploaded to their endpoints in separate request(s) during [prepare](https://vueform.com/docs/handling-form-data#preparing-for-submit) hook, before form data is sent.

### Upload Request [​](https://vueform.com/docs/file-uploads#upload-request)

The backend receives the following payload on submitting files to the endpoint:

js

```
{
  file: '(binary)', // file binary
  formKey: '...', // the form-key prop defined for `Vueform`
  path: 'file', // the full path of the file element
}
```

### Upload Response [​](https://vueform.com/docs/file-uploads#upload-response)

After storing the file temporarily on our backend, the backend has to return a JSON in the following format:

js

```
const responseBody = {
  tmp: 'y8wre123.pdf', // temp file name
  originalName: 'contract.pdf', // the original file name
}
```

Once we receive the response from the backend the response body will be set as element value which will be sent as the file value when the form is submitted. It can be used to identify the temp file and make it persist when the form is submitted.

### Skipping Temporary Upload State [​](https://vueform.com/docs/file-uploads#skipping-temporary-upload-state)

If we want to skip the temporary uploaded file state, the backend can return the final filename as a `string`:

js

`const responseBody = 'final-file.pdf'`

### Changing Upload Request Method [​](https://vueform.com/docs/file-uploads#changing-upload-request-method)

By default, file upload requests are using `POST` method, which can be changed by providing an object for `upload-temp-endpoint` prop:

vue

```
<FileElement :upload-temp-endpoint="{
  url: '/user/temp-files',
  method: 'PATCH',
}" />
```

### Custom Upload Handling [​](https://vueform.com/docs/file-uploads#custom-upload-handling)

We can also define an `async function` instead of a `string` endpoint for `upload-temp-endpoint`:

vue

```
<FileElement :upload-temp-endpoint="async (value, el$) => {
  const response = await el$.$vueform.services.axios.request({
    url: 'https://my-image-server.com/api/upload-temp',
    method: 'POST',
    data: el$.form$.convertFormData({
      file: value,
    }),
    onUploadProgress: (e) => {
      el$.progress = Math.round((e.loaded * 100) / e.total)
    },
    cancelToken: el$.$vueform.services.axios.CancelToken.source().token,
  }) // errors are handled automatically

  return response.data
}" />
```

### Global Upload Endpoint Config [​](https://vueform.com/docs/file-uploads#global-upload-endpoint-config)

When `upload-temp-endpoint` is not specified, its [config value](https://vueform.com/docs/configuration#endpoints) will be used from `vueform.config.js`. We can use this to set the endpoint globally:

js

```
// vueform.config.js

import { defineConfig } from '@vueform/vueform'

export default defineConfig({
  endpoints: {
    uploadTempFile: {
      url: '/vueform/file/upload-temp',
      method: 'POST',
    },
    // or
    uploadTempFile: async (value, el$) => {
      // ...
    }
  }
})
```

### Adding Params to Requests [​](https://vueform.com/docs/file-uploads#adding-params-to-requests)

We can add params to our request with [`params`](https://vueform.com/reference/file-element#option-params) when submitting to `upload-temp-endpoint`:

vue

```
<FileElement upload-temp-endpoint="/store-temp-files" :params="{
  foo: 'bar',
}" />
```

The backend will receive:

js

```
{
  file: '(binary)', // file binary
  formKey: '...', // the form-key prop defined for `Vueform`
  path: 'file', // the full path of the file element
  foo: 'bar', // our custom param
}
```

### Send Files on Form Submit Only [​](https://vueform.com/docs/file-uploads#send-files-on-form-submit-only)

If we don't want to have separate requests to upload files, but send them along with other form data upon submit, we can simply set `upload-temp-endpoint` to `false`:

vue

`<FileElement :upload-temp-endpoint="false" />`

We can also disable separate file upload requests on a config level:

js

```
// vueform.config.js

import { defineConfig } from '@vueform/vueform'

export default defineConfig({
  endpoints: {
    uploadTempFile: false
  }
})
```

### Restrict Accepted File Types [​](https://vueform.com/docs/file-uploads#restrict-accepted-file-types)

Accepted file types can be restricted by listing extensions or [MIME types](https://www.iana.org/assignments/media-types/media-types.xhtml) separated by comma:

vue

```
<!-- Extensions -->
<FileElement accept=".jpg,.png,.gif" />

<!-- MIME Types -->
<FileElement accept="image/jpeg,image/png,image/gif" />

<!-- MIME Type Groups -->
<FileElement accept="image/*,video/*" />
```

### Uploading Multiple Files [​](https://vueform.com/docs/file-uploads#uploading-multiple-files)

Multiple files can be uploaded using [`MultifileElement`](https://vueform.com/reference/multifile-element):

vue

`<MultifileElement upload-temp-endpoint="/store-temp-files" />`

When using `MultifileElement` each files will be uploaded in separate requests to `upload-temp-endpoint`.

### Sorting Files [​](https://vueform.com/docs/file-uploads#sorting-files)

When [uploading multiple files](https://vueform.com/docs/file-uploads#uploading-multiple-files) they can be sorted when `sort: true`:

vue

`<MultifileElement sort view="image" />`

### File Validation [​](https://vueform.com/docs/file-uploads#file-validation)

We can add validation rules to files restricting its size or even [dimensions](https://vueform.com/docs/validating-elements#rule-dimensions) when uploading images:

vue

```
<FileElement :rules="[
  'min:1024', // min 1 MB file size
  'max:4096', // max 4 MB file size

  // image dimension constraints
  'dimensions:min_width=100,min_height=100,max_witdh=1000,max_height=1000,ratio=2/3',
  'dimensions:width=1024,height=768', // fixed size
]"
/>
```

When [uploading multiple files](https://vueform.com/docs/file-uploads#uploading-multiple-files) the rules concerning one file instance should be passed via `file` prop:

vue

```
<MultifileElement
  :rules="[ // APPLIES FOR MULTIFILE ELEMENT
    'min:1', // min 1 file needs to be selected
    'max:5', // max 5 files can be selected
  ]"
  :file="{
    rules: [ // APPLIES FOR SINGLE FILES
      'min:1024', // min 1 MB file size
      'max:4096', // max 4 MB file size
      // ...
    ]
  }"
/>
```

### File Options [​](https://vueform.com/docs/file-uploads#file-options)

We can pass other file options eg. `label` to single files when using `MultifileElement` via `file` prop:

vue

```
<MultifileElement
  :file="{
    // ...
  }"
/>
```

The `MulfifileElement` behaves as a `ListElement` containing `FileElement` instances. With `file` prop we can pass options to each `FileElement`.

### Drop Area [​](https://vueform.com/docs/file-uploads#drop-area)

We can set `drop: true` to display a drop area instead of file upload button for both `FileElement` and `MultifileElement`:

vue

`<MultifileElement drop />`

### Image Upload Diagram [​](https://vueform.com/docs/file-uploads#image-upload-diagram)

Here's the full diagram of the image upload process:

![Image 1: Vueform File Upload Diagram](https://vueform.com/images/vueform-file-upload-diagram.svg)

File Preview [​](https://vueform.com/docs/file-uploads#file-preview)
--------------------------------------------------------------------

The `FileElement` and `MultifileElement` has different [alternative views](https://vueform.com/docs/styles-and-layout#alternative-views) which can be used with `view` prop:

#### default [​](https://vueform.com/docs/file-uploads#default)

vue

`<FileElement />`

#### image [​](https://vueform.com/docs/file-uploads#image)

vue

`<FileElement view="image" />`

#### gallery [​](https://vueform.com/docs/file-uploads#gallery)

vue

`<FileElement view="gallery" />`

### Clicking Files [​](https://vueform.com/docs/file-uploads#clicking-files)

The files are not clickable until they are persisted on our server (`stage: 3`). Once they are persisted, their URL will be composed from the file value (eg. `file.pdf`) prefixed with [`url`](https://vueform.com/reference/file-element#option-url), which is `/` by default.

If `url` is not specified for our `FileElement` the file will be opened in a new tab using `/file.pdf` URL.

If `url` is specified eg. `https://cdn.domain.com/files/` the URL will become `https://cdn.domain.com/files/file.pdf`:

vue

```
<!-- Click URL: https://cdn.domain.com/files/file.pdf -->
<FileElement url="https://cdn.domain.com/files/" />
```

If the `url` is `false` the URL will be `file.pdf`:

vue

```
<!-- Click URL: file.pdf -->
<FileElement :url="false" />
```

If we want to turn off clickable links on files we can set `clickable: false`:

vue

```
<!-- The file won't be clickable -->
<FileElement :clickable="false" />
```

Here are some of the most common combinations for file click URL settings:

| Filename | `url` | Click path |
| --- | --- | --- |
| `file.png` | - (`/`) | `/file.png` |
| `file.png` | `false` | `file.png` |
| `file.png` | `/files/` | `/files/file.png` |
| `file.png` | `https://cdn.com/` | `https://cdn.com/file.png` |
| `https://cdn.com/file.png` | `false` | `https://cdn.com/file.png` |

### Preview Images [​](https://vueform.com/docs/file-uploads#preview-images)

Before images are persisted on the server (`stage < 3`) the previews are converted to `base64` and loaded to `<img>` tag's `src` attribute.

Once the files are uploaded (their value is a `string`, `stage: 3`) they will be loaded using their string value, prefixed with [`url`](https://vueform.com/reference/file-element#option-url) or [`previewUrl`](https://vueform.com/reference/file-element#option-preview-url) prop.

If `previewUrl` is not defined then `url` will be used, which is also used for creating [click URL](https://vueform.com/docs/file-uploads#clicking-preview-files).

The `url` prop is `/` by default, so if neither `url` or `previewUrl` is set and our `FileElement`'s value is `file.png` it will be loaded from `/file.png`.

If `url` or `previewUrl` is set to eg. `https://cdn.domain.com/images/` the preview will be loaded from `https://cdn.domain.com/images/file.png`.

If the `url` is `false` and `previewUrl` is not defined, the file will not have a prefix (`file.png`).

Here are some of the most common combinations for image preview settings:

| Filename | `url`_(click)_ | `previewUrl` | Click path | Preview path |
| --- | --- | --- | --- | --- |
| `file.png` | - (`/`) | - | `/file.png` | `/file.png` |
| `file.png` | `false` | - | `file.png` | `file.png` |
| `file.png` | `/files/` | - | `/files/file.png` | `/files/file.png` |
| `file.png` | - (`/`) | `/thumbnails/` | `/file.png` | `/files/file.png` |
| `file.png` | `/files/` | `/thumbnails/` | `/files/file.png` | `/thumbnails/file.png` |
| `https://cdn.com/x.png` | `false` | - | `https://cdn.com/x.png` | `https://cdn.com/x.png` |

### Custom File Previews [​](https://vueform.com/docs/file-uploads#custom-file-previews)

If we need a custom file preview (eg. to render PDFs) we can create an [alternative view](https://vueform.com/docs/styles-and-layout#alternative-views).

Removing Files [​](https://vueform.com/docs/file-uploads#removing-files)
------------------------------------------------------------------------

When files are **uploaded in a temporary state**, meaning their value is an object containing `tmp` and `originalName` (`stage: 2`) they will issue a request to `remove-temp-endpoint` when removed:

vue

`<FileElement remove-temp-endpoint="/remove-temp-file">`

When files are **persisted**, meaning their value is a string containing the filename (`stage: 3`) they will issue a request to `remove-endpoint` when removed.

vue

`<FileElement remove-endpoint="/remove-file">`

> Remove requests are only issued if the file is **explicitly removed** by the user and **not** when eg. resetting, clearing or updating form data.

### Remove Request [​](https://vueform.com/docs/file-uploads#remove-request)

The backend receives the following data when submitting to `remove-temp-endpoint` or `remove-endpoint`:

js

```
{
  file: '(binary)', // file binary
  formKey: '...', // the form-key prop defined for `Vueform`
  path: 'file', // the full path of the file element
}
```

### Remove Response [​](https://vueform.com/docs/file-uploads#remove-response)

The response should have a `2XX` HTTP code and does not require any specific response. If the response is outside ot `2XX` the remove attempt will be considered failed and the file will not change its value.

### Changing Remove Request Method [​](https://vueform.com/docs/file-uploads#changing-remove-request-method)

By default, file remove requests are using `POST` method, which can be changed by providing an object for `remove-temp-endpoint` or `remove-endpoint` props:

vue

```
<FileElement
  :remove-temp-endpoint="{
    url: '/user/temp-files',
    method: 'DELETE',
  }"
  :remove-endpoint="{
    url: '/user/files',
    method: 'DELETE',
  }"
/>
```

### Custom Remove Handling [​](https://vueform.com/docs/file-uploads#custom-remove-handling)

We can also define an `async function` instead of a `string` endpoint for `:remove-temp-endpoint` and `:remove-endpoint`:

vue

```
<FileElement
  :remove-temp-endpoint="async (value, el$) => {
    await el$.$vueform.services.axios.request({
      url: 'https://my-image-server.com/api/remove-temp',
      method: 'POST',
      data: el$.form$.convertFormData({
        file: value,
      }),
    }) // errors are handled automatically
  }"
  :remove-endpoint="async (value, el$) => {
    // same as above
  }"
/>
```

### Global Remove Endpoints Config [​](https://vueform.com/docs/file-uploads#global-remove-endpoints-config)

When `:remove-temp-endpoint` and `:remove-endpoint` are not specified, their [config value](https://vueform.com/docs/configuration#endpoints) will be used from `vueform.config.js`. We can use this to set the endpoints globally:

js

```
// vueform.config.js

import { defineConfig } from '@vueform/vueform'

export default defineConfig({
  endpoints: {
    removeTempFile: {
      url: '/vueform/file/remove-temp',
      method: 'POST',
    },
    removeFile: {
      url: '/vueform/file/remove',
      method: 'POST',
    },
    // or
    removeTempFile: async (value, el$) => {
      // ...
    },
    removeFile: async (value, el$) => {
      // ...
    },
  }
})
```

### Adding Params to Requests [​](https://vueform.com/docs/file-uploads#adding-params-to-requests-1)

We can add params to our request with [`params`](https://vueform.com/reference/file-element#option-params) when submitting to `remove-temp-endpoint` or `remove-endpoint`:

vue

```
<FileElement ... :params="{
  foo: 'bar',
}" />
```

The backend will receive:

js

```
{
  file: '(binary)', // file binary
  formKey: '...', // the form-key prop defined for `Vueform`
  path: 'file', // the full path of the file element
  foo: 'bar', // our custom param
}
```

### Soft Remove [​](https://vueform.com/docs/file-uploads#soft-remove)

If we don't want to issue separate requests when users delete files, we can set `:soft-remove` to `true`:

vue

`<FileElement soft-remove />`

Alternatively, we can disable `remove-temp-endpoint` or `remove-endpoint` separately by setting them to `false`:

vue

```
<!-- Don't issue a request on removing temp file -->
<FileElement :remove-temp-endpoint="false" />

<!-- Don't issue a request on removing persisted file -->
<FileElement :remove-endpoint="false" />
```

We can also disable separate file remove requests on a config level:

js

```
// vueform.config.js

import { defineConfig } from '@vueform/vueform'

export default defineConfig({
  endpoints: {
    removeTempFile: false,
    removeFile: false,
  }
})
```

Loading Files [​](https://vueform.com/docs/file-uploads#loading-files)
----------------------------------------------------------------------

To load files to the form, we can simply set their filenames as values for `FileElement` or `MultifileElement`:

Composition API Options API

vue

```
<template>
  <Vueform ref="form$">
    <FileElement name="file" />
    <MultifileElement name="files" />
  </Vueform>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const form$ = ref(null)

onMounted(() => {
  form$.value.load({
    file: 'filename.png',
    files: [
      'file1.pdf',
      'file2.docx',
      'file3.mp3',
    ]
  })
})
</script>
```

vue

```
<template>
  <Vueform ref="form$">
    <FileElement name="file" />
    <MultifileElement name="files" />
  </Vueform>
</template>

<script>
export default {
  mounted() {
    this.$refs.form$.load({
      file: 'filename.png',
      files: [
        'file1.pdf',
        'file2.docx',
        'file3.mp3',
      ]
    })
  }
}
</script>
```

When images are loaded the previews will be composed of the loaded value for the file prefixed with `url` or `previewUrl` as we learned in [Previewing Images](https://vueform.com/docs/file-uploads#preview-images) section.

👋**Hire Vueform team** for form customizations and development

[Learn more](https://vueform.dev/)
