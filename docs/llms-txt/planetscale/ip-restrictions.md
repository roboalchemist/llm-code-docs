# Source: https://planetscale.com/docs/postgres/connecting/ip-restrictions.md

# IP restrictions

> Manage which IP addresses can establish connections to your database.

You can manage IP address restrictions for database connections in the "**IP restrictions**" tab under Settings for your database.
IP restrictions control which networks can connect to your database, providing an additional layer of security beyond authentication.

IP restrictions restrict database connections to the specified IP ranges.
Rules apply to all roles and schemas unless specified otherwise.

## Creating an IP restriction rule

You must be a database or organization administrator to create or modify an IP restriction rule.

<Steps>
  <Step>
    From the PlanetScale organization dashboard, select the desired database
  </Step>

  <Step>
    Navigate to **Settings** from the menu on the left
  </Step>

  <Step>
    Select the **IP restrictions** tab
  </Step>

  <Step>
    Click "**New rule**"
  </Step>

  <Step>
    Configure the rule settings:

    * **Role** (optional): Leave empty to apply to all PostgreSQL roles, or specify a particular role
    * **Schema** (optional): Leave empty to apply to all PostgreSQL schemas, or specify a particular schema
    * **IP ranges** (required): Enter a comma-separated list of IP addresses or CIDR ranges (e.g., `1.2.3.4/32, 10.0.0.0/8`)
  </Step>

  <Step>
    Click "**Create rule**"
  </Step>
</Steps>

## How IP restriction rules work

IP restrictions restrict database connections to the specified IP ranges. The behavior depends on how you configure each rule:

* **Apply to all roles and schemas**: Leave both the **Role** and **Schema** fields empty
* **Apply to specific role**: Specify a role name in the **Role** field to restrict connections for that role across all schemas
* **Apply to specific schema**: Specify a schema name in the **Schema** field to restrict connections to that schema from all roles
* **Apply to specific role and schema**: Specify both to create a rule that applies only when that role connects to that schema

Multiple rules can be created to build complex access policies for your database cluster.

## IP range format

The **IP ranges** field accepts:

* Individual IP addresses in CIDR notation (e.g., `1.2.3.4/32`)
* IP ranges in CIDR notation (e.g., `10.0.0.0/8`, `192.168.1.0/24`)
* Multiple entries separated by commas (e.g., `1.2.3.4/32, 10.0.0.0/8`)

## Editing an IP restriction rule

<Steps>
  <Step>
    Navigate to **Settings** → **IP restrictions**
  </Step>

  <Step>
    Click the menu icon (**...**) on the right side of the rule you want to edit
  </Step>

  <Step>
    Select **Edit** from the menu
  </Step>

  <Step>
    Modify the rule settings as needed:

    * **Role**: Change the role or leave empty to apply to all PostgreSQL roles
    * **Schema**: Change the schema or leave empty to apply to all PostgreSQL schemas
    * **IP ranges**: Update the comma-separated list of IP addresses or CIDR ranges
  </Step>

  <Step>
    Click "**Update rule**" to save your changes
  </Step>
</Steps>

## Deleting an IP restriction rule

<Steps>
  <Step>
    Navigate to **Settings** → **IP restrictions**
  </Step>

  <Step>
    Click the menu icon (**...**) on the right side of the rule you want to delete
  </Step>

  <Step>
    Select **Delete** from the menu
  </Step>

  <Step>
    Review the confirmation dialog showing the rule details (role, schema, and IP ranges)
  </Step>

  <Step>
    Click "**Delete rule**" to confirm deletion, or "**Cancel**" to keep the rule
  </Step>
</Steps>

<Warning>
  Deleting an IP restrictions rule is irreversible. After deletion, connections from those IP ranges will no longer be restricted, potentially allowing broader access to your database.
</Warning>

<Note>
  Rule creation and modification only applies to connections established after the change.
  It does not impact or disconnect existing connections, even if they break the newly-established rules.
</Note>

## Best practices

When configuring IP restrictions rules:

* Start with the most restrictive rules that meet your requirements
* Use CIDR notation to define ranges efficiently (e.g., `/24` for a subnet rather than listing individual IPs)
* Document the purpose of each rule by using descriptive role names or organizing rules by application
* Regularly audit your IP restrictions rules to remove access that is no longer needed
* Consider creating separate roles for different applications or environments to enable fine-grained access control

## Need help?

Get help from [the PlanetScale Support team](https://support.planetscale.com/), or join our [GitHub discussion board](https://github.com/planetscale/discussion/discussions) to see how others are using PlanetScale.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://planetscale.com/llms.txt