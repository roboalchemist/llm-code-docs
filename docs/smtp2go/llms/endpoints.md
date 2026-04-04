# Source: https://developers.smtp2go.com/docs/endpoints.md

# Endpoints

## :earth\_americas: Base URL

The SMTP2GO API's base URL is: **`https://api.smtp2go.com/v3/`**

For example, an API call to /stats/email\_summary will be reachable at: `https://api.smtp2go.com/v3/stats/email_summary`

## US, EU and AU Endpoints

Aside from the Global URL, requests may be prefixed with one of the following base URL's:

| Region              | Base URL                         |
| :------------------ | :------------------------------- |
| Global              | `https://api.smtp2go.com/v3/`    |
| US (United States)  | `https://us-api.smtp2go.com/v3/` |
| EU (European Union) | `https://eu-api.smtp2go.com/v3/` |
| AU (Oceania)        | `https://au-api.smtp2go.com/v3/` |

If you send your requests to the 'Global' endpoint, the API will automatically choose the US, EU or AU endpoint based on which is closer to the request origin.