# Source: https://dev.writer.com/components/page.md

# Page

A container component representing a single page within the application.

<img src="https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/page.png?fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=64979436113cfd5e25e7b99c74b6599b" data-og-width="502" width="502" data-og-height="148" height="148" data-path="framework/public/components/page.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/page.png?w=280&fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=20d121ddc5b78c45f06c3baaf334cb53 280w, https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/page.png?w=560&fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=b7c2a93d2983bec1c58e9e8065c6915d 560w, https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/page.png?w=840&fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=50e8784de0ac18532f6a7f63bff8dd9d 840w, https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/page.png?w=1100&fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=4ed63d1369a4456facaf0a96259e7e92 1100w, https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/page.png?w=1650&fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=e1abc609befc05be0f628a63fa26059d 1650w, https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/page.png?w=2500&fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=17782826ee45cbc858458612e4c68e0f 2500w" />

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
      <td>Page key</td>
      <td>Identifying Key</td>
      <td>Unique identifier. It's needed to enable navigation to this Page.</td>

      <td>
        <span>-</span>
      </td>
    </tr>

    <tr>
      <td>Page mode</td>
      <td>Text</td>
      <td>-</td>

      <td>
        <ol>
          <li>Compact</li>

          <li>Wide</li>
        </ol>
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
      <td>Secondary text</td>
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
  <Accordion title="wf-keydown" icon="code">
    Captures all key activity while this page is open.

    ```python  theme={null}

    def handle_keydown(state, payload):
    # The payload is a dictionary containing the key code and modifier keys.
    # For example,
    # {
    #	"key": "ArrowDown",
    #	"ctrl_key": False,
    #	"shift_key": False,
    #	"meta_key": False
    # }

    key_activated = payload.get("key")
    delta = 0
    if key_activated == "ArrowLeft":
    	delta += -10
    elif key_activated == "ArrowRight":
    	delta += 10

    shift_key = payload.get("shift_key")
    if shift_key:
    	delta *= 2 # Shift makes it go faster

    state["position"] += delta

    ```
  </Accordion>

  <Accordion title="wf-page-open" icon="code">
    Emitted when the page is opened.

    ```python  theme={null}

    def handle_page_open(state, payload):
    page_key = payload
    state["message"] = f"The page {page_key} has been opened."

    ```
  </Accordion>
</AccordionGroup>

<events />
