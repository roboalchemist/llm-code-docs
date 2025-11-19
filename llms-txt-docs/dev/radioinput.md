# Source: https://dev.writer.com/components/radioinput.md

# Radio Input

A user input component that allows users to choose a single value from a list of options using radio buttons.

<img src="https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/radioinput.png?fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=62f8fbd28517eeb9e69b3f04df059665" data-og-width="352" width="352" data-og-height="296" height="296" data-path="framework/public/components/radioinput.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/radioinput.png?w=280&fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=03a22bd568a286a180eb15ac5678f8ac 280w, https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/radioinput.png?w=560&fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=a3dc1092276142c1487f5115fe4b97c2 560w, https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/radioinput.png?w=840&fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=6a2e1ea6f239aab9fdfccd472c38ed8a 840w, https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/radioinput.png?w=1100&fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=6c19771bcc93faaa7271ceb34d54592d 1100w, https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/radioinput.png?w=1650&fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=85e06413bbb7b56aef81b03a84385dee 1650w, https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/radioinput.png?w=2500&fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=5f74d16566440914f5aa42df01b9dc86 2500w" />

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
  <Accordion title="wf-option-change" icon="code">
    Sent when the selected option changes.

    ```python  theme={null}
    def onchange_handler(state, payload):

    # Set the state variable "selected" to the selected radio option

    state["selected"] = payload
    ```
  </Accordion>
</AccordionGroup>

<events />
