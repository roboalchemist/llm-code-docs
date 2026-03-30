# Source: https://virustotal.readme.io/reference/ip-object-votes.md

# 🔀 votes

IP address' votes.

The *votes* relationship returns a list ***containing the votes for a given IP address***.

This relationship can be retrieved using the [relationships API endpoint](https://virustotal.readme.io/reference/ip-relationships). The response contains a list of [Vote](https://virustotal.readme.io/reference/vote-object) objects.

```json /ip_addresses/{ip_address}/votes
{
  "data": [
  	<VOTE_OBJECT>,
    <VOTE_OBJECT>
  ],
  "links": {
    "next": "<string>",
    "self": "<string>"
  },
  "meta": {
    	"count": <int>,
      "cursor": "<string>"
  }
}
```
```json Example
{
  "meta": {
    "count": 66,
    "cursor": "Cl4KEQoEZGF0ZRIJCPy8qrv4qvECEkVqEXN-dmlydXN0b3RhbGNsb3VkcjALEglJcEFkZHJlc3MiBzguOC44LjgMCxIEVm90ZSIQOC44LjguOC02YjY5OTk3NQwYACAB"
  },
  "data": [
    {
      "attributes": {
        "date": 1624368057,
        "verdict": "harmless",
        "value": 1
      },
      "type": "vote",
      "id": "i-8.8.8.8-2fa03e13",
      "links": {
        "self": "https://www.virustotal.com/api/v3/votes/i-8.8.8.8-2fa03e13"
      }
    },
    {
      "attributes": {
        "date": 1624354608,
        "verdict": "harmless",
        "value": 1
      },
      "type": "vote",
      "id": "i-8.8.8.8-6b699975",
      "links": {
        "self": "https://www.virustotal.com/api/v3/votes/i-8.8.8.8-6b699975"
      }
    }
  ],
  "links": {
    "self": "https://www.virustotal.com/api/v3/ip_addresses/8.8.8.8/votes?limit=2",
    "next": "https://www.virustotal.com/api/v3/ip_addresses/8.8.8.8/votes?cursor=Cl4KEQoEZGF0ZRIJCPy8qrv4qvECEkVqEXN-dmlydXN0b3RhbGNsb3VkcjALEglJcEFkZHJlc3MiBzguOC44LjgMCxIEVm90ZSIQOC44LjguOC02YjY5OTk3NQwYACAB&limit=2"
  }
}
```