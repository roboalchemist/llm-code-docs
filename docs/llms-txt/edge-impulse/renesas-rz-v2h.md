# Source: https://docs.edgeimpulse.com/hardware/boards/renesas-rz-v2h.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Renesas RZ/V2H

The RZ/V2H high-end AI MPU boasts Renesas' proprietary dynamically reconfigurable processor AI accelerator (DRP-AI3), quad Arm® Cortex®-A55 (1.8GHz) Linux processors, and dual Cortex®-R8 (800MHz) real-time processors. Furthermore, the RZ/V2H also includes another dynamically reconfigurable processor (DRP). This processor can accelerate image processing, such as OpenCV, and dynamics calculations required for robotics applications. It also features high-speed interfaces like PCIe®, USB 3.2, and Gigabit Ethernet, making it an ideal microprocessor for applications such as autonomous robots and machine vision in factory automation, where advanced AI processing must be implemented with low power consumption.

The RZ/V2H EVK provides a USB serial interface, 2 channel Ethernet interfaces, four camera interfaces and an HDMI display interface, in addition to many other interfaces (PMOD, microphone, audio output, etc.). The RZ/V2H EVK can be acquired directly through the Renesas website.

<Frame caption="Renesas RZ/V2H">
  <img src="https://mintcdn.com/edgeimpulse/8kB6BRmB5KYHTUny/.assets/images/RZ_V2H.png?fit=max&auto=format&n=8kB6BRmB5KYHTUny&q=85&s=a84466051b586b425a1ca4a785e8d9a6" width="607" height="449" data-path=".assets/images/RZ_V2H.png" />
</Frame>

The Renesas RZ/V2H board realizes hardware acceleration through the DRP-AI IP that consists of a Dynamically Configurable Processor (DRP), and Multiply and Accumulate unit (AI-MAC). The DRP-AI IP is designed to process the entire neural network plus the required pre- and post-processing steps. Additional optimization techniques reduce power consumption and increase processing performance. This leads to high power efficiency and allows using the MPU without a heat sink.

