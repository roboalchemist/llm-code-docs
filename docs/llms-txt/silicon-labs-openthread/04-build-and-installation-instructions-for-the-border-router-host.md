# Source: https://docs.silabs.com/openthread/3.0.0/using-sl-coprocessors-with-openthread-border-router/04-build-and-installation-instructions-for-the-border-router-host.md

# Build and Installation Instructions for the Border Router Host

> **Note**: The same Thread host works with both RCP and NCP architectures. The host automatically detects whether it is communicating with an RCP or NCP device and switches its operating mode accordingly.

## Install the Hardware

Connect each Wireless Starter Kit main board and the host computer to an Ethernet switch with an Ethernet cable as shown in the following figure. These connections will permit programming and network analysis of the Co-Processor and end devices. Optionally, end devices may be connected to the host computer by USB rather than Ethernet. To connect Raspberry Pi Border Router with a Co-Processor over SPI, you can either hardwire the SPI pins with WSTK's expansion connector or you can use wireless expansion board (brd8016), which mounts on the top of Raspberry Pi.

![diagram](/using-sl-coprocessors-with-openthread-border-router/0.1/images/sld1037-image11.png)

### Hardwire SPI Connections Between Raspberry Pi and WSTK

Connect the SPI pins as shown below:

|Raspberry Pi Connector (SPI Pins)|WPK’s Expansion Connector (brd4002)|
|---|---|
|GPIO10 / Pin19 (MOSI)|Pin 4|
|GPIO9 / Pin21 (MISO)|Pin 6|
|GPIO11 / Pin23 (SCLK)|Pin 8|
|GPIO7/8 / Pin24/26 (CS0/CS1)|Pin 10|
|GPIO21 / Pin40 (Interrupt line)|Pin 7|
|GND / Pin 6|Pin 1|
|GPIO20 / Pin38 (Reset line)|Pin F4 on breakout connector|

![photo](/using-sl-coprocessors-with-openthread-border-router/0.1/images/sld1037-image12.jpg)

### Wireless Expansion Board for SPI Connections Between Raspberry Pi and WSTK

