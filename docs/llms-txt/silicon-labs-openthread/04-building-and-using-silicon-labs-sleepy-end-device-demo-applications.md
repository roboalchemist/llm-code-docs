# Source: https://docs.silabs.com/openthread/3.0.0/openthread-sleepy-devices/04-building-and-using-silicon-labs-sleepy-end-device-demo-applications.md

# Building and Using Silicon Labs Sleepy End Device Demo Applications

The EFR32 Sleepy applications demonstrate Sleepy End Device behavior using the EFR32's low power deep sleep EM2 mode.

- **OpenThread – SoC Sleepy Demo (FTD) (sleepy-demo-ftd):**  An application to start and form a Thread network on a Full Thread Device (FTD) for the sleepy-demo. This application is used in conjunction with the other sleepy demo applications.
- **OpenThread – SoC Sleepy Demo (sleepy-demo-mtd):**  An application to demonstrate Sleepy End Device (SED) behavior on a Minimal Thread Device (MTD) that attaches to a Thread network started by a node running **sleepy-demo-ftd**. This application demonstrates power manager feature support and EM2 mode for the EFR32.
- **OpenThread – SoC Synchronized Sleepy Demo (sleepy-demo-ssed):**  An application to demonstrate SSED behavior using CSL that attaches to a Thread network started by a node running **sleepy-demo-ftd**. This application demonstrates power manager feature support and EM2 mode for the EFR32.

## Building Sleepy Demo Applications

1. With the target part connected to your computer, open Simplicity Studio’s **File** menu and select **New > Silicon Labs Project Wizard**.
2. The Target, SDK, and Toolchain Selection dialog opens. Click **NEXT**.
3. The Example Project Selection dialog opens. Use the Technology Type and Keyword filters to search for “**sleepy demo**” as the keyword.  
   ![Select sleepy demo example](/openthread-sleepy-devices/0.2/images/sld415-image4.png)  
   - To build an FTD that can act as a parent / router for the example, select **sleepy-demo-ftd**.  
   - To demonstrate a regular Sleepy End Device that can work with the **sleepy-demo-ftd** as its parent, select **sleepy-demo-mtd**.  
   - To demonstrate a Synchronized Sleepy End Device that can use CSL with the **sleepy-demo-ftd** as its parent, select **sleepy-demo-ssed**.  
   The Project Configuration dialog opens.
4. Rename the project, change the default project file location, and determine if you will link to or copy project files. Note that, if you change any linked resource, it is changed for any other project that references it. Click **FINISH**.
5. The Simplicity IDE Perspective opens with the Project Configurator open to the **OVERVIEW** tab. See the online Simplicity Studio User’s Guide for details about the functionality available through the Simplicity IDE perspective and the Project Configurator. The following is an example of how the **sleepy-demo-ftd** project will look in this perspective.  
   ![Sleepy-demo-ftd in Project Configurator](/openthread-sleepy-devices/0.2/images/sld415-image5.png)
6. Make any configuration changes to the software components. The autogeneration progress is available in the bottom right of the Simplicity IDE perspective. Make sure that progress is complete before you build.
7. Compile and flash the application image as described in the [OpenThread Quick Start Guide](/openthread/3.0.0/openthread-quick-start-guide).

## Demonstration

For demonstration purposes, the network settings are hardcoded within the source files. Within a few seconds of powering on, the devices start Thread and form a network. In a real-life application, the devices should implement and go through a commissioning process to create a network and add devices.

When the **sleepy-demo-ftd** device is started, the CLI displays:

```C
sleepy-demo-ftd started
sleepy-demo-ftd changed to leader
```

When the **sleepy-demo-mtd** device is started, the CLI displays:

```c
sleepy-demo-mtd started
[poll period: 2000 ms.]
```

The application is configured to join the pre-configured Thread network, disabling Rx-on-when-idle mode to become a Sleepy End Device. The default poll period is set in sleepy-mtd.c.

Issue the command to retrieve child table in the FTD console and observe that the R (Rx-on-when-idle) flag of the child is 0.

```c
> child table
| ID  | RLOC16 | Timeout    | Age        | LQ In | C_VN |R|D|N|Ver|CSL|QMsgCnt|Suprvsn| Extended MAC     |
+-----+--------+------------+------------+-------+------+-+-+-+---+---+-------+-------+------------------+
|   1 | 0x8401 |        240 |          3 |     3 |    3 |0|0|0|  4| 0 |     0 |   129 | 667bf54fcc2aed8a |
Done
```

When the **sleepy-demo-ssed** device is started, the CLI displays:

```c
sleepy-demo-ssed started
[csl period: 500000 us.] [csl timeout: 20 sec.]
```

The application is configured to join the pre-configured Thread network, disabling Rx-on-when-idle mode to become a Synchronous Sleepy End Device. The default CSL parameters are set in sleepy-ssed.c

Issue the command to retrieve the child table in the FTD console and observe that the R (Rx-on-when-idle) flag of the child is 0 and that the CSL flag is 1.

```c
> child table
| ID  | RLOC16 | Timeout    | Age        | LQ In | C_VN |R|D|N|Ver|CSL|QMsgCnt|Suprvsn| Extended MAC     |
+-----+--------+------------+------------+-------+------+-+-+-+---+---+-------+-------+------------------+
|   1 | 0x8402 |        240 |          3 |     3 |    3 |0|0|0|  4| 1 |     0 |   129 | 8e8582dbd78c243c |
Done
```

### Buttons on the MTD/SSED

Pressing button 0 on the MTD/SSED toggles between EM2 (sleep) and EM1 (idle) modes.

Pressing button 1 on the MTD/SSED sends a multicast UDP message containing a pre-defined string. The FTD listens on the multicast address and displays “Message Received: <string>” in the CLI.

### Buttons on the FTD

Pressing either button 0 or 1 on the FTD sends a UDP message to the FTD containing the string "ftd button". Before pressing either button on the FTD, press the MTD's or SSED's button 1 to send a multicast message so that the FTD knows the address of the sleepy device to send messages to.

### Monitoring Power Consumption of the MTD/SSED

Open the Energy Profiler in Simplicity Studio 5 (SSv5). In the Quick Access menu select _**Start Energy Capture...**_ and select the MTD / SSED device. For further information on monitoring power consumption and energy profiler, see _Multi-Node Energy Profiler_ in [Silicon Labs OpenThread QuickStart Guide](/openthread/3.0.0/openthread-quick-start-guide/05-development-tools/multi-node-energy-profiler).

### Notes on Sleeping, Sleepy Callback, and Interrupts

To allow the EFR32 to enter sleepy mode, the application must register a callback with efr32SetSleepCallback. The return value of the callback is used to indicate that the application has no further work to do and that it is safe to go into a low power mode. Because the callback is called with interrupts disabled, it should do the minimum required to check if it can sleep.