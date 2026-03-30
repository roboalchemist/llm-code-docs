# Source: https://docs.xano.com/building/logic/triggers/workspace.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Workspace Triggers

> Workspace triggers are workflows that will run when certain actions happen in the workspace.

Workspace triggers are workflows that will run when certain actions happen in the workspace.

Workspace triggers have predefined inputs that can not be changed. These inputs are:

* `to_branch` - The branch that is being merged into

```json  theme={null}
{
    "id": 1,
    "label": "main"
}
```

* `from_branch` - The branch that is being merged from

```json  theme={null}
{
    "id": 2,
    "label": "dev"
}
```

* `action` - The action that triggered the trigger (`branch_live`, `branch_merge`, `branch_new`)

## Creating a Workspace Trigger

Click the⚙️ button in the top-right corner of your workspace dashboard and select <span class="ui-bubble">Triggers</span>.

<Frame caption="Accessing the Triggers menu on your workspace"><img src="https://mintcdn.com/xano-997cb9ee/E3ZmWFmmOyx8Tmpx/images/workspace-20251014-121951.png?fit=max&auto=format&n=E3ZmWFmmOyx8Tmpx&q=85&s=67211b7d870504f2dfe6f66020912a57" alt="workspace-20251014-121951" width="501" height="453" data-path="images/workspace-20251014-121951.png" /></Frame><br />

Click <span class="ui-bubble"><Icon icon="plus" /> Add Workspace Trigger</span>.

<Tabs>
  <Tab title="Visually" icon="hammer-brush">
    Give your trigger a name, a description, and any tags you'd like.

    <Tip>
      Make sure to toggle your Active status to off if you don't want the trigger to run as you build and test.

            <img src="https://mintcdn.com/xano-997cb9ee/E3ZmWFmmOyx8Tmpx/images/workspace-20251014-122129.png?fit=max&auto=format&n=E3ZmWFmmOyx8Tmpx&q=85&s=f2879699fdb211ef8208aabe646d22a0" alt="workspace-20251014-122129" width="544" height="147" data-path="images/workspace-20251014-122129.png" />
    </Tip>

    Select the **action(s)** that will execute this trigger.

    **Branch Live**\
    Any time a branch status is set to live

    **Branch Merge**\
    When a branch is merged

    **Branch New**\
    When a new branch is created

    Click <span class="ui-bubble"><Icon icon="disk" /> Save</span>.

    Now, you can build your trigger logic.
  </Tab>

  <Tab title="XanoScript" icon="code">
    Triggers in XanoScript have three sections: **inputs**, **logic**, and **actions**.

    **Inputs** are the data that will be available to the trigger.

    **Logic** is the actual logic that will be executed when the trigger fires.

    **Actions** are the actions that will be executed when the trigger fires.

    Here's an example of a basic workspace trigger in XanoScript:

    ```javascript lines icon="code" Example of a basic workspace trigger in XanoScript theme={null}
    workspace_trigger notify_on_branch_change {
      description = "Sends an email to the admin on branch activities"

      input {
        object to_branch {
          schema {
            int id
            text label
          }
        }
      
        object from_branch {
          schema {
            int id
            text label
          }
        }
      
        enum action {
          values = ["branch_live", "branch_merge", "branch_new"]
        }
      }

      stack {
        util.send_email {
          api_key = ""
          service_provider = "xano"
          subject = "Branch activity has occurred"
          message = $input.action
          bcc = []
          cc = []
          from = ""
          reply_to = ""
          scheduled_at = ""
        } as $x1
      }

      actions = {branch_live: true, branch_merge: true, branch_new: true}
    }
    ```

    <Card title="Learn how to build workspace triggers in XanoScript" icon="code" horizontal href="/xanoscript/triggers">
      For more information on how to build workspace triggers in XanoScript, see the XanoScript Workspace Triggers documentation.
    </Card>
  </Tab>
</Tabs>


Built with [Mintlify](https://mintlify.com).