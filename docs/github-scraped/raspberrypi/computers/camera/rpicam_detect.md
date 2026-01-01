### `rpicam-detect`

NOTE: Raspberry Pi OS does not include `rpicam-detect`. However, you can build `rpicam-detect` if you have xref:camera*software.adoc#post-processing-with-tensorflow-lite[installed TensorFlow Lite]. For more information, see the xref:camera*software.adoc#build-libcamera-and-rpicam-apps[`rpicam-apps` build instructions]. Don't forget to pass `-Denable*tflite=enabled` when you run `meson`.

`rpicam-detect` displays a preview window and monitors the contents using a Google MobileNet v1 SSD (Single Shot Detector) neural network trained to identify about 80 classes of objects using the Coco dataset. `rpicam-detect` recognises people, cars, cats and many other objects.

Whenever `rpicam-detect` detects a target object, it captures a full-resolution JPEG. Then it returns to monitoring preview mode.

See the xref:camera*software.adoc#object*detect*tf-stage[TensorFlow Lite object detector] section for general information on model usage. For example, you might spy secretly on your cats while you are away with:

```console
$ rpicam-detect -t 0 -o cat%04d.jpg --lores-width 400 --lores-height 300 --post-process-file object*detect*tf.json --object cat
```