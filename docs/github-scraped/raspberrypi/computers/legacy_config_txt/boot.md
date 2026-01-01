## Legacy boot options
(See also xref:config*txt.adoc#boot-options[config.txt Boot Options].)

### `start*x`, `start*debug`

These provide a shortcut to some alternative `start*file` and `fixup*file` settings, and are the recommended methods for selecting firmware configurations.

`start*x=1` implies
```
  start*file=start*x.elf
  fixup*file=fixup*x.dat
```

On Raspberry Pi 4, if the files `start4x.elf` and `fixup4x.dat` are present, these files will be used instead.

`start*debug=1` implies
```
  start*file=start*db.elf
  fixup*file=fixup*db.dat
```

### `disable*commandline*tags`

Set the `disable*commandline*tags` command to `1` to stop `start.elf` from filling in ATAGS (memory from `0x100`) before launching the kernel.

### `arm*control`

WARNING: This setting is deprecated. Use `arm*64bit` instead to enable 64-bit kernels.

Sets board-specific control bits.

### `arm*peri*high`

Set `arm*peri*high` to `1` to enable high peripheral mode on Raspberry Pi 4. It is set automatically if a suitable DTB is loaded.

NOTE: Enabling high peripheral mode without a compatible Device Tree will make your system fail to boot. Currently ARM stub support is missing, so you will also need to load a suitable file using `armstub`.

### `kernel*address`

`kernel*address` is the memory address to which the kernel image should be loaded. By default, 32-bit kernels are loaded to address `0x8000`, and 64-bit kernels to address `0x200000`. If `kernel*old` is set, kernels are loaded to the address `0x0`.

### `kernel*old`

Set `kernel*old` to `1` to load the kernel to the memory address `0x0`.

### `init*uart*baud`

`init*uart*baud` is the initial UART baud rate. The default value is `115200`.

### `init*uart*clock`

`init*uart*clock` is the initial UART clock frequency. The default value is `48000000` (48 MHz). Note that this clock only applies to UART0 (ttyAMA0 in Linux), and that the maximum baudrate for the UART is limited to 1/16th of the clock. The default UART on the Raspberry Pi 3 and Raspberry Pi Zero is UART1 (ttyS0 in Linux), and its clock is the core VPU clock - at least 250 MHz.

### `bootcode*delay`

The `bootcode*delay` command delays for a given number of seconds in `bootcode.bin` before loading `start.elf`: the default value is `0`.

This is particularly useful to insert a delay before reading the EDID of the monitor, for example if the Raspberry Pi and monitor are powered from the same source, but the monitor takes longer to start up than the Raspberry Pi. Try setting this value if the display detection is wrong on initial boot, but is correct if you soft-reboot the Raspberry Pi without removing power from the monitor.

### `boot*delay`

The `boot*delay` command forces a wait for a given number of seconds in `start.elf` before loading the kernel: the default value is `0`. The total delay in milliseconds is calculated as `(1000 x boot*delay) + boot*delay*ms`. This can be useful if your SD card needs a while to get ready before Linux is able to boot from it.

### `boot*delay*ms`

The `boot*delay*ms` command means wait for a given number of milliseconds in `start.elf`, together with `boot*delay`, before loading the kernel. The default value is `0`.

### `enable*gic` (Raspberry Pi 4 Only)

On the Raspberry Pi 4B, if this value is set to `0` then the interrupts will be routed to the Arm cores using the legacy interrupt controller, rather than via the GIC-400. The default value is `1`.

[[upstream*kernel]]
### `upstream*kernel`

If `upstream*kernel=1` is used, the firmware sets xref:config*txt.adoc#os*prefix[`os*prefix`] to "upstream/", unless it has been explicitly set to something else, but like other `os*prefix` values it will be ignored if the required kernel and .dtb file can't be found when using the prefix.

The firmware will also prefer upstream Linux names for DTBs (`bcm2837-rpi-3-b.dtb` instead of `bcm2710-rpi-3-b.dtb`, for example). If the upstream file isn't found the firmware will load the downstream variant instead  and automatically apply the "upstream" overlay to make some adjustments. Note that this process happens *after* the `os_prefix` has been finalised.