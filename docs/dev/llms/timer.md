# Source: https://dev.writer.com/components/timer.md

# Timer

A component that emits an event repeatedly at specified time intervals, enabling time-based refresh.

<img src="https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/framework/public/components/timer.png?fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=033c952ea8a45dc5e1bfd30ff1d1a6f4" data-og-width="424" width="424" data-og-height="125" height="125" data-path="framework/public/components/timer.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/framework/public/components/timer.png?w=280&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=ff027738eacc20f6ea59d4401f8f166d 280w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/framework/public/components/timer.png?w=560&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=bfa1b7b791516450c48da1ae90748a00 560w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/framework/public/components/timer.png?w=840&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=36daf61ec47e58db1fdc047f6ff6be5c 840w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/framework/public/components/timer.png?w=1100&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=6070b6cb9621a7487a75a655d3e65290 1100w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/framework/public/components/timer.png?w=1650&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=42adea96b9c6a7db626ffc73feaa21be 1650w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/framework/public/components/timer.png?w=2500&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=63abff5106fb9f412c49994c34a94c7a 2500w" />

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
      <td>Interval (ms)</td>
      <td>Number</td>
      <td>How much time to wait between ticks. A tick is considered finished when its event is handled.</td>

      <td>
        <span>-</span>
      </td>
    </tr>

    <tr>
      <td>Active</td>
      <td>Boolean</td>
      <td>Whether the timer should trigger tick events.</td>

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
  <Accordion title="wf-tick" icon="code">
    Emitted when the timer ticks.

    ```python  theme={null}
    def handle_timer_tick(state):

    # Increment counter when the timer ticks

    state["counter"] += 1
    ```
  </Accordion>
</AccordionGroup>

<events />
