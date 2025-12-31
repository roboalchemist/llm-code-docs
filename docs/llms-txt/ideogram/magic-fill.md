# Source: https://docs.ideogram.ai/canvas-and-editing/canvas/magic-fill.md

# Magic Fill

Magic Fill, also known as inpainting, allows you to modify a part of an image while keeping the rest intact.

Using Magic Fill is a simple two-step process:

1. Create a mask using the [**Masking Tools**](https://docs.ideogram.ai/canvas-and-editing/canvas-overview#masking-options) over the areas you want to modify.
2. Adjust the generation window and available options in the **Prompt box**, then click **Magic Fill**.

## How to Use Magic Fill

### Replacing and Adding an Element

In the example below, the glass of water will be replaced by a glass of milk while a watch will be added to her left wrist.

<figure><img src="https://1799634369-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzjhNby3LLsIikYuvxAJP%2Fuploads%2FIL3fqLAebEhH8eeHqiO1%2FIdeogram%20-%20Light%20Dark%402x.png?alt=media&#x26;token=1ad34626-69ef-47b2-b63d-7978e25abc95" alt="" width="375"><figcaption><p>The original image to be modified.</p></figcaption></figure>

Here’s how:

1. Click the Magic Fill button on the left-side panel.
2. Using the [**Masking Tools**](https://docs.ideogram.ai/canvas-and-editing/canvas-overview#masking-options)**,** Mask the hand holding the glass of water and the area where the watch should be placed.

<figure><img src="https://1799634369-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzjhNby3LLsIikYuvxAJP%2Fuploads%2Fm6iirTJ3hzg8bAIkroVp%2FIdeogram%20-%20Light%20Dark%402x.png?alt=media&#x26;token=5343992a-66c4-44d2-8372-154ccb8316ba" alt="" width="375"><figcaption><p>The masked <strong>areas</strong> of the image.</p></figcaption></figure>

3. Click Next to access the Magic Fill options at the top of the canvas.
4. Adjust the generation window to include both masked areas and some surrounding image content for context. In this case, the whole image area was used.
5. Enter a prompt describing the scene and the desired modifications. In this example:\
   `A photo of a middle-aged woman with short hair holding a glass of milk in a modern, white kitchen with wooden countertops. She is wearing a blue shirt, a necklace and a watch...`

<figure><picture><source srcset="https://1799634369-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzjhNby3LLsIikYuvxAJP%2Fuploads%2F887agoJrooCstOeEv8Pd%2FMadame%20Cafe%CC%81%20%E2%80%93%20Ideogram%20-%20Light%20Dark%402x.png?alt=media&#x26;token=3463dc08-84ed-45d7-a836-016a80af4fa2" media="(prefers-color-scheme: dark)"><img src="https://1799634369-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzjhNby3LLsIikYuvxAJP%2Fuploads%2FMY0KSeB0JSUbqmkOxBkI%2FMadame%20Cafe%CC%81%20%E2%80%93%20Ideogram%20-%20Light%20Dark%402x.png?alt=media&#x26;token=57fe38f0-c389-4754-b7bd-56aad866732e" alt=""></picture><figcaption></figcaption></figure>

* Adjust additional options as desired.
* Click Magic Fill to generate the images.
* Select the image and use the arrows at the bottom to view all generated images.

<figure><img src="https://1799634369-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzjhNby3LLsIikYuvxAJP%2Fuploads%2FZyLTUnjqeJfL1HCxi5eu%2FCanvas%20-%20Magic%20Fill%20Results.webp?alt=media&#x26;token=6b790120-d8ca-4724-893c-453e215cca4d" alt="" width="375"><figcaption><p>The four generated images.</p></figcaption></figure>

***

### Adding Elements

In the example below, an image of a rabbit was generated first in Ideogram as a starting image. Using Magic Fill, a basket of carrots is added in the background, and a carrot is placed in front of the rabbit.

<div><figure><img src="https://1799634369-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzjhNby3LLsIikYuvxAJP%2Fuploads%2FomDGyiCUPiZfg0uTUiqK%2FUntitled%20Feb%204%20217%20PM%20%E2%80%93%20Ideogram%20-%20Light%20Dark%402x.png?alt=media&#x26;token=3b6be647-9fd6-4476-9cc7-9f08c22074ed" alt=""><figcaption><p>Starting image.</p></figcaption></figure> <figure><img src="https://1799634369-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzjhNby3LLsIikYuvxAJP%2Fuploads%2F7Ud5bYjm8Dz0b77iNb06%2FUntitled%20Feb%204%20217%20PM%20%E2%80%93%20Ideogram%20-%20Light%20Dark%402x.png?alt=media&#x26;token=0c9255d0-0eee-4ed3-a6b7-3ad179cf3458" alt=""><figcaption><p>Masked areas.</p></figcaption></figure> <figure><img src="https://1799634369-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzjhNby3LLsIikYuvxAJP%2Fuploads%2FEZhSotB9Sn9eegYLOKYJ%2FUntitled%20Feb%204%20217%20PM%20%E2%80%93%20Ideogram%20-%20Light%20Dark%402x.png?alt=media&#x26;token=c71a778c-e804-4281-aa2f-a8cf7f94cabc" alt=""><figcaption><p>Resulting Magic Fill image.</p></figcaption></figure></div>

Original prompt: `Photo of a rabbit in a beautiful garden.`&#x20;

Magic Fill prompt: `Photo of a rabbit in a beautiful garden. There is a basket with carrots in the background and a big carrot in front of the rabbit.`

***

### Making Variations on an Element

Magic Fill can also be used to create variations of specific details while keeping other elements unchanged

For example, a woman’s hair color can be altered without modifying her face or the rest of the image.

The prompt used to generate the original image was modified each time in Magic Fill to request a different hair color.

Original prompt: `A close-up three-quarter shot of a young woman with a sharp,`` `**`platinum blonde`**` ``pixie cut. She has icy blue eyes and a hit of a playful smirk. She has metallic earrings on her ears. The background is blurred and hints at a sleek, futuristic setting. She gazes directly at the camera with confidence.`

<div><figure><img src="https://1799634369-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzjhNby3LLsIikYuvxAJP%2Fuploads%2FALCkS3B64RQizxIkQ9Gz%2FPixie%20Cut%20-%2001%20Platinum.png?alt=media&#x26;token=7905e903-3c69-4b83-9996-c7467d18707e" alt=""><figcaption><p>Starting image.</p></figcaption></figure> <figure><img src="https://1799634369-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzjhNby3LLsIikYuvxAJP%2Fuploads%2FFsFlwSHtfre4bgrtkovr%2FA%20close-up%20three-quarter%20shot%20of%20a%20young%20woman%20wi%E2%80%A6%20%E2%80%93%20Ideogram%20-%20Light%20Dark%402x.png?alt=media&#x26;token=87a12183-3897-45e3-a807-b7add91e23e0" alt=""><figcaption><p>The masked area drawn over her hair.</p></figcaption></figure> <figure><img src="https://1799634369-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzjhNby3LLsIikYuvxAJP%2Fuploads%2FHQzPeDtdgmbRLpn1osJI%2FPixie%20Cut%20Color.webp?alt=media&#x26;token=49e2d285-f528-4045-badf-4a0b3aec51fb" alt=""><figcaption><p>Results using different colors in the prompt.</p></figcaption></figure></div>

***

### Fixing Parts of an Image

Magic Fill is great for refining AI-generated images where small details like faces and hands may appear distorted due to the limited number of pixels.

Here’s how to easily fix those issues using Magic Fill.

Below is an image generated with Ideogram v2.0 using a 1:1 aspect ratio (1024 × 1024 pixels). The original prompt was: `A dynamic photo of a family standing on the lawn in front of a well-maintained house. The sky is clear with scattered clouds. Overlaying the top of the image, there's a text that reads 'Welcome' in a curvy font. The family consists of four members in that order: a young boy, a father, a mother and a teenager girl. The house in the background has a classic design with a gabled roof.`

<figure><img src="https://1799634369-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzjhNby3LLsIikYuvxAJP%2Fuploads%2FV1piELRiQjaKr5g6d6eV%2FMagic%20Fill%20-%20Family%201.png?alt=media&#x26;token=e01b6855-7e47-4d5d-a4c1-723e5a8a6fe3" alt=""><figcaption><p>Original image generated with a 1:1 aspect ratio (1024 × 1024 pixels).</p></figcaption></figure>

Notice how the faces and hands appear very small in relation to the whole image. Because of this, the AI had difficulty rendering them correctly.

<div><figure><img src="https://1799634369-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzjhNby3LLsIikYuvxAJP%2Fuploads%2FwsPJM8q7xzzVa3ZplbU4%2FMagic%20Fill%20-%20Family%201.png%20%40%20400%20(RGB8%23)%20-%20Light%20Dark%402x.png?alt=media&#x26;token=b269bedf-dade-4f19-95e9-97ad85610b31" alt=""><figcaption><p>400% zoomed-in detailed view.</p></figcaption></figure> <figure><img src="https://1799634369-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzjhNby3LLsIikYuvxAJP%2Fuploads%2FuHLpoGPd0XO92owvIRjS%2FMagic%20Fill%20-%20Family%201.png%20%40%20400%20(RGB8%23)%20-%20Light%20Dark%402x.png?alt=media&#x26;token=21e2e1d2-25dc-4106-bc7b-98087852a992" alt=""><figcaption><p>400% zoomed-in detailed view.</p></figcaption></figure> <figure><img src="https://1799634369-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzjhNby3LLsIikYuvxAJP%2Fuploads%2FIYuOqWU5bEgdNVQ7vOPg%2FMagic%20Fill%20-%20Family%201.png%20%40%20400%20(RGB8%23)%20-%20Light%20Dark%402x.png?alt=media&#x26;token=86a238b2-e2bc-4120-a87d-d00d2d22c6d0" alt=""><figcaption><p>400% zoomed-in detailed view.</p></figcaption></figure></div>

To fix this:

* Mask the areas that need correction.
* Adjust the generation window to be as small as possible, covering all masked areas while keeping some unmasked visual references to help the AI understand the context.

{% hint style="info" %}
Because the aspect ratio dictates the dimensions (in pixels) of the generated image, it can be leveraged to improve pixel density in specific areas. This technique is particularly useful for fixing small details that were not properly rendered in the original image.
{% endhint %}

In the example below, the generation window boundaries has a custom aspect ratio of 17:14, thus a dimension of 1088 × 986 pixels. The AI will have more pixels to work with for generating the faces and hands in masked areas.

The prompt was also simplified to reflect only the content within the generation window: `A dynamic photo of a family standing on the lawn in front of a well-maintained house. The family consists of four members in that order: a young boy, a father, a mother and a teenager girl.`

<figure><img src="https://1799634369-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzjhNby3LLsIikYuvxAJP%2Fuploads%2FJu1l4QuakdQ0MAxAY2DP%2FA%20dynamic%20photo%20of%20a%20family%20standing%20on%20the%20lawn%E2%80%A6%20%E2%80%93%20Ideogram%20-%20Light%20Dark%402x.png?alt=media&#x26;token=be18e770-0fb8-4344-bfde-28a700d9c3ad" alt=""><figcaption><p>Masked areas to be generated. The generation window is kept as small as possible to achieve greater pixel density.</p></figcaption></figure>

The AI generated the updated image directly over the original, modifying only the masked parts while leaving the rest intact.

<figure><img src="https://1799634369-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzjhNby3LLsIikYuvxAJP%2Fuploads%2Fegz5Rv7MeweRYK1gU8Zi%2FA%20dynamic%20photo%20of%20a%20family%20standing%20on%20the%20lawn%E2%80%A6%20%E2%80%93%20Ideogram%20-%20Light%20Dark%402x.png?alt=media&#x26;token=8e119995-1b91-40e0-b683-a606202aff95" alt=""><figcaption></figcaption></figure>

While the faces now look significantly better, there is still room for improvement—particularly for the father holding his son’s hand. To refine this further:

* Mask that specific part of the image again.
* Resize the generation window to be even smaller.
* Ensure the young boy is included in the generation window to provide the AI with proper proportions and context.

This time, the generation window was set to a 1:1 aspect ratio, meaning the newly generated section had a resolution of 1024 × 1024 pixels.

<div><figure><img src="https://1799634369-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzjhNby3LLsIikYuvxAJP%2Fuploads%2FrsbfYoIgmM7HyJ63H9xZ%2FMagic%20Fill%20-%20Family%20intermediaire.png%20%40%20400%20(Layer%201%20RGB8%23)%20-%20Light%20Dark%402x.png?alt=media&#x26;token=d0d76e18-3759-4c36-98c7-1eb14f0183d8" alt=""><figcaption><p>The hands still require some adjustment.</p></figcaption></figure> <figure><img src="https://1799634369-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzjhNby3LLsIikYuvxAJP%2Fuploads%2FSVtFC9Uo760ZGoPWY39H%2FA%20dynamic%20photo%20of%20a%20family%20standing%20on%20the%20lawn%E2%80%A6%20%E2%80%93%20Ideogram%20-%20Light%20Dark%402x.png?alt=media&#x26;token=919dd91a-cb32-4a8a-b11e-180162bfbed4" alt=""><figcaption><p>The masked area and the small generation window. </p></figcaption></figure></div>

The final image below was downloaded using the Download feature. While the downloaded image retained a 1024 × 1024 resolution, areas with a higher pixel density were downscaled but still preserved the improvements made.

For more details on resolution and pixel density in Canvas, refer to the last two sections of the [Canvas documentation](https://docs.ideogram.ai/canvas-and-editing/canvas-overview#canvas-and-image-sizes).

<figure><img src="https://1799634369-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzjhNby3LLsIikYuvxAJP%2Fuploads%2FUx7Y8vOosjDf8o5pMmkg%2FMagic%20Fill%20-%20Family%20final.png?alt=media&#x26;token=0c73453d-9484-4445-acea-7a70cca5e5ec" alt=""><figcaption><p>The final image.</p></figcaption></figure>

{% hint style="info" %}
**Getting even better results**

To further enhance image quality, consider using the Upscale feature before attempting any fixes. This will provide the AI with up to twice as many pixels to work with for the same selected area.

Keep in mind:

• The generation window has a fixed number of pixels based on its aspect ratio.

• If you upscale a 1:1 image (e.g., from 1024 × 1024 to 2048 × 2048), then use Magic Fill at a 1:1 aspect ratio (which generates a 1024 × 1024 image), it’s best to keep the generation window under half the size—both horizontally and vertically—of the upscaled image for optimal results.
{% endhint %}

***

## Advanced and Creative Examples

Magic Fill can be used creatively to achieve impressive results. The examples below demonstrate how pushing the limits of the tool can lead to surprising outcomes. For example, you can take an image of a product and seamlessly integrate it into another existing image.

{% hint style="warning" %}
The advanced techniques presented below sometimes push the tool to its limits. They are more about creative exploration and achieving good results can be challenging at times. Indeed, many factors influence the final rendering of the image like the prompt, the original image, the options used, etc.

Experimenting with prompts and different options is often essential, but even then, results may vary. If you encounter difficulties, you can ask for help in the [#prompt-w-friend](https://discord.com/channels/1106248220687994911/1145120589955223602) channel on our Discord server. Simply share your prompt, the generated image, and a brief description of the issue. Other users may be able to help you achieve better results.
{% endhint %}

### Inserting an Item from One Image into Another

In the example below, there is a photo of a decorative pillow with a geometric pattern and an image of a loveseat with some pillows in a living room. The goal is to modify the loveseat pillows so they match the design of the patterned pillow.

<div><figure><img src="https://1799634369-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzjhNby3LLsIikYuvxAJP%2Fuploads%2FbpfHOqDVlTqOEiQpAal7%2FUntitled%20Feb%2012%201156%20AM%20%E2%80%93%20Ideogram%20-%20Light%20Dark%402x.png?alt=media&#x26;token=240c95bd-516f-48a7-85be-21e04bef6598" alt=""><figcaption></figcaption></figure> <figure><img src="https://1799634369-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzjhNby3LLsIikYuvxAJP%2Fuploads%2FhDr3L9wKV0gy3jlQeXci%2FUntitled%20Feb%2012%201156%20AM%20%E2%80%93%20Ideogram%20-%20Light%20Dark%402x.png?alt=media&#x26;token=c4fef874-521b-497c-8257-cd841153d234" alt=""><figcaption></figcaption></figure></div>

1. Obtain a good description of both images.
   1. These descriptions will later be merged and optimized into a single prompt.
   2. If the image was generated directly in Ideogram, you can reuse the original prompt.
   3. If not, it is strongly recommended to use the Describe feature to generate an accurate description.
2. Place the two images side by side and resize one if necessary.
3. Click Magic Fill and mask the pillows in the loveseat image.
4. Click Next and adjust the generation window to cover:
   1. The entire pillow with the geometric pattern image.
   2. The masked area and a sufficient portion of the loveseat image to provide proper context.

<figure><img src="https://1799634369-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzjhNby3LLsIikYuvxAJP%2Fuploads%2FPIYmo0ymgyQrzHe7VzcF%2FUntitled%20Feb%2012%201156%20AM%20%E2%80%93%20Ideogram%20-%20Light%20Dark%402x.png?alt=media&#x26;token=e4e9f10d-b521-4434-ba18-73c8e0e6a8d7" alt=""><figcaption><p>The masked pillow on the right and the generation window.</p></figcaption></figure>

5. Merge and optimize the descriptions of both images:
   1. Description of the patterned pillow: `A decorative pillow with a geometric pattern. The primary color of the pillow is a soft and dark olive green, and the pattern consists of intertwined white lines forming intricate designs. The design appears symmetrical, with two mirrored patterns on either side of the pillow. The pillow is on a white background.`
   2. Prompt used to generate the loveseat image: `A close-up view of a cozy loveseat, without any pillow, in a modern living room. There are a few soft and dark olive green accents.`
   3. Merged and optimized prompt: **`On the left`**`, a decorative pillow with a geometric pattern. The primary color of the pillow is a soft and dark olive green, and the pattern consists of intertwined white lines forming intricate designs. The design appears symmetrical, with two mirrored patterns on either side of the pillow.`` `**`On the right`**`, a close-up view of a cozy loveseat with two pillows like the one on the left.`

{% hint style="info" %}
**Why optimize the prompt?**

* The revised prompt removes unnecessary details and focuses on the most relevant elements for the AI.
* The pillow description is detailed since it is the main element being generated.
* The background context remains slightly less detailed, as long as it provides enough visual reference.
  {% endhint %}

6. Adjust other options such as Style and Magic Prompt (it is recommended not to use Magic Prompt, as it might alter your optimized prompt)
7. Click Magic Fill and wait for the generation to complete.
8. Once the image is generated, click on it to cycle through the four generated variations using the arrows at the bottom.

<figure><img src="https://1799634369-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzjhNby3LLsIikYuvxAJP%2Fuploads%2FB91HLw2soNGDoOK41JJy%2FUntitled%20Feb%2012%201156%20AM%20%E2%80%93%20Ideogram%20-%20Light%20Dark%402x.png?alt=media&#x26;token=e313cbf2-8d12-4369-b608-8d19cd20e5fb" alt=""><figcaption><p>The generated image includes the pillow and the area selected by the generation window.</p></figcaption></figure>

9. Download the final image:
   1. Click the Download tool on the left-side panel.
   2. Select the desired area to be included in the final image.
   3. Click Download.

<figure><img src="https://1799634369-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzjhNby3LLsIikYuvxAJP%2Fuploads%2FaLCuPHxJLTRK2bXMVLRt%2FUntitled%20Feb%2012%201156%20AM%20%E2%80%93%20Ideogram%20-%20Light%20Dark%402x.png?alt=media&#x26;token=84e0c975-f2cf-4a33-99da-401a6463baba" alt=""><figcaption><p>The bounding box indicates the area that will be downloaded.</p></figcaption></figure>

Below is a comparison of the image before and after the transformation.

<div><figure><img src="https://1799634369-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzjhNby3LLsIikYuvxAJP%2Fuploads%2FhDr3L9wKV0gy3jlQeXci%2FUntitled%20Feb%2012%201156%20AM%20%E2%80%93%20Ideogram%20-%20Light%20Dark%402x.png?alt=media&#x26;token=c4fef874-521b-497c-8257-cd841153d234" alt=""><figcaption><p>Before</p></figcaption></figure> <figure><img src="https://1799634369-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzjhNby3LLsIikYuvxAJP%2Fuploads%2FRTx58tM5pm4tLTEXNo2b%2FPillow%20%26%20Loveseat.png?alt=media&#x26;token=7ea96b3f-e7dc-4869-9193-ac398f86bbc2" alt=""><figcaption><p>After</p></figcaption></figure></div>

***

### Integrate Text and Logos in Images

It’s easy to overlay text on an image using the Text tool in Canvas, but seamlessly integrating text into the natural elements of an image can be more challenging.

In the example below, the goal is to make it look as if a message is handwritten in the sand on a beach.

Once a beach image is selected, the Text tool is used to choose a suitable font and position the text where it should appear in the final image.

<div><figure><img src="https://1799634369-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzjhNby3LLsIikYuvxAJP%2Fuploads%2FxkOxl9ChMs6CV76rGypw%2FText%20on%20the%20beach%201.png?alt=media&#x26;token=20177f01-e03d-4374-8529-7b5b6e3f54bc" alt=""><figcaption><p>The original image.</p></figcaption></figure> <figure><img src="https://1799634369-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzjhNby3LLsIikYuvxAJP%2Fuploads%2FjN4VOcaPMob5GWGLrB3s%2FA%20close-up%20bird%20eye%20view%20of%20an%20undisturbed%20sandy%E2%80%A6%20%E2%80%93%20Ideogram%20-%20Light%20Dark%402x.png?alt=media&#x26;token=d603ab43-f27a-460f-829e-29aab2ab124b" alt=""><figcaption><p>Positioning the text on the image.</p></figcaption></figure></div>

At this point, the text itself cannot be used directly to create the writing effect in the sand. Instead, follow these steps before proceeding to Magic Fill:

1. Move the text aside and make it completely black.
2. Use Remix on the text, setting the image weight to 100.\
   \&#xNAN;*This is necessary because a text box cannot be used directly in this technique—it must first be converted into an image.*
3. Place the newly created image near the beach image.

Now, apply the same technique used in the first example:

* Mask the area where the text should appear in the beach image.
* Adjust the Magic Fill generation window to include both the masked area and the black text image, ensuring the AI understands the reference.

Here's the prompt that was used:

**`On the left`**`, a text saying "Time for a little vacation?".`` `**`On the right`**`, the same text in the same style, roughly written by hand in the sand of an undisturbed sandy beach with seashells and other objects.`

<figure><img src="https://1799634369-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzjhNby3LLsIikYuvxAJP%2Fuploads%2FHIiecse63rpLJXnbANKf%2FA%20close-up%20bird%20eye%20view%20of%20an%20undisturbed%20sandy%E2%80%A6%20%E2%80%93%20Ideogram%20-%20Light%20Dark%402x.png?alt=media&#x26;token=da608baf-750f-4add-a812-26733121c1f8" alt=""><figcaption><p>The rendered text on the left and the masked area on the right, both encompassed within the generation window.</p></figcaption></figure>

<figure><img src="https://1799634369-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzjhNby3LLsIikYuvxAJP%2Fuploads%2FhXXvWGtBGgHLkE4iupjU%2FText%20on%20the%20beach%20final%201.png?alt=media&#x26;token=94c2be4e-c42a-48cf-b3d4-e4dee6ded9db" alt=""><figcaption><p>Final image with the text written in the sand.</p></figcaption></figure>

{% hint style="warning" %}
**Important notes**

The final image may appear more blurry or pixelated compared to the original. This happens because the Magic Fill-generated section is often about twice the size of the original image.

**Why does this happen?**

The total number of pixels remains constant for any aspect ratio, regardless of the generation window size on the canvas. This is a current limitation of this technique.

However, to achieve the best possible results, consider the following:

* Minimize the generation window
  * Keep it as small as possible while maintaining enough visual context for the AI.
* Reduce the size of the reference text or object
  * The AI can work with a smaller image as long as the prompt description is detailed enough.
  * Reducing the reference image by half often works just as well while helping shrink the generation window.
* Use the Upscale feature on the final image
  * Upscale makes the image larger and sharper.
  * Don’t forget to provide a detailed prompt when using Upscale for the best results.
    {% endhint %}

Here’s another example where text was integrated as embroidery on a baseball cap using the same technique.

<figure><img src="https://1799634369-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzjhNby3LLsIikYuvxAJP%2Fuploads%2FiZcIYxwqGcnDcIToaHdj%2FBaseball%20word.png?alt=media&#x26;token=455433b1-8ce5-4c5d-8ea9-9b1ac965b8b6" alt="" width="375"><figcaption><p>The word ‘Baseball’ in Lobster font and rendered using Remix.</p></figcaption></figure>

<div><figure><img src="https://1799634369-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzjhNby3LLsIikYuvxAJP%2Fuploads%2FdH98BH4oR8BTwvrfXLci%2FBaseball%201.png?alt=media&#x26;token=642ace3e-9edf-433f-9bcf-5d20e59c2b63" alt=""><figcaption><p>Original baseball cap image.</p></figcaption></figure> <figure><img src="https://1799634369-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzjhNby3LLsIikYuvxAJP%2Fuploads%2FmBJ7kgw71uRa9tytXdNm%2FBaseball%202.png?alt=media&#x26;token=623a28f6-ff78-4ad2-b0c8-465b8aaaf440" alt=""><figcaption><p>Result after Magic Fill.</p></figcaption></figure></div>

Here's the prompt that was used: **`On the right`**`, the word "Baseball" written in a bold script font.`` `**`On the left`**`, the same word and font style than the one on the right but embroidered in red on the front of a baseball cap.`

Finally, using the same technique, it’s easy to integrate a logo onto an object.

<figure><img src="https://1799634369-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzjhNby3LLsIikYuvxAJP%2Fuploads%2FL3r3E1PIO7xx2KgoQSl2%2FIron%20Helm%20logo.png?alt=media&#x26;token=6bba763b-5737-441f-b086-1f6f98172a12" alt="" width="375"><figcaption><p>The original logo.</p></figcaption></figure>

<div><figure><img src="https://1799634369-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzjhNby3LLsIikYuvxAJP%2Fuploads%2FjEuaVyA3XI1PuLC5kSI0%2FIron%20Helm%201.png?alt=media&#x26;token=c7e18dbe-443d-48dd-b1a0-05357e0370ae" alt=""><figcaption><p>The logo must be integrated into the glass.</p></figcaption></figure> <figure><img src="https://1799634369-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzjhNby3LLsIikYuvxAJP%2Fuploads%2F5RoiJ0tHgghVLC4lUIhF%2FIron%20Helm%202.png?alt=media&#x26;token=72328753-8129-40cd-8a12-8a0027df3a2f" alt=""><figcaption><p>The final result. Notice the reflections on the logo.</p></figcaption></figure></div>

Here's the prompt used for the example above: **`On the left`**`, logo for a brand of beer named "Iron Helm". At the center of the logo is a detailed illustration of a knight's helmet, which appears to be made of metal with rivets and a nose guard. The helmet is depicted in a frontal view. The logo is enclosed within a shield-like emblem, which is predominantly dark red and white.`` `**`On the right`**`, the exact same logo on a glass of beer.`

***

### Product Placement

In this example, a perfume bottle from a photo will be integrated into two different scenes:

1. A studio photography setup.
2. An image where a woman holds the bottle.

The original image of the perfume bottle was generated in Ideogram, but any image could be used. There is no need to remove the background, as long as the image isn’t cluttered with other objects.

<figure><img src="https://1799634369-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzjhNby3LLsIikYuvxAJP%2Fuploads%2FJZd75BZAH2mCt0Styr3F%2FProduct%201%20-%20Bottle.png?alt=media&#x26;token=9e52dde7-4e85-4b28-ba61-95461b313421" alt="" width="375"><figcaption><p>Original image to be integrated, generated with Ideogram.</p></figcaption></figure>

#### Integrating the perfume bottle into a studio setup

Using the same technique as described in the previous examples:

* An area was masked where the bottle should be integrated.
* A part of a plate was also masked, allowing the AI to transform it into a more suitable pedestal, which it successfully did.

The perfume bottle image was placed on the left side of the studio setup image, and the generation window was made as small as possible while keeping some context.

Prompt used: **`To the left`**`, a perfume bottle for women named 'Azure' stands out prominently. The bottle has a gem-like, faceted design, predominantly blue with a silver cap and a black neck. The word 'AZURE' is prominently displayed on both the bottle and the neck.`` `**`On the right`**`, a close-up view of the same bottle is captured, placed atop a short white pedestal in a studio photography setup.`

<figure><img src="https://1799634369-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzjhNby3LLsIikYuvxAJP%2Fuploads%2FzZWxEvsBmx6ym6oErW3K%2FProduct%20placement%20%20-%20Studio%20mask.jpeg?alt=media&#x26;token=0b3ee674-bc4f-4001-9542-ad7b16d5ed4f" alt=""><figcaption><p>Masked areas and generation window size</p></figcaption></figure>

<div><figure><img src="https://1799634369-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzjhNby3LLsIikYuvxAJP%2Fuploads%2FKvZSLIcEjl6EfhUN8RC9%2FProduct%20placement%20-%20Studio%20original.png?alt=media&#x26;token=380275d6-2e36-4222-bc26-48dfd9ea290e" alt=""><figcaption><p>Original image where the perfume bottle will be integrated</p></figcaption></figure> <figure><img src="https://1799634369-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzjhNby3LLsIikYuvxAJP%2Fuploads%2FvjjWkMygqSviZOACnaPY%2FProduct%20placement%20-%20Studio%20final.png?alt=media&#x26;token=71248e54-b9c9-44d6-9e27-5d2216c4cc72" alt=""><figcaption><p>Final image. Note the subtle shadow and reflection.</p></figcaption></figure></div>

#### Integrating the perfume bottle into a lifestyle scene

For the next integration, an image of a woman holding a perfume bottle was generated in Ideogram. The goal was to create a suitable scene for integration.

As before:

* The perfume bottle image was placed to the left of the woman’s image.
* The affected areas (her hands and the existing bottle) were masked.
* The generation window was made as small as possible while keeping enough context for the AI, including part of the face and the base of the hands.

Prompt used: **`On the left`**`, a woman’s perfume bottle named 'Azure' features a unique, faceted design. The bottle is predominantly blue, with a silver cap and a black neck. The word 'AZURE' is prominently displayed on both the bottle and the neck.`` `**`On the right`**`, a chic woman holds the very same bottle of perfume.`

<figure><img src="https://1799634369-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzjhNby3LLsIikYuvxAJP%2Fuploads%2FIidht8HzxwepdRsDWlWH%2FProduct%20placement%20-%20Woman%20mask.jpeg?alt=media&#x26;token=aa0ca827-f1ad-4482-9813-ec47e17b4a06" alt=""><figcaption><p>Masked areas and generation window size.</p></figcaption></figure>

<div><figure><img src="https://1799634369-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzjhNby3LLsIikYuvxAJP%2Fuploads%2FQfXoTiKfscXbUL3K1jsF%2FProduct%20placement%20-%20Woman%20original.png?alt=media&#x26;token=2829da94-f7cf-45e0-aaec-e4d56170a22b" alt=""><figcaption><p>Original image where the perfume bottle will be integrated</p></figcaption></figure> <figure><img src="https://1799634369-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzjhNby3LLsIikYuvxAJP%2Fuploads%2FlQHMoVWi3jHmsDye8OED%2FProduct%20placement%20-%20Woman%20final.png?alt=media&#x26;token=c84f7834-0077-45b9-ae55-9649cc6451c1" alt=""><figcaption><p>Final image with the integrated bottle. Note how the AI adjusted the bottle to match the lighting conditions.</p></figcaption></figure></div>

***

## Tips and Tricks for Best Results

Achieving great results with **Magic Fill** and **Extend**, especially with advanced techniques, takes a mix of creativity, experimentation, and a bit of patience. Here are some key factors that can impact the final outcome:

* **Craft precise and detailed prompts** – Clarity in wording helps the AI understand what to generate.
* **Experiment with synonyms and rephrase** - Changing a few words or testing different ways of expressing the same idea in a prompt can make big difference.
* **Start with a high-quality image** – The better the input, the better the output.
* **Consider the complexity of the image** – Simpler modifications often yield more accurate results.
* **Optimize the generation window size** – Keeping it as small as possible while including enough context leads to sharper and more realistic outcomes.
* **Manage your expectations** – AI-generated results can vary, so refining your approach and testing different options is key to success.

By experimenting with different approaches, adjusting prompts, and fine-tuning generation settings, you can push the boundaries of what's possible and create stunning images.
