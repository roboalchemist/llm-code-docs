# Source: https://dev.writer.com/components/ratinginput.md

# Rating Input

A user input component that allows users to provide a rating.

<img src="https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/ratinginput.png?fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=c6c89acc844e5cc114074d2c2c1c9916" data-og-width="560" width="560" data-og-height="214" height="214" data-path="framework/public/components/ratinginput.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/ratinginput.png?w=280&fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=3a0272e3187b2e522c71237a08a2b51f 280w, https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/ratinginput.png?w=560&fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=0f0e41e52d8ed683652fbde8e341a21a 560w, https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/ratinginput.png?w=840&fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=07273ff26519f570b27b13dd2f16b3f1 840w, https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/ratinginput.png?w=1100&fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=4b25bceb9e16b74016a8844301f2002c 1100w, https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/ratinginput.png?w=1650&fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=f8b171ee76988f3d76c718bf4853f29e 1650w, https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/ratinginput.png?w=2500&fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=9f9021a467651879aa0bee960fc6fe5e 2500w" />

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
      <td>Feedback</td>
      <td>Text</td>
      <td>-</td>

      <td>
        <ol>
          <li>Stars</li>

          <li>Faces</li>

          <li>Hearts</li>
        </ol>
      </td>
    </tr>

    <tr>
      <td>Minimum value</td>
      <td>Number</td>
      <td>Valid values are 0 and 1.</td>

      <td>
        <span>-</span>
      </td>
    </tr>

    <tr>
      <td>Max value</td>
      <td>Number</td>
      <td>Valid values are between 2 and 11.</td>

      <td>
        <span>-</span>
      </td>
    </tr>

    <tr>
      <td>Step</td>
      <td>Number</td>
      <td>Valid values are between 0.25 and 1.</td>

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
    ```python  theme={null}

    def onchange_handler(state, payload):

    # Set the state variable "rating" to the new value

    state["rating"] = payload
    ```
  </Accordion>
</AccordionGroup>

<events />
