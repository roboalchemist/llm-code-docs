# Source: https://docs.fiddler.ai/api/fiddler-evals-sdk/entities/project.md

# Source: https://docs.fiddler.ai/api/fiddler-python-client-sdk/entities/project.md

# Project

Represents a project container for organizing ML models and resources.

A Project is the top-level organizational unit in Fiddler that groups related machine learning models, datasets, and monitoring configurations. Projects provide logical separation, access control, and resource management for ML monitoring workflows.

Key Features:

* **Model Organization**: Container for related ML models and their versions
* **Resource Isolation**: Separate namespaces prevent naming conflicts
* **Access Management**: Project-level permissions and access control
* **Monitoring Coordination**: Centralized monitoring and alerting configuration
* **Lifecycle Management**: Coordinated creation, updates, and deletion of resources

Project Lifecycle:

1. **Creation**: Create project with unique name within organization
2. **Model Addition**: Add models using Model.create() or Model.from\_data()
3. **Configuration**: Set up monitoring, alerts, and baseline comparisons
4. **Operations**: Publish data, monitor performance, manage alerts
5. **Maintenance**: Update configurations, add new model versions
6. **Cleanup**: Delete project when no longer needed (removes all contained resources)

## Example

```python
# Create a new project for fraud detection models
project = Project(name="fraud-detection-2024")
project = project.create()
print(f"Created project: {project.name} (ID: {project.id})")

# Add a model to the project
model = Model.from_data(
    source=training_df,
    name="xgboost_v1",
    project_id=project.id,
    task=ModelTask.BINARY_CLASSIFICATION
)
model.create()

# List all models in the project
models = list(project.models)
print(f"Project contains {len(models)} models")

# Access project models
for model_compact in project.models:

    full_model = model_compact.fetch()
    print(f"Model: {full_model.name} (Task: {full_model.task})")
```

{% hint style="info" %}
Projects are permanent containers - once created, the name cannot be changed. Deleting a project removes all contained models, datasets, and configurations. Consider the organizational structure carefully before creating projects.
{% endhint %}

Initialize a Project instance.

Creates a new Project object with the specified name. The project is not created on the Fiddler platform until .create() is called.

## Parameters

| Parameter | Type  | Required | Default | Description                                                                                                                                                                                                                                                                                              |
| --------- | ----- | -------- | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `name`    | `str` | ✗        | `None`  | Project name, must be unique within the organization. Should follow slug-like naming conventions: Use lowercase letters, numbers, hyphens, and underscores; Start with a letter or number; Be descriptive of the project's purpose; Examples: "fraud-detection", "churn\_prediction\_2024", "nlp-models" |

## Example

```python
# Create project instance for fraud detection
project = Project(name="fraud-detection-prod")

# Create project instance for experimentation
experiment_project = Project(name="ml-experiments-q1-2024")

# Create on platform
created_project = project.create()
print(f"Project created with ID: {created_project.id}")
```

{% hint style="info" %}
The project exists only locally until .create() is called. Project names cannot be changed after creation, so choose descriptive, permanent names. Consider your organization's naming conventions and project structure.
{% endhint %}

## *classmethod* get(id\_)

Retrieve a project by its unique identifier.

Fetches a project from the Fiddler platform using its UUID. This is the most direct way to retrieve a project when you know its ID.

## Parameters

| Parameter | Type   | Required | Default | Description |
| --------- | ------ | -------- | ------- | ----------- |
| `id_`     | \`UUID | str\`    | ✗       | `None`      |

## Returns

The project instance with all metadata and configuration.

**Return type:** `Project`

## Raises

* **NotFound** -- If no project exists with the specified ID.
* **ApiError** -- If there's an error communicating with the Fiddler API.

## Example

```python
# Get project by UUID
project = Project.get(id_="550e8400-e29b-41d4-a716-446655440000")
print(f"Retrieved project: {project.name}")
print(f"Created: {project.created_at}")

# Access project models
model_count = len(list(project.models))
print(f"Project contains {model_count} models")
```

{% hint style="info" %}
This method makes an API call to fetch the latest project state from the server. The returned project instance reflects the current state in Fiddler.
{% endhint %}

## *classmethod* from\_name(name)

Retrieve a project by name.

Finds and returns a project using its name within the organization. This is useful when you know the project name but not its UUID. Project names are unique within an organization, making this a reliable lookup method.

## Parameters

| Parameter | Type  | Required | Default | Description                                                                                                  |
| --------- | ----- | -------- | ------- | ------------------------------------------------------------------------------------------------------------ |
| `name`    | `str` | ✗        | `None`  | The name of the project to retrieve. Project names are unique within an organization and are case-sensitive. |

## Returns

The project instance matching the specified name.

**Return type:** `Project`

## Raises

* **NotFound** -- If no project exists with the specified name in the organization.
* **ApiError** -- If there's an error communicating with the Fiddler API.

## Example

```python
# Get project by name
project = Project.from_name(name="fraud-detection")
print(f"Found project: {project.name} (ID: {project.id})")
print(f"Created: {project.created_at}")

# Use project to list models
for model in project.models:

    print(f"Model: {model.name} v{model.version}")

    # Get project for specific environment
    prod_project = Project.from_name(name="fraud-detection-prod")
    staging_project = Project.from_name(name="fraud-detection-staging")
