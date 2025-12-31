# Source: https://dev.writer.com/components/dateinput.md

# Date Input

A user input component that allows users to select a date using a date picker interface.

<img src="https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/dateinput.png?fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=3b6ac36de9d370ad186445ca5890b8a0" data-og-width="698" width="698" data-og-height="340" height="340" data-path="framework/public/components/dateinput.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/dateinput.png?w=280&fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=f674b95c8075aa42a6d67d65e22c959d 280w, https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/dateinput.png?w=560&fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=6bfd4bfd0d2916cda3d1ed740bd5ff85 560w, https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/dateinput.png?w=840&fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=11897eb748f4b206734b26eccebc372a 840w, https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/dateinput.png?w=1100&fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=4529c7a298f7b5bb307713482ee53b2e 1100w, https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/dateinput.png?w=1650&fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=358fac1dcea41fdb183e8eea838468ec 1650w, https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/dateinput.png?w=2500&fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=c9ee8ff540d199ce72ad679c116d6daa 2500w" />

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
  <Accordion title="wf-date-change" icon="code">
    Capture changes to this control.

    ```python  theme={null}

    def onchange_handler(state, payload):

    # Set the state variable "new_date" to the new value, provided as a YYYY-MM-DD string.

    state["new_date"] = payload
    ```
  </Accordion>
</AccordionGroup>

<events />
