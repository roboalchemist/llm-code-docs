# Source: https://docs.silabs.com/openthread/3.0.0/thread-fundamentals/12-application-layer.md

# Application Layer

Thread is a wireless mesh networking stack that is responsible for routing messages between different devices in the Thread network described in [Thread Technology Overview](./02-thread-technology-overview). The following figure illustrates the layers in the Thread protocol.

![Thread Protocol Layers](/thread-fundamentals/0.1/images/thread-protocol-layers.jpg)

A standard definition of an application layer is an ["abstraction layer that specifies the shared protocols and interface methods used by hosts in a communications network"](https://en.wikipedia.org/wiki/Application_layer). Put more simply, an application layer is the "language of devices," for example, how a switch talks to a light bulb. Using these definitions, an application layer does not exist in Thread. Customers build the application layer based on the capabilities in the Thread stack and their own requirements. Although Thread does not supply an application layer, it does provide basic application services:

- UDP messaging  
  UDP offers a way to send messages using a 16-bit port number and an IPv6 address. UDP is a simpler protocol than TCP and has less connection overhead (for example, UDP does not implement keep-alive messages). As a result, UDP enables a faster, higher throughput of messages and reduces the overall power budget of an application. UDP also has a smaller code space than TCP, which leaves more available flash on the chip for custom applications.
- Multicast messaging  
  Thread provides the ability to broadcast messages, that is, sending the same message to multiple nodes on a Thread network. Multicast allows a built-in way to talk to neighbor nodes, routers, and an entire Thread network with standard IPv6 addresses.
- Application layers using IP services  
  Thread allows the use of application layers such as UDP and CoAP to allow devices to communicate interactively over the Internet. Non-IP application layers will require some adaptation to work on Thread. (See [RFC 7252](https://tools.ietf.org/html/rfc7252) for more information on CoAP.)

The Silicon Labs OpenThread SDK includes the following sample applications that are also available from the OpenThread GitHub repository:

- ot-cli-ftd
- ot-cli-mtd
- ot-rcp (used in conjunction with an OpenThread Border Router)

These applications can be used to demonstrate the features of a Thread network. In addition, the Silicon Labs OpenThread SDK also provides a sleepy end device sample app (sleepy-demo-ftd and sleepy-demo-mtd), which demonstrates how to use the Silicon Labs power manager features to create a low power device. Finally, the ot-ble-dmp sample application demonstrates how to build a dynamic multiprotocol application using OpenThread and the Silicon Labs Bluetooth stack. See the [OpenThread Quick-Start Guide](/openthread/3.0.0/openthread-quick-start-guide) for more information on working with example applications in Simplicity Studio.
