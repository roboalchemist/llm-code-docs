## Change the default pin configuration

NOTE: Custom default pin configurations via user-provided Device Tree blobs has been deprecated.

### Device pins during boot sequence

During the bootup sequence, the GPIO pins go through various actions.

** Power-on - pins default to inputs with default pulls, which are described in the https://datasheets.raspberrypi.com/bcm2835/bcm2835-peripherals.pdf[datasheet]
** Setting by the bootrom
** Setting by `bootcode.bin`
** Setting by `dt-blob.bin` (this page)
** Setting by the xref:config*txt.adoc#gpio-control[GPIO command] in `config.txt`
** Additional firmware pins (e.g. UARTS)
** Kernel/Device Tree

On a soft reset, the same procedure applies, except for default pulls, which are only applied on a power-on reset.

It may take a few seconds to run through the process. During this time, the GPIO pins may not be in the state expected by attached peripherals (as defined in `dt-blob.bin` or `config.txt`). Since different GPIO pins have different default pulls, you should do **one of the following** for your peripheral:

** Choose a GPIO pin that defaults to pulls as required by the peripheral on reset
** Delay the peripheral's startup until the actions are completed
** Add an appropriate pull-up/pull-down resistor

### Provide a custom Device Tree blob

In order to compile a Device Tree source (`.dts`) file into a Device Tree blob (`.dtb`) file, the Device Tree compiler must be installed by running `sudo apt install device-tree-compiler`. The `dtc` command can then be used as follows:

```console
$ sudo dtc -I dts -O dtb -o /boot/firmware/dt-blob.bin dt-blob.dts
```

Similarly, a `.dtb` file can be converted back to a `.dts` file, if required.

```console
$ dtc -I dtb -O dts -o dt-blob.dts /boot/firmware/dt-blob.bin
```

### Sections of the `dt-blob`

The `dt-blob.bin` is used to configure the binary blob (VideoCore) at boot time. It is not currently used by the Linux kernel. The dt-blob can configure all versions of the Raspberry Pi, including the Compute Module, to use the alternative settings. The following sections are valid in the dt-blob:

#### `videocore`

This section contains all of the VideoCore blob information. All subsequent sections must be enclosed within this section.

#### `pins***`

There are a number of separate `pins***` sections, based on particular Raspberry Pi models, namely:

** `pins*rev1`: Rev1 pin setup. There are some differences because of the moved I2C pins.
** `pins*rev2`: Rev2 pin setup. This includes the additional codec pins on P5.
** `pins*bplus1`: Raspberry Pi 1 Model B+ rev 1.1, including the full 40pin connector.
** `pins*bplus2`: Raspberry Pi 1 Model B+ rev 1.2, swapping the low-power and lan-run pins.
** `pins*aplus`: Raspberry Pi 1 Model A+, lacking Ethernet.
** `pins*2b1`: Raspberry Pi 2 Model B rev 1.0; controls the SMPS via I2C0.
** `pins*2b2`: Raspberry Pi 2 Model B rev 1.1; controls the SMPS via software I2C on 42 and 43.
** `pins*3b1`: Raspberry Pi 3 Model B rev 1.0
** `pins*3b2`: Raspberry Pi 3 Model B rev 1.2
** `pins*3bplus`: Raspberry Pi 3 Model B+
** `pins*3aplus`: Raspberry Pi 3 Model A+
** `pins*pi0`: Raspberry Pi Zero
** `pins*pi0w`: Raspberry Pi Zero W
** `pins*pi02w`: Raspberry Pi Zero 2 W
** `pins*cm`: Raspberry Pi Compute Module 1. The default for this is the default for the chip, so it is a useful source of information about default pull-ups/pull-downs on the chip.
** `pins*cm3`: Raspberry Pi Compute Module 3
** `pins*cm3plus`: Raspberry Pi Compute Module 3+
** `pins*cm4s`: Raspberry Pi Compute Module 4S
** `pins*cm4`: Raspberry Pi Compute Module 4

Each `pins***` section can contain `pin*config` and `pin*defines` sections.

#### `pin*config`

The `pin*config` section is used to configure the individual pins. Each item in this section must be a named pin section, such as `pin@p32`, meaning GPIO32. There is a special section `pin@default`, which contains the default settings for anything not specifically named in the pin*config section.

#### `pin@pinname`

This section can contain any combination of the following items:

 ** `polarity`
  **** `active*high`
  **** `active*low`
 ** `termination`
  *** `pull*up`
  **** `pull*down`
  **** `no*pulling`
 ** `startup*state`
  *** `active`
  **** `inactive`
 ** `function`
  *** `input`
  **** `output`
  **** `sdcard`
  **** `i2c0`
  **** `i2c1`
  **** `spi`
  **** `spi1`
  **** `spi2`
  **** `smi`
  **** `dpi`
  **** `pcm`
  **** `pwm`
  **** `uart0`
  **** `uart1`
  **** `gp*clk`
  **** `emmc`
  **** `arm*jtag`
 ** `drive*strength*mA`
+
The drive strength is used to set a strength for the pins. Please note that you can only specify a single drive strength for the bank. <8> and <16> are valid values.

#### `pin*defines`

This section is used to set specific VideoCore functionality to particular pins. This enables the user to move the camera power enable pin to somewhere different, or move the HDMI hotplug position: these are things that Linux does not control. Please refer to the example DTS file below.

### Clock configuration

It is possible to change the configuration of the clocks through this interface, although it can be difficult to predict the results! The configuration of the clocking system is very complex. There are five separate PLLs, and each one has its own fixed (or variable, in the case of PLLC) VCO frequency. Each VCO then has a number of different channels which can be set up with a different division of the VCO frequency. Each of the clock destinations can be configured to come from one of the clock channels, although there is a restricted mapping of source to destination, so not all channels can be routed to all clock destinations.

Here are a couple of example configurations that you can use to alter specific clocks. We will add to this resource when requests for clock configurations are made.

```kotlin
clock*routing {
   vco@PLLA  {    freq = <1966080000>; };
   chan@APER {    div  = <4>; };
   clock@GPCLK0 { pll = "PLLA"; chan = "APER"; };
};

clock_setup {
   clock@PWM { freq = <2400000>; };
   clock@GPCLK0 { freq = <12288000>; };
   clock@GPCLK1 { freq = <25000000>; };
};
```

The above will set the PLLA to a source VCO running at 1.96608 GHz (the limits for this VCO are 600 MHz - 2.4 GHz), change the APER channel to /4, and configure GPCLK0 to be sourced from PLLA through APER. This is used to give an audio codec the 12288000Hz it needs to produce the 48000 range of frequencies.

### Sample Device Tree source file

The firmware repository contains a https://github.com/raspberrypi/firmware/blob/master/extra/dt-blob.dts[master Raspberry Pi blob] from which others are usually derived.