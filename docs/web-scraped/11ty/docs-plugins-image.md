# Source: https://www.11ty.dev/docs/plugins/image/

Title: Image

URL Source: https://www.11ty.dev/docs/plugins/image/

Markdown Content:
Breadcrumbs:

*   [Ecosystem](https://www.11ty.dev/docs/plugins/image/)
*   [Plugins](https://www.11ty.dev/docs/plugins/)

On this page

*   [Installation](https://www.11ty.dev/docs/plugins/image/#installation)
*   [Usage](https://www.11ty.dev/docs/plugins/image/#usage)
    *   [HTML Transform](https://www.11ty.dev/docs/plugins/image/#html-transform)
    *   [More configuration options](https://www.11ty.dev/docs/plugins/image/#more-configuration-options)

*   [Build Performance](https://www.11ty.dev/docs/plugins/image/#build-performance)
    *   [Optimize Images on Request](https://www.11ty.dev/docs/plugins/image/#optimize-images-on-request)
    *   [In-Memory Cache](https://www.11ty.dev/docs/plugins/image/#in-memory-cache)
    *   [Disk Cache](https://www.11ty.dev/docs/plugins/image/#disk-cache)

*   [Options](https://www.11ty.dev/docs/plugins/image/#options)
    *   [Output File Extensions](https://www.11ty.dev/docs/plugins/image/#output-file-extensions)
    *   [Output Widths](https://www.11ty.dev/docs/plugins/image/#output-widths)
    *   [Output Formats](https://www.11ty.dev/docs/plugins/image/#output-formats)
    *   [Skip raster formats for SVG](https://www.11ty.dev/docs/plugins/image/#skip-raster-formats-for-svg)
    *   [Allow SVG to upscale](https://www.11ty.dev/docs/plugins/image/#allow-svg-to-upscale)
    *   [Transparent Images](https://www.11ty.dev/docs/plugins/image/#transparent-images)
    *   [Animated Images](https://www.11ty.dev/docs/plugins/image/#animated-images)
    *   [Transform on Request](https://www.11ty.dev/docs/plugins/image/#transform-on-request)
    *   [returnType and htmlOptions](https://www.11ty.dev/docs/plugins/image/#return-type-and-html-options)
    *   [Fix Orientation](https://www.11ty.dev/docs/plugins/image/#fix-orientation)
    *   [Custom Filenames](https://www.11ty.dev/docs/plugins/image/#custom-filenames)
    *   [Dry-Run](https://www.11ty.dev/docs/plugins/image/#dry-run)

*   [Advanced Options](https://www.11ty.dev/docs/plugins/image/#advanced-options)
    *   [Fail on Error](https://www.11ty.dev/docs/plugins/image/#fail-on-error)
    *   [Format Filtering](https://www.11ty.dev/docs/plugins/image/#format-filtering)
    *   [Output Directory](https://www.11ty.dev/docs/plugins/image/#output-directory)
    *   [URL Path](https://www.11ty.dev/docs/plugins/image/#url-path)
    *   [Use Cache](https://www.11ty.dev/docs/plugins/image/#use-cache)
    *   [Advanced control of Sharp image processor](https://www.11ty.dev/docs/plugins/image/#advanced-control-of-sharp-image-processor)
    *   [Change Global Plugin Concurrency](https://www.11ty.dev/docs/plugins/image/#change-global-plugin-concurrency)
    *   [Change the default Hash length](https://www.11ty.dev/docs/plugins/image/#change-the-default-hash-length)
    *   [Advanced Caching Options for Remote Images](https://www.11ty.dev/docs/plugins/image/#advanced-caching-options-for-remote-images)
    *   [Using a Hosted Image Service](https://www.11ty.dev/docs/plugins/image/#using-a-hosted-image-service)

*   [From the Community](https://www.11ty.dev/docs/plugins/image/#from-the-community)

Utility to perform build-time image transformations for both vector and raster images: output multiple image sizes, multiple formats, and cache remote images locally. Uses the [sharp](https://sharp.pixelplumbing.com/) image processor.

*   Easily add `width` and `height` attributes for [proper aspect ratio](https://developer.mozilla.org/en-US/docs/Web/Media/images/aspect_ratio_mapping) to reduce layout shift.
*   Accepts a wide variety of input image types: `jpeg`, `png`, `webp`, `gif`, `tiff`, `avif`, and `svg`. _Does not_ rely on file extensions (e.g. `.png` or `.jpg`), which may be missing or inaccurate.
*   Output multiple sizes, maintaining the original aspect ratio. Does not upscale raster images larger than original size. Intelligently generates `srcset` attributes.
*   Output multiple formats: `jpeg`, `png`, `webp`, `avif`[`+1` Build Cost](https://www.11ty.dev/docs/plugins/image/#build-cost), and `svg`. Intelligently generates the most efficient markup with zero server-dependencies, using `<img>` or `<picture>`.
*   Fast: de-duplicates with both an in-memory and disk cache. During local development, images are [processed on request for even faster build performance](https://www.11ty.dev/docs/plugins/image/#optimize-images-on-request).
*   Robust and works offline: save remote images to prevent broken image URLs later (via [`eleventy-fetch`](https://www.11ty.dev/docs/plugins/fetch/)).

Installation
------------

[Jump to section titled: Installation](https://www.11ty.dev/docs/plugins/image/#installation)
Published as [`@11ty/eleventy-img`](https://www.npmjs.com/package/@11ty/eleventy-img) on npm. [Source code on GitHub](https://github.com/11ty/eleventy-img).

_Image v6.0.0 requires Node 18+._

`npm install @11ty/eleventy-img`

Usage
-----

[Jump to section titled: Usage](https://www.11ty.dev/docs/plugins/image/#usage)
There are a few different ways to use Eleventy image:

Eleventy Image Usage Types

*   [Image HTML Transform](https://www.11ty.dev/docs/plugins/image/#html-transform): **Recommended**—start with this one! It’s the easiest to configure and is compatible with all template syntax.

*   [Image Data Files](https://www.11ty.dev/docs/plugins/image-datafiles/): Use images to populate data in the Data Cascade.
*   [Image JavaScript API](https://www.11ty.dev/docs/plugins/image-js/): Low-level JavaScript API works independent of Eleventy.
*   [Image Shortcodes](https://www.11ty.dev/docs/plugins/image-shortcodes/): Use universal shortcodes in Nunjucks, Liquid, or 11ty.js templates.
*   [Image WebC](https://www.11ty.dev/docs/plugins/image-webc/): ~~Use a WebC component for WebC templates.~~

### HTML Transform

[Jump to section titled: HTML Transform](https://www.11ty.dev/docs/plugins/image/#html-transform)
Added in v3.0.0 Added in Image v4.0.1 This is the easiest method to configure. Eleventy will transform _any_`<img>` or `<picture>` tags in HTML files as a post-processing step in your build.

eleventy.config.js

```
import { eleventyImageTransformPlugin } from "@11ty/eleventy-img";

export default function (eleventyConfig) {
	eleventyConfig.addPlugin(eleventyImageTransformPlugin);
};
```

That’s it! All `<img>` and `<picture>` elements will be processed for you by Eleventy Image.

#### Resolving image sources

[Jump to section titled: Resolving image sources](https://www.11ty.dev/docs/plugins/image/#resolving-image-sources)
1.   Relative image sources (`<img src="./possum.png">`) will be co-located to your output directory with the template they are used in. If the same source image is used in multiple templates, it will be written to two different output locations!
2.   Absolute image sources (`<img src="/possum.png">`) will be normalized relative to your input/content directory and written to your output directory with the default directory (e.g. `_site/img/`).

If you explicitly define the [`urlPath` option](https://www.11ty.dev/docs/plugins/image/#url-path), the `urlPath` is used to determine the output location instead.

#### Attribute Overrides

[Jump to section titled: Attribute Overrides](https://www.11ty.dev/docs/plugins/image/#attribute-overrides)
You can configure individual `<img>` elements with per-instance overrides:

*   `<img width>` is aliased to `eleventy:widths` when it is valid HTML (a single `integer` value) Added in Image v6.0.0 _Related [#234](https://github.com/11ty/eleventy-img/issues/234)_.
*   `<img eleventy:widths="200,600">` comma separated string to override the default widths.
*   `<img eleventy:formats="webp">` comma separated string to override the default formats.
*   `<img eleventy:ignore>` skips this image.
*   `<img eleventy:optional>`Added in Image v6.0.0 controls what happens when processing this image throws an Error (good for remote images), see [`failOnError` option](https://www.11ty.dev/docs/plugins/image/#fail-on-error). Default behavior removes the `src` attribute from the `<img>` node. 
    *   `<img eleventy:optional="keep">`: leave as-is, which would likely result in an error when a user visits your page.
    *   `<img eleventy:optional="placeholder">`: replace the `src` attribute with a transparent PNG Data URI.

*   `<img eleventy:output>` overrides the output directory. Similar to [`urlPath`](https://www.11ty.dev/docs/plugins/image/#url-path), absolute paths (e.g. `<img eleventy:output="/mydirectory/">`) are relative to the Eleventy output directory and relative paths are relative to the template’s URL (e.g. `<img eleventy:output="./mydirectory/">`).
*   `<img eleventy:pictureattr:NAME="VALUE">`Added in Image v6.0.0 attributes are hoisted as `<picture NAME="VALUE">` (if `<picture>` is in use)

### More configuration options

[Jump to section titled: More configuration options](https://www.11ty.dev/docs/plugins/image/#more-configuration-options)
Any of the [configuration options](https://www.11ty.dev/docs/plugins/image/#options) can be defined when you add the plugin:

eleventy.config.js

```
import { eleventyImageTransformPlugin } from "@11ty/eleventy-img";

export default function (eleventyConfig) {
	eleventyConfig.addPlugin(eleventyImageTransformPlugin, {
		// output image formats
		formats: ["avif", "webp", "jpeg"],

		// output image widths
		widths: ["auto"],

		// optional, attributes assigned on <img> nodes override these values
		htmlOptions: {
			imgAttributes: {
				loading: "lazy",
				decoding: "async",
			},
			pictureAttributes: {}
		},
	});
};
```

*   Added in v3.0.0 Added in Image v5.0.0 During local development (when using `--serve`), images are optimized when requested in the browser. Read more about [`transformOnRequest`](https://www.11ty.dev/docs/plugins/image/#optimize-images-on-request).
*   The `sizes` attribute must be present if `widths` has more than one entry ([MDN](https://developer.mozilla.org/en-US/docs/Web/API/HTMLImageElement/sizes)). The `eleventyImageTransformPlugin` does not provide a default value for `sizes`, so it must be explicitly included in the HTML attribute or with `htmlOptions.imgAttributes`. 
    *   Added in Image v6.0.0 When using `loading="lazy"` and `sizes` is not supplied in markup — we’ll use `sizes="auto"` automatically. _Related [#207](https://github.com/11ty/eleventy-img/issues/207)_.

Build Performance
-----------------

[Jump to section titled: Build Performance](https://www.11ty.dev/docs/plugins/image/#build-performance)
Image optimization is likely one of the costlier pieces of your Eleventy build. The total build cost of this utility is dependent on a few things (in order of priority):

1.   Number of unique images optimized (not page count)
2.   Optimizing a lot of remote images (image content must be fetched from a remote server and is subsequently cached via [`eleventy-fetch`](https://www.11ty.dev/docs/plugins/fetch/)).
3.   Number of `formats` you generate for each source image: `avif` is more costly than other image formats. `+1` Build Cost
4.   Number of `widths` you generate for each source image.
5.   File size of images being optimized (larger source images are more expensive).

### Optimize Images on Request

[Jump to section titled: Optimize Images on Request](https://www.11ty.dev/docs/plugins/image/#optimize-images-on-request)
Added in v3.0.0 Added in Image v5.0.0 When using the [Image HTML transform](https://www.11ty.dev/docs/plugins/image/#html-transform) during local development, image processing is removed from the build for extra performance. Instead, they are processed when requested by the browser using a special middleware built-in to the Eleventy Dev Server. This is enabled or disabled using the [`transformOnRequest` option](https://www.11ty.dev/docs/plugins/image/#transform-on-request).

### In-Memory Cache

[Jump to section titled: In-Memory Cache](https://www.11ty.dev/docs/plugins/image/#in-memory-cache)
To prevent duplicate work and improve build performance, repeated calls to the same source image (remote or local) _with the same options_ will return a cached results object. If a request in-progress, the pending promise will be returned. This in-memory cache is maintained across builds in watch/serve mode. If you quit Eleventy, the in-memory cache will be discarded.

Images will be regenerated (and the cache bypassed) if:

*   The source image file size changes (on local image files)
*   The [cache asset](https://www.11ty.dev/docs/plugins/fetch/) duration expires (for remote images).

You can disable this behavior by using the [`useCache` option](https://www.11ty.dev/docs/plugins/image/#use-cache).

Example of in-memory cache reuse (returns the same promise)
**Filename**.eleventy.js

```
import Image from "@11ty/eleventy-img";

let stats1 = Image("./test/bio-2017.jpg");
let stats2 = Image("./test/bio-2017.jpg");

console.assert(stats1 === stats2, "The same promise");
```

Example of in-memory cache (returns a new promise with different options)
**Filename**eleventy.config.js

```
import Image from "@11ty/eleventy-img";

let stats1 = Image("./test/bio-2017.jpg");
let stats2 = Image("./test/bio-2017.jpg", { widths: [300] });

console.assert(stats1 !== stats2, "A different promise");
```

### Disk Cache

[Jump to section titled: Disk Cache](https://www.11ty.dev/docs/plugins/image/#disk-cache)
Added in Image v1.0.0 Eleventy will skip processing files that are unchanged and already exist in the output directory. This requires the built-in hashing algorithm and is not supported with custom filenames. More background at [Issue #51](https://github.com/11ty/eleventy-img/issues/51).

You can use this to [speed up builds on your build server](https://www.11ty.dev/docs/deployment/#persisting-cache).

Options
-------

[Jump to section titled: Options](https://www.11ty.dev/docs/plugins/image/#options)
### Output File Extensions

[Jump to section titled: Output File Extensions](https://www.11ty.dev/docs/plugins/image/#output-file-extensions)
Comma separated list of file extensions used in the [Image HTML Transform](https://www.11ty.dev/docs/plugins/image/#html-transform) to determine which template output files to process.

*   `extensions: "html"` (default)

### Output Widths

[Jump to section titled: Output Widths](https://www.11ty.dev/docs/plugins/image/#output-widths)
Controls how many output images will be created for each image format. Aspect ratio is preserved.

*   `widths: ["auto"]` (default, keep original width)
*   `widths: [200]` (output one 200px width)
*   `widths: [200, "auto"]` (output 200px and original width)

### Output Formats

[Jump to section titled: Output Formats](https://www.11ty.dev/docs/plugins/image/#output-formats)
Use almost any combination of `webp`, `jpeg`, `png`, `svg`, `avif`, `gif`, and `auto`:

*   `formats: ["webp", "jpeg"]` (default)
*   `formats: ["png"]`
*   `formats: ["auto"]` (keep original format)
*   `formats: ["svg"]` (requires SVG input)
*   `formats: ["avif"]`[`+1` Build Cost](https://www.11ty.dev/docs/plugins/image/#build-cost)

### Skip raster formats for SVG

[Jump to section titled: Skip raster formats for SVG](https://www.11ty.dev/docs/plugins/image/#skip-raster-formats-for-svg)
If using SVG output (the input format is SVG and `svg` is in your `formats` array option), we will skip all of the raster formats even if they’re in `formats`. This may be useful in a CMS-driven workflow when the input could be vector or raster.

*   `svgShortCircuit: false` (default)
*   `svgShortCircuit: true`
*   `svgShortCircuit: "size"`Added in Image v3.1.8

Using `svgShortCircuit: "size"` means that raster image format entries will only be thrown out if the optimized raster size is larger than the SVG. This helps with large SVG images that compress to smaller raster sizes at smaller widths and will prefer the SVG over raster formats when the SVG file size is smaller.

To use Brotli compressed SVG sizes when making file size comparisons, use the `svgCompressionSize: "br"` option Added in Image v3.1.8.

[Jump to section titled: Related:](https://www.11ty.dev/docs/plugins/image/#related)
### Allow SVG to upscale

[Jump to section titled: Allow SVG to upscale](https://www.11ty.dev/docs/plugins/image/#allow-svg-to-upscale)
While we do prevent raster images from upscaling (and filter upscaling `widths` from the output), you can optionally enable SVG input to upscale to larger sizes when converting to raster format.

*   `svgAllowUpscale: true` (default)
*   `svgAllowUpscale: false`

### Transparent Images

[Jump to section titled: Transparent Images](https://www.11ty.dev/docs/plugins/image/#transparent-images)
Transparency friendly formats: `avif`, `png`, `webp`, `gif`, and `svg`.

Added in Image v6.0.0 We will [filter out any non-transparency-friendly output formats](https://www.11ty.dev/docs/plugins/image/#format-filtering) from your `formats` list automatically (as long as at least _one_ of them is `png`, `gif`, or `svg`).

### Animated Images

[Jump to section titled: Animated Images](https://www.11ty.dev/docs/plugins/image/#animated-images)
Added in Image v1.1.0 To process and output animated `gif` or `webp` images, [use `sharpOptions`](https://www.11ty.dev/docs/plugins/image/#advanced-control-of-sharp-image-processor) to pass in an `animated` option.

```
import Image from "@11ty/eleventy-img";

await Image("./test/bio-2017.jpg", {
	formats: ["webp", "gif"],

	sharpOptions: {
		animated: true,
	},
});
```

Added in Image v6.0.0 We will [filter out any non-animation-friendly output formats](https://www.11ty.dev/docs/plugins/image/#format-filtering) from your `formats` list automatically (as long as at least _one_ of them supports animation).

### Transform on Request

[Jump to section titled: Transform on Request](https://www.11ty.dev/docs/plugins/image/#transform-on-request)
Development build performance improvement to [optimize images when they are requested in the browser](https://www.11ty.dev/docs/plugins/image/#optimize-images-on-request).

*   `transformOnRequest: false` (default)
*   `transformOnRequest: process.env.ELEVENTY_RUN_MODE === "serve"` (default for HTML Transform)

You can use [`transformOnRequest` with Shortcodes too](https://www.11ty.dev/docs/plugins/image-shortcodes/#boost-performance-optimize-images-on-request).

### `returnType` and `htmlOptions`

[Jump to section titled: returnType and htmlOptions](https://www.11ty.dev/docs/plugins/image/#return-type-and-html-options)
By default, Eleventy Image will return a metadata JavaScript object. To return HTML instead, use `returnType: "html"`. This is useful for the [Image JavaScript API](https://www.11ty.dev/docs/plugins/image-js/#return-html) and [Image Shortcode](https://www.11ty.dev/docs/plugins/image-shortcodes/) types.

*   `returnType: "object"` (default) or `"html"`Added in Image v6.0.0

Further customize the markup with `htmlOptions`Added in Image v6.0.0:

```
{
	// …
	returnType: "html",

	htmlOptions: {
		imgAttributes: {
			alt : "", // required
			loading: "lazy",
			decoding: "async",
		},

		// HTML attributes added to `<picture>` (omitted when <img> used)
		pictureAttributes: {},

		// Which source to use for `<img width height src>` attributes
		fallback: "largest", // or "smallest"
	}
}
```

### Fix Orientation

[Jump to section titled: Fix Orientation](https://www.11ty.dev/docs/plugins/image/#fix-orientation)
Added in Image v4.0.0 Rotates the image to enforce the correct orientation set in EXIF metadata.

*   `fixOrientation: false` (default)
*   `fixOrientation: true`

### Custom Filenames

[Jump to section titled: Custom Filenames](https://www.11ty.dev/docs/plugins/image/#custom-filenames)
Don’t like the hashes used in output file names? Make your own!

```
{
	// …
	filenameFormat: function (id, src, width, format, options) {
		// Define custom filenames for generated images
		// id: hash of the original image
		// src: original image path
		// width: current width in px
		// format: current file format
		// options: set of options passed to the Image call

		return `${id}-${width}.${format}`;
	}
}
```

Custom Filename Example: Use the original file slug
```
import path from "node:path";
import Image from "@11ty/eleventy-img";

await Image("./test/bio-2017.jpg", {
	widths: [300],
	formats: ["auto"],
	filenameFormat: function (id, src, width, format, options) {
		const extension = path.extname(src);
		const name = path.basename(src, extension);

		return `${name}-${width}w.${format}`;
	},
});

// Writes: "test/img/bio-2017-300w.jpeg"
```

### Dry-Run

[Jump to section titled: Dry-Run](https://www.11ty.dev/docs/plugins/image/#dry-run)
If you want to try the utility out and not write any files (useful for testing), use the `dryRun` option. Will include a `buffer` property in your return object.

*   `dryRun: false` (default)
*   `dryRun: true`

Advanced Options
----------------

[Jump to section titled: Advanced Options](https://www.11ty.dev/docs/plugins/image/#advanced-options)
### Fail on Error

[Jump to section titled: Fail on Error](https://www.11ty.dev/docs/plugins/image/#fail-on-error)
Added in Image v6.0.0 What happens when processing an image encounters an error? Useful for remote images.

*   `failOnError: true` (default)
*   `failOnError: false` no error is thrown (warning output is logged)

See also the [`eleventy:optional` attribute](https://www.11ty.dev/docs/plugins/image/#attribute-overrides). _Related [#225](https://github.com/11ty/eleventy-img/issues/225)_

### Format Filtering

[Jump to section titled: Format Filtering](https://www.11ty.dev/docs/plugins/image/#format-filtering)
Added in Image v6.0.0 When using [animated images](https://www.11ty.dev/docs/plugins/image/#animated-images) or images with transparency, we will automatically filter your [output `formats`](https://www.11ty.dev/docs/plugins/image/#output-formats) list to formats that support those features. If there are no valid `formats` left after filtering, the original `formats` list is used as-is. You can enable or disable this feature using the `formatFiltering` option.

*   `formatFiltering: ["transparent", "animated"]`

_Related [#105](https://github.com/11ty/eleventy-img/issues/105) and [#260](https://github.com/11ty/eleventy-img/issues/260)_

### Output Directory

[Jump to section titled: Output Directory](https://www.11ty.dev/docs/plugins/image/#output-directory)
Where to write the new images to disk. Project-relative path to the output image directory. Maybe you want to write these to your output directory directly (e.g. `./_site/img/`)?

*   `outputDir: "./img/"` (default)

If you’re using the Image HTML Transform, we recommended **_not_** to define `outputDir`.

### URL Path

[Jump to section titled: URL Path](https://www.11ty.dev/docs/plugins/image/#url-path)
A path-prefix-esque directory for the `<img src>` attribute. e.g. `/img/` for `<img src="/img/MY_IMAGE.jpeg">`:

*   `urlPath: "/img/"` (default)

Added in Image v6.0.0 Full URLs are now supported, e.g. `urlPath: "https://example.com/img/"`. _Related [#239](https://github.com/11ty/eleventy-img/issues/239)_.

If you’re using the Image HTML Transform, we recommended **_not_** to define `urlPath`.

### Use Cache

[Jump to section titled: Use Cache](https://www.11ty.dev/docs/plugins/image/#use-cache)
(Boolean) Controls whether to use the [disk cache](https://www.11ty.dev/docs/plugins/image/#disk-cache) and [memory cache](https://www.11ty.dev/docs/plugins/image/#in-memory-cache).

*   `useCache: true` (default)
*   `useCache: false` to bypass the cache and generate a new image every time.

### Advanced control of Sharp image processor

[Jump to section titled: Advanced control of Sharp image processor](https://www.11ty.dev/docs/plugins/image/#advanced-control-of-sharp-image-processor)
[Extra options to pass to the Sharp constructor](https://sharp.pixelplumbing.com/api-constructor#parameters) or the [Sharp image format converter for webp](https://sharp.pixelplumbing.com/api-output#webp), [png](https://sharp.pixelplumbing.com/api-output#png), [jpeg](https://sharp.pixelplumbing.com/api-output#jpeg), or [avif](https://sharp.pixelplumbing.com/api-output#avif).

*   `sharpOptions: {}`
*   `sharpWebpOptions: {}`
*   `sharpPngOptions: {}`
*   `sharpJpegOptions: {}`
*   `sharpAvifOptions: {}`

Added in Image v6.0.0[ICC Profiles](https://sharp.pixelplumbing.com/api-output#keepiccprofile) are preserved by default (when available) for better colors when images have `srgb`, `p3`, or `cmyk` color profiles. _Related [#244](https://github.com/11ty/eleventy-img/issues/244)_.

#### Full Sharp API Access

[Jump to section titled: Full Sharp API Access](https://www.11ty.dev/docs/plugins/image/#full-sharp-api-access)
Use the `transform` callback to access anything in the [Sharp API](https://sharp.pixelplumbing.com/api-constructor). _Related [#52](https://github.com/11ty/eleventy-img/issues/52)_. This runs before Eleventy Image processing (keep EXIF metadata, rotation, cropping, et al).

```
{
	// …
	transform: (sharp) => {
		sharp.keepExif();
	}
}
```

### Change Global Plugin Concurrency

[Jump to section titled: Change Global Plugin Concurrency](https://www.11ty.dev/docs/plugins/image/#change-global-plugin-concurrency)
```
import Image from "@11ty/eleventy-img";
Image.concurrency = 4; // default is between 8 and 16 based on os.availableParallelism()
```

### Change the default Hash length

[Jump to section titled: Change the default Hash length](https://www.11ty.dev/docs/plugins/image/#change-the-default-hash-length)
Added in v1.0.0 You can customize the length of the default filename format hash by using the `hashLength` property.

```
{
	// …
	hashLength: 8, // careful, don’t make it _too_ short!
}
```

### Advanced Caching Options for Remote Images

[Jump to section titled: Advanced Caching Options for Remote Images](https://www.11ty.dev/docs/plugins/image/#advanced-caching-options-for-remote-images)
For any full URL first argument to this plugin, the full-size remote image will be downloaded and cached locally. See all [relevant `eleventy-fetch` options](https://www.11ty.dev/docs/plugins/fetch/#options).

```
{
	// …
	cacheOptions: {
		// if a remote image URL, this is the amount of time before it fetches a fresh copy
		duration: "1d",

		// project-relative path to the cache directory
		directory: ".cache",

		removeUrlQueryParams: false,
	},
}
```

When caching remote images, you may want to check the processed image output into your `git` (et al) repository to avoid refetches in the future. If remote images are _not_ checked in, they may be refetched every time on your CI server unless you [preserve the `.cache` folder between builds](https://www.11ty.dev/docs/plugins/fetch/#running-this-on-your-build-server).

### Using a Hosted Image Service

[Jump to section titled: Using a Hosted Image Service](https://www.11ty.dev/docs/plugins/image/#using-a-hosted-image-service)
#### Custom URLs

[Jump to section titled: Custom URLs](https://www.11ty.dev/docs/plugins/image/#custom-urls)
Want to use a hosted image service instead? You can override the entire URL. Takes precedence over `filenameFormat` option. Useful with `statsSync` or `statsByDimensionsSync`.

The metadata object returned will not include `filename` or `outputPath` properties.

```
{
	// …
	urlFormat: function ({
		hash, // not included for `statsOnly` images
		src,
		width,
		format,
	}) {
		return `https://example.com/${encodeURIComponent(src)}/${width}/${format}/`;
	}
}
```

*   [_Example on `11ty-website`_](https://github.com/11ty/11ty-website/blob/516faa397a98f8990f3d02eb41e1c99bedfab9cf/.eleventy.js#L105)

#### Stats Only

[Jump to section titled: Stats Only](https://www.11ty.dev/docs/plugins/image/#stats-only)
Added in Image v1.1.0 Skips all image processing to return metadata. Doesn’t write files. Use this as an alternative to the separate `statsSync*` functions—this will use in-memory cache and de-duplicate requests.

*   `statsOnly: false` (default)
*   `statsOnly: true`

[Jump to section titled: From the Community](https://www.11ty.dev/docs/plugins/image/#from-the-community)
×141 resources via **[11tybundle.dev](https://11tybundle.dev/)** curated by [![Image 1: Favicon for v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fwww.bobmonsour.com%2F](https://v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fwww.bobmonsour.com%2F/)Bob Monsour](https://www.bobmonsour.com/).

**_Expand to see 136 more resources._**
*   [![Image 2: Favicon for v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fdsriseah.com%2Fjournal%2F2025%2F1016%2F](https://v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fdsriseah.com%2Fjournal%2F2025%2F1016%2F/)Eleventy Templates for Atom Feeds](https://dsriseah.com/journal/2025/1016/) — _DSri Seah (2025)_
*   [![Image 3: Favicon for v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fwww.cantoni.org%2F2025%2F10%2F14%2Fsimple-lossless-image-compression%2F](https://v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fwww.cantoni.org%2F2025%2F10%2F14%2Fsimple-lossless-image-compression%2F/)Simple Lossless Image Compression](https://www.cantoni.org/2025/10/14/simple-lossless-image-compression/) — _Brian Cantoni (2025)_
*   [![Image 4: Favicon for v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fashfurrow.com%2Fblog%2Feleventy-launch%2F](https://v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fashfurrow.com%2Fblog%2Feleventy-launch%2F/)Eleventy Launch](https://ashfurrow.com/blog/eleventy-launch/) — _Ash Furrow (2025)_
*   [![Image 5: Favicon for v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fshivjm.blog%2Fhire-shivjm-in%2F](https://v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fshivjm.blog%2Fhire-shivjm-in%2F/)hire.shivjm.in: The Missing Cover Letter](https://shivjm.blog/hire-shivjm-in/) — _Shiv J.M. (2025)_
*   [![Image 6: Favicon for v1.indieweb-avatar.11ty.dev/https%3A%2F%2Finfrequently.org%2F2025%2F10%2F11ty-hacks-for-fun-and-performance%2F](https://v1.indieweb-avatar.11ty.dev/https%3A%2F%2Finfrequently.org%2F2025%2F10%2F11ty-hacks-for-fun-and-performance%2F/)11ty Hacks for Fun and Performance](https://infrequently.org/2025/10/11ty-hacks-for-fun-and-performance/) — _Alex Russell (2025)_
*   [![Image 7: Favicon for v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fblog.nicholas.clooney.io%2Fposts%2Fresponsive-images-eleventy-img%2F](https://v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fblog.nicholas.clooney.io%2Fposts%2Fresponsive-images-eleventy-img%2F/)Leveling Up Responsive Images with Eleventy Img](https://blog.nicholas.clooney.io/posts/responsive-images-eleventy-img/) — _Nicholas Clooney (2025)_
*   [![Image 8: Favicon for v1.indieweb-avatar.11ty.dev/https%3A%2F%2Falix.guillard.fr%2Fnotes%2Fdotclear-to-eleventy%2Fcontent-migration%2F](https://v1.indieweb-avatar.11ty.dev/https%3A%2F%2Falix.guillard.fr%2Fnotes%2Fdotclear-to-eleventy%2Fcontent-migration%2F/)From Dotclear to Eleventy 3](https://alix.guillard.fr/notes/dotclear-to-eleventy/content-migration/) — _Alix Guillard (2025)_
*   [![Image 9: Favicon for v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fquesby.dev%2Fblog%2Feleventy-responsive-images-and-inline-svg%2F](https://v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fquesby.dev%2Fblog%2Feleventy-responsive-images-and-inline-svg%2F/)Quick Start: Eleventy Shortcodes for Responsive Images & Inline SVG](https://quesby.dev/blog/eleventy-responsive-images-and-inline-svg/) — _Emiliano Soravia (2025)_
*   [![Image 10: Favicon for v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fchriskirknielsen.com%2Fblog%2Fconditional-favicon-with-eleventy-passthrough-copy%2F](https://v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fchriskirknielsen.com%2Fblog%2Fconditional-favicon-with-eleventy-passthrough-copy%2F/)Conditional favicon in Elev­enty using passthrough copy](https://chriskirknielsen.com/blog/conditional-favicon-with-eleventy-passthrough-copy/) — _Christopher Kirk-Nielsen (2025)_
*   [![Image 11: Favicon for v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fmy.stuffandthings.lol%2Fblog%2F2025-08-23%2Fog-images-using-11ty-screenshot-service.html](https://v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fmy.stuffandthings.lol%2Fblog%2F2025-08-23%2Fog-images-using-11ty-screenshot-service.html/)OG Images using 11ty Screenshot Service](https://my.stuffandthings.lol/blog/2025-08-23/og-images-using-11ty-screenshot-service.html) — _Jason Moser (2025)_
*   [![Image 12: Favicon for v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fwww.cantoni.org%2F2025%2F08%2F18%2Fsolving-my-image-dimension-problem-with-an-eleventy-transform%2F](https://v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fwww.cantoni.org%2F2025%2F08%2F18%2Fsolving-my-image-dimension-problem-with-an-eleventy-transform%2F/)Solving my Image Dimension Problem with an Eleventy Transform](https://www.cantoni.org/2025/08/18/solving-my-image-dimension-problem-with-an-eleventy-transform/) — _Brian Cantoni (2025)_
*   [![Image 13: Favicon for v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fwww.zachleat.com%2Fweb%2Ffaster-builds-with-eleventy-img%2F](https://v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fwww.zachleat.com%2Fweb%2Ffaster-builds-with-eleventy-img%2F/)One weird trick to reduce Eleventy Image Build Times by 60%](https://www.zachleat.com/web/faster-builds-with-eleventy-img/) — _Zach Leatherman (2025)_
*   [![Image 14: Favicon for v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fchrismcleod.dev%2Fblog%2Fmigrating-an-eleventy-site-to-bunnynet%2F](https://v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fchrismcleod.dev%2Fblog%2Fmigrating-an-eleventy-site-to-bunnynet%2F/)Migrating An Eleventy Site to Bunny.Net](https://chrismcleod.dev/blog/migrating-an-eleventy-site-to-bunnynet/) — _Chris McLeod (2025)_
*   [![Image 15: Favicon for v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fblog.martin-haehnel.de%2Fhow-to-use-eleventy-img-to-optmize-images-in-eleventy-with-caching-to-keep-build-times-low-on-cloudflare-pages-which-cant-cache-optimize-images-out-of-the-box%2F](https://v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fblog.martin-haehnel.de%2Fhow-to-use-eleventy-img-to-optmize-images-in-eleventy-with-caching-to-keep-build-times-low-on-cloudflare-pages-which-cant-cache-optimize-images-out-of-the-box%2F/)How To Use eleventy-img (To Optmize Images In Eleventy) With Caching (To Keep Build Times Low) On Cloudflare Pages (Which Can't Cache Optimize Images Out Of The Box)](https://blog.martin-haehnel.de/how-to-use-eleventy-img-to-optmize-images-in-eleventy-with-caching-to-keep-build-times-low-on-cloudflare-pages-which-cant-cache-optimize-images-out-of-the-box/) — _Martin Hähnel (2025)_
*   [![Image 16: Favicon for v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fwww.cantoni.org%2F2025%2F07%2F12%2Fmigrating-wordpress-to-eleventy%2F](https://v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fwww.cantoni.org%2F2025%2F07%2F12%2Fmigrating-wordpress-to-eleventy%2F/)Migrating WordPress To Eleventy](https://www.cantoni.org/2025/07/12/migrating-wordpress-to-eleventy/) — _Brian Cantoni (2025)_
*   [![Image 17: Favicon for v1.indieweb-avatar.11ty.dev/https%3A%2F%2F11tycms.com%2Fblog%2Fposts%2F11tycms-image-uploads-and-design-enhancements%2F](https://v1.indieweb-avatar.11ty.dev/https%3A%2F%2F11tycms.com%2Fblog%2Fposts%2F11tycms-image-uploads-and-design-enhancements%2F/)11tyCMS: Image uploads and design enhancements](https://11tycms.com/blog/posts/11tycms-image-uploads-and-design-enhancements/) — _Jessie Heald (2025)_
*   [![Image 18: Favicon for v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fblog.martin-haehnel.de%2F2025%2F06%2F28%2Fworking-with-r2-from-obsidian%2F](https://v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fblog.martin-haehnel.de%2F2025%2F06%2F28%2Fworking-with-r2-from-obsidian%2F/)Uploading Images For Your Eleventy Blog to Cloudflare R2 from Obsidian](https://blog.martin-haehnel.de/2025/06/28/working-with-r2-from-obsidian/) — _Martin Hähnel (2025)_
*   [![Image 19: Favicon for v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fjeremyrobertjones.com%2Fblog%2Fproportional-equal-height-image-row-css-11ty-nunjucks%2F](https://v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fjeremyrobertjones.com%2Fblog%2Fproportional-equal-height-image-row-css-11ty-nunjucks%2F/)Creating proportional, equal-height image rows with CSS, 11ty, and Nunjucks](https://jeremyrobertjones.com/blog/proportional-equal-height-image-row-css-11ty-nunjucks/) — _Jeremy Robert Jones (2025)_
*   [![Image 20: Favicon for v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fchrisburnell.com%2Fnote%2Feleventy-animated-88x31%2F](https://v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fchrisburnell.com%2Fnote%2Feleventy-animated-88x31%2F/)'Built with Eleventy' Animated 88x31](https://chrisburnell.com/note/eleventy-animated-88x31/) — _Chris Burnell (2025)_
*   [![Image 21: Favicon for v1.indieweb-avatar.11ty.dev/https%3A%2F%2F11tycms.com%2Fblog%2Fposts%2F11tycms-trapped-in-image-hell%2F](https://v1.indieweb-avatar.11ty.dev/https%3A%2F%2F11tycms.com%2Fblog%2Fposts%2F11tycms-trapped-in-image-hell%2F/)11tyCMS: Trapped in image and markdown hell](https://11tycms.com/blog/posts/11tycms-trapped-in-image-hell/) — _Jessie Heald (2025)_
*   [![Image 22: Favicon for v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fflohgro.com%2Fblog%2Fmy-11ty-blogging-workflow%2F](https://v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fflohgro.com%2Fblog%2Fmy-11ty-blogging-workflow%2F/)My 11ty Blogging Workflow](https://flohgro.com/blog/my-11ty-blogging-workflow/) — _Floh Gro (2025)_
*   [![Image 23: Favicon for v1.indieweb-avatar.11ty.dev/https%3A%2F%2Factuallysomecat.github.io%2Fblog%2F2025-05-18%2520-%2520custom%2520emoji%2520shortcodes%2520in%252011ty%2520with%2520a%2520plugin%2F](https://v1.indieweb-avatar.11ty.dev/https%3A%2F%2Factuallysomecat.github.io%2Fblog%2F2025-05-18%2520-%2520custom%2520emoji%2520shortcodes%2520in%252011ty%2520with%2520a%2520plugin%2F/)custom emoji in 11ty with a plugin](https://actuallysomecat.github.io/blog/2025-05-18%20-%20custom%20emoji%20shortcodes%20in%2011ty%20with%20a%20plugin/) — _actuallysomecat (2025)_
*   [![Image 24: Favicon for v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fvalentinpratz.de%2Fposts%2F2025-05-17-eleventy-plugin-gallery%2F](https://v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fvalentinpratz.de%2Fposts%2F2025-05-17-eleventy-plugin-gallery%2F/)A Slightly Improved Image Gallery for Eleventy](https://valentinpratz.de/posts/2025-05-17-eleventy-plugin-gallery/) — _Valentin Pratz (2025)_
*   [![Image 25: Favicon for v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fchipcullen.com%2Fhow-i-built-dynamic-social-media-images-in-eleventy-using-cloudinary%2F](https://v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fchipcullen.com%2Fhow-i-built-dynamic-social-media-images-in-eleventy-using-cloudinary%2F/)How I built dynamic social media images in Eleventy using Cloudinary](https://chipcullen.com/how-i-built-dynamic-social-media-images-in-eleventy-using-cloudinary/) — _Chip Cullen (2025)_
*   [![Image 26: Favicon for v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fwww.inconsistent.software%2Fblog%2F2025-04-hello-eleventy-3%2F](https://v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fwww.inconsistent.software%2Fblog%2F2025-04-hello-eleventy-3%2F/)Hello 11ty 3](https://www.inconsistent.software/blog/2025-04-hello-eleventy-3/) — _Judah Perez (2025)_
*   [![Image 27: Favicon for v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fhamatti.org%2Fposts%2Fhow-i-write-and-publish-blog-posts-in-april-2025%2F](https://v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fhamatti.org%2Fposts%2Fhow-i-write-and-publish-blog-posts-in-april-2025%2F/)How I write and publish blog posts in April 2025](https://hamatti.org/posts/how-i-write-and-publish-blog-posts-in-april-2025/) — _Juha-Matti Santala (2025)_
*   [![Image 28: Favicon for v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fethanmarcotte.com%2Fwrote%2Fmagick-images%2F](https://v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fethanmarcotte.com%2Fwrote%2Fmagick-images%2F/)Magick images](https://ethanmarcotte.com/wrote/magick-images/) — _Ethan Marcotte (2025)_
*   [![Image 29: Favicon for v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fblog.chobble.com%2Fblog%2F25-04-16-adding-base64-image-backgrounds-to-eleventy-img%2F](https://v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fblog.chobble.com%2Fblog%2F25-04-16-adding-base64-image-backgrounds-to-eleventy-img%2F/)Adding base64 placeholder background images to eleventy-img](https://blog.chobble.com/blog/25-04-16-adding-base64-image-backgrounds-to-eleventy-img/) — _Stefan Burke (2025)_
*   [![Image 30: Favicon for v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fsyntackle.com%2Fblog%2Feleventy-image-html-transform-plugin-disk-cache%2F](https://v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fsyntackle.com%2Fblog%2Feleventy-image-html-transform-plugin-disk-cache%2F/)Eleventy's Image Plugin Disk Caching Approach For HTML Transform Method](https://syntackle.com/blog/eleventy-image-html-transform-plugin-disk-cache/) — _Murtuzaali Surti (2025)_
*   [![Image 31: Favicon for v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fwww.zachleat.com%2Fweb%2Fextract-colors%2F](https://v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fwww.zachleat.com%2Fweb%2Fextract-colors%2F/)Extract Colors from an Image for CSS Themes](https://www.zachleat.com/web/extract-colors/) — _Zach Leatherman (2025)_
*   [![Image 32: Favicon for v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fdamianwalsh.co.uk%2Fposts%2Fcreating-connections-with-music-and-technology%2F](https://v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fdamianwalsh.co.uk%2Fposts%2Fcreating-connections-with-music-and-technology%2F/)Building a personal digital music library with Eleventy and APIs](https://damianwalsh.co.uk/posts/creating-connections-with-music-and-technology/) — _Damian Walsh (2025)_
*   [![Image 33: Favicon for v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fnotes.jays.net%2Fblog%2F11ty%2F](https://v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fnotes.jays.net%2Fblog%2F11ty%2F/)11ty and OG images](https://notes.jays.net/blog/11ty/) — _Jay Hannah (2025)_
*   [![Image 34: Favicon for v1.indieweb-avatar.11ty.dev/https%3A%2F%2Frknight.me%2Fblog%2Floading-pixelfed-photos-with-eleventy%2F](https://v1.indieweb-avatar.11ty.dev/https%3A%2F%2Frknight.me%2Fblog%2Floading-pixelfed-photos-with-eleventy%2F/)Loading Pixelfed Photos with Eleventy](https://rknight.me/blog/loading-pixelfed-photos-with-eleventy/) — _Robb Knight (2025)_
*   [![Image 35: Favicon for v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fblog.embee.co%2Fposts%2F11ty-open-graph-funtimes%2F](https://v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fblog.embee.co%2Fposts%2F11ty-open-graph-funtimes%2F/)Eleventy, Open Graph images and fun?](https://blog.embee.co/posts/11ty-open-graph-funtimes/) — _Matt B (2025)_
*   [![Image 36: Favicon for v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fblog.chobble.com%2Fblog%2F25-01-19-social-preview-images%2F](https://v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fblog.chobble.com%2Fblog%2F25-01-19-social-preview-images%2F/)Adding social preview images to my Eleventy blog](https://blog.chobble.com/blog/25-01-19-social-preview-images/) — _Stefan Burke (2025)_
*   [![Image 37: Favicon for v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fmelkat.blog%2Fp%2F11ty-rewrite%2F](https://v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fmelkat.blog%2Fp%2F11ty-rewrite%2F/)Rewriting My Astro Blog with Eleventy](https://melkat.blog/p/11ty-rewrite/) — _Melanie Kat (2025)_
*   [![Image 38: Favicon for v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fdanburzo.ro%2Fnotes%2Feleventy-og-images%2F](https://v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fdanburzo.ro%2Fnotes%2Feleventy-og-images%2F/)Build-time og:image generation with eleventy-img](https://danburzo.ro/notes/eleventy-og-images/) — _Dan Cătălin Burzo (2025)_
*   [![Image 39: Favicon for v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fmy.stuffandthings.lol%2Fblog%2F2025-01-15%2Fo-m-g-images.html](https://v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fmy.stuffandthings.lol%2Fblog%2F2025-01-15%2Fo-m-g-images.html/)O(M)G Images](https://my.stuffandthings.lol/blog/2025-01-15/o-m-g-images.html) — _Jason Moser (2025)_
*   [![Image 40: Favicon for v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3De0OHgC677ec](https://v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3De0OHgC677ec/)Optimize Your Web Site's Images](https://www.youtube.com/watch?v=e0OHgC677ec) — _Zach Leatherman (2025)_
*   [![Image 41: Favicon for v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fbobmonsour.com%2Fblog%2Fbuilding-the-book-page%2F](https://v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fbobmonsour.com%2Fblog%2Fbuilding-the-book-page%2F/)How I built the Books page](https://bobmonsour.com/blog/building-the-book-page/) — _Bob Monsour (2025)_
*   [![Image 42: Favicon for v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fthisguise.wtf%2Fblog%2F2024%2F12%2F04%2Fan-idiots-guide-to-adding-open-graph-images-to-an-11ty-blog%2F](https://v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fthisguise.wtf%2Fblog%2F2024%2F12%2F04%2Fan-idiots-guide-to-adding-open-graph-images-to-an-11ty-blog%2F/)An idiot's guide to adding open graph images to an 11ty blog](https://thisguise.wtf/blog/2024/12/04/an-idiots-guide-to-adding-open-graph-images-to-an-11ty-blog/) — _Chazz Basuta (2024)_
*   [![Image 43: Favicon for v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fbobmonsour.com%2Fblog%2Fgoing-all-in-with-native-markdown%2F](https://v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fbobmonsour.com%2Fblog%2Fgoing-all-in-with-native-markdown%2F/)Going all in with 'native' markdown](https://bobmonsour.com/blog/going-all-in-with-native-markdown/) — _Bob Monsour (2024)_
*   [![Image 44: Favicon for v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fbobmonsour.com%2Fblog%2Ffast-as-hell%2F](https://v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fbobmonsour.com%2Fblog%2Ffast-as-hell%2F/)Eleventy Transform speeds local development...a lot!](https://bobmonsour.com/blog/fast-as-hell/) — _Bob Monsour (2024)_
*   [![Image 45: Favicon for v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fvalentinpratz.de%2Fposts%2F2024-11-13-11ty-jupyter-integration%2F](https://v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fvalentinpratz.de%2Fposts%2F2024-11-13-11ty-jupyter-integration%2F/)Integrating Jupyter Notebook Cells in Eleventy Posts](https://valentinpratz.de/posts/2024-11-13-11ty-jupyter-integration/) — _Valentin Pratz (2024)_
*   [![Image 46: Favicon for v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fwww.coryd.dev%2Fposts%2F2024%2Fheres-how-this-is-all-put-together](https://v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fwww.coryd.dev%2Fposts%2F2024%2Fheres-how-this-is-all-put-together/)Here's how this is all put together](https://www.coryd.dev/posts/2024/heres-how-this-is-all-put-together) — _Cory Dransfeldt (2024)_
*   [![Image 47: Favicon for v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fblog.sebin-nyshkim.net%2Fposts%2Fopen-graph-metadata-and-images-in-eleventy-made-easy%2F](https://v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fblog.sebin-nyshkim.net%2Fposts%2Fopen-graph-metadata-and-images-in-eleventy-made-easy%2F/)Open Graph Metadata and Images in Eleventy Made Easy](https://blog.sebin-nyshkim.net/posts/open-graph-metadata-and-images-in-eleventy-made-easy/) — _Sebin Nyshkim (2024)_
*   [![Image 48: Favicon for v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fsia.codes%2Fposts%2Fsocial-share-images-using-cloudinary%2F](https://v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fsia.codes%2Fposts%2Fsocial-share-images-using-cloudinary%2F/)Dynamic social share images using Cloudinary](https://sia.codes/posts/social-share-images-using-cloudinary/) — _Sia Karamalegos (2024)_
*   [![Image 49: Favicon for v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3D0pvqLW09D38](https://v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3D0pvqLW09D38/)Automatically generating social share images using Cloudinary with Sia Karamalegos](https://www.youtube.com/watch?v=0pvqLW09D38) — _Sia Karamalegos (2024)_
*   [![Image 50: Favicon for v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fblog.sebin-nyshkim.net%2Fposts%2Fresponsive-self-hosted-images-for-your-eleventy-blog%2F](https://v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fblog.sebin-nyshkim.net%2Fposts%2Fresponsive-self-hosted-images-for-your-eleventy-blog%2F/)Responsive, Self-hosted Images for Your Eleventy Blog](https://blog.sebin-nyshkim.net/posts/responsive-self-hosted-images-for-your-eleventy-blog/) — _Sebin Nyshkim (2024)_
*   [![Image 51: Favicon for v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fnotebook.samfeldstein.xyz%2Fnotes%2Fprairie-rose-arena-notes%2F](https://v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fnotebook.samfeldstein.xyz%2Fnotes%2Fprairie-rose-arena-notes%2F/)Prairie Rose Arena - Project Notes](https://notebook.samfeldstein.xyz/notes/prairie-rose-arena-notes/) — _Sam Feldstein (2024)_
*   [![Image 52: Favicon for v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fwww.patrickgrey.co.uk%2Fnotes%2F2024-09-21-my-decap-cms-setup-with-11ty-hosted-on-cloudflare-pages%2F](https://v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fwww.patrickgrey.co.uk%2Fnotes%2F2024-09-21-my-decap-cms-setup-with-11ty-hosted-on-cloudflare-pages%2F/)My Decap CMS setup with 11ty hosted on Cloudflare Pages](https://www.patrickgrey.co.uk/notes/2024-09-21-my-decap-cms-setup-with-11ty-hosted-on-cloudflare-pages/) — _Patrick Grey (2024)_
*   [![Image 53: Favicon for v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fwww.aleksandrhovhannisyan.com%2Fblog%2Feleventy-image-transform%2F](https://v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fwww.aleksandrhovhannisyan.com%2Fblog%2Feleventy-image-transform%2F/)Eleventy Images Just Got Better](https://www.aleksandrhovhannisyan.com/blog/eleventy-image-transform/) — _Aleksandr Hovhannisyan (2024)_
*   [![Image 54: Favicon for v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fwww.raymondcamden.com%2F2024%2F07%2F04%2Fbuilding-a-web-version-of-your-mastodon-archive-with-eleventy](https://v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fwww.raymondcamden.com%2F2024%2F07%2F04%2Fbuilding-a-web-version-of-your-mastodon-archive-with-eleventy/)Building a Web Version of Your Mastodon Archive with Eleventy](https://www.raymondcamden.com/2024/07/04/building-a-web-version-of-your-mastodon-archive-with-eleventy) — _Raymond Camden (2024)_
*   [![Image 55: Favicon for v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fsometimes.digital%2Fposts%2Fadding-a-photostream-to-eleventy%2F](https://v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fsometimes.digital%2Fposts%2Fadding-a-photostream-to-eleventy%2F/)Adding a Photo Stream to an Eleventy Site](https://sometimes.digital/posts/adding-a-photostream-to-eleventy/) — _nonnullish (2024)_
*   [![Image 56: Favicon for v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fptsefton.com%2F2024%2F06%2F24%2Fupdate%2F](https://v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fptsefton.com%2F2024%2F06%2F24%2Fupdate%2F/)Twenty year celebration: Site update number three](https://ptsefton.com/2024/06/24/update/) — _Peter Sefton (2024)_
*   [![Image 57: Favicon for v1.indieweb-avatar.11ty.dev/https%3A%2F%2Falex.zappa.dev%2Fblog%2Fupgrading-to-eleventy-v3%2F](https://v1.indieweb-avatar.11ty.dev/https%3A%2F%2Falex.zappa.dev%2Fblog%2Fupgrading-to-eleventy-v3%2F/)Upgrading to Eleventy v3](https://alex.zappa.dev/blog/upgrading-to-eleventy-v3/) — _Alex Zappa (2024)_
*   [![Image 58: Favicon for v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fshivjm.blog%2Fresponsive-images-in-html-w-and-x%2F](https://v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fshivjm.blog%2Fresponsive-images-in-html-w-and-x%2F/)Responsive Images in HTML: w and x](https://shivjm.blog/responsive-images-in-html-w-and-x/) — _Shiv J.M. (2024)_
*   [![Image 59: Favicon for v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fmarkllobrera.com%2Fposts%2Fupgrading-eleventy-v3%2F](https://v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fmarkllobrera.com%2Fposts%2Fupgrading-eleventy-v3%2F/)Upgrading to Eleventy 3.0](https://markllobrera.com/posts/upgrading-eleventy-v3/) — _Mark Llobrera (2024)_
*   [![Image 60: Favicon for v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fsmth.uk%2Fget-image-pixel-colours-in-eleventy-node%2F](https://v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fsmth.uk%2Fget-image-pixel-colours-in-eleventy-node%2F/)Get image pixel colours in Eleventy/Node](https://smth.uk/get-image-pixel-colours-in-eleventy-node/) — _Sam Smith (2024)_
*   [![Image 61: Favicon for v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fmxb.dev%2Fblog%2Feleventy-v3-update%2F](https://v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fmxb.dev%2Fblog%2Feleventy-v3-update%2F/)Updating to Eleventy v3](https://mxb.dev/blog/eleventy-v3-update/) — _Max Böck (2024)_
*   [![Image 62: Favicon for v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fwww.amykhar.dev%2Fconvert-obsidian-image-links-to-nunjucks-short-codes-in-eleventy%2F](https://v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fwww.amykhar.dev%2Fconvert-obsidian-image-links-to-nunjucks-short-codes-in-eleventy%2F/)Convert Obsidian Image Links to Nunjucks Shortcodes in Eleventy](https://www.amykhar.dev/convert-obsidian-image-links-to-nunjucks-short-codes-in-eleventy/) — _Amy Khar (2024)_
*   [![Image 63: Favicon for v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fsamimaatta.fi%2Fen%2Feleventy-image-problem-with-netlify-s-build%2F](https://v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fsamimaatta.fi%2Fen%2Feleventy-image-problem-with-netlify-s-build%2F/)Eleventy Image problem with Netlify's build](https://samimaatta.fi/en/eleventy-image-problem-with-netlify-s-build/) — _Sami Määttä (2024)_
*   [![Image 64: Favicon for v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fwww.coryd.dev%2Fposts%2F2024%2Fhandling-images-with-b2-netlifys-image-cdn-hazel-and-mountain-duck%2F](https://v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fwww.coryd.dev%2Fposts%2F2024%2Fhandling-images-with-b2-netlifys-image-cdn-hazel-and-mountain-duck%2F/)Handling images with B2, Netlify's image CDN, Hazel and Mountain Duck](https://www.coryd.dev/posts/2024/handling-images-with-b2-netlifys-image-cdn-hazel-and-mountain-duck/) — _Cory Dransfeldt (2024)_
*   [![Image 65: Favicon for v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fwww.markllobrera.com%2Fposts%2Fupgrading-eleventy-v1%2F](https://v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fwww.markllobrera.com%2Fposts%2Fupgrading-eleventy-v1%2F/)Upgrading to Eleventy 1.0.1](https://www.markllobrera.com/posts/upgrading-eleventy-v1/) — _Mark Llobrera (2024)_
*   [![Image 66: Favicon for v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fthomasrigby.com%2Fposts%2Ffixing-a-typo-shaved-4-minutes-off-my-netlify-build-time%2F](https://v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fthomasrigby.com%2Fposts%2Ffixing-a-typo-shaved-4-minutes-off-my-netlify-build-time%2F/)Fixing a typo shaved 4 minutes off my Netlify build time](https://thomasrigby.com/posts/fixing-a-typo-shaved-4-minutes-off-my-netlify-build-time/) — _Thomas Rigby (2024)_
*   [![Image 67: Favicon for v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fvelvetcache.org%2F2024%2F03%2F19%2Fgenerating-open-graph-preview-images-for-11ty%2F](https://v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fvelvetcache.org%2F2024%2F03%2F19%2Fgenerating-open-graph-preview-images-for-11ty%2F/)Generating Open Graph preview images for 11ty](https://velvetcache.org/2024/03/19/generating-open-graph-preview-images-for-11ty/) — _John Hobbs (2024)_
*   [![Image 68: Favicon for v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fwww.martingunnarsson.com%2Fposts%2Feleventy-automatic-image-pre-processing-part-2%2F](https://v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fwww.martingunnarsson.com%2Fposts%2Feleventy-automatic-image-pre-processing-part-2%2F/)Automatic image pre-processing in Eleventy, Part 2](https://www.martingunnarsson.com/posts/eleventy-automatic-image-pre-processing-part-2/) — _Martin Gunnarsson (2024)_
*   [![Image 69: Favicon for v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fchrismcleod.dev%2Fblog%2Fi-have-a-problem-with-build-times%2F](https://v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fchrismcleod.dev%2Fblog%2Fi-have-a-problem-with-build-times%2F/)I have a Problem with Build Times](https://chrismcleod.dev/blog/i-have-a-problem-with-build-times/) — _Chris McLeod (2024)_
*   [![Image 70: Favicon for v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fsimpixelated.com%2Fadding-inline-svgs-to-eleventy-js%2F](https://v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fsimpixelated.com%2Fadding-inline-svgs-to-eleventy-js%2F/)Adding inline SVGs to Eleventy.js](https://simpixelated.com/adding-inline-svgs-to-eleventy-js/) — _Jordan Kohl (2024)_
*   [![Image 71: Favicon for v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fwww.roboleary.net%2F2024%2F02%2F15%2Feleventy-favicon-modes.html](https://v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fwww.roboleary.net%2F2024%2F02%2F15%2Feleventy-favicon-modes.html/)Eleventy - Differentiate between dev and production builds with unique favicons](https://www.roboleary.net/2024/02/15/eleventy-favicon-modes.html) — _Rob O'Leary (2024)_
*   [![Image 72: Favicon for v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fwww.coryd.dev%2Fposts%2F2024%2Fsetting-up-image-transforms-in-eleventy%2F](https://v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fwww.coryd.dev%2Fposts%2F2024%2Fsetting-up-image-transforms-in-eleventy%2F/)Setting up image transforms in Eleventy](https://www.coryd.dev/posts/2024/setting-up-image-transforms-in-eleventy/) — _Cory Dransfeldt (2024)_
*   [![Image 73: Favicon for v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fchris.bur.gs%2Feleventy-immich%2F](https://v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fchris.bur.gs%2Feleventy-immich%2F/)Eleventy 🤝 Immich](https://chris.bur.gs/eleventy-immich/) — _Chris Burgess (2024)_
*   [![Image 74: Favicon for v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fwww.coryd.dev%2Fposts%2F2024%2Fcheck-if-images-are-available-before-optimizing-in-eleventy%2F](https://v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fwww.coryd.dev%2Fposts%2F2024%2Fcheck-if-images-are-available-before-optimizing-in-eleventy%2F/)Check if images are available before optimizing in Eleventy](https://www.coryd.dev/posts/2024/check-if-images-are-available-before-optimizing-in-eleventy/) — _Cory Dransfeldt (2024)_
*   [![Image 75: Favicon for v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fwww.pupismyname.com%2Farticles%2F11ty-og-images%2F](https://v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fwww.pupismyname.com%2Farticles%2F11ty-og-images%2F/)Using 11ty to generate Open Graph images](https://www.pupismyname.com/articles/11ty-og-images/) — _John Brooks (2024)_
*   [![Image 76: Favicon for v1.indieweb-avatar.11ty.dev/https%3A%2F%2Feystein.no%2Fblog%2Fsuper-fast-responsive-image-loading-in-eleventy%2F](https://v1.indieweb-avatar.11ty.dev/https%3A%2F%2Feystein.no%2Fblog%2Fsuper-fast-responsive-image-loading-in-eleventy%2F/)Super fast responsive image loading in Eleventy](https://eystein.no/blog/super-fast-responsive-image-loading-in-eleventy/) — _Eystein Mack Alnaes (2024)_
*   [![Image 77: Favicon for v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fdarthmall.net%2Fweblog%2F2024%2F11ty-photo-gallery%2F](https://v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fdarthmall.net%2Fweblog%2F2024%2F11ty-photo-gallery%2F/)Eleventy Photo Gallery](https://darthmall.net/weblog/2024/11ty-photo-gallery/) — _Evan Sheehan (2024)_
*   [![Image 78: Favicon for v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fwww.martingunnarsson.com%2Fposts%2Feleventy-automatic-image-pre-processing%2F](https://v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fwww.martingunnarsson.com%2Fposts%2Feleventy-automatic-image-pre-processing%2F/)Automatic pre-processing of post images in Eleventy](https://www.martingunnarsson.com/posts/eleventy-automatic-image-pre-processing/) — _Martin Gunnarsson (2023)_
*   [![Image 79: Favicon for v1.indieweb-avatar.11ty.dev/https%3A%2F%2Frknight.me%2Fblog%2Fgenerating-and-caching-open-graph-images-with-eleventy%2F](https://v1.indieweb-avatar.11ty.dev/https%3A%2F%2Frknight.me%2Fblog%2Fgenerating-and-caching-open-graph-images-with-eleventy%2F/)Generating and Caching Open Graph Images with Eleventy](https://rknight.me/blog/generating-and-caching-open-graph-images-with-eleventy/) — _Robb Knight (2023)_
*   [![Image 80: Favicon for v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fsometimes.digital%2Fposts%2Fgenerating-images-eleventy%2F](https://v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fsometimes.digital%2Fposts%2Fgenerating-images-eleventy%2F/)Generating Open Graph Images in Eleventy](https://sometimes.digital/posts/generating-images-eleventy/) — _nonnullish (2023)_
*   [![Image 81: Favicon for v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fpublishing-project.rivendellweb.net%2Fmigrating-from-wordpress-to-eleventy-part-4%2F](https://v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fpublishing-project.rivendellweb.net%2Fmigrating-from-wordpress-to-eleventy-part-4%2F/)Migrating from WordPress to Eleventy (part 4)](https://publishing-project.rivendellweb.net/migrating-from-wordpress-to-eleventy-part-4/) — _Carlos Araya (2023)_
*   [![Image 82: Favicon for v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fsheetsj.com%2Fblog%2Fvscode-pasting-11ty-images%2F](https://v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fsheetsj.com%2Fblog%2Fvscode-pasting-11ty-images%2F/)VSCode Pasting 11ty Images](https://sheetsj.com/blog/vscode-pasting-11ty-images/) — _Jeff Sheets (2023)_
*   [![Image 83: Favicon for v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fwww.zachleat.com%2Fweb%2Fsvg-short-circuit%2F](https://v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fwww.zachleat.com%2Fweb%2Fsvg-short-circuit%2F/)A new technique for image optimization: SVG short circuiting](https://www.zachleat.com/web/svg-short-circuit/) — _Zach Leatherman (2023)_
*   [![Image 84: Favicon for v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fcloudcannon.com%2Fblog%2Fautomatically-optimize-your-images-with-eleventy-image-and-cloudcannon%2F](https://v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fcloudcannon.com%2Fblog%2Fautomatically-optimize-your-images-with-eleventy-image-and-cloudcannon%2F/)Automatically optimize your images with Eleventy Image and CloudCannon](https://cloudcannon.com/blog/automatically-optimize-your-images-with-eleventy-image-and-cloudcannon/) — _Zach Leatherman (2023)_
*   [![Image 85: Favicon for v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fdarekkay.com%2Fblog%2Fphotography-website%2F](https://v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fdarekkay.com%2Fblog%2Fphotography-website%2F/)Building a photography website](https://darekkay.com/blog/photography-website/) — _Darek Kay (2023)_
*   [![Image 86: Favicon for v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fgoodenough.us%2Fblog%2F2023-10-17-adding-social-preview-images-to-our-11ty-blog%2F](https://v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fgoodenough.us%2Fblog%2F2023-10-17-adding-social-preview-images-to-our-11ty-blog%2F/)Adding Social Preview Images To Our 11ty Blog](https://goodenough.us/blog/2023-10-17-adding-social-preview-images-to-our-11ty-blog/) — _Matthew Lettini (2023)_
*   [![Image 87: Favicon for v1.indieweb-avatar.11ty.dev/https%3A%2F%2Frkblog.dev%2Fposts%2Fprogramming-general%2Fmaking-fast-website-with-eleventy%2F](https://v1.indieweb-avatar.11ty.dev/https%3A%2F%2Frkblog.dev%2Fposts%2Fprogramming-general%2Fmaking-fast-website-with-eleventy%2F/)Making a lighthouse-fast website with a static site generator like 11ty](https://rkblog.dev/posts/programming-general/making-fast-website-with-eleventy/) — _Piotr Maliński (2023)_
*   [![Image 88: Favicon for v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fgetkirby.com%2Fdocs%2Fcookbook%2Fsetup%2Fheadless-kiosk-application](https://v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fgetkirby.com%2Fdocs%2Fcookbook%2Fsetup%2Fheadless-kiosk-application/)Headless kiosk application (with Kirby CMS)](https://getkirby.com/docs/cookbook/setup/headless-kiosk-application) — _James Steel (2023)_
*   [![Image 89: Favicon for v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fjohnwargo.com%2Fposts%2F2023%2Feleventy-category-images%2F](https://v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fjohnwargo.com%2Fposts%2F2023%2Feleventy-category-images%2F/)Eleventy Category Images](https://johnwargo.com/posts/2023/eleventy-category-images/) — _John M. Wargo (2023)_
*   [![Image 90: Favicon for v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fequk.co.uk%2F2023%2F07%2F14%2Ffavicon-generation-in-eleventy%2F](https://v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fequk.co.uk%2F2023%2F07%2F14%2Ffavicon-generation-in-eleventy%2F/)Favicon Generation In Eleventy](https://equk.co.uk/2023/07/14/favicon-generation-in-eleventy/) — _equilibriumuk (2023)_
*   [![Image 91: Favicon for v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fequk.co.uk%2F2023%2F06%2F24%2Fmarkdown-image-optimization-in-eleventy%2F](https://v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fequk.co.uk%2F2023%2F06%2F24%2Fmarkdown-image-optimization-in-eleventy%2F/)Markdown Image Optimization In Eleventy](https://equk.co.uk/2023/06/24/markdown-image-optimization-in-eleventy/) — _equilibriumuk (2023)_
*   [![Image 92: Favicon for v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fequk.co.uk%2F2023%2F06%2F23%2Fimage-optimization-in-eleventy%2F](https://v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fequk.co.uk%2F2023%2F06%2F23%2Fimage-optimization-in-eleventy%2F/)Image Optimization In Eleventy](https://equk.co.uk/2023/06/23/image-optimization-in-eleventy/) — _equilibriumuk (2023)_
*   [![Image 93: Favicon for v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fflamedfury.com%2Fposts%2Fadding-game-cover-art-to-my-%2Fnow-page%2F](https://v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fflamedfury.com%2Fposts%2Fadding-game-cover-art-to-my-%2Fnow-page%2F/)Adding game cover art to my /now page](https://flamedfury.com/posts/adding-game-cover-art-to-my-/now-page/) — _fLaMEd (2023)_
*   [![Image 94: Favicon for v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fwww.simoncox.com%2Fshorts%2F2023-06-06-11ty-image-shortcode-best-practice%2F](https://v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fwww.simoncox.com%2Fshorts%2F2023-06-06-11ty-image-shortcode-best-practice%2F/)11ty image shortcode best practice](https://www.simoncox.com/shorts/2023-06-06-11ty-image-shortcode-best-practice/) — _Simon Cox (2023)_
*   [![Image 95: Favicon for v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fsteele.blue%2Fgatsby-opengraph-11ty-screenshots%2F](https://v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fsteele.blue%2Fgatsby-opengraph-11ty-screenshots%2F/)Generating Custom OpenGraph Cards with Gatsby and the 11ty Screenshot Service](https://steele.blue/gatsby-opengraph-11ty-screenshots/) — _Matt Steele (2023)_
*   [![Image 96: Favicon for v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fshivjm.blog%2Fcolophon%2Ffarewell-netlify-large-media-welcome-eleventy-img%2F](https://v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fshivjm.blog%2Fcolophon%2Ffarewell-netlify-large-media-welcome-eleventy-img%2F/)Farewell Netlify Large Media, Welcome eleventy-img](https://shivjm.blog/colophon/farewell-netlify-large-media-welcome-eleventy-img/) — _Shiv J.M. (2023)_
*   [![Image 97: Favicon for v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fwww.mikestreety.co.uk%2Fblog%2Ftake-your-11ty-build-from-1-second-to-2-minutes-by-generating-og-images%2F](https://v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fwww.mikestreety.co.uk%2Fblog%2Ftake-your-11ty-build-from-1-second-to-2-minutes-by-generating-og-images%2F/)Take your 11ty build from 1 second to 2 minutes by generating OG images](https://www.mikestreety.co.uk/blog/take-your-11ty-build-from-1-second-to-2-minutes-by-generating-og-images/) — _Mike Street (2023)_
*   [![Image 98: Favicon for v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fwww.markllobrera.com%2Fposts%2Feleventy-building-image-gallery-photoswipe%2F](https://v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fwww.markllobrera.com%2Fposts%2Feleventy-building-image-gallery-photoswipe%2F/)Eleventy: Building an Image Gallery with CSS Grid and PhotoSwipe](https://www.markllobrera.com/posts/eleventy-building-image-gallery-photoswipe/) — _Mark Llobrera (2023)_
*   [![Image 99: Favicon for v1.indieweb-avatar.11ty.dev/https%3A%2F%2Filltron.net%2F2023%2F01%2Fhello-2023%2F](https://v1.indieweb-avatar.11ty.dev/https%3A%2F%2Filltron.net%2F2023%2F01%2Fhello-2023%2F/)Hello 2023](https://illtron.net/2023/01/hello-2023/) — _Chris Coleman (2023)_
*   [![Image 100: Favicon for v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fwww.bash.lk%2Fposts%2Ftech%2F1-elventy-image-gallery%2F](https://v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fwww.bash.lk%2Fposts%2Ftech%2F1-elventy-image-gallery%2F/)Creating image galleries in eleventy(11ty) with elventy-img](https://www.bash.lk/posts/tech/1-elventy-image-gallery/) — _Prabashwara Seneviratne (2022)_
*   [![Image 101: Favicon for v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fwww.raymondcamden.com%2F2022%2F10%2F20%2Fintegrating-cloudinary-into-eleventy](https://v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fwww.raymondcamden.com%2F2022%2F10%2F20%2Fintegrating-cloudinary-into-eleventy/)Integrating Cloudinary into Eleventy](https://www.raymondcamden.com/2022/10/20/integrating-cloudinary-into-eleventy) — _Raymond Camden (2022)_
*   [![Image 102: Favicon for v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fchriskirknielsen.com%2Fblog%2Fmanage-your-svg-files-with-eleventys-render-plugin%2F](https://v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fchriskirknielsen.com%2Fblog%2Fmanage-your-svg-files-with-eleventys-render-plugin%2F/)Manage your SVG files with Eleventy's render plugin](https://chriskirknielsen.com/blog/manage-your-svg-files-with-eleventys-render-plugin/) — _Christopher Kirk-Nielsen (2022)_
*   [![Image 103: Favicon for v1.indieweb-avatar.11ty.dev/https%3A%2F%2Ftjaddison.com%2Fblog%2F2022%2F08%2Fprocessing-images-linked-from-frontmatter-with-eleventy-img-to-use-in-meta-tags%2F](https://v1.indieweb-avatar.11ty.dev/https%3A%2F%2Ftjaddison.com%2Fblog%2F2022%2F08%2Fprocessing-images-linked-from-frontmatter-with-eleventy-img-to-use-in-meta-tags%2F/)Processing images linked from frontmatter with eleventy-img to use in meta tags](https://tjaddison.com/blog/2022/08/processing-images-linked-from-frontmatter-with-eleventy-img-to-use-in-meta-tags/) — _TJ Addison (2022)_
*   [![Image 104: Favicon for v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fwww.raymondcamden.com%2F2022%2F07%2F01%2Freading-comic-books-in-the-jamstack](https://v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fwww.raymondcamden.com%2F2022%2F07%2F01%2Freading-comic-books-in-the-jamstack/)Reading Comic Books in the Jamstack](https://www.raymondcamden.com/2022/07/01/reading-comic-books-in-the-jamstack) — _Raymond Camden (2022)_
*   [![Image 105: Favicon for v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fwww.aleksandrhovhannisyan.com%2Fblog%2Feleventy-image-plugin%2F](https://v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fwww.aleksandrhovhannisyan.com%2Fblog%2Feleventy-image-plugin%2F/)Optimizing Images with the 11ty Image Plugin](https://www.aleksandrhovhannisyan.com/blog/eleventy-image-plugin/) — _Aleksandr Hovhannisyan (2022)_
*   [![Image 106: Favicon for v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fgfscott.com%2Fblog%2Feleventy-img-without-central-image-directory%2F](https://v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fgfscott.com%2Fblog%2Feleventy-img-without-central-image-directory%2F/)Using the Eleventy Image plugin without a central image folder](https://gfscott.com/blog/eleventy-img-without-central-image-directory/) — _Graham F. Scott (2022)_
*   [![Image 107: Favicon for v1.indieweb-avatar.11ty.dev/https%3A%2F%2Ftomichen.com%2Fblog%2Fposts%2F20220416-responsive-images-in-markdown-with-eleventy-image%2F](https://v1.indieweb-avatar.11ty.dev/https%3A%2F%2Ftomichen.com%2Fblog%2Fposts%2F20220416-responsive-images-in-markdown-with-eleventy-image%2F/)Responsive Images in Markdown with Eleventy Image](https://tomichen.com/blog/posts/20220416-responsive-images-in-markdown-with-eleventy-image/) — _Tomi Chen (2022)_
*   [![Image 108: Favicon for v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fflorian.ec%2Fblog%2Feleventy-apple-touch-icons%2F](https://v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fflorian.ec%2Fblog%2Feleventy-apple-touch-icons%2F/)Generating Apple Touch Icons with Eleventy](https://florian.ec/blog/eleventy-apple-touch-icons/) — _Florian Eckerstorfer (2022)_
*   [![Image 109: Favicon for v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fwww.marclittlemore.com%2Feasily-create-gravatar-images-with-eleventy%2F](https://v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fwww.marclittlemore.com%2Feasily-create-gravatar-images-with-eleventy%2F/)Easily Create Gravatar Images With Eleventy](https://www.marclittlemore.com/easily-create-gravatar-images-with-eleventy/) — _Marc Littlemore (2022)_
*   [![Image 110: Favicon for v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fmichaelharley.net%2Fposts%2F2022%2F01%2F29%2Fmy-complete-blogging-workflow%2F](https://v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fmichaelharley.net%2Fposts%2F2022%2F01%2F29%2Fmy-complete-blogging-workflow%2F/)My complete blogging workflow](https://michaelharley.net/posts/2022/01/29/my-complete-blogging-workflow/) — _Michael Harley (2022)_
*   [![Image 111: Favicon for v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fwww.raymondcamden.com%2F2022%2F01%2F28%2Fusing-a-google-photos-album-in-your-eleventy-site-with-pipedream](https://v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fwww.raymondcamden.com%2F2022%2F01%2F28%2Fusing-a-google-photos-album-in-your-eleventy-site-with-pipedream/)Using a Google Photos Album in your Eleventy Site with Pipedream](https://www.raymondcamden.com/2022/01/28/using-a-google-photos-album-in-your-eleventy-site-with-pipedream) — _Raymond Camden (2022)_
*   [![Image 112: Favicon for v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fwww.brycewray.com%2Fposts%2F2022%2F01%2Ffetching-remote-images-eleventy%2F](https://v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fwww.brycewray.com%2Fposts%2F2022%2F01%2Ffetching-remote-images-eleventy%2F/)Fetching remote images with Eleventy](https://www.brycewray.com/posts/2022/01/fetching-remote-images-eleventy/) — _Bryce Wray (2022)_
*   [![Image 113: Favicon for v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fshivjm.blog%2Fcolophon%2Fautomatically-generated-social-media-images-with-html-css-eleventy-and-puppeteer%2F](https://v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fshivjm.blog%2Fcolophon%2Fautomatically-generated-social-media-images-with-html-css-eleventy-and-puppeteer%2F/)Automatically Generated Social Media Images with HTML, CSS, Eleventy & Puppeteer](https://shivjm.blog/colophon/automatically-generated-social-media-images-with-html-css-eleventy-and-puppeteer/) — _Shiv J.M. (2021)_
*   [![Image 114: Favicon for v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fwww.alpower.com%2Ftutorials%2Fadding-figures-with-captions-to-images-in-markdown-with-eleventy](https://v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fwww.alpower.com%2Ftutorials%2Fadding-figures-with-captions-to-images-in-markdown-with-eleventy/)Adding figures with captions to images in markdown with eleventy](https://www.alpower.com/tutorials/adding-figures-with-captions-to-images-in-markdown-with-eleventy) — _Al Power (2021)_
*   [![Image 115: Favicon for v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fmichaelharley.net%2Fposts%2F2021%2F07%2F19%2Fsetting-a-conditional-variable-in-javascript%2F](https://v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fmichaelharley.net%2Fposts%2F2021%2F07%2F19%2Fsetting-a-conditional-variable-in-javascript%2F/)Setting a conditional variable in Javascript](https://michaelharley.net/posts/2021/07/19/setting-a-conditional-variable-in-javascript/) — _Michael Harley (2021)_
*   [![Image 116: Favicon for v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fmichaelharley.net%2Fposts%2F2021%2F07%2F14%2Fimproving-my-automated-open-graph-image-process-w-eleventy%2F](https://v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fmichaelharley.net%2Fposts%2F2021%2F07%2F14%2Fimproving-my-automated-open-graph-image-process-w-eleventy%2F/)Improving my automated open graph image process w/ Eleventy](https://michaelharley.net/posts/2021/07/14/improving-my-automated-open-graph-image-process-w-eleventy/) — _Michael Harley (2021)_
*   [![Image 117: Favicon for v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fmichaelharley.net%2Fposts%2F2021%2F07%2F13%2Fimproving-upon-my-image-processing-with-eleventy%2F](https://v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fmichaelharley.net%2Fposts%2F2021%2F07%2F13%2Fimproving-upon-my-image-processing-with-eleventy%2F/)Improving upon my image processing with Eleventy](https://michaelharley.net/posts/2021/07/13/improving-upon-my-image-processing-with-eleventy/) — _Michael Harley (2021)_
*   [![Image 118: Favicon for v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fbnijenhuis.nl%2Fnotes%2Fautomatically-generate-open-graph-images-in-eleventy%2F](https://v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fbnijenhuis.nl%2Fnotes%2Fautomatically-generate-open-graph-images-in-eleventy%2F/)Automatically generate open graph images in Eleventy](https://bnijenhuis.nl/notes/automatically-generate-open-graph-images-in-eleventy/) — _Bernard Nijenhuis (2021)_
*   [![Image 119: Favicon for v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fmartinschneider.me%2Farticles%2Feleventy-1-0%2F](https://v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fmartinschneider.me%2Farticles%2Feleventy-1-0%2F/)Eleventy 1.0](https://martinschneider.me/articles/eleventy-1-0/) — _Martin Schneider (2021)_
*   [![Image 120: Favicon for v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fwww.brycewray.com%2Fposts%2F2021%2F04%2Fusing-eleventys-official-image-plugin%2F](https://v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fwww.brycewray.com%2Fposts%2F2021%2F04%2Fusing-eleventys-official-image-plugin%2F/)Using Eleventy’s official image plugin](https://www.brycewray.com/posts/2021/04/using-eleventys-official-image-plugin/) — _Bryce Wray (2021)_
*   [![Image 121: Favicon for v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fwww.raymondcamden.com%2F2021%2F04%2F07%2Fbuilding-a-simple-image-gallery-with-eleventy](https://v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fwww.raymondcamden.com%2F2021%2F04%2F07%2Fbuilding-a-simple-image-gallery-with-eleventy/)Building a Simple Image Gallery with Eleventy](https://www.raymondcamden.com/2021/04/07/building-a-simple-image-gallery-with-eleventy) — _Raymond Camden (2021)_
*   [![Image 122: Favicon for v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fmartinschneider.me%2Farticles%2Fusing-the-eleventy-image-plugin-to-generate-images%2F](https://v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fmartinschneider.me%2Farticles%2Fusing-the-eleventy-image-plugin-to-generate-images%2F/)Using the Eleventy image plugin to generate images](https://martinschneider.me/articles/using-the-eleventy-image-plugin-to-generate-images/) — _Martin Schneider (2021)_
*   [![Image 123: Favicon for v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fwww.zachleat.com%2Fweb%2Feleventy-image%2F](https://v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fwww.zachleat.com%2Fweb%2Feleventy-image%2F/)Don't shut down your business! Instead use Eleventy Image](https://www.zachleat.com/web/eleventy-image/) — _Zach Leatherman (2021)_
*   [![Image 124: Favicon for v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fwww.raresportan.com%2Feleventy-part-four%2F](https://v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fwww.raresportan.com%2Feleventy-part-four%2F/)Let's Learn Eleventy (11ty) - Images](https://www.raresportan.com/eleventy-part-four/) — _Rares Portan (2021)_
*   [![Image 125: Favicon for v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fwww.ovl.design%2Ftext%2Fan-async-function-walks-into-a-loop%2F](https://v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fwww.ovl.design%2Ftext%2Fan-async-function-walks-into-a-loop%2F/)An async function walks into a loop.](https://www.ovl.design/text/an-async-function-walks-into-a-loop/) — _Oscar (2021)_
*   [![Image 126: Favicon for v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fmtm.dev%2Feleventy-social-sharing-images.html](https://v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fmtm.dev%2Feleventy-social-sharing-images.html/)Automatic social sharing images for Eleventy](https://mtm.dev/eleventy-social-sharing-images.html) — _Mark Thomas Miller (2021)_
*   [![Image 127: Favicon for v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fmichaelharley.net%2Fposts%2F2021%2F01%2F09%2Fautomated-social-sharing-images-with-eleventy-and-puppeteer%2F](https://v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fmichaelharley.net%2Fposts%2F2021%2F01%2F09%2Fautomated-social-sharing-images-with-eleventy-and-puppeteer%2F/)Automated social sharing images with Eleventy and Puppeteer](https://michaelharley.net/posts/2021/01/09/automated-social-sharing-images-with-eleventy-and-puppeteer/) — _Michael Harley (2021)_
*   [![Image 128: Favicon for v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fmichaelharley.net%2Fposts%2F2021%2F01%2F03%2Fsetup-social-sharing-previews-seo-and-favicons-on-eleventy%2F](https://v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fmichaelharley.net%2Fposts%2F2021%2F01%2F03%2Fsetup-social-sharing-previews-seo-and-favicons-on-eleventy%2F/)Setup social sharing previews, SEO, and favicons on Eleventy](https://michaelharley.net/posts/2021/01/03/setup-social-sharing-previews-seo-and-favicons-on-eleventy/) — _Michael Harley (2021)_
*   [![Image 129: Favicon for v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fwww.industrialempathy.com%2Fposts%2Fimage-optimizations%2F](https://v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fwww.industrialempathy.com%2Fposts%2Fimage-optimizations%2F/)Maximally optimizing image loading for the web](https://www.industrialempathy.com/posts/image-optimizations/) — _Malte Ubl (2020)_
*   [![Image 130: Favicon for v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fmichaelharley.net%2Fposts%2F2020%2F12%2F21%2Fconfiguring-responsive-and-optimized-images-with-eleventy%2F](https://v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fmichaelharley.net%2Fposts%2F2020%2F12%2F21%2Fconfiguring-responsive-and-optimized-images-with-eleventy%2F/)Configuring responsive and optimized images with Eleventy](https://michaelharley.net/posts/2020/12/21/configuring-responsive-and-optimized-images-with-eleventy/) — _Michael Harley (2020)_
*   [![Image 131: Favicon for v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fsia.codes%2Fposts%2Feleventy-and-cloudinary-images%2F](https://v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fsia.codes%2Fposts%2Feleventy-and-cloudinary-images%2F/)Optimize Images in Eleventy Using Cloudinary](https://sia.codes/posts/eleventy-and-cloudinary-images/) — _Sia Karamalegos (2020)_
*   [![Image 132: Favicon for v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fwww.stevenhicks.me%2Fblog%2F2020%2F12%2Fgenerating-social-sharing-images-in-eleventy%2F](https://v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fwww.stevenhicks.me%2Fblog%2F2020%2F12%2Fgenerating-social-sharing-images-in-eleventy%2F/)Generating Social Sharing Images In Eleventy](https://www.stevenhicks.me/blog/2020/12/generating-social-sharing-images-in-eleventy/) — _Steven Hicks (2020)_
*   [![Image 133: Favicon for v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fryanccn.dev%2Fposts%2Frespimg-11ty-sharp%2F](https://v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fryanccn.dev%2Fposts%2Frespimg-11ty-sharp%2F/)Responsive Images with Eleventy & Sharp](https://ryanccn.dev/posts/respimg-11ty-sharp/) — _Ryan Cao (2020)_
*   [![Image 134: Favicon for v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fflorian.ec%2Fblog%2Feleventy-and-responsive-images%2F](https://v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fflorian.ec%2Fblog%2Feleventy-and-responsive-images%2F/)Eleventy and Responsive Images](https://florian.ec/blog/eleventy-and-responsive-images/) — _Florian Eckerstorfer (2020)_
*   [![Image 135: Favicon for v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fwww.juanfernandes.uk%2Fblog%2Fautomated-open-graph-images-with-11ty-and-cloudinary%2F](https://v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fwww.juanfernandes.uk%2Fblog%2Fautomated-open-graph-images-with-11ty-and-cloudinary%2F/)Automated Open Graph images with 11ty and Cloudinary](https://www.juanfernandes.uk/blog/automated-open-graph-images-with-11ty-and-cloudinary/) — _Juan Fernandes (2020)_
*   [![Image 136: Favicon for v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fcss-tricks.com%2Ftips-for-rolling-your-own-lazy-loading%2F](https://v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fcss-tricks.com%2Ftips-for-rolling-your-own-lazy-loading%2F/)Tips for rolling your own lazy loading](https://css-tricks.com/tips-for-rolling-your-own-lazy-loading/) — _Phil Hawksworth (2019)_
*   [![Image 137: Favicon for v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fwww.webstoemp.com%2Fblog%2Fmultilingual-sites-eleventy%2F](https://v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fwww.webstoemp.com%2Fblog%2Fmultilingual-sites-eleventy%2F/)Multilingual sites with Eleventy](https://www.webstoemp.com/blog/multilingual-sites-eleventy/) — _Jérôme Coupé (2019)_

* * *

### Other pages in _Plugins_

*   [Create or use Plugins](https://www.11ty.dev/docs/create-plugin/)
*   [Image](https://www.11ty.dev/docs/plugins/image/)
*   [Fetch](https://www.11ty.dev/docs/plugins/fetch/)
*   [`<is-land>`](https://www.11ty.dev/docs/plugins/is-land/)
*   [Render](https://www.11ty.dev/docs/plugins/render/)
*   [Internationalization (i18n)](https://www.11ty.dev/docs/plugins/i18n/)
*   [RSS](https://www.11ty.dev/docs/plugins/rss/)
*   [Upgrade Helper](https://www.11ty.dev/docs/plugins/upgrade-help/)
*   [Syntax Highlighting](https://www.11ty.dev/docs/plugins/syntaxhighlight/)
*   [InputPath to URL](https://www.11ty.dev/docs/plugins/inputpath-to-url/)
*   [Navigation](https://www.11ty.dev/docs/plugins/navigation/)
*   [HTML `<base>`](https://www.11ty.dev/docs/plugins/html-base/)
*   [Bundle](https://www.11ty.dev/docs/plugins/bundle/)
*   [Id Attribute](https://www.11ty.dev/docs/plugins/id-attribute/)
*   [Community Plugins](https://www.11ty.dev/docs/plugins/community/)
*   [Retired Plugins](https://www.11ty.dev/docs/plugins/retired/)
