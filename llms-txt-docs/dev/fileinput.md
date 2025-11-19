# Source: https://dev.writer.com/components/fileinput.md

# File Input

A user input component that allows users to upload files.

<img src="https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/fileinput.png?fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=84f95658a2dc7fe861dea099da831b44" data-og-width="559" width="559" data-og-height="232" height="232" data-path="framework/public/components/fileinput.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/fileinput.png?w=280&fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=6ccd9c483e675740c89687bed9eaa303 280w, https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/fileinput.png?w=560&fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=5ab755bd8bbb972783567363689824bf 560w, https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/fileinput.png?w=840&fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=d0c0337f8d1ab7c8b6f0a0dedd1c3c6f 840w, https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/fileinput.png?w=1100&fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=a3430dc39dcf61a91e9293f6ef9dc5ae 1100w, https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/fileinput.png?w=1650&fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=1e5f853dcd4c08ba632e8a7f0e917189 1650w, https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/fileinput.png?w=2500&fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=2d0596c16aff8bf1d3242b33f9816dd8 2500w" />

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
      <td>Allowed file types</td>
      <td>Text</td>
      <td>Provides hints for browsers to select the correct file types. You can specify extensions and MIME types separated by comma, or leave empty to accept any file.</td>

      <td>
        <span>-</span>
      </td>
    </tr>

    <tr>
      <td>Allow multiple files</td>
      <td>Boolean</td>
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
  <Accordion title="wf-file-change" icon="code">
    Capture changes to this control.

    ```python  theme={null}
    def onchange_handler(state, payload):

    # An array of dictionaries is provided in the payload
    # The dictionaries have the properties name, type and data
    # The data property is a file-like object

    uploaded_files = payload
    for i, uploaded_file in enumerate(uploaded_files):
    	name = uploaded_file.get("name")
        file_data = uploaded_file.get("data")
        with open(f"{name}-{i}.jpeg", "wb") as file_handle:
            file_handle.write(file_data)
    ```
  </Accordion>
</AccordionGroup>

<events />
