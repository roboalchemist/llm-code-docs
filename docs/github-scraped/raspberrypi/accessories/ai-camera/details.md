## Under the hood

### Overview

The Raspberry Pi AI Camera works differently from traditional AI-based camera image processing systems, as shown in the diagram below:

image: images/imx500-comparison.svg[Traditional versus IMX500 AI camera systems]

The left side demonstrates the architecture of a traditional AI camera system. In such a system, the camera delivers images to the Raspberry Pi. The Raspberry Pi processes the images and then performs AI inference. Traditional systems may use external AI accelerators (as shown) or rely exclusively on the CPU.

The right side demonstrates the architecture of a system that uses IMX500. The camera module contains a small Image Signal Processor (ISP) which turns the raw camera image data into an ***input tensor****. The camera module sends this tensor directly into the AI accelerator within the camera, which produces ****output tensors**** that contain the inferencing results. The AI accelerator sends these tensors to the Raspberry Pi. There is no need for an external accelerator, nor for the Raspberry Pi to run neural network software on the CPU.

To fully understand this system, familiarise yourself with the following concepts:

Input Tensor: The part of the sensor image passed to the AI engine for inferencing. Produced by a small on-board ISP which also crops and scales the camera image to the dimensions expected by the neural network that has been loaded. The input tensor is not normally made available to applications, though it is possible to access it for debugging purposes.

Region of Interest (ROI): Specifies exactly which part of the sensor image is cropped out before being rescaled to the size demanded by the neural network. Can be queried and set by an application. The units used are always pixels in the full resolution sensor output. The default ROI setting uses the full image received from the sensor, cropping no data.

Output Tensors: The results of inferencing performed by the neural network. The precise number and shape of the outputs depend on the neural network. Application code must understand how to handle the tensors.

### System architecture

The diagram below shows the various camera software components (in green) used during our imaging/inference use case with the Raspberry Pi AI Camera module hardware (in red):

image: images/imx500-block-diagram.svg[IMX500 block diagram]

At startup, the IMX500 sensor module loads firmware to run a particular neural network model. During streaming, the IMX500 generates *both* an image stream and an inference stream. This inference stream holds the inputs and outputs of the neural network model, also known as input/output ****tensors****.

### Device drivers

At the lowest level, the the IMX500 sensor kernel driver configures the camera module over the I2C bus. The CSI2 driver (`CFE` on Pi 5, `Unicam` on all other Pi platforms) sets up the receiver to write the image data stream into a frame buffer, together with the embedded data and inference data streams into another buffer in memory.

The firmware files also transfer over the I2C bus wires. On most devices, this uses the standard I2C protocol, but Raspberry Pi 5 uses a custom high speed protocol. The RP2040 SPI driver in the kernel handles firmware file transfer, since the transfer uses the RP2040 microcontroller. The microcontroller bridges the I2C transfers from the kernel to the IMX500 via a SPI bus. Additionally, the RP2040 caches firmware files in on-board storage. This avoids the need to transfer entire firmware blobs over the I2C bus, significantly speeding up firmware loading for firmware you've already used.

### `libcamera`

Once `libcamera` dequeues the image and inference data buffers from the kernel, the IMX500 specific `cam-helper` library (part of the Raspberry Pi IPA within `libcamera`) parses the inference buffer to access the input/output tensors. These tensors are packaged as Raspberry Pi vendor-specific https://libcamera.org/api-html/namespacelibcamera*1*1controls.html[`libcamera` controls]. `libcamera` returns the following controls:

[%header,cols="a,a"]
|===
| Control
| Description

| `CnnOutputTensor`
| Floating point array storing the output tensors.

| `CnnInputTensor`
| Floating point array storing the input tensor.

| `CnnOutputTensorInfo`
| Network specific parameters describing the output tensors' structure:

```c
struct OutputTensorInfo {
	uint32*t tensorDataNum;
	uint32*t numDimensions;
	uint16*t size[MaxNumDimensions];
};

struct CnnOutputTensorInfo {
	char networkName[NetworkNameLen];
	uint32*t numTensors;
	OutputTensorInfo info[MaxNumTensors];
};
```

