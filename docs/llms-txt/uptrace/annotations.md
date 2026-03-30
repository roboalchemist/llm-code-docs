# Source: https://uptrace.dev/raw/features/annotations.md

# Chart annotations

> Add deployment and incident annotations to Uptrace charts via the API so teams can correlate timeline events with metric and trace changes.

Chart annotations are labels or notes added to a chart to provide additional information or context. Annotations help clarify the data presented in the chart and help the viewer understand key points or trends.

Uptrace displays annotations as square dots on the x-axis. Clicking on an annotation displays the annotation description and tags. The description field can contain markdown links to other systems with more details.

## Creating annotations

You can create annotations by sending an HTTP `POST` request to the Uptrace API:

```shell
curl -X POST https://api.uptrace.dev/api/v1/annotations \
   -H 'uptrace-dsn: <FIXME>' \
   -d '{"name":"Deployed to production", "attrs": {"service.version": "540d2ee"}}'
```

The JSON payload must include the `name` field. Other fields are optional.

<table>
<thead>
  <tr>
    <th>
      Field
    </th>
    
    <th>
      Description
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <code>
        name
      </code>
    </td>
    
    <td>
      Annotation name. Required.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        description
      </code>
    </td>
    
    <td>
      Annotation description text in Markdown format. Optional.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        color
      </code>
    </td>
    
    <td>
      Color to be used in charts, for example, <code>
        green
      </code>
      
       or <code>
        #00ff00
      </code>
      
      . Optional.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        attrs
      </code>
    </td>
    
    <td>
      Key-value metadata, for example, <code>
        {"deployment.environment": "production"}
      </code>
      
      . Optional.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        fingerprint
      </code>
    </td>
    
    <td>
      Unique string used for deduplication. Uptrace will ignore other annotations with the same fingerprint. Optional.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        time
      </code>
    </td>
    
    <td>
      Overrides annotation time in RFC3339 format. Optional.
    </td>
  </tr>
</tbody>
</table>

For example:

```shell
curl -X POST https://api.uptrace.dev/api/v1/annotations \
   -H 'uptrace-dsn: <FIXME>' \
   -d '{"name":"Deployed to production", "fingerprint": "v1.2.3", "attrs": {"service.version": "v1.2.3"}}'
```
