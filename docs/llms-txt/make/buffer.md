# Source: https://developers.make.com/custom-apps-documentation/block-elements/parameters/buffer.md

# Source: https://developers.make.com/custom-apps-documentation/component-blocks/api/buffer.md

# Buffer

Buffer is useful for handling files in download or upload modules.

Most APIs use the multipart/form-data content format to upload files and this works seamlessly with buffer types in Make.

## Download a file

The Download a file module downloads a file from the service with data type `buffer` in the interface.

{% tabs %}
{% tab title="Occurrence in a module" %}

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-91066c4cc0a831dd70c776ecbd03f453963a5a05%2Fbuffer_download1.png?alt=media" alt="" width="332"><figcaption></figcaption></figure></div>

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-f955a2b4a71142e7ca8b96a47071dc204bc14440%2Fbuffer_download2.png?alt=media" alt="" width="323"><figcaption></figcaption></figure></div>

{% hint style="info" %}
The parameters are correctly evaluated and automatically pre-mapped in the file input dialog in the following module that accepts `buffer` with the file's name and data.
{% endhint %}
{% endtab %}

{% tab title="Interface" %}

<pre class="language-json"><code class="lang-json">[
<strong>    {
</strong>        "name": "name",
        "type": "filename",
        "label": "Name",
        "semantic": "file:name"
    },
    {
        "name": "data",
        "type": "buffer",
        "label": "Data",
        "semantic": "file:data"
    }

]
</code></pre>

{% endtab %}
{% endtabs %}

## Upload a file

The Upload a file module uploads a file to the service with data type `buffer` in mappable parameters and type [`multipart/form-data` in communication](https://developers.make.com/custom-apps-documentation/component-blocks/api/multipart-form-data)**.**
