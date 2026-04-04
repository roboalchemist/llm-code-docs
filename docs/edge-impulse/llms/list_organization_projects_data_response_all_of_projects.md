# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/list_organization_projects_data_response_all_of_projects.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# list_organization_projects_data_response_all_of_projects

## ListOrganizationProjectsDataResponseAllOfProjects

```python  theme={"system"}
class edgeimpulse_api.models.list_organization_projects_data_response_all_of_projects.ListOrganizationProjectsDataResponseAllOfProjects(
		**data: Any
)
```

Create a new model by parsing and validating input data from keyword arguments.

Raises ValidationError if the input data cannot be parsed to form a valid model.

**Parameters**

* \*\*data: Any

**Bases**

* pydantic.main.BaseModel
* pydantic.utils.Representation

**Class variables**

* `Config`

* `description: pydantic.types.StrictStr`

* `id: pydantic.types.StrictInt`

* `name: pydantic.types.StrictStr`

* `owner: pydantic.types.StrictStr`

## Static methods

### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.list_organization_projects_data_response_all_of_projects.from_dict(
		obj: dict
) ‑> edgeimpulse_api.models.list_organization_projects_data_response_all_of_projects.ListOrganizationProjectsDataResponseAllOfProjects
```

Create an instance of ListOrganizationProjectsDataResponseAllOfProjects from a dict

**Parameters**

* obj: dict

**Return**

edgeimpulse\_api.models.list\_organization\_projects\_data\_response\_all\_of\_projects.ListOrganizationProjectsDataResponseAllOfProjects

### from\_json

```python  theme={"system"}
edgeimpulse_api.models.list_organization_projects_data_response_all_of_projects.from_json(
		json_str: str
) ‑> edgeimpulse_api.models.list_organization_projects_data_response_all_of_projects.ListOrganizationProjectsDataResponseAllOfProjects
```

Create an instance of ListOrganizationProjectsDataResponseAllOfProjects from a JSON string

**Parameters**

* json\_str: str

**Return**

edgeimpulse\_api.models.list\_organization\_projects\_data\_response\_all\_of\_projects.ListOrganizationProjectsDataResponseAllOfProjects

## Methods

### to\_dict

```python  theme={"system"}
edgeimpulse_api.models.list_organization_projects_data_response_all_of_projects.to_dict(
		self
)
```

Returns the dictionary representation of the model using alias

**Parameters**

* self

### to\_json

```python  theme={"system"}
edgeimpulse_api.models.list_organization_projects_data_response_all_of_projects.to_json(
		self,
		indent=None
) ‑> str
```

Returns the JSON representation of the model using alias

**Parameters**

* self
* indent=None

**Return**

str

### to\_str

```python  theme={"system"}
edgeimpulse_api.models.list_organization_projects_data_response_all_of_projects.to_str(
		self
) ‑> str
```

Returns the string representation of the model using alias

**Parameters**

* self

**Return**

str


Built with [Mintlify](https://mintlify.com).