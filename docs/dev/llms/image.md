# Source: https://dev.writer.com/components/image.md

# Image

A component to display images.

<img src="https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/image.png?fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=015843c9ddf0cefab72faf8e53e6adc5" data-og-width="668" width="668" data-og-height="1034" height="1034" data-path="framework/public/components/image.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/image.png?w=280&fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=f89d19ff9d22169f5c6b00fffb9c0304 280w, https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/image.png?w=560&fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=ca9f113d1fd32ba1a68a595749e58a58 560w, https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/image.png?w=840&fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=67497f7cc842c394fc845fef4af203d2 840w, https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/image.png?w=1100&fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=1d14bbbb692dfca3c76f900780c403e6 1100w, https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/image.png?w=1650&fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=a0763b0b488dc29191eb4990bee02bdd 1650w, https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/image.png?w=2500&fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=2fc7d359796e3ec289d2d18c25edd40b 2500w" />

Use your app's static folder to serve images directly. For example, `static/my_image.png`.

Alternatively, pass a Matplotlib figure via state.

`state[&quot;my_fig&quot;] = fig` and then setting the *Image* source to `@{fig}`

You can also use packed files or bytes:

`state[&quot;img_b&quot;] = wf.pack_bytes(img_bytes, &quot;image/png&quot;)`

`state[&quot;img_f&quot;] = wf.pack_file(img_file, &quot;image/png&quot;)`

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
      <td>A valid URL. Alternatively, you can provide a state reference to a Matplotlib figure or a packed file.</td>

      <td>
        <span>-</span>
      </td>
    </tr>

    <tr>
      <td>Caption</td>
      <td>Text</td>
      <td>Leave blank to hide.</td>

      <td>
        <span>-</span>
      </td>
    </tr>

    <tr>
      <td>Max width (px)</td>
      <td>Number</td>
      <td>-</td>

      <td>
        <span>-</span>
      </td>
    </tr>

    <tr>
      <td>Max height (px)</td>
      <td>Number</td>
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
    def click_handler(state):

    # Increment counter when the image is clicked

    state["counter"] += 1
    ```
  </Accordion>
</AccordionGroup>

<events />
