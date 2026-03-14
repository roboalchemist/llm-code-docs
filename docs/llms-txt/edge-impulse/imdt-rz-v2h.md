# Source: https://docs.edgeimpulse.com/hardware/boards/imdt-rz-v2h.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# IMDT RZ/V2H

IMDT's V2H SBC carrier board transforms the IMDT V2H SoM into a compact, high-performance mini-computer. This fully customizable small form factor SBC features a cost-effective system design ideal for diverse applications in robotics, drones, and smart city projects. The V2H SBC provides a multitude of assembly options, personalized and adjusted to meet specific customer needs, alongside comprehensive onboard connectivity. It presents developers with an energy-efficient solution that occupies minimal space.

The IMDT RZ/V2H SBC provides a USB serial interface, 2 channel Ethernet interfaces, two cameras and an HDMI display interface, in addition to many other interfaces (PMOD, microphone, audio output, etc.). The RZ/V2H EVK can be acquired directly through the Renesas website.

<Frame caption="IMDT RZ/V2H">
  <img src="https://mintcdn.com/edgeimpulse/x9Ga-7v4NxdQ7jXX/.assets/images/imdt-rz-v2h.png?fit=max&auto=format&n=x9Ga-7v4NxdQ7jXX&q=85&s=3845f8b21708d6cb8a809f6458021e65" width="621" height="392" data-path=".assets/images/imdt-rz-v2h.png" />
</Frame>

The IMDT RZ/V2H board realizes hardware acceleration through the DRP-AI IP that consists of a Dynamically Configurable Processor (DRP), and Multiply and Accumulate unit (AI-MAC). The DRP-AI IP is designed to process the entire neural network plus the required pre- and post-processing steps. Additional optimization techniques reduce power consumption and increase processing performance. This leads to high power efficiency and allows using the MPU without a heat sink.

