## Advanced `rpicam-apps`

### Build `libcamera` and `rpicam-apps`

Build `libcamera` and `rpicam-apps` for yourself for the following benefits:

** You can pick up the latest enhancements and features.

** `rpicam-apps` can be compiled with extra optimisation for Raspberry Pi 3 and Raspberry Pi 4 devices running a 32-bit OS.

** You can include optional OpenCV and/or TFLite post-processing stages, or add your own.

** You can customise or add your own applications derived from `rpicam-apps`

#### Remove pre-installed `rpicam-apps`

Raspberry Pi OS includes a pre-installed copy of `rpicam-apps`. Before building and installing your own version of `rpicam-apps`, you must first remove the pre-installed version. Run the following command to remove the `rpicam-apps` package from your Raspberry Pi:

```console
$ sudo apt remove --purge rpicam-apps
```

#### Building `rpicam-apps` without building `libcamera`

To build `rpicam-apps` without first rebuilding `libcamera` and `libepoxy`, install `libcamera`, `libepoxy` and their dependencies with `apt`:

```console
$ sudo apt install -y libcamera-dev libepoxy-dev libjpeg-dev libtiff5-dev libpng-dev libopencv-dev
```

TIP: If you do not need support for the GLES/EGL preview window, omit `libepoxy-dev`.

To use the Qt preview window, install the following additional dependencies:

```console
$ sudo apt install -y qtbase5-dev libqt5core5a libqt5gui5 libqt5widgets5
```

For xref:camera*software.adoc#libav-integration-with-rpicam-vid[`libav`] support in `rpicam-vid`, install the following additional dependencies:

```console
$ sudo apt install libavcodec-dev libavdevice-dev libavformat-dev libswresample-dev
```

If you run Raspberry Pi OS Lite, install `git`:

```console
$ sudo apt install -y git
```

Next, xref:camera*software.adoc#building-rpicam-apps[build `rpicam-apps`].

#### Building `libcamera`

NOTE: Only build `libcamera` from scratch if you need custom behaviour or the latest features that have not yet reached `apt` repositories.

[NOTE]
======
If you run Raspberry Pi OS Lite, begin by installing the following packages:

```console
$ sudo apt install -y python3-pip git python3-jinja2
```
======

First, install the following `libcamera` dependencies:

```console
$ sudo apt install -y libboost-dev
$ sudo apt install -y libgnutls28-dev openssl libtiff5-dev pybind11-dev
$ sudo apt install -y qtbase5-dev libqt5core5a libqt5gui5 libqt5widgets5
$ sudo apt install -y meson cmake
$ sudo apt install -y python3-yaml python3-ply
$ sudo apt install -y libglib2.0-dev libgstreamer-plugins-base1.0-dev
```

Now we're ready to build `libcamera` itself.

Download a local copy of Raspberry Pi's fork of `libcamera` from GitHub:

```console
$ git clone https://github.com/raspberrypi/libcamera.git
```

Navigate into the root directory of the repository:

```console
$ cd libcamera
```

Next, run `meson` to configure the build environment:

```console
$ meson setup build --buildtype=release -Dpipelines=rpi/vc4,rpi/pisp -Dipas=rpi/vc4,rpi/pisp -Dv4l2=true -Dgstreamer=enabled -Dtest=false -Dlc-compliance=disabled -Dcam=disabled -Dqcam=disabled -Ddocumentation=disabled -Dpycamera=enabled
```

NOTE: You can disable the `gstreamer` plugin by replacing `-Dgstreamer=enabled` with `-Dgstreamer=disabled` during the `meson` build configuration. If you disable `gstreamer`, there is no need to install the `libglib2.0-dev` and `libgstreamer-plugins-base1.0-dev` dependencies.

Now, you can build `libcamera` with `ninja`:

```console
$ ninja -C build
```

Finally, run the following command to install your freshly-built `libcamera` binary:

```console
$ sudo ninja -C build install
```

TIP: On devices with 1 GB of memory or less, the build may exceed available memory. Append the `-j 1` flag to `ninja` commands to limit the build to a single process. This should prevent the build from exceeding available memory on devices like the Raspberry Pi Zero and the Raspberry Pi 3.

`libcamera` does not yet have a stable binary interface. Always build `rpicam-apps` after you build `libcamera`.

#### Building `rpicam-apps`

First fetch the necessary dependencies for `rpicam-apps`.

```console
$ sudo apt install -y cmake libboost-program-options-dev libdrm-dev libexif-dev
$ sudo apt install -y meson ninja-build
```

Download a local copy of Raspberry Pi's `rpicam-apps` GitHub repository:

```console
$ git clone https://github.com/raspberrypi/rpicam-apps.git
```

Navigate into the root directory of the repository:

```console
$ cd rpicam-apps
```

