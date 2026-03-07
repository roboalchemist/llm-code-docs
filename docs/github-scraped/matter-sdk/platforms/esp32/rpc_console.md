## RPC Console and Device Tracing

## Using RPC Console

You can use the rpc default config to setup everything correctly for RPCs:

```bash
export SDKCONFIG_DEFAULTS=$PROJECT_ROOT/examples/all-clusters-app/esp32/sdkconfig_m5stack_rpc.defaults
rm sdkconfig
idf.py fullclean

```

Alternatively, Enable RPCs in the build using menuconfig:

- Enable the RPC library and Disable ENABLE_CHIP_SHELL

    ```text
    Component config → CHIP Core → General Options → Enable Pigweed PRC library
    Component config → CHIP Core → General Options → Disable CHIP Shell

    ```

- Ensure the UART is correctly configured for your board, for m5stack:

    ```text
    PW RPC Debug channel → UART port number → 0
    PW RPC Debug channel → UART communication speed → 115200
    PW RPC Debug channel → UART RXD pin number → 3
    PW RPC Debug channel → UART TXD pin number → 1

    ```

After configuring you can build and flash normally:

```bash
idf.py build
idf.py flash

```

After flashing a build with RPCs enabled you can use the rpc console to send
commands to the device.

Build or install the
[rpc console](../../../examples/common/pigweed/rpc_console/README.md)

Start the console

```text
chip-console --device /dev/ttyUSB0

```

From within the console you can then invoke rpcs:

- Configure WiFi

    ```text
    rpcs.chip.rpc.WiFi.Connect(ssid=b"MySSID", secret=b"MyPASSWORD")
    rpcs.chip.rpc.WiFi.GetIP6Address()

    ```

- Control Lighting

    ```text
    rpcs.chip.rpc.Lighting.Get()
    rpcs.chip.rpc.Lighting.Set(on=True, level=128, color=protos.chip.rpc.LightingColor(hue=5, saturation=5))

    ```

- Control Lock

    ```text
    rpcs.chip.rpc.Locking.Get()
    rpcs.chip.rpc.Locking.Set(locked=True)

    ```

- OTA Requestor

    ```text
    rpcs.chip.rpc.Device.TriggerOta()

    ```

## Device Tracing

Device tracing is available to analyze the device performance. To turn on
tracing, build with RPC enabled.

Obtain tracing json file.

```bash
$ ./{PIGWEED_REPO}/pw_trace_tokenized/py/pw_trace_tokenized/get_trace.py -d {PORT} -o {OUTPUT_FILE} \
    -t {ELF_FILE} {PIGWEED_REPO}/pw_trace_tokenized/pw_trace_protos/trace_rpc.proto

```
