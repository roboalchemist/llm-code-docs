# Source: https://docs.edgeimpulse.com/tools/clis/edge-impulse-cli/serial-daemon.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Serial daemon

The serial daemon is used to connect fully-supported devices to Edge Impulse so that data from their on-board sensors can be uploaded directly into Edge Impulse Studio. This is particularly helpful for devices without an IP connection, for which the serial daemon acts as a data upload proxy. You can also use the serial daemon to configure the upload parameters.

<Info>
  Recent versions of Google Chrome and Microsoft Edge can connect directly to fully-supported development boards, without the serial daemon. See [this blog post](https://edgeimpulse.com/blog/collect-sensor-data-straight-from-your-web-browser) for more information.
</Info>

### Getting Started

The serial daemon is part of the [Edge Impulse CLI](/tools/clis/edge-impulse-cli). In order to use the daemon, you first have to [install the CLI](/tools/clis/edge-impulse-cli/installation).

To use the daemon, connect a fully-supported development board to your computer and run:

```
$ edge-impulse-daemon
```

The daemon will prompt you to log in, and then configure the device. If your device does not have the right firmware yet, it will also prompt you to upgrade it.

This is an example of the output of the daemon:

```
Edge Impulse serial daemon v1.1.0
? What is your user name or e-mail address? jan@edgeimpulse.com
? What is your password? [hidden]
Endpoints:
    Websocket: wss://remote-mgmt.edgeimpulse.com
    API:       https://studio.edgeimpulse.com
    Ingestion: https://ingestion.edgeimpulse.com

[SER] Connecting to /dev/tty.usbmodem401203
[SER] Serial is connected, trying to read config...
[SER] Retrieved configuration
? To which project do you want to add this device? accelerometer-demo-1
Configuring API key in device... OK
Configuring HMAC key in device... OK
? What name do you want to give this device? Jan's DISCO-L475VG
Setting upload host in device... OK
Configuring remote management settings... OK
? WiFi is not connected, do you want to set up a WiFi network now? Yes
Scanning WiFi networks... OK
? Select WiFi network SSID: edgeimpulse-office, Security: WPA2 (3), RSSI: -60 dBm
? Enter password for network "edgeimpulse-office" 0624710192
Connecting to "edgeimpulse-office"... OK
[SER] Device is connected over WiFi to remote management API, no need to run the daemon. Exiting...
```

<Info>
  **Note:** Your credentials are never stored. When you log in, the serial daemon exchanges your credentials for a session token, which is used to further authenticate requests.
</Info>

#### Switching projects

You can use one device for many projects. To switch projects run:

```
$ edge-impulse-daemon --clean
```

And select the new project. The device will remain listed in the old project, and if you switch back will retain the same name and last seen date.

<Info>
  Running `--clean` resets both the daemon configuration and the on-device configuration. If you run into issues, you can connect to the device using a serial console (with a baud rate of 115,200) and send the `AT+CLEARCONFIG` command to the device, to remove its configuration.
</Info>

### Command Options

Serial daemon options can be invoked as follows:

```
$ edge-impulse-daemon [options]
```

#### API authentication `--api-key`

Enables authentication using a project API key. API keys are long strings of random characters that start with `ei_` and can be obtained from the project's dashboard on Edge Impulse Studio. Example:

```
$ edge-impulse-daemon --api-key ei_XXXXXXXXXXXXX
```

#### Baud Rate `--baud-rate`

Change the rate of the communication between the device and Edge Impulse Studio. Default is 115,200 baud. Example:

```
$ edge-impulse-daemon --baud-rate 9600
```

#### Clear Configuration `--clean`

Clears (resets) the daemon and device configurations.

#### Silent mode `--silent`

Skip all wizards (except for the login prompt). This is useful in headless environments where the session token has already been obtained, or authentication is requested via the `--api-key` option.

#### Verbose mode `--verbose`

Print additional information during execution. Useful for debugging.

#### Version `--version`

Prints the version of the Edge Impulse CLI (and therefore, the serial daemon) installed.

### Troubleshooting

#### Unable to set up WiFi with ST B-L475E-IOT01A development board

If you are using the [ST B-L475E-IOT01A](https://www.st.com/en/evaluation-tools/b-l475e-iot01a.html) development board, you may experience the following error when attempting to connect to a WiFi network:

```
? WiFi is not connected, do you want to set up a WiFi network now? Yes
Scanning WiFi networks...Error while setting up device Timeout
```

There is a [known issue](https://github.com/ARMmbed/wifi-ism43362/issues/53) with the firmware for this development board's WiFi module that results in a timeout during network scanning if there are more than 20 WiFi access points detected. If you are experiencing this issue, you can work around it by attempting to reduce the number of access points within range of the device, or by skipping WiFi configuration.


Built with [Mintlify](https://mintlify.com).