You can also use a [wireless expansion board](https://www.silabs.com/documents/public/user-guides/ug291-exp4320a-user-guide.pdf), which mounts on the top of Raspberry Pi to avoid hardwire connection, as shown below.

![photo](/using-sl-coprocessors-with-openthread-border-router/0.1/images/sld1037-image13.jpg)

> **Note**: Use correct OTBR_AGENT_OPTS as described in section [OTBR Configurations using SPI Interface](#otbr-configurations-using-spi-interface) depending on the SPI connections.

## Install and Configure a Raspberry Pi for Use with a Co-Processor

Two different methods for installing the OTBR software in a Raspberry Pi for use with a Co-Processor are:

- Manual installation
- Docker container

### Manual Installation

This guide covers how to build the OTBR using the tools provided by the Silicon Labs Simplicity SDK. You may also install the OTBR using the instructions detailed at [https://openthread.io/guides/border-router/build](https://openthread.io/guides/border-router/build). Note that this is a different build option, and either guide may be followed to build the OTBR.

For the manual setup, use the included version of the ot-br-posix in the Silicon Labs SDK:

```C
openthread_stack/util/third_party/ot-br-posix
```

You can find the Thread specification for a selected SDK under openthread_stack/util/third_party/openthread/README.md. If you have already downloaded the SDK as part of Simplicity Studio, skip the following step.

Begin by cloning the Simplicity SDK repository:

```C
git clone https://github.com/SiliconLabsSoftware/sisdk-release.git*
```

Check out the desired SDK branch. For this guide, we use the default branch.

In the openthread_stack/util/third_party/ot-br-posix directory run:

```C
sudo ./script/bootstrap
```

After running the bootstrap step, make sure to check out the right version of the openthread stack in third_party/openthread/repo by either copying or creating a symbolic link to the OpenThread stack:

```C
openthread_stack/util/third_party/ot-br-posix/third_party/openthread/repo -> openthread_stack/util/third_party/openthread
```

Make sure that the git commit under third_party/openthread/repo is supported by the release. Refer to the OpenThread Release Notes for the stable commits supported by a given release.

To use Silicon Labs-specific configuration settings for border router, you can grab the special configuration header hosted in the
SDK under **<sdk_location>/openthread/platform-abstraction/posix/openthread-core-silabs-posix-config.h.**

> **Note**: This configuration header overrides a lot of settings to recommended values from the certifiable OTBR configuration. Go over the configuration file to check any settings specific to your scenario.

Run the setup as follows:

```C
# Copy the config file to a known include path

sudo cp <sdk_location>/openthread/platform-abstraction/posix/openthread-core-silabs-posix-config.h <sdk_location>/openthread_stack/util/third_party/openthread/src/posix/platform/

# Run the setup by specifying the above config header

# Adjust your infrastructure link name appropriately, such as eth0 for Ethernet or wlan0 for WiFi

# (or whatever your link is named)

sudo INFRA_IF_NAME=eth0 OTBR_OPTIONS="-DOT_PLATFORM_CONFIG=openthread-core-silabs-posix-config.h -DOTBR_DUA_ROUTING=ON -DOTBR_DHCP6_PD=ON " ./script/setup
```

To build OTBR with SPI interface, include the `-DOT_POSIX_RCP_SPI_BUS=ON` flag in `OTBR_OPTIONS`.

Refer to `openthread/src/core/config` and `openthread/examples/README.md` for compile-time constants and cmake build options, respectively.

> **Note**: Prior to GSDK 4.4.0 the build flag for the OTBR SPI Interface was: `-DOT_POSIX_CONFIG_RCP_BUS=SPI`.

> **Note**: For SDK 7.x and lower, users must clone the Gecko SDK repository. For more information, please visit [https://github.com/SiliconLabs/gecko_sdk](https://github.com/SiliconLabs/gecko_sdk).

### OTBR Configurations Using UART Interface

- Configure the desired tty* port to use for the OTBR to connect your Co-Processor at startup. Look for the tty* port of the Co-Processor device. The easiest way to do this is to look for a `/tty/dev…` entry once the device is connected. It should generally either be `/dev/ttyUSB0` or `/dev/ttyACM0`.
- Edit the `/etc/default/otbr-agent` file and look for the `OTBR_AGENT_OPTS` configuration. Include the tty* port name in that parameter as follows:  
  ```C  
  OTBR_AGENT_OPTS="-I wpan0 spinel+hdlc+uart:///dev/ttyACM0"  
  ```
- If running a Backbone Border Router (Thread protocol version 1.2 or above), add the backbone interface as follows:  
  ```C  
  OTBR_AGENT_OPTS="-I wpan0 -B eth0 spinel+hdlc+uart:///dev/ttyACM0"  
  ```
- If running a Thread 1.3 or greater Border Router, specify the Thread Radio Encapsulation Link (TREL) interface to enable Thread over Infrastructure links as follows:

```C
OTBR_AGENT_OPTS="-I wpan0 -B eth0 spinel+hdlc+uart:///dev/ttyACM0 trel://eth0"
```

#### UART Baud Rate Settings

- By default, OTBR agent (the host daemon) is built to work with a baud rate of 460800. We recommend this configuration for a lot of realistic OTBR deployment scenarios.  Please make sure your Co-Processor and WSTK/WPK/STK adapter are configured accordingly.
- If you wish to change the default baud rate, we recommend that you update the radio URL options:

For example, to lower the baud rate to 115200:

```C
OTBR_AGENT_OPTS="-I wpan0 spinel+hdlc+uart:///dev/ttyACM0?uart-baudrate=115200 trel://eth0"
```

If intending to change this value, you _must_ also match the correct baud rate on the adapter board by issuing the following command on the admin console of the Co-Processor WSTK/WPK/STK adapter:

> serial vcom config speed 115200 (optional if you have updated adapter firmware that will autosense this rate)

Make sure to also set the correct baud rate in your Co-Processor project in the IO STREAM USART or IO STREAM EUSART component as shown in the following figure:

![screenshot](/using-sl-coprocessors-with-openthread-border-router/0.1/images/sld1037-image14.png)

- To verify the baud rate in use, issue the command:  
  ```C  
  stty -F /dev/ttyACM0  
  ```

### OTBR Configurations using SPI Interface

- Configure the desired SPI ports to use for the OTBR to connect your Co-Processor at startup. Ensure the SPI interface is enabled on the Raspberry Pi. If not:
- Enable it by adding following in /boot/config.txt  
  ```C  
  dtparam=spi=on  
  dtoverlay=disable-bt    #Maybe not required  
  ```
- Remove/comment `dtoverlay=spi0-1cs`,`cs0_pin=26` if it is defined in /boot/config.txt.
- Reboot the Raspberry Pi.
- Use this command to validate the SPI port `ls /dev | grep spi`.
- Two devices should be visible, `spidev0.0` and `spidev0.1`, depending on your Raspberry Pi version.
- Edit the `/etc/default/otbr-agent` file and look for the OTBR_AGENT_OPTS configuration. Include the correct GPIOs in that parameter as per the hardware setup in sections [Hardwire SPI Connections Between Raspberry Pi and WSTK](#hardwire-spi-connections-between-raspberry-pi-and-wstk) and [Wireless Expansion Board for SPI Connections Between Raspberry Pi and WSTK](#wireless-expansion-board-for-spi-connections-between-raspberry-pi-and-wstk).
- Use the following parameters if Raspberry Pi is hardwired to SPI pins on WSTK’s expansion connector. Use spidev0.0 if using Raspberry Pi’s CS0 or replace to spidev0.1 for CS1 pin.

```C
   OTBR_AGENT_OPTS="-I wpan0 -B eth0 spinel+spi:///dev/spidev0.0?gpio-int-device=/dev/gpiochip0&gpio-int-line=21&gpio-reset-device=/dev/gpiochip0&gpio-reset-line=20&no-reset=1&spi-speed=1000000"
```

- Use the following parameters if the radio board is mounted on Raspberry Pi using wireless expansion board (brd8016A).

```C
   OTBR_AGENT_OPTS="-I wpan0 -B eth0 spinel+spi:///dev/spidev0.0?gpio-int-device=/dev/gpiochip0&gpio-int-line=22&gpio-reset-device=/dev/gpiochip0&gpio-reset-line=23&no-reset=1&spi-speed=1000000"
```

- If using custom hardware connections, make sure to provide respective GPIOs pins.
- Start `otbr-agent` service by either rebooting the Raspberry Pi or issue `> sudo systemctl restart otbr-agent`.
- Issue the `> sudo ot-ctl state` command on the Raspberry Pi to see the status of the connection between the host and Co-Processor.
- Check whether all required services are running on the OTBR.  
  `sudo systemctl status` should not report any services as running in a “degraded” state.
- Check `/var/log/syslog` for a running log of otbr-agent.

### OTBR Configuration for CSL

When running OTBR as a CSL transmitter, OTBR can sometimes fail to transmit CSL packets with the error `Handle transmit done failed: Abort`. This can happen if `OPENTHREAD_CONFIG_MAC_CSL_REQUEST_AHEAD_US` is set too low.

The default SiLabs POSIX config header includes a recommended value (5000) for this parameter. When building your OTBR from the instructions in [Manual Installation](#manual-installation), make sure to use the latest `openthread-core-silabs-posix-config.h`.

If building the OTBR on your own using the instructions on the OpenThread website, then either:

- Modify the value of `OPENTHREAD_CONFIG_MAC_CSL_REQUEST_AHEAD_US` in `ot-br-posix/third_party/openthread/repo/src/core/config/mac.h`  
  or
- Include the configuration flag `-DCMAKE_CXX_FLAGS='-DOPENTHREAD_CONFIG_MAC_CSL_REQUEST_AHEAD_US=5000'` under `OTBR_OPTIONS`.

### Installation Guidance

- Starting with GSDK 4.2.0, Silicon Labs OpenThread Border Router uses the OpenThread-based NAT64 implementation, which automatically sets up a NAT64 prefix for address translation purposes. See the example at [https://openthread.io/guides/border-router/docker/test-connectivity](https://openthread.io/guides/border-router/docker/test-connectivity).

Silicon Labs does not recommend using the default NAT configuration on a network using 192.168.x.x addresses because that NAT uses those addresses by default on the NAT64 interface.

- For properly resolving mDNS queries, make sure the "**hosts:**" line under **/etc/nsswitch.conf** looks like the following:  
  `hosts:          files mdns4 minimal mdns5 minimal dns`
- For Thread 1.2 backbone routing and Thread 1.3 and 1.4 features, the onboard OTBR processes manage IPv6 prefixes and routing, so dhcpcd management of ipv6 should be disabled.

Check that the following lines are present in **/etc/dhcpcd.conf:**

```C
noipv6
noipv6rs
```

### OTBR Status

- Issue the `> sudo ot-ctl state` command on your Raspberry Pi to see the status of the connection between the host and Co-Processor.
- Check whether all required services are running on the OTBR.  
  `sudo systemctl status` should not report any services as running in a “degraded” state.
- Check `/var/log/syslog` for a running log of otbr-agent.

### Using ot-ctl to Configure and Control the OpenThread Border Router

For a full command list, run:

```C
> sudo ot-ctl help
```

Refer to [https://openthread.io/guides/border-router/external-commissioning](https://openthread.io/guides/border-router/external-commissioning) for examples on how to manually set up a Thread Network and examples on how to enable an external commissioner.

Run these two commands to check for a running Thread Network:

```C
> sudo ot-ctl state
```

and

```C
> sudo ot-ctl ifconfig
```

> **Note**: The error message OpenThread Daemon is not running indicates a problem with the Co-Processor connection. Check both for a valid /dev/tty entry and that a valid Co-Processor application was flashed onto the device.

### OTBR Feature Configuration for Certification

For information on how to properly configure OpenThread Border Router features and services, visit [https://openthread.io/guides/border-router](https://openthread.io/guides/border-router#features_and_services).

The following flags are recommended for an OTBR **Device Under Test (DUT)** for Thread Certification:

See [Manual Installation](#manual-installation) for instructions on obtaining Silicon Labs-specific configuration settings (`openthread-core-silabs-posix-config.h`) for border router.

```C
sudo RELEASE=1 NAT64=1 BORDER_ROUTING=1 DHCPV6_PD=0 REFERENCE_DEVICE=0 BACKBONE_ROUTER=1 WEB_GUI=0 ./script/bootstrap

sudo INFRA_IF_NAME=eth0 RELEASE=1 REFERENCE_DEVICE=0 BACKBONE_ROUTER=1 BORDER_ROUTING=1 NAT64=1 DHCPV6_PD=0 WEB_GUI=0 REST_API=0 OTBR_OPTIONS="-DOT_THREAD_VERSION=1.4 -DOT_PLATFORM_CONFIG=openthread-core-silabs-posix-config.h -DOTBR_DUA_ROUTING=ON -DOTBR_DHCP6_PD=ON" ./script/setup
```

OTBR supports a reference implementation of DHCPv6 Prefix Delegation client using the flag `DHCPV6_PD_REF=1` which can be passed to both commands above. This utilizes PD implementation using external utilities like dhcpcd and radvd. Border router products may have their own implementation of this feature they might choose to use.

### Docker Installation

> **Note**: The following Docker containers are only supposed to be used with RCPs built using Simplicity Studio for a given release. Be sure to match the container tag version with the Simplicity SDK version that you are using for testing.

Silicon Labs recommends deploying the company’s Docker container with the OTBR. Running the OTBR in a container allows for creation of easily deployable artifacts and fast development prototyping and testing.

Silicon Labs provides the following pre-built Docker containers (with tags), hosted on DockerHub:

[https://hub.docker.com/r/siliconlabsinc/openthread-border-router/tags](https://hub.docker.com/r/siliconlabsinc/openthread-border-router/tags)

For proprietary radio support (alpha release):

[https://hub.docker.com/r/siliconlabsinc/openthread-border-router-proprietary-na-915/tags](https://hub.docker.com/r/siliconlabsinc/openthread-border-router-proprietary-na-915/tags)

#### Prerequisites

- On the SD card, make sure to flash the [Raspberry Pi OS Lite image](https://www.raspberrypi.org/downloads/raspberry-pi-os/) or [Raspberry Pi OS with Desktop](https://www.raspberrypi.org/downloads/raspberry-pi-os/).
- Make sure to update the local repositories and package manager (**apt-get update** and **apt-get upgrade** prior to installing Docker).
- Optional but recommended: Install Haveged for better entropy conditions.

#### Installation Guidance

> **Note**: Replace the string <version> in the following commands with the actual version you are using. For example, gsdk-4.4.0, sisdk-2024.6.0, etc.

- Make sure to reboot after any updates:  
  ```C  
  curl -sSL https://get.docker.com | sh  
  ```
- Once finished, you can modify the Docker user settings to not require sudo before each command:  
  ```C  
  sudo usermod -aG docker $USER  
  ```
- Raspberry Pi and Linux users, make sure to run:  
  ```C  
  sudo modprobe ip6table_filter  
  ```  
  for OTBR firewall support. This allows OTBR scripts to create rules inside the Docker container before otbr-agent starts.  
  To make sure this setting persists between reboots, add the following line to `/etc/modules`:  
  ```C  
  ip6table_filter  
  ```  
  If this step is not completed, modprobe errors may be displayed when starting a Docker container.
- Issue the following commands to install the containers. Note that only one Border Router container can be running at one time with a Co-Processor. Also, be sure to verify the device version (Thread protocol version 1.4) that should be run against this container.  
  ```C  
  UART interface:  
  docker pull siliconlabsinc/openthread-border-router:<version>  
    
  SPI interface:  
  docker pull siliconlabsinc/openthread-border-router:<version>_spi  
  ```
- To run an OpenThread Border Router (default is Thread protocol version 1.4), issue the following command:  
  - Example for UART interface  
  ```C  
  docker run -d --name "otbr" \  
        --sysctl "net.ipv6.conf.all.disable_ipv6=0 net.ipv4.conf.all.forwarding=1 net.ipv6.conf.all.forwarding=1" \  
        -p 8080:80 --dns=127.0.0.1 -it \  
        --volume /dev/ttyACM0:/dev/ttyACM0 \  
        --privileged siliconlabsinc/openthread-border-router:<version> \  
        --radio-url “spinel+hdlc+uart:///dev/ttyACM0” \  
  --backbone-interface eth0  
  ```

See sections [OTBR Configurations Using UART Interface](#otbr-configurations-using-uart-interface) and [UART Baud Rate Settings](#uart-baud-rate-settings) for notes on configuring the UART Radio URL.

- Example for SPI interface (for more information, see [OTBR Configurations using SPI Interface](#otbr-configurations-using-spi-interface))

```C
docker run -d --name "otbr" \
      --sysctl "net.ipv6.conf.all.disable_ipv6=0 net.ipv4.conf.all.forwarding=1 net.ipv6.conf.all.forwarding=1" \
      -p 8080:80 --dns=127.0.0.1 -it \
      --volume /dev/spidev0.0:/dev/spidev0.0 \
      --privileged siliconlabsinc/openthread-border-router:<version> \
      --radio-url “spinel+spi:///dev/spidev0.0?gpio-int-device=/dev/gpiochip0&gpio-int-line=21&gpio-reset-device=/dev/gpiochip0&gpio-reset-line=20&no-reset=1&spi-speed=1000000” \
      --backbone-interface eth0
```

(See section [OTBR Configurations using SPI Interface](#otbr-configurations-using-spi-interface) for notes on configuring the SPI Radio URL.)

Use additional arguments to configure the containers. For more information, see the section below or the Dockerfile in the ot-br-posix installation directory.

#### Docker Configuration Notes

> **Note**: Silicon Labs-hosted Docker containers are only supposed to be used with RCPs built using Simplicity Studio for a given release. Be sure to match the container tag version with the Simplicity SDK version that you are testing with.

> **Note**: Replace the string <version> in the following commands with the actual version you are using. For example, gsdk-4.4.0, sisdk-2024.6.0, etc.

- Configure the desired TTY port for the OTBR to connect the Co-Processor at startup. Look for the TTY port of the Co-Processor device. The easiest way to do this is to look for a /tty/dev… entry once the device is connected. It should generally either be `/dev/ttyUSB0` or `/dev/ttyACM0`.
- Run the Docker installation as follows (example for UART interface):

```C
docker run -d --name "otbr" \
      --sysctl "net.ipv6.conf.all.disable_ipv6=0 net.ipv4.conf.all.forwarding=1 net.ipv6.conf.all.forwarding=1" \
      -p 8080:80 --dns=127.0.0.1 -it \
      --volume /dev/ttyACM0:/dev/ttyACM0 \
      --privileged siliconlabsinc/openthread-border-router:<version> \
      --radio-url “spinel+hdlc+uart:///dev/ttyACM0” \
      --backbone-interface eth0
```

- `-d` ensures that the container runs in detached mode.
- Review the running logs for the container any time using the `docker logs` command.
- `--name` is sticky until the docker container is properly closed (or removed).
- Port `8080` indicates the port of the web server hosting the Border Router management webpage.
- Issue commands directly to the container without having to attach to it:  
  `docker exec -ti otbr sh -c "sudo ot-ctl state"`  
  For more information, see the [docker exec documentation](https://docs.docker.com/engine/reference/commandline/exec/).
- Directly obtain an interactive shell above by issuing this command:  
  `docker exec -ti otbr sh -c "sudo ot-ctl"`
- Check the window running the OTBR Docker container for running log output of the Border Router, or follow the container log as follows:  
  `docker logs [container-id] -f`
- Manage the containers as shown below if they are loaded improperly:  
  ```C  
  # list all container images  
  docker images otbr  
  # remove existing container  
  docker image rm -f \<container ID\>  
  # list running containers  
  docker ps -a  
  # to remove running container  
  docker rm -f \<container name\>  
  ```