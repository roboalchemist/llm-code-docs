# Source: https://dev.writer.com/components/multiselectinput.md

# Multiselect Input

A user input component that allows users to select multiple values from a searchable list of options.

<img src="https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/multiselectinput.png?fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=d4f1b3922858c3241cc961bc59a9c3ad" data-og-width="1013" width="1013" data-og-height="196" height="196" data-path="framework/public/components/multiselectinput.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/multiselectinput.png?w=280&fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=787f2f590e8dea43289b73387e7c1e87 280w, https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/multiselectinput.png?w=560&fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=f1691aa69ff365eb03b13e26ed0ca7cb 560w, https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/multiselectinput.png?w=840&fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=2ef30113db114e77500706d0c18a1faf 840w, https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/multiselectinput.png?w=1100&fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=8aaf33aee4879cc989abf598033208d6 1100w, https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/multiselectinput.png?w=1650&fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=e11bf80b34cf21077d835cb6d8722285 1650w, https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/multiselectinput.png?w=2500&fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=6e4348400d9c1e04015be6b31cda62ce 2500w" />

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
      <td>Placeholder</td>
      <td>Text</td>
      <td>Text to show when no options are selected.</td>

      <td>
        <span>-</span>
      </td>
    </tr>

    <tr>
      <td>Maximum count</td>
      <td>Number</td>
      <td>The maximum allowable number of selected options. Set to zero for unlimited.</td>

      <td>
        <span>-</span>
      </td>
    </tr>

    <tr>
      <td>Accent</td>
      <td>Color</td>
      <td>The colour of the chips created for each selected option.</td>

      <td>
        <span>-</span>
      </td>
    </tr>

    <tr>
      <td>Chip text</td>
      <td>Color</td>
      <td>The colour of the text in the chips.</td>

      <td>
        <span>-</span>
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
      <td>Container background</td>
      <td>Color</td>
      <td>-</td>

      <td>
        <span>-</span>
      </td>
    </tr>

    <tr>
      <td>Separator</td>
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

    # Set the state variable "selected" to the selected option

    state["selected"] = payload
    ```
  </Accordion>
</AccordionGroup>

<events />
