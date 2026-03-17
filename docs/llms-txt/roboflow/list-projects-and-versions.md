# Source: https://docs.roboflow.com/developer/python-sdk/list-projects-and-versions.md

# List Projects and Versions

You can list all Projects and Versions within a Project with the Python package.

### List Projects

You can list all Projects within a Workspace using the following code:

```python
import roboflow

rf = roboflow.Roboflow(api_key=YOUR_API_KEY_HERE)
workspace = rf.workspace(WORKSPACE_ID)
```

Where `WORKSPACE_ID`  is your workspace URL identifier (e.g., "my-workspace" from `https://app.roboflow.com/my-workspace`).

### Get a Project

```
# get a specific project
project = rf.workspace().project("PROJECT_ID")

# list all versions in a specific project
project.versions()

# get a specific version from a project
project.version(version_number)
```
