# Source: https://docs.datadoghq.com/dashboards/guide/screenboard-api-doc.md

---
title: Screenboard API
description: >-
  DEPRECATED - API for the deprecated Screenboard endpoint. Use the Dashboard
  endpoint for dashboard operations instead.
breadcrumbs: Docs > Dashboards > Graphing Guides > Screenboard API
---

# Screenboard API

{% alert level="warning" %}
This endpoint is outdated. Use the [new Dashboard endpoint](https://docs.datadoghq.com/api/v1/dashboards/) instead.
{% /alert %}

The `Screenboard` endpoint allows you to programmatically create, update, delete, and query screenboards.

## Create a screenboard{% #create-a-screenboard %}

### Signature{% #signature %}

`POST https://api.datadoghq.com/api/v1/screen`

### Arguments{% #arguments %}

- **`board_title`** [*required*]: The name of the dashboard.
- **`description`** [*optional*, *default*=**None**]: A description of the dashboard's content.
- **`widgets`** [*required*]: A list of widget definitions. To get a widget definition, use the *JSON tab* in the widget configuration UI.
- **`template_variables`** [*optional*, *default*=**None**]: A list of template variables for using Dashboard templating.
- **`read_only`** [*optional*, *default*=**False**]: The read-only status of the screenboard.

### Examples{% #examples %}

{% tab title="Python" %}

```python
from datadog import initialize, api

options = {
    'api_key': '<DATADOG_API_KEY>',
    'app_key': '<DATADOG_APPLICATION_KEY>'
}

initialize(**options)

board_title = "My Screenboard"
description = "An informative screenboard."
width = 1024
widgets = [{
    "type": "image",
    "height": 20,
    "width": 32,
    "y": 7,
    "x": 32,
    "url": "https://path/to/image.jpg"
}]
template_variables = [{
    "name": "host1",
    "prefix": "host",
    "default": "host:my-host"
}]

api.Screenboard.create(board_title=board_title,
                       description=description,
                       widgets=widgets,
                       template_variables=template_variables,
                       width=width)
```

{% /tab %}

{% tab title="Ruby" %}

```ruby
require 'rubygems'
require 'dogapi'

api_key='<DATADOG_API_KEY>'
app_key='<DATADOG_APPLICATION_KEY>'

dog = Dogapi::Client.new(api_key, app_key)

board = {
    "width" => 1024,
    "height" => 768,
    "board_title" => "dogapi test",
    "widgets" => [
        {
          "type" => "image",
          "height" => 20,
          "width" => 32,
          "y" => 7,
          "x" => 32,
          "url" => "https://path/to/image.jpg"
        }
    ]
}

result = dog.create_screenboard(board)
```

{% /tab %}

{% tab title="Bash" %}

```bash
api_key=<DATADOG_API_KEY>
app_key=<DATADOG_APPLICATION_KEY>

curl -X POST -H "Content-type: application/json" \
-d '{
        "width": 1024,
        "height": 768,
        "board_title": "dogapi test",
        "widgets": [
            {
              "type": "image",
              "height": 20,
              "width": 32,
              "y": 7,
              "x": 32,
              "url": "https://path/to/image.jpg"
            }
        ]
}' \
"https://api.datadoghq.com/api/v1/screen?api_key=${DD_CLIENT_API_KEY}&application_key=${DD_CLIENT_APP_KEY}"
```

{% /tab %}

## Update a screenboard{% #update-a-screenboard %}

### Signature{% #signature-1 %}

`PUT https://api.datadoghq.com/api/v1/screen/<SCREEENBOARD_ID>`

### Arguments{% #arguments-1 %}

- **`board_title`** [*required*]: The name of the dashboard.
- **`description`** [*optional*, *default*=**None**]: A description of the dashboard's content.
- **`widgets`** [*required*]: A list of widget definitions. To get a widget definition, use the *JSON tab* in the widget configuration UI.
- **`template_variables`** [*optional*, *default*=**None**]: A list of template variables for using Dashboard templating.
- **`width`** [*optional*, *default*=**None**]: Screenboard width in pixels
- **`height`** [*optional*, *default*=**None**]: Screenboard height in pixels.
- **`read_only`** [*optional*, *default*=**False**]: The read-only status of the screenboard.

### Examples{% #examples-1 %}

{% tab title="Python" %}

```python
from datadog import initialize, api

options = {
    'api_key': '<DATADOG_API_KEY>',
    'app_key': '<DATADOG_APPLICATION_KEY>'
}

initialize(**options)
board_id = 2551
board_title = "My Screenboard"
description = "An informative screenboard."
width = 1024
widgets = [{
    "type": "image",
    "height": 20,
    "width": 32,
    "y": 7,
    "x": 32,
    "url": "https://path/to/image.jpg"
}]
template_variables = [{
    "name": "host1",
    "prefix": "host",
    "default": "host:my-host"
}]

api.Screenboard.update(board_id,
                       board_title=board_title,
                       description=description,
                       widgets=widgets,
                       template_variables=template_variables,
                       width=width)
```

{% /tab %}

{% tab title="Ruby" %}

```ruby
require 'rubygems'
require 'dogapi'

api_key = '<DATADOG_API_KEY>'
app_key = '<DATADOG_APPLICATION_KEY>'

dog = Dogapi::Client.new(api_key, app_key)

board_id = 7953
board = {
    "width" => 1024,
    "height" => 768,
    "board_title" => "dogapi test",
    "widgets" => [{
        "type" => "image",
        "height" => 20,
        "width" => 32,
        "y" => 7,
        "x" => 32,
        "url" => "https://path/to/image.jpg"
    }]
}

result = dog.update_screenboard(board_id, board)
```

{% /tab %}

{% tab title="Bash" %}

```bash
api_key=<DATADOG_API_KEY>
app_key=<DATADOG_APPLICATION_KEY>

curl -X PUT -H "Content-type: application/json" \
-d '{
        "width": 1024,
        "height": 768,
        "board_title": "dogapi test",
        "widgets": [
            {
              "type": "image",
              "height": 20,
              "width": 32,
              "y": 7,
              "x": 32,
              "url": "https://path/to/image.jpg"
            }
        ]
}' \
"https://api.datadoghq.com/api/v1/screen/${board_id}?api_key=${DD_CLIENT_API_KEY}&application_key=${DD_CLIENT_APP_KEY}"
```

{% /tab %}

## Delete a screenboard{% #delete-a-screenboard %}

Delete an existing screenboard. *This endpoint takes no JSON arguments.*

### Signature{% #signature-2 %}

`DELETE https://api.datadoghq.com/api/v1/screen/<SCREEENBOARD_ID>`

### Arguments{% #arguments-2 %}

*This endpoint takes no JSON arguments.*

### Examples{% #examples-2 %}

{% tab title="Python" %}

```python
from datadog import initialize, api

options = {
    'api_key': '<DATADOG_API_KEY>',
    'app_key': '<DATADOG_APPLICATION_KEY>'
}

initialize(**options)

api.Screenboard.delete(811)
```

{% /tab %}

{% tab title="Ruby" %}

```ruby
require 'rubygems'
require 'dogapi'

api_key = '<DATADOG_API_KEY>'
app_key = '<DATADOG_APPLICATION_KEY>'

dog = Dogapi::Client.new(api_key, app_key)

board_id = '2534'
result = dog.delete_screenboard(board_id)
```

{% /tab %}

{% tab title="Bash" %}

```bash
api_key=<DATADOG_API_KEY>
app_key=<DATADOG_APPLICATION_KEY>
board_id=2471

# Create a screenboard to delete
board_id=$(curl -X POST -H "Content-type: application/json" \
-d '{
        "width": 1024,
        "height": 768,
        "board_title": "dogapi tests",
        "widgets": [
            {
              "type": "image",
              "height": 20,
              "width": 32,
              "y": 7,
              "x": 32,
              "url": "https://path/to/image.jpg"
            }
        ]
  }' \
"https://api.datadoghq.com/api/v1/screen?api_key=${DD_CLIENT_API_KEY}&application_key=${DD_CLIENT_APP_KEY}" | jq '.id')

curl -X DELETE \
"https://api.datadoghq.com/api/v1/screen/${board_id}?api_key=${DD_CLIENT_API_KEY}&application_key=${DD_CLIENT_APP_KEY}"
```

{% /tab %}

## Get a screenboard{% #get-a-screenboard %}

Fetch an existing screenboard definition.

### Signature{% #signature-3 %}

`GET https://api.datadoghq.com/api/v1/screen/<SCREEENBOARD_ID>`

### Arguments{% #arguments-3 %}

*This endpoint takes no JSON arguments.*

### Examples{% #examples-3 %}

{% tab title="Python" %}

```python
from datadog import initialize, api

options = {
    'api_key': '<DATADOG_API_KEY>',
    'app_key': '<DATADOG_APPLICATION_KEY>'
}

initialize(**options)

api.Screenboard.get(811)
```

{% /tab %}

{% tab title="Ruby" %}

```ruby
require 'rubygems'
require 'dogapi'

api_key = '<DATADOG_API_KEY>'
app_key = '<DATADOG_APPLICATION_KEY>'

dog = Dogapi::Client.new(api_key, app_key)

board_id = '6334'
result = dog.get_screenboard(board_id)
```

{% /tab %}

{% tab title="Bash" %}

```bash
api_key=<DATADOG_API_KEY>
app_key=<DATADOG_APPLICATION_KEY>
board_id=6334

# Create a screenboard to get
board_id=$(curl -X POST -H "Content-type: application/json" \
-d '{
        "width": 1024,
        "height": 768,
        "board_title": "dogapi tests",
        "widgets": [
            {
              "type": "image",
              "height": 20,
              "width": 32,
              "y": 7,
              "x": 32,
              "url": "https://path/to/image.jpg"
            }
        ]
  }' \
"https://api.datadoghq.com/api/v1/screen?api_key=${DD_CLIENT_API_KEY}&application_key=${DD_CLIENT_APP_KEY}" | jq '.id')

curl -X GET \
"https://api.datadoghq.com/api/v1/screen/${board_id}?api_key=${DD_CLIENT_API_KEY}&application_key=${DD_CLIENT_APP_KEY}"
```

{% /tab %}

## Get all screenboards{% #get-all-screenboards %}

Fetch all of your screenboards' definitions.

### Signature{% #signature-4 %}

`GET https://api.datadoghq.com/api/v1/screen`

### Arguments{% #arguments-4 %}

*This endpoint takes no JSON arguments.*

### Examples{% #examples-4 %}

{% tab title="Python" %}

```python
from datadog import initialize, api

options = {
    'api_key': '<DATADOG_API_KEY>',
    'app_key': '<DATADOG_APPLICATION_KEY>'
}

initialize(**options)

api.Screenboard.get_all()
```

{% /tab %}

{% tab title="Ruby" %}

```ruby
require 'rubygems'
require 'dogapi'

api_key = '<DATADOG_API_KEY>'
app_key = '<DATADOG_APPLICATION_KEY>'

dog = Dogapi::Client.new(api_key, app_key)

result = dog.get_all_screenboards()
```

{% /tab %}

{% tab title="Bash" %}

```bash
api_key=<DATADOG_API_KEY>
app_key=<DATADOG_APPLICATION_KEY>

curl -X GET "https://api.datadoghq.com/api/v1/screen?api_key=${DD_CLIENT_API_KEY}&application_key=${DD_CLIENT_APP_KEY}"
```

{% /tab %}
