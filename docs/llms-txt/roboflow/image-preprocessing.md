# Source: https://docs.roboflow.com/roboflow/roboflow-ko/datasets/dataset-versions/image-preprocessing.md

# Source: https://docs.roboflow.com/roboflow/roboflow-jp/datasets/dataset-versions/image-preprocessing.md

# Source: https://docs.roboflow.com/roboflow/roboflow-hi/datasets/dataset-versions/image-preprocessing.md

# Source: https://docs.roboflow.com/datasets/dataset-versions/image-preprocessing.md

# Preprocess Images

Preprocessing ensures your dataset is in a standard format (e.g. all images are the same size). This step is essential to ensure your dataset is consistent before training a model.

Preprocessing applies to all images in your Train, Valid, and Test set (unlike [Augmentations](https://docs.roboflow.com/datasets/dataset-versions/image-augmentation), which only apply to the Train set).

The Roboflow platform offers the following preprocessing options:

* Auto-Orient
* Resize
* Grayscale
* Auto-Adjust Contrast
* Isolate Objects
* Static Crop
* Tile
* Modify Classes
* Filter Null
* Filter by Tag

Each option is described below.

### Auto-Orient

Auto-orient strips your images of their EXIF data so that you see images displayed the same way they are stored on disk.

EXIF data determines the orientation of a given image. Applications (like Preview on Mac) use this data to display an image in a specific orientation, even if the orientation of how it is stored on disk differs. See [**this**](https://news.ycombinator.com/item?id=21207411) front page Hacker News discussion on how this may silently ruin your object detection models.

* Roboflow recommends defaulting to leaving this on and checking how your images in inference are being fed to your model.
* If you want to learn more about whether or not you should auto-orient your images, [check out our blog](https://blog.roboflow.com/exif-auto-orientation/).

### Resize

Resize changes your images size and, optionally, scale to a desired set of dimensions. Annotations are adjusted proportionally (except in the case of “fill” below).

Currently, we only support downsizing. We provide some guidance for [what resize option may be best for your use case](https://blog.roboflow.com/you-might-be-resizing-your-images-incorrectly/).

* **Stretch to:** Stretch your images to a preferred pixel-by-pixel dimension. Annotations are scaled proportionally. Images are square, distorted, but no source image data is lost.
* **Fill (with center crop) in:** The generated image is a centered crop of your desired output dimensions. For example, if the source image is 2600x2080 and the resize option is set to 640x640, the outputted resize is the central 640x640 of the source image. The aspect ratio is maintained, but source image data is lost.
* **Fit within:** The dimensions of the source dimension are scaled to be the dimensions of the output image while maintaining the source image aspect ratio. For example, if a source image is 2600x2080 and the resize option is set to 640x640, the longer dimensions (2600) is scaled to 640 and the secondary dimension (2080) is scaled to \~512 pixels. Image aspect ratios and original data are maintained, but they are not square.
* **Fit (reflect edges) in:** The dimensions of the source dimension are scaled to be the dimensions of the output image while maintaining the source image aspect ratio, and any newly created padding is a reflection of the source image. For example, if a source image is 2600x2080 and the resize option is set to 416x416, the longer dimensions (2600) is scaled to 416 and the secondary dimension (2080) is scaled to \~335.48 pixels. The remaining pixel area (416-335.48, or 80.52 pixels) are reflected pixels of the source image. Notably, Roboflow also reflects annotations by default. Images are square, padded, and aspect ratios plus original data are maintained.
* **Fit (black edges) in:** The dimensions of the source dimension are scaled to be the dimensions of the output image while maintaining the source image aspect ratio, and any newly created padding is black area. For example, if a source image is 2600x2080 and the resize option is set to 416x416, the longer dimensions (2600) is scaled to 416 and the secondary dimension (2080) is scaled to \~335.48 pixels. The remaining pixel area (416-335.48, or 80.52 pixels) are black pixels. Images are square, black padded, and aspect ratios plus original data are maintained.
* **Fit (white edges) in:** The dimensions of the source dimension are scaled to be the dimensions of the output image while maintaining the source image aspect ratio, and any newly created padding is white area. For example, if a source image is 2600x2080 and the resize option is set to 416x416, the longer dimensions (2600) is scaled to 416 and the secondary dimension (2080) is scaled to \~335.48 pixels. The remaining pixel area (416-335.48, or 80.52 pixels) are white pixels. Images are square, white padded, and aspect ratios plus original data are maintained.

### Grayscale

Converts an image with RGB channels into an image with a single grayscale channel, which can save you memory. The value of each grayscale pixel is calculated as the weighted sum of the corresponding red, green and blue pixels: Y = 0.2125 R + 0.7154 G + 0.0721 B.

These weights are used by [CRT phosphors](http://poynton.ca/PDFs/ColorFAQ.pdf) as they better represent human perception of red, green and blue than equal weights. (Via [Scikit-Image](https://scikit-image.org/docs/dev/auto_examples/color_exposure/plot_rgb_to_gray.html).)

### Auto-Adjust Contrast

Enhances an image with low contrast. We've explored [whether you want to use contrast as a preprocessing step](https://blog.roboflow.com/when-to-use-contrast-as-a-preprocessing-step/).

* **Contrast Stretching**: the image is rescaled to include all intensities that fall within the 2nd and 98th percentiles. [See more](http://homepages.inf.ed.ac.uk/rbf/HIPR2/stretch.htm).
* **Histogram Equalization**: “spreads out the most frequent intensity values” in an image. The equalized image has a roughly uniform distribution, where all colors of pixels are approximately equally represented. [See more](https://en.wikipedia.org/wiki/Histogram_equalization).
* **Adaptive Equalization**: Contrast Limited Adaptive Histogram Equalization (CLAHE). An algorithm for local contrast enhancement, that uses histograms computed over different tile regions of the image. Local details can therefore be enhanced even in regions that are darker or lighter than most of the image. (Via [Scikit-Image](https://scikit-image.org/docs/dev/api/skimage.exposure.html#skimage.exposure.equalize_adapthist).)

## Advanced Preprocessing Features

### Isolate Objects

The Isolate Objects transform will crop and extract each bounding box into an individual image. This step converts Object Detection datasets into Classification datasets.

In cases where many classes in a dataset are similar, it is common to use two models in sequence. The first model (object detection) finds the object and the second model (classification) identifies what the object is. The Isolate Objects transformation is useful for creating the dataset necessary for training the second model.

### Static Crop

![The static crop feature, and an example output.](https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-4f30e8b0a744bea04bcf0dadd480f55d4cb9a034%2FScreenshot%202025-05-20%20at%2009.44.47.png?alt=media)

### Tile

Tiling can help when detecting small objects (especially in situations like aerial imagery and microscopy. The default setting is 2x2 tiling, however, you can adjust this as you see fit. Tiling is performed *before* resizing in the preprocessing pipeline.

![The tiling tool and a preview (depicted in "grid") of the output .](https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-7a09d308f703e2805c36bee439ee95451f05ca8b%2FScreenshot%202025-05-20%20at%2009.45.19.png?alt=media)

### Modify Classes

A preprocessing tool used to omit specific classes or remap (rename) classes when generating a new version of your dataset. These changes only apply to the version you generate. No changes will be made to your underlying dataset.

![Omitting the "Apple leaf" class.](https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-37b01b8cc97b0d694bed8bf5d7a445fce3dbd8c9%2FScreenshot%202025-05-20%20at%2009.45.43.png?alt=media)

![Remapping the class "scratches" to "scratch".](https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-6c39656c789b92a25f4a7775bb027f33382c706c%2FScreenshot%202025-05-20%20at%2009.46.57.png?alt=media)

### Filter Null

The Filter Null transformation allows users to require a share of images in a dataset to be annotated. Images marked as null annotation, or "unannotated" after applying the Modify Classes tool, are the only ones affected when using Filter Null.

This transformation is useful in the case where a large share of a dataset does not contain the objects of interest.

![Applying the Filter Null preprocessing step.](https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-438a722d13a06de4d81a8508b0f1204e3e61fc30%2FScreenshot%202025-05-20%20at%2009.47.41.png?alt=media)

{% hint style="warning" %}
Be sure that you have properly annotated ALL images within your dataset, designated appropriate images as null annotation, and/or omitted any unnecessary classes prior to using this tool.
{% endhint %}

{% hint style="info" %}
[The Difference Between Missing and Null Annotations](https://blog.roboflow.com/missing-and-null-image-annotations/)

"Missing Annotations" occur when images are not annotated (leaving images unannotated will cause issues with the performance of your trained dataset, and can result in a failed training). Null annotations should only be applied when there is *nothing* present within that image that you wish for your model to detect.
{% endhint %}

### Filter by Tag

The Filter by Tag transformation allows users to filter which images should or should not be included in a version based on which [Tags](https://docs.roboflow.com/datasets/add-tags-to-images) are applied. This transformation is useful for training a model on a new subset of data or excluding unwanted images from training.

Three options are available for each Tag:

* **Require:** Only images with Required tags will be included in the version.
* **Exclude**: Images with Excluded tags will not be included in the version.
* **Allow:** Images with Allowed tags will be included in the version, conditional on Exclude and Require rules.

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-a4764e905f41d1e1b4e83aa437ce5ebdb7328219%2FScreenshot%202025-05-20%20at%2009.49.32.png?alt=media" alt=""><figcaption><p>In this example, the resulting Version will only contain images that do not have the <code>do-not-include</code> tag.</p></figcaption></figure>
