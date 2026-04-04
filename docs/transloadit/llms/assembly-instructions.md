# Source: https://transloadit.com/docs/topics/assembly-instructions.md

# Assembly Instructions

To learn aboutAssembly Instructions let's look at this example:

![](/_next/static/media/copy.8f7d2926.svg?dpl=dpl_GAEaNRfbaNgVy6q3c3ke5o1s9Xtk)

```json
{
  "steps": {
    ":original": {
      "robot": "/upload/handle"
    },
    "imported_watermark": {
      "robot": "/http/import",
      "url": "https://transloadit.com/assets/images/face.jpg"
    },
    "resized": {
      "robot": "/image/resize",
      "use": {
        "steps": [
          { "name": ":original", "as": "base" },
          { "name": "imported_watermark", "as": "watermark" }
        ]
      },
      "width": 400,
      "height": 400,
      "watermark_position": "center",
      "watermark_size": "30%"
    },
    "exported": {
      "robot": "/s3/store",
      "use": [":original", "resized"],
      "credentials": "my_cloud_storage_credentials",
      "path": "/my_images/${file.id}/${file.url_name}"
    }
  }
}

```

The example shows four Steps: `:original`,`imported_watermark`, `resized` and `exported`. You can name yourSteps anything you like with the exception of`:original`, which refers to uploaded files and must use the[🤖/upload/handle](/docs/robots/upload-handle.md) robot.

Notice how both the `:original` and `imported_watermark` Steps are used as an input to the `resized` Step via the `use` parameter. We useStep bundling here via the "as" syntax to pass multiple files to the `resized` Step at the same time - one "as" the base image and one "as" the watermark to be printed on top of the base image. Different robots provide different possibilities for the "as" syntax, which makes things very powerful!

The `exported` step then just uses most of the otherSteps as input and stores them on S3 - one by one, withoutStep bundling. The used Variables `${file.id}` and `${file.url_name}` are available to all Steps and can be used to create unique filenames for each file.

This way we will be able to handle uploaded files, watermark them and have both the uploaded image and the resized and watermarked redition exported to S3.

Not all Steps require inputs. Our `imported_watermark` Step for instance provides the first input by downloading it, so that's where we'll omit `use`. Other examples ofRobots that don't require input files are[🤖/html/convert](/docs/robots/html-convert.md), which can take a screenshot from a website and create the first file that way, or the[🤖/upload/handle](/docs/robots/upload-handle.md), which takes its files from your app's visitors, instead of from another Step.

With one simple change we could make this app truly dynamic. Imagine replacing the static url in the`imported_watermark` Step with a dynamic one from a field in your app. All we need to do is change the `"url"` parameter to `"${fields.watermark_url}"`in our Template and then supply this input field in our HTML web form (or via an additional POST field in our request) to make the watermarking truly dynamic!

## Step parameters

As you can see, each Step is defined as an object with a handful of properties, or parameters. Most of them are in factRobot Parameters as they instruct, for instance, the`width` of an image after a resize. Those are all covered in the respective[Robot docs](/docs/robots.md). There are, however, also 4 parameters that instruct theAssembly engine itself, defining whichRobots are invoked and how they are interconnected:

* ### `use`

`string | Array<string> | Array<object> | object`\
Specifies which Step(s) to use as input.

* You can pick any names for Steps except `":original"` (reserved for user uploads handled by Transloadit)
* You can provide several Steps as input with arrays:\
  ![](/_next/static/media/copy.8f7d2926.svg?dpl=dpl_GAEaNRfbaNgVy6q3c3ke5o1s9Xtk)

```json
{  
  "use": [  
    ":original",  
    "encoded",  
    "resized"  
  ]  
}  
```

###### Tip

That's likely all you need to know about `use`, but you can view [Advanced use cases](/docs/topics/use-parameter.md).

* ### `robot`

`boolean` (default: `false`)\
Specifies which Robot should process files passed to this Step.\
There are [79 Robots](/docs/robots.md), each with their own parameters, such as `width` to control how an image is resized. The full list of parameters per Robot can be taken from the Robot docs.

* ### `result`

`boolean` (default: `false`)\
Whether the results of this Step should be present in the Assembly Status JSON

* ### `force_accept`

`boolean` (default: `false`)\
Force a Robot to accept a file type it would have ignored.\
By default, Robots ignore files they are not familiar with.[🤖/video/encode](/docs/robots/video-encode.md), for example, will happily ignore input images.\
With the `force_accept` parameter set to `true`, you can force Robots to accept all files thrown at them. This will typically lead to errors and should only be used for debugging or combatting edge cases.

## Order of execution

In order to speed up Assemblies,Steps will be executed as soon as their inputSteps emit files. In other words, many things are processed in parallel. For example, let's say you want to encode an uploaded video and would also like to extract thumbnails from it:

![](/_next/static/media/copy.8f7d2926.svg?dpl=dpl_GAEaNRfbaNgVy6q3c3ke5o1s9Xtk)

```json
{
  "steps": {
    ":original": {
      "robot": "/upload/handle"
    },
    "encoded": {
      "use": ":original",
      "robot": "/video/encode",
      "preset": "web/mp4/1080p"
    },
    "thumbed": {
      "use": ":original",
      "robot": "/video/thumbs",
      "count": 4
    },
    "exported": {
      "use": ["encoded", "thumbed"],
      "robot": "/s3/store",
      "credentials": "YOUR_S3_CREDENTIALS"
    }
  }
}

```

Both the `encoded` and the `thumbed` Steps will be executed in parallel as soon as the first file upload is complete. The `exported` Step is fired for each of the files coming from`encoded` and `thumbed`. It is likely that the thumbnails will hit your S3 bucket before the video that was optimized for iPad, even though thumbnails were defined later. So, the order ofSteps does not really matter. The `use` parameter defines the input for each Step and this ultimately dictates how our Steps are chained.

## Filtering to make Steps conditional

Using [🤖/file/filter](/docs/robots/file-filter.md), you can executeSteps based on a file's properties. This allows you to create Assembly Instructions that: cater to both video and audio uploads, reject files that are too small, only apply an effect on images that have transparent areas, etc. These and more things are also covered in theRobot's docs.

## Assembly Variables

For information about Assembly Variables like `${file.id}`, `${assembly.id}`, `${fields.*}`, and more, see the dedicated [Assembly Variables](/docs/topics/assembly-variables.md) page.
