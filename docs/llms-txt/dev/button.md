# Source: https://dev.writer.com/components/button.md

# Button

A standalone button component that can be linked to a click event handler.

<img src="https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/button.png?fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=9d815fb527db70a4663f7a3ea2dd7575" data-og-width="766" width="766" data-og-height="210" height="210" data-path="framework/public/components/button.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/button.png?w=280&fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=7de38897c7a44b6f13103b943d7337e2 280w, https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/button.png?w=560&fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=da183456d7dffdb93e1677a3b18e0384 560w, https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/button.png?w=840&fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=b4a3806d1e1677582590fe8fd8ac6aa7 840w, https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/button.png?w=1100&fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=61f436438006ddf30602ee03e8e0e3ac 1100w, https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/button.png?w=1650&fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=1bda45fd5548d2f8c399cd5b40595dea 1650w, https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/button.png?w=2500&fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=f67f49425a467b0003f162eb48465f00 2500w" />

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
      <td>Text</td>
      <td>Text</td>
      <td>-</td>

      <td>
        <span>-</span>
      </td>
    </tr>

    <tr>
      <td>Icon</td>
      <td>Text</td>
      <td>Lucide icon name in kebab-case, e.g. "badge-check".</td>

      <td>
        <span>-</span>
      </td>
    </tr>

    <tr>
      <td>Disabled</td>
      <td>Boolean</td>
      <td>Disables all event handlers.</td>

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
  <Accordion title="wf-click" icon="code">
    Capture single clicks.

    ```python  theme={null}
    def handle_button_click(state):

    # Increment counter when the button is clicked

    state["counter"] += 1
    ```
  </Accordion>
</AccordionGroup>

<events />
