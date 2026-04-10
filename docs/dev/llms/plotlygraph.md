# Source: https://dev.writer.com/components/plotlygraph.md

# Plotly Graph

export const fig_0 = undefined

A component that displays Plotly graphs.

<img src="https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/plotlygraph.png?fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=d73f45de15672a4c982cb82acb37ab10" data-og-width="740" width="740" data-og-height="660" height="660" data-path="framework/public/components/plotlygraph.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/plotlygraph.png?w=280&fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=ef28d9baabc39cc72e1c0ae348e2ec77 280w, https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/plotlygraph.png?w=560&fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=9e21b6b8366fe899746c0fc445311969 560w, https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/plotlygraph.png?w=840&fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=55ae154f9bbcb73d1ab4de37fbdba50e 840w, https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/plotlygraph.png?w=1100&fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=74942332c5beca376456c9d007bfa475 1100w, https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/plotlygraph.png?w=1650&fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=b72b869f69594ef3e8b5553850690efb 1650w, https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/plotlygraph.png?w=2500&fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=9682ead20f740da28416fe2fcb89d3d7 2500w" />

You can listen to events triggered by Plotly.js and add interactivity to your charts.
For example, implement cross-filtering.

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
      <td>Graph specification</td>
      <td>Object</td>
      <td>Plotly graph specification. Pass it using state, e.g. @{fig_0}, or paste a JSON specification.</td>

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
  <Accordion title="plotly-click" icon="code">
    Sends a list with the clicked points.

    ```python  theme={null}
    ```
  </Accordion>

  <Accordion title="plotly-selected" icon="code">
    Sends a list with the selected points.

    ```python  theme={null}
    ```
  </Accordion>

  <Accordion title="plotly-deselect" icon="code">
    Triggered when points are deselected.

    ```python  theme={null}
    ```
  </Accordion>
</AccordionGroup>

<events />
