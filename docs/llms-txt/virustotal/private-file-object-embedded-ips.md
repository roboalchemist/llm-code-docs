# Source: https://virustotal.readme.io/reference/private-file-object-embedded-ips.md

# 🔀 embedded_ips

IP addresses contained in the file

The *embedded\_ips* relationship returns the list of ***all IP addresses contained in the body of the sample***.

This relationship can be retrieved using the [relationships API endpoint](https://virustotal.readme.io/reference/private-files-relationships). The response contains a list of [IP addresses](https://virustotal.readme.io/reference/ip-object) objects.

```json /private/files/{sha256}/embedded_ips
{
  "data": [
    {
      "attributes": {
        ...
      },
      "type": "ip_address",
      "id": <string>
    }  ,
    ...
  ],
  "links": {
    "next": <string>,
    "self": <string>
  },
  "meta": {
    "count": <int>,
    "cursor": <string>
  }
}
```
```json Example
{
	"meta": {
		"count": 2,
		"cursor": "STEKLg=="
	},
	"data": [
		{
			"attributes": {
				.....
			},
			"type": "ip_address",
			"id": "8.8.8.8",
			"links": {
				"self": "http://www.virustotal.com/api/v3/ip_addresses/8.8.8.8"
			}
		}
	],
	"links": {
		"self": "http://www.virustotal.com/api/v3/private/files/079b1db08ac52c94ba8fdbab638134a6a09a510ba10a87c1541ad6c7939a5679/embedded_ips?limit=1",
		"next": "http://www.virustotal.com/api/v3/private/files/079b1db08ac52c94ba8fdbab638134a6a09a510ba10a87c1541ad6c7939a5679/embedded_ips?cursor=STEKLg%3D%3D&limit=1"
	}
}
```