For desktop-based operating systems like Raspberry Pi OS, configure the `rpicam-apps` build with the following `meson` command:

```console
$ meson setup build -Denable*libav=enabled -Denable*drm=enabled -Denable*egl=enabled -Denable*qt=enabled -Denable*opencv=disabled -Denable*tflite=disabled -Denable*hailo=disabled
```

For headless operating systems like Raspberry Pi OS Lite, configure the `rpicam-apps` build with the following `meson` command:

```console
$ meson setup build -Denable*libav=disabled -Denable*drm=enabled -Denable*egl=disabled -Denable*qt=disabled -Denable*opencv=disabled -Denable*tflite=disabled -Denable*hailo=disabled
```

[TIP]
======

** Use `-Dneon*flags=armv8-neon` to enable optimisations for 32-bit OSes on Raspberry Pi 3 or Raspberry Pi 4.
** Use `-Denable*opencv=enabled` if you have installed OpenCV and wish to use OpenCV-based post-processing stages.
** Use `-Denable*tflite=enabled` if you have installed TensorFlow Lite and wish to use it in post-processing stages.
** Use `-Denable*hailo=enabled` if you have installed HailoRT and wish to use it in post-processing stages.

======

You can now build `rpicam-apps` with the following command:

```console
$ meson compile -C build
```

TIP: On devices with 1 GB of memory or less, the build may exceed available memory. Append the `-j 1` flag to `meson` commands to limit the build to a single process. This should prevent the build from exceeding available memory on devices like the Raspberry Pi Zero and the Raspberry Pi 3.

Finally, run the following command to install your freshly-built `rpicam-apps` binary:

```console
$ sudo meson install -C build
```

[TIP]
====
The command above should automatically update the `ldconfig` cache. If you have trouble accessing your new `rpicam-apps` build, run the following command to update the cache:

```console
$ sudo ldconfig
```
====

Run the following command to check that your device uses the new binary:

```console
$ rpicam-still --version
```

The output should include the date and time of your local `rpicam-apps` build.

Finally, follow the `dtoverlay` and display driver instructions in the  xref:camera*software.adoc#configuration[Configuration section].

#### `rpicam-apps` meson flag reference

The `meson` build configuration for `rpicam-apps` supports the following flags:

`-Dneon*flags=armv8-neon`: Speeds up certain post-processing features on Raspberry Pi 3 or Raspberry Pi 4 devices running a 32-bit OS.

`-Denable*libav=enabled`: Enables or disables `libav` encoder integration.

`-Denable*drm=enabled`: Enables or disables ***DRM/KMS preview rendering****, a preview window used in the absence of a desktop environment.

`-Denable*egl=enabled`: Enables or disables the non-Qt desktop environment-based preview. Disable if your system lacks a desktop environment.

`-Denable*qt=enabled`: Enables or disables support for the Qt-based implementation of the preview window. Disable if you do not have a desktop environment installed or if you have no intention of using the Qt-based preview window. The Qt-based preview is normally not recommended because it is computationally very expensive, however it does work with X display forwarding.

`-Denable*opencv=enabled`: Forces OpenCV-based post-processing stages to link or not link. Requires OpenCV to enable. Defaults to `disabled`.

`-Denable*tflite=enabled`: Enables or disables TensorFlow Lite post-processing stages. Disabled by default. Requires Tensorflow Lite to enable. Depending on how you have built and/or installed TFLite, you may need to tweak the `meson.build` file in the `post*processing*stages` directory.

`-Denable*hailo=enabled`: Enables or disables HailoRT-based post-processing stages. Requires HailoRT to enable. Defaults to `auto`.

`-Ddownload*hailo*models=true`: Downloads and installs models for HailoRT post-processing stages. Requires `wget` to be installed. Defaults to `true`.

Each of the above options (except for `neon*flags`) supports the following values:

** `enabled`: enables the option, fails the build if dependencies are not available
** `disabled`: disables the option
** `auto`: enables the option if dependencies are available

#### Building `libepoxy`

Rebuilding `libepoxy` should not normally be necessary as this library changes only very rarely. If you do want to build it from scratch, however, please follow the instructions below.

Start by installing the necessary dependencies.

```console
$ sudo apt install -y libegl1-mesa-dev
```

Next, download a local copy of the `libepoxy` repository from GitHub:

```console
$ git clone https://github.com/anholt/libepoxy.git
```

Navigate into the root directory of the repository:

```console
$ cd libepoxy
```

Create a build directory at the root level of the repository, then navigate into that directory:

```console
$ mkdir *build
$ cd *build
```

Next, run `meson` to configure the build environment:

```console
$ meson
```

Now, you can build `libexpoxy` with `ninja`:

```console
$ ninja
```

Finally, run the following command to install your freshly-built `libepoxy` binary:

```console
$ sudo ninja install
```