| `CnnInputTensorInfo`
| Network specific parameters describing the input tensor's structure:

```c
struct CnnInputTensorInfo {
	char networkName[NetworkNameLen];
	uint32*t width;
	uint32*t height;
	uint32*t numChannels;
};
```

|===

### `rpicam-apps`

`rpicam-apps` provides an IMX500 post-processing stage base class that implements helpers for IMX500 post-processing stages: https://github.com/raspberrypi/rpicam-apps/blob/main/post*processing*stages/imx500/imx500*post*processing*stage.hpp[`IMX500PostProcessingStage`]. Use this base class to derive a new post-processing stage for any neural network model running on the IMX500. For an example, see https://github.com/raspberrypi/rpicam-apps/blob/main/post*processing*stages/imx500/imx500*object*detection.cpp[`imx500*object*detection.cpp`]:

```cpp
class ObjectDetection : public IMX500PostProcessingStage
{
public:
	ObjectDetection(RPiCamApp **app) : IMX500PostProcessingStage(app) {}

	char const *Name() const override;

	void Read(boost: property*tree::ptree const &params) override;

	void Configure() override;

	bool Process(CompletedRequestPtr &completed*request) override;
};
```

For every frame received by the application, the `Process()` function is called (`ObjectDetection: Process()` in the above case). In this function, you can extract the output tensor for further processing or analysis:

```cpp
auto output = completed*request->metadata.get(controls: rpi::CnnOutputTensor);
if (!output)
{
  LOG*ERROR("No output tensor found in metadata!");
  return false;
}

std: vector<float> output*tensor(output->data(), output->data() + output->size());
```

Once completed, the final results can either be visualised or saved in metadata and consumed by either another downstream stage, or the top level application itself. In the object inference case:

```cpp
if (objects.size())
  completed*request->post*process*metadata.Set("object*detect.results", objects);
```

The `object*detect*draw*cv` post-processing stage running downstream fetches these results from the metadata and draws the bounding boxes onto the image in the `ObjectDetectDrawCvStage: Process()` function:

```cpp
std: vector<Detection> detections;
completed*request->post*process*metadata.Get("object*detect.results", detections);
```

The following table contains a full list of helper functions provided by `IMX500PostProcessingStage`:

[%header,cols="a,a"]
|===
| Function
| Description

| `Read()`
| Typically called from `<Derived Class>: Read()`, this function reads the config parameters for input tensor parsing and saving.

This function also reads the neural network model file string (`"network*file"`) and sets up the firmware to be loaded on camera open.

| `Process()`
| Typically called from `<Derived Class>: Process()` this function processes and saves the input tensor to a file if required by the JSON config file.

| `SetInferenceRoiAbs()`
| Sets an absolute region of interest (ROI) crop rectangle on the sensor image to use for inferencing on the IMX500.

| `SetInferenceRoiAuto()`
| Automatically calculates region of interest (ROI) crop rectangle on the sensor image to preserve the input tensor aspect ratio for a given neural network.

| `ShowFwProgressBar()`
| Displays a progress bar on the console showing the progress of the neural network firmware upload to the IMX500.

| `ConvertInferenceCoordinates()`
| Converts from the input tensor coordinate space to the final ISP output image space.

There are a number of scaling/cropping/translation operations occurring from the original sensor image to the fully processed ISP output image. This function converts coordinates provided by the output tensor to the equivalent coordinates after performing these operations.

|===

### Picamera2

IMX500 integration in Picamera2 is very similar to what is available in `rpicam-apps`. Picamera2 has an IMX500 helper class that provides the same functionality as the `rpicam-apps` `IMX500PostProcessingStage` base class. This can be imported to any Python script with:

```python
from picamera2.devices.imx500 import IMX500

# This must be called before instantiation of Picamera2
imx500 = IMX500(model*file)
```

To retrieve the output tensors, fetch them from the controls. You can then apply additional processing in your Python script.

For example, in an object inference use case such as https://github.com/raspberrypi/picamera2/tree/main/examples/imx500/imx500*object*detection*demo.py[imx500*object*detection*demo.py], the object bounding boxes and confidence values are extracted in `parse*detections()` and draw the boxes on the image in `draw*detections()`:

