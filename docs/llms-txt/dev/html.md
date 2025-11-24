# Source: https://dev.writer.com/components/html.md

# HTML Element

A generic component that creates customisable HTML elements, which can serve as containers for other components.

<img src="https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/html.png?fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=e91906d9d569514e09b3ed67d6a8298c" data-og-width="574" width="574" data-og-height="568" height="568" data-path="framework/public/components/html.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/html.png?w=280&fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=1022ddfd571543677729f16bd73c007e 280w, https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/html.png?w=560&fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=f75a3e08f5c8cbf08744a5ed6b03d644 560w, https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/html.png?w=840&fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=3e2d40868145167dadf0629d52ec2f70 840w, https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/html.png?w=1100&fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=342fbea400c6e609fb7a5f630ba528db 1100w, https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/html.png?w=1650&fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=e1d64a0047dff3545421b689a2bda6cc 1650w, https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/html.png?w=2500&fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=cb054530a3b772b62550af4a8955aab1 2500w" />

You can configure the element type, styles, and attributes to fit your design requirements. You can link them to state for advanced use cases, such as custom animations.

All valid HTML tags are supported, including tags such as `iframe`, allowing you to embed external sites.

Take into account the potential risks of adding custom HTML to your app, including XSS. Be specially careful when injecting user-generated data.

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
      <td>Element</td>
      <td>Text</td>
      <td>Set the type of HTML element to create, e.g., 'div', 'section', 'span', etc.</td>

      <td>
        <span>-</span>
      </td>
    </tr>

    <tr>
      <td>Styles</td>
      <td>Object</td>
      <td>Define the CSS styles to apply to the HTML element using a JSON object or a state reference to a dictionary.</td>

      <td>
        <span>-</span>
      </td>
    </tr>

    <tr>
      <td>Attributes</td>
      <td>Object</td>
      <td>Set additional HTML attributes for the element using a JSON object or a dictionary via a state reference.</td>

      <td>
        <span>-</span>
      </td>
    </tr>

    <tr>
      <td>HTML inside</td>
      <td>Text</td>
      <td>Define custom HTML to be used inside the element. It will be wrapped in a div and rendered after children components.</td>

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
