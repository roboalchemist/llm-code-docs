# Source: https://docs.port.io/api-reference/delete-user-memory-records.md

# Delete user memory records

```
DELETE 
/v1/memory
```

This route allows you to delete your own memory records. You can either delete all memories at once or specify individual record IDs to delete.<br /><br />**Note:** Deletion is asynchronous and may take time to complete. Deleted records might still appear in list requests briefly. If deletion fails for some records, the response will indicate which deletions failed.

## Request[â](#request "Direct link to request")

## Responses[â](#responses "Direct link to Responses")

* 200
* 400
* 401

Successfully initiated deletion

Invalid request - must provide either deleteAll or recordIds

Unauthorized