```python
class Detection:
    def _*init**(self, coords, category, conf, metadata):
        """Create a Detection object, recording the bounding box, category and confidence."""
        self.category = category
        self.conf = conf
        obj*scaled = imx500.convert*inference*coords(coords, metadata, picam2)
        self.box = (obj*scaled.x, obj*scaled.y, obj*scaled.width, obj*scaled.height)

def draw*detections(request, detections, stream="main"):
    """Draw the detections for this request onto the ISP output."""
    labels = get*labels()
    with MappedArray(request, stream) as m:
        for detection in detections:
            x, y, w, h = detection.box
            label = f"{labels[int(detection.category)]} ({detection.conf:.2f})"
            cv2.putText(m.array, label, (x + 5, y + 15), cv2.FONT*HERSHEY*SIMPLEX, 0.5, (0, 0, 255), 1)
            cv2.rectangle(m.array, (x, y), (x + w, y + h), (0, 0, 255, 0))
        if args.preserve*aspect*ratio:
            b = imx500.get*roi*scaled(request)
            cv2.putText(m.array, "ROI", (b.x + 5, b.y + 15), cv2.FONT*HERSHEY*SIMPLEX, 0.5, (255, 0, 0), 1)
            cv2.rectangle(m.array, (b.x, b.y), (b.x + b.width, b.y + b.height), (255, 0, 0, 0))

def parse*detections(request, stream='main'):
    """Parse the output tensor into a number of detected objects, scaled to the ISP output."""
    outputs = imx500.get*outputs(request.get*metadata())
    boxes, scores, classes = outputs[0][0], outputs[1][0], outputs[2][0]
    detections = [ Detection(box, category, score, metadata)
                   for box, score, category in zip(boxes, scores, classes) if score > threshold]
    draw*detections(request, detections, stream)
```

Unlike the `rpicam-apps` example, this example applies no additional hysteresis or temporal filtering.

The IMX500 class in Picamera2 provides the following helper functions:

[%header,cols="a,a"]
|===
| Function
| Description

| `IMX500.get*full*sensor*resolution()`
| Return the full sensor resolution of the IMX500.

| `IMX500.config`
| Returns a dictionary of the neural network configuration.

| `IMX500.convert*inference*coords(coords, metadata, picamera2)`
| Converts the coordinates *coords* from the input tensor coordinate space to the final ISP output image space. Must be passed Picamera2's image metadata for the image, and the Picamera2 object.

There are a number of scaling/cropping/translation operations occurring from the original sensor image to the fully processed ISP output image. This function converts coordinates provided by the output tensor to the equivalent coordinates after performing these operations.

| `IMX500.show*network*fw*progress*bar()`
| Displays a progress bar on the console showing the progress of the neural network firmware upload to the IMX500.

| `IMX500.get*roi*scaled(request)`
| Returns the region of interest (ROI) in the ISP output image coordinate space.

| `IMX500.get*isp*output*size(picamera2)`
| Returns the ISP output image size.

| `IMX5000.get*input*size()`
| Returns the input tensor size based on the neural network model used.

| `IMX500.get*outputs(metadata)`
| Returns the output tensors from the Picamera2 image metadata.

| `IMX500.get*output*shapes(metadata)`
| Returns the shape of the output tensors from the Picamera2 image metadata for the neural network model used.

| `IMX500.set*inference*roi*abs(rectangle)`
| Sets the region of interest (ROI) crop rectangle which determines which part of the sensor image is converted to the input tensor that is used for inferencing on the IMX500. The region of interest should be specified in units of pixels at the full sensor resolution, as a `(x*offset, y*offset, width, height)` tuple.

| `IMX500.set*inference*aspect*ratio(aspect*ratio)`
| Automatically calculates region of interest (ROI) crop rectangle on the sensor image to preserve the given aspect ratio. To make the ROI aspect ratio exactly match the input tensor for this network, use `imx500.set*inference*aspect*ratio(imx500.get*input*size())`.

| `IMX500.get*kpi_info(metadata)`
| Returns the frame-level performance indicators logged by the IMX500 for the given image metadata.

|===