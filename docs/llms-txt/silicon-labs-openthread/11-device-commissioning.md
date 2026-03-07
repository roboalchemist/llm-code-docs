# Source: https://docs.silabs.com/openthread/3.0.0/thread-fundamentals/11-device-commissioning.md

# Device Commissioning

Thread devices are commissioned on Thread networks in different ways as described in the following subsections.

## Traditional Thread Commissioning

For the network commissioning of smaller networks (Thread Specification 1.1.1 or higher), installers can use the Thread commissioning app provided as a free resource for Android and iOS devices. This app can be used to easily add new devices to the network or reconfigure existing devices.

Thread uses the Mesh Commissioning Protocol (MeshCoP) to securely authenticate, commission, and join new, untrusted radio devices to a mesh network. Thread networks comprise an autonomous self-configuring mesh of devices with IEEE 802.15.4 interfaces and a link-level security layer that requires each device in the mesh to possess the current, shared secret master key.

The commissioning process begins when a Commissioner Candidate, typically a mobile phone connected via WiFi, discovers the Thread network through one of its Border Routers. Border Routers advertise their availability to Commissioners using whatever service location is appropriate. The discovery mechanism must provide a Commissioner Candidate with both a communication path and the network name, because the network name is used later as a cryptographic salt for establishing the Commissioning Session.

The Commissioner Candidate, after having discovered the Thread network of interest, securely connects to it using the Commissioning Credential (a human-selected passphrase for use in authenticating). The Commissioner Authentication step establishes a secure client/server socket connection between the Commissioner Candidate and a Border Router via DTLS. This secure session is known as a Commissioning Session. The Commissioning Session uses the assigned UDP port number advertised during the discovery phase. This port is known as the Commissioner Port. The credential used to establish the Commissioning Session is known as the Pre-Shared Key for the Commissioner (PSKc).

The Commissioner Candidate then registers its identity with its Border Router. The Leader responds by either accepting or rejecting the Border Router as a viable forwarder to the Commissioner. Upon acceptance, the Leader updates its internal state to track the active Commissioner, and the Border Router then sends a confirmation message to the Commissioner Candidate informing the device that it is now the Commissioner.

When there is an authorized Commissioner associated with the Thread Network, it becomes possible to join eligible Thread Devices. These are known as Joiners before they become part of the Thread network. The Joiner first creates a DTLS connection with the Commissioner to exchange commissioning material. It then uses the commissioning material to attach to the Thread network. The node is considered part of the network only after these two steps are complete. It may then participate in the join process for future nodes. All of these steps confirm that the correct device has joined the correct Thread network, and that the Thread network itself is secure against wireless and internet attacks. For more information on the Mesh Commissioning Protocol, see the Thread specification.

## Enhanced Commissioning with Commercial Extensions in Thread 1.2

Thread Specification 1.2 and its Commercial Extensions now allow for much larger scale networks, such as the ones required in office buildings, public buildings, hotels, or other types of industrial or commercial buildings. Due to better support of subnetting, Thread Specification 1.2 more easily allows thousands of devices in one deployment, which can be configured manually, autonomously, and via advanced remote commissioning features.

The Commercial Extensions in Thread 1.2 allow for large-scale authentication, network joining, subnet roaming, and operation based on trusted identities in an Enterprise Domain. To enable reliable authentication of devices and verification of authorization information, a system installer can set up an Enterprise Certificate Authority to simplify deploying a large-scale network. This allows the installer to set up and maintain the network without direct access to the individual devices and without any direct interaction with these devices, by means of an automated enrollment process called Autonomous Enrollment. Unlike Thread 1.1, where device passcode pairing is used for authentication, the Commercial Extensions in Thread 1.2 will support a more scalable certificate-based form of authentication. An enterprise network can have one or more Thread Domains and each Thread Domain can be set up to integrate multiple Thread networks.