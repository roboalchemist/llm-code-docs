# Source: https://docs.infrahub.app/schema-library/reference/qos.md

# QoS

This schema extension contains models for Quality of Service (QoS)

## Details[​](#details "Direct link to Details")

* **Dependencies:**
  * [base](/schema-library/reference/dcim.md)

## Nodes[​](#nodes "Direct link to Nodes")

### ForwardingClass[​](#forwardingclass "Direct link to ForwardingClass")

* **Label:** Forwarding Class
* **Description:** Represents a forwarding class in QoS with distinct loss priorities.
* **Namespace:** Qos
* **Display Labels:** name\_\_value
* **Uniqueness Constraints:**
  * name\_\_value
* **Human Friendly ID:** name\_\_value

#### Attributes[​](#attributes "Direct link to Attributes")

| name                       | description                                 | kind | optional | default\_value | choices |
| -------------------------- | ------------------------------------------- | ---- | -------- | -------------- | ------- |
| name                       | Name of the forwarding class.               | Text |          |                |         |
| high\_loss\_priority\_code | List of code points for high loss priority. | List | True     |                |         |
| low\_loss\_priority\_code  | List of code points for low loss priority.  | List | True     |                |         |

### ClassOfService[​](#classofservice "Direct link to ClassOfService")

* **Label:** Class of Service
* **Description:** Defines a Class of Service configuration.
* **Namespace:** Qos
* **Display Labels:** name\_\_value
* **Uniqueness Constraints:**
  * name\_\_value
* **Human Friendly ID:** name\_\_value

#### Attributes[​](#attributes-1 "Direct link to Attributes")

| name | description                   | kind | optional | default\_value | choices |
| ---- | ----------------------------- | ---- | -------- | -------------- | ------- |
| name | Name of the Class of Service. | Text |          |                |         |

#### Relationships[​](#relationships "Direct link to Relationships")

| name                       | peer                     | optional | cardinality | kind |
| -------------------------- | ------------------------ | -------- | ----------- | ---- |
| traffic\_control\_profiles | QosTrafficControlProfile | True     | many        |      |

### TrafficControlProfile[​](#trafficcontrolprofile "Direct link to TrafficControlProfile")

* **Label:** Traffic Control Profile
* **Description:** Defines a traffic control profile with an active/inactive state.
* **Namespace:** Qos
* **Display Labels:** name\_\_value
* **Uniqueness Constraints:**
  * name\_\_value
* **Human Friendly ID:** name\_\_value

#### Attributes[​](#attributes-2 "Direct link to Attributes")

| name   | description                                              | kind     | optional | default\_value | choices          |
| ------ | -------------------------------------------------------- | -------- | -------- | -------------- | ---------------- |
| name   | Name of the traffic control profile.                     | Text     |          |                |                  |
| status | Status of the traffic control profile (active/inactive). | Dropdown |          | inactive       | active, inactive |

### Classifier[​](#classifier "Direct link to Classifier")

* **Label:** Classifier
* **Description:** Represents a classifier mapping DSCP or EXP values to forwarding classes.
* **Namespace:** Qos
* **Display Labels:** name\_\_value
* **Uniqueness Constraints:**
  * name\_\_value
* **Human Friendly ID:** name\_\_value

#### Attributes[​](#attributes-3 "Direct link to Attributes")

| name             | description                           | kind     | optional | default\_value | choices              |
| ---------------- | ------------------------------------- | -------- | -------- | -------------- | -------------------- |
| name             | Name of the classifier.               | Text     |          |                |                      |
| classifier\_type | Type of classifier (DSCP, EXP, etc.). | Dropdown |          |                | dscp, exp, dscp-ipv6 |

#### Relationships[​](#relationships-1 "Direct link to Relationships")

| name                | peer               | optional | cardinality | kind |
| ------------------- | ------------------ | -------- | ----------- | ---- |
| forwarding\_classes | QosForwardingClass | True     | many        |      |

### Scheduler[​](#scheduler "Direct link to Scheduler")

* **Label:** Scheduler
* **Description:** Represents a scheduler configuration.
* **Namespace:** Qos
* **Display Labels:** name\_\_value
* **Uniqueness Constraints:**
  * name\_\_value
* **Human Friendly ID:** name\_\_value

#### Attributes[​](#attributes-4 "Direct link to Attributes")

| name             | description                      | kind     | optional | default\_value | choices                |
| ---------------- | -------------------------------- | -------- | -------- | -------------- | ---------------------- |
| name             | Name of the scheduler.           | Text     |          |                |                        |
| transmit\_rate   | Transmit rate in percentage.     | Number   |          |                |                        |
| buffer\_size     | Buffer size in percentage.       | Number   |          |                |                        |
| priority         | Priority of the scheduler.       | Dropdown | True     |                | low, high, strict-high |
| excess\_priority | Excess priority when applicable. | Dropdown | True     |                | low, high              |

### SchedulerMap[​](#schedulermap "Direct link to SchedulerMap")

* **Label:** Scheduler Map
* **Description:** Defines mappings of schedulers to forwarding classes.
* **Namespace:** Qos
* **Display Labels:** name\_\_value
* **Uniqueness Constraints:**
  * name\_\_value
* **Human Friendly ID:** name\_\_value

#### Attributes[​](#attributes-5 "Direct link to Attributes")

