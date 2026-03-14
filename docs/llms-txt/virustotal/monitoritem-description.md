# Source: https://virustotal.readme.io/reference/monitoritem-description.md

# Monitor Items

Details about objects stored in the VirusTotal Monitor service.

A MonitorItem object refers to a file or folder stored in VirusTotal Monitor and it is referenced via an ID. Using the right API calls it is not necessary to know how MonitorItem IDs are built, however, under certain circumstances you might find it easier to interact with the service by composing the IDs yourself.

A MonitorItem ID is made up of a base64 encoded string containing an utf8 formatted string following this pattern:

```
vtmonitor-v1://{owner_id}{path}
```

`{owner_id}` refers to the VirusTotal group your user belongs to and to whom the Monitor privilege was granted. This information can be retrieved using the [GET /users/{id}](#user) endpoint with your user ID. The name of the group from which your user inherits its Monitor privileges will appear in the the `inherited_from` field of the `monitor` privilege.

```json
{
  "type": "user",
  "id": "wcoyote",
  "links": {
    "self": "https://www.virustotal.com/api/v3/users/wcoyote"
  },
  "data": {
    "attributes": {
      "privileges": {
        "monitor": {
          "granted": true,
          "inherited_from": "acme"
        },
      }
    }  
  }
}
```