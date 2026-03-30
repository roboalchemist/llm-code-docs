# Source: https://docs.edgeimpulse.com/tools/protocols/remote-management/serial.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Serial

Devices that don't have a direct internet connection can connect to the remote management service over serial. This is done via the [serial daemon](/tools/clis/edge-impulse-cli/serial-daemon), which is an application that runs on a host machine. The serial daemon connects to a device over a serial port, and sends AT commands back and forth to the device. If your device implements all AT commands on this page, the serial daemon should work as-is on your device.

Communication between host and device is done with the following settings:

* Baud rate 115200.
* Data bits: 8.
* Return key: CR.

A comprehensive test suite for devices implementing this protocol is located here: [edgeimpulse/integration-tests-firmware](https://github.com/edgeimpulse/integration-tests-firmware).

## Overview of all commands

This overview should be printed when `AT+HELP` is issued.

```
AT+HELP - Lists all commands
AT+CLEARCONFIG - Clears complete config and resets system
AT+CLEARFILES - Clears all files from the file system, this does not clear config
AT+CONFIG? - Lists complete config
AT+DEVICEINFO? - Lists device information
AT+SENSORS? - Lists sensors
AT+RESET - Reset the system
AT+WIFI? - Lists current WiFi credentials
AT+WIFI= - Sets current WiFi credentials (SSID,PASSWORD,SECURITY) (3 parameters)
AT+SCANWIFI - Scans for WiFi networks
AT+SAMPLESETTINGS? - Lists current sampling settings
AT+SAMPLESETTINGS= - Sets current sampling settings (LABEL,INTERVAL_MS,LENGTH_MS) (3 parameters)
AT+SAMPLESETTINGS= - Sets current sampling settings (LABEL,INTERVAL_MS,LENGTH_MS,HMAC_KEY) (4 parameters)
AT+UPLOADSETTINGS? - Lists current upload settings
AT+UPLOADSETTINGS= - Sets current upload settings (APIKEY,PATH) (2 parameters)
AT+UPLOADHOST= - Sets upload host (HOST) (1 parameter)
AT+MGMTSETTINGS? - Lists current management settings
AT+MGMTSETTINGS= - Sets current management settings (URL) (1 parameter)
AT+LISTFILES - Lists all files on the device
AT+READFILE= - Read a specific file (as base64) (1 parameter)
AT+READBUFFER= - Read from the temporary buffer (as base64) (START,LENGTH) (2 parameters)
AT+UNLINKFILE= - Unlink a specific file (1 parameter)
AT+UPLOADFILE= - Upload a specific file (1 parameter)
AT+SAMPLESTART= - Start sampling (1 parameter)
```

### Custom commands

It's allowed to add custom commands. For example, these commands are implemented in the Edge Impulse firmware for the [ST B-L475E-IOT01A](/hardware/boards/st-b-l475e-iot01a), but are not used by the serial daemon.

```
AT+FILLMEMORY - Try and fill the full RAM, to report free heap stats
AT+RUNIMPULSE - Run the impulse
AT+RUNIMPULSEDEBUG - Run the impulse with debug messages
```

## System commands

### AT+CLEARCONFIG

Clears the complete configuration, and resets the system. Has no return value. Example:

```
> AT+CLEARCONFIG
Clearing config and restarting system...

Hello from the Edge Impulse Device SDK.
```

Afterwards all settings should be reset.

### AT+RESET

Restarts the system, but leaves all configuration intact. Has no return value. Example:

```
> AT+RESET

Hello from the Edge Impulse Device SDK.
```

## Full configuration

### AT+CONFIG?

Lists all configuration options, grouped by category. Lines with category names start and end with `=====`. Lines with configuration options follow `key: value`, with arbitrary whitespace between `:` and the value. Example:

```
===== Device info =====
ID:         C4:7F:51:94:4A:38
Type:       DISCO_L475VG_IOT01A
AT Version: 1.6.0
Data Transfer Baudrate: 921600

===== Sensors ======
Name: Built-in accelerometer, Max sample length: 300s, Frequencies: [62.50Hz, 100.00Hz]
Name: Built-in microphone, Max sample length: 60s, Frequencies: [16000.00Hz]

===== Snapshot ======
Has snapshot:    1
Supports stream: 1
Color depth:     Grayscale
Resolutions:     [ 128x96, 320x240, 640x480 ]

===== WIFI =====
Present:   1
SSID:      Edge Impulse Wifi
Password:  machinelearning
Security:  3
MAC:       C4:7F:51:94:4A:38
Connected: 1
Present:   1

===== Sampling parameters =====
Label:     noise
Interval:  10.00 ms.
Length:    1000 ms.
HMAC key:  cde1e82eec38e086db7b9c6d2f60c97e

===== Upload settings =====
Api Key:   ei_9231b10d97b18c6065868c0729400a0945df0d2715429495396678863d778f5c
Host:      http://ingestion.edgeimpulse.com
Path:      /api/training/data

===== Remote management =====
URL:        ws://remote-mgmt.edgeimpulse.com
Connected:  1
Last error:
```

See the separate sections per configuration option below for more information.

## Device information commands

### AT+DEVICEINFO?

Returns information about the device and the firmware. The `ID` here should be a globally unique ID (like a MAC address). If the device does not have a globally unique ID set this to `00:00:00:00:00:00` and implement the `AT+DEVICEID` command. The serial daemon will then use the MAC address of the USB controller instead.

The `Data Transfer Baudrate` is the baud rate that the device can switch to when offloading data for functions like `AT+BUFFER`. If the device does not support switching to a higher baud rate set this to `115200`. See "Switching to higher baud rates" later on this page for the protocol.

Example:

```
> AT+DEVICEINFO?
ID:         C4:7F:51:94:4A:38
Type:       DISCO_L475VG_IOT01A
AT Version: 1.6.0
Data Transfer Baudrate: 921600
```

For an overview of the different AT command versions, see the end of this page.

### AT+DEVICEID

Sets the device ID. This is only required for devices that do not have a globally unique ID (see `AT+DEVICEINFO?`).

Example:

```
> AT+DEVICEID=00:00:00:DD:EE:FF
OK
```

### AT+SENSORS?

Lists sensors on the device that can be used to collect data. One sensor per line, with Name, Max sample length, and Frequencies listed. The name that you list here will be passed back to `AT+SAMPLESTART=` to indicate which sensor should be used. Example:

```
> AT+SENSORS?
Name: Built-in accelerometer, Max sample length: 300s, Frequencies: [62.50Hz, 100.00Hz]
Name: Built-in microphone, Max sample length: 60s, Frequencies: [16000.00Hz]
```

### AT+SNAPSHOT?

Lists whether the device has a camera, whether the device supports snapshot streaming, and the resolutions of the camera. If the device does not have a camera set `Has snapshot` to `0` and omit the other options. The color depth should be either `Grayscale` or `RGB`. Example:

```
> AT+SNAPSHOT?
Has snapshot:    1
Supports stream: 1
Color depth:     Grayscale
Resolutions:     [ 128x96, 320x240, 640x480 ]
```

## File system commands

No file system? The serial daemon can also use a scratch buffer instead, e.g. on external or internal flash. For this you need to implement the `AT+READBUFFER` function and follow the instructions under `AT+SAMPLESTART`.

### AT+LISTFILES

Lists all files on the file system, one file per line. Example:

```
> AT+LISTFILES
/fs/noise12
/fs/noise13
```

### AT+READFILE

Read a single file from file system, returns the full file in base64 format. This function takes two parameters: 1) the name of the file, 2) whether to switch to the 'Data transfer baud rate' (`y/n`). Example:

