# Source: https://docs.infrahub.app/schema-library/reference/dwdm.md

# DWDM

This schema extension contains models for OADM (Optical Add Drop Multiplexer) supporting various WDM (Wavelength Division Multiplexing) technologies such as DWDM (Dense Wavelength Division Multiplexing) or CWDM (Coarse Wavelength Division Multiplexing). With some vendors, the tunable optics are not configured via the channel number but via the wavelength and/or the frequency. This model provides a unique entry in Infrahub for those.

## Details[​](#details "Direct link to Details")

* **Dependencies:**

  * [base](/schema-library/reference/dcim.md)
  * [extensions/sfp](/schema-library/reference/sfp.md)

## Nodes[​](#nodes "Direct link to Nodes")

### OpticalMultiplexer[​](#opticalmultiplexer "Direct link to OpticalMultiplexer")

* **Label:** Optical Multiplexer
* **Description:** An OADM (Optical Add Drop Multiplexer) supporting various WDM (Wavelength Division Multiplexing) technologies.
* **Namespace:** Dcim
* **Icon:** mdi
  <!-- -->
  :transit-connection-variant
* **Display Labels:** name\_\_value
* **Human Friendly ID:** name\_\_value
* **Inherit From:** DcimPhysicalDevice

#### Attributes[​](#attributes "Direct link to Attributes")

| name        | description                  | kind     | optional | default\_value | choices    |
| ----------- | ---------------------------- | -------- | -------- | -------------- | ---------- |
| name        |                              | Text     |          |                |            |
| wdm\_type   | Type of WDM (e.g CWDM. DWDM) | Dropdown | False    | dwdm           | cwdm, dwdm |
| description |                              | Text     | True     |                |            |

#### Relationships[​](#relationships "Direct link to Relationships")

| name              | peer                   | optional | cardinality | kind      |
| ----------------- | ---------------------- | -------- | ----------- | --------- |
| front\_interfaces | DcimOadmFrontInterface | True     | many        | Component |
| rear\_interface   | DcimOadmRearInterface  | True     | one         | Component |

### OadmFrontInterface[​](#oadmfrontinterface "Direct link to OadmFrontInterface")

* **Label:** Optical Multiplexer Front Interfaces
* **Namespace:** Dcim
* **Display Labels:** name\_\_value
* **Uniqueness Constraints:**
  * optical\_multiplexer, name\_\_value
* **Human Friendly ID:** optical\_multiplexer\_\_name\_\_value, name\_\_value
* **Inherit From:** DcimEndpoint, DcimGenericOadmInterface

#### Relationships[​](#relationships-1 "Direct link to Relationships")

| name                 | peer                   | optional | cardinality | kind      |
| -------------------- | ---------------------- | -------- | ----------- | --------- |
| optical\_multiplexer | DcimOpticalMultiplexer | False    | one         | Parent    |
| channels             | DcimWdmChannel         | True     | many        | Attribute |

### OadmRearInterface[​](#oadmrearinterface "Direct link to OadmRearInterface")

* **Label:** Optical Multiplexer Rear Interfaces
* **Namespace:** Dcim
* **Display Labels:** name\_\_value
* **Uniqueness Constraints:**
  * optical\_multiplexer, name\_\_value
* **Human Friendly ID:** optical\_multiplexer\_\_name\_\_value, name\_\_value
* **Inherit From:** DcimEndpoint, DcimGenericOadmInterface

#### Relationships[​](#relationships-2 "Direct link to Relationships")

| name                 | peer                   | optional | cardinality | kind   |
| -------------------- | ---------------------- | -------- | ----------- | ------ |
| optical\_multiplexer | DcimOpticalMultiplexer | False    | one         | Parent |

### WdmChannel[​](#wdmchannel "Direct link to WdmChannel")

* **Label:** WDM Channel

* **Description:** A WDM channel with its wavelength and frequency.

* **Namespace:** Dcim

