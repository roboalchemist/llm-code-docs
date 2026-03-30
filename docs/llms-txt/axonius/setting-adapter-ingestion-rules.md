# Source: https://docs.axonius.com/docs/setting-adapter-ingestion-rules.md

# Setting Adapter Ingestion Rules

Use **Ingestion Rules** to decide which entities to ingest from the data fetched from adapters. You can configure Ingestion Rules for all connections for an adapter, configure different Ingestion Rules for each adapter connection, or only configure Ingestion Rules for a specific adapter connection. Ingestion Rules support all Axonius asset types.

## Required Permissions

In order to use this feature, you require the following permissions:

* **View ingestion rules**
* **Update ingestion rules**

## Ingestion Rules Structure

* Ingestion rules work using Boolean operator conditions.

* Ingestion rules support multiple statements. These are either handled using **OR** or **AND** as follows:

  * Choose **OR** to ingest an entity once one of the rules applies (this is the default).
  * Choose **AND** to ingest an entity only if all of the rules apply.

<Image align="center" alt="Ingestiondiagram" border={false} width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Ingestiondiagram.png" />

## Using Ingestion Rules

1. Click the Adapters icon on the left navigation panel to open the **Adapters** page.

2. Search for and select the relevant adapter. The **Adapter Profile** page opens displaying the list of connected connections.

3. Under **Advanced Settings**,  choose **Ingestion Rules Configuration**. The **Ingestion Rules Configuration** page is displayed.

   <Image alt="IngestionPaneNEw" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/IngestionPaneNEw.png" />

4. Toggle on **Enable ingestion rules to configure which data to ingest from the adapter into the system**.

   <Image alt="IngestionRules1" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/IngestionRules1.png" />

5. If you want to add more than one rule, from the **Select logical operator for all rules** drop-down, select the operator to apply between the rules: **OR** (the default) or  **AND**.

