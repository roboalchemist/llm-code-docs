# Source: https://firebase.google.com/docs/ai-logic/edit-images-imagen-overview.md.txt

<br />

<br />

| **Preview** : Using theFirebase AI LogicSDKs to accessImagenmodels is a feature that's in Preview, which means that it isn't subject to any SLA or deprecation policy and could change in backwards-incompatible ways.
|
| Editing withImagenis only supported if you're using theVertex AIGemini API. It's also currently only supported for Android and Flutter apps. Support for other platforms is coming later in the year.

<br />

<br />

<br />

|-------------------------------------------------------------------------|
| *Only available when using theVertex AIGemini APIas your API provider.* |

<br />

<br />

TheFirebase AI LogicSDKs give you access to theImagenmodels (via the[ImagenAPI](https://cloud.google.com/vertex-ai/generative-ai/docs/model-reference/imagen-api)) so that you can edit images using either:

- [**Mask-based editing**](https://firebase.google.com/docs/ai-logic/edit-images-imagen-overview#mask-based-editing), like inserting and removing objects, expanding image content beyond original borders, and replacing backgrounds

- [**Customization**](https://firebase.google.com/docs/ai-logic/edit-images-imagen-overview#customization)options based on***style*** (like pattern, texture, or artist style),***subject*** (like product, person, or animal), or***control***(like a hand-drawn sketch).

This page describes each editing option at a high level. Each option has its own separate page with more details and code samples.

<br />

#### Models that support this capability

Imagenoffers image editing through its`capability`model:

- `imagen-3.0-capability-001`

Note that forImagenmodels, the`global`location is***not***supported.

<br />

## Mask-based editing

**Mask-based editing** lets you make localized, precise changes to an image. The model makes changes exclusively within a defined*masked area* of the image. A*mask*is a digital overlay defining the specific area you want to edit. The masked area can either be auto-detected and created by the model or be defined in a masked image that you provide. Depending on the use case, the model may require a text prompt to know what changes to make.

Here are the common use cases for mask-based editing:

- [Insert new objects into an image](https://firebase.google.com/docs/ai-logic/edit-images-imagen-overview#insert-objects)
- [Remove unwanted objects from an image](https://firebase.google.com/docs/ai-logic/edit-images-imagen-overview#remove-objects)
- [Expand an image's content beyond its original borders](https://firebase.google.com/docs/ai-logic/edit-images-imagen-overview#expand-images)
- [Replace the background of an image](https://firebase.google.com/docs/ai-logic/edit-images-imagen-overview#replace-background)

### Insert objects (inpainting)

You can use inpainting to[insert objects](https://firebase.google.com/docs/ai-logic/edit-images-imagen-insert-objects)into an image.

<br />

**How it works**: You provide an original image and a corresponding masked image --- either auto-generated or provided by you --- that defines a mask over an area where you want to add new content. You also provide a text prompt describing what you want to add. The model then generates and adds new content within the masked area.

For example, you can mask a table and prompt the model to add a vase of flowers.

<br />

### Remove objects (inpainting)

You can use inpainting to[remove objects](https://firebase.google.com/docs/ai-logic/edit-images-imagen-remove-objects)from an image.

<br />

**How it works**: You provide an original image and a corresponding masked image --- either auto-generated or provided by you --- that defines a mask over the object or subject that you want to remove. You can also optionally provide a text prompt describing what you want to remove, or the model can intelligently detect which object to remove. The model then removes the object and fills in the area with new, contextually appropriate content.

For example, you can mask a ball and replace it with a blank wall or a grassy field.

<br />

### Expand an image beyond its original borders (outpainting)

You can use*outpainting* to[expand an image beyond its original borders](https://firebase.google.com/docs/ai-logic/edit-images-imagen-expand-images).

<br />

**How it works**: You provide an original image and a corresponding masked image --- either auto-generated or provided by you --- that defines a mask of the new, expanded area. You can also optionally provide a text prompt describing what you want in the expanded area, or the model can intelligently decide what will logically continue the existing scene. The model generates the new content and fills in the masked area.

For example, you can change an image's aspect ratio or add more background context.

<br />

### Replace the background

You can[replace the background](https://firebase.google.com/docs/ai-logic/edit-images-imagen-replace-background)of an image.

<br />

**How it works**: You provide an original image and a corresponding masked image that defines a mask over the background --- either using automatic background detection or providing the mask of the background yourself. You also provide a text prompt describing what you want to change. The model then generates and applies a new background.

For example, you can change the setting around a subject or object without affecting the foreground (for example, in a product image).

<br />

## Customization

**Customization** lets you edit or generate images using text prompts and reference images that guide the model to generate a new image based on a specified[style](https://firebase.google.com/docs/ai-logic/edit-images-imagen-overview#style-customization),[subject](https://firebase.google.com/docs/ai-logic/edit-images-imagen-overview#subject-customization)(like a product, person, or animal), or a[control](https://firebase.google.com/docs/ai-logic/edit-images-imagen-overview#controlled-customization).

### Customize based on a style

You can[edit or generate images based on a specified*style*](https://firebase.google.com/docs/ai-logic/edit-images-imagen-style-customization).

<br />

**How it works** : You provide a text prompt and at least one reference image that shows a specific style (like a pattern, texture, or design style). The model uses these inputs to generate a new image based on the specified*style*in the reference images.

For example, you can generate a new image of a kitchen based on an image from a popular retail catalog that you provide.

<br />

### Customize based on a subject

You can[edit or generate images based on a specified*subject*](https://firebase.google.com/docs/ai-logic/edit-images-imagen-subject-customization).

<br />

**How it works** : You provide a text prompt and at least one reference image that shows a specific subject (like a product, person, or animal companion). The model uses these inputs to generate a new image based on the specified*subject*in the reference images.

For example, you can ask the model to apply a cartoon style to a photo of a child or change the color of a bicycle in a picture.

<br />

### Customize based on a control

You can[edit or generate images based on a specified*control*](https://firebase.google.com/docs/ai-logic/edit-images-imagen-controlled-customization).

<br />

**How it works** : You provide a text prompt and at least one*control*reference image (like a drawing or a Canny edge image). The model uses these inputs to generate a new image based on the control images.

For example, you can provide the model with a drawing of a rocket ship and the moon along with a text prompt to create a watercolor painting based on the drawing.

<br />

<br />

[Give feedback about your experience withFirebase AI Logic](https://firebase.google.com/docs/ai-logic/feedback)

<br />