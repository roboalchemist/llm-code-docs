# Source: https://docs.roboflow.com/developer/rest-api/list-workspaces-and-projects.md

# Source: https://docs.roboflow.com/developer/command-line-interface/list-workspaces-and-projects.md

# List Workspaces and Projects

### List Workspaces

You can retrieve a list of all Workspaces of which you are a member with the CLI.

To list Workspaces with the CLI, use the following command:

<pre class="language-bash"><code class="lang-bash"><strong>roboflow workspace list
</strong></code></pre>

This will return a list of Workspaces with their corresponding application links and Workspace IDs:

```
tonyprivate
  link: https://app.roboflow.com/tonyprivate
  id: tonyprivate

wolfodorpythontests
  link: https://app.roboflow.com/wolfodorpythontests
  id: wolfodorpythontests

test minimize
  link: https://app.roboflow.com/test-minimize
  id: test-minimize

```

### List Projects in a Workspace

To list projects in a workspace, use the following command:

```
roboflow project list -w WORKSPACE_ID
```

Where `WORKSPACE_ID` is your Roboflow Workspace ID.

This will return a list of Projects:

```json
annotation-upload
  link: https://app.roboflow.com/tonyprivate/annotation-upload
  id: tonyprivate/annotation-upload
  type: object-detection
  versions: 0
  images: 1
  classes: dict_keys(['0', 'Rabbits1', 'Rabbits2', 'minion1', 'minion0', '5075E'])

hand-gestures
  link: https://app.roboflow.com/tonyprivate/hand-gestures-fsph8
  id: tonyprivate/hand-gestures-fsph8
  type: object-detection
  versions: 5
  images: 387
  classes: dict_keys(['zero', 'four', 'one', 'two', 'five', 'three', 'Guard'])
```

### Get a Project

To get information about a project in the CLI, use the following command:

```bash
roboflow project get -w WORKSPACE_ID PROJECT_ID
```

This will return a JSON object with information about a project, as well as a list of Versions within the project:

```json
{
  "workspace": {
    "name": "tonyprivate",
    "url": "tonyprivate",
    "members": 4
  },
  "project": {
    "id": "tonyprivate/annotation-upload",
    "type": "object-detection",
    "name": "annotation-upload",
    "created": 1685199749.708,
    "updated": 1695910515.48,
    "images": 1,
    (...)
  },
  "versions": []
}
```
