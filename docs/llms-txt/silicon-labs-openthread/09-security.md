# Source: https://docs.silabs.com/openthread/3.0.0/thread-fundamentals/09-security.md

# Security

Thread networks are wireless networks that need to be secured against over-the-air (OTA) attacks. They are also connected to the internet and therefore must be secured against internet attacks. Many of the applications being developed for Thread will serve a broad range of uses that require long periods of unattended operation and low power consumption. As a result, the security of Thread networks is critical.

Thread utilizes a network-wide key that is used at the Media Access Layer (MAC) for encryption. This key is used for standard IEEE 802.15.4-2006 authentication and encryption. IEEE 802.15.4-2006 security protects the Thread network from over-the-air attacks originating from outside the network. Compromise of any individual node could potentially reveal the network-wide key. As a result, it is usually not the only form of security used within the Thread network. Each node in the Thread network exchanges frame counters with its neighbors via an MLE handshake. These frame counters help protect against replay attacks. (For more information on MLE, see the Thread Specification.) Thread allows the application to use any internet security protocol for end-to-end communication.

Nodes obfuscate both their mesh-wide IP address interfaces and their MAC extended IDs by randomizing them. The stock EUI64 assigned to the node is used as a source address only during the initial join phase. Once a node is joined to a network, the node uses as its source either an address based on its two-byte node ID, or one of its randomized addresses mentioned above. The EUI64 is not used as a source address once the node is joined to a network.

Network management also needs to be secure. A Thread network management application can be run on any internet-connected device. If that device is not itself a member of a Thread network, it must first establish a secure Datagram Transport Layer Security (DTLS) connection with a Thread Border Router. Every Thread network has a management passphrase that is used in establishing this connection. Once a management application has been connected to the Thread network, new devices can be added to the network.

## 802.15.4 Security

The IEEE 802.15.4-2006 specification describes wireless and media access protocols for PANs and HANs. These protocols are intended for implementation on dedicated radio devices such as those available from Silicon Labs. IEEE 802.15.4-2006 supports a variety of applications, many of which are security-sensitive. For example, consider the case of an alarm system application that monitors building occupancy. If the network is not secure and an intruder gains access to the network, messages could be broadcast to create a false alarm, modify an existing alarm, or silence a legitimate alarm. Each of these situations poses significant risks to the building occupants.

Many applications require confidentiality and most also need integrity protection. 802-15.4-2006 addresses these requirements by using a link layer security protocol with four basic security services:

- Access control
- Message integrity
- Message confidentiality
- Replay protection

The replay protection provided by IEEE 802.15.4-2006 is only partial. Thread delivers additional security using MLE handshakes between nodes discussed above to complete the replay protection.

## Secure Network Management

Network management also needs to be secure. A Thread network management application can be run on any internet-connected device. There are two parts to the security:

- Over-the-air security which 802.15.4 takes care of. Thread implements 802.15.4-2006 level 5 security.
- CCM networks: If a device is not itself a member of a CCM network, it must establish a connection with a backbone border router in order to obtain its operational certificate to establish itself as part of the Thread domain.
- Non-CCM networks: Internet security: If a device is not itself a member of a Thread network, it must first establish a secure Datagram Transit Layer Security (DTLS) connection with a Thread Border Router. Every Thread network has a management passphrase that is used for establishing secure connections between external management devices and Border Routers. Once a management application has been connected to the Thread network, new devices can be added to the network.