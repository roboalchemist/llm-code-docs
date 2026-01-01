### Post-Processing with TensorFlow Lite

#### Prerequisites

These stages require TensorFlow Lite (TFLite) libraries that export the {cpp} API. From Raspberry Pi OS *Trixie* onwards, Raspberry Pi builds and distributes a TFLite package, which can be installed with the following command:

```console
$ sudo apt install libtensorflow-lite-dev
```

After installing, you must xref:camera*software.adoc#build-libcamera-and-rpicam-apps[recompile `rpicam-apps` with TensorFlow Lite support].

#### `object*classify*tf` stage

Download: https://storage.googleapis.com/download.tensorflow.org/models/mobilenet*v1*2018*08*02/mobilenet*v1*1.0*224*quant.tgz[]

`object*classify*tf` uses a Google MobileNet v1 model to classify objects in the camera image. This stage requires a https://storage.googleapis.com/download.tensorflow.org/models/mobilenet*v1*1.0*224*frozen.tgz[`labels.txt` file].

You can configure this stage with the following parameters:

[cols="1,3"]
|===
| `top*n*results` | The number of results to show
| `refresh*rate` | The number of frames that must elapse between model runs
| `threshold*high` | Confidence threshold (between 0 and 1) where objects are considered as being present
| `threshold*low` | Confidence threshold which objects must drop below before being discarded as matches
| `model*file` | Filepath of the TFLite model file
| `labels*file` | Filepath of the file containing the object labels
| `display*labels` | Whether to display the object labels on the image; inserts `annotate.text` metadata for the `annotate*cv` stage to render
| `verbose` | Output more information to the console
|===

Example `object*classify*tf.json` file:

```json
{
    "object*classify*tf" : {
        "top*n*results" : 2,
        "refresh*rate" : 30,
        "threshold*high" : 0.6,
        "threshold*low" : 0.4,
        "model*file" : "/home/<username>/models/mobilenet*v1*1.0*224*quant.tflite",
        "labels*file" : "/home/<username>/models/labels.txt",
        "display*labels" : 1
    },
    "annotate*cv" : {
        "text" : "",
        "fg" : 255,
        "bg" : 0,
        "scale" : 1.0,
        "thickness" : 2,
        "alpha" : 0.3
    }
}
```

The stage operates on a low resolution stream image of size 224×224.
Run the following command to use this stage file with `rpicam-hello`:

```console
$ rpicam-hello --post-process-file object*classify*tf.json --lores-width 224 --lores-height 224
```

.Object classification of a desktop computer and monitor.
image: images/classify.jpg[Object classification of a desktop computer and monitor]

#### `pose*estimation*tf` stage

Download: https://github.com/Qengineering/TensorFlow*Lite*Pose*RPi*32-bits[]

`pose*estimation*tf` uses a Google MobileNet v1 model to detect pose information.

You can configure this stage with the following parameters:

[cols="1,3"]
|===
| `refresh*rate` | The number of frames that must elapse between model runs
| `model*file` | Filepath of the TFLite model file
| `verbose` | Output extra information to the console
|===

Use the separate `plot*pose*cv` stage to draw the detected pose onto the main image.

You can configure the `plot*pose*cv` stage with the following parameters:

[cols="1,3"]
|===
| `confidence*threshold` | Confidence threshold determining how much to draw; can be less than zero
|===

Example `pose*estimation*tf.json` file:

```json
{
    "pose*estimation*tf" : {
        "refresh*rate" : 5,
        "model*file" : "posenet*mobilenet*v1*100*257x257*multi*kpt*stripped.tflite"
    },
    "plot*pose*cv" : {
       "confidence*threshold" : -0.5
    }
}
```

The stage operates on a low resolution stream image of size 257×257. ***Because YUV420 images must have even dimensions, round up to 258×258 for YUV420 images.***

Run the following command to use this stage file with `rpicam-hello`:

```console
$ rpicam-hello --post-process-file pose*estimation*tf.json --lores-width 258 --lores-height 258
```

.Pose estimation of an adult human male.
image: images/pose.jpg[Pose estimation of an adult human male]

