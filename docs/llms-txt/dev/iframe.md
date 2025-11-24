# Source: https://dev.writer.com/components/iframe.md

# IFrame

A component to embed an external resource in an iframe.

<img src="https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/iframe.png?fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=f4aba06e4441d3099c6af3e1f2f54328" data-og-width="1220" width="1220" data-og-height="641" height="641" data-path="framework/public/components/iframe.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/iframe.png?w=280&fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=aabea02ad1e71ceb768750343f1836f5 280w, https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/iframe.png?w=560&fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=03b18f6940829c462d7af4a8e9fff8d2 560w, https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/iframe.png?w=840&fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=3776628b412bd4a43408f1df12b23900 840w, https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/iframe.png?w=1100&fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=acab1ac3b1da533d1db0ba375cb541a1 1100w, https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/iframe.png?w=1650&fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=a8973cee02f84c5826d9501325339018 1650w, https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/iframe.png?w=2500&fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=61702b7d3a29990b356b8c015a312f8d 2500w" />

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
      <td>Source</td>
      <td>Text</td>
      <td>A valid URL</td>

      <td>
        <span>-</span>
      </td>
    </tr>

    <tr>
      <td>Referrer Policy</td>
      <td>Text</td>
      <td>Define which referrer is sent when fetching the resource</td>

      <td>
        <ol>
          <li>no-referrer</li>

          <li>no-referrer-when-downgrade</li>

          <li>origin</li>

          <li>origin-when-cross-origin</li>

          <li>same-origin</li>

          <li>strict-origin</li>

          <li>strict-origin-when-cross-origin</li>

          <li>unsafe-url</li>
        </ol>
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
  <Accordion title="wf-load" icon="code">
    Fires when the resource has successfully loaded.

    ```python  theme={null}
    def load_handler(state):

    # Sets status message when resource is loaded

    state["status"] = "Page loaded"
    ```
  </Accordion>
</AccordionGroup>

<events />
