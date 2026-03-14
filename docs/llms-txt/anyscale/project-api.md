# Source: https://docs.anyscale.com/reference/project-api.md

# Project API Reference

[View Markdown](/reference/project-api.md)

# Project API Reference

#### Customer-hosted cloud features[​](#customer-hosted-only "Direct link to Customer-hosted cloud features")

note

Some features are only available on customer-hosted clouds. Reach out to <support@anyscale.com> for info.

## Project CLI[​](#project-cli "Direct link to Project CLI")

### `anyscale project get`[​](#anyscale-project-get "Direct link to anyscale-project-get")

**Usage**

`anyscale project get [OPTIONS]`

Get details of a project.

**Options**

* **`--id/-i`**: ID of the project.
* **`--json/-j`**: Output the details in a structured JSON format.

#### Examples[​](#examples "Direct link to Examples")

* CLI

```
$ anyscale project get --id my-project-id
```

### `anyscale project list`[​](#anyscale-project-list "Direct link to anyscale-project-list")

**Usage**

`anyscale project list [OPTIONS]`

List all projects with optional filters.

**Options**

* **`--name/-n`**: A string to filter projects by name.
* **`--creator/-u`**: The ID of a creator to filter projects.
* **`--cloud/-c`**: The ID of a parent cloud to filter projects.
* **`--include-defaults/--exclude-defaults`**: Whether to include default projects.
* **`--max-items`**: The maximum number of projects to return.
* **`--page-size`**: The number of projects to return per page.
* **`--sort`**: Sort by FIELD (prefix with '-' for desc). Allowed: NAME
* **`--interactive/--no-interactive`**: Use interactive paging.
* **`--json/-j`**: Output the list in a structured JSON format.

#### Examples[​](#examples-1 "Direct link to Examples")

* CLI

```
$ anyscale project list --include-defaults --non-interactive --max-items 2
```

### `anyscale project create`[​](#anyscale-project-create "Direct link to anyscale-project-create")

**Usage**

`anyscale project create [OPTIONS]`

Create a new project.

**Options**

* **`--name/-n`**: Name of the project.
* **`--cloud/-c`**: Parent cloud ID for the project.
* **`--description/-d`**: Description of the project.
* **`--initial-cluster-config/-f`**: Initial cluster config for the project.

#### Examples[​](#examples-2 "Direct link to Examples")

* CLI

```
$ anyscale project create --name "my-project" --cloud "my-cloud-id"
```

### `anyscale project delete`[​](#anyscale-project-delete "Direct link to anyscale-project-delete")

**Usage**

`anyscale project delete [OPTIONS]`

Delete a project.

**Options**

* **`--id/-i`**: ID of the project to delete.

#### Examples[​](#examples-3 "Direct link to Examples")

* CLI

```
$ anyscale project delete --id project-id
```

### `anyscale project get-default`[​](#anyscale-project-get-default "Direct link to anyscale-project-get-default")

**Usage**

`anyscale project get-default [OPTIONS]`

Get the default project for a cloud.

**Options**

* **`--cloud/-c`**: Parent cloud ID for the project.
* **`--json/-j`**: Output the project in a structured JSON format.

#### Examples[​](#examples-4 "Direct link to Examples")

* CLI

```
$ anyscale project get-default --cloud my-cloud-id --json
```

### `anyscale project add-collaborators`[​](#anyscale-project-add-collaborators "Direct link to anyscale-project-add-collaborators")

**Usage**

`anyscale project add-collaborators [OPTIONS]`

Add collaborators to the project.

**Options**

* **`--cloud/-c`**: Name of the cloud that the project belongs to.
* **`--project/-p`**: Name of the project to add collaborators to.
* **`--users-file`**: Path to a YAML file containing a list of users to add to the project.

#### Examples[​](#examples-5 "Direct link to Examples")

* CLI

```
$ anyscale project add-collaborators --cloud cloud_name --project project_name --users-file collaborators.yaml
(anyscale +1.3s) Successfully added 3 collaborators to project project_name.
$ cat collaborators.yaml
collaborators:
  - email: "test1@anyscale.com"
    permission_level: "collaborator"
  - email: "test2@anyscale.com"
    permission_level: "readonly"
  - email: "test3@anyscale.com"
    permission_level: "owner"
```

