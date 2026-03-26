# Source: https://docs.infrahub.app/guides/events-rules-actions.md

# Creating Event triggers rules and actions

[Triggers rules and actions feature](/topics/event-actions.md), allows you to respond to [events](/topics/events.md) as they occur within Infrahub by defining filter conditions and triggering actions.

success

By creating multiple rules and actions, you can build automated workflows.

## How it works[​](#how-it-works "Direct link to How it works")

1. **Define actions** that will be executed when triggered
2. **Create trigger rules** that match specific events
3. **Set filter conditions** to narrow down which events should trigger actions
4. **Activate the trigger** to start the automation

## Example workflows[​](#example-workflows "Direct link to Example workflows")

### Workflow 1: adding devices to group[​](#workflow-1-adding-devices-to-group "Direct link to Workflow 1: adding devices to group")

1. Device is created → with platform `Arista EOS`
2. → Node trigger rule detects the creation
3. → Group action adds device to `arista_devices` group

### Workflow 2: Automating circuit endpoint creation[​](#workflow-2-automating-circuit-endpoint-creation "Direct link to Workflow 2: Automating circuit endpoint creation")

1. Circuit is added to `provisioning_circuits` group
2. → Group trigger rule detects the addition
3. → Generator action runs `create_circuit_endpoints` Generator

## Step-by-step guide[​](#step-by-step-guide "Direct link to Step-by-step guide")

### 1. Creating actions[​](#1-creating-actions "Direct link to 1. Creating actions")

Actions define what will happen when a trigger rule's conditions are met.

#### Creating a group action[​](#creating-a-group-action "Direct link to Creating a group action")

A Group Action allows you to add or remove nodes from a group when triggered.

1. Navigate to the Actions page

2. Click the "Create" button and select "Group Action"

3. Configure the Group Action:

   * Enter a name (example: `add-to-group-arista_devices`)
   * Select the associated Kind of group, here we are using "Standard Group Core"
   * Choose the target group (example: `arista_devices`)
   * Click "Save"

![Group Action creation form](/assets/images/grp_actions-form-creation-d757bb6ea6a491f959820830cf590107.png)

4. View the created Group Action details

![Group Action details](/assets/images/grp_actions-details-f92e37708f8e697f9ae9009dbba4a014.png)

#### Creating a Generator action[​](#creating-a-generator-action "Direct link to Creating a Generator action")

A Generator Action allows you to run a Generator when triggered.

1. Navigate to the Actions page

2. Click the "Create" button and select "Generator Action"

3. Configure the Generator Action:

   * Enter a name (example: `create_circuit_endpoints`)
   * Select the Generator (example: `create_circuit_endpoints`)
   * Click "Save"

![Generator Action creation form](/assets/images/generator-action-form-creation-34c7932d1b6ceea3bee8de79fb6cac67.png)

### 2. Creating trigger rules[​](#2-creating-trigger-rules "Direct link to 2. Creating trigger rules")

Trigger rules define **when** actions should be executed based on specific events.

#### Creating a node trigger rule[​](#creating-a-node-trigger-rule "Direct link to Creating a node trigger rule")

A Node Trigger Rule allows you to detect changes to specific nodes and execute actions in response.

1. Navigate to the Trigger Rules page

2. Click the "Create" button and select "Node Trigger"

3. Configure the Node Trigger Rule:

   * Enter a name (example: `new-arista-devices`)
   * Select the node kind (example: "Device Infra")
   * Choose the mutation action (example: "created")
   * Select the action kind (example: "Group Action Core")
   * Choose the group action (example: `add-to-group-arista_devices`)
   * Click "Save"

![Node Trigger form creation](/assets/images/node-trigger-form-creation-9901e133baf23d4da80289b5bfae1932.png)

4. Add match conditions to refine when the trigger fires:

   <!-- -->

   * Navigate to the "Matches" tab
   * Click "Add Match"
   * Select "Node Trigger Relationship"
   * Choose the relationship name (example: "Platform")
   * Select the peer (example: `Arista EOS`)
   * Click "Save"

![Node Trigger matches form](/assets/images/node-trigger-matches-form-creation-1cad5213281dc45f534fd7b40aa1398a.png)

#### Creating a group trigger rule[​](#creating-a-group-trigger-rule "Direct link to Creating a group trigger rule")

A Group Trigger Rule allows you to detect changes to group membership and execute actions in response.

1. Navigate to the Trigger Rules page

2. Click the "Create" button and select "Group Trigger"

3. Configure the Group Trigger Rule:

   * Enter a name (example: `added-to-provisioning-circuits-group`)
   * Select the kind (example: "Standard Group Core")
   * Choose the standard group (example: `provisioning_circuits`)
   * Select the action kind (example: "Generator Action Core")
   * Choose the Generator action (example: `create_circuit_endpoints`)
   * Click "Save"

![Group Trigger form creation](/assets/images/group-trigger-form-creation-d575c2551fc910995a5c9dd89afce99c.png)
