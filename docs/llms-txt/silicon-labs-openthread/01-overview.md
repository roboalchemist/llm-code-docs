# Source: https://docs.silabs.com/openthread/3.0.0/iot-endpoint-security-fundamentals/01-overview.md

# Source: https://docs.silabs.com/openthread/3.0.0/bootloader-user-guide-gsdk-4/01-overview.md

# Source: https://docs.silabs.com/openthread/3.0.0/bootloader-fundamentals/01-overview.md

# Source: https://docs.silabs.com/openthread/3.0.0/wireless-networking-application-development-fundamentals/01-overview.md

# Source: https://docs.silabs.com/openthread/3.0.0/thread-fundamentals/01-overview.md

# Introduction

## Silicon Labs and the Internet of Things

Internet Protocol version 4 (IPv4) was defined in 1981 in RFC 791, [DARPA Internet Program Protocol Specification](https://datatracker.ietf.org/doc/html/rfc791) ("RFC" stands for "Request for Comments."). Using 32-bit (4-byte) addressing, IPv4 provided 232 unique addresses for devices on the internet, a total of approximately 4.3 billion addresses. However, as the number of users and devices grew exponentially, it was clear that the number of IPv4 addresses would be exhausted and there was a need for a new version of the IP. Hence the development of IPv6 in the 1990s and its intention to replace IPv4. With 128-bit (16-byte) addressing, IPv6 allows for 2128 addresses, more than 7.9x1028 addresses than IPv4 ([http://en.wikipedia.org/wiki/IPv6](http://en.wikipedia.org/wiki/IPv6)).

The challenge for companies in the embedded industry like Silicon Labs is to address this technology migration and more importantly the demands of customers as we move to an ever-connected world of devices in the home and commercial space, what is often refer-red to as the Internet of Things (IoT). At a high level the goals of IoT for Silicon Labs are to:

- Connect all the devices in the home and commercial space with best-in-class networking, whether with Zigbee PRO, Thread, Blue-tooth, or other emerging standards.
- Leverage the company's expertise in energy-friendly microcontrollers.
- Enhance established low-power, mixed-signal chips.
- Provide low-cost bridging to existing Ethernet and Wi-Fi devices.
- Enable cloud services and connectivity to smartphones and tablets that will promote ease of use and a common user experience for customers.

Achieving all of these goals will increase adoption rates and user acceptance for IoT devices.

## Thread Group

[Thread Group](https://www.threadgroup.org/) was launched on July 15, 2014. Silicon Labs was a founding company along with six other companies. Thread Group is a market education group that offers product certification and promotes the use of Thread-enabled device-to-device (D2D) and machine-to-machine (M2M) products. Membership in Thread Group is open.

Thread Specification 1.4.0 may be downloaded after submitting a request here: [Thread Specification Request Form](https://www.threadgroup.org/ThreadSpec). The latest 1.4.1-draft Thread specification is only available to Thread members (as of the release of this document).

## What is Thread?

Thread is a secure, wireless mesh networking protocol. The Thread stack is an open standard that is built upon a collection of existing Institute for Electrical and Electronics Engineers (IEEE) and Internet Engineering Task Force (IETF) standards, rather than a whole new standard (see the following figure).

![Thread Stack Overview](/thread-fundamentals/0.1/images/thread-stack-overview.jpg)

## Thread General Characteristics

The Thread stack supports IPv6 addresses and provides low-cost bridging to other IP networks and is optimized for low-power / battery-backed operation, and wireless device-to-device communication. The Thread stack is designed specifically for Connected Home and commercial applications where IP-based networking is desired and a variety of application layers can be used on the stack.

These are the general characteristics of the Thread stack:

- **Simple network installation, start-up, and operation**: The Thread stack supports several network topologies. Installation is simple using a smartphone, tablet, or computer. Product installation codes are used to ensure only authorized devices can join the network. The simple protocols for forming and joining networks allow systems to self-configure and fix routing problems as they occur.
- **Secure**: Devices do not join the network unless authorized and all communications are encrypted and secure. Security is provided at the network layer and can be at the application layer. All Thread networks are encrypted using a smartphone-era authentication scheme and Advanced Encryption Standard (AES) encryption. The security used in Thread networks is stronger than other wireless standards the Thread Group has evaluated.
- **Small and large home networks**: Home networks vary from several to hundreds of devices. The networking layer is designed to optimize the network operation based on the expected use.
- **Large commercial networks**: For larger commercial installations, a single Thread network is not sufficient to cover all the application, system and network requirements. The Thread Domain model allows scalability for up to 10,000s of Thread devices in a single deployment, using a combination of different connectivity technologies (Thread, Ethernet, Wi-fi, and so on).
- **Bi-directional service discovery and connectivity**: Multicast and broadcast are inefficient on wireless mesh networks. For off-mesh communication, Thread provides a service registry where devices can register their presence and services, and clients can use unicast queries to discover the registered services.
- **Range**: Typical devices provide sufficient range to cover a normal home. Readily available designs with power amplifiers extend the range substantially. A distributed spread spectrum is used at the Physical Layer (PHY) to be more immune to interference. For commercial installations, the Thread Domain model allows multiple Thread networks to communicate with each other over a backbone, thus extending the range to cover many mesh subnets.
- **No single point of failure**: The Thread stack is designed to provide secure and reliable operations even with the failure or loss of individual devices.  Thread devices can also incorporate IPv6-based links such as Wi-Fi and Ethernet into the topology to reduce the probability of multiple Thread partitions. This way, they can utilize the higher throughput, channel capacity, and coverage of those infrastructure links, while still supporting low-power devices.
- **Low power**: Devices efficiently communicate to deliver an enhanced user experience with years of expected life under normal battery conditions. Devices can typically operate for several years on AA type batteries using suitable duty cycles.
- **Cost-effective**: Compatible chipsets and software stacks from multiple vendors are priced for mass deployment and designed from the ground up to have extremely low-power consumption.

## OpenThread

OpenThread released by Google is an open-source implementation of Thread®. Google has released OpenThread to make the networking technology used in Google Nest products more broadly available to developers, in order to accelerate the development of products for the connected home and commercial buildings.

With a narrow platform abstraction layer and a small memory footprint, OpenThread is highly portable. It supports system-on-chip (SoC), network co-processor (NCP), and radio co-processor (RCP) designs.

OpenThread defines an IPv6-based reliable, secure, and low-power wireless device-to-device communication protocol for home and commercial building applications. It implements all features defined up to draft Thread Specification 1.4.1 (as of the release of this document).

Silicon Labs has implemented an OpenThread-based protocol tailored to work with Silicon Labs hardware. This protocol is available on GitHub and also as a software development kit (SDK) installed with Simplicity Studio. The SDK is a fully tested snapshot of the GitHub source. It supports a broader range of hardware than does the GitHub version, and includes documentation and example applications not available on GitHub.