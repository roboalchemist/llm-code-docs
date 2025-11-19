# Source: https://dev.writer.com/framework/dataframe.md

# Source: https://dev.writer.com/components/dataframe.md

# DataFrame

A component to display Pandas DataFrames.

<img src="https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/dataframe.png?fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=c444e32b85b12ede5bb8e41a99eca8f5" data-og-width="1828" width="1828" data-og-height="322" height="322" data-path="framework/public/components/dataframe.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/dataframe.png?w=280&fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=3b069ce9ae8f7386e35eefa67c4452ca 280w, https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/dataframe.png?w=560&fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=6bfd6416971372d136393f692e24555f 560w, https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/dataframe.png?w=840&fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=07ffc62165feb35a26523dc1b777ea3a 840w, https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/dataframe.png?w=1100&fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=5ce50e3d77925cf6492a6b6be45d28b1 1100w, https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/dataframe.png?w=1650&fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=7c0b06df3ab0818c8d1f07d1614f8c45 1650w, https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/dataframe.png?w=2500&fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=fe00981ff149d389d24da5a244f5ef25 2500w" />

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
      <td>Data</td>
      <td>Text</td>
      <td>Must be a state reference to a Pandas dataframe or PyArrow table. Alternatively, a URL for an Arrow IPC file.</td>

      <td>
        <span>-</span>
      </td>
    </tr>

    <tr>
      <td>Show index</td>
      <td>Boolean</td>
      <td>Shows the dataframe's index. If an Arrow table is used, shows the zero-based integer index.</td>

      <td>
        <span>-</span>
      </td>
    </tr>

    <tr>
      <td>Enable search</td>
      <td>Boolean</td>
      <td>-</td>

      <td>
        <span>-</span>
      </td>
    </tr>

    <tr>
      <td>Enable adding a record</td>
      <td>Boolean</td>
      <td>-</td>

      <td>
        <span>-</span>
      </td>
    </tr>

    <tr>
      <td>Enable updating a record</td>
      <td>Boolean</td>
      <td>-</td>

      <td>
        <span>-</span>
      </td>
    </tr>

    <tr>
      <td>Enable download</td>
      <td>Boolean</td>
      <td>Allows the user to download the data as CSV.</td>

      <td>
        <span>-</span>
      </td>
    </tr>

    <tr>
      <td>Actions</td>
      <td>Key-Value</td>
      <td>Define rows actions</td>

      <td>
        <span>-</span>
      </td>
    </tr>

    <tr>
      <td>Enable markdown</td>
      <td>Boolean</td>
      <td>If active, the output will be sanitized; unsafe elements will be removed.</td>

      <td>
        <span>-</span>
      </td>
    </tr>

    <tr>
      <td>Display row count</td>
      <td>Number</td>
      <td>Specifies how many rows to show simultaneously.</td>

      <td>
        <span>-</span>
      </td>
    </tr>

    <tr>
      <td>Wrap text</td>
      <td>Boolean</td>
      <td>Not wrapping text allows for an uniform grid, but may be inconvenient if your data contains longer text fields.</td>

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
      <td>Accent</td>
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
      <td>Background</td>
      <td>Color</td>
      <td>-</td>

      <td>
        <span>-</span>
      </td>
    </tr>

    <tr>
      <td>Font style</td>
      <td>Text</td>
      <td>-</td>

      <td>
        <ol>
          <li>normal</li>

          <li>monospace</li>
        </ol>
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
  <Accordion title="wf-dataframe-add" icon="code">
    Capture adding a row.

    ```python  theme={null}
    # Subscribe this event handler to the `wf-dataframe-add` event
    #
    # more on : https://dev.writer.com/framework/dataframe
    def on_record_add(state, payload):
    payload['record']['sales'] = 0 # default value inside the dataframe
    state['mydf'].record_add(payload) # should contain an EditableDataFrame instance
    ```
  </Accordion>

  <Accordion title="wf-dataframe-update" icon="code">
    Capture a cell change.

    ```python  theme={null}
    # Subscribe this event handler to the `wf-dataframe-update` event
    #
    # more on : https://dev.writer.com/framework/dataframe
    def on_record_change(state, payload):
    state['mydf'].record_update(payload) # should contain an EditableDataFrame instance
    ```
  </Accordion>

  <Accordion title="wf-dataframe-action" icon="code">
    Remove or open a row.

    ```python  theme={null}
    # Subscribe this event handler to the `wf-dataframe-action` event
    #
    # more on : https://dev.writer.com/framework/dataframe
    def on_record_action(state, payload):
    # state['mydf'] should contains an EditableDataFrame instance
    record_index = payload['record_index']
    if payload['action'] == 'remove':
    	state['mydf'].record_remove(payload) # should contain an EditableDataFrame instance
    if payload['action'] == 'open':
    	state['record'] = state['mydf'].record(record_index) # dict representation of record
    ```
  </Accordion>
</AccordionGroup>

<events />
