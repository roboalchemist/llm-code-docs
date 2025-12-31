# Source: https://developer.nvidia.com/networking/ethernet-switch-sdk.md

# NVIDIA Ethernet Switch SDK and SAI

The optimized SDK for high-performance Ethernet switches.

The NVIDIA® Ethernet Switch SDK provides the flexibility to implement any switching and routing functionality, with sophisticated programmability that doesn’t compromise performance in packet rate, bandwidth, or latency. With the SDK, server and networking OEMs and network operating system (NOS) vendors can take advantage of **the advanced networking features** of the Ethernet switch family of integrated circuits (ICs) and build flexible, innovative, and cost-optimized switching solutions.  
  
 SAI (Switch Abstraction Interface) defines a community-standard API, providing a vendor-independent way of controlling an Ethernet Switch ASIC. NVIDIA is a founding member of SAI and has been part of the governance board since 2014. NVIDIA&#39;s SAI implementation offers a subset of the functionalities available in the NVIDIA SDK.

  

Apply for access to NVIDIA Spectrum Ethernet Switch SDK and SAI documentation and code. Please log in or create an account using a business email address. Applications using personal accounts (e.g., @gmail, @yahoo) won’t be accepted. An NVIDIA representative may reach out to you through Email to be accepted to participate in this program.

Access will only be approved after signing an SDK license agreement. For more information, please reach out to an NVIDIA representative.

  
[Join now](/networking/ethernet-switch-sdk/join)

* * *

## Typical Use Cases for the Ethernet Switch SDK

**The Ethernet Switch SDK offers a flexible business model with multiple development paths:**

- From the application-specific integrated circuit (ASIC) up, build your own switch hardware, PCB, and system and develop a NOS.
- Start from a wide selection of white-box options, and develop your own NOS running on production-ready hardware. NVIDIA offers hardware customization and rebranding.
- Run on top of SONiC to benefit from an existing NOS and develop your own containerized application with access to the switch ASIC. This path is typically for applications not part of a mainstream switch or router NOS.

  

**The Ethernet Switch SDK is an open, flexible, high-performance infrastructure for building private clouds to develop powerful applications. The typical users are:**

- Cloud service providers (CSPs) who build their own gear for self-consumption
- Original equipment manufacturers (OEMs) for applications such as Ethernet Bunch of Flash (eBOF), embedded connectivity (5G for telecommunications), and tactical equipment
- OEMs for applications such as TAP aggregation, packet brokering, security appliances such as firewalls, and networking test equipment
- Original design manufacturers (ODMs) developing tailored solutions for deployments that off-the-shelf switches cannot support, such as analytics services

* * *

## Powerful and Flexible SDK

- Single, consistent API model across the entire Ethernet switch family of switch ASICs
- Proven with 10+ years in production
- Multi-threaded on multiple CPU architectures
- Container with SDK access on an existing NOS
- Easily portable code base for fast time to market
- Linux development environment
- API library written in ANSI C
- Python libraries for fast development and prototyping

 ![](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/networking/nvidia-diagram-spectrum-asic.svg)

* * *

## Development Environment

 ![](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/networking/nvidia-icon-sdk-dvs-os_0.svg)

**Rapid Feature Development**  
  
 NVIDIA development systems (DVS) and DVS-OS with native Linux are used as the development environment:  
  

- Open Network Linux based on Debian 9.2 (Kernel 4.9) base OS
- Open Network Installation Environment (ONIE)
- Straightforward, practical feature usage by example, supported on every Ethernet platform. Code examples in Python and C
- User-friendly development environment, including everything needed to build and debug the SDK, switch abstraction interface (SAI), and NVIDIA What Just Happened® (WJH)

* * *

## Key Features

- **Unified forwarding capacity** – Up to 12.8 terabits per second (Tb/s) with up to 128 low-latency ports running from 1GbE to 400GbE
- **Layer 1** – Port interfaces, speeds, and form factors. Cables (including split) and transceivers.
- **Layer 2 switching** – 802.1Q, 802.1D, LAG, STP, MSTP, PVRST, QinQ, IGMP snooping with (\*,G) and (S,G) support. SFLOW and port mirroring (SPAN, RSPAN, ERSPAN), port isolation, 802.1X.
- **Layer 3 routing** – VLAN and physical port router interface, VRF, IPv4 and IPv6 unicast and multicast routing. Router interface and router counters. Shared ECMP containers. Tunneling, IPinIP, VxLAN, and QinVXLAN. PIM-EVPN and EVPN multihoming. MPLS, BFD.
- **Quality of Service (QoS)** – RDMA over Converged Ethernet (RoCE) support. Dynamic shared buffers configuration and monitoring. Bridge-level storm control policers. RED, ECN. Flow control and priority flow control (PFC). ETS. Port and TC-based policers and shapers. HLL and SLL monitoring and configuration.
- **Lossless traffic and performance** – Facilities to set priorities per port, per virtual port, and per traffic flow. Efficient traffic for latency and bandwidth, buffer management, and QoS resources.
- **Flexible programmability and ACL** – Predefined L2, L3, L4, and above match keys. Flexible and user-defined match keys. Parsing and lookup on the first 256 bytes of the packet’s header. Multiple ingress and egress binding points for ACL, pipeline overwrite actions, packet flexible modifier actions, policy and classification actions, redirect actions, and tunnel and mirror actions.

- **Telemetry and visibility** – What Just Happen (WJH) event-based visibility with raw and aggregated data streaming. Buffer utilization visibility, histograms, and thresholds. Unit-based counters and generic flow flexible counters.
- **In-service software upgrade (ISSU)** – Zero-hit traffic loss for zero downtime of the data plane. Fast boot for minimizing traffic hits.
- **Precision Timing Protocol (PTP)** – 1588v2 with as low as 5ns accuracy.
- **AI switching** – 200GbE, adaptive routing, congestion control with dynamic resource allocation.
- **Resource management** – Centralized resources management module with utilization and prediction capabilities. The SDK provides access to the maximum available capacity of the configuration and forwarding tables
- **Debuggability** – Logging facilities, SDK dump, and API recorder and player. Interactive Python buildings and example scripts.
- **Host** – Flexible control packets trap to host CPU. Policing and rate limiting to host CPU. Netdev per port/LAG and bridge Linux kernel integration. User space file descriptor-based packet send and receive. Iterators for every allocable SDK object. Convenient logging for debugging and troubleshooting. System debug information collection script. Precompiled packages for CentOS- and Debian-based systems. 


