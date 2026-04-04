# Source: https://docs.ideogram.ai/using-ideogram/features-and-tools/upscale.md

# Upscale

The Upscale feature, available to users on the **Basic Plan** or higher, increases the resolution of your Ideogram-generated images, and of any images you’ve uploaded using the [Image Upload](https://docs.ideogram.ai/canvas-and-editing/image-upload) function (available on the **Plus Plan** or higher), by up to **2×**.

{% hint style="warning" %}
**Important:** Upscale **crops** images to the nearest supported aspect ratio listed in the table below. This behavior applies to all images, including both default and custom aspect ratios used in Ideogram v2.0 and later.
{% endhint %}

Aspect ratios and their final pixel dimensions after upscaling:

| Aspect ratio | Final dimensions (pixels) |
| :----------: | :-----------------------: |
|   **`1:3`**  |        1024 x 3072        |
|  **`9:16`**  |        1440 x 2560        |
|  **`10:16`** |        1536 x 2464        |
|   **`2:3`**  |        1536 x 2304        |
|   **`3:4`**  |        1536 x 2048        |
|   **`1:1`**  |        2048 x 2048        |
|   **`4:3`**  |        2048 x 1536        |
|   **`3:2`**  |        2304 x 1536        |
|  **`16:10`** |        2464 x 1536        |
|  **`16:9`**  |        2560 x 1440        |
|   **`3:1`**  |        3072 x 1024        |

**Example 1** — If you upload an image that is 1500 pixels by 1500 pixels, which has an aspect ratio of 1:1, the upscale will result in a 2048 pixels by 2048 pixels image.&#x20;

**Example 2** — If you generate an image with a custom aspect ratio of 17:12 (1088 × 768 pixels) and then use *Upscale*, the image will be cropped it to the nearest available aspect ratio, which is 3:2, and the final image will be 2304 pixels by 1536 pixels.

## Upscaling an Image

You can access Upscale in several ways:

1. **From image feeds** (Home and Creations pages) –\
   Hover over any image in the [Image Gallery](https://docs.ideogram.ai/using-ideogram/ui-overview/ui-components/image-gallery), select the **More** icon <picture><source srcset="https://1799634369-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzjhNby3LLsIikYuvxAJP%2Fuploads%2FPYS9T78uhmDmuEqNWvcb%2FMore%20-%20White%2020px.svg?alt=media&#x26;token=cba9b268-f5f2-4895-bef0-fa43e5ae3724" media="(prefers-color-scheme: dark)"><img src="https://1799634369-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzjhNby3LLsIikYuvxAJP%2Fuploads%2FqhNBoUUnrp0grTzHJonA%2FMore%20-%20Black%2020px.svg?alt=media&#x26;token=dee426ba-09fe-4735-bdd3-81c5ecb71035" alt=""></picture> at the top of the image, and select **Upscale** from the [More menu](https://docs.ideogram.ai/using-ideogram/ui-overview/ui-components/more-menu-...).
2. **From image details** –\
   In the [Details Panel](https://docs.ideogram.ai/using-ideogram/ui-overview/ui-components/details-panel), select the **Upscale** button.\
   Alternatively, select the **More** icon <picture><source srcset="https://1799634369-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzjhNby3LLsIikYuvxAJP%2Fuploads%2FPYS9T78uhmDmuEqNWvcb%2FMore%20-%20White%2020px.svg?alt=media&#x26;token=cba9b268-f5f2-4895-bef0-fa43e5ae3724" media="(prefers-color-scheme: dark)"><img src="https://1799634369-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzjhNby3LLsIikYuvxAJP%2Fuploads%2FqhNBoUUnrp0grTzHJonA%2FMore%20-%20Black%2020px.svg?alt=media&#x26;token=dee426ba-09fe-4735-bdd3-81c5ecb71035" alt=""></picture> in the upper-right corner and choose **Upscale** from the More menu.
3. **When** [importing an image](https://docs.ideogram.ai/ui-overview/ui-components/prompt-box#importing-an-image) **into the** [Prompt Box](https://docs.ideogram.ai/using-ideogram/ui-overview/ui-components/prompt-box) –\
   In the popup window, select **Upscale** to generate an automatic description.

## Parameters

To adjust settings, select the Upscale thumbnail in the [Prompt Box](https://docs.ideogram.ai/using-ideogram/ui-overview/ui-components/prompt-box). A pop-up window appears, allowing you to fine-tune the **Resemblance** and **Detail** parameters. You also have the option to [Describe](https://docs.ideogram.ai/using-ideogram/features-and-tools/describe) the image or to edit it in the [Editor](https://docs.ideogram.ai/canvas-and-editing/editor) before applying the upscale.

Upscale lets you control how much **Resemblance** the new image retains from the original, and how much **Detail** the AI adds during generation.

Select the **Upscale** thumbnail in the Prompt Box to open its options.

<figure><picture><source srcset="https://1799634369-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzjhNby3LLsIikYuvxAJP%2Fuploads%2FFAmj1AsrRSLOGR96oWDA%2FPB%20-%20Upscale%20Settings%20-%20Dark%402x.png?alt=media&#x26;token=d24a7786-2677-48c9-814a-18a56ddee104" media="(prefers-color-scheme: dark)"><img src="https://1799634369-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzjhNby3LLsIikYuvxAJP%2Fuploads%2FI8NpPdJ9jKtSw6xAeeI1%2FPB%20-%20Upscale%20Settings%20-%20Light%402x.png?alt=media&#x26;token=93271bf2-c168-4054-b54f-e6e942fbb169" alt="Adjustable Upscale parameters: Resemblance and Detail." width="220"></picture><figcaption><p>Adjustable Upscale parameters: Resemblance and Detail.</p></figcaption></figure>

### Resemblance

This parameter determines how closely you want the enlarged image to resemble the original. A value of 1 allows the AI more freedom to be creative with the image, which can be useful for correcting certain defects or enhancing specific details. On the other hand, a value of 100 will produce a result that is as close as possible to the original image while still enlarging it and maintaining optimal sharpness.

<div><figure><img src="https://1799634369-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzjhNby3LLsIikYuvxAJP%2Fuploads%2FzIZIacsLta0mNNbsTpmR%2FDog-Orig-vs-1.webp?alt=media&#x26;token=44085eff-d01d-4a3a-a8e5-ba40e015738e" alt=""><figcaption><p>Original compared to an upscaled image with a Resemblance value of 1</p></figcaption></figure> <figure><img src="https://1799634369-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzjhNby3LLsIikYuvxAJP%2Fuploads%2F18wFFYfgSJiUxTR6N1iy%2FDog-Orig-vs-100.webp?alt=media&#x26;token=f985c250-9cae-4d91-b068-1f9a59afd4c0" alt=""><figcaption><p>Animation of the original image compared to an upscaled image generated with a Resemblance value of 100</p></figcaption></figure></div>

### Detail Slider

This slider allows you to adjust the level of detail in the enlarged image. A higher value will increase the visibility of details, while a lower value will reduce them.

**Detail value: 1 vs 100**

<figure><img src="https://1799634369-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzjhNby3LLsIikYuvxAJP%2Fuploads%2FbPhj4woVM1DnAbUnEiN0%2FDog%20Detail%20Compare.webp?alt=media&#x26;token=1ff00210-115a-47ce-9df8-e1703a74470b" alt="" width="563"><figcaption><p>Animation of two upscaled images generated with a Detail value of 1 compared to the same generated with a value of 100.</p></figcaption></figure>

After adjusting both sliders to your desired values, click or tap the **Upscale** button to begin the process.

Once the upscaling is complete, you can click on the image preview to get a more detailed view of the upscaled image.

Select the **Split View** icon <picture><source srcset="https://1799634369-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzjhNby3LLsIikYuvxAJP%2Fuploads%2FZHGC1o58ae969aXjN28C%2FSplit%20View%20Icon%20-%20Dark%2020px.svg?alt=media&#x26;token=0a61b006-2ad0-4949-8605-733b325000b7" media="(prefers-color-scheme: dark)"><img src="https://1799634369-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzjhNby3LLsIikYuvxAJP%2Fuploads%2FTBn5uHVNf7Yx6KWPRYuA%2FSplit%20View%20Icon%20-%20Light%2020px.svg?alt=media&#x26;token=7d574d18-4539-43d6-a171-dc4f1a38fee0" alt=""></picture> in the upper-right corner to open an interactive comparison slider between the original and upscaled images.

<figure><img src="https://1799634369-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzjhNby3LLsIikYuvxAJP%2Fuploads%2FdlVV1ZYOAO9ftZgltiTj%2FDog-Split.webp?alt=media&#x26;token=b35deb9a-1fdd-485e-af99-39b44866915a" alt=""><figcaption><p>Using the split view function.</p></figcaption></figure>

You can view the final image dimensions and the parameters used during upscaling in the [Details panel](https://docs.ideogram.ai/using-ideogram/ui-overview/ui-components/details-panel).&#x20;

<figure><picture><source srcset="https://1799634369-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzjhNby3LLsIikYuvxAJP%2Fuploads%2F8kb7YuXNLWRW9UJHYyGT%2FImage%20Info%20-%20Dark%402x.png?alt=media&#x26;token=26b60b6a-644f-4db1-b4b2-593c4a96fe7c" media="(prefers-color-scheme: dark)"><img src="https://1799634369-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzjhNby3LLsIikYuvxAJP%2Fuploads%2Fi8FgDf5EPeF8F5sEBPNm%2FImage%20Info%20-%20Light%402x.png?alt=media&#x26;token=83818b9d-2a9e-4007-a7c0-cb11c02bf243" alt="" width="352"></picture><figcaption><p>Information availableIn the Details panel when viewing an upscaled image.</p></figcaption></figure>

{% hint style="info" %}
**Note:** Images can currently be upscaled up to **2×**. Additional scaling options may be introduced in future updates.
{% endhint %}
