# Source: https://docs.roboflow.com/roboflow/roboflow-ko/datasets/project-folders.md

# Source: https://docs.roboflow.com/roboflow/roboflow-jp/datasets/project-folders.md

# Source: https://docs.roboflow.com/roboflow/roboflow-hi/datasets/project-folders.md

# Source: https://docs.roboflow.com/datasets/project-folders.md

# Project Folders

Project Folders improves the organization and security of projects within your workspace. Folders allow you to group one or more projects into distinct categories, which improves your ability to navigate, organize, and manage your projects. Additionally, for workspaces with SSO enabled, you can restrict access to projects within a folder to certain team members, which enhances the security of your data.

#### Viewing Folders

From your workspace view, any Project Folders you have will appear at the top. Your workspace can have one or more Project Folders, and each Project Folder can contain one or more Projects.

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-14fd4a03b0a908ce48c534106c592c407099c4eb%2FScreenshot%202024-06-26%20at%2010.36.05.png?alt=media" alt=""><figcaption><p>Project Folders appear at the top of your Workspace</p></figcaption></figure>

#### Creating a Folder

To create a new folder, click the "+ New Folder" button in the top right. Provide a name for your folder and click "Save". The page will navigate to your project folder where you can create a new project. Any project created from the project folder view will automatically added to that folder.

[\[Roboflow Documentation\] Project Folders - Create Project - Watch Video](https://www.loom.com/share/aefb3b5fd1ea40cdb4183c903f13d9c8)

<figure><img src="https://cdn.loom.com/sessions/thumbnails/aefb3b5fd1ea40cdb4183c903f13d9c8-with-play.gif" alt=""><figcaption><p>Creating a new Project Folder</p></figcaption></figure>

#### Renaming a Folder

To rename a folder, click on the dropdown menu (3 dots) on the project folder. Select the "Rename" option, and then provide the new name for your project. After clicking "Save", your folder will have its new name.

[\[Roboflow Documentation\] Project Folders - Rename Folder - Watch Video](https://www.loom.com/share/63508a2ff629454690ac0957d5cfc990)

<figure><img src="https://cdn.loom.com/sessions/thumbnails/63508a2ff629454690ac0957d5cfc990-with-play.gif" alt=""><figcaption></figcaption></figure>

#### Managing Projects in Folders

You can move existing projects into a folder. To move a project, click on the project's dropdown menu (3 dots) and select "Move Project". You will then see a pop up where you can select the new target destination. If you do not have any project folders, you can add one by clicking the "New Folder" button. Otherwise, you can select any of your existing folders as the target location. If you want to move your project out of a folder, you can select your workspace's name.

[\[Roboflow Documentation\] Project Folders - Move Project - Watch Video](https://www.loom.com/share/a411cabb98f14255b07c3c2e209c3abd)

<figure><img src="https://cdn.loom.com/sessions/thumbnails/a411cabb98f14255b07c3c2e209c3abd-with-play.gif" alt=""><figcaption></figcaption></figure>

#### Deleting a Folder

You can delete a folder by clicking the dropdown menu (3 dots) on the project folder and selecting the "Delete" option (this action cannot be undone). Deleting a folder **will not** delete the projects in the folder, it will move those projects back to the workspace level.

[\[Roboflow Documentation\] Project Folders - Delete Folder - Watch Video](https://www.loom.com/share/852e70b217de4d5d9ca79bef41903ad9)

<figure><img src="https://cdn.loom.com/sessions/thumbnails/852e70b217de4d5d9ca79bef41903ad9-with-play.gif" alt=""><figcaption></figcaption></figure>

### Custom Folder Permissions

Folders provide a great way to organize and manage your projects, but they also enable you to set custom permissions for a subset of your folders. For example, if you only want a few members of your workspace to access projects in a particular folder, you can accomplish that with Roboflow's SSO integration. To get started, please contact support and we will be happy to get you set up.

### Project Folders API

Project Folders can be managed programmatically using the Roboflow API. For details on available endpoints, view the [Project Folders API](https://app.gitbook.com/s/e5GEiPeDoFksvZv1vH3A/rest-api/manage-project-folders) documentation.
