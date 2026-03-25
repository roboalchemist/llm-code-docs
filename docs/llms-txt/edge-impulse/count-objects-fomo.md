# Source: https://docs.edgeimpulse.com/tutorials/topics/post-processing/count-objects-fomo.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Count objects using FOMO

<a href="https://colab.research.google.com/github/edgeimpulse/notebooks/blob/main/notebooks/object-counting-using-fomo.ipynb" target="_blank">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open in Google Colab" noZoom />
</a>

The Edge Impulse object detection model (FOMO) is effective at classifying objects and very lightweight (can run on MCUs). It does not however have any object persistence between frames. One common use of computer vision is for object counting- in order to achieve this you will need to add in some extra logic when deploying.

This notebook takes you through how to count objects **using the linux deployment block** (and provides some pointers for how to achieve similar logic other firmware deployment options).

Relevant links:

* Raw python files for the linux deployment example: [https://github.com/edgeimpulse/object-counting-demo](https://github.com/edgeimpulse/object-counting-demo)
* An end-to-end demo for on-device deployment of object counting: [https://github.com/edgeimpulse/conveyor-counting-data-synthesis-demo](https://github.com/edgeimpulse/conveyor-counting-data-synthesis-demo)

## 1. Download the linux deployment .eim for your project

To run your model locally, you need to deploy to a linux target in your project. First you need to enable all linux targets. Head to the deployment screen and click "Linux Boards" then in the following pop-up select "show all Linux deployment options on this page":

<Frame caption="Enable linux deployment">
  <img src="https://raw.githubusercontent.com/edgeimpulse/notebooks/main/.assets/images/show-linux-deploy.png" />
</Frame>

Then download the linux/mac target which is relevant to your machine:

<Frame caption="Download your relevant .eim">
  <img src="https://raw.githubusercontent.com/edgeimpulse/notebooks/main/.assets/images/linux-deploy-options.png" />
</Frame>

Finally, follow the instructions shown as a pop-up to make your .eim file executable (for example for MacOS):

* Open a terminal window and navigate to the folder where you downloaded this model.
* Mark the model as executable: chmod +x path-to-model.eim
* Remove the quarantine flag: xattr -d com.apple.quarantine ./path-to-model.eim

## 2. Object Detection

### Dependencies

Ensure you have these libraries installed before starting:

```python  theme={"system"}
! pip install edge_impulse_linux
! pip install numpy
! pip install opencv-python
```

### 2.1 Run Object Counting on a video file

(see next heading for running on a webcam)

This program will run object detection on an input video file and count the objects going upwards which pass a threshold (TOP\_Y). The sensitivity can be tuned with the number of columns (NUM\_COLS) and the DETECT\_FACTOR which is the factor of width/height of the object used to determine object permanence between frames.

Ensure you have added the relevant paths to your model file and video file:

* modelfile = '/path/to/modelfile.eim'
* videofile = '/path/to/video.mp4'

```python  theme={"system"}
import cv2
import os
import time
import sys, getopt
import numpy as np
from edge_impulse_linux.image import ImageImpulseRunner


modelfile = '/path/to/modelfile.eim'
videofile = '/path/to/video.mp4'


runner = None
# if you don't want to see a video preview, set this to False
show_camera = True
if (sys.platform == 'linux' and not os.environ.get('DISPLAY')):
    show_camera = False
print('MODEL: ' + modelfile)

with ImageImpulseRunner(modelfile) as runner:
    try:
        model_info = runner.init()
        print('Loaded runner for "' + model_info['project']['owner'] + ' / ' + model_info['project']['name'] + '"')
        labels = model_info['model_parameters']['labels']
        count = 0
        vidcap = cv2.VideoCapture(videofile)
        sec = 0
        start_time = time.time()

        def getFrame(sec):
            vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
            hasFrames,image = vidcap.read()
            if hasFrames:
                return image
            else:
                print('Failed to load frame', videofile)
                exit(1)


        img = getFrame(sec)


        # Define the top of the image and the number of columns
        TOP_Y = 30
        NUM_COLS = 5
        COL_WIDTH = int(vidcap.get(3) / NUM_COLS)
        # Define the factor of the width/height which determines the threshold
        # for detection of the object's movement between frames:
        DETECT_FACTOR = 1.5

        # Initialize variables
        count = [0] * NUM_COLS
        countsum = 0
        previous_blobs = [[] for _ in range(NUM_COLS)]

        while img.size != 0:
            # imread returns images in BGR format, so we need to convert to RGB
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

            # get_features_from_image also takes a crop direction arguments in case you don't have square images
            features, cropped = runner.get_features_from_image(img)
            img2 = cropped
            COL_WIDTH = int(np.shape(cropped)[0]/NUM_COLS)

            # the image will be resized and cropped, save a copy of the picture here
            # so you can see what's being passed into the classifier
            cv2.imwrite('debug.jpg', cv2.cvtColor(cropped, cv2.COLOR_RGB2BGR))

            res = runner.classify(features)
            # Initialize list of current blobs
            current_blobs = [[] for _ in range(NUM_COLS)]

            if "bounding_boxes" in res["result"].keys():
                print('Found %d bounding boxes (%d ms.)' % (len(res["result"]["bounding_boxes"]), res['timing']['dsp'] + res['timing']['classification']))
                for bb in res["result"]["bounding_boxes"]:
                    print('\t%s (%.2f): x=%d y=%d w=%d h=%d' % (bb['label'], bb['value'], bb['x'], bb['y'], bb['width'], bb['height']))
                    img2 = cv2.rectangle(cropped, (bb['x'], bb['y']), (bb['x'] + bb['width'], bb['y'] + bb['height']), (255, 0, 0), 1)

                        # Check which column the blob is in
                    col = int(bb['x'] / COL_WIDTH)

                    # Check if blob is within DETECT_FACTOR*h of a blob detected in the previous frame and treat as the same object
                    for blob in previous_blobs[col]:
                        if abs(bb['x'] - blob[0]) < DETECT_FACTOR * (bb['width'] + blob[2]) and abs(bb['y'] - blob[1]) < DETECT_FACTOR * (bb['height'] + blob[3]):
                        # Check this blob has "moved" across the Y threshold
                            if blob[1] >= TOP_Y and bb['y'] < TOP_Y:
                                # Increment count for this column if blob has left the top of the image
                                count[col] += 1
                                countsum += 1
                    # Add current blob to list
                    current_blobs[col].append((bb['x'], bb['y'], bb['width'], bb['height']))



            # Update previous blobs
            previous_blobs = current_blobs

            if (show_camera):
                im2 = cv2.resize(img2, dsize=(800,800))
                cv2.putText(im2, f'{countsum} items passed', (15,750), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)
                cv2.imshow('edgeimpulse', cv2.cvtColor(im2, cv2.COLOR_RGB2BGR))
                print(f'{count}')
                if cv2.waitKey(1) == ord('q'):
                    break

            sec = time.time() - start_time
            sec = round(sec, 2)
            # print("Getting frame at: %.2f sec" % sec)
            img = getFrame(sec)
    finally:
        if (runner):
            print(f'{countsum} Items Left Conveyorbelt')
            runner.stop()

```

### 2.2 Run Object Counting on a webcam stream

This program will run object detection on a webcam port and count the objects going upwards which pass a threshold (TOP\_Y). The sensitivity can be tuned with the number of columns (NUM\_COLS) and the DETECT\_FACTOR which is the factor of width/height of the object used to determine object permanence between frames.

Ensure you have added the relevant paths to your model file and video file:

* modelfile = '/path/to/modelfile.eim'
* \[OPTIONAL] camera\_port = '/camera\_port'

```python  theme={"system"}
import cv2
import os
import sys, getopt
import signal
import time
from edge_impulse_linux.image import ImageImpulseRunner

modelfile = '/path/to/modelfile.eim'
# If you have multiple webcams, replace None with the camera port you desire, get_webcams() can help find this
camera_port = None


runner = None
# if you don't want to see a camera preview, set this to False
show_camera = True
if (sys.platform == 'linux' and not os.environ.get('DISPLAY')):
    show_camera = False

def now():
    return round(time.time() * 1000)

def get_webcams():
    port_ids = []
    for port in range(5):
        print("Looking for a camera in port %s:" %port)
        camera = cv2.VideoCapture(port)
        if camera.isOpened():
            ret = camera.read()[0]
            if ret:
                backendName =camera.getBackendName()
                w = camera.get(3)
                h = camera.get(4)
                print("Camera %s (%s x %s) found in port %s " %(backendName,h,w, port))
                port_ids.append(port)
            camera.release()
    return port_ids

def sigint_handler(sig, frame):
    print('Interrupted')
    if (runner):
        runner.stop()
    sys.exit(0)

signal.signal(signal.SIGINT, sigint_handler)


print('MODEL: ' + modelfile)



with ImageImpulseRunner(modelfile) as runner:
    try:
        model_info = runner.init()
        print('Loaded runner for "' + model_info['project']['owner'] + ' / ' + model_info['project']['name'] + '"')
        labels = model_info['model_parameters']['labels']
        if camera_port:
            videoCaptureDeviceId = int(args[1])
        else:
            port_ids = get_webcams()
            if len(port_ids) == 0:
                raise Exception('Cannot find any webcams')
            if len(port_ids)> 1:
                raise Exception("Multiple cameras found. Add the camera port ID as a second argument to use to this script")
            videoCaptureDeviceId = int(port_ids[0])

        camera = cv2.VideoCapture(videoCaptureDeviceId)
        ret = camera.read()[0]
        if ret:
            backendName = camera.getBackendName()
            w = camera.get(3)
            h = camera.get(4)
            print("Camera %s (%s x %s) in port %s selected." %(backendName,h,w, videoCaptureDeviceId))
            camera.release()
        else:
            raise Exception("Couldn't initialize selected camera.")

        next_frame = 0 # limit to ~10 fps here

        # Define the top of the image and the number of columns
        TOP_Y = 100
        NUM_COLS = 5
        COL_WIDTH = int(w / NUM_COLS)
        # Define the factor of the width/height which determines the threshold
        # for detection of the object's movement between frames:
        DETECT_FACTOR = 1.5

        # Initialize variables
        count = [0] * NUM_COLS
        countsum = 0
        previous_blobs = [[] for _ in range(NUM_COLS)]



        for res, img in runner.classifier(videoCaptureDeviceId):
            # Initialize list of current blobs
            current_blobs = [[] for _ in range(NUM_COLS)]

            if (next_frame > now()):
                time.sleep((next_frame - now()) / 1000)

            if "bounding_boxes" in res["result"].keys():
                print('Found %d bounding boxes (%d ms.)' % (len(res["result"]["bounding_boxes"]), res['timing']['dsp'] + res['timing']['classification']))
                for bb in res["result"]["bounding_boxes"]:
                    print('\t%s (%.2f): x=%d y=%d w=%d h=%d' % (bb['label'], bb['value'], bb['x'], bb['y'], bb['width'], bb['height']))
                    img = cv2.rectangle(img, (bb['x'], bb['y']), (bb['x'] + bb['width'], bb['y'] + bb['height']), (255, 0, 0), 1)

                        # Check which column the blob is in
                    col = int(bb['x'] / COL_WIDTH)
                    # Check if blob is within DETECT_FACTOR*h of a blob detected in the previous frame and treat as the same object
                    for blob in previous_blobs[col]:
                        print(abs(bb['x'] - blob[0]) < DETECT_FACTOR * (bb['width'] + blob[2]))
                        print(abs(bb['y'] - blob[1]) < DETECT_FACTOR * (bb['height'] + blob[3]))
                        if abs(bb['x'] - blob[0]) < DETECT_FACTOR * (bb['width'] + blob[2]) and abs(bb['y'] - blob[1]) < DETECT_FACTOR * (bb['height'] + blob[3]):
                        # Check this blob has "moved" across the Y threshold
                            if blob[1] >= TOP_Y and bb['y'] < TOP_Y:
                                # Increment count for this column if blob has left the top of the image
                                count[col] += 1
                                countsum += 1
                    # Add current blob to list
                    current_blobs[col].append((bb['x'], bb['y'], bb['width'], bb['height']))

            # Update previous blobs
            previous_blobs = current_blobs

            if (show_camera):
                im2 = cv2.resize(img, dsize=(800,800))
                cv2.putText(im2, f'{countsum} items passed', (15,750), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)
                cv2.imshow('edgeimpulse', cv2.cvtColor(im2, cv2.COLOR_RGB2BGR))
                print('Found %d bounding boxes (%d ms.)' % (len(res["result"]["bounding_boxes"]), res['timing']['dsp'] + res['timing']['classification']))

                if cv2.waitKey(1) == ord('q'):
                    break

            next_frame = now() + 100
    finally:
        if (runner):
            runner.stop()


```

## 3. Deploying to MCU firmware

While running object counting on linux hardware is fairly simple, it would be more useful to be able to deploy this to one of the firmware targets. This method varies per target but broadly speaking it is simple to add the object counting logic into existing firmware.

Here are the main steps:

### 1. Find and clone the Edge Impulse firmware repository for your target hardware

This can be found on our github pages e.g. [https://github.com/edgeimpulse/firmware-arduino-nicla-vision](https://github.com/edgeimpulse/firmware-arduino-nicla-vision)

### 2. Deploy your model to a C++ library

You'll need to replace the "edge-impulse-sdk", "model-parameters" and "tflite-model" folders within the cloned firmware with the ones you've just downloaded for your model.

### 3. Find the object detection bounding boxes printout code in your firmware

This will be in a .h or similar file somewhere in the firmware. Likely in the ei\_image\_nn.h file. It can be found by searching for these lines:

```python  theme={"system"}
#if EI_CLASSIFIER_OBJECT_DETECTION == 1
        bool bb_found = result.bounding_boxes[0].value > 0;
```

The following lines must be added into the logic in these files (For code itself see below, diff for clarity). Firstly these variables must be instantiated: &#x20;

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/FtCF_ajfwASxt-xU/.assets/images/diff1.png?fit=max&auto=format&n=FtCF_ajfwASxt-xU&q=85&s=aea2e8bcc56d7244b0e75456595d342c" alt="" width="796" height="309" data-path=".assets/images/diff1.png" />
</Frame>

Then this logic must be inserted into the bounding box printing logic here:&#x20;

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/FtCF_ajfwASxt-xU/.assets/images/diff2.png?fit=max&auto=format&n=FtCF_ajfwASxt-xU&q=85&s=f7b5d8b80c6678001d33710df757051a" alt="" width="1159" height="700" data-path=".assets/images/diff2.png" />
</Frame>

Full code example for nicla vision (src/inference/ei\_run\_camera\_impulse.cpp):

```python  theme={"system"}
/* Edge Impulse ingestion SDK
 * Copyright (c) 2022 EdgeImpulse Inc.
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in
 * all copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 * SOFTWARE.
 */

/* Include ----------------------------------------------------------------- */
#include "model-parameters/model_metadata.h"
#include "ei_device_lib.h"

#if defined(EI_CLASSIFIER_SENSOR) && EI_CLASSIFIER_SENSOR == EI_CLASSIFIER_SENSOR_CAMERA

#include "edge-impulse-sdk/classifier/ei_run_classifier.h"
#include "edge-impulse-sdk/dsp/image/image.hpp"
#include "ei_camera.h"
#include "firmware-sdk/at_base64_lib.h"
#include "firmware-sdk/jpeg/encode_as_jpg.h"
#include "firmware-sdk/ei_device_interface.h"
#include "stdint.h"
#include "ei_device_nicla_vision.h"
#include "ei_run_impulse.h"

#include <ea_malloc.h>

#define DWORD_ALIGN_PTR(a)   ((a & 0x3) ?(((uintptr_t)a + 0x4) & ~(uintptr_t)0x3) : a)
#define ALIGN_PTR(p,a)   ((p & (a-1)) ?(((uintptr_t)p + a) & ~(uintptr_t)(a-1)) : p)

typedef enum {
    INFERENCE_STOPPED,
    INFERENCE_WAITING,
    INFERENCE_SAMPLING,
    INFERENCE_DATA_READY
} inference_state_t;

static inference_state_t state = INFERENCE_STOPPED;
static uint64_t last_inference_ts = 0;

static bool debug_mode = false;
static bool continuous_mode = false;

static uint8_t *snapshot_buf = nullptr;
static uint32_t snapshot_buf_size;

static ei_device_snapshot_resolutions_t snapshot_resolution;
static ei_device_snapshot_resolutions_t fb_resolution;

static bool resize_required = false;
static uint32_t inference_delay;

 // Define the top of the image and the number of columns
static int TOP_Y = 50;
static int NUM_COLS = 5;
static int COL_WIDTH = EI_CLASSIFIER_INPUT_WIDTH / NUM_COLS;
static int MAX_ITEMS = 10;

// Define the factor of the width/height which determines the threshold
// for detection of the object's movement between frames:
static float DETECT_FACTOR = 1.5;

// Initialize variables
std::vector<int> count(NUM_COLS, 0);
int countsum =0;
int notfoundframes = 0;
std::vector<std::vector<ei_impulse_result_bounding_box_t> > previous_blobs(NUM_COLS);

static int ei_camera_get_data(size_t offset, size_t length, float *out_ptr)
{
    // we already have a RGB888 buffer, so recalculate offset into pixel index
    size_t pixel_ix = offset * 3;
    size_t pixels_left = length;
    size_t out_ptr_ix = 0;

    while (pixels_left != 0) {
        out_ptr[out_ptr_ix] = (snapshot_buf[pixel_ix] << 16) + (snapshot_buf[pixel_ix + 1] << 8) + snapshot_buf[pixel_ix + 2];

        // go to the next pixel
        out_ptr_ix++;
        pixel_ix+=3;
        pixels_left--;
    }

    // and done!
    return 0;
}

void ei_run_impulse(void)
{
    switch(state) {
        case INFERENCE_STOPPED:
            // nothing to do
            return;
        case INFERENCE_WAITING:
            if(ei_read_timer_ms() < (last_inference_ts + inference_delay)) {
                return;
            }
            state = INFERENCE_DATA_READY;
            break;
        case INFERENCE_SAMPLING:
        case INFERENCE_DATA_READY:
            if(continuous_mode == true) {
                state = INFERENCE_WAITING;
            }
            break;
        default:
            break;
    }

    snapshot_buf = (uint8_t*)ea_malloc(snapshot_buf_size + 32);
    snapshot_buf = (uint8_t *)ALIGN_PTR((uintptr_t)snapshot_buf, 32);

    // check if allocation was successful
    if(snapshot_buf == nullptr) {
        ei_printf("ERR: Failed to allocate snapshot buffer!\n");
        return;
    }

    EiCameraNiclaVision *camera = static_cast<EiCameraNiclaVision*>(EiCameraNiclaVision::get_camera());

    ei_printf("Taking photo...\n");

    bool isOK = camera->ei_camera_capture_rgb888_packed_big_endian(snapshot_buf, snapshot_buf_size);
    if (!isOK) {
        return;
    }

    if (resize_required) {
        ei::image::processing::crop_and_interpolate_rgb888(
            snapshot_buf,
            fb_resolution.width,
            fb_resolution.height,
            snapshot_buf,
            snapshot_resolution.width,
            snapshot_resolution.height);
    }

    ei::signal_t signal;
    signal.total_length = EI_CLASSIFIER_INPUT_WIDTH * EI_CLASSIFIER_INPUT_HEIGHT;
    signal.get_data = &ei_camera_get_data;

    // Print framebuffer as JPG during debugging
    if(debug_mode) {
        ei_printf("Begin output\n");

        size_t jpeg_buffer_size = EI_CLASSIFIER_INPUT_WIDTH * EI_CLASSIFIER_INPUT_HEIGHT >= 128 * 128 ?
            8192 * 3 :
            4096 * 4;
        uint8_t *jpeg_buffer = NULL;
        jpeg_buffer = (uint8_t*)ei_malloc(jpeg_buffer_size);
        if (!jpeg_buffer) {
            ei_printf("ERR: Failed to allocate JPG buffer\r\n");
            return;
        }

        size_t out_size;
        int x = encode_rgb888_signal_as_jpg(&signal, EI_CLASSIFIER_INPUT_WIDTH, EI_CLASSIFIER_INPUT_HEIGHT, jpeg_buffer, jpeg_buffer_size, &out_size);
        if (x != 0) {
            ei_printf("Failed to encode frame as JPEG (%d)\n", x);
            return;
        }

        ei_printf("Framebuffer: ");
        base64_encode((char*)jpeg_buffer, out_size, ei_putc);
        ei_printf("\r\n");

        if (jpeg_buffer) {
            ei_free(jpeg_buffer);
        }
    }

    // run the impulse: DSP, neural network and the Anomaly algorithm
    ei_impulse_result_t result = { 0 };

    EI_IMPULSE_ERROR ei_error = run_classifier(&signal, &result, false);
    if (ei_error != EI_IMPULSE_OK) {
        ei_printf("ERR: Failed to run impulse (%d)\n", ei_error);
        ea_free(snapshot_buf);
        return;
    }
    ea_free(snapshot_buf);

    // print the predictions
    ei_printf("Predictions (DSP: %d ms., Classification: %d ms., Anomaly: %d ms., Count: %d ): \n",
                result.timing.dsp, result.timing.classification,result.timing.anomaly, countsum);

#if EI_CLASSIFIER_OBJECT_DETECTION == 1
    bool bb_found = result.bounding_boxes[0].value > 0;
    std::vector<std::vector<ei_impulse_result_bounding_box_t> > current_blobs(NUM_COLS);
    for (size_t ix = 0; ix < result.bounding_boxes_count; ix++) {
        auto bb = result.bounding_boxes[ix];
        if (bb.value == 0) {
            continue;
        }
        // Check which column the blob is in
        int col = int(bb.x / COL_WIDTH);
        // Check if blob is within DETECT_FACTOR*h of a blob detected in the previous frame and treat as the same object
        for (auto blob : previous_blobs[col]) {
            if (abs(int(bb.x - blob.x)) < DETECT_FACTOR * (bb.width + blob.width) && abs(int(bb.y - blob.y)) < DETECT_FACTOR * (bb.height + blob.height)) {
                // Check this blob has "moved" across the Y threshold
                if (blob.y >= TOP_Y && bb.y < TOP_Y) {
                    // Increment count for this column if blob has left the top of the image
                    count[col]++;
                    countsum++;
                }
            }
        }
        // Add current blob to list
        current_blobs[col].push_back(bb);
        ei_printf("    %s (%f) [ x: %u, y: %u, width: %u, height: %u ]\n", bb.label, bb.value, bb.x, bb.y, bb.width, bb.height);
    }
    previous_blobs = std::move(current_blobs);
    if (bb_found) {
        ei_printf("    Count: %d\n",countsum);
        notfoundframes = 0;
    }
    else {
        notfoundframes ++;
        if (notfoundframes == 1){
            ei_printf("    No objects found\n");
        }
        else {
            ei_printf("    Count: %d\n",countsum);
        }
    }

#else
    for (size_t ix = 0; ix < EI_CLASSIFIER_LABEL_COUNT; ix++) {
        ei_printf("    %s: %.5f\n", result.classification[ix].label,
                                    result.classification[ix].value);

    }

#if EI_CLASSIFIER_HAS_ANOMALY == 1
        ei_printf("    anomaly score: %.3f\n", result.anomaly);
#endif
#endif

    if (debug_mode) {
        ei_printf("\r\n----------------------------------\r\n");
        ei_printf("End output\r\n");
    }

    if(continuous_mode == false) {
        ei_printf("Starting inferencing in %d seconds...\n", inference_delay / 1000);
        last_inference_ts = ei_read_timer_ms();
        state = INFERENCE_WAITING;
    }
}

void ei_start_impulse(bool continuous, bool debug, bool use_max_uart_speed)
{
    snapshot_resolution.width = EI_CLASSIFIER_INPUT_WIDTH;
    snapshot_resolution.height = EI_CLASSIFIER_INPUT_HEIGHT;

    debug_mode = debug;
    continuous_mode = (debug) ? true : continuous;

    EiDeviceNiclaVision* dev = static_cast<EiDeviceNiclaVision*>(EiDeviceNiclaVision::get_device());
    EiCameraNiclaVision *camera = static_cast<EiCameraNiclaVision*>(EiCameraNiclaVision::get_camera());

    // check if minimum suitable sensor resolution is the same as
    // desired snapshot resolution
    // if not we need to resize later
    fb_resolution = camera->search_resolution(snapshot_resolution.width, snapshot_resolution.height);

    if (snapshot_resolution.width != fb_resolution.width || snapshot_resolution.height != fb_resolution.height) {
        resize_required = true;
    }

    if (!camera->init(snapshot_resolution.width, snapshot_resolution.height)) {
        ei_printf("Failed to init camera, check if camera is connected!\n");
        return;
    }

    snapshot_buf_size = fb_resolution.width * fb_resolution.height * 3;

    // summary of inferencing settings (from model_metadata.h)
    ei_printf("Inferencing settings:\n");
    ei_printf("\tImage resolution: %dx%d\n", EI_CLASSIFIER_INPUT_WIDTH, EI_CLASSIFIER_INPUT_HEIGHT);
    ei_printf("\tFrame size: %d\n", EI_CLASSIFIER_DSP_INPUT_FRAME_SIZE);
    ei_printf("\tNo. of classes: %d\n", sizeof(ei_classifier_inferencing_categories) / sizeof(ei_classifier_inferencing_categories[0]));

    if(continuous_mode == true) {
        inference_delay = 0;
        state = INFERENCE_DATA_READY;
    }
    else {
        inference_delay = 2000;
        last_inference_ts = ei_read_timer_ms();
        state = INFERENCE_WAITING;
        ei_printf("Starting inferencing in %d seconds...\n", inference_delay / 1000);
    }

    if (debug_mode) {
        ei_printf("OK\r\n");
        ei_sleep(100);
        dev->set_max_data_output_baudrate();
        ei_sleep(100);
    }

    while(!ei_user_invoke_stop_lib()) {
        ei_run_impulse();
        ei_sleep(1);
    }

    ei_stop_impulse();

    if (debug_mode) {
        ei_printf("\r\nOK\r\n");
        ei_sleep(100);
        dev->set_default_data_output_baudrate();
        ei_sleep(100);
    }

}

void ei_stop_impulse(void)
{
    state = INFERENCE_STOPPED;
}

bool is_inference_running(void)
{
    return (state != INFERENCE_STOPPED);
}

#endif /* defined(EI_CLASSIFIER_SENSOR) && EI_CLASSIFIER_SENSOR == EI_CLASSIFIER_SENSOR_CAMERA */

// AT+RUNIMPULSE

```

### 4. Build your firmware locally and flash to your device

Follow the instructions in the README.md file for the firmware repo you have been working in.

### 5. Run your impulse on device

Use the command below to see on-device inference (follow the local link to see bounding boxes and count output in the browser)

```python  theme={"system"}
edge-impulse-run-impulse --debug
```


Built with [Mintlify](https://mintlify.com).