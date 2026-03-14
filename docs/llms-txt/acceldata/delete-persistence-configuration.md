# Source: https://docs.acceldata.io/api/delete-persistence-configuration.md

# Delete Persistence Configuration

Deletes a persistence configuration.

### Endpoint

```bash
DELETE /catalog-server/api/persistence/configs/{id}
```



### Path Parameter

| Parameter | Description | 
| ---- | ---- | 
| id | Configuration ID | 


### Sample Request

```bash
curl -X DELETE "https://{HOST}/catalog-server/api/persistence/configs/6" \
  -H "accessKey: {ACCESS_KEY}" \
  -H "secretKey: {SECRET_KEY}"
```



**Response (204 No Content):** Empty response on success.

NOTE 

A configuration cannot be deleted if:

- It is set as the tenant default
- It is currently referenced by policies