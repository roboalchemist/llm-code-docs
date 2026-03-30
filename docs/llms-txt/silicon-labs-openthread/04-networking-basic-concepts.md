# Source: https://docs.silabs.com/openthread/3.0.0/wireless-networking-application-development-fundamentals/04-networking-basic-concepts.md

# Networking: Basic Concepts

A _network_ is a system of computers and other devices (such as printers and modems) that are connected in such a way that they can exchange data. This data may be informational or command-oriented, or a combination of the two.

A _networking system_ consists of hardware and software. Hardware on a network includes physical devices such as computer workstations, peripherals, and computers acting as file servers, print servers, and routers. These devices are all referred to as _nodes_ on the network.

If the nodes are not all connected to a single physical cable, special hardware and software devices must connect the different cables in order to forward messages to their destination addresses. A _bridge or repeater_ is a device that connects networking cables without examining the addresses of messages or making decisions as to the best route for a message to take. In contrast, a _router_ contains addressing and routing information that lets it determine, from a message's address, the most efficient route for the message. A message can be passed from router to router several times before being delivered to its target destination.

In order for nodes to exchange data, they must use a common set of rules defining the format of the data and the manner in which it is to be transmitted. A _protocol_ is a formalized set of procedural rules for the exchange of data. The protocol also provides rules for the interactions among the network's interconnected nodes. A network software developer implements these rules in software applications that carry out the functions required by the protocol.

Whereas a router can connect networks only if they use the same protocol and address format, a _gateway_ converts addresses and protocols to connect dissimilar networks. Such a set of interconnected networks can be referred to as an internet, intranet, wide area network (WAN), or other specialized network topology. The term Internet is often used to refer to the largest worldwide system of networks, also called the World Wide Web. The basic protocol used to implement the World Wide Web is called the Internet protocol, or IP.

A networking protocol commonly uses the services of another, more fundamental protocol to achieve its ends. For example, the Transmission Control Protocol (TCP) uses the IP to encapsulate the data and deliver it over an IP network. The protocol that uses the services of an underlying protocol is said to be a client of the lower protocol; for example, TCP is a client of IP. A set of protocols related in this fashion is called a _protocol stack_.