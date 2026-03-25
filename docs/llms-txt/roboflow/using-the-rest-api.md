# Source: https://docs.roboflow.com/developer/rest-api/using-the-rest-api.md

# Using the REST API

You can retrieve information about your Roboflow projects and datasets using the REST API.

* `/` - the [Root route](https://docs.roboflow.com/developer/rest-api/broken-reference) can be used to validate your API Key and find your workspace ID.
* `/:workspace` - the [Workspace route](https://docs.roboflow.com/developer/rest-api/broken-reference) gives you information about your workspace and a list of its projects.
* `/:workspace/:project` - the Project route shows information about a project and its versions.
* `/:workspace/:project/:version` - the Version route surfaces information about a version, its trained model (if present), and exported datasets.
* `/:workspace/:project/:version/:format` - the Format route is where you go to retrieve a download link for a zipped dataset in a particular [export format](https://roboflow.com/formats).

### Routes

The data structure in Roboflow is largely hierarchical; the API layout matches this. [Workspaces](https://docs.roboflow.com/developer/rest-api/broken-reference) contain Projects which contain Versions which have trained models and are exported in various Formats.

### Root Endpoint

At the top level (`https://api.roboflow.com/`), you can verify your `api_key` is working. The response will tell you which `workspace` owns the key.

Example for the `roboflow` workspace:

```bash
$ curl "https://api.roboflow.com/?api_key=$ROBOFLOW_API_KEY"
{
    "welcome": "Welcome to the Roboflow API.",
    "instructions": "You are successfully authenticated.",
    "docs": "https://docs.roboflow.com",
    "workspace": "roboflow"
}
```

You can drill down into this workspace with its [Workspace endpoint](https://docs.roboflow.com/developer/rest-api/broken-reference) to access information about your projects.
