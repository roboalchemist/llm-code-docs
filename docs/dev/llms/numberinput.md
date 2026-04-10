# Source: https://dev.writer.com/components/numberinput.md

# Number Input

A user input component that allows users to enter numeric values.

<img src="https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/numberinput.png?fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=9ac0193e8bc4b79c02f96941b0dc3f4b" data-og-width="1176" width="1176" data-og-height="349" height="349" data-path="framework/public/components/numberinput.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/numberinput.png?w=280&fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=61640bed22d90061ef22f7612b169bbf 280w, https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/numberinput.png?w=560&fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=f8d1d271bf9b2d7bfd087523e0bd325b 560w, https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/numberinput.png?w=840&fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=9d99e4e4047ec2744cae2e8771fed91d 840w, https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/numberinput.png?w=1100&fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=d4fe5fe91cf9c2de2e8baea9038e00de 1100w, https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/numberinput.png?w=1650&fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=d5b15e1b56bd5174e9d24892f724ef76 1650w, https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/numberinput.png?w=2500&fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=0b3dfdcb944ea63078ff62c5e83b34f8 2500w" />

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
      <td>Placeholder</td>
      <td>Text</td>
      <td>-</td>

      <td>
        <span>-</span>
      </td>
    </tr>

    <tr>
      <td>Minimum value</td>
      <td>Number</td>
      <td>-</td>

      <td>
        <span>-</span>
      </td>
    </tr>

    <tr>
      <td>Max value</td>
      <td>Number</td>
      <td>-</td>

      <td>
        <span>-</span>
      </td>
    </tr>

    <tr>
      <td>Step</td>
      <td>Number</td>
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
  <Accordion title="wf-number-change" icon="code">
    Capture changes as they happen.

    ```python  theme={null}

    def onchange_handler(state, payload):

    # Set the state variable "new_val" to the new value

    state["new_val"] = payload
    ```
  </Accordion>

  <Accordion title="wf-number-change-finish" icon="code">
    Capture changes once this control has lost focus.

    ```python  theme={null}

    def onchange_handler(state, payload):

    # Set the state variable "new_val" to the new value

    state["new_val"] = payload
    ```
  </Accordion>
</AccordionGroup>

<events />
