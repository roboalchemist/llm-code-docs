# Source: https://dev.writer.com/agent-builder/state.md

> ## Documentation Index
> Fetch the complete documentation index at: https://dev.writer.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Manage agent state

The agent's state is a core component of the agent's behavior. It contains values that the UI, blueprint, and custom Python code can access and update. The state acts as a shared memory for each part of the agent.

## Agent state explained

Think of an agent's "state" like a memory or a notebook that stores important information. Just like how you might jot down notes to remember things, an agent uses its state to keep track of various values or data that it needs to perform its tasks.

Imagine you're building a chatbot using Writer's Agent Builder. The chatbot needs to remember the user's name, so it can greet them by name later. In this case, the agent stores the user's name in its state as a variable. The chatbot can access this information and use it to personalize its responses.

The state is like a shared notebook that different parts of the agent can read from and write to. This allows the agent to keep track of its progress, remember important details, and make decisions based on the information stored in its state.

<img src="https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/agent-state-overview.png?fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=4e36344cda72982ab9263783fb3388a1" alt="Agent state explained" data-og-width="2424" width="2424" data-og-height="1455" height="1455" data-path="images/agent-builder/agent-state-overview.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/agent-state-overview.png?w=280&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=ef10b750efc6839c31da8da1d437c0c2 280w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/agent-state-overview.png?w=560&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=fb558dee1f481f321fa980c55e98abd8 560w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/agent-state-overview.png?w=840&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=752e58343330042833b6b0a00ffba407 840w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/agent-state-overview.png?w=1100&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=bdc81f86216f1ac50beb38ec3b244f59 1100w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/agent-state-overview.png?w=1650&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=80f66623dc46678b08c2c7e2861e304d 1650w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/agent-state-overview.png?w=2500&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=a839df6213cb12d5995985d008a35f1f 2500w" />

<Note>
  Agent state is session-based, temporary, and visible in the UI.

  * For persistent, non-sensitive data: use the [**Key-Value Storage** block](/blueprints/key-valuestorage) to store data in the cloud.
  * For sensitive data: use [**Vault**](/agent-builder/secrets) to store sensitive information like API keys, passwords, and credentials.
</Note>

## Inspect the state

You can view the agent's state from any view by clicking the **State explorer** icon in the top right of the page. This is helpful for debugging and understanding how the agent is working.

<img src="https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/state-explorer-icon.png?fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=dc9b3e4865094cbb8ab1c1b016b1393d" alt="State explorer icon" data-og-width="830" width="830" data-og-height="183" height="183" data-path="images/agent-builder/state-explorer-icon.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/state-explorer-icon.png?w=280&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=c879c37cc482564a6d147017903e4783 280w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/state-explorer-icon.png?w=560&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=3f059d1a8f0aef068d333aab62ac3eee 560w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/state-explorer-icon.png?w=840&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=9fc574243187e6eddf1fbd838e21c0d8 840w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/state-explorer-icon.png?w=1100&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=b6244e617a09a9b798cedf1d021f946a 1100w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/state-explorer-icon.png?w=1650&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=3a2844ff0e041c4880ddb3f7306038b4 1650w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/state-explorer-icon.png?w=2500&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=f31a2f62a7a3b151be20e9c1901f1f42 2500w" />

## Set state variables

You can set and update state variables in two ways:

* In a UI input element
* Using the **Set state** block in the blueprint
* Using custom Python code

### Set state in a UI input element

You can set state variables in any input block in the UI under the **Binding** section of the UI element's properties.

When a user enters a value in the input element, the value is automatically set as a state variable with the name you provide in the **Binding** section. Other parts of the agent can access this value.