Note that, the DRP-AI is designed for feed-forward neural networks that are usually in vision-based architectures. For more information about the DRP-AI, please [refer to the white paper published by the Renesas team](https://www.renesas.com/eu/en/solution/technologies/ai-accelerator-drp-ai).

The Renesas tool “DRP-AI TVM” is used to translate machine learning models and optimize the processing for DRP-AI. The tool is fully supported by Edge Impulse. This means that machine learning models downloaded from the studio can be directly deployed to the RZ/V2H board.

For more technical information about RZ/V2H, please [refer to the Renesas RZ/V2H documentation](https://www.renesas.com/en/products/microcontrollers-microprocessors/rz-mpus/rzv2h-quad-core-vision-ai-mpu-drp-ai3-accelerator-and-high-performance-real-time-processor) and for the [RZ/V2H-EVK](https://www.renesas.com/en/products/microcontrollers-microprocessors/rz-mpus/rzv2h-evk-rzv2h-quad-core-vision-ai-mpu-evaluation-kit).

### Installing dependencies

#### Yocto image preparation/patch/build for V2H

Renesas provides Yocto build system to build all the necessary packages and create the Linux image. The Renesas documentation calls out that the build system must be based off of Ubuntu 20.04. The following instructions [here](https://renesas-rz.github.io/rzv_ai_sdk/5.00/howto_build_aisdk_v2h.html) outline the necessary steps to setup your build environment.

In order to use the Edge Impulse CLI tools, NodeJS v18 needs to be installed into the yocto image that you build. You will need to download the required NodeJS v18 patch [here](https://cdn.edgeimpulse.com/build-system/nodejs_patches_for_EdgeImpulse_20240805.tar.gz).   Given the instructions called out [here](https://renesas-rz.github.io/rzv_ai_sdk/5.00/howto_build_aisdk_v2h.html), once the following file must be downloaded from Renesas (specific versions specified are required):

```
RTK0EF0180F05000SJ_linux-src.zip
```

After downloaded, you should have these two files in your directory:

```
nodejs_patches_for_EdgeImpulse_20240805.tar.gz
RTK0EF0180F05000SJ_linux-src.zip
```

Next we need to download a specific layer from Edge Impulse to properly setup/install the DRP-AI and TVM SDK.  The zip file for the layer can be downloaded from [here](https://cdn.edgeimpulse.com/build-system/meta-ei.zip). Once downloaded, you will then place the file into the same directory as the RTK0EF0180F05000SJ\_linux-src.zip above.

Next, you will need to create and patch your V2H yocto build environment as follows (this can be exported into a script that can be run):

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
tar zxf rzv2h_ai-sdk_yocto_recipe_v5.00.tar.gz
unzip ./archive/meta-ei.zip
cd $DIR
TEMPLATECONF=$DIR/meta-renesas/meta-rzv2h/docs/template/conf/
export MACHINE=rzv2h-evk-ver1
source poky/oe-init-build-env
cd $DIR/build
bitbake-layers add-layer ../meta-rz-features/meta-rz-graphics
bitbake-layers add-layer ../meta-rz-features/meta-rz-drpai
bitbake-layers add-layer ../meta-rz-features/meta-rz-opencva
bitbake-layers add-layer ../meta-rz-features/meta-rz-codecs
bitbake-layers add-layer ../meta-openembedded/meta-filesystems
bitbake-layers add-layer ../meta-openembedded/meta-networking
bitbake-layers add-layer ../meta-virtualization
bitbake-layers add-layer ../meta-ei
patch -p1 < ../0001-tesseract.patch
cd ${DIR}/meta-openembedded/meta-oe/recipes-devtools/
tar -zxvf ${DIR}/archive/nodejs_patches_for_EdgeImpulse/nodejs_18.17.1.tar.gz
mv nodejs nodejs_12.22.12
ln -s nodejs_18.17.1 nodejs
cd ${DIR}
cd ${DIR}/poky/meta/recipes-support/
tar -zxvf ${DIR}/archive/nodejs_patches_for_EdgeImpulse/icu_70.1.tar.gz
mv icu icu_66.1
ln -s icu_70.1 icu
cd $DIR/build
echo ""                                     >> ./conf/local.conf
echo "IMAGE_INSTALL_append = \" \\"         >> ./conf/local.conf
echo "    nodejs \\"                        >> ./conf/local.conf
echo "    nodejs-npm \\"                    >> ./conf/local.conf
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
#
# Extra image configuration defaults
#
# The EXTRA_IMAGE_FEATURES variable allows extra packages to be added to the generated
# images. Some of these options are added to certain image types automatically. The
# variable can contain the following options:
#  "dbg-pkgs"       - add -dbg packages for all installed packages
#                     (adds symbol information for debugging/profiling)
#  "src-pkgs"       - add -src packages for all installed packages
#                     (adds source code for debugging)
#  "dev-pkgs"       - add -dev packages for all installed packages
#                     (useful if you want to develop against libs in the image)
#  "ptest-pkgs"     - add -ptest packages for all ptest-enabled packages
#                     (useful if you want to run the package test suites)
#  "tools-sdk"      - add development tools (gcc, make, pkgconfig etc.)
#  "tools-debug"    - add debugging tools (gdb, strace)
#  "eclipse-debug"  - add Eclipse remote debugging support
#  "tools-profile"  - add profiling tools (oprofile, lttng, valgrind)
#  "tools-testapps" - add useful testing tools (ts_print, aplay, arecord etc.)
#  "debug-tweaks"   - make an image suitable for development
#                     e.g. ssh root access has a blank password
# There are other application targets that can be used here too, see
# meta/classes/image.bbclass and meta/classes/core-image.bbclass for more details.
#
echo "WHITELIST_GPL-3.0 += \" cpp gcc gcc-dev mpfr g++ cpp make make-dev binutils libbfd \""             >> ./conf/local.conf
echo "IMAGE_INSTALL_append = \" zlib gcc g++ make cpp packagegroup-core-buildessential \""               >> ./conf/local.conf
echo "IMAGE_INSTALL_append = \" python3 python3-pip python3-core python3-modules \""                     >> ./conf/local.conf
echo "IMAGE_INSTALL_append = \" gstreamer1.0 gstreamer1.0-plugins-base gstreamer1.0-plugins-good \""     >> ./conf/local.conf
echo "IMAGE_INSTALL_append = \" gstreamer1.0-plugins-bad gstreamer1.0-plugins-ugly \""                   >> ./conf/local.conf
echo "EXTRA_IMAGE_FEATURES ?= \" debug-tweaks dev-pkgs tools-debug tools-sdk \""                         >> ./conf/local.conf
echo "DISTRO_FEATURES ?= \" usbgadget usbhost wifi opengl \""                                            >> ./conf/local.conf
echo "IMAGE_ROOTFS_EXTRA_SPACE_append_qemuall = \" + 3000000\""                                          >> ./conf/local.conf
#-# glibc2.31 instead of glibc2.28
sed -i 's/^CIP_MODE = "Buster"/CIP_MODE = "Bullseye"/g' ./conf/local.conf
```

You can then invoke your V2H yocto build process via:

```
#!/bin/bash

set -x
DIR=`pwd`
export TEMPLATECONF=$DIR/meta-renesas/meta-rzv2h/docs/template/conf/
export MACHINE=rzv2h-evk-ver1
source poky/oe-init-build-env
time bitbake core-image-weston
```

Renesas documentation [here](https://renesas-rz.github.io/rzv_ai_sdk/5.00/howto_build_aisdk_v2h.html) then shows you different build options + how to flash your compiled images onto your V2H board. Once your build completes, your files that will be used in those subsequent instructions called out [here](https://renesas-rz.github.io/rzv_ai_sdk/5.00/howto_build_aisdk_v2h.html) to flash your V2H board can be found here:

```
#!/bin/bash

DIR=`pwd`
ls -al $DIR/build/tmp/deploy/images/rzv2h-evk-ver1
```

#### Post-flashing tasks

Once your RZ V2H board is running your new image, you will need to complete an additional task.  Please perform the following to setup the DRP-AI and TVM SDK:

```
# cd /usr/drpaitvm
# ./ei_install.sh
```

Your RZ V2H board should now be ready to run an EI model optimized for DRP-AI and TVM!

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

With all software set up, connect your USB camera ([or a supported MIPI CSI camera](https://renesas-rz.github.io/rzv_ai_sdk/5.00/howto_build_aisdk_v2h.html)) to your Renesas board (see 'Next steps' further on this page if you want to connect a different sensor), and run:

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
  <img src="https://mintcdn.com/edgeimpulse/b53JLZcI-O3Jueox/.assets/images/target-renesas-v2h.png?fit=max&auto=format&n=b53JLZcI-O3Jueox&q=85&s=c51848cc99c118d0dd6f7168dee6cd16" width="972" height="126" data-path=".assets/images/target-renesas-v2h.png" />
</Frame>

If you would like to do object detection with Yolov5 (v5) you need to fix the image resolution in the impulse design to **320x320**, otherwise, you might risk that the training fails.

With everything set up you can now build your first machine learning model with these tutorials:

* [Image classification](/tutorials/end-to-end/image-classification).
* [Detect objects using FOMO](/tutorials/end-to-end/object-detection-centroids).

### Deploying back to device

To run your impulse locally, just connect to your Renesas RZ/V2H and run:

```
edge-impulse-linux-runner
```

This will automatically compile your model with full hardware acceleration and download the model to your Renesas board, and then start classifying.

Or you can select the RZ/V2H board from the deployment page, this will download an `eim` model that you can use with the above runner as follows:

Go to the deployment page and select:

<Frame caption="EIM model for the RZ/V2H">
  <img src="https://mintcdn.com/edgeimpulse/BCrJzLAs8FGQ0Eny/.assets/images/rz-v2h-eim.png?fit=max&auto=format&n=BCrJzLAs8FGQ0Eny&q=85&s=476c72f85c999fdf758cb94bf2bc7d2a" width="1426" height="230" data-path=".assets/images/rz-v2h-eim.png" />
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