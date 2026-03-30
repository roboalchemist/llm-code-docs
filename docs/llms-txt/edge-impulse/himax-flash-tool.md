# Source: https://docs.edgeimpulse.com/tools/clis/edge-impulse-cli/himax-flash-tool.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Himax flash tool

The Himax flash tool uploads new binaries to the [Himax WE-I Plus](/hardware/boards/himax-we-i-plus) or `Grove Vision AI Module V2 (Himax WiseEye2)` over a serial connection.

You upload a new binary via:

```
$ himax-flash-tool -f path/to/a/firmware.img
```

This will yield a response like this:

```
[HMX] Connecting to /dev/tty.usbserial-DT04551Q...
[HMX] Connected, press the **RESET** button on your Himax WE-I now
[HMX] Restarted into bootloader. Sending file.
[HMX] Sending 2964 blocks
 ████████████████████████████████████████ 100% | ETA: 0s | 2964/2964
[HMX] Firmware update complete
[HMX] Press **RESET** to start the application

Flashed your Himax WE-I Plus development board.
To set up your development with Edge Impulse, run 'edge-impulse-daemon'
To run your impulse on your development board, run 'edge-impulse-run-impulse'
```

### Other options

* `--baud-rate <n>` - sets the baud rate of the bootloader. This should only be used during development.
* `--verbose` - enable debug logs, including all communication received from the device.
* `--device <device>` - select the device type: `WE-I-Plus` (default) or `WiseEye2` (Grove Vision AI Module V2)
* `--skip-reset` - skip the reset procedure (in case the device is already in bootloader mode)
* `--version` - output the version number
* `--help` - display help for command
* `--firmware-path <file>` - firmware path (required)


Built with [Mintlify](https://mintlify.com).