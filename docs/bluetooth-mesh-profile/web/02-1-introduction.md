# Source: https://www.bluetooth.com/wp-content/uploads/Files/Specification/HTML/MshPRT_v1.1/out/en/index-en.html

## 1. Introduction

The Mesh Protocol specification (previously named Mesh Profile, as noted in the Version History) defines fundamental requirements to enable an interoperable mesh networking solution for Bluetooth low energy wireless technology.

Terms, acronyms, and abbreviations that have a specific meaning in the context of this specification or the Bluetooth environment in general are defined or expanded upon on their first use. Defined terms that are used in this specification are listed in [Section 1.5](index-en.html#UUID-a4a5435a-0e4e-ad22-c4d7-c09cb025d0ac "1.5. Terminology").

### 1.1. Conformance

Each capability of this specification shall be supported in the specified manner. This specification may provide options for design flexibility, because, for example, some products do not implement every portion of the specification. For each implementation option that is supported, it shall be supported as specified.

### 1.2. Bluetooth specification release compatibility

This specification shall be used with:

* Core Specification Addendum 6 [[3](index-en.html#idp254744)] combined with an allowed Bluetooth Core Specification (see [[2](index-en.html#idp254742)] Volume 1, Part D, Section 1.2, Table 1.3), OR
* Any version of the Bluetooth Core Specification later than v5.0.

The Generic Attribute Profile (GATT) is required if the GATT provisioning bearer defined in [Section 5.2.2](index-en.html#UUID-fe54c9f6-602f-fa6d-3b92-029198c9c8a7 "5.2.2. PB-GATT") is supported or if the GATT bearer defined in [Section 3.3.2](index-en.html#UUID-2d60af03-4443-f026-58fe-b2ce0261f42b "3.3.2. GATT bearer") is supported.

### 1.3. Language

#### 1.3.1. Language conventions

In the development of a specification, the Bluetooth SIG has established the following conventions for use of the terms *“shall”*, *“shall not”*, *“should”*, *“should not”*,
*“may”*, *“must”*, and *“can”*. In this Bluetooth specification, the terms in [Table 1.1](index-en.html#UUID-d1eb13d3-64ef-e23e-e812-46d53a35fe1d_Table_1.1 "Table 1.1. Language conventions terms and definitions") have the specific meanings given in that table, irrespective of other meanings that exist.

| **Term** | **Definition** |
| --- | --- |
| shall | —used to express what is required by the specification and is to be implemented exactly as written without deviation |
| shall not | —used to express what is forbidden by the specification |
| should | —used to express what is recommended by the specification without forbidding anything |
| should not | —used to indicate that something is discouraged but not forbidden by the specification |
| may | —used to indicate something that is permissible within the limits of the specification |
| must | —used to indicate either:  1. an indisputable statement of fact that is always true regardless of the circumstances 2. an implication or natural consequence if a separately-stated requirement is followed |
| can | —used to express a statement of possibility or capability |

Table 1.1. Language conventions terms and definitions

Certain terms used in this specification have been updated and are no longer used by Bluetooth SIG. For a list of terms that have been updated and their replacement terms, see the Appropriate Language Mapping Tables [[25](index-en.html#idp254806)].

##### 1.3.1.1. Implementation alternatives

When specification content indicates that there are multiple alternatives to satisfy specification requirements, if one alternative is explained or illustrated in an example it is not intended to limit other alternatives that the specification requirements permit.

##### 1.3.1.2. Discrepancies

It is the goal of Bluetooth SIG that specifications are clear, unambiguous, and do not contain discrepancies. However, members can report any perceived discrepancy by filing an erratum and can request a test case waiver as appropriate.

#### 1.3.2. Reserved for Future Use

Where a field in a packet, Protocol Data Unit (PDU), or other data structure is described as "Reserved for Future Use" (irrespective of whether in uppercase or lowercase), the device creating the structure shall set its value to zero unless otherwise specified in this specification. Any device receiving or interpreting the
structure shall ignore that field unless otherwise specified in this specification; in particular, it shall not reject the structure because of the value of the field.

Where a field, parameter, or other variable object can take a range of values and some values are described as "Reserved for Future Use," a device sending the object shall not set the object to those values. A device receiving an object with such a value should reject it, and any data structure containing it, as being erroneous;
however, this does not apply in a context where the object is described as being ignored or it is specified to ignore unrecognized values.

When a field value is a bit field, unassigned bits can be marked as Reserved for Future Use and shall be set to 0. Implementations that receive a message that contains a Reserved for Future Use bit that is set to 1 shall process the message as if that bit was set to 0, except where specified otherwise in this specification.

The acronym RFU is equivalent to "Reserved for Future Use."

#### 1.3.3. Prohibited

When a field value is an enumeration, unassigned values can be marked as “Prohibited.” These values shall never be used by an implementation, and any message received that includes a Prohibited value shall be ignored and shall not be processed and shall not be responded to, unless otherwise specified in this specification.

Where a field, parameter, or other variable object can take a range of values, and some values are described as “Prohibited,” devices shall not set the object to any of those Prohibited values. A device receiving an object with such a value should reject it, and any data structure containing it, as being erroneous, unless
otherwise specified in this specification.

“Prohibited” is never abbreviated.

### 1.4. Table conventions

This section describes conventions regarding the following:

* Requirements that are in a table
* Indicating a cell that has no value or content

#### 1.4.1. Requirements that are in a table

Unless otherwise stated, requirements that are in a table in this specification can be defined as "Mandatory" (M), "Optional" (O), "Excluded" (X), or "Conditional" (C.n). Conditional statements (C.n) are listed directly below the table in which they appear.

#### 1.4.2. Indicating a cell that has no value or content

Where a cell in a table indicates an intended absence of a value or other content, the cell will contain “none” or a hyphen (i.e., a “minus” sign). Examples of this are:

* In the “condition” column of the description of a finite state machine where a rule is unconditional
* In the “action” column of the description of a finite state machine where a rule has no action
* In a “restrictions” column where there are no applicable restrictions
* In an interface description where there are no parameters of a specific type

An empty cell in a table indicates that there is no useful information that can be placed in that cell. Examples of this are:

* In a “comments” column when there is no comment to make in a particular row
* In a column specifying properties when the relevant item is reserved for future use (and therefore does not have any properties)
* In a “units” column when the relevant item is unitless

### 1.5. Terminology

[Table 1.2](index-en.html#UUID-a4a5435a-0e4e-ad22-c4d7-c09cb025d0ac_Table_1.2 "Table 1.2. Terminology") lists all of the defined terms used in this specification.

| Term | Definition Location |
| --- | --- |
| accept list | [Section 6.4.1](index-en.html#UUID-ea5adb7e-b82f-c2bc-024f-9df54eb2dc17 "6.4.1. Filter types") |
| Access message | [Section 3.7.2](index-en.html#UUID-f65c4984-f100-77c9-d5e5-7a161e002bb9 "3.7.2. Access message") |
| address | [Section 3.4.2](index-en.html#UUID-d00b17f6-feae-0749-6734-e8b9d952d2bb "3.4.2. Addresses") |
| application key (AppKey) | [Section 3.9.6](index-en.html#UUID-2b66a565-a23e-1531-b7c2-29c7962145ad "3.9.6. Keys") |
| beacon | [Section 3.10](index-en.html#UUID-f17ee0cf-93c1-0e9e-1c41-d35b0d204a9f "3.10. Mesh beacons") |
| bound states | [Section 2.3.2](index-en.html#UUID-8b781a3a-8e9f-8707-1a28-d04bb4bdb83f "2.3.2. Bound states") |
| composite state | [Section 2.3.1](index-en.html#UUID-cf82584a-ed77-2a0c-55fa-cc01f17c57eb "2.3.1. States") |
| Configuration Manager | [Section 2.2.2](index-en.html#UUID-3cc64993-ea9e-1b46-7421-abcc642eedd3 "2.2.2. Devices") |
| device | [Section 2.2.2](index-en.html#UUID-3cc64993-ea9e-1b46-7421-abcc642eedd3 "2.2.2. Devices") |
| device key (DevKey) | [Section 3.9.6](index-en.html#UUID-2b66a565-a23e-1531-b7c2-29c7962145ad "3.9.6. Keys") |
| directed forwarding | [Section 2.3.11](index-en.html#UUID-f41a44a2-4b53-dc5e-0371-9e1a6cf8ad48 "2.3.11. Directed forwarding") |
| directed relay | [Section 2.3.13](index-en.html#UUID-63a2951f-d940-de76-94f0-744b45622131 "2.3.13. Features and functionality") |
| element | [Section 2.3.4](index-en.html#UUID-5db857eb-73fe-195b-1bb3-09880ad0c535 "2.3.4. Elements") |
| foundation models | [Section 4](index-en.html#UUID-c2bbeabd-dcd8-c62a-d660-b83abb347dda "4. Foundation models") |
| friendship | [Section 2.2.5](index-en.html#UUID-90c5d44d-f657-9cd3-733e-2f8ad846ae5a "2.2.5. Low power support") |
| IV Index | [Section 2.3.10.4](index-en.html#UUID-7e70c775-3ca9-13ca-492b-fe9cf3444457 "2.3.10.4. Initialization vector index") |
| key identifier | [Section 2.3.10.3](index-en.html#UUID-afb14c49-471b-0a71-dcfe-147951ca71ba "2.3.10.3. Network and application key identifiers") |
| low power | [Section 2.2.5](index-en.html#UUID-90c5d44d-f657-9cd3-733e-2f8ad846ae5a "2.2.5. Low power support") |
| managed flooding | [Section 2.2](index-en.html#UUID-59567b3e-ff9c-e95c-262f-5ecf9fdc3d34 "2.2. Overview of mesh operation") |
| mesh gateway | [Section 2.4](index-en.html#UUID-3fe43776-d695-389e-b232-a295d0db1a16 "2.4. Mesh gateway") |
| Mesh Manager | [Section 2.2.2](index-en.html#UUID-3cc64993-ea9e-1b46-7421-abcc642eedd3 "2.2.2. Devices") |
| mesh network | [Section 2.2.1](index-en.html#UUID-569c4c62-28af-beab-3c12-ae4fde1742ff "2.2.1. Network and subnets") |
| mesh profile | [Section 2.1](index-en.html#UUID-5a00137e-ae3d-00cf-cd29-abf59856cf26 "2.1. Layered architecture") |
| model | [Section 2.3.6](index-en.html#UUID-9cc6a130-3bbf-847a-91f6-2ff5a9f37ef9 "2.3.6. Models") |
| multilane path | [Section 3.6.8.1.1](index-en.html#UUID-9ea05810-ba5d-5c06-1507-312f131183fe "3.6.8.1.1. Multilane paths") |
| neighboring node | [Section 2.2](index-en.html#UUID-59567b3e-ff9c-e95c-262f-5ecf9fdc3d34 "2.2. Overview of mesh operation") |
| network key (NetKey) | [Section 3.9.6](index-en.html#UUID-2b66a565-a23e-1531-b7c2-29c7962145ad "3.9.6. Keys") |
| Network Message Cache | [Section 3.4.6.5](index-en.html#UUID-9c785f13-300e-0afe-d592-fe2f37ee4869 "3.4.6.5. Network Message Cache") |
| node | [Section 2.2.2](index-en.html#UUID-3cc64993-ea9e-1b46-7421-abcc642eedd3 "2.2.2. Devices") |
| obfuscation | [Section 2.3.10.2](index-en.html#UUID-7c2383dd-328e-d763-c1b7-22a720063859 "2.3.10.2. Obfuscation") |
| path | [Section 2.3.11](index-en.html#UUID-f41a44a2-4b53-dc5e-0371-9e1a6cf8ad48 "2.3.11. Directed forwarding") |
| primary element | [Section 2.3.4](index-en.html#UUID-5db857eb-73fe-195b-1bb3-09880ad0c535 "2.3.4. Elements") |
| primary subnet | [Section 2.2.1](index-en.html#UUID-569c4c62-28af-beab-3c12-ae4fde1742ff "2.2.1. Network and subnets") |
| Provisionee | [Section 5.4](index-en.html#UUID-3b8e4e4b-4422-810a-8e0e-bcb1913572a2 "5.4. Provisioning protocol") |
| Provisioner | [Section 2.2.2](index-en.html#UUID-3cc64993-ea9e-1b46-7421-abcc642eedd3 "2.2.2. Devices") |
| provisioning | [Section 2.2.3](index-en.html#UUID-cc301db0-ba02-d038-8dda-d28b57f7938c "2.2.3. Adding devices to a mesh network") |
| Proxy feature | [Section 2.3.13](index-en.html#UUID-63a2951f-d940-de76-94f0-744b45622131 "2.3.13. Features and functionality") |
| Proxy node | [Section 2.3.13](index-en.html#UUID-63a2951f-d940-de76-94f0-744b45622131 "2.3.13. Features and functionality") |
| Proxy Server | [Section 2.1.7](index-en.html#UUID-edbad4e3-7f62-6b38-623d-34ca6f92f574 "2.1.7. Bearer layer") |
| reject list | [Section 6.4.1](index-en.html#UUID-ea5adb7e-b82f-c2bc-024f-9df54eb2dc17 "6.4.1. Filter types") |
| Relay feature | [Section 2.3.13](index-en.html#UUID-63a2951f-d940-de76-94f0-744b45622131 "2.3.13. Features and functionality") |
| Relay node | [Section 2.3.13](index-en.html#UUID-63a2951f-d940-de76-94f0-744b45622131 "2.3.13. Features and functionality") |
| remote provisioning | [Section 5](index-en.html#UUID-c2ed2695-c7e2-6000-08bb-72c4b7c7e7fe "5. Provisioning") |
| replay protection | [Section 3.9.8](index-en.html#UUID-c39c2e5d-eba0-ea25-6edb-f88aa4bef4e5 "3.9.8. Message replay protection") |
| secondary element | [Section 2.3.4](index-en.html#UUID-5db857eb-73fe-195b-1bb3-09880ad0c535 "2.3.4. Elements") |
| state | [Section 2.3.1](index-en.html#UUID-cf82584a-ed77-2a0c-55fa-cc01f17c57eb "2.3.1. States") |
| subnet | [Section 2.2.1](index-en.html#UUID-569c4c62-28af-beab-3c12-ae4fde1742ff "2.2.1. Network and subnets") |
| tagging | [Section 2.1](index-en.html#UUID-5a00137e-ae3d-00cf-cd29-abf59856cf26 "2.1. Layered architecture") |
| term | [Section 2.3.7](index-en.html#UUID-46f8e936-55f4-be60-152c-2de49fca322e "2.3.7. Terms") |
| Transport Control message | [Section 3.6.3](index-en.html#UUID-3d3d31e4-d555-364d-bd0e-4bcef00386d4 "3.6.3. Upper Transport Control PDU") |
| unprovisioned device | [Section 2.2.2](index-en.html#UUID-3cc64993-ea9e-1b46-7421-abcc642eedd3 "2.2.2. Devices") |
| unsolicited message | [Section 2.3.3](index-en.html#UUID-5bdfda52-ba1c-68d5-d7b8-7c4a8e2db889 "2.3.3. Messages") |

Table 1.2. Terminology