6. Enter one Ingestion Rule statement in the **Custom ingestion statement** input box. Click the `+` button to add another Ingestion Rule statement. Learn [how to create an Ingestion Rule statement](#creating-an-ingestion-rule-statement).

7. Once you have entered all the rules you need, click **Save** to save your settings. An entity is ingested according to the Boolean logic of the operator that you set.

## Configuring Ingestion Rules for each Adapter Connection

**To configure Ingestion Rules separately for each adapter connection**

1. On the Ingestion rules Configuration page, toggle on **Enable ingestion rules settings for each connection separately**.

<Image alt="ingestioneach connection" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ingestioneach%20connection.png" />

2. Click **Save**.  The **Ingestion Rules  Configuration** tab now also appears on the **Add Connection** drawer.
3. Click **Add Connection**. The **Connection Configuration** drawer now has an additional tab (**Ingestion Rules Configuration**).

<Image alt="newTabingest" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/newTabingest.png" />

4. Select the Ingestion Rules Configuration tab and toggle on **Enable ingestion rules to configure which data to ingest from the adapter into the system**.  The Ingestion Rules configuration pane opens.

   <Image alt="IngestToggleOn" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/IngestToggleOn.png" />

5. Configure the Ingestion rules that you want for this specific  connection,  and then select **Save** or **Save and Fetch**.

## Creating an Ingestion Rule Statement

To use Ingestion Rules, you need to create at least one **Custom ingestion statement** that describes the data to ingest. Each statement is made up of a primary statement and an optional post action.

### Primary Statement

An entity is considered for ingestion if the pre-ingestion statement is true. A pre-ingestion statement can be built in one of two ways (use the relevant asset name in the first parenthesis):

* *`{asset type}.{flattened key path of the entity}{operator}{rule values}`*
* *`{asset type}{operator}{rule values}`*

#### Complex Primary Statements

Primary statements support complex conditions by combining multiple sub-rules using AND, OR, and parentheses. This enables creating detailed asset ingestion criteria. For example: ((Value `>`  50 AND Confidence = HIGH) OR (Value `>` 90 AND Confidence = LOW))

* Each sub-rule within a primary statement is evaluated independently for an asset.

  * OR: If any sub-rule is TRUE, the statement is TRUE. Evaluation stops when a TRUE sub-rule is found.
  * AND: All sub-rules must be TRUE for the statement to be TRUE.
* If multiple primary statements exist, each is evaluated independently.

  * OR: If any primary statement is TRUE, the asset is ingested. Evaluation stops when a TRUE primary statement is found.
  * AND: All primary statements must be TRUE for the asset to be ingested.

**Examples**

```TEXT
{entity}.{key} {operator} {value} or/and {entity} {operator} {value}
```

<br />

<Callout icon="📘" theme="info">
  Note:

  The above complex statement is equivalent to creating the following two simple primary statements with an OR or AND operator:

  `{entity}.{key} {operator} {value}`

  OR/AND

  `﻿{entity} {operator} {value}`
</Callout>

```TEXT
({entity}.{key} {operator} {value} or/and {entity} {operator} {value}) and/or {entity}.{key} {operator} {value}
```

```TEXT
({entity}.{key} {operator} {value} or/and {entity} {operator} {value}) and/or ({entity}.{key} {operator} {value} or/and {entity} {operator} {value})
```

### Post Action

Post actions are optional actions performed on the entity before it is ingested into Axonius. Common use cases for post statements are to filter out poor data or to drop PII.

The syntax is as follows:

*`{primary statement}` then `{action} {post rule values}`*

## Ingestion Rule Components

### Entities

Defines which entity (asset type) this rule will be applied on (device, user, ticket, certificate, etc.).

### Flattened Key Path

The flattened key path of the entity is the name of the key path as presented in the Axonius database. The following example can explain how to obtain this value. “I want to only ingest device from the cmdb\_ci\_server table in ServiceNow”. You can translate this to a Query Wizard statement.

<Image alt="IngestionFlattenedEg" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/IngestionFlattenedEg.png" />

This statement is automatically translated into an Axonius statement in the **Devices** search bar.

```TEXT
("adapters_data.service_now_adapter.class_name" == "cmdb_ci_server")
```

Because Ingestion rules are already being performed at an adapter level, you can ignore adapters\_data.service\_now\_adapter.

That leaves the flattened key path to simply be `class_name`

<Image align="center" alt="IngestionPathMain" border={false} width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/IngestionPathMain.png" />

When working with complex objects such as network interface IP addresses, you need to copy the complete complex object, for instance `network_interfaces.ips `.

<Image align="center" alt="IngestionMore" border={false} width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/IngestionMore.png" />

### Operators Supported

The following operators are supported:

#### **Equal / Not Equal (== | !=)**

Checks whether the value from the entity is equal or not equal to the rule values.

<Callout icon="📘" theme="info">
  Note:

  The condition asset.key != "value" only returns assets where the field key exists and is not equal to "value". To also include assets where key is missing or empty, use: (asset.key != 'value' or asset key\_not\_exists \["key"]). See below an explanation of key\_not\_exists.
</Callout>

```TEXT
device.class_name == "cmdb_ci_computer"
```

```TEXT
(device.class_name != "cmdb_ci_computer" or device key_not_exists ["class_name"])
```

```
(device key_not_exists ["vlan"] or device.vlan != "888") and (device key_not_exists ["ssid"] or device.ssid != "ALLETEGUEST")
```

Do not use equals with lists, as they will be converted to strings.

```TEXT
 'device.ad_dc_source != ["10.10.11.0/24"]` (checks if value is equal to str(list))
```

#### **Dates** **Less Than / Greater Than (`<` | `>`)**

Checks whether the value from the entity is less than or greater than the date specified in the rule value.

**Supported Syntax**

* **date**(YYYY-MM-DD)
* **date**(**now-nd**)
* **date**(**now+nd**)

Where **n** is the number of days (**d**).

**Examples**

```TEXT
user.termination_date > date(2024-10-31)
```

Ingest users whose termination date is after October 31st 2024.

```TEXT
user.last_logon > date(now-10d)
```

Ingest all users with last\_logon later than 10 days ago (i.e., within the last 10 days).

```TEXT
user.terminated_date > date(now+365d)then skip_field ["terminated_date"]
```

Ingest all users with terminated\_date later than 365 days in the future (i.e., in more than one year), but skip the ingestion of the terminated\_date field itself.

<Callout icon="📘" theme="info">
  Note:

  Dates currently do not support greater than or equal to `>=` OR less than or equal to `<=` operators.
</Callout>

#### **Numbers**

Checks whether the value from the entity is greater than or less than the value provided.

```TEXT
device.confidence_level < 65 then skip_field ["os.type", "os.distribution", "os.type_distribution", "os.os_str"]
```

If the confidence level for devices is below 65, then do not ingest OS level information.

<Callout icon="📘" theme="info">
  Note:

  This rule excludes all devices with a confidence level `>=`65. Using the following rule in conjunction with the OR operator ensures that all devices are still ingested from that adapter.

  `device key_exists ["id"]`
</Callout>

```TEXT
device.policies_compliance_count >= 1
```

Ingests all devices with at least one compliance policy present.

#### **Value In / Value Not In (in | not\_in)**

Checks whether the value from the entity is in or not in the list of rule values

```TEXT
device.ad_name in ["EC2AMAZ-71GIQSBBB", "EC2AMAZ-71GIQSORRRR"]
```

```TEXT
device.ad_name not_in ["EC2AMAZ-71GIQSBBB", "EC2AMAZ-71GIQSORRRR", "EC2AMAZ-71GIQSO"]
```

#### **IP Address In or Not In (in\_net | not\_in\_net)**

Checks whether the IP address / network value from the entity is in or not in the rule\_values IP network. This means that you can check if an IP/Subnet is in a CIDR. This is applicable both for IPv4 and for IPv6.

**Examples**

```TEXT
device.network_interfaces.ips in_net ["10.10.11.0/24"]
```

```TEXT
device.network_interfaces.ips not_in_net ["192.168.11.0/24"]
```

#### **Starts or Does not Start with (starts\_with | not\_starts\_with)**

Checks whether the value from the entity starts with or does not start with a required pattern that was entered.

**Examples**

```TEXT
device.ad_usn_changed starts_with ["91"]
```

```TEXT
device.ad_name not_starts_with ["EC2", "S3"]
```

#### **Ends or Does not End With (ends\_with | not\_ends\_with)**

Checks whether the value from the entity ends with or does not end with a required pattern that was entered.

**Examples**

```TEXT
user.mail ends_with ["@gmail.com", "@yahoo.com"]
```

```TEXT
user.username not_ends_with ["_test"]
```

#### **Key Exists or Does Not Exist (key\_exists | key\_not\_exists)**

Checks whether **all supplied** key values exist or not.

```TEXT
device key_exists ["network_interfaces.ip", "ad_name"]
```

```TEXT
user key_not_exists ["database"]
```

#### **Field Equal / Not Equal (field\_equal |field\_not\_equal)**

Checks whether the value of one field in an entity is equal or not equal to the value of another field in that entity.

**Examples**

```TEXT
device.hostname field_not_equal ["ad_name"]
```

Only ingest devices where the hostname field is not equal to the value in the ad\_name field.

#### Field Starts With (field\_starts\_with)

Checks whether the value of one field in an entity starts with the value of another field in that entity.

**Examples**

```TEXT
device.ad_sAMAccountName field_starts_with ["ad_name"]
```

Ingest the device only if its sAMAccountName name begins with the ad\_name.

#### Field Not Starts With ( field\_not\_starts\_with)

Checks whether the value of one field in an entity does not start with the value of another field in that entity.

**Examples**

```TEXT
device.hostname field_not_starts_with ["name"] then skip_field ["hostname", "fqdn"]
```

The device will only be ingested if its hostname does not start with its asset name. Those devices ingested will also have their hostname and FQDN fields dropped. Consider adding `device key_exists` \["id"] to this rule (OR'd together) if you would still like to ingest devices where their hostname begins with their asset name.

#### Contains (contains) and Not Contains (not\_contains)

Checks whether the value from the entity does or does not contain any of the rule values. This is case insensitive.

**Examples**

```TEXT
device.ad_sAMAccountName contains ["axonius"]
device.ad_sAMAccountName not_contains ["check1", "check2"]
```

#### Matches or Does Not Match Regex Value (match\_regex|not\_match\_regex)

Checks whether the provided regex string pattern matches or does not match the device field value.

**Examples**

```TEXT
device.name match_regex ["WIN.+test"]
```

### Post Actions

Post actions can perform additional operations on the entity (asset) before it is ingested. A post action is not required for an Ingestion Rule statement.
The following post action operators are available.

#### **Skip Field (skip\_field)**

Removes the supplied fields from the entity and does not insert them into the database.

**Examples**

```TEXT
device.ad_dc_source == "10.10.11.5" then skip_field ["network_interfaces.ips", "ad_name"]
```

<Callout icon="📘" theme="info">
  Note:

  This rule excludes all devices with an ad\_dc\_source not equal to 10.10.11.5. Therefore, if you want to include ALL entities (assets), but only skip fields on a subset of entities, include the following rule (in conjunction with the OR operator) to ensure that all entities are still ingested from that adapter.

  `device key_exists ["id"]`
</Callout>

```TEXT
 device.ad_usn_changed starts_with ["91"] then skip_field ["ad_dc_source"]
```

If you want to skip a field(s) on all devices coming from an adapter, change the ingestion rule to the following:

```TEXT
device key_exists ["id"] then skip_field ["physical_location", "qualys_agnet_ports"]
```

* `device key_exists ["id"]` ensures that all devices are ingested from that adapter.

* then `skip_field ["physical_location", "qualys_agnet_ports"]` allows you to specify the field(s) to not ingest on those devices.

#### **Remove Values (remove\_values)**

Removes values from a list field or from a field in a list object. Note that if you already fetched these values, they still appear in the asset table for the amount of time set in [**Delete devices (or users) and other assets that have not been returned from the source in the last X hours**](/docs/advanced-settings#adapter-configuration). To only see the latest values, from the Query Wizard create a query that shows “from last fetch” = true. Use **remove\_values** on fields that contain a list of simple objects such as strings (**Last Used Users from WMI** as seen above) or numbers, or on fields that contain a list of complex objects.

<Image alt="IngestionremoveValue" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/IngestionremoveValue.png" />

**Example 1 - Removes values from a list field**

```TEXT
device key_exists ["last_used_users"] then remove_values last_used_users starts_with ["Admin"]

```

This rule will ingest all devices with a last used user, but will only include last used users that do not start with "Admin"

**Example 2 - Removes values from a field in a list object**

```TEXT
device key_exists ["id"] then remove_values network_interfaces.mac == "00:00:4f:21:53:af"

```

This rule will ingest all devices with an ID, but will remove the MAC address from each device that has a network interface with MAC equal to 00:00:4f:21:53:af.

#### **Remove Items (remove\_items)**

Removes items from a list field. Some fields contain lists of items, for example **network\_interfaces**, which contains subfields such as MAC addresses, IP addresses, etc. If a condition is applied to one of the subfields, then when it is true, the complete item is removed and is not ingested. **remove\_items** should be used for lists of complex objects, such as Network Interfaces.

<Image alt="egNetworkIn" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/egNetworkIn.png" />

**Example**

```TEXT
device key_exists ["id"] then remove_items network_interfaces.ip4 in_net ["10.20.0.0/24"]
```

This rule will ingest all devices, but will remove all associated network interface information for IPs between 10.10.10.0 - 10.10.10.255

#### **Trim Prefix/Suffix** (trim\_suffix / trim\_prefix)

Removes a certain prefix or suffix from the field if it exists.

**Examples**

```TEXT
device key_exists ["id"] then trim_prefix hostname ["domain.local"]
```

```TEXT
device key_exists ["id"] then trim_prefix network_interfaces.ips ["(IP Address)", "IP Prefix"]
```

```TEXT
user key_exists ["id"] then trim_suffix hostname [".com"]
```

<Callout icon="📘" theme="info">
  Note:

  If you want to run a post action on only a subset of entities and still ingest all other entities, you will need to include the following rule:

  `device|user key_exists ["id"]`
</Callout>

This is useful for scenarios when you would like to remove employee IDs from an MSSP that collides with your primary email.

The Ingestion Rules would look like the following (joined with 'OR')

```TEXT
user.email ends_with ["@mssp.com"] then skip_field ["employee_id"]

user key_exists ["id"]
```

#### **Trim Regex** (trim\_regex)

The *trim\_regex* action removes a specific string or pattern from a field using a regular expression (regex) template.

**Syntax**

```
trim_regex [field] [regex_template] 
```

Where:

* \[field] - The target field from which to remove the string.

* \[regex\_template] - The regex pattern that identifies the string to be removed.

**Example**
This example uses trim\_regex to remove a MAC address from the **ad\_hostname** field.

Original ‘ad\_hostname value': 'EC2AMAZ-71GIQSO-A4:B7:3C:E9:2F:81’

```TEXT
device key_exists ["id"] then trim_regex ad_hostname ["-([A-Fa-f0-9]{2}(:[A-Fa-f0-9]{2}){5})"]
```

Explanation of the regex template "-(\[A-Fa-f0-9]`{2}`(:\[A-Fa-f0-9]`{2}`){5})" :

* \-: This matches the hyphen (-) that precedes the MAC address.
* (\[A-Fa-f0-9]`{2}`): This matches two hexadecimal digits (0-9, a-f, A-F). The parentheses create a capture group.
* (:\[A-Fa-f0-9]`{2}`){5}: This matches a colon (:) followed by two hexadecimal digits, repeating this pattern exactly five times.

Result:

The action removes the hyphen and the MAC address, leaving ad\_hostname as 'EC2AMAZ-71GIQSO'.

<Callout icon="📘" theme="info">
  Note:

  If you want to run a post action on only a subset of entities and still ingest all other entities, you will need to include the following rule:

  `device|user key_exists ["id"]`
</Callout>

This is useful for scenarios when you would like to remove employee IDs from an MSSP that collides with your primary email.

The Ingestion Rules would look like the following (joined with 'OR')

```TEXT
user.email ends_with ["@mssp.com"] then skip_field ["employee_id"]

user key_exists ["id"]
```

### Performing Post Action Only if Field Value Exists / Not Exists

Use **key\_exists** and **key\_not\_exists** operators in the post action of an ingestion rule so that the post action is performed on the asset, only if a value exists or does not exist in the specified field (key).

**Example**

```TEXT
device key_exists ["id"] then remove_items network_interfaces.ips_v4 key_not_exists
```

This rule ingests all devices, but removes all network interfaces without a value in ips\_v4, i.e., without an IPv4 address.

## Testing Ingestion Rules

From the **Add Connection** page, click **Save and Fetch** to test the Ingestion Rules.
The system then performs a fetch. Each entity brought from the adapter goes through the Ingestion Rule process.

<Callout icon="📘" theme="info">
  Note:

  Instead of initiating a fetch to test the Ingestion Rules, you can wait until the adapter fetches in accordance with your discovery cycle.
</Callout>

After the fetch is complete, open the relevant assets page in order to see your results. In the Query Wizard, specify your adapter and select “From Last Fetch - yes”

<Image alt="TestIngestoion" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/TestIngestoion.png" />

In the **Adapter Fetch History**, you can also see how many assets of each asset type were ignored before and after the Ingestion Rules were implemented.

<Image alt="IngestionAdapterFetch" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/IngestionAdapterFetch.png" />

If required, you can fine-tune the rules and rerun a fetch.

Entities not ingested will still appear in Axonius for the amount of time set in **Delete devices (or users) and other assets that have not been returned from the source in the last X hours**  setting.

## Ingestion Rules Examples

### A problematic MAC address is being added to my devices after using an ethernet connection.

Perhaps the same ethernet connection is used when imaging company workstations. This might cause the same MAC address to appear on multiple devices, resulting in unintended correlation issues.

```TEXT
device key_exists ["id"] then remove_items network_interfaces.mac == "00:00:5E:00:53:AF"
```

This will find any network interface records containing this MAC address and remove it from the device.

### Exclude device records that have neither open ports NOR hostname.

Whenever you want to “exclude” a device, you need to think about the other side of the coin. What type of devices do you want to “ingest”?

It would be equivalent to say the following, “I want to ingest devices that have an open port OR hostname”

```TEXT
device key_exists ["hostname"]
```

```TEXT
device key_exists ["open_ports"]
```

These rules can be used together with OR.

<Image alt="IngestionEG1" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/IngestionEG1.png" />

Why can’t we combine these statements into a single rule?

```TEXT
device key_exists ["hostname", "open_ports"]
```

That is because BOTH keys need to exist on the device when we insert both fields into the list. Again, key\_exists checks whether all supplied key values exist or not. If any key does not exist, then the device will not be ingested.

### Exclude data from an acquired company in your CMDB

Perhaps you acquire another company and begin putting their devices into your CMDB. However, perhaps you do not want to ingest those devices into Axonius. You could use the following ingestion rule:

```TEXT
device.company != "Child Company"
```

### Working with Boolean Values

<Image align="center" alt="IngestionEG2" border={false} width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/IngestionEG2.png" />

While **has\_agent** is a boolean field (True|False), the UI shows Yes|No. How do you only ingest devices with an agent?

While the field in the UI shows 'Yes' or 'No', you use the actual value 'True' or 'False' in the rule, as follows:

```TEXT
device.has_agent == "True"
```

### Exclude specific classes from the CMDB

Let’s filter the following classes from the ServiceNow fetch list: cmdb\_ci\_win\_server, cmdb\_ci\_linux\_server, cmdb\_ci\_unix\_server, etc.

Before building the rule, we can build a field segmentation to get a rough idea of the devices we want to exclude.

<Image align="center" alt="IngestionEG4" border={true} width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/IngestionEG4.png" className="border" />

8 Win Servers + 7 Unix Servers + 5 Linux Servers = 20 total devices to exclude

The ingestion rule should ignore 20 additional devices after implementation.

```TEXT
device.class_name not_in ["cmdb_ci_win_server", "cmdb_ci_linux_server", "cmdb_ci_unix_server"]
```

<Image align="center" alt="IngestionCMDB" border={true} width="300px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/IngestionCMDB.png" className="border" />

Success. Note the adapter was already ignoring 5 devices prior to the ingestion rule

### Filtering AWS Resources Coming from CrowdStrike

Maybe your security controls are installed on ephemeral EC2 instances in AWS that constantly get spun up and spun down. While we have filtered these devices from the AWS adapter, they are still appearing in Axonius from the other adapters that see them, such as CrowdStrike.

<Image align="center" alt="Ingestionnext" border={false} width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Ingestionnext.png" />

To start we might want to remove based on cloud\_provider.

```TEXT
device.cloud_provider != "AWS"
```

With this rule, we should expect 3 devices to be ignored.

<Image align="center" alt="IngestinEG6" border={true} width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/IngestinEG6.png" className="border" />

However, this rule excluded our non-AWS devices too. Because those devices don’t have a cloud\_provider field, the ingestion rule failed on those devices. So, we need another check to bring in devices that don’t have a cloud\_provider.

```TEXT
device key_not_exists ["cloud_provider"]
```

<Image align="center" alt="IngestionEG7" border={true} width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/IngestionEG7.png" className="border" />

These rules would be used together with OR

### Excluding Expired Certificates

Perhaps we are pulling in certificate data from a Certificate Lifecycle Management system such as Digicert, Sectigo, or Venafi, and we want to filter out expired certificates that are considered stale. In this scenario, we want to exclude all certs that expired more than 30 days ago.

```TEXT
device.certificate.cert_expiry_date > date(now - 30d)
```

This statement will look back 30 days and ingest all certificates that have expired in the last 30 days or have yet to expire.

### Skip physical location field for multiple OS-type devices

The organization has a prefix for each device hostname in its environment. This example presents a complex Ingestion Rule, which determines to ingest only those devices with:

* device.hostname starts\_with \["worg"] and device.os.type == "Windows"
* device.hostname starts\_with \["morg"] and device.os.type == "MacOS"

in ingested devices (matching either of those rules), skips the physical location field.

```TEXT
(device.hostname starts_with ["worg"] and device.os.type == "Windows") or (device.hostname starts_with ["morg"] and device.os.type == "MacOS") then skip_field ["physical_location"]
```

<Image align="center" alt="IngestionRuleComplexConfiguration" border={true} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/IngestionRuleComplexConfiguration.png" className="border" />

### Ingest specific servers

The following rule ingests servers according to the following customer use case:

* When a server's hostname starts with "SER\_" AND the OS is "windows" --> Do not ingest.
* If the server's hostname starts with "SER\_" and the OS is Linux or any other OS  --> Ingest.
* if the server's hostname does not start with SER\_ and the OS is any OS  --> Ingest.

```TEXT
(device.hostname not_starts_with "SER_" or device.os.type != "windows"))
```

According to this rule, devices with the following field values will or will not be ingested.

* Hostname = SER\_123 AND OS = windows --> NOT ingested
* Hostname = SER\_124 AND OS = Linux --> Ingested
* Hostname = Linux\_ser123 AND OS = windows --> Ingested