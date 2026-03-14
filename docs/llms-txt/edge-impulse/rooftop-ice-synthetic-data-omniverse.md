# Source: https://docs.edgeimpulse.com/projects/expert-network/rooftop-ice-synthetic-data-omniverse.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Rooftop Ice Detection with Things Network Visualization - Nvidia Omniverse Replicator

Created By: Eivind Holt

Public Project Link: [https://studio.edgeimpulse.com/public/332581/live](https://studio.edgeimpulse.com/public/332581/live)

GitHub Repo: [https://github.com/eivholt/icicle-monitor](https://github.com/eivholt/icicle-monitor)

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Rd2O8sszhA3K-oLX/.assets/images/rooftop-ice-synthetic-data-omniverse/cover1.png?fit=max&auto=format&n=Rd2O8sszhA3K-oLX&q=85&s=31eb0e61339918bffa4850a224d82f96" width="1600" height="908" data-path=".assets/images/rooftop-ice-synthetic-data-omniverse/cover1.png" />
</Frame>

## Introduction

The portable device created in this project monitors buildings and warns the responsible parties when potentially hazardous icicles are formed. In ideal conditions, icicles can form at a rate of [more than 1 cm (0.39 in) per minute](https://en.wikipedia.org/wiki/Icicle). In cold climates, many people are injured and killed each year by these solid projectiles, leading responsible building owners to often close sidewalks in the spring to minimize risk. This project demonstrates how an extra set of digital eyes can notify property owners icicles are forming and need to be removed before they can cause harm.

<Frame caption="Downtown, photo: Avisa Nordland">
  <img src="https://mintcdn.com/edgeimpulse/Rd2O8sszhA3K-oLX/.assets/images/rooftop-ice-synthetic-data-omniverse/IMG_8710.jpg?fit=max&auto=format&n=Rd2O8sszhA3K-oLX&q=85&s=9709645f0e6e06f0b8769f800975109d" width="1333" height="1000" data-path=".assets/images/rooftop-ice-synthetic-data-omniverse/IMG_8710.jpg" />
</Frame>

## Hardware used

* [Arduino Portenta H7](https://docs.arduino.cc/hardware/portenta-h7/)
* [Arduino Portenta Vision Shield w/LoRa Connectivity](https://docs.arduino.cc/hardware/portenta-vision-shield/)
* NVIDIA GeForce RTX
* [Otii Arc from Qoitech](https://www.qoitech.com/otii-arc-pro/)

## Software used

* [Edge Impulse Studio](https://studio.edgeimpulse.com/studio)
* [NVIDIA Omniverse Code](https://www.nvidia.com/en-us/omniverse/) with [Replicator](https://developer.nvidia.com/omniverse/replicator)
* [NVIDIA Isaac Sim](https://developer.nvidia.com/isaac-sim) with [Edge Impulse extension](https://github.com/edgeimpulse/edge-impulse-omniverse-ext)
* [Visual Studio Code](https://code.visualstudio.com/)
* [Blender](https://www.blender.org/)

## Code and machine learning repository

Project [Impulse](https://studio.edgeimpulse.com/public/332581/live) and [Github code repository](https://github.com/eivholt/icicle-monitor).

## Working principle

Icicle formation is detected using a neural network (NN) designed to identify objects in images from the onboard camera. The NN is trained and tested **exclusively** on synthesized images. The images are generated with realistic simulated lighting conditions. A small amount of real images are used to later verify the model.

<div className="flex justify-center">
  <iframe src="https://www.youtube.com/embed/aIkj3uZ_MSE" title="YouTube video player" className="w-1/2 aspect-[9/16] rounded-xl" allowfullscreen />
</div>

## Challenges

The main challenge of detecting forming icicles is the translucent nature of ice and natural variation of sunlight. Because of this we need a great number of images to train a model that captures enough features of the ice with varying lighting conditions. Capturing and annotating such a large dataset is incredibly labor intensive. We can mitigate this problem by synthesizing images with varying lighting conditions in a realistic manner and have the objects of interest automatically labeled.

<iframe src="https://www.youtube.com/embed/qvDXRqBxECo" title="YouTube video player" className="w-full aspect-video rounded-xl" frameborder="0" allowFullScreen />

## Mobility

A powerful platform combined with a high resolution camera with fish-eye lens would increase the ability to detect icicles. However, by deploying the object detection model to a small, power-efficient, but highly constrained device, options for device installation increase. Properly protected against moisture this device can be mounted outdoors on walls or poles facing the roofs in question. LoRaWAN communication enables low battery consumption and long transmission range.

<Frame caption="Arduino Portenta H7">
  <img src="https://mintcdn.com/edgeimpulse/Rd2O8sszhA3K-oLX/.assets/images/rooftop-ice-synthetic-data-omniverse/20240413_215105_.jpg?fit=max&auto=format&n=Rd2O8sszhA3K-oLX&q=85&s=28906b4fe297fbd9c5384b311ec3808c" width="1534" height="1000" data-path=".assets/images/rooftop-ice-synthetic-data-omniverse/20240413_215105_.jpg" />
</Frame>

## Object detection using a neural network

[FOMO (Faster Objects, More Objects)](/studio/projects/learning-blocks/blocks/object-detection/fomo) is a novel machine learning algorithm that allows for visual object detection on highly constrained devices through training of a neural network with a number of convolutional layers.

### Capturing training data and labeling objects

One of the most labor intensive aspects of building any machine learning model is gathering the training data and labeling it. For an object detection model this requires taking hundreds or thousands of images of the objects to detect, drawing rectangles around them, and choosing the correct label for each class. Recently generating pre-labeled images has become feasible and has proven to have great results. This is referred to as **synthetic data generation with domain randomization**. In this project a model will be trained exclusively on synthetic data, and we will see how it can detect the real life counterparts.

### Domain randomization using NVIDIA Omniverse Replicator

NVIDIA Omniverse Code is an IDE that allows us to compose 3D scenes and to write simple Python code to capture images. Further, the Replicator extension is a toolkit that allows us to label the objects in the images and to simplify common domain randomization tasks, such as scattering objects between images. For an in-depth walkthrough on getting started with Omniverse and Replicator, [see this associated article](/projects/expert-network/surgery-inventory-synthetic-data).

### Making a scene

It's possible to create an empty scene in Omniverse and add content programmatically. However, composing initial objects by hand serves as a practical starting point. In this project [a royalty free 3D model of a house](https://www.cgtrader.com/free-3d-models/exterior/house/house-model-3d-dom-2) was used as a basis.

<Frame caption="3D house model">
  <img src="https://mintcdn.com/edgeimpulse/Rd2O8sszhA3K-oLX/.assets/images/rooftop-ice-synthetic-data-omniverse/house.png?fit=max&auto=format&n=Rd2O8sszhA3K-oLX&q=85&s=e9558bb704a33d348b4c6ae2a0e8b0af" width="938" height="623" data-path=".assets/images/rooftop-ice-synthetic-data-omniverse/house.png" />
</Frame>

### Icicle models

To represent the icicle, a high quality model pack was purchased at [Turbo Squid](https://www.turbosquid.com/3d-models/).

<Frame caption="3D icicle models purchased at Turbo Squid">
  <img src="https://mintcdn.com/edgeimpulse/BCrJzLAs8FGQ0Eny/.assets/images/rooftop-ice-synthetic-data-omniverse/turbo-squid-icicle.png?fit=max&auto=format&n=BCrJzLAs8FGQ0Eny&q=85&s=00baa9e95a23626547517bfda8474868" width="1243" height="748" data-path=".assets/images/rooftop-ice-synthetic-data-omniverse/turbo-squid-icicle.png" />
</Frame>

To be able to import the models into Omniverse and Isaac Sim, all models have to be converted to [OpenUSD-format](https://developer.nvidia.com/usd). While USD is a great emerging standard for describing, composing, simulating, and collaborating within 3D worlds, it is not yet commonly supported in asset marketplaces. [This article](/projects/expert-network/surgery-inventory-synthetic-data) outlines considerations when performing conversion using Blender to USD. Note that it is advisable to export each individual model and to choose a suitable origin/pivot point.

Blender change origin cheat sheet:

* Select vertex on model (Edit Mode), Shift+S-> Cursor to selected
* (Object Mode) Select Hierarchy, Object>Set Origin\Origin to 3D Cursor
* (Object Mode) Shift+S\Cursor to World Origin

Tip for export:

* Selection only
* Convert Orientation:
  * Forward Axis: X
  * Up Axis: Y

<Frame caption="3D icicle models exported from Blender">
  <img src="https://mintcdn.com/edgeimpulse/Rd2O8sszhA3K-oLX/.assets/images/rooftop-ice-synthetic-data-omniverse/Blender_select_vertex.png?fit=max&auto=format&n=Rd2O8sszhA3K-oLX&q=85&s=cfe24758bd9f0e442ddd11199153628e" width="1466" height="914" data-path=".assets/images/rooftop-ice-synthetic-data-omniverse/Blender_select_vertex.png" />
</Frame>

### Setting semantic metadata on objects

To be able to produce images for training and include labels, we can use a feature of Replicator toolbox found under menu Replicator > Semantics Schema Editor.

<Frame caption="Semantics Schema Editor">
  <img src="https://mintcdn.com/edgeimpulse/BCrJzLAs8FGQ0Eny/.assets/images/rooftop-ice-synthetic-data-omniverse/semantic-editor.png?fit=max&auto=format&n=BCrJzLAs8FGQ0Eny&q=85&s=a5ad86d6a97c015e413859983348212a" width="1600" height="941" data-path=".assets/images/rooftop-ice-synthetic-data-omniverse/semantic-editor.png" />
</Frame>

Here we can select each top node representing an item for object detection and add a key-value pair. Choosing "class" as Semantic Type and "ice" as Semantic Data enables us to export this string as a label later.

### Creating a program for domain randomization

With a basic 3D stage created and objects of interest labeled, we can continue creating a program that will make sure we produce images with slight variations. Our program can be named anything, ending in `.py` and preferably placed close to the stage USD-file. Here is a sample of such a program: [replicator\_init.py](https://github.com/eivholt/icicle-monitor/blob/main/omniverse-replicator/replicator_init.py):

To keep the items generated in our script separate from the manually created content, we start by creating a new layer in the 3D stage:

```python  theme={"system"}
with rep.new_layer():
```

Next we specify that we want to use ray-tracing as our image output. We create a camera and hard code the position. We will point it to our icicles for each render later. Then we use our previously defined semantics data to get references to the icicles for easier manipulation. We also define references to a plane on which we want to scatter the icicles. Lastly we define our render output by selecting the camera and setting the desired resolution. Due to an issue in Omniverse where artifacts are produces at certain resolutions, e.g. 120x120 pixels, we set the output resolution at 128x128 pixels. Edge Impulse Studio will take care of scaling the images to the desired size should we use images of different size than the configured model size.

```python  theme={"system"}
rep.settings.set_render_pathtraced(samples_per_pixel=64)
cameraPlane = rep.get.prims(path_pattern='/World/CameraPlane')
icePlane = rep.get.prims(path_pattern='/World/IcePlane')
icicles = rep.get.prims(semantics=[("class", "ice")])

camera = rep.create.camera(position=(0, 0, 0))
render_product = rep.create.render_product(camera, (128, 128))
```

Due to the asynchronous nature of Replicator we need to define our randomization logic as call-back methods by first registering them in the following fashion:

```python  theme={"system"}
rep.randomizer.register(randomize_camera)
rep.randomizer.register(scatter_ice)
```

Before defining the logic of the randomization methods we define what will happen during each render:

```python  theme={"system"}
with rep.trigger.on_frame(num_frames=10000, rt_subframes=50):
    rep.randomizer.scatter_ice(icicles)
    rep.randomizer.randomize_camera(icicles)
```

The parameter *num\_frames* specifies the desired number of renders. The *rt\_subframes* parameter allows the rendering process to advance a set number of frames before the result is captured and saved to disk. A higher setting enhances complex ray tracing effects like reflections and translucency by giving them more time to interact across surfaces, though it increases rendering time. Each randomization routine is invoked with the option to include specific parameters.

To save each image and its corresponding semantic data, we utilize a designated API. While customizing the writer was considered, attempts to do so using Replicator version 1.9.8 on Windows led to errors. Therefore, we are employing the "BasicWriter" and will develop an independent script to generate a label format that is compatible with Edge Impulse.

```python  theme={"system"}
writer = rep.WriterRegistry.get("BasicWriter")
writer.initialize(
    output_dir="[set output]",
    rgb=True,
    bounding_box_2d_loose=True)

writer.attach([render_product])
asyncio.ensure_future(rep.orchestrator.step_async())
```

*rgb* indicates that we want to save images to disk as `.png` files. Note that labels are created setting *bounding\_box\_2d\_loose*. This is used in this case instead of *bounding\_box\_2d\_tight* as the latter in some cases would not include the tip of the icicles in the resulting bounding box. It also creates labels from the previously defined semantics. The code ends with running a single iteration of the process in Omniverse Code, so we can preview the results.

The bounding boxes can be visualized by clicking the sensor widget, checking "BoundingBox2DLoose" and finally "Show Window".

<Frame caption="Omniverse bounding box">
  <img src="https://mintcdn.com/edgeimpulse/Rd2O8sszhA3K-oLX/.assets/images/rooftop-ice-synthetic-data-omniverse/omniverse-bb.png?fit=max&auto=format&n=Rd2O8sszhA3K-oLX&q=85&s=ab94d6bfaf92cfdbf8c7f3a778713cb5" width="1260" height="582" data-path=".assets/images/rooftop-ice-synthetic-data-omniverse/omniverse-bb.png" />
</Frame>

Now we can implement the randomization logic. First we'll use a method that flips and scatters the icicles on a defined plane.

```python  theme={"system"}
def scatter_ice(icicles):
with icicles:
    carb.log_info(f'Scatter icicle {icicles}')
    ice_rotation = random.choice(
        [
            (-90, 90, 0),
            (-90, -90, 0),
        ]
    )
    rep.modify.pose(rotation=ice_rotation)
    rep.randomizer.scatter_2d(surface_prims=icePlane, check_for_collisions=True)
return icicles.node
```

Next a method that randomly places the camera on another defined plane, and makes sure the camera is pointing at the group of icicles and randomizes focus.

```python  theme={"system"}
def randomize_camera(targets):
with camera:
    rep.randomizer.scatter_2d(surface_prims=cameraPlane)
    rep.modify.pose(look_at=targets)
    rep.modify.attribute("focalLength", rep.distribution.uniform(10.0, 40.0))
return camera.node
```

We can define the methods in any order we like, but in *rep.trigger.on\_frame* it is crucial that the icicles are placed before pointing the camera.

### Running domain randomization

With a basic randomization program in place, we could run it from the embedded script editor (Window > Script Editor), but more robust Python language support can be achieved by developing in Visual Studio Code instead. To connect VS Code with Omniverse we can use the Visual Studio Code extension [Embedded VS Code for NVIDIA Omniverse](https://marketplace.visualstudio.com/items?itemName=Toni-SM.embedded-vscode-for-nvidia-omniverse). See the [extension repo](https://github.com/Toni-SM/semu.misc.vscode) for setup. When ready to run go to Replicator > Start and check progress in the defined output folder.

<Frame caption="Produced images">
  <img src="https://mintcdn.com/edgeimpulse/Rd2O8sszhA3K-oLX/.assets/images/rooftop-ice-synthetic-data-omniverse/output1.png?fit=max&auto=format&n=Rd2O8sszhA3K-oLX&q=85&s=2e537140221152a3f59228a8714fe0fe" width="1244" height="721" data-path=".assets/images/rooftop-ice-synthetic-data-omniverse/output1.png" />
</Frame>

### Randomizing colors

The surface behind the icicles may vary greatly, both in color and texture. Using Replicator randomizing the color of an object's material is easy.

In the scene in Omniverse, either manually create a plane behind the icicles, or create one programmatically.

In Code, define a function that takes in a reference to the plane we want to randomize, the color of the distribution functions with min and max value span:

```python  theme={"system"}
def randomize_screen(screen):
    with screen:
        # Randomize each RGB channel for the whole color spectrum.
        rep.randomizer.color(colors=rep.distribution.uniform((0, 0, 0), (1, 1, 1)))
    return screen.node
```

Then get a reference to the plane:

```python  theme={"system"}
screen = rep.get.prims(path_pattern='/World/Screen')
```

Lastly register the function and trigger it on each new frame:

```python  theme={"system"}
rep.randomizer.register(randomize_screen)
with rep.trigger.on_frame(num_frames=2000, rt_subframes=50):  # rt_subframes=50
    # Other randomization functions...
    rep.randomizer.randomize_screen(screen)
```

<Frame caption="Random background color">
  <img src="https://mintcdn.com/edgeimpulse/BCrJzLAs8FGQ0Eny/.assets/images/rooftop-ice-synthetic-data-omniverse/random_color.png?fit=max&auto=format&n=BCrJzLAs8FGQ0Eny&q=85&s=b47ae494f1a7c1daa12b7681869d302a" width="1305" height="1000" data-path=".assets/images/rooftop-ice-synthetic-data-omniverse/random_color.png" />
</Frame>

<br />

<Frame caption="Random background color">
  <img src="https://mintcdn.com/edgeimpulse/Rd2O8sszhA3K-oLX/.assets/images/rooftop-ice-synthetic-data-omniverse/output2.png?fit=max&auto=format&n=Rd2O8sszhA3K-oLX&q=85&s=2cf154f46d5b24160cb09dc4f02e122a" width="1236" height="703" data-path=".assets/images/rooftop-ice-synthetic-data-omniverse/output2.png" />
</Frame>

Now each image will have a background with random (deterministic, same starting seed) RGB color. Replicator takes care of creating a material with a shader for us. As you might remember, in an effort to reduce RAM usage our neural network reduces RGB color channels to grayscale. In this project we could simplify the color randomization to only pick grayscale colors. The example has been included as it would benefit in projects where color information is not reduced. To only randomize in grayscale, we could change the code in the randomization function to use the same value for R, G and B as follows:

```python  theme={"system"}
def randomize_screen(screen):
    with screen:
        # Generate a single random value for grayscale
        gray_value = rep.distribution.uniform(0, 1)
        # Apply this value across all RGB channels to ensure the color is grayscale
        rep.randomizer.color(colors=gray_value)
    return screen.node
```

<Frame caption="Random background grayscale">
  <img src="https://mintcdn.com/edgeimpulse/BCrJzLAs8FGQ0Eny/.assets/images/rooftop-ice-synthetic-data-omniverse/random_grayscale.png?fit=max&auto=format&n=BCrJzLAs8FGQ0Eny&q=85&s=818c8b75fc47e5567ef672d598574956" width="1463" height="1000" data-path=".assets/images/rooftop-ice-synthetic-data-omniverse/random_grayscale.png" />
</Frame>

### Randomizing textures

To further steer training of the object detection model in capturing features of the desired class, the icicles, and not features that appear due to short comings in the domain randomization, we can create images with the icicles in front of a large variety of background images. A simple way of achieving this is to use a large dataset of random images and randomly assigning one of them to a background plane for each image generated.

```python  theme={"system"}
import os

def randomize_screen(screen, texture_files):
    with screen:
        # Let Replicator pick a random texture from list of .jpg-files
        rep.randomizer.texture(textures=texture_files)
    return screen.node

# Define what folder to look for .jpg files in
folder_path = 'C:/Users/eivho/source/repos/icicle-monitor/val2017/testing/'
# Create a list of strings with complete path and .jpg file names
texture_files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith('.jpg')]

# Register randomizer
rep.randomizer.register(randomize_screen)

# For each frame, call randomization function
with rep.trigger.on_frame(num_frames=2000, rt_subframes=50):
    # Other randomization functions...
    rep.randomizer.randomize_screen(screen, texture_files)
```

<Frame caption="Random background texture">
  <img src="https://mintcdn.com/edgeimpulse/BCrJzLAs8FGQ0Eny/.assets/images/rooftop-ice-synthetic-data-omniverse/random_texture.png?fit=max&auto=format&n=BCrJzLAs8FGQ0Eny&q=85&s=9cc6e617c6caf7fa627edd6d62a2c894" width="1463" height="1000" data-path=".assets/images/rooftop-ice-synthetic-data-omniverse/random_texture.png" />
</Frame>

<br />

<Frame caption="Random background texture, camera perspective">
  <img src="https://mintcdn.com/edgeimpulse/BCrJzLAs8FGQ0Eny/.assets/images/rooftop-ice-synthetic-data-omniverse/random_texture_viewport.png?fit=max&auto=format&n=BCrJzLAs8FGQ0Eny&q=85&s=6953b09a24bf3c28bed895a2ef9fc9f3" width="1463" height="1000" data-path=".assets/images/rooftop-ice-synthetic-data-omniverse/random_texture_viewport.png" />
</Frame>

<br />

<Frame caption="Random background texture">
  <img src="https://mintcdn.com/edgeimpulse/Rd2O8sszhA3K-oLX/.assets/images/rooftop-ice-synthetic-data-omniverse/output3.png?fit=max&auto=format&n=Rd2O8sszhA3K-oLX&q=85&s=e0547370052a2b8241e6040a1982a839" width="1230" height="702" data-path=".assets/images/rooftop-ice-synthetic-data-omniverse/output3.png" />
</Frame>

We could instead generate textures with random shapes and colors. Either way, the resulting renders will look weird, but help the model training process weight features that are relevant for the icicles, not the background.

These are rather unsophisticated approaches. More realistic results would be achieved by changing the [materials](https://docs.omniverse.nvidia.com/materials-and-rendering/latest/materials.html) of the actual walls of the house used as background. Omniverse has a large selection of available materials available in the NVIDIA Assets browser, allowing us to randomize a [much wider range of aspects](https://docs.omniverse.nvidia.com/extensions/latest/ext_replicator/randomizer_details.html) of the rendered results.

### Creating realistic outdoor lighting conditions using Sun Study

In contrast to a controlled indoor environment, creating a robust object detection model intended for outdoor use needs training images with a wide range of realistic natural light. When generating synthetic images we can utilize an [extension that approximates real world sunlight](https://docs.omniverse.nvidia.com/composer/latest/skills/rendering-sun-study.html) based on sun studies.

<iframe src="https://www.youtube.com/embed/MRD-oAxaV8w" title="YouTube video player" className="w-full aspect-video rounded-xl" frameborder="0" allowFullScreen />

The extension let's us set world location, date and time. We can also mix this with the Environment setting in Omniverse, allowing for a wide range of simulation of clouds. As of March 2024 it is not easy to randomize these parameters in script, but this [is likely to change](https://forums.developer.nvidia.com/t/randomize-time-of-day-in-dynamic-sky/273833/9). In the mean time we can set the parameters, generate a few thousand images, change time of day, generate more images and so on.

<iframe src="https://www.youtube.com/embed/qvDXRqBxECo" title="YouTube video player" className="w-full aspect-video rounded-xl" frameborder="0" allowFullScreen />

<Frame caption="Sun Study">
  <img src="https://mintcdn.com/edgeimpulse/Rd2O8sszhA3K-oLX/.assets/images/rooftop-ice-synthetic-data-omniverse/output5.png?fit=max&auto=format&n=Rd2O8sszhA3K-oLX&q=85&s=2ca4a87d4b50037949b9fe768fbfe587" width="1234" height="350" data-path=".assets/images/rooftop-ice-synthetic-data-omniverse/output5.png" />
</Frame>

<br />

<Frame caption="Sun Study">
  <img src="https://mintcdn.com/edgeimpulse/Rd2O8sszhA3K-oLX/.assets/images/rooftop-ice-synthetic-data-omniverse/output4.png?fit=max&auto=format&n=Rd2O8sszhA3K-oLX&q=85&s=e348f74c9f444f3e704e01de623ad085" width="1240" height="352" data-path=".assets/images/rooftop-ice-synthetic-data-omniverse/output4.png" />
</Frame>

<br />

<Frame caption="Sun Study">
  <img src="https://mintcdn.com/edgeimpulse/Rd2O8sszhA3K-oLX/.assets/images/rooftop-ice-synthetic-data-omniverse/output6.png?fit=max&auto=format&n=Rd2O8sszhA3K-oLX&q=85&s=1f8d39ae96ee1620371b8e53d5f00639" width="1235" height="354" data-path=".assets/images/rooftop-ice-synthetic-data-omniverse/output6.png" />
</Frame>

### Creating label file for Edge Impulse Studio

Edge Impulse Studio supports a wide range of image labeling formats for object detection. The output from Replicator's BasicWriter needs to be transformed so it can be uploaded either through the web interface or via the [Ingestion API](/apis/ingestion).

Provided is a simple Python program, [basic\_writer\_to\_pascal\_voc.py](https://github.com/eivholt/icicle-monitor/blob/main/scripts/basic_writer_to_pascal_voc.py) to help get started. Documentation on the supported object detection label formats is located [here](/tools/specifications/data-annotation/object-detection). Run the program from a terminal with:

```
python basic_writer_to_pascal_voc.py <input_folder>
```

or debug from Visual Studio Code by setting input folder in `launch.json` like this:

```
"args": ["../out"]
```

This will create a file `bounding_boxes.labels` that contains all labels and bounding boxes per image.

## Creating an object detection project in Edge Impulse Studio

Look at the [provided object detection Edge Impulse project](https://studio.edgeimpulse.com/public/332581/live) or [follow a guide to create a new FOMO project](/studio/projects/learning-blocks/blocks/object-detection/fomo).

### Uploading images and labels using CLI edge-impulse-uploader

Since we have generated both synthetic images and labels, we can use the [CLI tool from Edge Impulse](/tools/clis/edge-impulse-cli/uploader) to efficiently upload both. Use:

```
edge-impulse-uploader --category split --directory [folder]
```

to connect to your account and project, and upload the image files and labels in `bounding_boxes.labels`. To switch project if necessary, first run:

```
edge-impulse-uploader --clean
```

At any time we can find "Perform train/test split" under "Danger zone" in project dashboard, to distribute images between training/testing in a 80/20 split.

### Model training and performance

Since our synthetic training images are based on both individual and two different sized clusters of icicles, we can't trust the model performance numbers too much. Greater F1 scores are better, but we will never achieve 100%. Still, we can upload increasing numbers of labeled images and observe how performance numbers increase.

2,000 images:

<Frame caption="2000 images">
  <img src="https://mintcdn.com/edgeimpulse/Rd2O8sszhA3K-oLX/.assets/images/rooftop-ice-synthetic-data-omniverse/2000-images.png?fit=max&auto=format&n=Rd2O8sszhA3K-oLX&q=85&s=eefd0c6060596a84e37c7006b509629c" width="671" height="502" data-path=".assets/images/rooftop-ice-synthetic-data-omniverse/2000-images.png" />
</Frame>

6,000 images:

<Frame caption="6000 images">
  <img src="https://mintcdn.com/edgeimpulse/Rd2O8sszhA3K-oLX/.assets/images/rooftop-ice-synthetic-data-omniverse/6000-images-120cycles.png?fit=max&auto=format&n=Rd2O8sszhA3K-oLX&q=85&s=13dba2ef31ff742c7c4f598f357fab13" width="796" height="502" data-path=".assets/images/rooftop-ice-synthetic-data-omniverse/6000-images-120cycles.png" />
</Frame>

14,000 images:

<Frame caption="14000 images">
  <img src="https://mintcdn.com/edgeimpulse/Rd2O8sszhA3K-oLX/.assets/images/rooftop-ice-synthetic-data-omniverse/14000-images-120cycles_no-opt.png?fit=max&auto=format&n=Rd2O8sszhA3K-oLX&q=85&s=fc5e3d1004245ce55da062dd911c83e7" width="946" height="502" data-path=".assets/images/rooftop-ice-synthetic-data-omniverse/14000-images-120cycles_no-opt.png" />
</Frame>

26,000 images:

<Frame caption="26000 images">
  <img src="https://mintcdn.com/edgeimpulse/Rd2O8sszhA3K-oLX/.assets/images/rooftop-ice-synthetic-data-omniverse/26000-images-light-5000coco-120cycles_no-opt.png?fit=max&auto=format&n=Rd2O8sszhA3K-oLX&q=85&s=8af4e62ad850e6a488dce79f93c03806" width="944" height="505" data-path=".assets/images/rooftop-ice-synthetic-data-omniverse/26000-images-light-5000coco-120cycles_no-opt.png" />
</Frame>

Note that the final results include 5000 images from the [COCO 2017 dataset](https://cocodataset.org). Adding this reduces F1 score a bit, but results in a model with significantly less overfitting, that shows almost no false positives when classifying random background scenes.

If we look at results from model testing in Edge Impulse Studio, at first glance the numbers are less than impressive.

<Frame caption="Model testing">
  <img src="https://mintcdn.com/edgeimpulse/Rd2O8sszhA3K-oLX/.assets/images/rooftop-ice-synthetic-data-omniverse/model-testing1.png?fit=max&auto=format&n=Rd2O8sszhA3K-oLX&q=85&s=7e7bd6f91b6c34711963a9472f95ad40" width="1362" height="821" data-path=".assets/images/rooftop-ice-synthetic-data-omniverse/model-testing1.png" />
</Frame>

However if we investigate individual samples where F1 score is less than 100%, we see that the model indeed has detected the icicles, but clustered differently than how the image was originally labeled. What we should look out for are samples that contain visible icicles where none were detected.

In the end virtual and real-life testing tells us how well the model really performs.

### Testing model in simulated environment with NVIDIA Isaac Sim and Edge Impulse extension

We can get useful information about model performance with minimal effort by testing it in a virtual environment. Install [NVIDIA Isaac Sim](https://developer.nvidia.com/isaac-sim) and the [Edge Impulse extension](https://github.com/edgeimpulse/edge-impulse-omniverse-ext).

<Frame caption="Edge Impulse extension">
  <img src="https://mintcdn.com/edgeimpulse/Rd2O8sszhA3K-oLX/.assets/images/rooftop-ice-synthetic-data-omniverse/EI-ext-enable.png?fit=max&auto=format&n=Rd2O8sszhA3K-oLX&q=85&s=13e85c9c32a6b33630ff93fd10888b13" width="1295" height="622" data-path=".assets/images/rooftop-ice-synthetic-data-omniverse/EI-ext-enable.png" />
</Frame>

Install the Sun Study extension in Isaac Sim to be able to vary light conditions while testing.

<Frame caption="Sun Study in Isaac Sim">
  <img src="https://mintcdn.com/edgeimpulse/Rd2O8sszhA3K-oLX/.assets/images/rooftop-ice-synthetic-data-omniverse/Isaac-sunstudy.png?fit=max&auto=format&n=Rd2O8sszhA3K-oLX&q=85&s=fe817cb3dd07889fcb63c9f718f0b5ed" width="1520" height="870" data-path=".assets/images/rooftop-ice-synthetic-data-omniverse/Isaac-sunstudy.png" />
</Frame>

Paste your API key found in the Edge Impulse Studio > Dashboard > Keys > Add new API key into Omniverse Extension:

<Frame caption="Edge Impulse extension API key">
  <img src="https://mintcdn.com/edgeimpulse/Rd2O8sszhA3K-oLX/.assets/images/rooftop-ice-synthetic-data-omniverse/EI-ext-api-key.png?fit=max&auto=format&n=Rd2O8sszhA3K-oLX&q=85&s=e03241f5e4968caf727bac6f997d6b50" width="377" height="318" data-path=".assets/images/rooftop-ice-synthetic-data-omniverse/EI-ext-api-key.png" />
</Frame>

To be able to classify any virtual camera capture we first need to build a version of the model that can run in a JavaScript environment. In Edge Impulse Studio, go to **Deployment**, find "WebAssembly" in the search box and click **Build**. We don't need to keep the resulting .zip package, the extension will find and download it by itself in a moment.

<Frame caption="Edge Impulse WebAssembly">
  <img src="https://mintcdn.com/edgeimpulse/Rd2O8sszhA3K-oLX/.assets/images/rooftop-ice-synthetic-data-omniverse/EI-webasm.png?fit=max&auto=format&n=Rd2O8sszhA3K-oLX&q=85&s=0e087ebc4308ac28f66fce65219b0575" width="1542" height="1000" data-path=".assets/images/rooftop-ice-synthetic-data-omniverse/EI-webasm.png" />
</Frame>

Back in the Edge Impulse extension in Isaac Sim, when we expand the "Classification" group, a message will tell us everything is ready: "Your model is ready! You can now run inference on the current scene".

Before we test it we will make some accommodations in the viewport.

Switch to "RTX - Interactive" to make sure the scene is rendered realistically.

Set viewport resolution to square 1:1 with either the same resolution as our intended device inference (120x120 pixels), or (512x512 pixels).

<Frame caption="Isaac Sim viewport resolution">
  <img src="https://mintcdn.com/edgeimpulse/Rd2O8sszhA3K-oLX/.assets/images/rooftop-ice-synthetic-data-omniverse/Isaac-resolution.png?fit=max&auto=format&n=Rd2O8sszhA3K-oLX&q=85&s=d0fa6666e65ed52e984ba37bf6e7354f" width="517" height="332" data-path=".assets/images/rooftop-ice-synthetic-data-omniverse/Isaac-resolution.png" />
</Frame>

Display Isaac bounding boxes by selecting "BoundingBox2DLoose" under the icon that resembles a robotic sensor, then click "Show Window". Now we can compare the ground truth with model prediction.

<Frame caption="Isaac Sim sensors">
  <img src="https://mintcdn.com/edgeimpulse/Rd2O8sszhA3K-oLX/.assets/images/rooftop-ice-synthetic-data-omniverse/Isaac-sensor.png?fit=max&auto=format&n=Rd2O8sszhA3K-oLX&q=85&s=e9842ffebc4bb7c082b99ef1e5f501a6" width="544" height="505" data-path=".assets/images/rooftop-ice-synthetic-data-omniverse/Isaac-sensor.png" />
</Frame>

<br />

<Frame caption="Isaac Sim model testing">
  <img src="https://mintcdn.com/edgeimpulse/Rd2O8sszhA3K-oLX/.assets/images/rooftop-ice-synthetic-data-omniverse/Isaac-EI-1.png?fit=max&auto=format&n=Rd2O8sszhA3K-oLX&q=85&s=a156dd017f2c554d3c78c29d8962fd95" width="1520" height="738" data-path=".assets/images/rooftop-ice-synthetic-data-omniverse/Isaac-EI-1.png" />
</Frame>

<br />

<Frame caption="Isaac Sim model testing">
  <img src="https://mintcdn.com/edgeimpulse/Rd2O8sszhA3K-oLX/.assets/images/rooftop-ice-synthetic-data-omniverse/Isaac-EI-2.png?fit=max&auto=format&n=Rd2O8sszhA3K-oLX&q=85&s=ab6c0cb59341c23f807619d825e39104" width="1520" height="738" data-path=".assets/images/rooftop-ice-synthetic-data-omniverse/Isaac-EI-2.png" />
</Frame>

<br />

<Frame caption="Isaac Sim model testing">
  <img src="https://mintcdn.com/edgeimpulse/Rd2O8sszhA3K-oLX/.assets/images/rooftop-ice-synthetic-data-omniverse/Isaac-EI-3.png?fit=max&auto=format&n=Rd2O8sszhA3K-oLX&q=85&s=ff0aec45d2dc22f07041cb1d143666bf" width="1600" height="715" data-path=".assets/images/rooftop-ice-synthetic-data-omniverse/Isaac-EI-3.png" />
</Frame>

## Deployment to device and LoRaWAN

### Testing model on device using OpenMV

To get visual verification our model works as intended we can go to Deployment in Edge Impulse Studio, select **OpenMV Firmware** as target and build.

<Frame caption="Edge Impulse Studio Deployment OpenMV Firmware">
  <img src="https://mintcdn.com/edgeimpulse/Rd2O8sszhA3K-oLX/.assets/images/rooftop-ice-synthetic-data-omniverse/OpenMV_deployment.png?fit=max&auto=format&n=Rd2O8sszhA3K-oLX&q=85&s=25ba3969a7924b4b64609928ffb62718" width="975" height="956" data-path=".assets/images/rooftop-ice-synthetic-data-omniverse/OpenMV_deployment.png" />
</Frame>

Follow [the documentation](/hardware/deployments/run-openmv) on how to flash the device and to modify the `ei_object_detection.py` code. Remember to change: `sensor.set_pixformat(sensor.GRAYSCALE)`. The file `edge_impulse_firmware_arduino_portenta.bin` is our firmware for the Arduino Portenta H7 with Vision shield.

<Frame caption="Testing model on device with OpenMV">
  <img src="https://mintcdn.com/edgeimpulse/Rd2O8sszhA3K-oLX/.assets/images/rooftop-ice-synthetic-data-omniverse/OpenMV-testing.png?fit=max&auto=format&n=Rd2O8sszhA3K-oLX&q=85&s=3fb3885d4fa41567c527602efb39bc15" width="1568" height="1000" data-path=".assets/images/rooftop-ice-synthetic-data-omniverse/OpenMV-testing.png" />
</Frame>

### Deploy model as Arduino compatible library and send inference results to The Things Network with LoRaWAN

Start by selecting **Arduino library** as a Deployment target.

<Frame caption="Deploy model as Arduino compatible library">
  <img src="https://mintcdn.com/edgeimpulse/Rd2O8sszhA3K-oLX/.assets/images/rooftop-ice-synthetic-data-omniverse/EI-arduino-library.png?fit=max&auto=format&n=Rd2O8sszhA3K-oLX&q=85&s=dd456f12b734b1c1719f180b62083d9b" width="1600" height="936" data-path=".assets/images/rooftop-ice-synthetic-data-omniverse/EI-arduino-library.png" />
</Frame>

Once built and downloaded, open Arduino IDE, go to **Sketch > Include Library > Add .zip Library ...** and locate the downloaded library. Next go to **File > Examples > \[name of project]\_inferencing > portenta\_h7 > portenta\_h7\_camera** to open a generic sketch template using our model. To test the model continuously and print the results to console this sketch is ready to go. The code might appear daunting, but we really only need to focus on the `loop()` function.

<Frame caption="Arduino compatible library example sketch">
  <img src="https://mintcdn.com/edgeimpulse/Rd2O8sszhA3K-oLX/.assets/images/rooftop-ice-synthetic-data-omniverse/EI-arduino-library-example.png?fit=max&auto=format&n=Rd2O8sszhA3K-oLX&q=85&s=f8ea306614439c9257963c6574b43352" width="1113" height="1000" data-path=".assets/images/rooftop-ice-synthetic-data-omniverse/EI-arduino-library-example.png" />
</Frame>

### Transmit results to The Things Stack sandbox using LoRaWAN

Using The Things Stack sandbox (formerly known as The Things Network) we can create a low-power sensor network that allows transmitting device data with minimal energy consumption, long range, and no network fees. Your area may already be covered by a crowd funded network, or you can [create your own](https://www.thethingsnetwork.org/community/) gateway. [Getting started with LoRaWAN](https://www.thethingsindustries.com/docs/getting-started/) is really fun!

<Frame caption="The Things Network">
  <img src="https://mintcdn.com/edgeimpulse/BCrJzLAs8FGQ0Eny/.assets/images/rooftop-ice-synthetic-data-omniverse/ttn-map.png?fit=max&auto=format&n=BCrJzLAs8FGQ0Eny&q=85&s=41a246a68fb993374288f9138ee05013" width="985" height="454" data-path=".assets/images/rooftop-ice-synthetic-data-omniverse/ttn-map.png" />
</Frame>

Following the [Arduino guide](https://docs.arduino.cc/tutorials/portenta-vision-shield/connecting-to-ttn/) on the topic, we create an application in The Things Stack sandbox and register our first device.

<Frame caption="The Things Stack application">
  <img src="https://mintcdn.com/edgeimpulse/BCrJzLAs8FGQ0Eny/.assets/images/rooftop-ice-synthetic-data-omniverse/ttn-app.png?fit=max&auto=format&n=BCrJzLAs8FGQ0Eny&q=85&s=13d0719613b9f80a9c1804e4610b570a" width="1376" height="775" data-path=".assets/images/rooftop-ice-synthetic-data-omniverse/ttn-app.png" />
</Frame>

<br />

<Frame caption="The Things Stack device">
  <img src="https://mintcdn.com/edgeimpulse/BCrJzLAs8FGQ0Eny/.assets/images/rooftop-ice-synthetic-data-omniverse/ttn-device.png?fit=max&auto=format&n=BCrJzLAs8FGQ0Eny&q=85&s=2881d8eccfe3f982470aae381d3dcb2a" width="1377" height="984" data-path=".assets/images/rooftop-ice-synthetic-data-omniverse/ttn-device.png" />
</Frame>

Next we will simplify things by merging an example Arduino sketch for transmitting a LoRaWAN message, with the Edge Impulse generated object detection model code. Open the example sketch called `LoraSendAndReceive` included with the MKRWAN(v2) library mentioned in the [Arduino guide](https://docs.arduino.cc/tutorials/portenta-vision-shield/connecting-to-ttn/). There is an example of this for you in the [project code repository](https://github.com/eivholt/icicle-monitor/tree/main/portenta-h7/portenta_h7_camera_lora), where you can find an Arduino sketch with the merged code.

<Frame caption="Arduino transmitting inference results over LoRaWAN">
  <img src="https://mintcdn.com/edgeimpulse/Rd2O8sszhA3K-oLX/.assets/images/rooftop-ice-synthetic-data-omniverse/arduino-lora.png?fit=max&auto=format&n=Rd2O8sszhA3K-oLX&q=85&s=82b4d7b80d10e202daf62207859e2e01" width="955" height="656" data-path=".assets/images/rooftop-ice-synthetic-data-omniverse/arduino-lora.png" />
</Frame>

In short, we perform inference every 10 seconds. If any icicles are detected we simply transmit a binary `1` to the The Things Stack application. It is probably obvious that the binary payload is redundant, the presence of a message is enough, but this could be extended to transmit other data, for example the prediction confidence, number of clusters, battery level, temperature or light level.

```python  theme={"system"}
if(bb_found) {
    int lora_err;
    modem.setPort(1);
    modem.beginPacket();
    modem.write((uint8_t)1); // This sends the binary value 0x01
    lora_err = modem.endPacket(true);
}
```

There are a few things to consider in the implementation: The device should enter deep sleep mode and disable/put to sleep all peripherals between object detection runs. Default operation of the Portenta H7 with the Vision shield consumes a lot of energy and will drain a battery quickly. To find out how much energy is consumed we can use a device such as the [Otii Arc from Qoitech](https://www.qoitech.com/otii-arc-pro/). Hook up the positive power supply to **VIN**, negative to **GND**. Since VIN bypasses the Portenta power regulator we should provide 5V, however in my setup the Otii Arc is limited to 4.55V. Luckily it seems to be sufficient and we can take some measurements. By connecting the Otii Arc pin RX to the Portenta pin D14/PA9/UART1 TX, in code we can write debug messages to *Serial1*. This is incredibly helpful in determining what power consumption is associated with what part of the code.

<Frame caption="Arduino Portenta H7 power specs">
  <img src="https://mintcdn.com/edgeimpulse/Rd2O8sszhA3K-oLX/.assets/images/rooftop-ice-synthetic-data-omniverse/portenta_h7_power.png?fit=max&auto=format&n=Rd2O8sszhA3K-oLX&q=85&s=ef316d06fb93e97b4e91b6f44563bf1d" width="997" height="168" data-path=".assets/images/rooftop-ice-synthetic-data-omniverse/portenta_h7_power.png" />
</Frame>

<br />

<Frame caption="Arduino Portenta H7 pin-out">
  <img src="https://mintcdn.com/edgeimpulse/Rd2O8sszhA3K-oLX/.assets/images/rooftop-ice-synthetic-data-omniverse/portenta_h7_pinout.png?fit=max&auto=format&n=Rd2O8sszhA3K-oLX&q=85&s=35ec9f2bf90f6525bb842d26e70e3d26" width="924" height="696" data-path=".assets/images/rooftop-ice-synthetic-data-omniverse/portenta_h7_pinout.png" />
</Frame>

<br />

<Frame caption="Otii Arc hook-up">
  <img src="https://mintcdn.com/edgeimpulse/Rd2O8sszhA3K-oLX/.assets/images/rooftop-ice-synthetic-data-omniverse/otii-arc-portenta.png?fit=max&auto=format&n=Rd2O8sszhA3K-oLX&q=85&s=bb042201b486dd5ade234a8d96ba56b8" width="1200" height="900" data-path=".assets/images/rooftop-ice-synthetic-data-omniverse/otii-arc-portenta.png" />
</Frame>

<br />

<Frame caption="Otii Arc power profile">
  <img src="https://mintcdn.com/edgeimpulse/Rd2O8sszhA3K-oLX/.assets/images/rooftop-ice-synthetic-data-omniverse/otii-icicle-profile.png?fit=max&auto=format&n=Rd2O8sszhA3K-oLX&q=85&s=dc9ab97f8fdb37c838ab76fb7b6cae92" width="1600" height="861" data-path=".assets/images/rooftop-ice-synthetic-data-omniverse/otii-icicle-profile.png" />
</Frame>

As we can see the highlighted section should be optimized for minimal power consumption. This is a complicated subject, especially on a [complex board such as the Arduino Portenta H7](https://github.com/arduino/ArduinoCore-mbed/issues/619) but there are some examples for general guidance:

* [Snow monitor](https://www.hackster.io/eivholt/low-power-snow-depth-sensor-using-lora-e5-b8e7b8#toc-power-profiling-16)
* [Mail box sensor](https://community.element14.com/challenges-projects/project14/rf/b/blog/posts/got-mail-lorawan-mail-box-sensor).

The project code presented here runs inference on an image every 10 seconds. However, this is for demonstration purposes and in a deployment should be much less frequent, like once per hour during daylight. Have a look at this project for an example of how to [remotely control inference interval](https://www.hackster.io/eivholt/low-power-snow-depth-sensor-using-lora-e5-b8e7b8#toc-lora-application-14) via LoRaWAN downlink message. This could be further controlled automatically via an application that has access to an [API for daylight data](https://developer.yr.no/doc/GettingStarted/).

<Frame caption="YR weather API">
  <img src="https://mintcdn.com/edgeimpulse/BCrJzLAs8FGQ0Eny/.assets/images/rooftop-ice-synthetic-data-omniverse/yr-sun.png?fit=max&auto=format&n=BCrJzLAs8FGQ0Eny&q=85&s=ca66cbcfd068cc636774e1437a92ad3f" width="613" height="272" data-path=".assets/images/rooftop-ice-synthetic-data-omniverse/yr-sun.png" />
</Frame>

Next, in the The Things Stack application we need to define a function that will be used to decode the byte into a JSON structure that is easier to interpret when we pass the message further up the chain of services. The function can be found in the [project code repository](https://github.com/eivholt/icicle-monitor/blob/main/TheThingsStack/decoder.js).

<Frame caption="The Things Stack decoder">
  <img src="https://mintcdn.com/edgeimpulse/BCrJzLAs8FGQ0Eny/.assets/images/rooftop-ice-synthetic-data-omniverse/ttn-decoder.png?fit=max&auto=format&n=BCrJzLAs8FGQ0Eny&q=85&s=b0328348f3d2da6b3182deca274b49b2" width="1184" height="812" data-path=".assets/images/rooftop-ice-synthetic-data-omniverse/ttn-decoder.png" />
</Frame>

```javascript  theme={"system"}
function Decoder(bytes, port) {
    // Initialize the result object
    var result = {
        detected: false
    };

    // Check if the first byte is non-zero
    if(bytes[0] !== 0) {
        result.detected = true;
    }

    // Return the result
    return result;
}
```

Now we can observe messages being received and decoded in **Live data** in the TTS console.

<Frame caption="The Things Stack live data">
  <img src="https://mintcdn.com/edgeimpulse/BCrJzLAs8FGQ0Eny/.assets/images/rooftop-ice-synthetic-data-omniverse/ttn-data.png?fit=max&auto=format&n=BCrJzLAs8FGQ0Eny&q=85&s=de64bb6ff2efdeaa0199c621713c4241" width="1600" height="469" data-path=".assets/images/rooftop-ice-synthetic-data-omniverse/ttn-data.png" />
</Frame>

An integral part of The Things Stack is an MQTT message broker. At this point we can use [any MQTT client to subscribe to topics](https://www.thethingsindustries.com/docs/integrations/mqtt/mqtt-clients/) and create any suitable notification system for the end user. The following is an MQTT client written in Python to demonstrate the principle. Note that the library `paho-mqtt` has been used in a way so that it will block the program execution until two messages have been received. Then it will print the topic and payloads. In a real implementation, it would be better to register a callback and perform some action for each message received.

```
python
# pip install paho-mqtt
import paho.mqtt.subscribe as subscribe

m = subscribe.simple(topics=['#'], hostname="eu1.cloud.thethings.network", port=1883, auth={'username':"icicle-monitor",'password':"NNSXS.V7RI4O2LW3..."}, msg_count=2)
for a in m:
    print(a.topic)
    print(a.payload)
```

```
json
v3/icicle-monitor@ttn/devices/portenta-h7-icicle-00/up
{"end_device_ids":{"device_id":"portenta-h7-icicle-00","application_ids":{"application_id":"icicle-monitor"},"dev_eui":"3036363266398F0D","join_eui":"0000000000000000","dev_addr":"260BED9C"},"correlation_ids":["gs:uplink:01HSKMT8KSZFJ7FB23RGSTJAEA"],"received_at":"2024-03-22T17:54:52.358270423Z","uplink_message":{"session_key_id":"AY5jAnqK0GdPG1yygjCmqQ==","f_port":1,"f_cnt":9,"frm_payload":"AQ==","decoded_payload":{"detected":true},"rx_metadata":[{"gateway_ids":{"gateway_id":"eui-ac1f09fffe09141b","eui":"AC1F09FFFE09141B"},"time":"2024-03-22T17:54:52.382076978Z","timestamp":254515139,"rssi":-51,"channel_rssi":-51,"snr":13.5,"location":{"latitude":67.2951736450195,"longitude":14.4321346282959,"altitude":50,"source":"SOURCE_REGISTRY"},"uplink_token":"CiIKIAoUZXVpLWFjMWYwOWZmZmUwOTE0MWISfCf/+CRQbEMOvrnkaCwjsi/evBhDurYRJILijo5K00mQ=","received_at":"2024-03-22T17:54:52.125610010Z"}],"settings":{"data_rate":{"lora":{"bandwidth":125000,"spreading_factor":7,"coding_rate":"4/5"}},"frequency":"867300000","timestamp":254515139,"time":"2024-03-22T17:54:52.382076978Z"},"received_at":"2024-03-22T17:54:52.154041574Z","confirmed":true,"consumed_airtime":"0.046336s","locations":{"user":{"latitude":67.2951772015745,"longitude":14.43232297897339,"altitude":13,"source":"SOURCE_REGISTRY"}},"version_ids":{"brand_id":"arduino","model_id":"lora-vision-shield","hardware_version":"1.0","firmware_version":"1.2.1","band_id":"EU_863_870"},"network_ids":{"net_id":"000013","ns_id":"EC656E0000000181","tenant_id":"ttn","cluster_id":"eu1","cluster_address":"eu1.cloud.thethings.network"}}}'

v3/icicle-monitor@ttn/devices/portenta-h7-icicle-00/up
{"end_device_ids":{"device_id":"portenta-h7-icicle-00","application_ids":{"application_id":"icicle-monitor"},"dev_eui":"3036363266398F0D","join_eui":"0000000000000000"},"correlation_ids":["as:up:01HSKMTN7F60CC3BQXE06B3Q4X","rpc:/ttn.lorawan.v3.AppAs/SimulateUplink:17b97b44-a5cd-45f0-9439-2de42e187300"],"received_at":"2024-03-22T17:55:05.070404295Z","uplink_message":{"f_port":1,"frm_payload":"AQ==","decoded_payload":{"detected":true},"rx_metadata":[{"gateway_ids":{"gateway_id":"test"},"rssi":42,"channel_rssi":42,"snr":4.2}],"settings":{"data_rate":{"lora":{"bandwidth":125000,"spreading_factor":7}},"frequency":"868000000"},"locations":{"user":{"latitude":67.2951772015745,"longitude":14.43232297897339,"altitude":13,"source":"SOURCE_REGISTRY"}}},"simulated":true}'
```

Observe the difference in the real uplink (first) and simulated uplink (second). In both we find `"decoded_payload":{"detected":true}`.

TTS has a range of [integration options](https://www.thethingsindustries.com/docs/integrations/) for specific platforms, or you could set up a [custom webhook using a standard HTTP/REST](https://www.thethingsindustries.com/docs/integrations/webhooks/) mechanism.

## Limitations

### Weatherproofing

For permanent outdoor installation the device requires a properly sealed enclosure. The camera is mounted on the shield PCB and will need some engineering to be able to see through the enclosure while remaining water tight. For inspiration on how to create weather-proof enclosures that allow sensors and antennas outside access, [see this project](https://www.hackster.io/eivholt/low-power-snow-depth-sensor-using-lora-e5-b8e7b8) on friction fitting and use of rubber washers. The referenced project also proves that battery operated sensors can work with no noticeable degradation in winter conditions (to at least -15 degrees Celcius).

### Obscured view

The project has no safe-guard against false negatives. The device will not report if it's view is blocked. This could be resolved by placing static markers on both sides of an area to monitor and included in synthetic training data. Absence of at least one marker could trigger a notification that the view is obscured.

<Frame caption="Markers to avoid false negatives">
  <img src="https://mintcdn.com/edgeimpulse/Rd2O8sszhA3K-oLX/.assets/images/rooftop-ice-synthetic-data-omniverse/marker.png?fit=max&auto=format&n=Rd2O8sszhA3K-oLX&q=85&s=9724295bb891394c5555b1791b654685" width="1214" height="658" data-path=".assets/images/rooftop-ice-synthetic-data-omniverse/marker.png" />
</Frame>

### Object scale

Due to optimization techniques in Faster Objects - More Objects (FoMo) determining relative sizes of the icicles is not feasible. As even icicles with small mass can be harmful at moderate elevation this is not a crucial feature.

<Frame caption="Object scale">
  <img src="https://mintcdn.com/edgeimpulse/Rd2O8sszhA3K-oLX/.assets/images/rooftop-ice-synthetic-data-omniverse/object-scale.png?fit=max&auto=format&n=Rd2O8sszhA3K-oLX&q=85&s=b4c56ff06c71383894354bd2951236c8" width="1176" height="612" data-path=".assets/images/rooftop-ice-synthetic-data-omniverse/object-scale.png" />
</Frame>

### Exact number of icicles

The object detection model has not been trained to give an exact number of icicles in view. This has no practical implication other than the model verification results appearing worse than practical performance.

<Frame caption="Icicle grouping">
  <img src="https://mintcdn.com/edgeimpulse/Rd2O8sszhA3K-oLX/.assets/images/rooftop-ice-synthetic-data-omniverse/grouping.png?fit=max&auto=format&n=Rd2O8sszhA3K-oLX&q=85&s=f591f2be9da6366638c33113af530cd2" width="1174" height="617" data-path=".assets/images/rooftop-ice-synthetic-data-omniverse/grouping.png" />
</Frame>

### Non-vertical icicles and snow

Icicles can appear bent or angled either due to wind or more commonly due to ice and snow masses slowly dropping over roof edges. The dataset generated in this project does not cover this, but it would not take a lot of effort to extend the domain randomization to rotate or warp the icicles.

<Frame caption="AULSSON\_EBBA">
  <img src="https://mintcdn.com/edgeimpulse/Rd2O8sszhA3K-oLX/.assets/images/rooftop-ice-synthetic-data-omniverse/AULSSON_EBBA.png?fit=max&auto=format&n=Rd2O8sszhA3K-oLX&q=85&s=5f38ece30f9180c1d32282082429a7cc" width="561" height="434" data-path=".assets/images/rooftop-ice-synthetic-data-omniverse/AULSSON_EBBA.png" />
</Frame>

<br />

<Frame caption="Martin Cathrae">
  <img src="https://mintcdn.com/edgeimpulse/Rd2O8sszhA3K-oLX/.assets/images/rooftop-ice-synthetic-data-omniverse/Martin-Cathrae.png?fit=max&auto=format&n=Rd2O8sszhA3K-oLX&q=85&s=178fefcdb52aa8d56f0e3556071c8e9c" width="1465" height="958" data-path=".assets/images/rooftop-ice-synthetic-data-omniverse/Martin-Cathrae.png" />
</Frame>

The training images could benefit from simulating snow with particle effects in Omniverse. The project could also be extended to detect build-up of snow on roofs. For inspiration check out this demo of simulated snow dynamic made in 2014 by Walt Disney Animation Studios for the movie Frozen:

<iframe src="https://www.youtube.com/embed/9H1gRQ6S7gg" title="YouTube video player" className="w-full aspect-video rounded-xl" frameborder="0" allowFullScreen />

### Grayscale

To be able to compile a representation of our neural network and have it run on the severely limited amount of RAM available on the Arduino Portenta H7, pixel representation has been limited to a single channel - grayscale. Colors are not needed to detect icicles so this does not affect the results.

<Frame caption="Grayscale">
  <img src="https://mintcdn.com/edgeimpulse/Rd2O8sszhA3K-oLX/.assets/images/rooftop-ice-synthetic-data-omniverse/grayscale1.png?fit=max&auto=format&n=Rd2O8sszhA3K-oLX&q=85&s=1c229cde4dfc3eb9c119f98683dfd917" width="1029" height="593" data-path=".assets/images/rooftop-ice-synthetic-data-omniverse/grayscale1.png" />
</Frame>

## Further reading

Insights into [how icicles are formed](https://www.insidescience.org/news/riddles-rippled-icicle).


Built with [Mintlify](https://mintlify.com).