<img src="https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/set-state-binding.png?fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=8d9db5288724df259cd60eebe64a6884" alt="Set state in a UI input element" data-og-width="776" width="776" data-og-height="466" height="466" data-path="images/agent-builder/set-state-binding.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/set-state-binding.png?w=280&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=b89fb3d0d3db08301c54838b0651a7ce 280w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/set-state-binding.png?w=560&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=965604543f9e7e078098993affdb4237 560w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/set-state-binding.png?w=840&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=3aa5e5d96875b046784df72ee55f1406 840w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/set-state-binding.png?w=1100&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=e95e77718746298cd81ac41c9a1d9ca2 1100w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/set-state-binding.png?w=1650&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=77f39ee6221b10ad4760ba096ecc384d 1650w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/set-state-binding.png?w=2500&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=84b844f0b34c0b171c6611880fc8e236 2500w" />

### Set state block

The [**Set state** block](/blueprints/setstate) allows you to set a state variable within a blueprint. Provide the name of the state variable and the value you want to set. When the block runs, the state variable is created or updated with the provided value.

<img src="https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/set-state-block.png?fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=ef439a171b99236a03a471d08691e66e" alt="Set state block" data-og-width="2078" width="2078" data-og-height="1260" height="1260" data-path="images/agent-builder/set-state-block.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/set-state-block.png?w=280&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=6e02a4c3df8b9c93199f5839576ac016 280w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/set-state-block.png?w=560&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=c97c07b8af35d5c6777f50303a23cc33 560w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/set-state-block.png?w=840&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=5d941af5941a0016c6f036daa5154a72 840w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/set-state-block.png?w=1100&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=6bf255dfe27fbae9caadb5dd2ca58fb6 1100w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/set-state-block.png?w=1650&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=d670f8a151f37e18239ae3036b91489b 1650w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/set-state-block.png?w=2500&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=3b4adc61ae1e1ae41638dc03f4f2f977 2500w" />

You can set state variables as `text` or `JSON`. Under the **Value type** dropdown, select the type of value you want to set. In the **Value** field, enter the value you want to set.

If you set the value as `text`, the value of the state variable is stored as a string. If you set the value as `JSON`, the value of the state variable is stored as a JSON object.

