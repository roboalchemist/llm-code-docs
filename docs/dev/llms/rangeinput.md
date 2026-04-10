# Source: https://dev.writer.com/components/rangeinput.md

# Slider Range Input

A user input component that allows users to select numeric values range using a range slider with optional constraints like min, max, and step.

<img src="https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/rangeinput.png?fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=97dd38e810528289dc0a7ef53d95694a" data-og-width="1091" width="1091" data-og-height="165" height="165" data-path="framework/public/components/rangeinput.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/rangeinput.png?w=280&fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=02cadae820ce84083b5eb76df4a8463f 280w, https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/rangeinput.png?w=560&fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=365f736c37506af60c3c18a28589bc08 560w, https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/rangeinput.png?w=840&fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=ff01c1ec3409dbfa66d6336a883d7220 840w, https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/rangeinput.png?w=1100&fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=2bfa8583705938697894678126ffca36 1100w, https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/rangeinput.png?w=1650&fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=8c26b3b975e950c2fecd11204e39e882 1650w, https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/rangeinput.png?w=2500&fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=5308b65bc8642e52db7a91aeb9ea58f4 2500w" />

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
  <Accordion title="wf-range-change" icon="code">
    Capture changes to this control.

    ```python  theme={null}

    def onchange_handler(state, payload):

    # Set the state variables "from" & "to" to the new range
    state["from"] = payload[0]
    state["to"] = payload[1]
    ```
  </Accordion>
</AccordionGroup>

<events />
