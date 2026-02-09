# Source: https://docs.warp.dev/agent-platform/agent/using-agents/agent-context/images-as-context.md

# Images as Context

## **Attaching images as context**

To provide visual context, you can attach images directly to an agent prompt. This is useful for including screenshots, diagrams, or other visual references alongside your query.

You can attach images in the following ways:

* Using the **image upload button** found on the toolbelt (either on the bottom left or right), depending on which input mode you're using:

<figure><img src="https://769506432-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FAULCelT4yIUOcSwWWvPk%2Fuploads%2Fgit-blob-80b86c4c1b497d18e27403dba7a5e4b75eb61536%2Fimage-as-context-universal.png?alt=media" alt=""><figcaption><p>Attaching 5 images on the new "Universal" input (bottom left toolbelt)</p></figcaption></figure>

<figure><img src="https://769506432-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FAULCelT4yIUOcSwWWvPk%2Fuploads%2Fgit-blob-9df3481f3deeeeae681bad2f4699b0194e69a91b%2Fimage-as-context-classic.png?alt=media" alt=""><figcaption><p>Attaching 4 images on the "Classic" input (bottom right)</p></figcaption></figure>

* Copy and paste images directly (e.g. right-click an image > "Copy image" or copy from a file manager) into Warp.
* Drag and drop images, such as from a file manager or screenshot utility.

{% hint style="info" %}
Warp accepts the following image formats: `.jpg` , `.jpeg` , `.png` , `.gif` , and .`webp` .
{% endhint %}

You can attach up to **5 images per request**, and up to **20 images across a single conversation**. Each image is sent to the model provider and immediately discarded — nothing is stored on Warp's servers.

### Model behavior and image handling

All supported models listed in [Model Choice](https://docs.warp.dev/agent-platform/agent/using-agents/model-choice) can interpret image input.

Attaching images will consume additional requests, proportional to the number of images added. To stay within model limits, Warp will intelligently resize images before passing it as context, minimizing token usage and respecting the model's maximum image dimensions.
