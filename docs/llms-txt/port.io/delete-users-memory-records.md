# Source: https://docs.port.io/api-reference/delete-users-memory-records.md

# Delete users memory records

```
DELETE 
/v1/memory/users
```

This route allows organization administrators to delete memory records for specific users.<br /><br />**Note:** Deletion is asynchronous and may take time to complete. If deletion fails for some users, the response will indicate which deletions failed.

## Request[â](#request "Direct link to request")

## Responses[â](#responses "Direct link to Responses")

* 200
* 401
* 403

Successfully initiated deletion

Unauthorized

Forbidden - Admin permissions required