```
> AT+READFILE=/fs/noise12,n
SGVsbG8gZnJvbSBFZGdlIEltcHVsc2U=
```

If the file does not exist, a string should be returned such as:

```
> AT+READFILE=/fs/non-existent
File '/fs/non-existent' does not exist
```

### AT+UNLINKFILE

Removes a single file from file system. Returns nothing if the file was unlinked successfully. Example:

```
> AT+UNLINKFILE=/fs/noise12
```

If the file does not exist, or if unlink fails, a string should be returned:

```
> AT+UNLINKFILE=/fs/non-existent
File '/fs/non-existent' could not be unlinked
```

### AT+UPLOADFILE

Uploads a file to Edge Impulse. This uses the upload settings (see `AT+UPLOADSETTINGS?`) to specify where the file will be sent. Once uploading is completed, the device should respond with `File uploaded`. Example:

```
> AT+UPLOADFILE=/fs/noise0
Uploading '/fs/noise0' to http://ingestion.edgeimpulse.com/api/training/data...
File uploaded
```

If the file does not exist, an error should be thrown that starts with "Failed to upload file". Example:

```
> AT+UPLOADFILE=/fs/non-existent
Uploading '/fs/non-existent' to http://ingestion.edgeimpulse.com/api/training/data...
Failed to upload file, cannot open '/fs/non-existent'
```