Note that, the DRP-AI is designed for feed-forward neural networks that are usually in vision-based architectures. For more information about the DRP-AI, please [refer to the white paper published by the Renesas team](https://www.renesas.com/eu/en/solution/technologies/ai-accelerator-drp-ai).

The Renesas tool “DRP-AI TVM” is used to translate machine learning models and optimize the processing for DRP-AI. The tool is fully supported by Edge Impulse. This means that machine learning models downloaded from the studio can be directly deployed to the RZ/V2H board.

For more technical information about the RZ/V2H, please [refer to the Renesas RZ/V2H documentation](https://www.renesas.com/en/products/microcontrollers-microprocessors/rz-mpus/rzv2h-quad-core-vision-ai-mpu-drp-ai3-accelerator-and-high-performance-real-time-processor) and for the [IMDT RZ/V2H SBC](https://www.imd-tec.com/products/v2h-sbc).

### Installing dependencies

#### Yocto image preparation/patch/build for IMDT V2H

Renesas provides Yocto build system to build all the necessary packages and create the Linux image. The Renesas documentation calls out that the build system must be based off of Ubuntu 20.04. The following instructions [here](https://renesas-rz.github.io/rzv_ai_sdk/5.00/howto_build_aisdk_v2h.html) outline the necessary steps to setup your build environment.

In order to use the Edge Impulse CLI tools, NodeJS v18 needs to be installed into the yocto image that you build. You will need to download the required NodeJS v18 patch [here](https://cdn.edgeimpulse.com/build-system/nodejs_patches_for_EdgeImpulse_20240805.tar.gz). The following file needs to be downloaded from Renesas (specific versions specified are required):

```
RTK0EF0180F04000SJ_linux-src.zip
```

After downloaded, you should have these two files in your directory:

```
nodejs_patches_for_EdgeImpulse_20240805.tar.gz
RTK0EF0180F04000SJ_linux-src.zip
```

Next we need to download a specific layer from Edge Impulse to properly setup/install the DRP-AI and TVM SDK.  The zip file for the layer can be downloaded from [here](https://cdn.edgeimpulse.com/build-system/meta-ei.zip). Once downloaded, you will then place the file into the same directory as the RTK0EF0180F04000SJ\_linux-src.zip above.

Next, you will need to create and patch your IMDT V2H yocto build environment as follows (this can be exported into a script that can be run):

```
#!/bin/bash

set -x
DIR=`pwd`
# Go to the directory that you have downloaded all of the above files into... then:
mkdir ./archive
mv RTK* ./archive
mv nodejs_patches*gz ./archive
mv meta-ei.zip ./archive
cd ./archive
tar xzpf ./nodejs_patches_for_EdgeImpulse_20240805.tar.gz
cd $DIR
unzip ./archive/RTK0EF0180F05000SJ_linux-src.zip
unzip ./archive/meta-ei.zip
tar xzpf ./rzv2h_ai-sdk_yocto_recipe_v4.00.tar.gz
mv ./meta-rz-features $DIR
cd $DIR
repo init -u https://github.com/imd-tec/imdt-renesas-manifest.git -b imdt-linux-dunfell -m imdt-v2h-bsp-v2.0.0.xml
repo sync
export TEMPLATECONF=${DIR}/sources/meta-imdt-renesas/docs/template/conf/
export MACHINE='imdt-v2h-sbc'
cd $DIR
source sources/poky/oe-init-build-env
bitbake-layers add-layer ../sources/meta-openembedded/meta-filesystems
bitbake-layers add-layer ../sources/meta-openembedded/meta-networking
bitbake-layers add-layer ../sources/meta-virtualization
bitbake-layers add-layer ../meta-rz-features/meta-rz-graphics
bitbake-layers add-layer ../meta-rz-features/meta-rz-codecs
bitbake-layers add-layer ../meta-ei
cd $DIR
cp archive/0002_add_TRUE_FALSE_to_libical-3.0.7_icalrecur.h.patch $DIR/sources/poky/meta/recipes-support/libical/libical
cp archive/libical*bb $DIR/sources/poky/meta/recipes-support/libical/
cd $DIR/sources/poky/meta/recipes-support
rm -rf icu 2>&1 1> /dev/null
cp -r $DIR/archive/icu_70.1 icu
cd $DIR/sources/meta-openembedded/meta-oe/recipes-devtools
rm -rf nodejs 2>&1 1> /dev/null
cp -r $DIR/archive/nodejs_18.17.1 nodejs
cp $DIR/archive/packagegroup-qt5.bb ./meta-renesas/meta-rz-common/dynamic-layers/qt5-layer/packagegroups/
cd $DIR/build
echo ""                                     >> ./conf/local.conf
echo "IMAGE_INSTALL_append = \" \\"         >> ./conf/local.conf
echo "    nodejs \\"                        >> ./conf/local.conf
echo "    nodejs-npm \\"                    >> ./conf/local.conf
echo "    e2fsprogs-resize2fs \\"           >> ./conf/local.conf
echo "    \""                               >> ./conf/local.conf
echo ""                                     >> ./conf/local.conf

echo ""                                     >> ./conf/local.conf
echo "IMAGE_INSTALL_append = \" \\"         >> ./conf/local.conf
echo "    nvme-cli \\"                      >> ./conf/local.conf
echo "    sudo \\"                          >> ./conf/local.conf
echo "    curl \\"                          >> ./conf/local.conf
echo "    zlib \\"                          >> ./conf/local.conf
echo "    drpaitvm \\"                      >> ./conf/local.conf
echo "    binutils \\"                      >> ./conf/local.conf
echo "    \""                               >> ./conf/local.conf
echo ""                                     >> ./conf/local.conf

echo "WHITELIST_GPL-3.0 += \" cpp gcc gcc-dev mpfr g++ cpp make make-dev binutils libbfd \""                >> ./conf/local.conf
echo "IMAGE_INSTALL_append = \" zlib gcc g++ make cpp packagegroup-core-buildessential e2fsprogs-mke2fs \"" >> ./conf/local.conf
echo "IMAGE_INSTALL_append = \" python3 python3-pip python3-core python3-modules \""                        >> ./conf/local.conf
echo "IMAGE_INSTALL_append = \" gstreamer1.0 gstreamer1.0-plugins-base gstreamer1.0-plugins-good \""        >> ./conf/local.conf
echo "IMAGE_INSTALL_append = \" gstreamer1.0-plugins-bad gstreamer1.0-plugins-ugly \""                      >> ./conf/local.conf
echo "EXTRA_IMAGE_FEATURES ?= \" debug-tweaks dev-pkgs tools-debug tools-sdk \""                            >> ./conf/local.conf
echo "DISTRO_FEATURES ?= \" virtualization usbgadget usbhost wifi opengl systemd \""                        >> ./conf/local.conf
echo "IMAGE_ROOTFS_EXTRA_SPACE_append_qemuall = \" + 6000000\""                                             >> ./conf/local.conf

#-# glibc2.31 instead of glibc2.28
sed -i 's/^CIP_MODE = "Buster"/CIP_MODE = "Bullseye"/g' ./conf/local.conf
```

You can then invoke your IMDT V2H yocto build process via:

```
#!/bin/bash

set -x
DIR=`pwd`
export MACHINE='imdt-v2h-sbc'
export TEMPLATECONF=${DIR}/sources/meta-imdt-renesas/docs/template/conf/
cd $DIR
source sources/poky/oe-init-build-env
time bitbake imdt-image-weston
```

IMDT's Github documentation [here](https://github.com/imd-tec/meta-imdt-renesas) then shows you different build options. Once your build completes, your files that will be used in those subsequent instructions called out [here](https://github.com/imd-tec/meta-imdt-renesas) to flash your V2H board can be found here:

```
#!/bin/bash

DIR=`pwd`
ls -al $DIR/build/tmp/deploy/images/imdt-v2h-sbc
```

#### Flash the board

The easiest way to flash and boot the board is through the use of an SD card.  The above files from your yocto build contain a "wic" file that can be imaged onto a SD card via popular utilities like [Balena Etcher](https://etcher.balena.io/).

#### Post-flashing tasks

Once your IMDT board is running your new image, you will need to complete an additional task.  Please perform the following to setup the DRP-AI and TVM SDK:

```
# cd /usr/drpaitvm
# ./ei_install.sh
```

Your IMDT board should now be ready to run an EI model optimized for DRP-AI and TVM!

#### Accessing the board using `screen`

The easiest way is to connect through serial to the RZ/V2H board using the USB mini b port.

1. After connecting the board with a USB-C cable, please power the board.
2. Power on the board: Connect the power cable to the board, switch `SW3` ON then `SW2` ON.
3. Please install `screen` to the host machine and then execute the following command from Linux to access the board:

   ```
   screen /dev/ttyUSB0 115200
   ```
4. You will see the boot process, then you will be asked to log in:
   * Log in with username `root`
   * There is no password

Note that, it should be possible to use an Ethernet cable and log in via SSH if the daemon is installed on the image. However, for simplicity purposes, we do not refer to this one here.

#### Installing Edge Impulse Linux CLI

Once you have logged in to the board, please run the following command to install Edge Impulse Linux CLI

```
npm install edge-impulse-linux -g --unsafe-perm
```

### Connecting to Edge Impulse

With all software set up, run:

```
edge-impulse-linux
```

This will start a wizard which will ask you to log in and choose an Edge Impulse project. If you want to switch projects run the command with `--clean`.

#### Verifying that your device is connected

That's all! Your device is now connected to Edge Impulse. To verify this, go to [your Edge Impulse project](https://studio.edgeimpulse.com/studio/profile/projects), and click **Devices**. The device will be listed here.

<Frame caption="Device connected to Edge Impulse.">
  <img src="https://mintcdn.com/edgeimpulse/rTWxVUHegAMX0AbN/.assets/images/renesas_mpu.png?fit=max&auto=format&n=rTWxVUHegAMX0AbN&q=85&s=1e9ceeee97dc9da30586d0fdb83109df" width="1600" height="164" data-path=".assets/images/renesas_mpu.png" />
</Frame>

### Next steps: building a machine learning model

Currently, all Edge Impulse models can run on the RZ/V2H CPU which is a dedicated Cortex A55. In addition, you can bring your own model to Edge Impulse and use it on the device. However, if you would like to benefit from the DRP-AI3 hardware acceleration support including higher performance and power efficiency, please use one of the following models:

For object detection:

* Yolov5 (v5)
* FOMO (Faster objects More Objects)

For Image classification:

* MobileNet v1, v2

It supports as well models built within the studio using the available layers on the training page.

Note that, on the training page you **have** to select the **target** before starting the training in order to tell the studio that you are training the model for the RZ/V2H. This can be done on the top right in the training page.

<Frame caption="Selecting the target from the training page">
  <img src="https://mintcdn.com/edgeimpulse/b53JLZcI-O3Jueox/.assets/images/target-imdt-v2h.png?fit=max&auto=format&n=b53JLZcI-O3Jueox&q=85&s=1967d7f96683daacc4432b751d64d9c3" width="789" height="416" data-path=".assets/images/target-imdt-v2h.png" />
</Frame>

If you would like to do object detection with Yolov5 (v5) you need to fix the image resolution in the impulse design to **320x320**, otherwise, you might risk that the training fails.

With everything set up you can now build your first machine learning model with these tutorials:

* [Image classification](/tutorials/end-to-end/image-classification).
* [Detect objects using FOMO](/tutorials/end-to-end/object-detection-centroids).

### Deploying back to device

To run your impulse locally, just connect to your IMDT RZ/V2H and run:

```
edge-impulse-linux-runner
```

This will automatically compile your model with full hardware acceleration and download the model to your Renesas board, and then start classifying.

Or you can select the RZ/V2H board from the deployment page, this will download an `eim` model that you can use with the above runner as follows:

Go to the deployment page and select:

<Frame caption="EIM model for the IMDT RZ/V2H">
  <img src="https://mintcdn.com/edgeimpulse/x9Ga-7v4NxdQ7jXX/.assets/images/imdt-rz-v2h-eim.png?fit=max&auto=format&n=x9Ga-7v4NxdQ7jXX&q=85&s=62521e869dd7715795b1961fae6f897b" width="1237" height="442" data-path=".assets/images/imdt-rz-v2h-eim.png" />
</Frame>

Then run the following on the RZ/V2H:

```
edge-impulse-linux-runner --model-file downloaded-model.eim
```

You will see the model inferencing results in the terminal also we stream the results to the local network. This allows you to see the output of the model in real-time in your web browser. Open the URL shown when you start the `runner` and you will see both the camera feed and the classification results.

### DRP-AI TVM i8 library

Since the RZ/V2H benefits from hardware acceleration using the DRP-AI, we provide you with the `drp-ai-tvm-i8` library that uses our C++ Edge Impulse SDK, DRP-AI TVM and models headers that run on the hardware accelerator. If you would like to integrate the model source code into your applications and benefit from the DRP-AI then you need to select the `drp-ai-tvm-i8` library.

We have an example showing how to use the `drp-ai-tvm-i8` library that can be found in [Deploy your model as a DRP-AI TVM i8 library](/hardware/deployments/run-drpai-rzv2h).

<Frame caption="DRP-AI TVM i8 library">
  <img src="https://mintcdn.com/edgeimpulse/s8dsOgJvVXspqLe-/.assets/images/renesas-rz-v2h/drp-ai-tvm-i8.png?fit=max&auto=format&n=s8dsOgJvVXspqLe-&q=85&s=49b8aba0fce352b6d4320f88dd728d48" width="1200" height="686" data-path=".assets/images/renesas-rz-v2h/drp-ai-tvm-i8.png" />
</Frame>


Built with [Mintlify](https://mintlify.com).