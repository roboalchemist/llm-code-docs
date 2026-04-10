# Source: https://dev.writer.com/components/switchinput.md

# Switch Input

A user input component with a simple on/off status.

<img src="https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/switchinput.png?fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=a7c8e23a278a0399ace156799dde5567" data-og-width="480" width="480" data-og-height="138" height="138" data-path="framework/public/components/switchinput.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/switchinput.png?w=280&fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=371a060577d4c4b7bdc285d4f95e11a6 280w, https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/switchinput.png?w=560&fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=39f3c07c0713b6912cbf92f2bd5e8887 560w, https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/switchinput.png?w=840&fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=e6fc75152824da192485570aec704734 840w, https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/switchinput.png?w=1100&fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=7fe94b1a5f72983f9333bb1a4595e96f 1100w, https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/switchinput.png?w=1650&fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=dc28645573fa9d10b26e84f89f01290c 1650w, https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/switchinput.png?w=2500&fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=f9e9ee08e84e5f6b73bf2161dc79b68b 2500w" />

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
      <td>Accent</td>
      <td>Color</td>
      <td>-</td>

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
  <Accordion title="wf-toggle" icon="code">
    Sent when the switch is toggled.

    ```python  theme={null}
    def handle_toggle(state, payload):

    # The payload will be a bool 

    state["its_on"] = payload
    ```
  </Accordion>
</AccordionGroup>

<events />
