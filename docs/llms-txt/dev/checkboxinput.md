# Source: https://dev.writer.com/components/checkboxinput.md

# Checkbox Input

A user input component that allows users to choose multiple values from a list of options using checkboxes.

<img src="https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/checkboxinput.png?fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=2339dfe24b24547585529dff24aa7199" data-og-width="384" width="384" data-og-height="326" height="326" data-path="framework/public/components/checkboxinput.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/checkboxinput.png?w=280&fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=fbc2cc3f357b8a55d08b30be0e4f22da 280w, https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/checkboxinput.png?w=560&fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=294f734fb84e31b8e7de54577eb42ff9 560w, https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/checkboxinput.png?w=840&fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=a67048ffab180b4794e3ed7c3531118e 840w, https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/checkboxinput.png?w=1100&fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=d0aeab9ebd1b4bad2ec191d292f27873 1100w, https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/checkboxinput.png?w=1650&fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=30fba91002215583a0ce2015e7bd384b 1650w, https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/checkboxinput.png?w=2500&fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=bd2b4fcf08fefd559e12d014d6b273df 2500w" />

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
      <td>Options</td>
      <td>Key-Value</td>
      <td>Key-value object with options. Must be a JSON string or a state reference to a dictionary.</td>

      <td>
        <span>-</span>
      </td>
    </tr>

    <tr>
      <td>Orientation</td>
      <td>Text</td>
      <td>Specify how to lay out the options.</td>

      <td>
        <ol>
          <li>Vertical</li>

          <li>Horizontal</li>
        </ol>
      </td>
    </tr>

    <tr>
      <td>Primary text</td>
      <td>Color</td>
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
  <Accordion title="wf-options-change" icon="code">
    Sent when the selected options change.

    ```python  theme={null}
    def onchange_handler(state, payload):

    # Set the state variable "selected" to the selected options.
    # The payload will be a list, as multiple options are allowed.

    state["selected"] = payload
    ```
  </Accordion>
</AccordionGroup>

<events />