See how to [access nested state variables that are set as JSON](#nested-state-variables) below.

### Set state with custom Python

You can also set state variables with custom Python code.

To initialize the state, use the `wf.init_state` function:

```python  theme={null}
import writer as wf

wf.init_state({
    "counter": 0
})
```

To update the state, define a function that takes the state as an argument and updates the state. The state is similar to a Python dictionary, so you can update it by accessing the key and assigning a new value.

```python  theme={null}
def increment(state):
    state["counter"] += 1
```

#### Private state variables

You can create private state variables with custom Python code. Private state variables are not visible to the agent's UI and are only accessible via code.

To create a private state variable, prefix the variable with an underscore (`_`).

```python  theme={null}
wf.init_state({
    "_user_name": "John Doe"
})
```

## Access state variables

You can access state variables in the agent's blueprint, UI, and custom Python code.

### Access state variables in a UI element

You can access state variables in a UI element by using the `@` syntax.

<img src="https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/access-state-variables-in-ui.png?fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=e055a20dd98cd3cdda9e6c629b4acf92" alt="Access state variables in a UI element" data-og-width="1514" width="1514" data-og-height="346" height="346" data-path="images/agent-builder/access-state-variables-in-ui.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/access-state-variables-in-ui.png?w=280&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=c168032e2872f214b03722943a9739a9 280w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/access-state-variables-in-ui.png?w=560&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=4c4bae9866586366e89a1f43cb8c5d6e 560w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/access-state-variables-in-ui.png?w=840&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=21c15f79d5583a442beefc4c94b2ced0 840w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/access-state-variables-in-ui.png?w=1100&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=c8da487356f141bc49f6e5ca4fbee13f 1100w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/access-state-variables-in-ui.png?w=1650&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=b7a80615615be292cb1221dfdf0ffb65 1650w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/access-state-variables-in-ui.png?w=2500&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=ab2b8206c2e172fd65f319fec006536b 2500w" />

### Access state variables in a blueprint

Access state variables in a blueprint by using the `@` syntax.

<img src="https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/access-state-variables-in-a-blueprint.png?fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=4440a39610cb0006b0e63e576b32f582" alt="Access state variables in a blueprint" data-og-width="1554" width="1554" data-og-height="680" height="680" data-path="images/agent-builder/access-state-variables-in-a-blueprint.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/access-state-variables-in-a-blueprint.png?w=280&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=4a182348fd9694b8c196c6f781b1c7ae 280w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/access-state-variables-in-a-blueprint.png?w=560&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=fab49dd0932fcc198f6dd00e220c7d70 560w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/access-state-variables-in-a-blueprint.png?w=840&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=9a6d0bedddcd2e3a91380c4c8cf62a31 840w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/access-state-variables-in-a-blueprint.png?w=1100&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=9cc9a9ddb89905ddb85e865768aab636 1100w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/access-state-variables-in-a-blueprint.png?w=1650&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=47e2b71d039af1b80cf93f76a09e7685 1650w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/access-state-variables-in-a-blueprint.png?w=2500&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=855fde8b527af1e9965af31c80c17c80 2500w" />

### Access state variables in custom Python

You can access state variables in custom Python code by referencing the `state` variable. The `state` variable functions like a Python dictionary, so you can access and update state variables by referencing the key.

Pass the `state` variable to the function when you call it.

```python  theme={null}
def increment(state):
    state["counter"] += 1
```

## Nested state variables

Agent Builder allows you to create and access nested state variables. This is useful when you need to store complex data that requires multiple levels of organization.

### Set nested state variables

You can set nested state variables in the **Set state** block using `JSON` as the value type and a JSON object as the value.

You can also set nested state variables in custom Python code.

### Access nested state variables

In the UI or a blueprint, use `.` to access the different levels of nested state variables. For example, consider a state variable with the following structure:

```json  theme={null}
"tasks": [
    {
        "title": "Write a blog post"
    }
]
```

<img src="https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/nested-state-explorer.png?fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=73f697a54d675d4b4d4d4253bf7f6d2c" alt="Nested state variables" data-og-width="2388" width="2388" data-og-height="674" height="674" data-path="images/agent-builder/nested-state-explorer.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/nested-state-explorer.png?w=280&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=72c3939e2d24a2e0f6eb5d7b064e5e41 280w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/nested-state-explorer.png?w=560&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=5974e0675848d677a48bf979b28d2252 560w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/nested-state-explorer.png?w=840&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=a989fdf2be25c60f0e4517797dd361ee 840w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/nested-state-explorer.png?w=1100&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=5250c584900216abe944abcf5cb2272b 1100w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/nested-state-explorer.png?w=1650&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=1d197c10e5db22f128dc0948833d0cb5 1650w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/nested-state-explorer.png?w=2500&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=a3f73eeaa7d84121100c91d909578e4d 2500w" />

To access the `title` of the first task in a blueprint or UI block, use the following syntax:

```
@{tasks.0.title}
```

<img src="https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/nested-state-ui.png?fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=686ef244f4b99caccac318b712d81e4c" alt="Accessing nested state variables in a UI element" data-og-width="2556" width="2556" data-og-height="712" height="712" data-path="images/agent-builder/nested-state-ui.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/nested-state-ui.png?w=280&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=d45c2ede0c6fca5ed9ab37eaf12a3a4c 280w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/nested-state-ui.png?w=560&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=d34ff09a5c04a2921ef58077a12e2995 560w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/nested-state-ui.png?w=840&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=96248c09fbb9b2641f87b842afc7d7f4 840w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/nested-state-ui.png?w=1100&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=5472f179dd7d06e87805f138f69e8f25 1100w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/nested-state-ui.png?w=1650&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=a05f036809474eba77790b4fb9fd8fdb 1650w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/nested-state-ui.png?w=2500&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=68f4f81ee34c607c3719227a5f9c3fa9 2500w" />

<feedback />
