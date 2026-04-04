# Source: https://docs.edgeimpulse.com/projects/expert-network/zededa-model-monitoring.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Deploying Edge Impulse Models on ZEDEDA Cloud Devices

Created By: Attila Tokes

## Introduction

With increasing fleet sizes, managing edge devices and applications becomes increasingly harder. This introduces the necessity for device management platforms such as [ZEDEDA](https://zededa.com/), which allow orchestrating large number of edge devices and applications with ease. Applications also need to be packaged in a more structured way, allowing deploying and updating them in a more automated manner.

This project shows how we can package and deploy [Edge Impulse](https://edgeimpulse.com/) based Machine Learning (ML) applications on devices managed by the ZEDEDA Cloud platform.

<Frame caption="Overview">
  <img src="https://mintcdn.com/edgeimpulse/Y4Lfo5IVCYFA4G8k/.assets/images/zededa-model-monitoring/overview.png?fit=max&auto=format&n=Y4Lfo5IVCYFA4G8k&q=85&s=5648192d4ad13c6900023ea436d22d79" width="909" height="533" data-path=".assets/images/zededa-model-monitoring/overview.png" />
</Frame>

A Raspberry Pi 4 single-board computer will be used as our example Edge Device. On the Raspberry Pi 4 we will install EVE OS, then we will provision it into the ZEDEDA Cloud platform.

Our Edge Impulse model will be packaged as a containerized application based on the [EI Impulse Runner](/tools/clis/edge-impulse-cli/impulse-runner). The containerized application then will be imported into the ZEDEDA platform as an Edge App, from where and it will be deployed to the Edge Device.

Finally, we will show a quick preview on how the experimental Model Monitoring features can be used to monitor Edge Impulse models running on production devices.

## Edge Impulse

In this project we will focus on deploying Image / Video based Edge Impulse projects on ZEDEDA Cloud devices. We can use an existing Edge Impulse project, or create a new one.

For this demo, I created a simple object detection project. First, I collected a couple of images with a mug, a glass and a Raspberry Pi 4:

<Frame caption="Data Acquisition">
  <img src="https://mintcdn.com/edgeimpulse/Y4Lfo5IVCYFA4G8k/.assets/images/zededa-model-monitoring/08-01-ei-data-acq.png?fit=max&auto=format&n=Y4Lfo5IVCYFA4G8k&q=85&s=2667d4de541eed5bbf66a384d4346b3b" width="1582" height="1000" data-path=".assets/images/zededa-model-monitoring/08-01-ei-data-acq.png" />
</Frame>

Then the target objects in the collected images were manually labeled in the *Data acquisition* section in Edge Impulse Studio. The dataset was then split into train and test sets.

Then, I set up an Impulse implementing Object Detection for our target objects:

<Frame caption="Create Impulse">
  <img src="https://mintcdn.com/edgeimpulse/Y4Lfo5IVCYFA4G8k/.assets/images/zededa-model-monitoring/08-02-ei-impulse.png?fit=max&auto=format&n=Y4Lfo5IVCYFA4G8k&q=85&s=c78cc0168c1da1db7107e30c3867a05a" width="1600" height="995" data-path=".assets/images/zededa-model-monitoring/08-02-ei-impulse.png" />
</Frame>

The Impulse I used is a simple one, and uses the standard Object Detection processing block with the default parameters. Different Impulse architectures can also be used, as it makes little difference on how we will package our EI application later in this project.

After we train our Impulse, we can can test its basic functionality with Live classification on a supported device. If everything is good, the Impulse should be ready to be used in an edge application.

In order to access the trained Impulse from ZEDEDA Cloud / EVE OS devices we will need an API Key from the Edge Impulse Studio. We can get this from the **Dashboard -> Keys** section:

<Frame caption="API Key">
  <img src="https://mintcdn.com/edgeimpulse/Y4Lfo5IVCYFA4G8k/.assets/images/zededa-model-monitoring/08-03-api-key.png?fit=max&auto=format&n=Y4Lfo5IVCYFA4G8k&q=85&s=3122b16ad932f687d0a4a58654496869" width="1600" height="685" data-path=".assets/images/zededa-model-monitoring/08-03-api-key.png" />
</Frame>

From here, copy the API Key's value with the `ei_...` format.

## ZEDEDA

The [ZEDEDA Cloud](https://zededa.com/) is a SaaS platform offering among others, orchestration and management services of edge device and applications directly from the Cloud. ZEDEDA works with fully managed Edge Devices, to which one or more Edge Applications can be seamlessly deployed.

In this project we will show how an Edge Impulse ML model can be deployed on a ZEDEDA managed edge devices.

<Frame caption="Add project">
  <img src="https://mintcdn.com/edgeimpulse/Y4Lfo5IVCYFA4G8k/.assets/images/zededa-model-monitoring/ei-on-zededa.png?fit=max&auto=format&n=Y4Lfo5IVCYFA4G8k&q=85&s=e399808f91f89440c00906309c117a91" width="1024" height="497" data-path=".assets/images/zededa-model-monitoring/ei-on-zededa.png" />
</Frame>

For the purpose of the demo we will use a Raspberry Pi 4 as our ZEDEDA Edge Node. The Edge Impulse ML model, also known as an Impulse, will be deployed to the platform as an Edge App. Additionally, the new experimental Model Monitoring features will be used to inspect the live running AI model directly from Edge Impulse Studio.

Hardware used:

* a Raspberry Pi 4 Model B, with at least 2GB of RAM
* a microSD card with at least 8GB capacity
* wired LAN connection with Internet access
* an IP camera or an USB webcam
* (optional) an HDMI display and micro-HDMI to HDMI cable - these are only needed to view the debug output of EVE-OS

### Installing EVE-OS on a Raspberry Pi 4

Edge Nodes managed by the ZEDEDA cloud platform must run [EVE-OS](https://lfedge.org/projects/eve/), which is light-weight, open-source Linux distribution designed to run containerized or VM-based workloads. In this section we will show how to install EVE-OS on a Raspberry Pi 4.

To install EVE-OS we need to generate and flash an SD Card image. This can be done using the [lfedge/eve](https://hub.docker.com/r/lfedge/eve) tool which is packaged as a Docker container.

The default settings create an EVE-OS image intended for production use. In case we are using a demo / trial account with ZEDEDA Cloud, we need to prepare a small customization to point the EVE-OS installation to the ZEDEDA Demo server. This can be done as bellow:

```sh  theme={"system"}
$ mkdir "$HOME/eve-overrides-demo"
$ echo zedcloud.gmwtus.zededa.net > "$HOME/eve-overrides-demo/server"
```

With this we are ready to generate an EVE-OS image by running the following command:

```sh  theme={"system"}
$ docker run -v "$HOME/eve-overrides-demo:/in" --rm lfedge/eve:latest-arm64 live > ./live.img

...
b5171159-734b-4254-9930-2c35239d3858     # <-- this is an uniquely generated soft serial number
```

The command produces a `live.img` file with our EVE-OS image. Along with this, there is uniquely generated soft serial number printed as the last line of the output. Make sure to note this, as it will be needed later in the provisioning step.

The resulting `live.img` should be a regular disk image file, and can flashed to a microSD card using [Balena Etcher](https://etcher.balena.io/) or similar tools.

After the SD card is flashed we can insert it into the Raspberry Pi 4. EVE OS should boot automatically. In case we have a HDMI display connected we will see some message with EVE-OS trying to connect to ZEDEDA Cloud.

### Creating an ZEDEDA Cloud Project

With the Raspberry Pi 4 running EVE-OS, we can start setting up things in the ZEDEDA Cloud platform.

The first thing we need in ZEDEDA Cloud is a Project. To create it we go to [Administration -> Projects](https://zedcontrol.gmwtus.zededa.net/administration/projects/list) and click on *Add Project*:

<Frame caption="Projects page">
  <img src="https://mintcdn.com/edgeimpulse/Y4Lfo5IVCYFA4G8k/.assets/images/zededa-model-monitoring/01-01-projects.png?fit=max&auto=format&n=Y4Lfo5IVCYFA4G8k&q=85&s=a27f7e65b7cd0fa971e911e0619214b3" width="1600" height="985" data-path=".assets/images/zededa-model-monitoring/01-01-projects.png" />
</Frame>

Next, give a name to the project and select the "Deployment" type:

<Frame caption="Add project">
  <img src="https://mintcdn.com/edgeimpulse/Y4Lfo5IVCYFA4G8k/.assets/images/zededa-model-monitoring/01-02-add-project.png?fit=max&auto=format&n=Y4Lfo5IVCYFA4G8k&q=85&s=42c7c15c3cb66452b248dee80905f7a3" width="1600" height="810" data-path=".assets/images/zededa-model-monitoring/01-02-add-project.png" />
</Frame>

On the Deployments and Policies pages we can use the same name:

<Frame caption="Add project / Deployments">
  <img src="https://mintcdn.com/edgeimpulse/Y4Lfo5IVCYFA4G8k/.assets/images/zededa-model-monitoring/01-03-add-project-deployments.png?fit=max&auto=format&n=Y4Lfo5IVCYFA4G8k&q=85&s=36fb07a126c4eec307d48682883e9a24" width="1600" height="808" data-path=".assets/images/zededa-model-monitoring/01-03-add-project-deployments.png" />
</Frame>

...While keeping the rest of the options as default:

<Frame caption="Add project / Policies">
  <img src="https://mintcdn.com/edgeimpulse/Y4Lfo5IVCYFA4G8k/.assets/images/zededa-model-monitoring/01-04-add-project-policies.png?fit=max&auto=format&n=Y4Lfo5IVCYFA4G8k&q=85&s=4c08b057fcc6f2cd0e5b4b127816e954" width="1600" height="805" data-path=".assets/images/zededa-model-monitoring/01-04-add-project-policies.png" />
</Frame>

Lastly, we can review our inputs and hit *Next* to create our project:

<Frame caption="Add project / Review">
  <img src="https://mintcdn.com/edgeimpulse/Y4Lfo5IVCYFA4G8k/.assets/images/zededa-model-monitoring/01-05-add-project-review.png?fit=max&auto=format&n=Y4Lfo5IVCYFA4G8k&q=85&s=374e119fc31712e29c85882dd0826897" width="1600" height="806" data-path=".assets/images/zededa-model-monitoring/01-05-add-project-review.png" />
</Frame>

After the project is created, our Projects list should look something like this:

<Frame caption="View Project">
  <img src="https://mintcdn.com/edgeimpulse/Y4Lfo5IVCYFA4G8k/.assets/images/zededa-model-monitoring/01-06-project.png?fit=max&auto=format&n=Y4Lfo5IVCYFA4G8k&q=85&s=0733b0dbaa720d2671190ef1247de7b3" width="1600" height="224" data-path=".assets/images/zededa-model-monitoring/01-06-project.png" />
</Frame>

### Configuring a Network

Before being able to onboard the Raspberry Pi 4 we will need to configure a network for the Edge Nodes to use. For this go to [Library -> Networks](https://zedcontrol.gmwtus.zededa.net/library/networks/list) and click *Add Network*.

<Frame caption="Networks">
  <img src="https://mintcdn.com/edgeimpulse/Y4Lfo5IVCYFA4G8k/.assets/images/zededa-model-monitoring/02-01-networks.png?fit=max&auto=format&n=Y4Lfo5IVCYFA4G8k&q=85&s=a98d4307ea84d6b07ef0d8c6c3c12ce7" width="1600" height="891" data-path=".assets/images/zededa-model-monitoring/02-01-networks.png" />
</Frame>

Here, add a new IPv4 network with an arbitrary name, DHCP client mode, and 1500 MTU:

<Frame caption="Add Networks">
  <img src="https://mintcdn.com/edgeimpulse/Y4Lfo5IVCYFA4G8k/.assets/images/zededa-model-monitoring/02-02-add-network.png?fit=max&auto=format&n=Y4Lfo5IVCYFA4G8k&q=85&s=ec0408ad79ec7a84bf2874bae5612b44" width="1600" height="607" data-path=".assets/images/zededa-model-monitoring/02-02-add-network.png" />
</Frame>

The newly added network should appear in the networks list:

<Frame caption="Networks">
  <img src="https://mintcdn.com/edgeimpulse/Y4Lfo5IVCYFA4G8k/.assets/images/zededa-model-monitoring/02-03-networks.png?fit=max&auto=format&n=Y4Lfo5IVCYFA4G8k&q=85&s=27b3db01c8e27f35d9bcd54740a729bf" width="1600" height="211" data-path=".assets/images/zededa-model-monitoring/02-03-networks.png" />
</Frame>

### Onboarding the Raspberry Pi 4 to ZEDEDA Cloud

At this point we should be ready to onboard our Raspberry Pi 4 into ZEDEDA Cloud.

If this is our first Edge Node we first need to import a supported hardware model from the ZEDEDA Marketplace. For this go to [MarketPlace -> Models](https://zedcontrol.gmwtus.zededa.net/marketplace/models/list), and in the Global Models section find a import the **RPi4-4G** model:

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Y4Lfo5IVCYFA4G8k/.assets/images/zededa-model-monitoring/03-00-import-rpi4.png?fit=max&auto=format&n=Y4Lfo5IVCYFA4G8k&q=85&s=fd829eabb98aeb900973bb1963f14f79" width="1261" height="807" data-path=".assets/images/zededa-model-monitoring/03-00-import-rpi4.png" />
</Frame>

Next, go to the [Edge Nodes](https://zedcontrol.gmwtus.zededa.net/edge-nodes/list) page, and click *Add Edge Node*.

Here we should give a name to the new node, and select our previously created Project and Deployment Tag:

<Frame caption="Add Edge Node">
  <img src="https://mintcdn.com/edgeimpulse/Y4Lfo5IVCYFA4G8k/.assets/images/zededa-model-monitoring/03-01-add-edge-node.png?fit=max&auto=format&n=Y4Lfo5IVCYFA4G8k&q=85&s=13ab4239ea2c03a06563a4a96e039282" width="1600" height="882" data-path=".assets/images/zededa-model-monitoring/03-01-add-edge-node.png" />
</Frame>

In the Details sections, select *Onboarding Key* as the Identity Type. Set the Onboarding Key to `5d0767ee-0547-4569-b530-387e526f8cb9`, which is the default key for all projects. In the Serial Number field enter the unique serial number we got earlier at the generate EVE OS image step. For the Brand and Model select *RaspberryPi* and *RPi-4G*.

In the Port Mapping section set `eth0` as a Management interface, with our previously created Network attached to it. The `wlan0` network can be left unused, while the USB port can be set as *App Direct* (we will not use them).

<Frame caption="Add Edge Node (cont)">
  <img src="https://mintcdn.com/edgeimpulse/Y4Lfo5IVCYFA4G8k/.assets/images/zededa-model-monitoring/03-02-add-edge-node-cont.png?fit=max&auto=format&n=Y4Lfo5IVCYFA4G8k&q=85&s=388457f4de4736e6bbe53e1e22bdcdd6" width="1600" height="879" data-path=".assets/images/zededa-model-monitoring/03-02-add-edge-node-cont.png" />
</Frame>

In the *Additional Configuration* section we can check both activation options.

After we click Next, the onboarding of the Edge Node will start. During the onboarding, if we have an HDMI screen connected to the Raspberry Pi, we should see some console activity showing the device is trying to onboard to the ZEDEDA cloud platform.

The onboarding process can take a couple of minutes, after which we should find that our Edge Node comes online:

<Frame caption="Edge Nodes">
  <img src="https://mintcdn.com/edgeimpulse/Y4Lfo5IVCYFA4G8k/.assets/images/zededa-model-monitoring/03-03-node-list.png?fit=max&auto=format&n=Y4Lfo5IVCYFA4G8k&q=85&s=092d801fa42515895285189ff11fb556" width="1600" height="238" data-path=".assets/images/zededa-model-monitoring/03-03-node-list.png" />
</Frame>

In the Edge Node's page we can find various details and metrics:

<Frame caption="Edge Node Metrics">
  <img src="https://mintcdn.com/edgeimpulse/Y4Lfo5IVCYFA4G8k/.assets/images/zededa-model-monitoring/03-04-node-online.png?fit=max&auto=format&n=Y4Lfo5IVCYFA4G8k&q=85&s=5a0af40c326a633e138e439a4a53bb1e" width="1553" height="820" data-path=".assets/images/zededa-model-monitoring/03-04-node-online.png" />
</Frame>

## Deploying the Edge Impulse Project to ZEDEDA

In this section we will show how we can deploy Edge Impulse models as an Edge App into the ZEDEDA platform.

EVE OS and the ZEDEDA platform supports running applications based either on Containers or Virtual Machines (VM). In this project we will build and deploy our Edge Impulse model as a Container-based Edge App.

### Preparing a Container Image

Edge Impulse already packages the EI Runner as a Docker container. We can use this as a base of our Container image, over which we can apply customizations.

Customizations can range from running EI Runner parameters to run in different modes (ex. API server vs. live inference), to adding startup scripts or implementing custom applications.

For this demo project, I added the following customizations to the base Docker image:

1. A set of GStreamer plugins was added to be able to use RTSP Camera as our video source.
   *(note: this was needed as ZEDEDA / EVE OS does not seems to support USB cameras with the Raspberry Pi)*
2. A entry point script was added, which can start the EI Impulse Runner with custom parameters

The final `Dockerfile` looks like this:

```docker  theme={"system"}
FROM aureleq/ei-inference-container

ARG DEBIAN_FRONTEND=noninteractive

RUN ln -snf /usr/share/zoneinfo/Europe/Bucharest /etc/localtime && echo Europe/Bucharest > /etc/timezone

RUN apt update -y && apt install -y gstreamer1.0-tools gstreamer1.0-plugins-good gstreamer1.0-plugins-base gstreamer1.0-plugins-base-apps gstreamer1.0-libav && apt dist-upgrade -y && apt autoremove -y && apt autoclean -y

ADD app.sh /app/app.sh
```

The `app.sh` is a script used as the container's entry point. It can start the Edge Impulse runner in two possible modes:

1. HTTP Server mode - starts an inference server on port `1337` - this exposes the EI model as an API to be used by other applications
2. RTSP Camera mode, with Model Monitoring - starts the EI Runner with a RTSP Camera as the video source, and the experimental Model Monitoring features enabled

The script also accepts an EI API Key, and a custom Device Name:

```sh  theme={"system"}
#!/bin/bash

MODE="$1"
EI_API_KEY="$2"
DEVICE_NAME="$3"

echo "Mode: $MODE"
echo "EI API Key: $EI_API_KEY"

if [[ "$MODE" == "http-server" ]]; then
    echo "Running EI runner in HTTP server mode..."
    node /app/linux/node/build/cli/linux/runner.js --api-key "${EI_API_KEY}" --run-http-server 1337 --impulse-id 1

elif [[ "$MODE" == "gst-model-monitoring" ]]; then
    echo "Running EI runner with GStreamer sources + Model monitoring..."
    while true; do
       echo "${DEVICE_NAME}" | node /app/linux/node/build/cli/linux/runner.js --clean --silent --monitor --api-key "${EI_API_KEY}" --verbose --enable-camera --gst-launch-args "rtspsrc location=rtsp://<RTSP-CAM-IP>:8554/stream ! rtph264depay ! avdec_h264 ! videoconvert ! jpegenc" || true;
       echo "Runner stopped! Restarting it..."
    done
else
    echo "Unknown mode!"
    exit 1;
fi
```

To be able to use this container image in ZEDEDA Cloud, we need to make it available in a container repository. I used a private Docker Hub repository for this purpose. The image was built and published as follows:

```sh  theme={"system"}
$ docker buildx build . --platform linux/arm64 --tag attitokes/zededa-test:edge-impulse-in-docker-0.1.0 --load
$ docker push attitokes/zededa-test:edge-impulse-in-docker-0.1.0
```

### Configuring the Container Registry and Adding the Container Image

As we will use a slightly modified container image, we will need a container registry that we can attach to ZEDEDA Cloud. To attach a container registry to ZEDEDA Cloud, go to [Library -> Data Stores](https://zedcontrol.gmwtus.zededa.net/library/data-stores/list), and hit `+` to create a new data store.

<Frame caption="Configure Container Registry">
  <img src="https://mintcdn.com/edgeimpulse/Y4Lfo5IVCYFA4G8k/.assets/images/zededa-model-monitoring/04-01-docker-io-data-store.png?fit=max&auto=format&n=Y4Lfo5IVCYFA4G8k&q=85&s=d09f79073a2dde9c33c7966337c29f10" width="1600" height="830" data-path=".assets/images/zededa-model-monitoring/04-01-docker-io-data-store.png" />
</Frame>

Give it a name, and select *Container Registry* as the Category. I used Docker Hub, for which we should set `docker://docker.io` as the FQDN. Select the type of Container, and enter a Docker IO user name and API key.

After this we should be able to import our container image into ZEDEDA. For this go to [Library -> Edge App Images](https://zedcontrol.gmwtus.zededa.net/library/images/app/list), and click `+` to add a new image:

<Frame caption="Add Container Image">
  <img src="https://mintcdn.com/edgeimpulse/Y4Lfo5IVCYFA4G8k/.assets/images/zededa-model-monitoring/04-02-add-image.png?fit=max&auto=format&n=Y4Lfo5IVCYFA4G8k&q=85&s=e1a09235c2c5410ea2313a9204742534" width="1600" height="586" data-path=".assets/images/zededa-model-monitoring/04-02-add-image.png" />
</Frame>

Here, select the newly added Data Store, specify the image URL using the `/<username>/<image>:<tag>` format.

### Creating and Edge App

With this we are ready to package our EI model as an ZEDEDA Edge App. For this go to [Marketplace -> Edge Apps](https://zedcontrol.gmwtus.zededa.net/marketplace/edge-apps/local/list), and create a new edge app. Select *Container* as the application type.

<Frame caption="Add Edge App">
  <img src="https://mintcdn.com/edgeimpulse/Y4Lfo5IVCYFA4G8k/.assets/images/zededa-model-monitoring/05-01-add-edge-app.png?fit=max&auto=format&n=Y4Lfo5IVCYFA4G8k&q=85&s=0ed0fce14eec4e192d50f1bf250b3e0a" width="1600" height="776" data-path=".assets/images/zededa-model-monitoring/05-01-add-edge-app.png" />
</Frame>

In the *Add Edge App* page give the application a name, and select *Standalone* as the Deployment Type. For *Resources*, Tiny or Small should be enough.

<Frame caption="Edge App Image">
  <img src="https://mintcdn.com/edgeimpulse/Y4Lfo5IVCYFA4G8k/.assets/images/zededa-model-monitoring/05-02-edge-app-image.png?fit=max&auto=format&n=Y4Lfo5IVCYFA4G8k&q=85&s=c0cbfaf1aad2d539e0ee6a5c830773cd" width="1538" height="305" data-path=".assets/images/zededa-model-monitoring/05-02-edge-app-image.png" />
</Frame>

In the *Drives* section, select the Edge App Image we created previously.

Then, in the *Networking* section we need to configure an Outbound rule that allows any traffic:

<Frame caption="Edge App | Networking">
  <img src="https://mintcdn.com/edgeimpulse/Y4Lfo5IVCYFA4G8k/.assets/images/zededa-model-monitoring/05-03-edge-app-networking.png?fit=max&auto=format&n=Y4Lfo5IVCYFA4G8k&q=85&s=11a64c6cfcc355ea4a76edcf941891a6" width="1525" height="863" data-path=".assets/images/zededa-model-monitoring/05-03-edge-app-networking.png" />
</Frame>

Additionally, if we want to use the HTTP server, we also need to expose the `1337` port to the outside world.

In the *Configurations*, enable the custom edge app configuration as follows:

<Frame caption="Edge App | Configurations">
  <img src="https://mintcdn.com/edgeimpulse/Y4Lfo5IVCYFA4G8k/.assets/images/zededa-model-monitoring/05-04-edge-app-configuration.png?fit=max&auto=format&n=Y4Lfo5IVCYFA4G8k&q=85&s=958dce46e527410a6f66a55143fff177" width="1529" height="283" data-path=".assets/images/zededa-model-monitoring/05-04-edge-app-configuration.png" />
</Frame>

This will allow us to inject settings like the Device name and Edge Impulse API Key later when we deploy the Edge App to the Raspberry Pi 4.

On the Developer Info section, fill in the necessary details, and click *Add* to create the Edge App.

<Frame caption="Edge App | Developer Info">
  <img src="https://mintcdn.com/edgeimpulse/Y4Lfo5IVCYFA4G8k/.assets/images/zededa-model-monitoring/05-05-edge-app-devinfo.png?fit=max&auto=format&n=Y4Lfo5IVCYFA4G8k&q=85&s=ab0e668829be43de9953ef1a55e7b8a4" width="1541" height="435" data-path=".assets/images/zededa-model-monitoring/05-05-edge-app-devinfo.png" />
</Frame>

### Deploying the Edge App to the Raspberry Pi 4

With the Edge App created, we should be able deploy it to our Raspberry Pi 4 Edge Node. To do this go to the [Edge App Instances](https://zedcontrol.gmwtus.zededa.net/edge-app-instances/list) section, and use the `+` button to create a new deployment:

In the first page select the Raspberry Pi 4 Edge Node to deploy to:

<Frame caption="Edge App Deployment">
  <img src="https://mintcdn.com/edgeimpulse/Y4Lfo5IVCYFA4G8k/.assets/images/zededa-model-monitoring/06-01-edge-app-instance.png?fit=max&auto=format&n=Y4Lfo5IVCYFA4G8k&q=85&s=6737e90420248f59be18213c319788e4" width="1544" height="944" data-path=".assets/images/zededa-model-monitoring/06-01-edge-app-instance.png" />
</Frame>

Then, in the next page, give the app instance a name:

<Frame caption="Edge App Deployment | Identity">
  <img src="https://mintcdn.com/edgeimpulse/Y4Lfo5IVCYFA4G8k/.assets/images/zededa-model-monitoring/06-02-edge-app-identity.png?fit=max&auto=format&n=Y4Lfo5IVCYFA4G8k&q=85&s=af09ae84f9eeebeca727a9fd8fec8636" width="1551" height="946" data-path=".assets/images/zededa-model-monitoring/06-02-edge-app-identity.png" />
</Frame>

In the next page, the Networking settings should be already pre-populated with the correct adapter, so we can go the next page:

<Frame caption="Edge App Deployment | Networking">
  <img src="https://mintcdn.com/edgeimpulse/Y4Lfo5IVCYFA4G8k/.assets/images/zededa-model-monitoring/06-03-edge-app-networking.png?fit=max&auto=format&n=Y4Lfo5IVCYFA4G8k&q=85&s=6264f2acc6a98cbac239760665f414d5" width="1544" height="943" data-path=".assets/images/zededa-model-monitoring/06-03-edge-app-networking.png" />
</Frame>

On the next page we need to configure the settings for our Edge App instance. Here we can specify a Device Name and our Edge Impulse API Key as follows:

<Frame caption="Edge App Deployment | Configuration">
  <img src="https://mintcdn.com/edgeimpulse/Y4Lfo5IVCYFA4G8k/.assets/images/zededa-model-monitoring/06-04-edge-app-configuration.png?fit=max&auto=format&n=Y4Lfo5IVCYFA4G8k&q=85&s=f2adf5b3438b56047285c95f4a7311fb" width="1552" height="947" data-path=".assets/images/zededa-model-monitoring/06-04-edge-app-configuration.png" />
</Frame>

For this use the following configuration:

```
EVE_ECO_CMD="/app/app.sh gst-model-monitoring <EI_API KEY> <DEVICE_NAME>"
```

Finally, we can review and deploy the app:

<Frame caption="Edge App Deployment">
  <img src="https://mintcdn.com/edgeimpulse/Y4Lfo5IVCYFA4G8k/.assets/images/zededa-model-monitoring/06-05-edge-app-deploy.png?fit=max&auto=format&n=Y4Lfo5IVCYFA4G8k&q=85&s=307cf87719a31ee68db584c8c60f2894" width="1554" height="942" data-path=".assets/images/zededa-model-monitoring/06-05-edge-app-deploy.png" />
</Frame>

It takes a couple of minutes until the container image is fully downloaded, a volume is created and the app is booted. During this time the Edge App Instance will go through various states, and in the end it should come online:

<Frame caption="Edge App Deployment">
  <img src="https://mintcdn.com/edgeimpulse/Y4Lfo5IVCYFA4G8k/.assets/images/zededa-model-monitoring/06-06-edge-app-online.png?fit=max&auto=format&n=Y4Lfo5IVCYFA4G8k&q=85&s=6e05ce1b0063dc1ddaea17026fcdf5b8" width="1600" height="892" data-path=".assets/images/zededa-model-monitoring/06-06-edge-app-online.png" />
</Frame>

## Edge Impulse Model Monitoring

Managing large fleets of Edge Devices can get complex. The ZEDEDA Cloud solves this by offering a centralized platform that makes managing Edge Devices and Apps easy.

The ZEDEDA platform however does not have insights on what our Edge Apps are actually doing. With Edge ML applications it is particularly important to get insights about our model's performance in the real world.

Up until recently, in Edge Impulse implementing monitoring of production Edge ML apps was left to the users.

Now, Edge Impulse is working on a new set of [Model Monitoring](https://edgeimpulse.com/industrial-new-features) features, meant to enable deployment and monitoring of EdgeML apps.

With Model Monitoring enabled on our ZEDEDA Edge App we can benefit from the following features:

1. New devices running the Edge App are automatically populated in the Devices tab in EI Studio.
2. Using Live Inference we can monitor / debug the AI models running on the Edge Device in real-time.
3. We can push a new model version to the Edge Devices, without the need to restart or redeploy the Edge App.

The Model Monitoring features are still experimental, but here is a quick demo on how Live Inference currently looks in the Edge Impulse Studio:

<Frame caption="Edge App Deployment">
  <img src="https://mintcdn.com/edgeimpulse/Y4Lfo5IVCYFA4G8k/.assets/images/zededa-model-monitoring/07-01-model-monitoring.gif?s=19e842491695ff8cd6189af4baf6240d" width="800" height="505" data-path=".assets/images/zededa-model-monitoring/07-01-model-monitoring.gif" />
</Frame>

## Conclusions

The ZEDEDA platform allows managing and orchestrating large number of edge devices and applications from a centralized platform. It provides visibility and control over the edge devices deployed in the field directly from the cloud. Its zero-trust security model ensures device integrity, and allows secure communication of edge apps with the cloud.

Packaging Edge Impulse models into container-based edge apps allow deploying them to multiple devices with ease. Using the EI Impulse Runner in various modes allows launching models and integrating them with external applications and data sources in flexible ways. Additionally, the new set of model monitoring features will allow monitoring edge models deployed in the real world and collecting data from them in real-time.

These features make the combination of the ZEDEDA and Edge Impulse platforms a great solution for deploying edge ML applications to large fleets of edge devices.


Built with [Mintlify](https://mintlify.com).