## Project SDK[​](#project-sdk "Direct link to Project SDK")

### `anyscale.project.get`[​](#anyscaleprojectget "Direct link to anyscaleprojectget")

Get details of a project.

**Arguments**

* **`project_id` (str)**: The ID of the project to get details of.

**Returns**: [Project](/reference/project-api.md#project)

#### Examples[​](#examples-6 "Direct link to Examples")

* Python

```
import anyscale
from anyscale.project.models import Project

project: Project = anyscale.project.get(project_id="my-project-id")
```

### `anyscale.project.list`[​](#anyscaleprojectlist "Direct link to anyscaleprojectlist")

List projects.

**Arguments**

* **`name_contains` (str | None) = None**: A string to filter projects by name.
* **`creator_id` (str | None) = None**: The ID of a creator to filter projects.
* **`parent_cloud_id` (str | None) = None**: The ID of a parent cloud to filter projects.
* **`include_defaults` (bool) = True**: Whether to include default projects.
* **`max_items` (int | None) = None**: The maximum number of projects to return.
* **`page_size` (int | None) = None**: The number of projects to return per page.
* **`sort_field` ([ProjectSortField](/reference/project-api.md#projectsortfield) | None) = None**: The field to sort projects by.
* **`sort_order` ([ProjectSortOrder](/reference/project-api.md#projectsortorder) | None) = None**: The order to sort projects by.

**Returns**: ResultIterator\[[Project](/reference/project-api.md#project)]

#### Examples[​](#examples-7 "Direct link to Examples")

* Python

```
from typing import Iterator

import anyscale
from anyscale.project.models import Project, ProjectSortField, ProjectSortOrder

projects: Iterator[Project] = anyscale.project.list(
    name_contains="my-project",
    creator_id="my-user-id",
    parent_cloud_id="my-cloud-id",
    include_defaults=True,
    max_items=20,
    page_size=10,
    sort_field=ProjectSortField.NAME,
    sort_order=ProjectSortOrder.ASC,
)
for project in projects:
    print(project.name)
```

### `anyscale.project.create`[​](#anyscaleprojectcreate "Direct link to anyscaleprojectcreate")

Create a project.

**Arguments**

* **`name` (str)**: The name of the project.
* **`parent_cloud_id` (str)**: The parent cloud that the project belongs to.
* **`description` (str | None) = None**: The description of the project.
* **`initial_cluster_config` (str | None) = None**: A YAML string containing the initial cluster config for the project.

**Returns**: str

#### Examples[​](#examples-8 "Direct link to Examples")

* Python

```
import anyscale

project_id: str = anyscale.project.create(
    name="my-project",
    parent_cloud_id="my-cloud-id",
    description="my-project-description",
)
```

### `anyscale.project.delete`[​](#anyscaleprojectdelete "Direct link to anyscaleprojectdelete")

Delete a project.

**Arguments**

* **`project_id` (str)**: The ID of the project to delete.

#### Examples[​](#examples-9 "Direct link to Examples")

* Python

```
import anyscale

anyscale.project.delete(project_id="my-project-id")
```

### `anyscale.project.get_default`[​](#anyscaleprojectget_default "Direct link to anyscaleprojectget_default")

Get the default project for a cloud.

**Arguments**

* **`parent_cloud_id` (str)**: The ID of the parent cloud to get the default project for.

**Returns**: [Project](/reference/project-api.md#project)

#### Examples[​](#examples-10 "Direct link to Examples")

* Python

```
import anyscale
from anyscale.project.models import Project

project: Project = anyscale.project.get_default(parent_cloud_id="my-cloud-id")
```

### `anyscale.project.add_collaborators`[​](#anyscaleprojectadd_collaborators "Direct link to anyscaleprojectadd_collaborators")

Batch add collaborators to a project.

**Arguments**

* **`cloud` (str)**: The cloud that the project belongs to.
* **`project` (str)**: The project to add users to.
* **`collaborators` (List\[[CreateProjectCollaborator](/reference/project-api.md#createprojectcollaborator)])**: The list of collaborators to add to the project.

**Returns**: str

#### Examples[​](#examples-11 "Direct link to Examples")

* Python

```
import anyscale
from anyscale.project.models import CreateProjectCollaborator, ProjectPermissionLevel

anyscale.project.add_collaborators(
    cloud="cloud_name",
    project="project_name",
    collaborators=[
        CreateProjectCollaborator(
            email="test1@anyscale.com",
            permission_level=ProjectPermissionLevel.OWNER,
        ),
        CreateProjectCollaborator(
            email="test2@anyscale.com",
            permission_level=ProjectPermissionLevel.WRITE,
        ),
        CreateProjectCollaborator(
            email="test3@anyscale.com",
            permission_level=ProjectPermissionLevel.READONLY,
        ),
    ],
)
```

## Project Models[​](#project-models "Direct link to Project Models")

### `Project`[​](#project "Direct link to project")

Project object.

#### Fields[​](#fields "Direct link to Fields")

* **`id` (str)**: ID of the project.
* **`name` (str)**: Name of the project.
* **`description` (str)**: Description of the project.
* **`created_at` (str)**: Datetime of the project creation.
* **`creator_id` (str | None)**: ID of the creator of the project.
* **`parent_cloud_id` (str | None)**: ID of the parent cloud.
* **`is_owner` (bool)**: Whether the user is the owner of the project.
* **`is_read_only` (bool)**: Whether the user has read-only access to the project.
* **`directory_name` (str)**: Directory name of project to be used as working directory of clusters.
* **`is_default` (bool)**: Whether the project is the default project for the organization.
* **`initial_cluster_config` (str | Dict\[str, Any] | None)**: Initial cluster config associated with the project.
* **`last_used_cloud_id` (str | None)**: ID of the last cloud used in this project, or by the user if this is a new project.
* **`owners` (List\[str])**: List of IDs of users who have owner access to the project.

#### Python Methods[​](#python-methods "Direct link to Python Methods")

```
def to_dict(self) -> Dict[str, Any]
    """Return a dictionary representation of the model."""
```

#### Examples[​](#examples-12 "Direct link to Examples")

* Python

```
import anyscale
from anyscale.project.models import Project

project: Project = anyscale.project.get(project_id="my-project-id")
```

### `ProjectSortField`[​](#projectsortfield "Direct link to projectsortfield")

Field to sort projects by.

#### Values[​](#values "Direct link to Values")

* **`NAME`**: Sort by project name.

### `ProjectSortOrder`[​](#projectsortorder "Direct link to projectsortorder")

Direction of sorting.

#### Values[​](#values-1 "Direct link to Values")

* **`ASC`**: Sort in ascending order.
* **`DESC`**: Sort in descending order.

### `CreateProjectCollaborator`[​](#createprojectcollaborator "Direct link to createprojectcollaborator")

User to be added as a collaborator to a project.

#### Fields[​](#fields-1 "Direct link to Fields")

* **`email` (str)**: Email of the user to be added as a collaborator.
* **`permission_level` ([ProjectPermissionLevel](/reference/project-api.md#projectpermissionlevel))**: Permission level the added user should have for the project(one of: OWNER,WRITE,READONLY

#### Python Methods[​](#python-methods-1 "Direct link to Python Methods")

```
def to_dict(self) -> Dict[str, Any]
    """Return a dictionary representation of the model."""
```

#### Examples[​](#examples-13 "Direct link to Examples")

* Python

```
import anyscale
from anyscale.project.models import ProjectPermissionLevel, CreateProjectCollaborator
create_project_collaborator = CreateProjectCollaborator(
   # Email of the user to be added as a collaborator
    email="test@anyscale.com",
    # Permission level for the user to the project (ProjectPermissionLevel.OWNER, ProjectPermissionLevel.WRITE, ProjectPermissionLevel.READONLY)
    permission_level=ProjectPermissionLevel.READONLY,
)
```

### `ProjectPermissionLevel`[​](#projectpermissionlevel "Direct link to projectpermissionlevel")

Permission levels for project collaborators.

#### Values[​](#values-2 "Direct link to Values")

* **`OWNER`**: Owner permission level for the project
* **`WRITE`**: Write permission level for the project
* **`READONLY`**: Readonly permission level for the project
