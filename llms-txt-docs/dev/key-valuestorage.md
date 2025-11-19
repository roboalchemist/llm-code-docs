# Source: https://dev.writer.com/blueprints/key-valuestorage.md

# Key-Value Storage

Allows to store data between sessions. Uses unique keys (names) to identify the data. Keys can only contain alphanumeric characters, underscores and hyphens

## Fields

<table className="blueprintFields">
  <thead>
    <th>Name</th>
    <th>Type</th>
    <th>Control</th>
    <th>Default</th>
    <th>Description</th>
    <th>Options</th>
    <th>Validation</th>
  </thead>

  <tbody>
    <tr>
      <td>Action</td>
      <td>Text</td>
      <td>-</td>

      <td>
        <code>Save</code>
      </td>

      <td>-</td>

      <td>
        <ul>
          <li>Save - Save</li>

          <li>Get - Get</li>

          <li>Delete - Delete</li>
        </ul>
      </td>

      <td>
        <span>-</span>
      </td>
    </tr>

    <tr>
      <td>Key</td>
      <td>Text</td>
      <td>-</td>

      <td>
        <span>-</span>
      </td>

      <td>-</td>

      <td>
        <span>-</span>
      </td>

      <td>
        <span>-</span>
      </td>
    </tr>

    <tr>
      <td>Value</td>
      <td>Text</td>
      <td>Textarea</td>

      <td>
        <span>-</span>
      </td>

      <td>-</td>

      <td>
        <span>-</span>
      </td>

      <td>
        <span>-</span>
      </td>
    </tr>
  </tbody>
</table>

## End states

Below are the possible end states of the block call.

<table className="blueprintFields">
  <thead>
    <th>Name</th>
    <th>Field</th>
    <th>Type</th>
    <th>Description</th>
  </thead>

  <tbody>
    <tr>
      <td>Success</td>
      <td>-</td>
      <td>success</td>
      <td>The request was successful.</td>
    </tr>

    <tr>
      <td>Error</td>
      <td>-</td>
      <td>error</td>
      <td>The request wasn't successful.</td>
    </tr>
  </tbody>
</table>