| name | description                | kind | optional | default\_value | choices |
| ---- | -------------------------- | ---- | -------- | -------------- | ------- |
| name | Name of the scheduler map. | Text |          |                |         |

#### Relationships[​](#relationships-2 "Direct link to Relationships")

| name                | peer               | optional | cardinality | kind |
| ------------------- | ------------------ | -------- | ----------- | ---- |
| schedulers          | QosScheduler       | True     | many        |      |
| forwarding\_classes | QosForwardingClass | True     | many        |      |

## Code[​](#code "Direct link to Code")

```
version: '1.0'
nodes:
- name: ForwardingClass
  namespace: Qos
  label: Forwarding Class
  description: Represents a forwarding class in QoS with distinct loss priorities.
  display_labels:
  - name__value
  order_by:
  - name__value
  human_friendly_id:
  - name__value
  uniqueness_constraints:
  - - name__value
  menu_placement: QosClassOfService
  attributes:
  - name: name
    kind: Text
    description: Name of the forwarding class.
    unique: true
    order_weight: 1000
  - name: high_loss_priority_code
    kind: List
    description: List of code points for high loss priority.
    optional: true
    order_weight: 1200
  - name: low_loss_priority_code
    kind: List
    description: List of code points for low loss priority.
    optional: true
    order_weight: 1300
- name: ClassOfService
  namespace: Qos
  label: Class of Service
  description: Defines a Class of Service configuration.
  display_labels:
  - name__value
  order_by:
  - name__value
  human_friendly_id:
  - name__value
  uniqueness_constraints:
  - - name__value
  attributes:
  - name: name
    kind: Text
    description: Name of the Class of Service.
    unique: true
    order_weight: 1000
  relationships:
  - name: traffic_control_profiles
    peer: QosTrafficControlProfile
    description: List of traffic control profiles.
    cardinality: many
    optional: true
    order_weight: 1200
- name: TrafficControlProfile
  namespace: Qos
  label: Traffic Control Profile
  description: Defines a traffic control profile with an active/inactive state.
  display_labels:
  - name__value
  order_by:
  - name__value
  human_friendly_id:
  - name__value
  uniqueness_constraints:
  - - name__value
  menu_placement: QosClassOfService
  attributes:
  - name: name
    kind: Text
    description: Name of the traffic control profile.
    unique: true
    order_weight: 1000
  - name: status
    kind: Dropdown
    description: Status of the traffic control profile (active/inactive).
    choices:
    - name: active
      label: Active
    - name: inactive
      label: Inactive
    default_value: inactive
    order_weight: 1200
- name: Classifier
  namespace: Qos
  label: Classifier
  description: Represents a classifier mapping DSCP or EXP values to forwarding classes.
  display_labels:
  - name__value
  order_by:
  - name__value
  human_friendly_id:
  - name__value
  uniqueness_constraints:
  - - name__value
  menu_placement: QosClassOfService
  attributes:
  - name: name
    kind: Text
    description: Name of the classifier.
    unique: true
    order_weight: 1000
  - name: classifier_type
    kind: Dropdown
    description: Type of classifier (DSCP, EXP, etc.).
    choices:
    - name: dscp
      label: DSCP Classifier
    - name: exp
      label: EXP Classifier
    - name: dscp-ipv6
      label: DSCP-IPv6 Classifier
    order_weight: 1200
  relationships:
  - name: forwarding_classes
    peer: QosForwardingClass
    description: List of forwarding classes defined in the classifier.
    cardinality: many
    optional: true
    order_weight: 1300
- name: Scheduler
  namespace: Qos
  label: Scheduler
  description: Represents a scheduler configuration.
  display_labels:
  - name__value
  order_by:
  - name__value
  human_friendly_id:
  - name__value
  uniqueness_constraints:
  - - name__value
  menu_placement: QosClassOfService
  attributes:
  - name: name
    kind: Text
    description: Name of the scheduler.
    unique: true
    order_weight: 1000
  - name: transmit_rate
    label: Transmit Rate (%)
    kind: Number
    description: Transmit rate in percentage.
    order_weight: 1200
  - name: buffer_size
    label: Buffer Size (%)
    kind: Number
    description: Buffer size in percentage.
    order_weight: 1300
  - name: priority
    kind: Dropdown
    description: Priority of the scheduler.
    choices:
    - name: low
      label: Low Priority
    - name: high
      label: High Priority
    - name: strict-high
      label: Strict High Priority
    optional: true
    order_weight: 1400
  - name: excess_priority
    kind: Dropdown
    description: Excess priority when applicable.
    choices:
    - name: low
      label: Low Excess Priority
    - name: high
      label: High Excess Priority
    optional: true
    order_weight: 1500
- name: SchedulerMap
  namespace: Qos
  label: Scheduler Map
  description: Defines mappings of schedulers to forwarding classes.
  display_labels:
  - name__value
  order_by:
  - name__value
  human_friendly_id:
  - name__value
  uniqueness_constraints:
  - - name__value
  menu_placement: QosClassOfService
  attributes:
  - name: name
    kind: Text
    description: Name of the scheduler map.
    unique: true
    order_weight: 1000
  relationships:
  - name: schedulers
    peer: QosScheduler
    description: List of schedulers defined in the map.
    cardinality: many
    optional: true
    order_weight: 1200
  - name: forwarding_classes
    peer: QosForwardingClass
    description: List of forwarding classes associated with schedulers.
    cardinality: many
    optional: true
    order_weight: 1300
```