* **Icon:** game-icons
  <!-- -->
  :laser-warning

* **Display Labels:** wdm\_type\_\_value, channel\_\_value

* **Uniqueness Constraints:**

  * frequency\_\_value, wavelength\_\_value, channel\_\_value, wdm\_type\_\_value
  * channel\_\_value, wdm\_type\_\_value

* **Human Friendly ID:** wdm\_type\_\_value, channel\_\_value

#### Attributes[​](#attributes-1 "Direct link to Attributes")

| name       | description                      | kind     | optional | default\_value | choices    |
| ---------- | -------------------------------- | -------- | -------- | -------------- | ---------- |
| channel    | WDM channel number.              | Number   |          |                |            |
| wdm\_type  | Type of WDM (e.g CWDM. DWDM)     | Dropdown | False    | dwdm           | cwdm, dwdm |
| wavelength | Wavelength of the channel in nm. | Text     |          |                |            |
| frequency  | Frequency of the channel in GHz. | Text     |          |                |            |

### WdmSFP[​](#wdmsfp "Direct link to WdmSFP")

* **Label:** WDM SFP
* **Description:** SFP with configuration for Wavelength Division Multiplexing.
* **Namespace:** Dcim
* **Icon:** mdi
  <!-- -->
  :laser-pointer
* **Inherit From:** DcimGenericSFP

#### Attributes[​](#attributes-2 "Direct link to Attributes")

| name      | description                  | kind     | optional | default\_value | choices    |
| --------- | ---------------------------- | -------- | -------- | -------------- | ---------- |
| wdm\_type | Type of WDM (e.g CWDM. DWDM) | Dropdown | False    | dwdm           | cwdm, dwdm |

#### Relationships[​](#relationships-3 "Direct link to Relationships")

| name         | peer           | optional | cardinality | kind      |
| ------------ | -------------- | -------- | ----------- | --------- |
| wdm\_channel | DcimWdmChannel | False    | one         | Attribute |

## Generics[​](#generics "Direct link to Generics")

### GenericOadmInterface[​](#genericoadminterface "Direct link to GenericOadmInterface")

* **Label:** Optical Multiplexer Interfaces
* **Namespace:** Dcim
* **Icon:** mdi
  <!-- -->
  :ethernet

#### Attributes[​](#attributes-3 "Direct link to Attributes")

| name            | description | kind     | optional | default\_value | choices                                                                                                                                                                                        |
| --------------- | ----------- | -------- | -------- | -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| name            |             | Text     |          |                |                                                                                                                                                                                                |
| description     |             | Text     | True     |                |                                                                                                                                                                                                |
| connector\_type |             | Dropdown |          |                | FC, LC, LC\_PC, LC\_UPC, LC\_APC, LSH, LSH\_PC, LSH\_UPC, LSH\_APC, LX\_5, LX\_5\_PC, LX\_5\_UPC, LX\_5\_APC, MPO, MTRJ, SC, SC\_PC, SC\_UPC, SC\_APC, ST, CS, SN, SMA\_905, SMA\_906, URM\_P2 |

## Code[​](#code "Direct link to Code")

