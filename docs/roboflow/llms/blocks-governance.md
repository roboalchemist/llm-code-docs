# Source: https://docs.roboflow.com/roboflow/roboflow-ko/workflows/blocks-governance.md

# Source: https://docs.roboflow.com/roboflow/roboflow-jp/workflows/blocks-governance.md

# Source: https://docs.roboflow.com/roboflow/roboflow-hi/workflows/blocks-governance.md

# Source: https://docs.roboflow.com/workflows/blocks-governance.md

# Blocks Governance

{% hint style="info" %}
Blocks Governance is a premium feature, available to select Enterprise plan customers. [Talk to our Sales team](https://roboflow.com/sales) to get access to Blocks Governance.
{% endhint %}

Super Users can control which workflow blocks are available to users in the workspace. This allows you to manage complexity, enforce best practices, and control which AI\
models and processing steps your team can use in their workflows.

{% hint style="info" %}
Super User requires [Custom Role feature](https://docs.roboflow.com/team-members/role-based-access-control#custom-roles) so the page can being seeing. Standard Admin, Labeler, and Reviewer roles do not have access to manage workflow blocks.
{% endhint %}

Workflow blocks can be enabled or disabled at the workspace level. When a block is disabled:

* It will not appear in the block picker when users build workflows
* Existing workflows using the disabled block will continue to function
* Users cannot add the disabled block to new workflows or existing workflows

This feature helps Super Users:

* Simplify the workflow builder interface for specific use cases
* Prevent the use of certain AI models or processing steps
* Gradually roll out new blocks to users
* Maintain consistency across team workflows

## Accessing Workflow Blocks Settings

To manage workflow blocks, you must have the manage\_workspace\_blocks permission. By default, this permission is only granted to Super Users.

To access the settings:

1. Navigate to your workspace settings
2. Select Workflow Blocks from the sidebar
3. You'll see a list of all available workflow blocks with enable/disable toggles

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2FEFe6HbEINiGM3z61WprF%2Fimage.png?alt=media&#x26;token=d6293aca-b362-420e-bfae-2d8a4029337d" alt=""><figcaption></figcaption></figure>

### Enabling and Disabling Blocks

#### Disabling a Block

To disable a workflow block:

1. Locate the block in the Workflow Blocks settings list
2. Toggle the switch to the off position
3. The block is immediately disabled for all users in the workspace
4. Users will no longer see this block in the workflow editor's block picker

**Important:** Disabling a block affects existing workflows that use it:

* Workflows containing the disabled block cannot be updated or edited
* Workflows with disabled blocks cannot be loaded from inference servers
* You must modify any such workflows to remove or replace the disabled block before you can continue using them

#### Enabling a Block

To enable a workflow block:

1. Locate the block in the Workflow Blocks settings list
2. Toggle the switch to the on position
3. The block is immediately available to all users in the workspace
4. Users can now add this block to their workflows

#### Default Behavior for New Blocks

When you disable any workflow block for the first time, all newly created blocks will be disabled by default from that point forward. This behavior ensures that:

* New blocks don't automatically become available without Super User review
* You maintain control over which blocks are accessible to your team
* Blocks can be tested and validated before being enabled for general use

After the first block is disabled, any new blocks added to Roboflow will require explicit enablement in the Workflow Blocks settings before users can access them in the workflow editor.

#### Impact on the Workflow Editor

When a block is disabled, users will see it in the block picker in a disabled state. This allows users to be aware of the block's existence while preventing them from using it.

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2FvOS5YGN8MMLJn70vgffu%2Fimage.png?alt=media&#x26;token=368ff908-1e33-4811-8fc2-a6524ef6b727" alt=""><figcaption></figcaption></figure>

Disabled blocks:

* Appear in the block picker with a visual indication that they are disabled (e.g., grayed out)
* Are visible in search results and block categories
* Cannot be dragged into the workflow canvas
* Allow users to see that the block exists and request enablement from a Super User if needed

This approach maintains visibility while preventing usage, enabling users to reach out to Super Users to request that specific blocks be enabled if they are needed for their workflows.

### Common use cases for managing block availability:

Restricting AI Models: Disable blocks that use specific AI models you don't want users to access (e.g., certain premium models or models not suitable for your use case)

Simplifying Workflows: For teams focused on specific tasks, disable irrelevant blocks to reduce clutter and confusion

Phased Rollout: When new blocks are released by Roboflow, keep them disabled initially and enable them once training and documentation are ready

Compliance: Disable blocks that don't meet your organization's security, privacy, or compliance requirements
