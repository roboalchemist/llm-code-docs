# Source: https://dev.writer.com/components/tabs.md

# Tab Container

A container component for organising and displaying Tab components in a tabbed interface.

<img src="https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/tabs.png?fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=4d0cd3f2d5386d72cd6e0f864e879783" data-og-width="1182" width="1182" data-og-height="330" height="330" data-path="framework/public/components/tabs.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/tabs.png?w=280&fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=d460b24d8fb529b2ab724c25f2222e67 280w, https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/tabs.png?w=560&fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=dc7b56605fc2051a4d9e15a201f88705 560w, https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/tabs.png?w=840&fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=f529e80f0b7a54460de0ea5286372588 840w, https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/tabs.png?w=1100&fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=af11f252f7227a561a346a2f0a0c349a 1100w, https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/tabs.png?w=1650&fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=ffcea284a3c1a311aff4df1fcd353f1b 1650w, https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/tabs.png?w=2500&fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=82e4142ee571ec159fdaaa6ca2d0c51f 2500w" />

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
      <td>Secondary text</td>
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
      <td>Container shadow</td>
      <td>Shadow</td>
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
      <td>Button</td>
      <td>Color</td>
      <td>-</td>

      <td>
        <span>-</span>
      </td>
    </tr>

    <tr>
      <td>Button text</td>
      <td>Color</td>
      <td>-</td>

      <td>
        <span>-</span>
      </td>
    </tr>

    <tr>
      <td>Button shadow</td>
      <td>Shadow</td>
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
  <Accordion title="wf-tab-change" icon="code">
    Sent when the active tab changes.

    ```python  theme={null}
    def tab_change_handler(state, payload):

    # The payload contains the name of the newly activated tab

    state["active_tab"] = payload
    ```
  </Accordion>
</AccordionGroup>

<events />
