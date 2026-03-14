# Source: https://docs.edgeimpulse.com/hardware/boards/renesas-rz-v2l.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Renesas RZ/V2L

The Renesas RZ/V2L is a state-of-the-art general-purpose 64-bit Linux MPU with a dual-core ARM Cortex-A55 processor running at 1.2GHz and ARM Mali-G31 3D graphic engine.

The RZ/V2L EVK consists of a SMARC SOM module and an I/O carrier board that provides a USB serial interface, 2 channel Ethernet interfaces, a camera and an HDMI display interface, in addition to many other interfaces (PMOD, microphone, audio output, etc.). The RZ/V2L EVK can be acquired directly through the Renesas website. Since the RZ/V2L is intended for vision AI, the EVK already contains the [Google Coral Camera Module](https://coral.ai/products/camera/).

<Frame caption="Renesas RZ/V2L">
  <img src="https://mintcdn.com/edgeimpulse/8kB6BRmB5KYHTUny/.assets/images/RZ_V2L.png?fit=max&auto=format&n=8kB6BRmB5KYHTUny&q=85&s=25318b6471d373fe99cbf5cbd4df6125" width="673" height="464" data-path=".assets/images/RZ_V2L.png" />
</Frame>

The Renesas RZ/V2L board realizes hardware acceleration through the DRP-AI IP that consists of a Dynamically Configurable Processor (DRP), and Multiply and Accumulate unit (AI-MAC). The DRP-AI IP is designed to process the entire neural network plus the required pre- and post-processing steps. Additional optimization techniques reduce power consumption and increase processing performance. This leads to high power efficiency and allows using the MPU without a heat sink.

Note that, the DRP-AI is designed for feed-forward neural networks that are usually in vision-based architectures. For more information about the DRP-AI, please [refer to the white paper published by the Renesas team](https://www.renesas.com/eu/en/solution/technologies/ai-accelerator-drp-ai).

The Renesas tool “DRP-AI TVM” is used to translate machine learning models and optimize the processing for DRP-AI. The tool is fully supported by Edge Impulse. This means that machine learning models downloaded from the studio can be directly deployed to the RZ/V2L board.

For more technical information about RZ/V2L, please [refer to the Renesas RZ/V2L documentation](https://www.renesas.com/eu/en/products/microcontrollers-microprocessors/rz-mpus/rzv2l-general-purpose-microprocessor-equipped-renesas-original-ai-dedicated-accelerator-drp-ai-12ghz-dual).

### Installing dependencies

#### Yocto image preparation/patch/build for V2L

Renesas provides Yocto build system to build all the necessary packages and create the Linux image. The Renesas documentation calls out that the build system must be based off of Ubuntu 20.04. The following instructions [here](https://www.renesas.com/us/en/document/gde/smarc-evk-rzv2l-linux-start-gude-rev102) outline the necessary steps to setup your build environment.

In order to use the Edge Impulse CLI tools, NodeJS v18 needs to be installed into the yocto image that you build. You will need to download the required NodeJS v18 patch [here](https://cdn.edgeimpulse.com/build-system/nodejs_patches_for_EdgeImpulse_20240805.tar.gz).   Given the instructions called out [here](https://www.renesas.com/us/en/document/gde/smarc-evk-rzv2l-linux-start-gude-rev102), once the following files are downloaded from Renesas (specific versions specified are required):

```
RTK0EF0045Z0024AZJ-v3.0.6.zip
RTK0EF0045Z13001ZJ-v1.2.2_EN.zip
RTK0EF0045Z15001ZJ-v1.2.2_EN.zip
oss_pkg_rzv_drpai_v7.50.7z
```

In addition to the above files, you also need to download the `DRP-AI` package from Renesas' website as well. Please consult this [link](https://www.renesas.com/eu/en/products/microcontrollers-microprocessors/rz-arm-based-high-end-32-64-bit-mpus/rzv2l-drp-ai-support-package#overview) for the software download link. Thus, all of the files needed for the build are:

```
RTK0EF0045Z0024AZJ-v3.0.6.zip
RTK0EF0045Z13001ZJ-v1.2.2_EN.zip
RTK0EF0045Z15001ZJ-v1.2.2_EN.zip
oss_pkg_rzv_drpai_v7.50.7z
r11an0549ej0750-rzv2l-drpai-sp.zip
```

Next, you need to download the NodeJS v18 patch archive [here](https://cdn.edgeimpulse.com/build-system/nodejs_patches_for_EdgeImpulse_20240805.tar.gz).

Next we need to download a specific layer from Edge Impulse to properly setup/install the DRP-AI and TVM SDK.  The zip file for the layer can be downloaded from [here](https://cdn.edgeimpulse.com/build-system/meta-ei.zip). Once downloaded, you will then place the file into the same directory as the RTK0EF0045Z15001ZJ-v1.2.2\_EN.zip above.

After putting all of these files into a single directory + patch file, you will need to create and patch your V2L yocto build environment as follows (this can be exported into a script that can be run):

```
#!/bin/bash

DIR=`pwd`
export TEMPLATECONF=$DIR/meta-renesas/meta-rzv2l/docs/template/conf/
export MACHINE=smarc-rzv2l
# Go to the directory that you have downloaded all of the above files into... then:
mkdir ./archive
mv RTK* oss* r11* ./archive
mv nodejs_patches*gz ./archive
mv meta-ei.zip ./archive
cd ./archive
tar xzpf ./nodejs_patches_for_EdgeImpulse_20240805.tar.gz
cd $DIR
unzip ./archive/RTK0EF0045Z0024AZJ-v3.0.6.zip
unzip ./archive/RTK0EF0045Z13001ZJ-v1.2.2_EN.zip
unzip ./archive/RTK0EF0045Z15001ZJ-v1.2.2_EN.zip
unzip ./archive/r11an0549ej0750-rzv2l-drpai-sp.zip
unzip ./archive/meta-ei.zip
tar zxf ./RTK0EF0045Z0024AZJ-v3.0.6/rzv_vlp_v3.0.6.tar.gz
tar zxf ./RTK0EF0045Z13001ZJ-v1.2.2_EN/meta-rz-features_graphics_v1.2.2.tar.gz
tar zxf ./RTK0EF0045Z15001ZJ-v1.2.2_EN/meta-rz-features_codec_v1.2.2.tar.gz
tar zxf ./rzv2l_drpai-driver/meta-rz-drpai.tar.gz
7z x ./archive/oss_pkg_rzv_drpai_v7.50.7z
cd $DIR/meta-renesas
patch -p1 < ${DIR}/RTK0EF0045Z0024AZJ-v3.0.6/0001-rz-common-recipes-debian-buster-glibc-update-to-v2.2.patch
cd ${DIR}/meta-openembedded/meta-oe/recipes-devtools/
tar -zxvf ${DIR}/archive/nodejs_patches_for_EdgeImpulse/nodejs_18.17.1.tar.gz
mv nodejs nodejs_12.22.12
ln -s nodejs_18.17.1 nodejs
cd ${DIR}
patch -p1 < ${DIR}/archive/nodejs_patches_for_EdgeImpulse/nodejs_18.17.1.bb.patch
cd ${DIR}/poky/meta/recipes-support/
tar -zxvf ${DIR}/archive/nodejs_patches_for_EdgeImpulse/icu_70.1.tar.gz
mv icu icu_66.1
ln -s icu_70.1 icu
cd ${DIR}
patch -p1 < ${DIR}/archive/nodejs_patches_for_EdgeImpulse/icu_70.1.bb.patch
cd ${DIR}
cp ${DIR}/archive/nodejs_patches_for_EdgeImpulse/0002_add_TRUE_FALSE_to_libical-3.0.7_icalrecur.h.patch ${DIR}/poky/meta/recipes-support/libical/libical
patch -p1 < ${DIR}/archive/nodejs_patches_for_EdgeImpulse/libical_3.0.7.bb.patch
source poky/oe-init-build-env build
cd $DIR/build
bitbake-layers add-layer ../meta-qt5
bitbake-layers add-layer ../meta-rz-features/meta-rz-graphics
bitbake-layers add-layer ../meta-rz-features/meta-rz-codecs
bitbake-layers add-layer ../meta-rz-features/meta-rz-drpai
bitbake-layers add-layer ../meta-openembedded/meta-filesystems
bitbake-layers add-layer ../meta-openembedded/meta-networking
bitbake-layers add-layer ../meta-virtualization
bitbake-layers add-layer ../meta-ei
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
echo "    binutils \\"                      >> ./conf/local.conf
echo "    drpaitvm \\"                      >> ./conf/local.conf
echo "    git git-perltools \\"             >> ./conf/local.conf
echo "    \""                               >> ./conf/local.conf
echo ""                                     >> ./conf/local.conf
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

You can then invoke your V2L yocto build process via:

```
#!/bin/bash

DIR=`pwd`
export TEMPLATECONF=$DIR/meta-renesas/meta-rzv2l/docs/template/conf/
export MACHINE=smarc-rzv2l
source poky/oe-init-build-env
time bitbake core-image-weston
```

Renesas documentation [here](https://www.renesas.com/us/en/document/gde/smarc-evk-rzv2l-linux-start-gude-rev102) then shows you different build options + how to flash your compiled images onto your V2L board. Once your build completes, your files that will be used in those subsequent instructions called out [here](https://www.renesas.com/us/en/document/gde/smarc-evk-rzv2l-linux-start-gude-rev102) to flash your V2L board can be found here:

```
#!/bin/bash

DIR=`pwd`
ls -al $DIR/build/tmp/deploy/images/smarc-rzv2l
```

#### Post-flashing tasks

Once your RZ V2L board is running your new image, you will need to complete an additional task.  Please perform the following to setup the DRP-AI and TVM SDK:

```
# cd /usr/drpaitvm
# ./ei_install.sh
```

Your RZ V2L board should now be ready to run an EI model optimized for DRP-AI and TVM!

#### Accessing the board using `screen`

The easiest way is to connect through serial to the RZ/V2L board using the USB mini b port.

1. After connecting the board with a USB-C cable, please power the board with the red power button.
2. Please install `screen` to the host machine and then execute the following command from Linux to access the board:

   ```
   screen /dev/ttyUSB0 115200
   ```
3. You will see the boot process, then you will be asked to log in:
   * Log in with username `root`
   * There is no password

Note that, it should be possible to use an Ethernet cable and log in via SSH if the daemon is installed on the image. However, for simplicity purposes, we do not refer to this one here.

#### Installing Edge Impulse Linux CLI

Once you have logged in to the board, please run the following command to install Edge Impulse Linux CLI

```
npm install edge-impulse-linux -g --unsafe-perm
```

### Connecting to Edge Impulse

With all software set up, connect your google coral camera to your Renesas board (see 'Next steps' further on this page if you want to connect a different sensor), and run:

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

Currently, all Edge Impulse models can run on the RZ/V2L CPU which is a dedicated Cortex A55. In addition, you can bring your own model to Edge Impulse and use it on the device. However, if you would like to benefit from the DRP-AI hardware acceleration support including higher performance and power efficiency, please use one of the following models:

For object detection:

* Yolov5 (v5)
* FOMO (Faster objects More Objects)

For Image classification:

* MobileNet v1, v2

It supports as well models built within the studio using the available layers on the training page.

Note that, on the training page you **have** to select the **target** before starting the training in order to tell the studio that you are training the model for the RZ/V2L. This can be done on the top right in the training page.

<Frame caption="Selecting the target from the training page">
  <img src="https://mintcdn.com/edgeimpulse/b53JLZcI-O3Jueox/.assets/images/target-renesas-v2l.png?fit=max&auto=format&n=b53JLZcI-O3Jueox&q=85&s=d8a5d414ecb3062ede4c389cb3ebfe77" width="351" height="46" data-path=".assets/images/target-renesas-v2l.png" />
</Frame>

If you would like to do object detection with Yolov5 (v5) you need to fix the image resolution in the impulse design to **320x320**, otherwise, you might risk that the training fails.

With everything set up you can now build your first machine learning model with these tutorials:

* [Image classification](/tutorials/end-to-end/image-classification).
* [Detect objects using FOMO](/tutorials/end-to-end/object-detection-centroids).

### Deploying back to device

To run your impulse locally, just connect to your Renesas RZ/V2L and run:

```
edge-impulse-linux-runner
```

This will automatically compile your model with full hardware acceleration and download the model to your Renesas board, and then start classifying.

Or you can select the RZ/V2L board from the deployment page, this will download an `eim` model that you can use with the above runner as follows:

Go to the deployment page and select:

<Frame caption="EIM model for the RZ/V2L">
  <img src="https://mintcdn.com/edgeimpulse/BCrJzLAs8FGQ0Eny/.assets/images/rz-v2l-eim.png?fit=max&auto=format&n=BCrJzLAs8FGQ0Eny&q=85&s=5581508423ca7a4d35f580295fbc0be2" width="547" height="241" data-path=".assets/images/rz-v2l-eim.png" />
</Frame>

Then run the following on the RZ/V2L:

```
edge-impulse-linux-runner --model-file downloaded-model.eim
```

You will see the model inferencing results in the terminal also we stream the results to the local network. This allows you to see the output of the model in real-time in your web browser. Open the URL shown when you start the `runner` and you will see both the camera feed and the classification results.

### DRP-AI library

Since the RZ/V2L benefits from hardware acceleration using the DRP-AI, we provide you with the `drp-ai` library that uses our C++ Edge Impulse SDK and models headers that run on the hardware accelerator. If you would like to integrate the model source code into your applications and benefit from the `drp-ai` then you need to select the `drp-ai` library.

We have an example showing how to use the `drp-ai` library that can be found in [Deploy your model as a DRP-AI library](/hardware/deployments/run-drpai-rzv2l).

<Frame caption="DRP-AI library">
  <img src="https://mintcdn.com/edgeimpulse/FtCF_ajfwASxt-xU/.assets/images/drp-ai-lib.png?fit=max&auto=format&n=FtCF_ajfwASxt-xU&q=85&s=88c0b096be2208f0dc85b48905e80115" width="308" height="196" data-path=".assets/images/drp-ai-lib.png" />
</Frame>


Built with [Mintlify](https://mintlify.com).