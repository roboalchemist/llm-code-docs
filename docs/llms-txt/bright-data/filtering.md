# Source: https://docs.brightdata.com/api-reference/serp/google-maps/filtering.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Filtering

```txt wrap theme={null}
https://www.google.com/maps/search/hotels+new+york/?brd_accomodation_type=vacation_rentals
```

## Parameters

<ParamField path="q" type="string" required>
  The search path parameter. Specifies the keyword or phrase you want to search for on Google Maps.
</ParamField>

<ParamField query="brd_accomodation_type" type="string">
  Accomodation type: Hotels or Vacation Rentals.

  > **Examples:**\
  > `brd_accomodation_type=hotels` (default) - search for Hotels \
  > `brd_accomodation_type=vacation_rentals` - search for Vacation Rentals

  ```txt wrap theme={null}
  https://www.google.com/maps/search/hotels+new+york/?brd_accomodation_type=vacation_rentals
  ```
</ParamField>

<RequestExample>
  ```shell cURL highlight={6} theme={null}
    curl -X POST https://api.brightdata.com/request \
    --header "Content-Type: application/json" \
    --header "Authorization: Bearer API_KEY" \
    --data '{
      "zone": "serp_api1",
      "url": "https://www.google.com/maps/search/hotels+new+york/?brd_accomodation_type=vacation_rentals",
      "format": "raw"
    }'
  ```

  ```shell Native proxy highlight={4} theme={null}
  curl --proxy brd.superproxy.io:33335 \
    --proxy-user CUSTOMER_USERNAME:CUSTOMER_PASSWORD \
    --ssl-no-revoke \
    "https://www.google.com/maps/search/hotels+new+york/?brd_accomodation_type=vacation_rentals"
  ```

  ```js Node.js highlight={10} theme={null}
  (async () => {
    const response = await fetch('https://api.brightdata.com/request', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer API_KEY'
      },
      body: JSON.stringify({
        zone: 'serp_api1',
        url: 'https://www.google.com/maps/search/hotels+new+york/?brd_accomodation_type=vacation_rentals',
        format: 'raw'
      })
    });
    
    const data = await response.text();
    console.log(data);
  })();
  ```

  ```python Python highlight={11} theme={null}
  import requests

  # API Configuration
  headers = {
      'Content-Type': 'application/json',
      'Authorization': 'Bearer API_KEY',
  }

  payload = {
      'zone': 'serp_api1',
      'url': 'https://www.google.com/maps/search/hotels+new+york/?brd_accomodation_type=vacation_rentals',
      'format': 'raw'
  }

  # Make the request
  response = requests.post(
      'https://api.brightdata.com/request', 
      json=payload, 
      headers=headers
  )

  print(response.text)
  ```
</RequestExample>
