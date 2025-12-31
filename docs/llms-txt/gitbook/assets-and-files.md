# Source: https://gitbook.com/docs/help-center/editing-content/assets-and-files.md

# Assets and files

## Is there a storage limit for asset uploads?

We don’t have a set limit for the total number of assets in a space, but we reserve the right to block your account if we see any abuse. There is an upload limit of 50MB for each asset.

{% hint style="warning" %}

### Unexpected Error when uploading images

`Unexpected Error` \
\
Please note that there is a file size limitation for image uploads. Ensure your image is below the 50MB threshold.
{% endhint %}

### How can I upload assets that are bigger than 50 MB to GitBook?&#x20;

If you need to upload files larger than the 50MB limit, the best solution is to store them somewhere like Dropbox or Google Drive and add a link to them in GitBook.

### Can I upload and embed gifs in GitBook?

Yes, you can add gifs to your page in GitBook. There are two limitations to keep in mind:

* There is a 50MB upload limit on individual files in GitBook. If your gif is larger than 50MB you will need to reduce its size before you upload.
* There is a 200 frame limit per gif file. If your gif has more than 200 frames, you will need to reduce the number of frames before you upload.

{% hint style="info" %}
Any large file — gifs included — will slow the performance and loading time of your page. We recommend you avoid uploading and embedding large files directly to maximize performance.
{% endhint %}

***

## Can I embed an iframe in GitBook?

GitBook doesn't support direct embedding of external content using an HTML `<iframe>`.&#x20;

This is due to our content security policy.&#x20;

### How to embed a URL in GitBook?

If the external content is publicly available, you can embed it using the **Embed a URL** block instead or copy and past the link into an empty block and click `Enter`.

<figure><img src="https://content.gitbook.com/content/Ua3kTfM3iWAoECzM0u90/blobs/ZvjzOXsi8tmwWmLLGqTw/CleanShot%202024-01-31%20at%2010.38.02.gif" alt="" width="356"><figcaption><p>How to embed a URL in GitBook</p></figcaption></figure>

***

## Does GitBook Support MP4 files?

GitBook does support uploading MP4 files up to 100MB, but they **do not automatically embed as videos** — they will simply appear as links that users can click to open or download the video file.&#x20;

### How to embed video/MP4 files in GitBook

You can [embed videos](https://app.gitbook.com/s/NkEGS7hzeqa35sMXQZ4X/creating-content/blocks/embed-a-url) by uploading them to a publicly accessible platform, such as Google Drive or YouTube, and then copying and pasting the link into GitBook.

{% hint style="info" %}
GitBook can only embed URLs that are publicly accessible. **Private URLs will not display on your page.**
{% endhint %}

It is technically possible to upload a video to GitBook and then [embed that video](https://app.gitbook.com/s/LBGJKQic7BQYBXmVSjy0/editing-and-publishing-documentation/upload-and-embed-a-playable-video-into-your-gitbook-docs) on a page via its URL. However, this is not officially supported and is very inefficient for end-users who view the videos. The slower page load can also impact your SEO ranking.

***

## Why is my image not loading?

The "could not load image" issue occurs when the image has been modified or deleted from its source.

For instance, if you have embedded an image instead of uploading it as a file into GitBook, we rely on the URL to display the image on your page. If there are any changes or the image is removed from the source, this will result in the image not being displayed.

<figure><img src="https://content.gitbook.com/content/Ua3kTfM3iWAoECzM0u90/blobs/JcVOlosETvGxzhSUwNtK/CleanShot%202024-01-24%20at%2012.22.15@2x.png" alt=""><figcaption><p>Example of the "could not load image" error in the documentation</p></figcaption></figure>

### Resolving the "could not load image" issue.

Consider uploading the images directly to GitBook or if the URL under which the image was available has changed, update it in your space.

This error may also occur if you copy an image from one space into another because each space has its file directory. In this case, re-upload the image to your new space.

{% hint style="info" %}
You can see and review all assets uploaded to your GitBook space in the **Files** side panel. Open it by clicking on the image icon in the top right-hand corner.

Find out more about files in [our documentation](https://gitbook.com/docs/content-editor/blocks/insert-files).
{% endhint %}
