# Source: https://dev.writer.com/blueprints/addtostatelist.md

# Add to state list

Adds a new item to a list in the Agent's state. Useful for tracking multiple values over time.

<img src="https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/blueprints/add-to-state-list-block.png?fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=100e5471f1ca96fe0db3e31f6032c060" alt="" data-og-width="2310" width="2310" data-og-height="1490" height="1490" data-path="images/agent-builder/blueprints/add-to-state-list-block.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/blueprints/add-to-state-list-block.png?w=280&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=39895ec897067c0aa9161ba47fda2059 280w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/blueprints/add-to-state-list-block.png?w=560&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=25bb63a54bed430d69e18d4ad482bbe2 560w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/blueprints/add-to-state-list-block.png?w=840&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=1e21b5ce1618e5a45bc8b6bb5ac01d06 840w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/blueprints/add-to-state-list-block.png?w=1100&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=d8a45bb2304bf73961263953b08a4c7a 1100w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/blueprints/add-to-state-list-block.png?w=1650&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=4ad617d562ef1f0ec9e35aac59d640ad 1650w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/blueprints/add-to-state-list-block.png?w=2500&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=a4f5ba6f33e9719fdd2cc583d2951896 2500w" />

## Overview

This block adds a string value to a list in the agent's state. It behaves differently depending on the state element's type:

* If the state element doesn't already exist, the block creates it and adds the value to it.
* If the state element already exists as a list, the block adds the value to the list.
* If the state element exists but isn't a list, the block fails.

<Warning>The **Add to state list** block only accepts string values. If you pass a value such as a dictionary, it will be converted to a string and added to the list.</Warning>

## Example

The following example shows an **Add to state list** block as part of a **For-each** workflow.

<img src="https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/blueprints/add-to-state-list-example.png?fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=d093788c9b4e0e578056caa75864838c" alt="" data-og-width="2852" width="2852" data-og-height="1610" height="1610" data-path="images/agent-builder/blueprints/add-to-state-list-example.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/blueprints/add-to-state-list-example.png?w=280&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=b2dd33f4671d0db01936a2a8dd778478 280w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/blueprints/add-to-state-list-example.png?w=560&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=1fa6ca007a1e204dbe11346d29e33d9d 560w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/blueprints/add-to-state-list-example.png?w=840&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=6ada7b2f19d8972ba687c58adf0b7fe6 840w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/blueprints/add-to-state-list-example.png?w=1100&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=ddd71d0c7ad556553220844fc3e2c9e1 1100w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/blueprints/add-to-state-list-example.png?w=1650&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=c4b6aeb36a86c483c971bfaa826b54a4 1650w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/blueprints/add-to-state-list-example.png?w=2500&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=f0db87ef7839af326220ed2817d0f3ae 2500w" />

The **For-each loop** block iterates over a list of values and generates text for each value. Then, the **Add to state list** block adds the result of each iteration to the state list called `text_gen_results`.

On the initial run, the **Add to state list** block creates the state element and adds the first value to it. Every subsequent run, the block adds the next value to the list.

## Fields

<table className="blueprintFields">
  <thead>
    <th>Name</th>
    <th>Type</th>
    <th>Control</th>
    <th>Default</th>
    <th>Description</th>
    <th>Options</th>
    <th>Validation</th>
  </thead>

  <tbody>
    <tr>
      <td>Link Variable</td>
      <td>Binding</td>
      <td>-</td>

      <td>
        <span>-</span>
      </td>

      <td>Set the variable here and use it across your agent.</td>

      <td>
        <span>-</span>
      </td>

      <td>
        <span>-</span>
      </td>
    </tr>

    <tr>
      <td>Value</td>
      <td>Text</td>
      <td>Textarea</td>

      <td>
        <span>-</span>
      </td>

      <td>-</td>

      <td>
        <span>-</span>
      </td>

      <td>
        <span>-</span>
      </td>
    </tr>
  </tbody>
</table>

## End states

Below are the possible end states of the block call.

<table className="blueprintFields">
  <thead>
    <th>Name</th>
    <th>Field</th>
    <th>Type</th>
    <th>Description</th>
  </thead>

  <tbody>
    <tr>
      <td>Success</td>
      <td>-</td>
      <td>success</td>
      <td>If the function doesn't raise an Exception.</td>
    </tr>

    <tr>
      <td>Error</td>
      <td>-</td>
      <td>error</td>
      <td>If the function raises an Exception.</td>
    </tr>
  </tbody>
</table>
