# Source: https://docs.edgeimpulse.com/tools/clis/edge-impulse-linux-cli.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Edge Impulse Linux CLI

The Edge Impulse Linux CLI is used for collecting data and running inferences on Linux devices. It is bundled as part of the [Linux Node.js SDK](/tools/libraries/sdks/inference/linux/node-js) and consists of multiple tools:

* [edge-impulse-linux](/tools/clis/edge-impulse-linux-cli#edge-impulse-linux)
* [edge-impulse-linux-runner](/tools/clis/edge-impulse-linux-cli#edge-impulse-linux-runner)

## Installation

<Tabs>
  <Tab title="Linux, Ubuntu, MacOS, and Raspbian OS">
    1. Install [Node.js](https://nodejs.org/en/) v16.x+ or above on your host computer.
       Alternatively, run the following commands:

       ```bash  theme={"system"}
       curl -sL https://deb.nodesource.com/setup_22.x | sudo -E bash -
       sudo apt install -y gcc g++ make build-essential nodejs sox gstreamer1.0-tools gstreamer1.0-plugins-good gstreamer1.0-plugins-base gstreamer1.0-plugins-base-apps
       node -v
       ```

       The last command should return the node version, v16 or above.

       Let's verify the node installation directory:

       ```bash  theme={"system"}
       npm config get prefix
       ```

       If it returns */usr/local/*, run the following commands to change npm's default directory:

       ```bash  theme={"system"}
       mkdir ~/.npm-global
       npm config set prefix '~/.npm-global'
       echo 'export PATH=~/.npm-global/bin:$PATH' >> ~/.profile
       ```

       On MacOS you might be using zsh as default, so you will want to update the correct profile

       ```bash  theme={"system"}
       mkdir ~/.npm-global
       npm config set prefix '~/.npm-global'
       echo 'export PATH=~/.npm-global/bin:$PATH' >> ~/.zprofile
       ```
    2. Install the CLI tools via:

       ```bash  theme={"system"}
       npm install -g edge-impulse-linux
       ```

    You should now have the tools available in your PATH.
  </Tab>

  <Tab title="Windows Subsystem for Linux (WSL)">
    Windows Subsystem for Linux (WSL) allows you to run a Linux environment directly on Windows. This is particularly useful for developers who want to use Linux-based tools and workflows on a Windows machine.

    To install the Edge Impulse CLI using WSL, follow these steps:

    1. Create an [Edge Impulse account](https://studio.edgeimpulse.com/signup).
    2. Install [WSL](https://docs.microsoft.com/en-us/windows/wsl/install) on your Windows machine.

    To install WSL, open PowerShell as an Administrator and run:

    ```bash  theme={"system"}
    wsl --install
    ```

    You can find full instructions on how to install WSL [here](https://docs.microsoft.com/en-us/windows/wsl/install).

    Once complete you can then enable WSL by running the following command in PowerShell as an Administrator:

    ```bash  theme={"system"}
    wsl
    ```

    If you are using WSL, you will need to install the following npm packages, and may need to install audio / video dependencies for your machine:

    e.g. audio dependencies for Ubuntu:

    ```bash  theme={"system"}
    sudo apt-get install libportaudio2 libportaudiocpp0 portaudio19-dev
    ```

    npm route for WSL use administrator user permissions:

    ```bash  theme={"system"}
    sudo apt install -y gcc g++ make build-essential nodejs sox gstreamer1.0-tools gstreamer1.0-plugins-good gstreamer1.0-plugins-base gstreamer1.0-plugins-base-apps
    sudo npm install -g edge-impulse-linux --unsafe-perm
    ```

    Then proceed with installing the Linux CLI:

    ```bash  theme={"system"}
    sudo npm install -g edge-impulse-linux --unsafe-perm
    ```
  </Tab>
</Tabs>

***

## Edge Impulse Linux

```bash  theme={"system"}
edge-impulse-linux --help
```

```
Usage: edge-impulse-linux [options]

Edge Impulse Linux client 1.18.1

Options:
  -V, --version              output the version number
  --api-key <key>            API key to authenticate with Edge Impulse (overrides
                             current credentials)
  --hmac-key <key>           HMAC key to sign new data with (overrides current
                             credentials)
  --disable-camera           Don't prompt for camera
  --disable-microphone       Don't prompt for microphone
  --width <px>               Desired width of the camera stream
  --height <px>              Desired height of the camera stream
  --gst-launch-args <args>   Override the arguments to gst-launch-1.0. This should
                             be a stream that returns JPEG images, e.g.: "v4l2src
                             device=/dev/video0 ! video/x-raw,width=640,height=480
                             ! videoconvert ! jpegenc"
  --clean                    Clear credentials
  --silent                   Run in silent mode, don't prompt for credentials
  --dev                      List development servers, alternatively you can use
                             the EI_HOST environmental variable to specify the Edge
                             Impulse instance.
  --camera <camera>          Which camera to use (either the name, or the device
                             address - e.g. /dev/video0). If this argument is
                             omitted, and multiple cameras are found, a CLI
                             selector is shown.
  --microphone <microphone>  Which microphone to use (either the name, or the
                             device address). If this argument is omitted, and
                             multiple microphones are found, a CLI selector is
                             shown.
  --verbose                  Enable debug logs
  --greengrass               Enable AWS IoT greengrass integration mode
  -h, --help                 output usage information
```

## Edge Impulse Linux Runner

```bash  theme={"system"}
edge-impulse-linux-runner --help
```

```
Usage: edge-impulse-linux-runner [options]

Edge Impulse Linux runner 1.18.1

Options:
  -V, --version                       output the version number
  --model-file <file>                 Specify model file (either path to .eim, or
                                      the socket on which the model is running), if
                                      not provided the model will be fetched from
                                      Edge Impulse
  --api-key <key>                     API key to authenticate with Edge Impulse
                                      (overrides current credentials)
  --download <file>                   Just download the model and store it on the
                                      file system
  --list-targets                      List all supported targets and inference
                                      engines
  --force-target <target>             Do not autodetect the target system, but set
                                      it by hand (e.g. "runner-linux-aarch64")
  --force-engine <engine>             Do not autodetect the inference engine, but
                                      set it by hand (e.g. "tflite")
  --force-variant <variant>           Do not autodetect the model variant, but set
                                      it by hand (e.g. "int8")
  --force-resize-mode <mode>          Do not use the resize method from the
                                      impulse, but set it by hand (valid: "squash",
                                      "fit-shortest" or "fit-longest")
  --impulse-id <impulseId>            Select the impulse ID (if you have multiple
                                      impulses)
  --run-http-server <port>            Do not run using a sensor, but instead expose
                                      an API server at the specified port
  --preview-port <port>               Port to use to render the preview HTTP
                                      interface (default: 4912) (ignored when
                                      running with --run-http-server).
                                      Alternatively you can use the PORT
                                      environmental variable. If both are set then
                                      `--preview-port` takes precedence.
  --preview-host <host>               Host to listen on for the preview HTTP
                                      interface (default: 0.0.0.0) (ignored when
                                      running with --run-http-server).
                                      Alternatively you can use the HOST
                                      environmental variable. If both are set then
                                      `--preview-host` takes precedence.
  --preview-original-resolution       If set, does not resize the preview image to
                                      the impulse resolution
  --monitor                           Enable model monitoring (default: false)
  --monitor-max-storage-size <size>   The maximum storage size to be used for model
                                      monitoring, in MB. Defaults to 250.
  --monitor-summary-interval-ms <ms>  The time interval (in milliseconds) for model
                                      monitoring summaries. Defaults to 60000.
  --clean                             Clear credentials
  --silent                            Run in silent mode, don't prompt for
                                      credentials
  --quantized                         Download int8 quantized neural networks,
                                      rather than the float32 neural networks.
                                      These might run faster on some architectures,
                                      but have reduced accuracy.
  --enable-camera                     Always enable the camera. This flag needs to
                                      be used to get data from the microphone on
                                      some USB webcams.
  --gst-launch-args <args>            Override the arguments to gst-launch-1.0.
                                      This should be a stream that returns JPEG
                                      images, e.g.: "v4l2src device=/dev/video0 !
                                      video/x-raw,width=640,height=480 !
                                      videoconvert ! jpegenc"
  --dev                               List development servers, alternatively you
                                      can use the EI_HOST environmental variable to
                                      specify the Edge Impulse instance.
  --greengrass                        Enable AWS IoT greengrass integration mode
  --dont-print-predictions            If set, suppresses the printing of
                                      predictions
  --thresholds <values>               Override model thresholds. E.g. --thresholds
                                      4.min_anomaly_score=35 overrides the min.
                                      anomaly score for block ID 4 to 35.The
                                      current thresholds are printed on startup.
  --mode <mode>                       Either: "streaming" (runs on a camera/audio
                                      stream and outputs a live inference server)
                                      or "http-server" (opens an HTTP server for
                                      inference on-demand). When passing
                                      --run-http-server XXX in, the mode will
                                      always default to "http-server", in all other
                                      cases the mode defaults to "streaming".
  --camera <camera>                   Which camera to use (either the name, or the
                                      device address - e.g. /dev/video0). If this
                                      argument is omitted, and multiple cameras are
                                      found, a CLI selector is shown.
  --microphone <microphone>           Which microphone to use (either the name, or
                                      the device address). If this argument is
                                      omitted, and multiple microphones are found,
                                      a CLI selector is shown.
  --shm-behavior <mode>               Whether to use shared memory to communicate
                                      between .eim file and Linux runner
                                      (experimental feature), valid: "auto",
                                      "always", "never". If not set, defaults to
                                      'auto' - which will use shm if available, and
                                      fall back to JSON over TCP otherwise. If set
                                      to 'always' will only use shm to communicate
                                      (errors out if not available), if set to
                                      'never' will always use JSON over TCP socket.
  --profiling                         If set, prints profiling info
  --verbose                           Enable debug logs
  -h, --help                          output usage information
```

### Edge Impulse Linux Runner Inter-process Communication Debugging

If you are getting errors with the runner you can get additional debug data. With your EIM model downloaded use two terminals with the following commands to print additional debug data.

Terminal 1:

```
$ ./<path-to-model.eim> /tmp/ei.socket
```

Terminal 2:

```
$ edge-impulse-linux-runner --model-file /tmp/ei.socket
```


Built with [Mintlify](https://mintlify.com).