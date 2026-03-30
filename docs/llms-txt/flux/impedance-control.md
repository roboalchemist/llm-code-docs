# Source: https://docs.flux.ai/reference/impedance-control.md

# Impedance Control

Set up differential pair or single-ended impedance-controlled lines.

![](https://uploads.developerhub.io/prod/86Yw/wuadlqiktt5hqmvjj80366djzraz9lxs17uazvp1rvuj2uft5a335b72mfmy0v1g.png)

## Overview

Impedance control in Flux is defined at a part level instead of at a project level. Meaning that parts that require impedance control or differential pair routing come pre-configured with all the required parameters. This implementation greatly simplifies the routing process and reduces busy work. 

Learn more about impedance control in this [tutorial.](https://docs.flux.ai/flux/tutorials/advanced-routing)

## Configuring Impedance Control

There are two ways of configuring impedance control for a part:

- **Automatic setup:** this is the recommended process as it only requires part pins to be properly named.
- **Manual setup:** it’s also possible to manually add parameters directly to the pins.

## Automatic Setup

Flux will automatically add the right parameters to every terminal in the part if the “Part Type” property is set to any of the supported interfaces listed below.

| Supported Interfaces | 
| ---- | 
| USB A, USB B, USB C, HDMI, PCIe x1, PCIe x2, PCIe x4, PCIe x8, PCIe x16, MIPI CSI, MIPI DSI, DDR3, DDR4 | 


For an interface to be automatically configured, the terminal's name in the part need to follow one of the following names_

|  | Compatible Terminal Names | 
| ---- | ---- | 
| USB 2.0 | "d+"\n\n\n\n        "d-"\n\n\n        dp\n\n\n\n        dn\n\n\n\n        dm\n\n\n\n        "data+"\n\n\n\n        "data-"\n\n\n        dp1\n\n\n\n        dn2\n\n\n\n        p\n\n\n\n        n\n\n\n\n        usb_dp\n\n\n\n        usb_dm | 
| USB 3. | txp\n\n\n\n        txn\n\n\n\n        "tx+"\n\n\n\n        "tx-"\n\n\n        txm\n\n\n\n        sstxp1\n\n\n\n        sstxn1\n\n\n\n        "dptx+"\n\n\n\n        "dptx-"\n\n\n        "superspeed_tx+"\n\n\n\n        "superspeed_tx-"\n\n\n        "rx+"\n\n\n\n        "rx-"\n\n\n        rxp\n\n\n\n        rxn\n\n\n\n        rxm\n\n\n\n        ssrxp1\n\n\n\n        ssrxn1\n\n\n\n        "rx2+"\n\n\n\n        "rx2-"\n\n\n        "dprx2+"\n\n\n\n        "dprx2-"\n\n\n        "superspeed_rx2+"\n\n\n\n        "superspeed_rx2-"\n\n\n        vbus | 
| MIPI | "dp0+"\n\n\n\n        "dp0-"\n\n\n        "dp1+"\n\n\n\n        "dp1-"\n\n\n        "dp2+"\n\n\n\n        "dp2-"\n\n\n        "dp3+"\n\n\n\n        "dp3-"\n\n\n        "dp4+"\n\n\n\n        "dp4-"\n\n\n        data_p0\n\n\n\n        data_n0\n\n\n\n        data_p1\n\n\n\n        data_n1\n\n\n\n        data_p2\n\n\n\n        data_n2\n\n\n\n        data_p3\n\n\n\n        data_n3\n\n\n\n        data_p4\n\n\n\n        data_n4\n\n\n\n        "d0+"\n\n\n\n        "d0-"\n\n\n        "d1+"\n\n\n\n        "d1-"\n\n\n        "d2+"\n\n\n\n        "d2-"\n\n\n        "d3+"\n\n\n\n        "d3-"\n\n\n        "d4+"\n\n\n\n        "d4-"\n\n\n        "clk+"\n\n\n\n        "clk-"\n\n\n        clock_p\n\n\n\n        clock_n | 
| HDMI | "data0+"\n\n\n\n        "data0-"\n\n\n        "data1+"\n\n\n\n        "data1-"\n\n\n        "data2+"\n\n\n\n        "data2-"\n\n\n        "data3+"\n\n\n\n        "data3-"\n\n\n        "d0+"\n\n\n\n        "d0-"\n\n\n        "d1+"\n\n\n\n        "d1-"\n\n\n        "d2+"\n\n\n\n        "d2-"\n\n\n        "d3+"\n\n\n\n        "d3-"\n\n\n        "in_d0+"\n\n\n\n        "in_d0-"\n\n\n        "in_d1+"\n\n\n\n        "in_d1-"\n\n\n        "in_d2+"\n\n\n\n        "in_d2-"\n\n\n        "in_d3+"\n\n\n\n        "in_d3-"\n\n\n        "out_d0+"\n\n\n\n        "out_d0-"\n\n\n        "out_d1+"\n\n\n\n        "out_d1-"\n\n\n        "out_d2+"\n\n\n\n        "out_d2-"\n\n\n        "out_d3+"\n\n\n\n        "out_d3-"\n\n\n        data0_p\n\n\n\n        data0_n\n\n\n\n        data1_p\n\n\n\n        data1_n\n\n\n\n        data2_p\n\n\n\n        data2_n\n\n\n\n        data3_p\n\n\n\n        data3_n\n\n\n\n        "tmds data0+"\n\n\n\n        "tmds data0-"\n\n\n        "tmds data1+"\n\n\n\n        "tmds data1-"\n\n\n        "tmds data2+"\n\n\n\n        "tmds data2-"\n\n\n        "tmds data3+"\n\n\n\n        "tmds data3-"\n\n\n        "tmds data 0+"\n\n\n\n        "tmds data 0-"\n\n\n        "tmds data 1+"\n\n\n\n        "tmds data 1-"\n\n\n        "tmds data 2+"\n\n\n\n        "tmds data 2-"\n\n\n        "tmds data 3+"\n\n\n\n        "tmds data 3-"\n\n\n        "tmds clock+"\n\n\n\n        "tmds clock-"\n\n\n        "tmds_d0+"\n\n\n\n        "tmds_d0-"\n\n\n        "tmds_d1+"\n\n\n\n        "tmds_d1-"\n\n\n        "tmds_d2+"\n\n\n\n        "tmds_d2-"\n\n\n        "tmds_d3+"\n\n\n\n        "tmds_d3-"\n\n\n        "tmds_ck+"\n\n\n\n        "tmds_ck-"\n\n\n        "d_in0+"\n\n\n\n        "d_in0-"\n\n\n        "d_in1+"\n\n\n\n        "d_in1-"\n\n\n        "d_in2+"\n\n\n\n        "d_in2-"\n\n\n        "d_in3+"\n\n\n\n        "d_in3-"\n\n\n        "clk+"\n\n\n\n        "clk-"\n\n\n        "clock+"\n\n\n\n        "clock-"\n\n\n        clock_p\n\n\n\n        clock_n\n\n\n\n        in_clkp\n\n\n\n        in_clkn\n\n\n\n        out_clkp\n\n\n\n        out_clkn | 
| PCI | a2\n\n\n\n        a3\n\n\n\n        a5\n\n\n\n        a6\n\n\n\n        a14\n\n\n\n        a15\n\n\n\n        a17\n\n\n\n        a18\n\n\n\n        a11\n\n\n\n        a12\n\n\n\n        rxa0p\n\n\n\n        rxa0n\n\n\n\n        rxa1p\n\n\n\n        rxa1n\n\n\n\n        rxa2p\n\n\n\n        rxa2n\n\n\n\n        rxa3p\n\n\n\n        rxa3n\n\n\n\n        tx0p\n\n\n\n        tx0n\n\n\n\n        tx1p\n\n\n\n        tx1n\n\n\n\n        tx2p\n\n\n\n        tx2n\n\n\n\n        tx3p\n\n\n\n        tx3n | 


## Manual  Setup

If you’re configuring impedance control for an interface that is not currently supported, you’ll need to add the parameters to every terminal manually. Below is a list of all the parameters that need to be configured:

### Flux-Defined properties

#### Defined at component level

- **Bus Type:** target interface. For example HDMI, PCIe or USB

#### Defined at terminal level

- **Bus Group:** this property defines the different differential pairs. Some interfaces might require many different bus groups (like ethernet), while others only require one (like USB2.0). For example, if a microcontroller contains two USB buses, terminals for one bus should contain “Bus Group” = USB_1 and terminals in the second bus should contain “Bus Group” = USB_ 2
- **Pair Role:** defines what type of role the terminal has. For example CLK, D1, D2, D3, D4, TX, TX1, TX2, TX3, RX, RX1, RX2, RX3, etc.
- **Controlled Impedance Pair:** this should be a unique name that identifies the pair. This is particularly important for parts that contain more than one bus. For example in a part with two USB buses, you will have two Data 1 pairs. In that case one pair could be named “Data1_Bus1” and the other pair “Data1_Bus2”. You can follow any naming convention you prefer, the only requirement is that each pair has a unique “Controlled Impedance Pair” string. 

### Impedance Constraints

- **Controlled Impedance:** target impedance, measured in Ohms.
- **Controlled Impedance Tolerance:** how much the actual impedance can vary with respect to the “Controlled Impedance” property, measured in %.

These rules configure the impedance parameters that need to be obeyed and are usually part of the interface specifications. For example, USB 3.2 Gen 2 (10 Gbps) requires VBUS=90Ω±15% and D+ and D- =90Ω±7.5%

### Differential Pair Constraints

- **PN Skew Max:** the maximum time difference tolerated for signals between the two terminals in the pair, measured in pico-seconds.
- **Pin Delay:** specifies the time delay from the IC to the terminal connection point, measured in ps.

### Bus Constraints

- **Pair to Pair Skew Max:** the maximum time difference tolerated for signals between the two different pairs in a bus, for example, data and clock lines. 

## Limitations

The following features will be supported in the next releases:

- Squiggles
- Multi-tracing for bus:
    - PCIe
    - HDM
    - Ethernet

- DRC Checks
    - DRC for length matching
    - DRC for ground underneath
    - DRC for trace spacing (uncoupled length)