If there's no WiFi connection, an error should be thrown that starts with "Not connected to WiFi". Example:

```
> AT+UPLOADFILE=/fs/noise0
Not connected to WiFi, cannot upload
```

### AT+CLEARFILES

Clears all files on the underlying file system, except the config file. Example:

```
> AT+CLEARFILES
Clearing file system...
Unlinked '/fs/noise12'
Unlinked '/fs/noise15'
Unlinked '/fs/noise16'
```

### AT+READBUFFER

Read part of the scratch buffer, and returns this data in base64 format. This function takes three parameters: 1) the start offset, 2) the end offset, 3) whether to switch to the 'Data transfer baud rate' (`y/n`). Example:

```
> AT+READBUFFER=0,20,n
o2lwcm90ZWN0ZWSiY3ZlcmJ2MWM=
```

## WiFi

### Security values

An integer is used to specify the security mode for a WiFi network, according to this list:

* 0 - Open access point
* 1 - WEP
* 2 - WPA
* 3 - WPA2
* 4 - WPA/WPA2
* 5 - PPP authentication context
* 6 - PPP authentication context
* 7 - EAP-TLS
* 8 - PEAP
* 255 - Unknown

### AT+SCANWIFI

Scans for nearby WiFi networks. Returns one network per line. Example:

```
> AT+SCANWIFI
SSID: Edge Impulse WiFi, Security: WPA2 (3), RSSI: -56 dBm
SSID: _HOME, Security: WPA2 (3), RSSI: -83 dBm
SSID: VFNL-EDA318, Security: WPA2 (3), RSSI: -91 dBm
SSID: HZN242073819, Security: WPA2 (3), RSSI: -73 dBm
SSID: Ziggo, Security: Unknown (255), RSSI: -89 dBm
SSID: Ziggo911B311, Security: WPA2 (3), RSSI: -85 dBm
SSID: Recover.Me-2B6F30, Security: WPA2 (3), RSSI: -88 dBm
```

### AT+WIFI?

Lists current WiFi credentials, MAC address, and whether the device is connected. Example:

```
Present:   1
SSID:      Edge Impulse WiFi
Password:  machinelearning
Security:  3
MAC:       C4:7F:51:94:4A:38
Connected: 1
Present:   1
```

**No WiFi?** Return `0` for 'Present' and leave the other fields empty. The serial daemon will then no longer prompt to connect the development board to WiFi.

### AT+WIFI=

Sets WiFi credentials. Takes three parameters: SSID, password, and security mode (integer). After calling this function the device connects to the WiFi network, gets NTP info, and connects to the remote management service (if the remote management settings are set). Returns OK when done. Example:

```
> AT+WIFI=Edge Impulse WiFi,machinelearning,3
Connecting to 'Edge Impulse WiFi'
Connected to WiFi, will now automatically upload samples
Getting NTP info...
Current time is Tue Jan 21 17:30:20 2020
ws connect
Connecting to WS Client returned 0
OK
```

Note: failure to connect to the remote management service should not throw an error, and should still return OK.

## Sample settings

### AT+SAMPLESETTINGS?

Lists the current sample settings, such as the label to use, the interval, the length and the HMAC key. Example:

```
> AT+SAMPLESETTINGS?
Label:     noise
Interval:  10.00 ms.
Length:    1000 ms.
HMAC key:  cde1e82eec38e086db7b9c6d2f60c97e
```

