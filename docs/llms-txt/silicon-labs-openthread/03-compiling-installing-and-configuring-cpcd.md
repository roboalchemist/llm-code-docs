# Source: https://docs.silabs.com/openthread/3.0.0/using-co-processor-communication-daemon/03-compiling-installing-and-configuring-cpcd.md

# Compiling, Installing, and Configuring CPCd

## Downloading

Download the daemon source files from Silicon Labs GitHub project:

[https://github.com/SiliconLabs/cpc_daemon](https://github.com/SiliconLabs/cpc_daemon)

The main branch contains the latest official versions. Early access versions are available in the specific version branches.

## Compiling CPCd and the CPC Library

The build essential and CMake packages in Linux are required for this step. Compile the CPC daemon in the source folder using the following commands:

```sh
mkdir build
cd build
cmake ../
make
```

## Installing CPCd

Super-user permissions are required to install the daemon, cpclib, and the configuration file. These can be installed with the following commands:

```sh
make install
```

The following components will be installed:

- /usr/local/lib/libcpc.so.0.1
- /usr/local/lib/libcpc.so.1
- /usr/local/lib/libcpc.so
- /usr/local/include/sl_enum.h
- /usr/local/include/sl_cpc.h
- /usr/local/bin/cpcd
- /etc/cpcd.conf

Once installed, CPCd can be executed by invoking the cpcd command.

## Configuring CPCd

When running the daemon without arguments, it starts with the default configuration file installed in the previous step. To specify a different configuration file, use the --conf argument. For example:

```sh
cpcd --conf <configuration file path>
```

## Obtaining the Version of CPCd

If CPCd is started with the -v or --version argument, the daemon first prints the version of CPCd and exit. For example:

```sh
cpcd –version
```

## Available Configurations

CPCd is configured in a key/value manner in the **cpcd.conf** file.

**Table**: CPCd configuration

|Description|Key|Possible Values|Default Value|Mandatory|
|---|---|---|---|---|
|Instance Name|INSTANCE_NAME|string|cpcd_0|No|
|Bus type selection|BUS_TYPE|UART SPI|UART|Yes|
|SPI device file|SPI_DEVICE_FILE|Any path to SPI device file|/dev/spidev0.0|Yes if BUS_TYPE is SPI|
|SPI Chip Select GPIO #|SPI_CS_GPIO|Any GPIO # (1)|24|Yes if BUS_TYPE is SPI|
|SPI RX IRQ GPIO|SPI_RX_IRQ_GPIO|Any GPIO # (1)|23|Yes if BUS_TYPE is SPI|
|SPI Bitrate|SPI_DEVICE_BITRATE|Any (2)|1000000|Yes if BUS_TYPE is SPI|
|SPI Mode|SPI_DEVICE_MODE|SPI_MODE_0 (3) SPI_MODE_1 SPI_MODE_2 SPI_MODE_3|SPI_MODE_0|Yes if BUS_TYPE is SPI|
|UART Device File|UART_DEVICE_FILE|Any (4)|/dev/serial0|Yes if BUS_TYPE is UART|
|UART Baud Rate|UART_DEVICE_BAUD|1200 (5) 2400 4800 19200 38400 57600 115200|115200|Yes if BUS_TYPE is UART|
|UART Hardware Flow Control|UART_HARDFLOW|True or false|False|Yes if BUS_TYPE is UART|
|Trace to stdout|STDOUT_TRACE|True or false|False|No|
|Trace to a file located under TRACES_FOLDER|TRACE_TO_FILE|True or False|False|No|
|Destination folder when TRACE_TO_FILE is enabled|TRACES_FOLDER|Any path that the CPCd can access|./cpcd-traces|No|
|The maximum number of open file descriptors.|RLIMIT_NOFILE|Depends on the OS limit|2000|No|
|Disable the encryption over CPC endpoints|DISABLE_ENCRYPTION|True or false|False|No|

(1) Make sure the CPC daemon has enough permissions to access this GPIO.

(2) This setting depends on various factors. The bitrate needs to satisfy both side requirements.

(3) Refer to section 2.6 for additional details.

(4) This setting depends on the Linux SOC.

(5) These baud rates are typical, but any value that meets both requirements can be used.

## Available SPI Modes

The SPI_DEVICE_MODE configuration allows SPI clock polarity and phase to be configured, as shown in the following table.

**Table**: SPI Mode configuration

|Mode|Clock Polarity (CPOL)|Clock Phase (CPHA)|
|---|---|---|
|SPI_MODE_0|0|0|
|SPI_MODE_1|0|1|
|SPI_MODE_2|1|0|
|SPI_MODE_3|1|1|