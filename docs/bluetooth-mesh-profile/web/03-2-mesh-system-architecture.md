# Source: https://www.bluetooth.com/wp-content/uploads/Files/Specification/HTML/MshPRT_v1.1/out/en/index-en.html

## 2. Mesh system architecture

This section provides an overview of the mesh network operation and layered system architecture.

### 2.1. Layered architecture

The Mesh Protocol specification is defined as a layered architecture as shown in [Figure 2.1](index-en.html#UUID-5a00137e-ae3d-00cf-cd29-abf59856cf26_Figure_2.1 "Figure 2.1. Mesh system architecture"). The architecture includes two stacks – the mesh networking stack
used by mesh nodes to communicate with each other (see [Sections 3](index-en.html#UUID-bfac145c-378b-4427-a2d0-d37745433ed1 "3. Mesh networking"), [4](index-en.html#UUID-c2bbeabd-dcd8-c62a-d660-b83abb347dda "4. Foundation models"), and [[9](index-en.html#idp254760)]), and the mesh provisioning stack (see [Section 5](index-en.html#UUID-c2ed2695-c7e2-6000-08bb-72c4b7c7e7fe "5. Provisioning")) used to provision
devices on the network.

Both stacks are built on top of the LE Physical Transport defined in the Bluetooth Core Specification (see Vol 1, Part A, Section 3.2 in [[24](index-en.html#idp254804)]). Mesh profiles are optional specifications that define use cases and implementation patterns to help
improve interoperability and performance of systems based on Bluetooth mesh, such as networked lighting control systems or sensor networks.

Each layer of a stack processes the given messages and may deliver the processed messages to the next layer for further processing. The processing may involve, for example, encryption, decryption, the packing or unpacking of fields, or the execution of certain behaviors as indicated by data fields in the message.

During the course of processing, a layer can attach certain metadata, called tags, to a message in order to inform subsequent layers to customize the processing of the message for specific functionality. This process of attaching metadata to a message is called tagging.

The architecture is illustrated in [Figure 2.1](index-en.html#UUID-5a00137e-ae3d-00cf-cd29-abf59856cf26_Figure_2.1 "Figure 2.1. Mesh system architecture"). The layers shown in blue are defined in this specification. The layers and profiles shown in green are defined
in other specifications.

|  |
| --- |
| Mesh system architecture |

Figure 2.1. Mesh system architecture

#### 2.1.1. Model layer

Models are used to standardize the operation of typical user scenarios.

The model layer specifies the rules for allocating models on elements within a node.

The model layer also includes models which are defined in the Mesh Model specification [[9](index-en.html#idp254760)] or in other higher-layer specifications.

#### 2.1.2. Foundation Model layer

The foundation model layer defines the states, messages, and models required to configure and manage a mesh network.

#### 2.1.3. Access layer

The access layer defines how higher layer applications can use the upper transport layer. It defines the format of the application data; it defines and controls the application data encryption and decryption performed in the upper transport layer; and it checks whether the incoming application data has been received in the
context of the right network and application keys before forwarding it to the higher layer.

#### 2.1.4. Upper transport layer

The upper transport layer encrypts, decrypts, and authenticates application data and is designed to provide confidentiality of Access messages. It also defines how Transport Control messages are used to manage the upper transport layer between nodes, including when used by the Friend feature and by directed forwarding
functionality.

#### 2.1.5. Lower transport layer

The lower transport layer defines how upper transport layer messages are segmented and reassembled into multiple Lower Transport PDUs to deliver large upper transport layer messages to other nodes. It also defines a single message to manage segmentation and reassembly (SAR).

#### 2.1.6. Network layer

The network layer defines how transport messages are addressed towards one or more elements. It defines the Network PDU format that allows Transport PDUs to be transported by the bearer layer. The network layer decides whether to relay/forward Network PDUs, accept them for further processing, or reject them. It also defines how
a Network PDU is encrypted and authenticated.

#### 2.1.7. Bearer layer

The bearer layer defines how Network PDUs are transported between nodes. There are two bearers defined, the connectionless advertising bearer and the connection-oriented GATT bearer (for connections established between nodes known as a Proxy Server and a Proxy Client). Additional bearers may be defined in the future.

### 2.2. Overview of mesh operation

The mesh network operation defined by this specification is designed to:

* enable messages to be sent from one element to one or more elements;
* allow messages to be relayed via other nodes to extend the range of communication;
* secure messages against known security attacks, including eavesdropping attacks, man-in-the-middle attacks, replay attacks, trash-can attacks, brute-force key attacks, and possible additional security attacks not documented here;
* work on existing devices in the market today;
* deliver messages in a timely manner;
* continue to work when one or more devices are moved or stop operating; and
* have built-in forward compatibility to support future versions of the Mesh Protocol specification.

Message relaying may use managed flooding, in which potentially every relay node relays the message further out, so the message is propagated in all directions. Messages are delivered over multiple hops by re-broadcasting the message at each hop to all neighboring nodes (i.e., nodes within direct radio range of each other), thus
extending the range of the original message.

Alternatively, relaying may use directed forwarding (see [Section 2.3.11](index-en.html#UUID-f41a44a2-4b53-dc5e-0371-9e1a6cf8ad48 "2.3.11. Directed forwarding")), in which only relay nodes along a path toward the destination will relay the message until the message reaches
the destination.

The node that originates the message decides whether to use managed flooding or directed forwarding.

A network message caching mechanism, also specified, is designed to prevent nodes from reprocessing Network PDUs that have already been processed. Entries corresponding to recently processed Network PDUs are added to a cached list. When a Network PDU is received, it is checked against the list and is ignored if a corresponding
entry is already present. If an entry is not present, then it is added to the list so that the corresponding Network PDU can be ignored in the future. This helps prevent escalation of traffic in managed flooding as well as in directed forwarding when relays overhear repeated message transmissions. To keep the list from getting too
long, an implementation limits the number of messages that are cached.

Each message includes a time to live (TTL) value that limits the number of times a message can be relayed (up to a maximum of 126 times). Each time a message is received and then relayed by a node, the TTL value is decremented by 1. This allows an originator to decide how far into the network the message is propagated.

#### 2.2.1. Network and subnets

A mesh network consists of nodes sharing four common resources:

* network addresses used to identify source and destination of messages (see [Section 3.4.2](index-en.html#UUID-d00b17f6-feae-0749-6734-e8b9d952d2bb "3.4.2. Addresses"));
* network keys used to secure and authenticate messages at the network layer (see [Section 3.9.6.3](index-en.html#UUID-29747365-51b0-d0c2-fc71-34915bdf5059 "3.9.6.3. Network key"));
* application keys used to secure and authenticate messages at the access layer (see [Section 3.9.6.2](index-en.html#UUID-aa7285fa-b0af-1a9e-4c6d-06086a5bf073 "3.9.6.2. Application key")); and
* an IV Index used to extend the lifetime of the network (see [Section 3.9.4](index-en.html#UUID-e38b6660-a18c-f82c-8ee8-93cee1b37134 "3.9.4. IV Index")).

A network can have one or more subnets that facilitate ”area” isolation (e.g., isolated hotel room subnets within a hotel network). A subnet is a group of nodes that can communicate with each other at a network layer because they share a network key. A node may belong to one or more subnets by knowing one or more network keys.
At the time of provisioning, a device is provisioned to one subnet and may be added to more subnets using the Configuration Model.

A node that belongs to multiple subnets may support subnet bridge functionality. A node supporting subnet bridge functionality may be configured to retransmit messages from nodes in a subnet to nodes in other subnets, while attempts to reach unauthorized addresses are blocked. The second subnet, the one on which the messages are
retransmitted, is referred to as a bridged subnet.

There is one special subnet called the primary subnet, which is based on the primary NetKey (see [Section 3.9.6.4](index-en.html#UUID-e0060755-7da2-90f0-9982-4cf72fcecbb7 "3.9.6.4. Global key indexes")). Nodes on the primary subnet participate in the IV Update procedure
(see [Section 3.11.5](index-en.html#UUID-44c81932-033f-50df-97d8-9424e13baea7 "3.11.5. IV Update procedure")), and propagate IV updates to other subnets, while nodes on other subnets only propagate the IV Index updates to those subnets.

The network resources are managed by a node, known as the Configuration Manager (typically a smart phone or other mobile computing device), which implements the Configuration Client model and optionally implements any of the Remote Provisioning Client and Directed Forwarding Configuration Client models. The network resources are
allocated to nodes at the time of configuration. In particular, a Provisioner manages allocation of addresses to make sure no duplicate unicast addresses are allocated, whereas a Configuration Manager generates and distributes network and application keys and makes sure that devices that need to communicate with each other share
proper keys for both network and access layers. The Configuration Manager also knows device keys (see [Section 3.9.6.1](index-en.html#UUID-6b7d377d-3452-3cc2-3729-e6cdf9d03e83 "3.9.6.1. Device key")), which are used to secure communication with each individual node,
including distributing updated network and application keys.

#### 2.2.2. Devices

In the context of this specification, a device is a Bluetooth end product. A device that is not a member of a mesh network is known as an unprovisioned device. A device that is a member of a mesh network is known as a node. A device that is used to manage the transitions between an unprovisioned device and a node is known as a
Provisioner.

An unprovisioned device cannot send or receive mesh messages; however, it advertises its presence to Provisioners. The process of authenticating and providing basic information, including unicast addresses (see [Section 3.4.2.2](index-en.html#UUID-c139b258-d021-13f6-964e-d996ca675f1a "3.4.2.2. Unicast address")) and a network key (see [Section 3.9.6.3](index-en.html#UUID-29747365-51b0-d0c2-fc71-34915bdf5059 "3.9.6.3. Network key")) to an unprovisioned device is known as provisioning (see [Section 2.2.3](index-en.html#UUID-cc301db0-ba02-d038-8dda-d28b57f7938c "2.2.3. Adding devices to a mesh network")). A Provisioner will provision an unprovisioned device into a mesh network, converting the unprovisioned device into a node.

A node that implements the Configuration Client model (see [Section 4.4.2](index-en.html#UUID-4db74f6a-03d8-94ed-ddaa-a309a8d8c829 "4.4.2. Configuration Client model")) can start acting as a Configuration Manager when the Provisioner provides the node with the device
keys of the nodes on the network. The Configuration Manager can then configure the nodes by providing them application keys (see [Section 3.9.6.2](index-en.html#UUID-aa7285fa-b0af-1a9e-4c6d-06086a5bf073 "3.9.6.2. Application key")) and setting publish and subscribe
addresses (see [Section 2.3.9](index-en.html#UUID-04e1d1e8-d24a-e7c4-7fd4-2b0a2b5184ca "2.3.9. Publish-subscribe and message exchange")) so that the nodes can communicate with each other.

A Configuration Manager, which is the same physical device as the Provisioner, is known as a Mesh Manager. A Configuration Manager can remove a node from a mesh network, which reverts it back to an unprovisioned device.

A device may support multiple instances of a node by offering itself to be provisioned to another mesh network after already being provisioned to a mesh network. Each instance of a mesh network is determined by addresses and a device key obtained by the device during provisioning.

#### 2.2.3. Adding devices to a mesh network

Devices are added to a mesh network by a Provisioner, at which point they become nodes. The provisioning of devices into a mesh network differs from the point-to-point bonding and pairing that is typically used in Bluetooth wireless technology. Provisioning of devices is enabled using either a simple advertising bearer or a
point-to-point GATT-based bearer. A single provisioning protocol is used over both bearers. Provisioning over an advertising-based bearer is implemented by all devices. Provisioning over a GATT-based bearer allows devices such as legacy phones (i.e., devices that do not support provisioning over an advertising bearer natively) to
be Provisioners.

To assist with provisioning of multiple devices, a device has an attention timer that can be set by a Provisioner. When set to a non-zero value, the device identifies itself using any means it can. For example, the device may flash a light, make a sound, or vibrate. When the attention timer expires, the device stops identifying
itself. This allows a Provisioner to send a single message to a device to cause it to identify itself and the device automatically stops identifying itself after a given time.

The protocol to run over these two bearers is a derivative of the Security Manager protocol of v4.2 of the Bluetooth Core Specification to introduce the ability to authenticate devices that have a very limited user interface, such as a light or a switch. The Security Manager protocol requires a reliable bearer, something that
cannot be guaranteed by the advertising provisioning bearer; therefore the protocol used in this specification is designed to enable reliable delivery of messages independent of the bearer. The similarity to the Security Manager protocol enables significant reuse of existing code on devices that have implemented such
functionality.

#### 2.2.4. Communications support

Many current devices are unable to advertise or comprehend mesh messages without being updated. To enable these devices to communicate with a node in a mesh network without the need for an operating system update or similar hardware/software update, the specification enables the use of GATT connectivity for all existing
devices.

#### 2.2.5. Low power support

The features within this specification enable many devices in the mesh network to be battery-powered or to use techniques such as energy harvesting. Such devices may be constrained in how they can function as a part of a mesh network (e.g., devices that only send data when interacted with). This specification does not require
devices to coordinate transmissions, make connections, or restart security on every connection; thus facilitating low power operation. Devices needing low power support can associate themselves with an always-on device that stores and relays messages on their behalf, using the concept known as friendship (see [Section 3.6.6](index-en.html#UUID-8fe081f8-4c1b-92fd-f6c2-fb5461eb824b "3.6.6. Friendship")). However, devices that relay messages will receive messages as well as forward messages a majority of the time and are likely to use significantly more power than could be provided by
typical small batteries or capacitors.

### 2.3. Architectural concepts

The mesh networking architecture uses several different concepts: states, messages, bindings, elements, addressing, models, publish-subscribe, mesh keys, and associations.

#### 2.3.1. States

A state is a value representing a condition of an element or a node. A state may be valid in the context of a subnet or of one or more models.

An element exposing a state is referred to as a server. For example, the simplest server is a Generic OnOff Server, representing that it is either on or off.

An element accessing a state is referred to as a client. For example, the simplest client is a Generic OnOff Client (a binary switch) that is able to control a Generic OnOff Server via messages defined by the Generic OnOff Model.

A state that is made of two or more states is known as a composite state. For example, a color-changing lamp can control color hue separately from color saturation and brightness.

#### 2.3.2. Bound states

When a state is bound to another state, a change in one results in a change in the other. Bound states may be from different models in one or more elements. For example, a common type of binding is between a Level state and an OnOff state: changing the Level to 0 changes the bound OnOff state to Off and changing the Level to a
non-zero value changes the bound OnOff state to On.

#### 2.3.3. Messages

All communication within a mesh network is accomplished by sending messages. There are two types of messages: Access messages and Transport Control messages.

Access messages operate on states. For each state, there is a defined set of Access messages that a server supports and a client may use to request a value of a state or to change a state. A server may also transmit unsolicited Access messages carrying information about states and/or changing states.

An Access message is defined as having an opcode, associated parameters, and behavior. An opcode may be a single octet (for special Access messages that require the maximum possible payload for parameters), 2 octets (for standard Access messages), or 3 octets (for vendor-specific Access messages).

A total Access message size, including an opcode, is determined by the underlying transport layer, which may use a SAR mechanism. To maximize performance and avoid the overhead of SAR, a design goal is to fit Access messages in a single segment. The lower transport layer provides up to 11 octets for a non-segmented message,
leaving up to 10 octets that are available for parameters when using a 1-octet opcode, up to 9 octets available for parameters when using a 2-octet opcode, and up to 8 octets available for parameters when using a vendor-specific 3-octet opcode.

The lower transport layer provides a SAR mechanism capable of transporting up to 32 Access or Transport Control message segments. The maximum Upper Transport Access PDU size when using a SAR is 384 octets. This means that (excluding a TransMIC, see [Section 3.9.7.1](index-en.html#UUID-e4d164f2-569b-58e9-6b01-4ebd013606df "3.9.7.1. Upper transport layer authentication and encryption")) up to 379 octets are available for parameters when using a 1-octet opcode, up to 378 octets are available for parameters when using a 2-octet opcode, and up to 377 octets are
available for parameters when using a vendor-specific 3-octet opcode. The maximum Transport Control message size when using a SAR is 257 octets (including an opcode).

SAR effectively does not impose any extra overhead on the Access message per segment: a 10-octet Access message is transported as an unsegmented message, and a 20-octet message is transported as a segmented message that uses two segments.

Access message definitions contain tables of parameters. In a message payload, parameters follow an opcode, and parameter offsets are in octets unless otherwise specified.

Access messages are defined as acknowledged or unacknowledged. An acknowledged message requires a response whereas an unacknowledged message does not require a response.

Transport Control messages are associated with functionalities supported by the node. The Transport Control messages are transmitted and received by the upper transport layer. A Transport Control message is defined as having an opcode, associated parameters, and behavior. Transport Control messages use single-octet opcodes.

The lower transport layer provides a mechanism of SAR that is capable of transporting up to 32 segments of a Transport Control message.

Transport Control message definitions contain tables of parameters. In a message payload, parameters follow an opcode, and parameter offsets are in octets unless otherwise specified.

##### 2.3.3.1. Aggregation of Access messages

The number of Access messages that need to be sent to set up complicated nodes can easily be more than 100. Each response that acknowledges an Access message is delayed by a random value from 20 to 50 milliseconds (see [Section 3.7.3](index-en.html#UUID-ef1bf56c-61c3-410f-da21-46d4e84b5699 "3.7.3. Access layer behavior")). For 100 Access messages, this recommendation introduces an average delay of 3.5 seconds. Additional delay is introduced by round-trip time for each request and response message.

To speed up the configuration of a node on a mesh network, aggregation of Access messages is introduced in this specification. The aggregation of messages mechanism can significantly lower configuration time for a newly provisioned device, by reducing the number of Access messages that need to be acknowledged and the
round-trip time for each request and response message.

#### 2.3.4. Elements

An element is an addressable entity on a node. Each node has at least one element, the primary element, and may have up to 254 additional secondary elements. The number and structure of elements is static and does not change throughout a term of a node (see [Section 2.3.7](index-en.html#UUID-46f8e936-55f4-be60-152c-2de49fca322e "2.3.7. Terms")).

The primary element is addressed using the first unicast address assigned to the node. Each additional secondary element is addressed using the subsequent addresses assigned to the node. The unicast element addresses allow nodes to identify which element on a node is transmitting or receiving a message.

If the number and structure of elements changes, for example due to a firmware update or a functionality being added by attaching a new physical component to the device, the current term of the node must end and a new term for the node must start, as required by [Section 4.2.2.1](index-en.html#UUID-16195ab6-ad86-3a5b-d7b5-d6e4577a537a "4.2.2.1. Composition Data Page 0").

Messages are dispatched within models based on opcodes and element addresses.

An element is not allowed to contain multiple instances of models that use the same message in the same way (for example, receive an “On” message). When multiple models within the same element use the same message, the models are said to “overlap.” To implement multiple instances of overlapping models within a single node (for
example, to control multiple light fixtures that can be turned on and off), the node is required to contain multiple elements.

For example, a light fixture may have two lamps, each implementing an instance of the Light Lightness Server model and an instance of the Generic Power OnOff Server model. This requires that the node contain two elements, one for each lamp. When it receives an "On" message, the node uses the unicast address of the element to
identify which instance of the Generic Power OnOff Server model the message is addressed to.

In another example, a dual-socket power strip contains two independent energy measurement sensors that can measure power consumed by an appliance connected to a socket. This would require that the node have two Sensor Data states, each in a separate element. The first element, the primary element, would be identified using the
unicast address for the node and would include a state for the first energy sensor as well as states representing the configuration of the node. The second element, a secondary element, would be identified using a unicast element address and would include the state for the second energy sensor.

Each element has a GATT Bluetooth Namespace Descriptor [[4](index-en.html#idp254746)] value that helps identify which part of the node this element represents. These namespace descriptor values use the same definitions as GATT. For example, the elements of the temperature
sensor would use the values “inside” and “outside.”

#### 2.3.5. Addresses

An address may be a unicast address, a virtual address, or a group address. There is also a special value to represent an unassigned address that is not used in messages.

A unicast address is allocated to an element and always represents a single element of a node during a term. There are 32767 unicast addresses per mesh network.

A virtual address is a multicast address and can represent multiple elements on one or more nodes. Each virtual address logically represents a Label UUID, which is a 128-bit value that does not have to be managed centrally. Each message sent to a Label UUID includes the full Label UUID in the message integrity check value that
is used to authenticate the message. To reduce the overhead of checking every known Label UUID, a hash of the Label UUID is used. There are 16384 hash values, each of which codifies a set of virtual addresses. While there are only 16384 hash values used in a virtual address, each hash value can represent millions of possible Label
UUIDs; therefore, the number of virtual addresses is considered very large.

A group address is a multicast address and can represent multiple elements on one or more nodes. There are 16384 group addresses per mesh network. There are a set of fixed group addresses that are used to address a subset of all primary elements of nodes based on the functionality of those nodes. All other group addresses are
known as dynamically assigned group addresses. There are 256 fixed group addresses and 16128 dynamically assigned group addresses.

#### 2.3.6. Models

A model defines the basic functionality of a node. A node may include multiple models. A model defines the required states (as described in [Section 2.3.1](index-en.html#UUID-cf82584a-ed77-2a0c-55fa-cc01f17c57eb "2.3.1. States")), the messages that act upon those states
(as described in [Section 2.3.3](index-en.html#UUID-5bdfda52-ba1c-68d5-d7b8-7c4a8e2db889 "2.3.3. Messages")), and any associated behavior.

A mesh application is specified using a client-server architecture communicating with a publish-subscribe paradigm. Due to the nature of mesh networks and the recognition that the configuration of behavior is performed by a Configuration Manager, an application is not defined in a single end-to-end specification such as a
profile. Instead, an application is defined in a client model and a server model.

This specification defines two types of model: server models and client models:

* **Server model:** A server model is composed of one or more states spanning one or more elements. The server model defines a set of mandatory messages that it can transmit or receive, the behavior required of the element when it transmits and receives such messages, and any
  additional behavior that occurs after messages are transmitted or received.
* **Client model:** A client model defines a set of messages (both mandatory and optional) that a client uses to request, change, or consume corresponding server states, as defined by a server model. The client model does not have states.

A single device may include server models and/or client models. In addition, some models may contain both client and server functionality as described below.

This specification defines the following relationships among models:

* **Extend.** When a first model inherits all states, messages and procedures of a second model, and the first model optionally contains additional states and supports additional messages and procedures not defined in the second model, the two models have an extend relationship (i.e.,
  the first model extends the second model). The extend relationship may be hierarchical (e.g., the first model may extend a second model that extends a third model).
* **Correspond.** When models share state/procedure instances and work together to achieve some functionality, they have a correspond relationship. Models that have a correspond relationship may share either state instances or state bindings; however, they may have different
  messages and uninherited procedures interacting with the states.

This specification defines the following types of models:

* **Base.** A model that is extended by another model is called a base model.
* **Root.** A model is defined as a root model if it does not extend any other models. A root model may serve as a base model for other models.
* **Extending.** A model that is extending another model is called an extending model.
* **Corresponding.** A model that has a correspond relationship with another model is called a corresponding model.
* **Main.** A main model is a model at the end of an extension hierarchy that indicates an instance of a functionality on a node. A main model is not extended by other models within the scope of the functionality. A main model can be an extending model or a corresponding model.

For example, [Figure 2.2](index-en.html#UUID-9cc6a130-3bbf-847a-91f6-2ff5a9f37ef9_figure-idm4603410096313634088096728726 "Figure 2.2. Client-server model communication") shows the element-model structure for a device that implements a server model (Device C)
with a state and supporting messages R, S, T, X, Y, Z; and two devices that implement a client model, with Device A supporting messages X, Y, and Z and Device B supporting messages R, S, T, and Z.

|  |
| --- |
| Client-server model communication |

Figure 2.2. Client-server model communication

In another example, [Figure 2.3](index-en.html#UUID-9cc6a130-3bbf-847a-91f6-2ff5a9f37ef9_figure-idm4555426845129634088104363639 "Figure 2.3. Control model communication") shows the element-model structure of a device that implements a model that is itself a server
model and also a client of some other server models. Device C can communicate with server models as a client (supporting messages X, Y, and Z and messages R, S, and T respectively) and can communicate with client models as a server (supporting messages A, B, and C).

![Control model communication](image/1671b81d5307d2.png)

Figure 2.3. Control model communication

A lighting control model is an example of a model that includes server functionality, client functionality, and control logic. A typical lighting control model needs to function as a client to sensors (e.g., to determine occupancy and/or the ambient light level by receiving relevant sensor status messages) and to function as a
server to a settings client (such as a smartphone application that configures its parameters). Control logic in such a model may then control the lighting via defined state bindings if the model is included within a light source such as a lamp or other luminaire. In addition, if the lighting controller also acts as a client for one
or more light sources, the lighting controller can be implemented in a separate node rather than necessarily being included within a light source.

Models can define functions of a device as a network node, such as key management, address assignment, and relaying of messages. Models also define physical behaviors of a device built around a network node, such as power control, lighting control, and sensor data collection. There may be nodes implementing only network-related
functions, such as Relay nodes or Proxy nodes, while the majority of nodes are able to interact with the physical world by means of controlling electrical power, controlling light emissions, or sensing environmental data.

A message can be used by multiple different models. Message behavior is the same in each model, enabling a common understanding among client and server models because the behavior is consistent regardless of the models that send and process the message.

Model specifications are designed to be very small and self-contained. A model may, at the specification definition time, require other models to be instantiated within the same node. This is called extending, which means a model can extend other models.

Models that do not extend other models are referred to as root models.

Model specifications are immutable: it is not possible to remove or add behavior to a model, whether the desired behavior is optional behavior or mandatory. Models are not versioned and have no feature bits. If additional behavior is required in a model, then a new extended model is defined that exposes the required behavior and
can be implemented alongside the original model.

Therefore, knowledge of the models supported by an element determines the exact behavior exposed by that element.

Additionally, models may support metadata that provide additional information about a specific instance of the model. For example, the lighting control model may expose information about the purpose of the light source in the physical device.

Models may be defined and adopted by Bluetooth SIG and may be defined by vendors. Models defined by Bluetooth SIG are known as SIG adopted models, and models defined by vendors are known as vendor models. Models are identified by unique identifiers, which can be either 16 bits, for SIG adopted models, or 32 bits, for
vendor models.

For example, [Figure 2.4](index-en.html#UUID-9cc6a130-3bbf-847a-91f6-2ff5a9f37ef9_figure-idm455542658213603408810636945 "Figure 2.4. Element-model structure of a device") shows the element-model structure of a device that implements a root model with two bound
states and a set of messages operating on each state. The root model is within the primary element and is extended by the extended model that adds another state on a secondary element. Messages are not capable of differentiating among multiple instances of the same state on the same element. Therefore, when more than one instance
of a given state is present on a device, each instance is required to be in a separate element. In this example, the second instance of State X is required to be located on the second element because it is the same type of a state and thus has the same types of messages serving it.

|  |
| --- |
| Element-model structure of a device |

Figure 2.4. Element-model structure of a device

This example structure can be multiplied for a composite device. For example, a composite device can have multiple instances of the same root model (or extended models), each on a separate element (or set of elements). Also, if a model (root or extended) needs more than one instance of a particular state, the states are
distributed across several elements so that, at most, a single instance of any given state is on an element.

[Figure 2.5](index-en.html#UUID-9cc6a130-3bbf-847a-91f6-2ff5a9f37ef9_figure-idm4611434205838434088108625735 "Figure 2.5. Element-model structure of a composite device") illustrates how the element-model structure of the device in [Figure 2.4](index-en.html#UUID-9cc6a130-3bbf-847a-91f6-2ff5a9f37ef9_figure-idm455542658213603408810636945 "Figure 2.4. Element-model structure of a device") might be implemented in a composite device. The element-model structure of the device is described by the Composition Data (see [Section 4.2.1](index-en.html#UUID-23a0fd2f-d435-3f00-ac1d-e1e65a5fe02f "4.2.1. State instances for multiple subnets")) that is read by a Configuration Manager after provisioning (see [Section 5](index-en.html#UUID-c2ed2695-c7e2-6000-08bb-72c4b7c7e7fe "5. Provisioning")), using the Configuration Server model and the Configuration Client model (see [Sections 4.4.1](index-en.html#UUID-983db022-d6e3-ac72-0296-26a0d31afc91 "4.4.1. Configuration Server model") and [4.4.2](index-en.html#UUID-4db74f6a-03d8-94ed-ddaa-a309a8d8c829 "4.4.2. Configuration Client model")).

|  |
| --- |
| Element-model structure of a composite device |

Figure 2.5. Element-model structure of a composite device

#### 2.3.7. Terms

A term is a period in the lifetime of a node during which the structure of the node (i.e., the features, the elements and models) and the unicast addresses of the node’s elements do not change.

Starting a new term may be necessary to support a change in the hardware configuration of a physical device, such as the attachment of an auxiliary sensor, or to support a change in subsystem configuration on the node, such as the attachment of a new gear to an intra-luminaire network. The changes are indicated by the node by
populating Composition Data Page 128 (see [Section 4.2.2.4](index-en.html#UUID-665d39a3-1c26-b81d-3c45-7eb85d21c8ea "4.2.2.4. Composition Data Page 128")) and take effect when a new term starts.

The initial term of a node on a network starts when the node is provisioned on the network.

A term ends and a new term starts when a Node Address Refresh procedure or a Node Composition Refresh procedure is executed (see [Section 3.11.8](index-en.html#UUID-abe7a4a8-fdc0-ec16-10d6-db919df07d22 "3.11.8. Node Provisioning Protocol Interface procedures")).

The last term of a node on a network ends when the node is removed from the network.

#### 2.3.8. Example device

To help explain how the arrangement of models within elements determines the state and behavior of a device, we will use a dual-socket smart power strip device (shown in [Figure 2.6](index-en.html#UUID-69c8fd60-ca40-a179-9991-a8842be03e76_Figure_2.6 "Figure 2.6. Dual-socket smart power strip")) as an example. This device has a single radio that has the low energy feature of Bluetooth and two independent power sockets, each capable of controlling the power output. This example includes states, messages, and models defined in the Mesh Model
specification [[9](index-en.html#idp254760)].

|  |
| --- |
| Dual-socket smart power strip |

Figure 2.6. Dual-socket smart power strip

The device has two elements (see [Section 2.3.4](index-en.html#UUID-5db857eb-73fe-195b-1bb3-09880ad0c535 "2.3.4. Elements")) that represent each of the two power sockets. Each element has a unicast address assigned to it.

The functionality of each element is defined by the Generic Power Level Server model. The model defines a set of states on a server, as well as a set of messages that operate on the states.

A Generic Power Level Set message may be sent to the device to control the output power. The message is addressed to an element and carries the element’s address in the DST field (see [Section 2.3.9](index-en.html#UUID-04e1d1e8-d24a-e7c4-7fd4-2b0a2b5184ca "2.3.9. Publish-subscribe and message exchange")).

The sockets can also be controlled by generic devices (such as a dimmer) that implement the Generic Level Client model (and do not know anything about power control). This model simply sets a desired level to zero, a maximum value, or a value in between. Power to the sockets is controlled through state binding. In each power
socket, the Generic Power Actual state is bound to the Generic Level state. A Generic Level Client sends Generic Level messages to the Generic Level Server. The Generic Level state is changed, which in turn (via the defined binding) changes the Generic Power Actual state that controls the power output.

Elements can report states. In our example, each socket may report power level as well as the energy consumption of a device plugged into the socket. Energy consumption is reported using messages defined by the Sensor Server model. Each message has the element’s address, which identifies the socket, in its SRC field (see
[Section 3.4.4.6](index-en.html#UUID-358c7a6d-adf9-2d32-4c24-5281201dc6b6 "3.4.4.6. SRC")).

[Figure 2.7](index-en.html#UUID-69c8fd60-ca40-a179-9991-a8842be03e76_figure-idm4661379531676834088125396657 "Figure 2.7. Element-model structure for the example device") illustrates the element-model structure for the dual-socket device. Functionally, both elements
of the device have identical features. The only difference is that the primary element handles the Configuration Server model, which is used for network management, in addition to the other models. Each element may have other models defined such as the Health Server model (see [Section 4.4.4](index-en.html#UUID-50a8103c-f138-9de4-de4a-0912f51dac71 "4.4.4. Health Client model")) or models defined in the Mesh Model specification [[9](index-en.html#idp254760)].

![Element-model structure for the example device](image/1671b81d54a902.png)

Figure 2.7. Element-model structure for the example device

#### 2.3.9. Publish-subscribe and message exchange

Publication and subscription of data within the mesh network is described as using a publish-subscribe paradigm. Nodes that generate messages publish the messages to a unicast address, group address, or virtual address. Nodes that are interested in receiving the messages will subscribe to these addresses.

Generated messages are sent to destination mesh addresses that can be unicast, pre-configured group addresses, or virtual addresses. Messages can be sent as replies to other messages or can be unsolicited messages. When an instance of a model is sending a reply message, it uses the incoming message originator’s source address as
the destination address. When an instance of a model is sending unsolicited messages, it uses a model publish address as the destination address. Each instance of a model within a node has a single publish address.

On the receiving side, each instance of a model within a node can subscribe to one or more group addresses or virtual addresses. Whenever a message that is addressed to a group address or a virtual address on one of the model’s subscription lists arrives, it is processed by the node. A message is also processed when its
destination address is the unicast address of a receiving element or when its destination address is a fixed group address that this device is a member of. If a node has multiple elements, then the message is processed once on each of the addressed elements.

Publish addresses and subscription lists for models defined by higher layer specifications use the Model Publication and Subscription List states that are managed by the Configuration Server Model.

A node can have multiple subscriptions per instance of a model’s element, although nodes may limit the number of subscriptions that are supported. Using multiple subscription addresses allows a node to respond to messages that are published to different groups. For example, a light may be subscribed to messages sent to the
bedside light group, the bedroom group, the upstairs group, and the house group.

Each message is sent from a single unicast address (an element address) and sequenced using a unique sequence number to facilitate detection of and protection against replay attacks.

#### 2.3.10. Security

All messages are encrypted and authenticated using two types of keys. One key type is for the network layer communication, such that all communication within a mesh network would use the same network key. The other key type is for application data. Separating the keys for networking and applications allows different application
keys for different purposes. This allows the creation of separate security domains for separate applications (e.g., one domain for access control to a building and another domain for ambient temperature sensing).

##### 2.3.10.1. Application and network security

Encrypting and authenticating messages at the upper transport layer and network layer is designed to secure communications within the mesh network against eavesdroppers and malicious attacks. Each layer maintains distinct keys to allow separation between application and network entities.

Splitting application keys from network keys enables secure relay transmission of messages: Relay nodes can authenticate messages at network level without accessing the application data. For example, a light bulb acting as a Relay node should not be able to unlock doors.

The application key is used directly along with an associated application key identifier (AID) that is used in certain contexts to identify the application used. However, the network key is always used through a key derivation function to generate other keys that are used directly. Examples of such keys include EncryptionKey
and PrivacyKey. This allows a single network key to be changed and all the associated values that are derived from that key to be quickly derived. As with the application key, the network key is also used to derive a network key identifier (see [Section 3.9.6](index-en.html#UUID-2b66a565-a23e-1531-b7c2-29c7962145ad "3.9.6. Keys")).

The security model defines three separate keys (the device key (DevKey), the application key (AppKey), and the network key (NetKey)) to secure the messages. When a node is given a key, it is authorized to use that key. A key that is shared between multiple nodes enables any node with that key to transmit and receive messages
using that key.

The device key facilitates confidentiality and authentication of key material between a Configuration Manager and a single node. The application key facilitates confidentiality and authentication of application data sent between intended nodes. The network key facilitates privacy, confidentiality, and authenticity of network
messages. A node may have knowledge of a single device key, multiple application keys, and multiple network keys.

A device key is similar to an application key in that it is designed to secure information sent by an application in the upper transport layer. However, a device key is known only by the Provisioner, the Configuration Manager, and the single node. The Configuration Manager knows the device keys for all nodes, which allows the
Configuration Manager to securely distribute keys to a set of nodes by sending these keys secured with the device key for each individual node, allowing a key distribution to be targeted at only those nodes that need to know. Use of a device key is designed to protect against the “trash-can” attack (a technique to retrieve
information from a disposed device that can be used to carry out an attack on a network) by allowing the distribution of new network and application keys to selected devices only.

The network key and the device keys for the nodes on the network constitute the ownership of the network. Ownership of the network may be changed by executing any of the Node Provisioning Protocol Interface procedures for every node on the network (see [Section 3.11.8](index-en.html#UUID-abe7a4a8-fdc0-ec16-10d6-db919df07d22 "3.11.8. Node Provisioning Protocol Interface procedures")) and executing the Key Refresh procedure (see [Section 3.11.4](index-en.html#UUID-710f87fc-c656-787c-98a3-9b0bad889506 "3.11.4. Key Refresh procedure")).

An application key can only be used with a single network key. This implies that a network key has one or more application keys associated with it. This association is known as the key binding.

The granularity of access layer security is on a per-model basis. Each server model has a set of application keys bound to it, defining the possible keys that should be used to encrypt and authenticate a message to be processed by the model. This allows multiple entities to operate certain node functions. Up to 251 application
keys can be bound to a model. For example, a Light Lightness Server Model has three keys bound to it because the admin, user, and guest can all switch on a light. However, only the admin can configure the lamp, so the Configuration Server Model has only the admin application key bound to it.

##### 2.3.10.2. Obfuscation

The network security model utilizes a privacy mechanism called obfuscation that utilizes the Advanced Encryption Standard (AES) to encrypt the source address, sequence numbers, and other header information using a PrivacyKey. The intent for obfuscation is to make tracking nodes more difficult.

##### 2.3.10.3. Network and application key identifiers

A node may have multiple network or application keys.

By using a key identifier, it is possible to identify which subset of keys are used to secure the message. For example, instead of checking 20 keys, a node may only need to check two keys that have the same least significant bits of the key identifier. If a message is received with a key identifier that is not known, then the
node can immediately discard it.

The key identifier is generated from the network or application key using a key derivation function.

This specification defines a separate identifier for the network key and application key. A network key identifier is transmitted in each Network PDU using a 7-bit value, while the AID is transmitted in each Lower Transport PDU using a 6-bit value.

##### 2.3.10.4. Initialization vector index

A Network PDU contains a 24-bit sequence number that allows an element to transmit 16,777,216 Network PDUs. The sequence number is used in the security nonce to provide uniqueness; therefore, the sequence number cannot wrap. If an element is transmitting a new message at 2 Hz, then these sequence numbers would be exhausted
after 97 days. To enable a mesh network to operate for longer periods of time than the sequence number space allows, an additional 4-octet value called the IV Index is defined that is included in the security nonce. For example, using the same 2 Hz message frequency would measure the lifetime of the network using the IV Index in
billions of years.

To enable a gradual transition from one IV Index to the next, each Network PDU includes the least significant bit of the IV Index that was used to transmit the message. A node can also use an IV Update procedure to signal to peer nodes that it is updating the IV Index. This procedure takes a minimum of eight days to transition
from the old IV Index to the new IV Index, thereby limiting the frequency that a node can transmit messages to 24 Hz. However, a node should not send more than 100 Network PDUs in any 10 second window, so this would typically take approximately 19 days to exhaust.

#### 2.3.11. Directed forwarding

Directed forwarding is designed to help improve performance of a multi-hop network by selecting only a subset of nodes to relay a message from a source to a destination. This subset, including the source node and the destination node(s), constitutes a path, as defined by directed forwarding. A path is identified by a pair of
addresses: a source address and a destination address. The destination address may be a unicast address, a group address, or a virtual address.

The source node of a path is the Path Origin, and each destination node of a path is a Path Target (see [Section 3.6.8.1](index-en.html#UUID-38e58962-1337-0b5b-b28c-e9c4879bb04c "3.6.8.1. Functional overview of directed forwarding")).

The Path Origin is configured to use managed flooding or directed forwarding when originating a message (see [Section 3.7.3.1](index-en.html#UUID-32c1a8f7-5ee7-402c-04e0-35fe2bce7455 "3.7.3.1. Transmitting an Access message")). Managed flooding and directed forwarding
use different security materials, respectively the managed flooding security material and the directed security material, which are obtained from the same network key (see [Section 3.9.6.3.1](index-en.html#UUID-d0b55b79-5d9d-9a14-e649-f8d9d9fcd7d1 "3.9.6.3.1. NID, EncryptionKey, and PrivacyKey")).

A directed forwarding node uses a forwarding table to store pairs of source and destination addresses for each path it is part of. There is a separate forwarding table for each subnet. When a message is received by a node that is configured to relay messages using directed forwarding, the node compares the source and destination
addresses of the message against the entries in the table and retransmits the message only if there is a match. That restricts message forwarding only to nodes along an established path.

Nodes forming a path may be explicitly configured by a Configuration Manager or a path may be discovered and maintained following the request of a node that is originating messages. To help improve reliability and resilience, a path may have multiple lanes between source node and destination node(s) that take advantage of
several relays overhearing a message relayed on each hop. Lanes of a path are discovered sequentially. The path discovery and maintenance policy of an originator is configured by the Configuration Manager and controls aspects such as path lifetime, verification and rediscovery cadence, the number of redundant lanes, and whether the
paths are unidirectional or bidirectional.

Directed forwarding nodes, known as supporting nodes, may act on behalf of Low Power nodes or Proxy Client nodes, known as dependent nodes, to discover paths, to establish paths, and to provide path updates when the network topology changes. For more information on node dependence, see [Section 3.6.8.3](index-en.html#UUID-0c0fc10c-4a72-e0d8-2944-e1408b1d2734 "3.6.8.3. Node dependence in directed forwarding").

There is no limitation on the number of directed forwarding relays in a network (other than the total number of nodes). When using directed forwarding, the message forwarding load may be distributed among several nodes. Each node may function as a directed forwarding relay: the node will only relay a portion of overall
traffic.

#### 2.3.12. Friendship

Friendship is used by Low Power nodes to limit the amount of time that they need to listen. If a node cannot receive continuously, then it is possible that it will not receive mesh messages that it should be processing. This includes security updates required for maintaining the security of the network as well as the normal mesh
messages.

If the Low Power node does not receive such messages, then it may not operate as desired and it may also fail to keep up-to-date with the latest security state of the network and eventually drop off the network if this security is changed without its knowledge.

Friendship is a special relationship between a Low Power node and one neighboring Friend node. These nodes must be within a single hop of each other and in the same subnet, as required by [Section 3.6.6.3.1](index-en.html#UUID-b9fc5379-b71a-2993-c918-1e0dad878237 "3.6.6.3.1. Friend establishment").

Friendship is first established and initiated by the Low Power node; once established, the Friend node performs a number of actions that help reduce the power consumption on the Low Power node. The Friend node maintains a Friend Queue for the Low Power node, which stores all incoming messages addressed to the Low Power node. The
Friend node delivers those messages to the Low Power node when requested by the Low Power node. Also, the Friend node delivers security updates to the Low Power node.

When friendship is established between a Low Power node and one Friend node, the two nodes are considered to be “friends”.

An example topology of a mesh network illustrating Friend nodes and Low Power nodes is shown and described in [Section 2.3.14](index-en.html#UUID-2dbbe25c-c6d0-f3f2-1fc1-e3987a1fc638 "2.3.14. Topology").

#### 2.3.13. Features and functionality

The capabilities of a node are determined by the features and functionality that the node supports. All nodes have the ability to transmit and receive mesh messages. Nodes can also optionally support one or more additional features, as defined by the Configuration Server model:

* Relay feature – the ability to receive and retransmit mesh messages over the advertising bearer to enable larger networks.
* Proxy feature – the ability to receive and retransmit mesh messages between GATT and advertising bearers.
* Low Power feature – the ability to operate within a mesh network at significantly reduced receiver duty cycles only in conjunction with a node supporting the Friend feature.
* Friend feature – the ability to help a node supporting the Low Power feature to operate by storing messages destined for those nodes.

A node that supports a feature may have that feature enabled or disabled, and the feature, when enabled, may be or may not be in use.

A node supporting the Relay feature may have this feature disabled, but it would still support the Relay feature, it is just that it is not performing the functionality required by that feature. A node that supports the Relay feature and has the Relay feature enabled is known as a Relay node.

Proxy functionality is supported by nodes that support relaying/forwarding of Network PDUs received by a node between GATT and advertising bearers. A node supporting the Proxy feature may have this feature disabled, but it would still support the Proxy feature, it is just that it is not performing the functionality required by
that feature. A node that supports the Proxy feature and has the Proxy feature enabled is known as a Proxy node.

A node supporting the Low Power feature cannot have this feature disabled and, as required by [Section 3.6.6.3](index-en.html#UUID-0f8e0687-04fa-84e4-46cc-4b1d5db372d2 "3.6.6.3. Friend feature"), must establish a friendship with another node supporting the Friend feature
before it can use the Low Power feature to reduce receiver duty cycles. A node that supports the Low Power feature and has a friendship with a node that supports the Friend feature is known as a Low Power node.

A node supporting the Friend feature may have this feature disabled, but it would still support the Friend feature, it is just that it is not performing the functionality required by that feature. A node that supports the Friend feature, has the Friend feature enabled, and has a friendship with a node that supports the Low Power
feature is known as a Friend node.

Other Foundation models support additional functionality. For example, the Directed Forwarding Configuration Server model (see [Section 4.4.7](index-en.html#UUID-b6798fda-618c-2a98-5558-f53a2a8db930 "4.4.7. Directed Forwarding Configuration Server model")) supports
directed forwarding functionality. Directed forwarding can be performed only among nodes in a subnet that have directed forwarding functionality enabled. A node with directed forwarding functionality enabled in a subnet is known as a Directed Forwarding node in that subnet.

Additional functionalities can be enabled or disabled in Directed Forwarding nodes:

* directed relay functionality – the ability to participate in finding paths and relaying messages along paths
* directed proxy functionality – the ability to establish paths on behalf of a Proxy Client
* directed friend functionality – the ability to establish paths on behalf of a Low Power node

Directed relay functionality can be enabled or disabled in nodes that support directed forwarding. A Directed Forwarding node with directed relay functionality enabled in a subnet is known as a Directed Relay node in that subnet (see [Section 3.6.8.1](index-en.html#UUID-38e58962-1337-0b5b-b28c-e9c4879bb04c "3.6.8.1. Functional overview of directed forwarding")).

Directed proxy functionality is supported by nodes that support both the Proxy feature and directed forwarding functionality; otherwise, it is not supported. When directed proxy functionality is supported, it can be enabled or disabled. A Directed Forwarding node with directed proxy functionality enabled in a subnet is known as
a Directed Proxy node in that subnet (see [Section 3.6.8.1](index-en.html#UUID-38e58962-1337-0b5b-b28c-e9c4879bb04c "3.6.8.1. Functional overview of directed forwarding")).

Directed friend functionality is supported by nodes that support both the Friend feature and directed forwarding functionality. When directed friend functionality is supported, it can be enabled or disabled. A Directed Forwarding node with directed friend functionality enabled in a subnet is known as a Directed Friend node in
that subnet (see [Section 3.6.8.1](index-en.html#UUID-38e58962-1337-0b5b-b28c-e9c4879bb04c "3.6.8.1. Functional overview of directed forwarding")).

A Directed Forwarding node that supports the Low Power feature in a subnet can perform directed forwarding in that subnet if the node is not in a friendship in the same subnet, because the node behaves like a regular node while not in a friendship. If the node is in a friendship with a Directed Friend node, then directed
forwarding can be performed by the Directed Friend node. If the node is in a friendship with a Friend node that does not have directed friend functionality supported and enabled, then directed forwarding cannot be performed.

Subnet bridging can be performed only by a node that has subnet bridge functionality enabled. A node with subnet bridge functionality enabled is known as a Subnet Bridge.

Private Proxy functionality is supported by nodes that support the Proxy feature, Private Network Identity advertising (see [Section 7.2.2.2.4](index-en.html#UUID-1179d3eb-6975-8148-e5b5-a7962035cd19 "7.2.2.2.4. Advertising with Private Network Identity")), and Mesh
Private beacons (see [Section 3.10.4](index-en.html#UUID-7b47a908-e147-61ac-8aa0-d60bd1ad9c37 "3.10.4. Mesh Private beacon")); otherwise, Private Proxy functionality is not supported. When Private Proxy functionality is supported, it can be enabled or disabled.

On-Demand Private Proxy functionality is supported by nodes that support On-Demand Private Proxy Server model (see [Section 4.4.13](index-en.html#UUID-c50312c6-d68d-0472-0e62-d2f09c0e600a "4.4.13. On-Demand Private Proxy Server model")) and Solicitation PDU with
Identification Type equal to 0x00 (see [Section 6.9.1](index-en.html#UUID-73f808b4-bcc9-64ad-51bb-72ef47c91ccf "6.9.1. Solicitation PDU")); otherwise, On-Demand Private Proxy functionality is not supported.

Node Identity functionality is supported by nodes that support exchange of Network PDUs between two nodes connected via GATT; otherwise, Node Identity functionality is not supported.

Private Node Identity functionality is supported by nodes that support Node Identity functionality and Advertising with Private Node Identity (see [Section 7.2.2.2.5](index-en.html#UUID-a987a3e0-2c20-ba0c-3da8-5f10729c013e "7.2.2.2.5. Advertising with Private Node Identity")); otherwise, Private Node Identity functionality is not supported.

#### 2.3.14. Topology

Nodes that support the various features described above can be formed into a mesh network. An illustration of a mesh network is shown in [Figure 2.8](index-en.html#UUID-2dbbe25c-c6d0-f3f2-1fc1-e3987a1fc638_figure-idm4515608854256034088140547756 "Figure 2.8. Example topology of a mesh network") below.

![Example topology of a mesh network](image/1671b81d5518d6.png)

Figure 2.8. Example topology of a mesh network

[Figure 2.8](index-en.html#UUID-2dbbe25c-c6d0-f3f2-1fc1-e3987a1fc638_figure-idm4515608854256034088140547756 "Figure 2.8. Example topology of a mesh network") shows three Relay nodes: Q, R, and S. Although three nodes N, O, and P support the Friend feature, node N
does not have any friendships, and therefore, only O and P are Friend nodes. There are five Low Power nodes: I, J, K, L, and M. Nodes I, J, and K have node P as their friend, while nodes L and M have node O as their friend. Node T is connected to the mesh network using a GATT bearer; therefore, node S retransmits all messages to
and from node T.

For example, if a message is to be sent from T to L, then T will send the message to node S using the GATT bearer. Node S will retransmit this message using the advertising bearer. Nodes H, R, N, and O are within radio range of node S; therefore, they will receive this message. Node O, being the friend of node L will store the
message, and if the message was a segmented message, node O will respond with an acknowledgment at the lower transport layer. Sometime later, L will poll node O to check for new messages, such that O will forward the message originally sent by T to L.

![Example topology of a mesh network using directed forwarding between a source node M and a destination node H.](image/1671b81d55ac96.png)

Figure 2.9. Example topology of a mesh network using directed forwarding between a source node M and a destination node H.

[Figure 2.9](index-en.html#UUID-2dbbe25c-c6d0-f3f2-1fc1-e3987a1fc638_figure-idm4515608719014434088143651793 "Figure 2.9. Example topology of a mesh network using directed forwarding between a source node M and a destination node H.") shows the same topology in
[Figure 2.8](index-en.html#UUID-2dbbe25c-c6d0-f3f2-1fc1-e3987a1fc638_figure-idm4515608854256034088140547756 "Figure 2.8. Example topology of a mesh network"), used in the context of directed forwarding between a source node M and a destination node H. Node M is a Low
Power node and is in friendship with node O. Node O implements directed friend functionality and establishes a 2-lane path on behalf of node M toward the destination node H. Nodes A, C, E, G, N, Q, R, and S support directed relay functionality, but only node R and node S are in the path between node M and node H. Therefore,
regardless of the number of Directed Relay nodes, traffic is confined within the established paths. In this example, nodes E, G, N, and Q do not relay messages from node M to node H, even if they overhear them.

### 2.4. Mesh gateway

A mesh gateway is a node that is able to translate messages between the mesh network and a non-Bluetooth technology. A node may be able to send and receive mesh messages through a mesh gateway while not in the range of any of the Relay nodes. This translation is out of scope for this specification.

### 2.5. Concurrency limitations and restrictions

There are no concurrency limitations or restrictions for nodes imposed by this specification.

### 2.6. Topology limitations and restrictions

There are no topology limitations or restrictions imposed by this specification when used with the LE Physical Transport (see Vol 1, Part A, Section 3.2 in [[24](index-en.html#idp254804)]).