```
version: '1.0'
generics:
- name: GenericOadmInterface
  label: Optical Multiplexer Interfaces
  menu_placement: DcimOpticalMultiplexer
  namespace: Dcim
  icon: mdi:ethernet
  attributes:
  - name: name
    kind: Text
    order_weight: 1000
  - name: description
    kind: Text
    optional: true
    order_weight: 2000
  - name: connector_type
    kind: Dropdown
    order_weight: 1100
    choices:
    - name: FC
      label: FC
      description: Standardized fiber optic connector used primarily in datacom and
        telecom applications.
    - name: LC
      label: LC
      description: Compact fiber optic connector with a push-pull mechanism.
    - name: LC_PC
      label: LC/PC
      description: Polished LC connector providing physical contact (PC).
    - name: LC_UPC
      label: LC/UPC
      description: Ultra-Physical Contact (UPC) variant of the LC connector with enhanced
        polish.
    - name: LC_APC
      label: LC/APC
      description: Angled Physical Contact (APC) version of the LC connector with
        a slanted fiber end-face.
    - name: LSH
      label: LSH
      description: European fiber optic connector offering high durability.
    - name: LSH_PC
      label: LSH/PC
      description: Physical Contact version of LSH with standard polish.
    - name: LSH_UPC
      label: LSH/UPC
      description: Ultra-Physical Contact variant of LSH, minimizing return loss with
        a superior polish.
    - name: LSH_APC
      label: LSH/APC
      description: Angled Physical Contact version of LSH, designed to reduce back
        reflections.
    - name: LX_5
      label: LX.5
      description: Miniaturized fiber optic connector similar to LC but with an additional
        shutter mechanism.
    - name: LX_5_PC
      label: LX.5/PC
      description: Physical Contact version of LX.5.
    - name: LX_5_UPC
      label: LX.5/UPC
      description: Ultra-Physical Contact variant of LX.5.
    - name: LX_5_APC
      label: LX.5/APC
      description: Angled Physical Contact version of LX.5.
    - name: MPO
      label: MPO
      description: Multi-fiber Push-On connector typically used in data centers for
        high-speed applications.
    - name: MTRJ
      label: MTRJ
      description: Male-to-female fiber optic connector with two fibers.
    - name: SC
      label: SC
      description: Square fiber optic connector with push-pull lock.
    - name: SC_PC
      label: SC/PC
      description: Physical Contact SC connector with a polished end-face.
    - name: SC_UPC
      label: SC/UPC
      description: Ultra-Physical Contact variant of SC.
    - name: SC_APC
      label: SC/APC
      description: Angled Physical Contact version of SC.
    - name: ST
      label: ST
      description: Bayonet-style fiber optic connector primarily used in industrial
        and military applications.
    - name: CS
      label: CS
      description: Compact connector with a high-density duplex configuration.
    - name: SN
      label: SN
      description: Small-form connector with dual fibers.
    - name: SMA_905
      label: SMA 905
      description: Stainless steel fiber optic connector.
    - name: SMA_906
      label: SMA 906
      description: Variant of SMA 905 with similar durability, frequently used in
        high-vibration settings.
    - name: URM_P2
      label: URM-P2
      description: Specialized fiber optic connector for industrial and harsh environments.
nodes:
- name: OpticalMultiplexer
  label: Optical Multiplexer
  description: An OADM (Optical Add Drop Multiplexer) supporting various WDM (Wavelength
    Division Multiplexing) technologies.
  icon: mdi:transit-connection-variant
  namespace: Dcim
  human_friendly_id:
  - name__value
  order_by:
  - name__value
  display_labels:
  - name__value
  inherit_from:
  - DcimPhysicalDevice
  attributes:
  - name: name
    kind: Text
    unique: true
    order_weight: 1000
  - name: wdm_type
    kind: Dropdown
    description: Type of WDM (e.g CWDM. DWDM)
    order_weight: 1110
    optional: false
    choices:
    - name: cwdm
      label: CWDM (Coarse Wavelength Division Multiplexing)
      description: Supports multiple wavelengths for communication up to 70km.
      color: '#0099cc'
    - name: dwdm
      label: DWDM (Dense Wavelength Division Multiplexing)
      description: Supports dense wavelengths and amplification for long-distance
        communication.
      color: '#9933cc'
    default_value: dwdm
  - name: description
    kind: Text
    optional: true
    order_weight: 2000
  relationships:
  - name: front_interfaces
    peer: DcimOadmFrontInterface
    identifier: front_interfaces
    optional: true
    cardinality: many
    kind: Component
  - name: rear_interface
    peer: DcimOadmRearInterface
    identifier: rear_interfaces
    optional: true
    cardinality: one
    kind: Component
- name: OadmFrontInterface
  label: Optical Multiplexer Front Interfaces
  menu_placement: DcimGenericOadmInterface
  namespace: Dcim
  human_friendly_id:
  - optical_multiplexer__name__value
  - name__value
  display_labels:
  - name__value
  order_by:
  - optical_multiplexer__name__value
  - name__value
  uniqueness_constraints:
  - - optical_multiplexer
    - name__value
  inherit_from:
  - DcimEndpoint
  - DcimGenericOadmInterface
  relationships:
  - name: optical_multiplexer
    peer: DcimOpticalMultiplexer
    order_weight: 900
    identifier: front_interfaces
    optional: false
    cardinality: one
    kind: Parent
  - name: channels
    peer: DcimWdmChannel
    order_weight: 1200
    optional: true
    cardinality: many
    kind: Attribute
- name: OadmRearInterface
  label: Optical Multiplexer Rear Interfaces
  menu_placement: DcimGenericOadmInterface
  namespace: Dcim
  human_friendly_id:
  - optical_multiplexer__name__value
  - name__value
  display_labels:
  - name__value
  order_by:
  - optical_multiplexer__name__value
  - name__value
  uniqueness_constraints:
  - - optical_multiplexer
    - name__value
  inherit_from:
  - DcimEndpoint
  - DcimGenericOadmInterface
  relationships:
  - name: optical_multiplexer
    peer: DcimOpticalMultiplexer
    order_weight: 900
    identifier: rear_interface
    optional: false
    cardinality: one
    kind: Parent
- name: WdmChannel
  namespace: Dcim
  description: A WDM channel with its wavelength and frequency.
  label: WDM Channel
  icon: game-icons:laser-warning
  order_by:
  - wdm_type__value
  - channel__value
  display_labels:
  - wdm_type__value
  - channel__value
  uniqueness_constraints:
  - - frequency__value
    - wavelength__value
    - channel__value
    - wdm_type__value
  - - channel__value
    - wdm_type__value
  human_friendly_id:
  - wdm_type__value
  - channel__value
  attributes:
  - name: channel
    kind: Number
    description: WDM channel number.
  - name: wdm_type
    kind: Dropdown
    description: Type of WDM (e.g CWDM. DWDM)
    order_weight: 1110
    optional: false
    choices:
    - name: cwdm
      label: CWDM (Coarse Wavelength Division Multiplexing)
      description: Supports multiple wavelengths for communication up to 70km.
      color: '#0099cc'
    - name: dwdm
      label: DWDM (Dense Wavelength Division Multiplexing)
      description: Supports dense wavelengths and amplification for long-distance
        communication.
      color: '#9933cc'
    default_value: dwdm
  - name: wavelength
    label: Wavelength (nm)
    kind: Text
    description: Wavelength of the channel in nm.
  - name: frequency
    label: Frequency (GHz)
    kind: Text
    description: Frequency of the channel in GHz.
- name: WdmSFP
  namespace: Dcim
  inherit_from:
  - DcimGenericSFP
  description: SFP with configuration for Wavelength Division Multiplexing.
  label: WDM SFP
  icon: mdi:laser-pointer
  menu_placement: DcimGenericSFP
  attributes:
  - name: wdm_type
    kind: Dropdown
    description: Type of WDM (e.g CWDM. DWDM)
    order_weight: 1110
    optional: false
    choices:
    - name: cwdm
      label: CWDM (Coarse Wavelength Division Multiplexing)
      description: Supports multiple wavelengths for communication up to 70km.
      color: '#0099cc'
    - name: dwdm
      label: DWDM (Dense Wavelength Division Multiplexing)
      description: Supports dense wavelengths and amplification for long-distance
        communication.
      color: '#9933cc'
    default_value: dwdm
  relationships:
  - name: wdm_channel
    label: WDM Channel
    peer: DcimWdmChannel
    kind: Attribute
    cardinality: one
    optional: false
    order_weight: 1150
```