#### `object*detect*tf` stage

Download: https://storage.googleapis.com/download.tensorflow.org/models/tflite/coco*ssd*mobilenet*v1*1.0*quant*2018*06*29.zip[]

`object*detect*tf` uses a Google MobileNet v1 SSD (Single Shot Detector) model to detect and label objects.

You can configure this stage with the following parameters:

[cols="1,3"]
|===
| `refresh*rate` | The number of frames that must elapse between model runs
| `model*file` | Filepath of the TFLite model file
| `labels*file` | Filepath of the file containing the list of labels
| `confidence*threshold` | Confidence threshold before accepting a match
| `overlap*threshold` | Determines the amount of overlap between matches for them to be merged as a single match.
| `verbose` | Output extra information to the console
|===

Use the separate `object*detect*draw*cv` stage to draw the detected objects onto the main image.

You can configure the `object*detect*draw*cv` stage with the following parameters:

[cols="1,3"]
|===
| `line*thickness` | Thickness of the bounding box lines
| `font*size` | Size of the font used for the label
|===

Example `object*detect*tf.json` file:

```json
{
    "object*detect*tf" : {
        "number*of*threads" : 2,
        "refresh*rate" : 10,
        "confidence*threshold" : 0.5,
        "overlap*threshold" : 0.5,
        "model*file" : "/home/<username>/models/coco*ssd*mobilenet*v1*1.0*quant*2018*06*29/detect.tflite",
        "labels*file" : "/home/<username>/models/coco*ssd*mobilenet*v1*1.0*quant*2018*06*29/labelmap.txt",
        "verbose" : 1
    },
    "object*detect*draw*cv" : {
       "line*thickness" : 2
    }
}
```

The stage operates on a low resolution stream image of size 300×300. Run the following command, which passes a 300×300 crop to the detector from the centre of the 400×300 low resolution image, to use this stage file with `rpicam-hello`:

```console
$ rpicam-hello --post-process-file object*detect*tf.json --lores-width 400 --lores-height 300
```

.Detecting apple and cat objects.
image: images/detection.jpg[Detecting apple and cat objects]

#### `segmentation*tf` stage

Download: https://tfhub.dev/tensorflow/lite-model/deeplabv3/1/metadata/2?lite-format=tflite[]

`segmentation*tf` uses a Google MobileNet v1 model. This stage requires a label file, found at the `assets/segmentation*labels.txt`.

This stage runs on an image of size 257×257. Because YUV420 images must have even dimensions, the low resolution image should be at least 258 pixels in both width and height. The stage adds a vector of 257×257 values to the image metadata where each value indicates the categories a pixel belongs to. You can optionally draw a representation of the segmentation into the bottom right corner of the image.

You can configure this stage with the following parameters:

[cols="1,3"]
|===
| `refresh*rate` | The number of frames that must elapse between model runs
| `model*file` | Filepath of the TFLite model file
| `labels*file` | Filepath of the file containing the list of labels
| `threshold` | When verbose is set, prints when the number of pixels with any label exceeds this number
| `draw` | Draws the segmentation map into the bottom right hand corner of the image
| `verbose` | Output extra information to the console
|===

Example `segmentation*tf.json` file:

```json
{
    "segmentation*tf" : {
        "number*of*threads" : 2,
        "refresh*rate" : 10,
        "model*file" : "/home/<username>/models/lite-model*deeplabv3*1*metadata*2.tflite",
        "labels*file" : "/home/<username>/models/segmentation*labels.txt",
        "draw" : 1,
        "verbose" : 1
    }
}
```

This example takes a camera image and reduces it to 258×258 pixels in size. This stage even works when squashing a non-square image without cropping. This example enables the segmentation map in the bottom right hand corner.

Run the following command to use this stage file with `rpicam-hello`:

```console
$ rpicam-hello --post-process-file segmentation_tf.json --lores-width 258 --lores-height 258 --viewfinder-width 1024 --viewfinder-height 1024
```

.Running segmentation and displaying the results on a map in the bottom right.
image: images/segmentation.jpg[Running segmentation and displaying the results on a map in the bottom right]