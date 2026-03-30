# Source: https://docs.roboflow.com/roboflow/roboflow-ko/deploy/device-manager/setting-up/hardware-requirements.md

# Source: https://docs.roboflow.com/roboflow/roboflow-hi/deploy/device-manager/setting-up/hardware-requirements.md

# Source: https://docs.roboflow.com/deploy/device-manager/setting-up/hardware-requirements.md

# Hardware Requirements

Roboflow Deployment Manager is designed to work most effectively with specific supported hardware. Deployment onto alternative hardware is at your own risk and may not be officially supported.

### Machine Requirements

Before installing Deployment Manager, ensure your device meets these requirements:

* **Root access** — You must have root (sudo) access to the machine
* **Docker Daemon** — Your machine must be able to run Docker. This will be set up by the install script
* **Debian-based OS** — Your machine must be running a recent version of a major Debian-based operating system. Windows and MacOS is not supported.&#x20;
* **No existing Docker containers** — The machine should not have other Docker containers running

### Supported Cameras

Roboflow supports several types of cameras for Deployment Manager; however, compatibility is often limited by environmental conditions, such as networking.&#x20;

* USB Cameras
* RTSP Streams
* Ethernet cameras (Please contact sales for official support)

### Supported Compute Devices

Roboflow Deployment Manager is primary designed to be implemented on Orin based NVIDIA Jetson devices provided by Roboflow. Roboflow also provides limited support for deployment on x86 devices running a recent Debian based operating system with an NVIDIA GPU. Please contact Roboflow sales for the most up-to-date supported compute devices.

### Network Requirements

Edge devices must be hardwired into the network on a dedicated RJ45 CAT6/7 or fiber network drop per deployment.

A typical deployment will also need stable bandwith with the minimums defined below.

| Scenario                                       | Minimum Bandwidth  |
| ---------------------------------------------- | ------------------ |
| Normal operation (monitoring, dataset sync)    | 20 Mbps symmetric  |
| Active Learning & software updates (scheduled) | 200 Mbps symmetric |

### Outbound Traffic

Outbound HTTPS/TLS on **port 443** must be allowed to:

* `api.roboflow.com`
* `repo.roboflow.com`<br>