### AT+SAMPLESETTINGS=

Sets the current sample settings. This either takes three parameters (label, interval, length) or four parameters (label, interval, length, HMAC key). Returns OK. Example:

```
> AT+SAMPLESETTINGS=idle,12,1000,cde2831ae
OK
```

Note that the interval may be ignore if the sensor does not support this. E.g. if a microphone only supports sampling at 16KHz it will ignore this setting.

## Upload settings

### AT+UPLOADSETTINGS?

Lists the current upload settings, such as the API Key (used to authenticate to the ingestion service, but also used for connecting to the remote management service). Example:

```
> AT+UPLOADSETTINGS?
Api Key:   ei_9231b10d97b18c6065868c0729400a0945df0d2715429495396678863d778f5c
Host:      http://ingestion.edgeimpulse.com
Path:      /api/training/data
```

### AT+UPLOADSETTINGS=

Sets the upload and remote management API key and sets the path (two parameters). Returns OK. Example:

```
> AT+UPLOADSETTINGS=ei_myapikey,/api/training/data
OK
```

### AT+UPLOADHOST=

Sets the upload host. Returns OK. Example:

```
> AT+UPLOADHOST=http://ingestion.edgeimpulse.com
OK
```

## Management settings

### AT+MGMTSETTINGS?

Lists the current settings and state for the remote management service. Note that the API key used to authenticate to the service is set by `AT+UPLOADSETTINGS=`. If the device is not connected, the `Last error` field can be used to indicate why the connection failed. Example:

```
> AT+MGMTSETTINGS?
URL:        ws://remote-mgmt.edgeimpulse.com
Connected:  1
Last error:
```

Or when something went wrong:

```
> AT+MGMTSETTINGS?
URL:        ws://remote-mgmt.edgeimpulse.com
Connected:  0
Last error: Error: Invalid API key
```

### AT+MGMTSETTINGS=

Sets the management URL. After this value is changed the device should not disconnect from the current remote management service - this only happens after re-connecting to WiFi or when restarting the device. Returns OK. Example:

```
> AT+MGMTSETTINGS=ws://remote-mgmt.edgeimpulse.com
OK
```

## Start sampling

### AT+SAMPLESTART=

Starts sampling according to the parameters in `AT+SAMPLESETTINGS?`, and then uploads the file (if connected to WiFi) according to the parameters in `AT+UPLOADSETTINGS?`. Takes one parameter, the name of the sensor (one of the sensors listed in `AT+SENSORS?`).

If the upload succeeds, you can unlink the file to save space. If the device is not connected to WiFi it should print the string `Not uploading file`. The serial daemon will then use `AT+READFILE` with the file name specified earlier to read the file back.

If you have stored the file in a scratch buffer - e.g. on external flash - without a file system, you need to print: `Not uploading file. Used buffer, from=0, to=310.` (where 0 and 310 are parameters that will be passed in to `AT+READBUFFER`).

The sample interval from `AT+SAMPLESETTINGS?` may be ignored, e.g. if this is set to a value that the sensor does not support.

While sampling you can print the following lines to give feedback about the sampling status. These messages are intercepted by the daemon and used to set UI updates in the studio.

* `Sampling...` - sampling has started, currently recording data from the sensor.
* `Done sampling` - sampling has finished.
* `Processing...` - if the sample requires post-processing (e.g. signing the file, or copying the file over), send this event.
* `Done processing` - post-processing was done.
* `Uploading...` - uploading has started.
* `OK` - full process is done.

If the device is not connected, end with the line `Not uploading file`, and don't emit `OK`.

Prior to starting, please print out a line that starts with `File name:` and lists where the file will be stored.

Example:

```
> AT+SAMPLESTART=Built-in microphone
Sampling settings:
        Interval: 0.06250 ms.
        Length: 1000 ms.
        Name: noise
        HMAC Key: efe9cb503c6f29ead60228cc63a68e5f
        File name: /fs/noise0
Starting in 2000 ms... (or until all flash was erased)
Sampling...
Done sampling, total bytes collected: 32000
Processing...
[1/3] Copying from tempfile to /fs/noise0 (this might take a while)...
[1/3] Copying from tempfile to /fs/noise0 OK (took 1378 ms.)
[2/3] Calculating hash...
[2/3] Calculating hash OK
Done processing
[3/3] Uploading file to Edge Impulse...
Uploading... '/fs/noise0' to http://ingestion.edgeimpulse.com/api/training/data...
[3/3] Uploading file to Edge Impulse OK (took 2403 ms.)
OK
```

