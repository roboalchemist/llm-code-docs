# Source: https://dev.writer.com/components/timeinput.md

# Time Input

A user input component that allows users to select a time.

<img src="https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/framework/public/components/timeinput.png?fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=3d11d45afa17bf645a69103e890f74b7" data-og-width="171" width="171" data-og-height="125" height="125" data-path="framework/public/components/timeinput.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/framework/public/components/timeinput.png?w=280&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=1c384764d1b6db0cac606f00096ded78 280w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/framework/public/components/timeinput.png?w=560&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=f98c2bb96f5164f39af8c1165c1f7169 560w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/framework/public/components/timeinput.png?w=840&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=b30e91e81c34c07b527e02d00993338f 840w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/framework/public/components/timeinput.png?w=1100&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=c15bba20eed650bfe14d02e9c446a6ae 1100w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/framework/public/components/timeinput.png?w=1650&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=3384ce9b4e1ebe8603659c3d8886fce7 1650w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/framework/public/components/timeinput.png?w=2500&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=8570761f477d981c6e7fafd64482f6d8 2500w" />

## Fields

<table className="componentFields">
  <thead>
    <th>Name</th>
    <th>Type</th>
    <th class="desc">Description</th>
    <th>Options</th>
  </thead>

  <tbody>
    <tr>
      <td>Label</td>
      <td>Text</td>
      <td>-</td>

      <td>
        <span>-</span>
      </td>
    </tr>

    <tr>
      <td>Custom CSS classes</td>
      <td>Text</td>
      <td>CSS classes, separated by spaces. You can define classes in custom stylesheets.</td>

      <td>
        <span>-</span>
      </td>
    </tr>
  </tbody>
</table>

## Events

<AccordionGroup>
  <Accordion title="wf-time-change" icon="code">
    Capture changes to this control.

    ```python  theme={null}

    def onchange_handler(state, payload):

    # Set the state variable "new_time" to the new value, provided as a hh:mm string (in 24-hour format that includes leading zeros).

    state["new_time"] = payload
    ```
  </Accordion>
</AccordionGroup>

<events />
