# Source: https://docs.acceldata.io/api/get-template-variables.md

# Get Template Variables

Returns the list of available template variables that can be used in persistence path templates.

### Endpoint

```bash
GET /catalog-server/api/persistence/configs/variables
```



### Sample Request

```bash
curl -X GET "https://{HOST}/catalog-server/api/persistence/configs/variables" \
  -H "accessKey: {ACCESS_KEY}" \
  -H "secretKey: {SECRET_KEY}"
```



### Response (200 OK)

Returns an array of available variables with `name`, `syntax`, and `description` for each.