### AT+SNAPSHOT

Makes a photo and prints the frame buffer as a base64 encoded string. This function takes three parameters: 1) the width of the snapshot, 2) the height of the snapshot, 3) whether to switch to the 'Data transfer baud rate' (`y/n`). The content of the base64 buffer should be a `uint8_t` array, with one value per pixel when in grayscale mode, or three values per pixel in RGB mode. E.g. an 2x1 image with a black and a white pixel would be:

* Grayscale: `[ 0x00, 0xff ]` (pixel 1, pixel 2).
* RGB: `[ 0x00, 0x00, 0x00, 0xff, 0xff, 0xff ]` (pixel 1 red, pixel 1 green, pixel 1 blue, pixel 2 red, pixel 2 green, pixel 2 blue).

Example:

```
> AT+SNAPSHOT=128,96,n
Q0lMTFpobWpZgnViU1JVVlZXW32Vkm9ERkxQSkc9NzhGUTNrSj09PC0yNTpAQ1FWWV1UT09O...
OK
```

To decode the framebuffer you can use the `edge-impulse-framebuffer2jpg` tool which is part of the [Edge Impulse CLI](/tools/clis/edge-impulse-cli). Write the base64 string to a file called `features.txt` and then invoke:

```
$ edge-impulse-framebuffer2jpg -f features.txt -o framebuffer.jpg -w 128 -h 96
```

This will create a file called `framebuffer.jpg` with the decoded content.

### AT+SNAPSHOTSTREAM

Constantly snaps photos and prints the frame buffer as a base64 encoded string, until `b` is received on stdin. This function takes three parameters: 1) the width of the snapshot, 2) the height of the snapshot, 3) whether to switch to the 'Data transfer baud rate' (`y/n`). The format is the same as `AT+SNAPSHOT`, but every snapshot should be on a new line.

Example:

```
> AT+SNAPSHOTSTREAM=128,96,n
Starting snapshot stream...
ODw9Pj8tIiEjMEI/NiopO0dMRC8vMDAyNDQ0OFtlPi47Yks2Ly8wMC0uLiwtKywrKyopKCgoKC...
ODw+Pj8tIiIjMEJANiopO0dMRC8vMDAyNTQ1OVxlPS08Yks1MC8wLy0uLSwsLCwrKyopKCgnKC...
OD0+Pj8vIiIjL0JAOCopOkZLRS8vMDAyNDQ0OFllPi46YUw2Ly8wMC0uLSwsLCsrKyopKCgoKC...
Snapshot streaming stopped by user
OK
```

## Switching to higher baud rates

For commands that allow switching to a higher baud rate (`AT+READFILE`, `AT+READBUFFER`, `AT+SNAPSHOT`, `AT+SNAPSHOTSTREAM`) you'll need to follow this procedure:

1. When `n` is passed in for the 'use max rate' property:
   * Do nothing, just print as usual.
2. When `y` is passed in for the 'use max rate' property:
   * Print `\r\nOK` on baud rate 115,200.
   * Wait 100ms and switch to the max. baud rate. This gives the serial daemon time to switch the rate.
   * Print the result of the command.
   * Print `\r\nOK` (on the max. baud rate).
   * Wait 100ms. and switch back to baud rate 115,200.
   * Print a new REPL start line (`\r\n>` ).

## Version history

* 1.2.0 - switch the return type of `AT+READFILE` from hex to base64.
* 1.3.0 - implement `AT+READBUFFER` and the `Present` field for WiFi.
* 1.4.0 - add snapshot mode and the data transfer baud rate property.
* 1.5.0 - add snapshot streaming mode.
* 1.6.0 - allow explicit switching to higher baud rates.


Built with [Mintlify](https://mintlify.com).