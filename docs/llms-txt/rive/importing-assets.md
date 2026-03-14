# Source: https://uat.rive.app/docs/editor/fundamentals/importing-assets.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://uat.rive.app/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Importing Assets

> Import your assets by dragging and dropping them onto the Rive Editor. You can import SVG, JSON, PNG, PSD, and JPG formats.

export const YouTube = ({id, timestamp}) => {
  const videoSrc = timestamp ? `https://www.youtube.com/embed/${id}?start=${timestamp}` : `https://www.youtube.com/embed/${id}`;
  return <iframe width="100%" height="400" src={videoSrc} title="YouTube video player" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerPolicy="strict-origin-when-cross-origin" allowFullScreen />;
};

## Assets Panel

<YouTube id="B9uD-Gh8zjg" />

<YouTube id="vH9UHmdVwx4" />

<YouTube id="hPbgPGJNE78" />

After dragging in your graphics, they now appear in the Assets Panel, located in the left side of the editor UI. Drag and drop them onto an artboard to begin using them.

## Importing Custom Font

For Pro customers, you can add custom fonts to be used with our Text tool. Drag and drop your `.OTF` or `.TTF` file into the editor, or use the plus button next to the Font section.

## Updating image assets

You can make updates to your images after they've been imported.

Do this by selecting the image in the Assets Panel; the asset's properties appear in the Inspector, and a "Replace" button will be available for raster assets (PNG, JPG, PSD).

Hit the replace button, and when prompted, select the updated image. You'll notice that this updates all instances of the graphic used in the file.

## Supported formats

Rive supports importing SVG (see limitations below), JSON, PNG, PSD, and JPG formats.

#### Copy and paste directly from Figma

You can use "copy as SVG" and paste it directly into the Rive editor.

![Image](https://ucarecdn.com/ec7e980c-ea0a-4147-96df-f29b7dc2be2c/)

#### Import Lottie file

<Note>
  Importing Lottie files is available on the Enterprise plan. [Learn more about our plans and pricing](https://rive.app/pricing).

  This workflow can introduce risks that vary across customer setups, and implementing them without our guidance can lead to issues in performance, security, or reliability. Helping customers assess and mitigate these risks takes significant time and effort, which is why this level of support is only available on Enterprise.
</Note>

You can import your Lottie animations into Rive. To get started, drag and drop your Lottie JSON file into the Rive editor. This adds it to your Assets panel.

<img src="https://mintcdn.com/rive/KnNrDuhU1mIj7cOb/images/editor/fundamentals/12a13a71-d5d0-4ed2-a1b1-2fe49bbbb9df.webp?fit=max&auto=format&n=KnNrDuhU1mIj7cOb&q=85&s=c598755433b70742d01e408fa7b3f620" alt="Image" width="2716" height="1694" data-path="images/editor/fundamentals/12a13a71-d5d0-4ed2-a1b1-2fe49bbbb9df.webp" />

From there, you can drag it into an existing Artboard or drag it into an empty space to create a new Artboard.

<img src="https://mintcdn.com/rive/KnNrDuhU1mIj7cOb/images/editor/fundamentals/49c02a1d-18d9-4937-8ea1-bad52ba9ce4e.webp?fit=max&auto=format&n=KnNrDuhU1mIj7cOb&q=85&s=8d42bbe2dad0c6466bd70bc7b25ca268" alt="Image" width="2566" height="1622" data-path="images/editor/fundamentals/49c02a1d-18d9-4937-8ea1-bad52ba9ce4e.webp" />

<Note>If you run into issues at runtime, you may need to convert any `Plus`, `Add`, or `Hard Mix` layer blend modes to a a blend mode supported by the Rive runtimes.</Note>

## SVG Tips

SVG is a very flexible and feature-rich format. We aim to support SVG as best we can; however, there are some features that we do not support at this stage.

Exporting files as SVG with inline style instead of CSS will work best for our importer.

When exporting from other design tools, look for the option to retain the IDs and names of your shapes when you export. This will ensure that your imported file retains the same structure and layer names. Most tools have this option, as in the Figma example below.

<img src="https://mintcdn.com/rive/KnNrDuhU1mIj7cOb/images/editor/fundamentals/9a2b2c37-c330-4323-a4c6-9928fbac8d94.webp?fit=max&auto=format&n=KnNrDuhU1mIj7cOb&q=85&s=b1ded07a05c5c0af63ba514946dfce41" alt="Image" width="1127" height="472" data-path="images/editor/fundamentals/9a2b2c37-c330-4323-a4c6-9928fbac8d94.webp" />

### Photoshop

<YouTube id="Mlo9mQBUaTE" />

When exporting from Photoshop, make sure you're only using vector layers. Don't convert or flatten anything to raster.

### Illustrator

When using "Save As" to export an SVG from Illustrator, set the CSS Properties in the SVG Options to "Presentation Attributes" instead of the default setting. Similarly, when using "Export As" to export an SVG from Illustrator, set Styling to "Presentation Attributes" in the SVG Options. Note that Illustrator uses the "Export As" SVG Options when copying directly from Illustrator, so if you are copy-pasting from Illustrator to the Rive editor, be sure to set Styling to "Presentation Attributes" in the SVG Options.

Additionally, disable the "Preserve Illustrator Editing Capabilities" option, as this will make your file much larger and add data that our importer does not recognize.

### Known Issues

* Embedded images are ignored. We plan to implement this.
* Gradient transforms are ignored.
  * We currently cannot provide equal support for this across our runtimes, so this is not supported.
  * However, we support linear and radial gradients, which can cover some use cases.
* Rive does not have a concept of point (pt) or millimeter (mm) sizing. An SVG that uses dimensions provided in pt or mm will have its values converted to pixels (px). Points are converted to 1.33 px, and millimeters are converted to 3.78 px.
* SVG provides `inherit` to let strokes and fills use the color of their ancestors. Rive does not support this, and any inherited color defaults to white.
* Other unsupported SVG features:
  * `stroke-dasharray` - you may see a solid stroke line instead
  * `mask` - we treat this like clipping
  * `filter`
  * `skew`
