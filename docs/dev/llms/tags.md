# Source: https://dev.writer.com/components/tags.md

# Tags

A component to display coloured tag pills.

<img src="https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/framework/public/components/tags.png?fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=e063b7fc90bfb6b61b52e86c618888e5" data-og-width="718" width="718" data-og-height="118" height="118" data-path="framework/public/components/tags.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/framework/public/components/tags.png?w=280&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=8b7790e2f1135f3e5b23bad2496a3dde 280w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/framework/public/components/tags.png?w=560&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=e284ec9d84b218fc3597b059a4cc6af1 560w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/framework/public/components/tags.png?w=840&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=0cad8792ff4178e778df975b47e3656b 840w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/framework/public/components/tags.png?w=1100&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=f53fac8fd43f10b1133538be5981f878 1100w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/framework/public/components/tags.png?w=1650&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=66f0324ccc590154ae60c9c19dd19544 1650w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/framework/public/components/tags.png?w=2500&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=3f08cdd4f51eed04b2f19f7ee9cdd7b4 2500w" />

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
      <td>Tags</td>
      <td>Key-Value</td>
      <td>Key-value object with tags. Must be a JSON string or a state reference to a dictionary.</td>

      <td>
        <span>-</span>
      </td>
    </tr>

    <tr>
      <td>Reference</td>
      <td>Color</td>
      <td>The colour to be used as reference for chroma and luminance, and as the starting point for hue rotation.</td>

      <td>
        <span>-</span>
      </td>
    </tr>

    <tr>
      <td>Seed value</td>
      <td>Number</td>
      <td>Choose a different value to reshuffle colours.</td>

      <td>
        <span>-</span>
      </td>
    </tr>

    <tr>
      <td>Rotate hue</td>
      <td>Boolean</td>
      <td>If active, rotates the hue depending on the content of the string. If turned off, the reference colour is always used.</td>

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
  <Accordion title="wf-tag-click" icon="code">
    Triggered when a tag is clicked.

    ```python  theme={null}
    def handle_tag_click(state, payload):
    state["selected_tag_id"] = payload
    ```
  </Accordion>
</AccordionGroup>

<events />
