# Source: https://documentation.ubuntu.com/lxd/en/latest/howto/network_acls/

[]

# How to configure network ACLs[¶](#how-to-configure-network-acls "Link to this heading")

Note

Network ACLs are available for the [[OVN NIC type]](../../reference/devices_nic/#nic-ovn), the [[OVN network]](../../reference/network_ovn/#network-ovn) and the [[Bridge network]](../../reference/network_bridge/#network-bridge) (with some exceptions; see [[Bridge limitations]](#network-acls-bridge-limitations)).

[[▶] [Watch on YouTube]](https://www.youtube.com/watch?v=mu34G0cX6Io)

Network ACLs define rules for controlling traffic:

-   Between instances connected to the same network

-   To and from other networks

Network ACLs can be assigned directly to the NIC of an instance, or to a network. When assigned to a network, the ACL applies indirectly to all NICs connected to that network.

When an ACL is assigned to multiple instance NICs, either directly or indirectly, those NICs form a logical port group. You can use the name of that ACL to refer to that group in the traffic rules of other ACLs. For more information, see: [[Subject name selectors (ACL groups)]](#network-acls-selectors-subject-name).

[]

## List ACLs[¶](#list-acls "Link to this heading")

CLI

API

UI

To list all ACLs, run:

    lxc network acl list

To list all ACLs, query the [[`GET`]` `[`/1.0/network-acls`]](/lxd/latest/api/#/network-acls/network_acls_get) endpoint:

    lxc query --request GET /1.0/network-acls

You can also use [[recursion]](../../rest-api/#rest-api-recursion) to list the ACLs with a higher level of detail:

    lxc query --request GET /1.0/network-acls?recursion=1

View ACL information from the [Networking] section of the main navigation.

[]

## Show an ACL[¶](#show-an-acl "Link to this heading")

CLI

API

UI

To show details about a specific ACL, run:

    lxc network acl show <ACL-name>

Example:

    lxc network acl show my-acl

For details about a specific ACL, query the [[`GET`]` `[`/1.0/network-acls/`]](/lxd/latest/api/#/network-acls/network_acl_get) endpoint\`:

    lxc query --request GET /1.0/network-acls/

Example:

    lxc query --request GET /1.0/network-acls/my-acl

To show the detail page of an ACL, select the desired ACL from the [ACLs] page.

<figure class="align-default">
<a href="../../_images/network_ACLs.png" class="reference internal image-reference"><img src="../../_images/network_ACLs.png" style="width: 80%;" alt="A Network ACL in LXD" /></a>
</figure>

[]

## Create an ACL[¶](#create-an-acl "Link to this heading")

[]

### Name requirements[¶](#name-requirements "Link to this heading")

Network ACL names must meet the following requirements:

-   Must be between 1 and 63 characters long.

-   Can contain only ASCII letters (a--z, A--Z), numbers (0--9), and dashes (-).

-   Cannot begin with a digit or a dash.

-   Cannot end with a dash.

### Instructions[¶](#instructions "Link to this heading")

CLI

API

UI

To create an ACL, run:

    lxc network acl create <ACL-name> [user.KEY=value ...]

-   You must provide an ACL name that meets the [[Name requirements]](#network-acls-name-requirements).

-   You can optionally provide one or more custom [`user`] keys to store metadata or other information.

ACLs have no rules upon creation via command line, so as a next step, [[add rules]](#network-acls-rules) to the ACL. You can also [[edit the ACL configuration]](#network-acls-edit), or [[assign the ACL to a network or NIC]](#network-acls-assign).

Another way to create ACLs from the command line is to provide a YAML configuration file:

    lxc network acl create <ACL-name> < <filename.yaml>

This file can include any other [[ACL properties]](#network-acls-properties), including the [`egress`] and [`ingress`] properties for defining [[ACL rules]](#network-acls-rules). See the second example in the set below.

Examples

Create an ACL with the name [`my-acl`] and an optional custom user key:

    lxc network acl create my-acl user.my-key=my-value

Create an ACL using a YAML configuration file:

First, create a file named [`config.yaml`] with the following content:

    description: Allow web traffic from internal network
    config:
      user.owner: devops
    ingress:
      - action: allow
        description: Allow HTTP/HTTPS from internal
        protocol: tcp
        source: "@internal"
        destination_port: "80,443"
        state: enabled

Note that the custom user keys are stored under the [`config`] property.

The following command creates an ACL from that file's configuration:

    lxc network acl create my-acl < config.yaml

To create an ACL, query the [[`POST`]` `[`/1.0/network-acls`]](/lxd/latest/api/#/network-acls/network_acls_post) endpoint:

    lxc query --request POST /1.0/network-acls --data ',
      "description": "<description of the ACL>",
      "egress": [, ],
      "ingress": [, ]
    }'

-   You must provide an ACL name that meets the [[Name requirements]](#network-acls-name-requirements).

-   You can optionally provide one or more custom [`config.user.*`] keys to store metadata or other information.

-   The [`ingress`] and [`egress`] lists contain rules for inbound and outbound traffic. See [[ACL rules]](#network-acls-rules) for details.

Examples

Create an ACL with the name [`my-acl`], a custom user key of [`my-key`], and a [`description`]:

    lxc query --request POST /1.0/network-acls --data ',
      "description": "Web servers"
    }'

Create an ACL with the name [`my-acl`] and an [`ingress`] rule:

    lxc query --request POST /1.0/network-acls --data '
      ]
    }'

To create an ACL, navigate to [ACLs] from the [Networking] tab in the main navigation, then click the [Create ACL] button in the upper-right corner.

<figure class="align-default">
<a href="../../_images/network_ACL_create.png" class="reference internal image-reference"><img src="../../_images/network_ACL_create.png" style="width: 80%;" alt="Create an ACL in LXD" /></a>
</figure>

[]

### ACL properties[¶](#acl-properties "Link to this heading")

ACLs have the following properties:

[[`config`]][]

User-provided free-form key/value pairs

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#network-acl-acl-properties:config)]

+-----------------------------------+---------------------------------------------------+
| **Key:**                          | [`config`] |
+-----------------------------------+---------------------------------------------------+
| **Type:**                         | []                                      |
|                                   |                                                   |
|                                   | string set                                        |
+-----------------------------------+---------------------------------------------------+
| **Required:**                     | []                                      |
|                                   |                                                   |
|                                   | no                                                |
+-----------------------------------+---------------------------------------------------+

The only supported keys are [`user.*`] custom keys.

[[`description`]][]

Description of the network ACL

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#network-acl-acl-properties:description)]

+-----------------------------------+--------------------------------------------------------+
| **Key:**                          | [`description`] |
+-----------------------------------+--------------------------------------------------------+
| **Type:**                         | []                                           |
|                                   |                                                        |
|                                   | string                                                 |
+-----------------------------------+--------------------------------------------------------+
| **Required:**                     | []                                           |
|                                   |                                                        |
|                                   | no                                                     |
+-----------------------------------+--------------------------------------------------------+

[[`egress`]][]

Egress traffic rules

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#network-acl-acl-properties:egress)]

+-----------------------------------+---------------------------------------------------+
| **Key:**                          | [`egress`] |
+-----------------------------------+---------------------------------------------------+
| **Type:**                         | []                                      |
|                                   |                                                   |
|                                   | rule list                                         |
+-----------------------------------+---------------------------------------------------+
| **Required:**                     | []                                      |
|                                   |                                                   |
|                                   | no                                                |
+-----------------------------------+---------------------------------------------------+

[[`ingress`]][]

Ingress traffic rules

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#network-acl-acl-properties:ingress)]

+-----------------------------------+----------------------------------------------------+
| **Key:**                          | [`ingress`] |
+-----------------------------------+----------------------------------------------------+
| **Type:**                         | []                                       |
|                                   |                                                    |
|                                   | rule list                                          |
+-----------------------------------+----------------------------------------------------+
| **Required:**                     | []                                       |
|                                   |                                                    |
|                                   | no                                                 |
+-----------------------------------+----------------------------------------------------+

[[`name`]][]

Unique name of the network ACL in the project

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#network-acl-acl-properties:name)]

+-----------------------------------+-------------------------------------------------+
| **Key:**                          | [`name`] |
+-----------------------------------+-------------------------------------------------+
| **Type:**                         | []                                    |
|                                   |                                                 |
|                                   | string                                          |
+-----------------------------------+-------------------------------------------------+
| **Required:**                     | []                                    |
|                                   |                                                 |
|                                   | yes                                             |
+-----------------------------------+-------------------------------------------------+

[]

## ACL rules[¶](#acl-rules "Link to this heading")

Each ACL contains two lists of rules:

-   Rules in the [`egress`] list apply to outbound traffic from the NIC.

-   Rules in the [`ingress`] list apply to inbound traffic to the NIC.

For both [`egress`] and [`ingress`], the rule configuration looks like this:

YAML

JSON

    action: <allow|reject|drop>
    description: <description>
    destination: <destination-IP-range>
    destination_port: <destination-port-number>
    icmp_code: <ICMP-code>
    icmp_type: <ICMP-type>
    protocol: <icmp4|icmp6|tcp|udp>
    source: <source-of-traffic>
    source_port: <source-port-number>
    state: <enabled|disabled|logged>

    

-   The **[`action`]** property is required.

-   The **[`source`]** and **[`destination`]** properties can be specified as one or more CIDR blocks, IP ranges, or [[selectors]](#network-acls-selectors). If left empty, they match any source or destination. Comma-separate multiple values.

-   If the **[`protocol`]** is unset, it matches any protocol.

-   The **[`destination_port`]** and **[`source_port`]** properties and **[`icmp_code`]** and **[`icmp_type`]** properties are mutually exclusive sets. Although both sets are shown in the same rule above to demonstrate the syntax, they never appear together in practice.

    -   The **[`destination_port`]** and **[`source_port`]** properties are only available when the **[`protocol`]** for the rule is [`tcp`] or [`udp`].

    -   The [**[`icmp_code`]**](https://www.iana.org/assignments/icmp-parameters/icmp-parameters.xhtml#icmp-parameters-codes) and [**[`icmp_type`]**](https://www.iana.org/assignments/icmp-parameters/icmp-parameters.xhtml#icmp-parameters-types) properties are only available when the **[`protocol`]** is [`icmp4`] or [`icmp6`].

-   The **[`state`]** is [`enabled`] by default. The [`logged`] value is used to [[log traffic]](#network-acls-log) to a rule.

For more information, see: [[Rule properties]](#network-acls-rule-properties).

### Add a rule[¶](#add-a-rule "Link to this heading")

CLI

API

UI

To add a rule to an ACL, run:

    lxc network acl rule add <ACL-name> <egress|ingress> [properties...]

Example

Add an [`egress`] rule with an [`action`] of [`drop`] to [`my-acl`]:

    lxc network acl rule add my-acl egress action=drop

There is no specific endpoint for adding a rule. Instead, you must [[edit the full ACL]](#network-acls-edit), which contains the [`egress`] and [`ingress`] lists.

To add an ingress or egress rule to an ACL, go to its [[detail page]](#network-acls-show).

Click [Add rule], then configure your ingress or egress settings.

<figure class="align-default">
<a href="../../_images/network_ACL_addrule.png" class="reference internal image-reference"><img src="../../_images/network_ACL_addrule.png" style="width: 80%;" alt="Add a rule to an ACL in LXD" /></a>
</figure>

Note that the [Save changes] button displays the number of changes you have made. Save your changes.

### Remove a rule[¶](#remove-a-rule "Link to this heading")

CLI

API

UI

To remove a rule from an ACL, run:

    lxc network acl rule remove <ACL-name> <egress|ingress> [properties...]

You must either specify all properties needed to uniquely identify a rule or add [`--force`] to the command to delete all matching rules.

There is no specific endpoint for removing a rule. Instead, you must [[edit the full ACL]](#network-acls-edit), which contains the [`egress`] and [`ingress`] lists.

To remove a rule from an ACL, go to the ACL's [[detail page]](#network-acls-show). From the row of the rule to remove, click the [Delete] button.

<figure class="align-default">
<a href="../../_images/network_ACL_remove_edit.png" class="reference internal image-reference"><img src="../../_images/network_ACL_remove_edit.png" style="width: 80%;" alt="Add a rule to an ACL in LXD" /></a>
</figure>

Note that the [Save changes] button displays the number of changes you have made. Save your changes.

### Edit a rule[¶](#edit-a-rule "Link to this heading")

You cannot edit a rule directly. Instead, you must [[edit the full ACL]](#network-acls-edit), which contains the [`egress`] and [`ingress`] lists.

### Rule ordering and application of actions[¶](#rule-ordering-and-application-of-actions "Link to this heading")

ACL rules are defined as lists, but their order within the list does not affect how they are applied.

LXD automatically prioritizes rules based on the action property, in the following order:

-   [`drop`]

-   [`reject`]

-   [`allow`]

-   The default action for unmatched traffic (defaults to [`reject`], see [[Configure default actions]](#network-acls-defaults))

When you assign multiple ACLs to a NIC, you do not need to coordinate rule order across them. As soon as a rule matches, its action is applied and no further rules are evaluated.

[]

### Rule properties[¶](#rule-properties "Link to this heading")

ACL rules have the following properties:

[[`action`]][]

Action to take for matching traffic

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#network-acl-rule-properties:action)]

+-----------------------------------+---------------------------------------------------+
| **Key:**                          | [`action`] |
+-----------------------------------+---------------------------------------------------+
| **Type:**                         | []                                      |
|                                   |                                                   |
|                                   | string                                            |
+-----------------------------------+---------------------------------------------------+
| **Required:**                     | []                                      |
|                                   |                                                   |
|                                   | yes                                               |
+-----------------------------------+---------------------------------------------------+

Possible values are [`allow`], [`reject`], and [`drop`].

[[`description`]][]

Description of the rule

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#network-acl-rule-properties:description)]

+-----------------------------------+--------------------------------------------------------+
| **Key:**                          | [`description`] |
+-----------------------------------+--------------------------------------------------------+
| **Type:**                         | []                                           |
|                                   |                                                        |
|                                   | string                                                 |
+-----------------------------------+--------------------------------------------------------+
| **Required:**                     | []                                           |
|                                   |                                                        |
|                                   | no                                                     |
+-----------------------------------+--------------------------------------------------------+

[[`destination`]][]

Comma-separated list of destinations

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#network-acl-rule-properties:destination)]

+-----------------------------------+--------------------------------------------------------+
| **Key:**                          | [`destination`] |
+-----------------------------------+--------------------------------------------------------+
| **Type:**                         | []                                           |
|                                   |                                                        |
|                                   | string                                                 |
+-----------------------------------+--------------------------------------------------------+
| **Required:**                     | []                                           |
|                                   |                                                        |
|                                   | no                                                     |
+-----------------------------------+--------------------------------------------------------+

Destinations can be specified as CIDR or IP ranges, destination subject name selectors (for egress rules), or be left empty for any.

[[`destination_port`]][]

Destination ports or port ranges

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#network-acl-rule-properties:destination_port)]

+-----------------------------------+-------------------------------------------------------------+
| **Key:**                          | [`destination_port`] |
+-----------------------------------+-------------------------------------------------------------+
| **Type:**                         | []                                                |
|                                   |                                                             |
|                                   | string                                                      |
+-----------------------------------+-------------------------------------------------------------+
| **Required:**                     | []                                                |
|                                   |                                                             |
|                                   | no                                                          |
+-----------------------------------+-------------------------------------------------------------+

This option is valid only if the protocol is [`udp`] or [`tcp`]. Specify a comma-separated list of ports or port ranges (start-end inclusive), or leave the value empty for any.

[[`icmp_code`]][]

ICMP message code

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#network-acl-rule-properties:icmp_code)]

+-----------------------------------+------------------------------------------------------+
| **Key:**                          | [`icmp_code`] |
+-----------------------------------+------------------------------------------------------+
| **Type:**                         | []                                         |
|                                   |                                                      |
|                                   | string                                               |
+-----------------------------------+------------------------------------------------------+
| **Required:**                     | []                                         |
|                                   |                                                      |
|                                   | no                                                   |
+-----------------------------------+------------------------------------------------------+

This option is valid only if the protocol is [`icmp4`] or [`icmp6`]. Specify the ICMP code number, or leave the value empty for any.

[[`icmp_type`]][]

Type of ICMP message

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#network-acl-rule-properties:icmp_type)]

+-----------------------------------+------------------------------------------------------+
| **Key:**                          | [`icmp_type`] |
+-----------------------------------+------------------------------------------------------+
| **Type:**                         | []                                         |
|                                   |                                                      |
|                                   | string                                               |
+-----------------------------------+------------------------------------------------------+
| **Required:**                     | []                                         |
|                                   |                                                      |
|                                   | no                                                   |
+-----------------------------------+------------------------------------------------------+

This option is valid only if the protocol is [`icmp4`] or [`icmp6`]. Specify the ICMP type number, or leave the value empty for any.

[[`protocol`]][]

Protocol to match

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#network-acl-rule-properties:protocol)]

+-----------------------------------+-----------------------------------------------------+
| **Key:**                          | [`protocol`] |
+-----------------------------------+-----------------------------------------------------+
| **Type:**                         | []                                        |
|                                   |                                                     |
|                                   | string                                              |
+-----------------------------------+-----------------------------------------------------+
| **Required:**                     | []                                        |
|                                   |                                                     |
|                                   | no                                                  |
+-----------------------------------+-----------------------------------------------------+

Possible values are [`icmp4`], [`icmp6`], [`tcp`], and [`udp`]. Leave the value empty to match any protocol.

[[`source`]][]

Comma-separated list of sources

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#network-acl-rule-properties:source)]

+-----------------------------------+---------------------------------------------------+
| **Key:**                          | [`source`] |
+-----------------------------------+---------------------------------------------------+
| **Type:**                         | []                                      |
|                                   |                                                   |
|                                   | string                                            |
+-----------------------------------+---------------------------------------------------+
| **Required:**                     | []                                      |
|                                   |                                                   |
|                                   | no                                                |
+-----------------------------------+---------------------------------------------------+

Sources can be specified as CIDR or IP ranges, source subject name selectors (for ingress rules), or be left empty for any.

[[`source_port`]][]

Source ports or port ranges

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#network-acl-rule-properties:source_port)]

+-----------------------------------+--------------------------------------------------------+
| **Key:**                          | [`source_port`] |
+-----------------------------------+--------------------------------------------------------+
| **Type:**                         | []                                           |
|                                   |                                                        |
|                                   | string                                                 |
+-----------------------------------+--------------------------------------------------------+
| **Required:**                     | []                                           |
|                                   |                                                        |
|                                   | no                                                     |
+-----------------------------------+--------------------------------------------------------+

This option is valid only if the protocol is [`udp`] or [`tcp`]. Specify a comma-separated list of ports or port ranges (start-end inclusive), or leave the value empty for any.

[[`state`]][]

State of the rule

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#network-acl-rule-properties:state)]

+-----------------------------------+----------------------------------------------------+
| **Key:**                          | [`state`]   |
+-----------------------------------+----------------------------------------------------+
| **Type:**                         | []                                       |
|                                   |                                                    |
|                                   | string                                             |
+-----------------------------------+----------------------------------------------------+
| **Default:**                      | []                                       |
|                                   |                                                    |
|                                   | [`enabled`] |
+-----------------------------------+----------------------------------------------------+
| **Required:**                     | []                                       |
|                                   |                                                    |
|                                   | yes                                                |
+-----------------------------------+----------------------------------------------------+

Possible values are [`enabled`], [`disabled`], and [`logged`].

[]

### Use selectors in rules[¶](#use-selectors-in-rules "Link to this heading")

Note

This feature is supported only for the [[OVN NIC type]](../../reference/devices_nic/#nic-ovn) and the [[OVN network]](../../reference/network_ovn/#network-ovn).

In ACL rules, the [`source`] and [`destination`] properties support using selectors instead of CIDR blocks or IP ranges. You can only use selectors in the [`source`] of [`ingress`] rules, and in the [`destination`] of [`egress`] rules.

Using selectors allows you to define rules for groups of instances instead of managing lists of IP addresses or subnets manually.

There are two types of selectors:

-   subject name selectors (ACL groups)

-   network subject selectors

[]

#### Subject name selectors (ACL groups)[¶](#subject-name-selectors-acl-groups "Link to this heading")

When an ACL is assigned to multiple instance NICs, either directly or through their networks, those NICs form a logical port group. You can use the name of that ACL as a *subject name selector* to refer to that group in the egress and ingress lists of other ACLs.

For example, if you have an ACL with the name [`my-acl`], you can specify the group of instance NICs that are assigned this ACL as an egress or ingress rule's source by setting [`source`] to [`my-acl`].

[]

#### Network subject selectors[¶](#network-subject-selectors "Link to this heading")

Use *network subject selectors* to define rules based on the network that the traffic is coming from or going to.

All network subject selectors begin with the [`@`] symbol. There are two special network subject selectors called [`@internal`] and [`@external`]. They represent the network's local and external traffic, respectively.

Here's an example ACL rule (in YAML) that allows all internal traffic with the specified destination port:

    ingress:
      - action: allow
        description: Allow HTTP/HTTPS from internal
        protocol: tcp
        source: "@internal"
        destination_port: "80,443"
        state: enabled

If your network supports [[network peers]](../network_ovn_peers/), you can reference traffic to or from the peer connection by using a network subject selector in the format [`@<network-name>/<peer-name>`]. Example:

    source: "@my-network/my-peer"

When using a network subject selector, the network that has the ACL assigned to it must have the specified peer connection.

[]

### Log traffic[¶](#log-traffic "Link to this heading")

ACL rules are primarily used to control network traffic between instances and networks. However, they can also be used to log specific types of traffic, which is useful for monitoring or testing rules before enabling them.

To configure a rule so that it only logs traffic, configure its [`state`] to [`logged`] when you [[add the rule]](#network-acls-rules) or [[edit the ACL]](#network-acls-edit).

#### View logs[¶](#view-logs "Link to this heading")

CLI

API

UI

To display the logs for all [`logged`] rules in an ACL, run:

    lxc network acl show-log <ACL-name>

To display the logs for all [`logged`] rules in an ACL, query the [[`GET`]` `[`/1.0/network-acls//log`]](/lxd/latest/api/#/network-acls/network_acl_log_get) endpoint:

    lxc query --request GET /1.0/network-acls//log

Example

    lxc query --request GET /1.0/network-acls/my-acl/log

Download a [`.log`] file of your ACL's logs from its [[detail page]](#network-acls-show) by clicking the [Download logs] button in the upper-right corner.

Note

If your attempt to view logs returns no data, that means either:

-   No [`logged`] rules have matched any traffic yet.

-   The ACL does not contain any rules with a [`state`] of [`logged`].

When displaying logs for an ACL, LXD intentionally displays all existing logs for that ACL, including logs from formerly [`logged`] rules that are no longer set to log traffic. Thus, if you see logs from an ACL rule, that does not necessarily mean that its [`state`] is *currently* set to [`logged`].

[]

## Edit an ACL[¶](#edit-an-acl "Link to this heading")

[]

### Rename an ACL[¶](#rename-an-acl "Link to this heading")

Requirements:

-   You can only rename an ACL that is not currently [[assigned to a NIC or network]](#network-acls-assign).

-   The new name must meet the [[Name requirements]](#network-acls-name-requirements).

CLI

API

UI

To rename an ACL, run:

    lxc network acl rename <old-ACL-name> <new-ACL-name>

To rename an ACL, query the [[`POST`]` `[`/1.0/network-acls/`]](/lxd/latest/api/#/network-acls/network_acl_post) endpoint:

    lxc query --request POST /1.0/network-acls/ --data ''

Example

Rename an ACL named [`web-traffic`] to [`internal-web-traffic`]:

    lxc query --request POST /1.0/network-acls/web-traffic --data ''

To rename an ACL, go to its [[detail page]](#network-acls-show) and select its name in the header.

[]

### Edit other properties[¶](#edit-other-properties "Link to this heading")

CLI

API

UI

Run:

    lxc network acl edit <ACL-name>

This command opens the ACL configuration in YAML format for editing. You can edit any part of the configuration *except* for the ACL name, including the custom user keys.

You can update any ACL property except for [`name`], including the custom user keys, by querying the [[`PUT`]` `[`/1.0/network-acls/`]](/lxd/latest/api/#/network-acls/network_acl_put) endpoint:

    lxc query --request PUT /1.0/network-acls/ --data ',
      "description": "<description of the ACL>",
      "egress": [<egress rule>, <another egress rule...>,...],
      "ingress": [<ingress rule>, <another ingress rule...>,...]
    }'

Caution

Any properties you omit from this request (aside from the ACL [`name`]) will be reset to defaults. See: [[The PUT method]](../../rest-api/#rest-api-put).

If you *only* want to update the [`config`] custom user keys, see: [[Edit a custom user key via PATCH API]](#network-acls-edit-custom-api).

Example

Consider an ACL named [`my-acl`] with the following properties (shown in JSON):

    ,
      "description": "My test ACL",
      "egress": [
        
      ]
      "ingress": [
        
      ]
    }

This query updates that ACL's [`egress`] rule [`state`] from [`logged`] to [`enabled`]:

    lxc query --request PUT /1.0/network-acls/my-acl --data '
      ]
    }'

After the above query is run, [`my-acl`] contains the following properties:

    ,
      "description": "",
      "egress": [
        
      ],
      "ingress": []
    }

Note that the [`description`] and [`ingress`] properties have been reset to defaults because they were not provided in the API request.

To avoid this behavior and preserve the values of any existing properties, you must include them in the [`PUT`] request along with the updated property:

    lxc query --request PUT /1.0/network-acls/my-acl --data '
      ],
      "ingress": [
        
      ]
    }'

To edit an ACL, navigate to its [[detail page]](#network-acls-show). From here, you can add or remove ingress or egress rules, as well as configure other settings.

[]

### Edit a custom user key via PATCH API[¶](#edit-a-custom-user-key-via-patch-api "Link to this heading")

There's one more way to add or update a custom [`config.user.*`] key when using the API. Instead of the PUT method shown in the [[Edit other properties]](#network-acls-edit-properties) section above, you can query the [[`PATCH`]` `[`/1.0/network-acls/`]](/lxd/latest/api/#/network-acls/network_acl_patch) endpoint:

    lxc query --request PATCH /1.0/network-acls/ --data '
    }'

Caution

Any ACL properties you omit from this request (aside from [`config`] and [`name`]) will be reset to defaults.

This [`PATCH`] endpoint allows you to add or update custom [`config.user.*`] keys without affecting other existing [`config.user.*`] entries. However, this [[partial update behavior]](../../rest-api/#rest-api-patch) applies *only* to the [`config`] property. For the [`description`], [`egress`], and [`ingress`] properties, this request behaves like a [[PUT request]](../../rest-api/#rest-api-put): it replaces any provided values and resets any omitted properties to their defaults. Thus, ensure you include any properties you want to keep.

#### Example[¶](#id5 "Link to this heading")

Consider an ACL named [`my-acl`] with the following properties (shown in JSON):

    ,
    }

The following query adds a [`config.user.my-key2`] key with the value of [`2`]:

    lxc query --request PATCH /1.0/network-acls/my-acl --data '
    }'

After sending the above request, [`my-acl`]'s properties are updated to:

    
    }

Note that the request *inserted* the new [`user.my-key2`] key without affecting the pre-existing [`user.my-key1`] key. Also notice that the [`description`] property was not sent in the request, and thus was reset to an empty value.

[]

## Delete an ACL[¶](#delete-an-acl "Link to this heading")

You can only delete an ACL that is not [[assigned to a NIC or network]](#network-acls-assign).

CLI

API

UI

To delete an ACL, run:

    lxc network acl delete <ACL-name>

To delete an ACL, query the [[`DELETE`]` `[`/1.0/network-acls/`]](/lxd/latest/api/#/network-acls/network_acl_delete) endpoint:

    lxc query --request DELETE /1.0/network-acls/

To delete an ACL, ensure that it is not assigned to an NIC or network. You can then delete it from its [[detail page]](#network-acls-show).

[]

## Assign an ACL[¶](#assign-an-acl "Link to this heading")

An ACL is inactive until it is assigned to one of the following targets:

-   a [[OVN network]](../../reference/network_ovn/#network-ovn)

-   a [[Bridge network]](../../reference/network_bridge/#network-bridge)

-   an [[OVN NIC type of an instance]](../../reference/devices_nic/#nic-ovn)

To assign an ACL, you must update the [`security.acls`] option within its target's configuration.

Assigning one or more ACLs to a NIC or network adds a default rule that rejects all unmatched traffic. See [[Configure default actions]](#network-acls-defaults) for details.

### Assign an ACL to a bridge or OVN network[¶](#assign-an-acl-to-a-bridge-or-ovn-network "Link to this heading")

CLI

API

UI

To set the network's [`security.acls`], run the following command. Set the value to a string that contains the ACL name or names you want to add, and comma-separate multiple names:

Set the network's [`security.acls`] to a string that contains the ACL name or names you want to add. Comma-separate multiple names:

    lxc network set <network-name> security.acls="<ACL-name>[,<ACL-name>,...]"

For more information about using [`lxc`]` `[`network`]` `[`set`], see: [[How to configure a network]](../network_configure/#network-configure).

Example

Set the [`my-network`] network's [`security.acls`] to contain three ACLs:

    lxc network set my-network security.acls="my-acl1,my-acl2,my-acl3"

To set the network's [`security.acls`], query the [[`PATCH`]` `[`/1.0/networks/`]](/lxd/latest/api/#/networks/network_patch) endpoint. Set the value to a string that contains the ACL name or names you want to add, and comma-separate multiple names:

    lxc query --request PATCH /1.0/networks/ --data '
    }'

Example

Set the [`my-network`] network's [`security.acls`] to contain three ACLs:

    lxc query --request PATCH /1.0/networks/my-network --data '
    }'

You can assign an ACL to a bridge or OVN network when [[creating]](../network_create/#network-create) or [[editing]](../network_configure/#network-configure) the network. In either case, select your pre-configured ACL from the [ACLs] dropdown.

<figure class="align-default">
<a href="../../_images/network_create.png" class="reference internal image-reference"><img src="../../_images/network_create.png" style="width: 80%;" alt="Create a network in LXD" /></a>
</figure>

### Assign an ACL to the OVN NIC of an instance[¶](#assign-an-acl-to-the-ovn-nic-of-an-instance "Link to this heading")

For NICs, ACLs can only be used with the [[OVN NIC type]](../../reference/devices_nic/#nic-ovn).

An NIC is considered a type of instance [[device]](../../reference/devices/#devices). For general information about configuring instance devices, see: [[Configure devices]](../instances_configure/#instances-configure-devices).

CLI

API

To assign an ACL to an instance's OVN NIC, run:

    lxc config device set <instance-name> <NIC-name> security.acls="<ACL-name>[,ACL-name,...]"

Example

Assign three ACLs to an instance's OVN NIC:

    lxc config device set my-instance my-ovn-nic security.acls="my-acl1,my-acl2,my-acl3"

To assign an ACL to an instance's OVN NIC, query the [[`PATCH`]` `[`/1.0/instances/`]](/lxd/latest/api/#/instances/instance_patch) endpoint. Set [`security.acls`] to a string that contains the ACL name or names you want to add, and comma-separate multiple names:

    lxc query --request PATCH /1.0/instances/ --data '
      }
    }'

The [`type`] and [`network`] options are required in the body (see: [[Required device options]](../instances_configure/#instances-configure-devices-api-required)).

Caution

Patching an instance device's configuration unsets any options for that device omitted from the PATCH request body. For more information, see [[Effects of patching device options]](../instances_configure/#instances-configure-devices-api-patch-effects).

Example

For [`my-instance`], set its [`my-ovn-nic`] device's [`security.acls`] to contain three ACLs:

    lxc query --request PATCH /1.0/instances/my-instance --data '
      }
    }'

[]

### Additional options[¶](#additional-options "Link to this heading")

To view additional options for the [`security.acls`] lists, refer to the configuration options for the target network or NIC:

-   Bridget network's [[`security.acls`]](../../reference/network_bridge/#network-bridge-network-conf:security.acls)

-   OVN network's [[`security.acls`]](../../reference/network_ovn/#network-ovn-network-conf:security.acls)

-   Instance's OVN NIC [[`security.acls`]](../../reference/devices_nic/#device-nic-ovn-device-conf:security.acls)

[]

## Configure default actions[¶](#configure-default-actions "Link to this heading")

When one or more ACLs are assigned to a NIC---either directly or through its network---a default reject rule is added to the NIC. This rule rejects all traffic that doesn't match any of the rules in the assigned ACLs.

You can change this behavior with the network- and NIC-level [`security.acls.default.ingress.action`] and [`security.acls.default.egress.action`] settings. The NIC-level settings override the network-level settings.

CLI

API

Configure a default action for a network

To set the default action for a network's egress or ingress traffic, run:

    lxc network set <network-name> security.acls.default.<egress|ingress>.action=<allow|reject|drop>

Example

To set the default action for inbound traffic to [`allow`] for all instances on the [`my-network`] network, run:

    lxc network set my-network security.acls.default.ingress.action=allow

Configure a default action for an instance OVN NIC device

To set the default action for an instance OVN NIC's egress or ingress traffic, run:

    lxc config device set <instance-name> <NIC-name> security.acls.default.<egress|ingress>.action=<allow|reject|drop>

Example

To set the default action for inbound traffic to [`allow`] for the [`my-ovn-nic`] device of [`my-instance`], run:

    lxc config device set my-instance my-ovn-nic security.acls.default.ingress.action=allow

Configure a default action for a network

To set the default action for a network's egress or ingress traffic, query the [[`PATCH`]` `[`/1.0/networks/`]](/lxd/latest/api/#/networks/network_patch) endpoint:

    lxc query --request PATCH /1.0/networks/ --data '
    }'

Example

Set the [`my-network`] network's default egress action to [`allow`]:

    lxc query --request PATCH /1.0/networks/my-network --data '
    }'

Configure a default action for an instance's OVN NIC device

To set the default action for an instance's OVN NIC's traffic, query the [[`PATCH`]` `[`/1.0/instances/`]](/lxd/latest/api/#/instances/instance_patch) endpoint:

    lxc query --request PATCH /1.0/instances/ --data '
      }
    }'

The [`type`] and [`network`] options are required in the body (see: [[Required device options]](../instances_configure/#instances-configure-devices-api-required)).

Caution

Patching an instance device's configuration unsets any options for that device omitted from the PATCH request body. For more information, see [[Effects of patching device options]](../instances_configure/#instances-configure-devices-api-patch-effects).

Example

This request sets the default action for inbound traffic to [`allow`] for the [`my-ovn-nic`] device of [`my-instance`]:

    lxc query --request PATCH /1.0/instances/my-instance --data '
      }
    }'

[]

## Bridge limitations[¶](#bridge-limitations "Link to this heading")

When using network ACLs with a bridge network, be aware of the following limitations:

-   Unlike OVN ACLs, bridge ACLs apply only at the boundary between the bridge and the LXD host. This means they can enforce network policies only for traffic entering or leaving the host. Intra-bridge firewalls (rules controlling traffic between instances on the same bridge) are not supported.

-   [[ACL groups and network selectors]](#network-acls-selectors) are not supported.

-   If you're using the [`iptables`] firewall driver, you cannot use IP range subjects (such as [`192.0.2.1-192.0.2.10`]).

-   Baseline network service rules are added before ACL rules in their respective INPUT/OUTPUT chains. Because we cannot differentiate between INPUT/OUTPUT and FORWARD traffic after jumping into the ACL chain, ACL rules cannot block these baseline rules.