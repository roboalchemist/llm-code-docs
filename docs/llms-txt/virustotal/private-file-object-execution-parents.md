# Source: https://virustotal.readme.io/reference/private-file-object-execution-parents.md

# 🔀 execution_parents

Files dropping the file during its execution

The *execution\_parents* relationship returns the list of ***all files dropping the given file during its execution***. Each of the files returned also contains contextual information (paths where the file was dropped and file type).

This relationship can be retrieved using the [relationships API endpoint](https://virustotal.readme.io/reference/private-files-relationships). The response contains a list of [private files](https://virustotal.readme.io/reference/private-files) objects.

```json /private/files/{sha256}/execution_parents
{
  "data": [
    {
      "attributes": {
        ...
      },
      "context_attributes": {
        "paths": [<string>, ...],
        "type": <string>
      }
      "type": "private_file",
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
		"count": 1
	},
	"data": [
		{
			"attributes": {
				...
			},
			"type": "private_file",
			"id": "7354b30f2e7ff0166dd73be94ec6d33b8b12f614798a6c735ede0d9e26a2b36f",
			"links": {
				"self": "https://www.virustotal.com/api/v3/private/files/7354b30f2e7ff0166dd73be94ec6d33b8b12f614798a6c735ede0d9e26a2b36f"
			},
			"context_attributes": {
				"paths": [
					"C:\\Users\\user\\AppData\\Local\\Microsoft\\Teams\\Update.exe"
				],
				"type": "Win32 EXE"
			}
		}
	],
	"links": {
		"self": "https://www.virustotal.com/api/v3/private/files/7a8c0b2d05f1d104837bc5fa31d936f608691c5937bcd2ccf05553d1a6bf4f87/execution_parents?limit=10"
	}
}
```