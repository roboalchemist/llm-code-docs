# Source: https://www.theatrejs.com/docs/latest/manual/assets

Title: Assets – Theatre.js

URL Source: https://www.theatrejs.com/docs/latest/manual/assets

Markdown Content:
Since 0.6.0

Theatre.js assets let you use images and other files as the value of props. It also allows you to use these assets for keyframe values.

**Need more asset types?**
*   Feel free to suggest more asset types on our [Discord server](https://discord.gg/bm9f8F9Y9N).
*   Or submit a PR of your own. Here is how:
    1.   Fork the [repo](https://github.com/theatre-js/theatre/) and [set up your dev environment](https://github.com/theatre-js/theatre/blob/main/CONTRIBUTING.md).
    2.   Define a new prop type by copying and editing [`types.image()`](https://github.com/theatre-js/theatre/blob/8d8e2348dd3528fe508456738dddd1644f79004f/theatre/core/src/propTypes/index.ts#L159)
    3.   Define a new prop editor similar to how [`ImagePropEditor`](https://github.com/theatre-js/theatre/blob/8d8e2348dd3528fe508456738dddd1644f79004f/theatre/studio/src/propEditors/simpleEditors/ImagePropEditor.tsx#L1) is defined.
    4.   Add the new prop editor to the list of known editors [here](https://github.com/theatre-js/theatre/blob/8d8e2348dd3528fe508456738dddd1644f79004f/theatre/studio/src/propEditors/simpleEditors/simplePropEditorByPropType.ts#L18).

To get started with assets, decide on a location you are going to host them at (like `/theatrejs-assets`, or a CDN of your choice), then let Theatre.js know about it when creating a project.

`const project = getProject('My project', {  assets: {    baseUrl: '/theatrejs-assets',  },})`

Theatre.js will then look for assets at this location. If you don't specify it, it'll default to the value `'/'`.

To use an asset prop, define it in a `sheet.object()` call.

`const object = sheet.object('My Object', {  texture: types.image('', {    label: 'Texture',  }),})`

Studio lets you assign files to asset props, which it will initially store in IndexedDB.

![Image 1: Image props in the Details panel](https://www.theatrejs.com/images/docs/0.5/manual/assets/image-prop-ui.png)

If any assets are used in your project, upon exporting the project, you also get a zip file with all the assets, which you need to extract to the location specified in `projectConfig.assets.baseUrl`. As soon as an asset is found at this location, it is deleted from IndexedDB to free up space.

The values of asset props are asset handles, which you can use to retrieve the URL for that asset using [`Project.getAssetUrl()`](https://www.theatrejs.com/docs/latest/api/core#project.getasseturl_assethandle_).

`const object = sheet.object('My Object', {  texture: types.image(undefined, {    label: 'Texture',  }),})object.onValuesChange(({ texture }) => {  setImageUrl(project.getAssetUrl(texture))})`

#Learn more
-----------

To learn more about assets, check out the documentation for

*   [`types.image`](https://www.theatrejs.com/docs/latest/api/core#types.image_default-opts_)_image assets_
*   [`types.file`](https://www.theatrejs.com/docs/latest/api/core#types.file_default-opts_)_generic file assets_
*   [`Project.getAssetUrl()`](https://www.theatrejs.com/docs/latest/api/core#project.getasseturl_assethandle_)

* * *

Was this article helpful to you?

Last edited on February 01, 2024.

[Edit this page](https://github.com/theatre-js/website/blob/main/content/docs/0.5/300-manual/137-assets.mdx)