```

{% hint style="info" %}
Project names are case-sensitive and must match exactly. Use this method when you have a known project name from configuration or user input.
{% endhint %}

## *classmethod* list()

List all projects in the organization.

Retrieves all projects that the current user has access to within the organization. Returns an iterator for memory efficiency when dealing with many projects.

## Yields

`Project` -- Project instances for all accessible projects.

## Raises

**ApiError** -- If there's an error communicating with the Fiddler API. **Return type:** *Iterator*\[[*Project*](#project)]

## Example

```python
# List all projects
for project in Project.list():

    print(f"Project: {project.name}")
    print(f"  ID: {project.id}")
    print(f"  Created: {project.created_at}")
    print(f"  Models: {len(list(project.models))}")

    # Convert to list for counting and filtering
    projects = list(Project.list())
    print(f"Total accessible projects: {len(projects)}")

    # Find projects by name pattern
    prod_projects = [
        p for p in Project.list()
        if "prod" in p.name.lower()
    ]
    print(f"Production projects: {len(prod_projects)}")

    # Get project summaries
    for project in Project.list():

        model_count = len(list(project.models))
        print(f"{project.name}: {model_count} models")
```

{% hint style="info" %}
This method returns an iterator for memory efficiency. Convert to a list with list(Project.list()) if you need to iterate multiple times or get the total count. The iterator fetches projects lazily from the API.
{% endhint %}

## create()

Create the project on the Fiddler platform.

Persists this project instance to the Fiddler platform, making it available for adding models, configuring monitoring, and other operations. The project must have a unique name within the organization.

## Returns

This project instance, updated with server-assigned fields like : ID, creation timestamp, and other metadata.

**Return type:** `Project`

## Raises

* **Conflict** -- If a project with the same name already exists in the organization.
* **ValidationError** -- If the project configuration is invalid (e.g., invalid name format).
* **ApiError** -- If there's an error communicating with the Fiddler API.

## Example

```python
# Create a new project
project = Project(name="customer-churn-analysis")
created_project = project.create()
print(f"Created project with ID: {created_project.id}")
print(f"Created at: {created_project.created_at}")

# Project is now available for adding models
assert created_project.id is not None

# Add a model to the newly created project
model = Model.from_data(
    source=training_data,
    name="churn_model_v1",
    project_id=created_project.id
)
model.create()
```

{% hint style="info" %}
After successful creation, the project instance is updated in-place with server-assigned metadata. The same instance can be used for subsequent operations without needing to fetch it again.
{% endhint %}

## *classmethod* get\_or\_create(name)

Get an existing project by name or create a new one if it doesn't exist.

This is a convenience method that attempts to retrieve a project by name, and if not found, creates a new project with that name. Useful for idempotent project setup in automation scripts and deployment pipelines.

## Parameters

| Parameter | Type  | Required | Default | Description                                                                                               |
| --------- | ----- | -------- | ------- | --------------------------------------------------------------------------------------------------------- |
| `name`    | `str` | ✗        | `None`  | The name of the project to retrieve or create. Must follow project naming conventions (slug-like format). |

## Returns

Either the existing project with the specified name, : or a newly created project if none existed.

**Return type:** `Project`

## Raises

* **ValidationError** -- If the project name format is invalid.
* **ApiError** -- If there's an error communicating with the Fiddler API.

## Example

```python
# Safe project setup - get existing or create new
project = Project.get_or_create(name="fraud-detection-prod")
print(f"Using project: {project.name} (ID: {project.id})")

# Idempotent setup in deployment scripts
project = Project.get_or_create(name="ml-pipeline-staging")

# Add models safely - project guaranteed to exist
model = Model.from_data(
    source=data,
    name="model_v1",
    project_id=project.id
)
model.create()

# Use in configuration management
environments = ["dev", "staging", "prod"]
projects = {}
for env in environments:

    projects[env] = Project.get_or_create(name=f"fraud-detection-{env}")
```

{% hint style="info" %}
This method is idempotent - calling it multiple times with the same name will return the same project. It logs when creating a new project for visibility in automation scenarios.
{% endhint %}

## delete()

Delete the project and all its contained resources.

Permanently removes the project from the Fiddler platform, including all associated models, datasets, baselines, alerts, and monitoring configurations. This operation cannot be undone.

## Raises

* **NotFound** -- If the project doesn't exist or has already been deleted.
* **ApiError** -- If there's an error communicating with the Fiddler API.
* **PermissionError** -- If the user doesn't have permission to delete the project. **Return type:** None

{% hint style="warning" %}
This operation is irreversible and will delete ALL resources associated with the project, including:

* All models and their versions
* All datasets and published data
* All baselines and monitoring configurations
* All alert rules and notification settings
* All access permissions and project settings
  {% endhint %}

## Example

```python
# Delete a test or temporary project
test_project = Project.from_name(name="temp-experiment")
test_project.delete()
print(f"Deleted project: {test_project.name}")

# Safe deletion with confirmation
project = Project.from_name(name="old-project")
model_count = len(list(project.models))
if model_count == 0:

    project.delete()
    print("Empty project deleted")

else:
    print(f"Project has {model_count} models - deletion cancelled")

    # Cleanup projects by pattern
    for project in Project.list():

        if project.name.startswith("temp-"):
            print(f"Deleting temporary project: {project.name}")
            project.delete()
```

{% hint style="info" %}
Requires Fiddler platform version 25.2.0 or higher. Consider exporting important data or configurations before deletion. There is no recovery mechanism once a project is deleted.
{% endhint %}

## *property* models *: Iterator\[ModelCompact]*

Fetch all the models of this project.

## Yields

[`ModelCompact`](https://docs.fiddler.ai/api/fiddler-python-client-sdk/entities/model-compact) -- Lightweight model objects for this project.
