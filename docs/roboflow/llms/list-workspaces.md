# Source: https://docs.roboflow.com/developer/python-sdk/list-workspaces.md

# List Workspaces

You can list all the Workspaces of which you are a member using the following code:

```python
import roboflow

rf = roboflow.Roboflow(api_key=YOUR_API_KEY_HERE)

# List all projects for your workspace
workspace = rf.workspace()
```
