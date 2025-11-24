# Source: https://dev.writer.com/components/progressbar.md

# Progress Bar

A component to display a progression.

<img src="https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/progressbar.png?fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=ed78987befd23991e3d2d9758da124fa" data-og-width="816" width="816" data-og-height="111" height="111" data-path="framework/public/components/progressbar.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/progressbar.png?w=280&fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=a996aba6123b36b5ffd3fcdd113f3f05 280w, https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/progressbar.png?w=560&fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=128dfca89d0745e13e6e17d23d40a38c 560w, https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/progressbar.png?w=840&fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=8de86ac61c37e5283fd73dc2ba524081 840w, https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/progressbar.png?w=1100&fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=e494e56a131db3f61f446d1fd1b6d497 1100w, https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/progressbar.png?w=1650&fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=faa7022fef1c7d07ff564adac895a733 1650w, https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/progressbar.png?w=2500&fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=d85ef36488d9a5c3176fa1c1e91b75a0 2500w" />

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
      <td>Value</td>
      <td>Number</td>
      <td>-</td>

      <td>
        <span>-</span>
      </td>
    </tr>

    <tr>
      <td>Minimum value</td>
      <td>Number</td>
      <td>-</td>

      <td>
        <span>-</span>
      </td>
    </tr>

    <tr>
      <td>Maximum value</td>
      <td>Number</td>
      <td>-</td>

      <td>
        <span>-</span>
      </td>
    </tr>

    <tr>
      <td>Display percentage</td>
      <td>Boolean</td>
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
  <Accordion title="wf-click" icon="code">
    Triggered when the Progress bar is clicked.

    ```python  theme={null}
    def handle_progress_bar_click():
    print("The Progress bar was clicked")
    ```
  </Accordion>
</AccordionGroup>

<events />
