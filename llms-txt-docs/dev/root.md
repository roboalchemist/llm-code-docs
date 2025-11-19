# Source: https://dev.writer.com/components/root.md

# Root

The root component of the application, which serves as the starting point of the component hierarchy.

<img src="https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/root.png?fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=ad1add9fb4d2198426dd7c920bd67acd" data-og-width="506" width="506" data-og-height="152" height="152" data-path="framework/public/components/root.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/root.png?w=280&fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=d1fc47e94accb88574737573c94f509a 280w, https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/root.png?w=560&fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=69d34321713b2ca13074e07dafab55e6 560w, https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/root.png?w=840&fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=b5060da8166642293265309b7bc552bc 840w, https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/root.png?w=1100&fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=d5efd3c673e13e34781a9d70bf406007 1100w, https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/root.png?w=1650&fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=d964f2858549ccb2154eeb38a0655284 1650w, https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/root.png?w=2500&fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=78257c4fba84086d247f5ad9c350c732 2500w" />

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
      <td>App name</td>
      <td>Text</td>
      <td>The app name will be shown in the browser's title bar.</td>

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

    <tr>
      <td>Button</td>
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
      <td>Accent</td>
      <td>Color</td>
      <td>-</td>

      <td>
        <span>-</span>
      </td>
    </tr>

    <tr>
      <td>Padding</td>
      <td>Padding</td>
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
      <td>Button text</td>
      <td>Color</td>
      <td>-</td>

      <td>
        <span>-</span>
      </td>
    </tr>

    <tr>
      <td>Emptiness</td>
      <td>Color</td>
      <td>Page background color</td>

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
      <td>Secondary text</td>
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
      <td>Content alignment (V)</td>
      <td>Align (V)</td>
      <td>-</td>

      <td>
        <span>-</span>
      </td>
    </tr>

    <tr>
      <td>Content alignment (H)</td>
      <td>Align (H)</td>
      <td>-</td>

      <td>
        <span>-</span>
      </td>
    </tr>

    <tr>
      <td>Content width</td>
      <td>Width</td>
      <td>Configure content width using CSS units, e.g. 100px, 50%, 10vw, etc.</td>

      <td>
        <span>-</span>
      </td>
    </tr>
  </tbody>
</table>

## Events

<AccordionGroup>
  <Accordion title="wf-app-open" icon="code">
    Captures the first application load, including page key and route vars.

    ```python  theme={null}
    def handle_app_open(state):
    # The payload is a dictionary with the page key and all the route variables in the URL hash.
    # For example, if the current URL is http://localhost:3000/#/animal=duck&colour=yellow
    # you will get the following dictionary
    # {
    #   "page_key": "main",
    #	  "route_vars": {
    #		  "animal": "duck",
    #		  "colour": "yellow"
    #	  }
    # }

    page_key = payload.get("page_key")
    route_vars = payload.get("route_vars")
    ```
  </Accordion>

  <Accordion title="wf-hashchange" icon="code">
    Capture changes to the URL hash, including page key and route vars.

    ```python  theme={null}
    def handle_hashchange(state, payload):
    # The payload is a dictionary with the page key and all the route variables in the URL hash.
    # For example, if the current URL is http://localhost:3000/#main/animal=duck&colour=yellow
    # you will get the following dictionary
    # {
    #	  "page_key": "main",
    #	  "route_vars": {
    #		  "animal": "duck",
    #		  "colour": "yellow"
    #	  }
    # }

    page_key = payload.get("page_key")
    route_vars = payload.get("route_vars")

    if not route_vars:
    	return

    if route_vars.get("animal") == "duck":
    	state["message"] = "You've navigated to the Duck zone."
    else:
    	state["message"] = "You're not in the Duck zone.
    ```
  </Accordion>
</AccordionGroup>

<events />
