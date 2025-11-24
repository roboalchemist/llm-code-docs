# Source: https://dev.writer.com/components/sliderinput.md

# Slider Input

A user input component that allows users to select numeric values using a slider with optional constraints like min, max, and step.

<img src="https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/sliderinput.png?fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=ac02c4d2112cadc7f0c399fbaf107922" data-og-width="429" width="429" data-og-height="165" height="165" data-path="framework/public/components/sliderinput.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/sliderinput.png?w=280&fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=24ee076a0d0237bf90b57f6dc1fc5881 280w, https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/sliderinput.png?w=560&fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=7af34892e614736fae84cb7512188e57 560w, https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/sliderinput.png?w=840&fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=fe90c971f5d91a11a7f27064c4801aba 840w, https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/sliderinput.png?w=1100&fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=c7e22f280f2394958e222aabd601e685 1100w, https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/sliderinput.png?w=1650&fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=c3d4ab9e8ec920c25ad90c6bdee980ef 1650w, https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/sliderinput.png?w=2500&fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=02436b7fc8bb4635d9341240e40ccd67 2500w" />

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
      <td>Minimum value</td>
      <td>Number</td>
      <td>-</td>

      <td>
        <span>-</span>
      </td>
    </tr>

    <tr>
      <td>Maximum value</td>
      <td>Number</td>
      <td>-</td>

      <td>
        <span>-</span>
      </td>
    </tr>

    <tr>
      <td>Step size</td>
      <td>Number</td>
      <td>-</td>

      <td>
        <span>-</span>
      </td>
    </tr>

    <tr>
      <td>Accent</td>
      <td>Color</td>
      <td>-</td>

      <td>
        <span>-</span>
      </td>
    </tr>

    <tr>
      <td>Popover color</td>
      <td>Color</td>
      <td>-</td>

      <td>
        <span>-</span>
      </td>
    </tr>

    <tr>
      <td>Popover background</td>
      <td>Color</td>
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
    Capture changes to this control.

    ```python  theme={null}

    def onchange_handler(state, payload):

    # Set the state variable "new_val" to the new value

    state["new_val"] = payload
    ```
  </Accordion>
</AccordionGroup>

<events />
