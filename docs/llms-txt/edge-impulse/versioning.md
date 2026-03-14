# Source: https://docs.edgeimpulse.com/studio/projects/versioning.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Versioning

In this documentation, we will explore versioning in Edge Impulse. Edge Impulse allows you to version control individual blocks and your entire project and pipeline. Versioning is crucial to project management, ensuring you can track changes, revert to previous states, and collaborate effectively with your team. We will draw comparisons to Git versioning to help illustrate these concepts and mainly focus on project-level versioning.

<Frame caption="Versioning projects">
  <img src="https://mintcdn.com/edgeimpulse/sFtdfPhSpbLZ2-cz/.assets/images/studio-versioning.png?fit=max&auto=format&n=sFtdfPhSpbLZ2-cz&q=85&s=fe0a8f1ee895c0fae879e6c08db31205" width="1600" height="824" data-path=".assets/images/studio-versioning.png" />
</Frame>

## Introduction

Versioning allows you to create snapshots of your project at different stages of development. This feature is particularly useful for managing complex machine learning projects, where tracking changes and maintaining a history of modifications is essential. Similar to how Git manages different versions of code, Edge Impulse’s versioning system helps manage the evolution of your machine learning projects.

## Key Benefits

* **Track Changes**: Monitor the evolution of your project over time, akin to committing changes in [Git version control](https://docs.github.com/en/get-started/using-git/about-git).
* **Revert to Previous Versions**: Restore your project to a prior state if needed, similar to checking out a previous commit in Git.
* **Collaborate Effectively**: Share specific versions of your project with team members, like sharing branches or commits in Git.
* **Maintain History**: Keep a detailed record of all changes made to your project, much like the commit history in Git.

## What Prompts a Version Change

Version changes are prompted by significant modifications to the project, such as:

* **Model Architecture**: Alterations to the structure of your machine learning model.
* **Dataset**: Additions or modifications to the training or testing data.
* **Hardware Target Configuration**: Changes to the target hardware configuration for deployment.
* **Other Significant Changes**: Any other substantial changes that affect the performance or functionality of your project.

## How It Works

Edge Impulse provides a straightforward versioning system that allows you to create and manage versions of your projects. Each version captures the current state of your project, including data, configurations, models, and settings. This is comparable to how a Git commit captures the state of a codebase at a particular point in time.

The following diagram illustrates the workflow for creating and managing versions in Edge Impulse:

<Frame caption="Version workflow">
  <img src="https://mintcdn.com/edgeimpulse/ZGbvQAs-QNgkltKA/.assets/images/version-flow.png?fit=max&auto=format&n=ZGbvQAs-QNgkltKA&q=85&s=ee0d3ecbf10de3639dbd40a939b730c1" width="1600" height="531" data-path=".assets/images/version-flow.png" />
</Frame>

## Getting Started

To start using the versioning feature, log in to your Edge Impulse account and open a project. Navigate to the "Version" tab and begin creating versions to manage your project's development effectively.

## Creating a Version

To create a version of your project, follow these steps:

1. **Navigate to Your Project**: Open the project you want to version in the Edge Impulse Studio.

2. **Create a New Version**: Click on the "Version" tab in the left-hand menu. Then, click the "Store your current project version" button.

   <Frame caption="Store your current project version">
     <img src="https://mintcdn.com/edgeimpulse/YmjKhgkCrlx3Nxh9/.assets/images/create-version.png?fit=max&auto=format&n=YmjKhgkCrlx3Nxh9&q=85&s=ef5d053123c362af51ffdae1ec9d654a" width="1600" height="585" data-path=".assets/images/create-version.png" />
   </Frame>

3. **Name Your Version**: Provide a meaningful name and description for your version. This will help you identify it later, similar to writing a commit message in Git.

   <Frame caption="Detail Version Changes">
     <img src="https://mintcdn.com/edgeimpulse/BCrJzLAs8FGQ0Eny/.assets/images/second-version.png?fit=max&auto=format&n=BCrJzLAs8FGQ0Eny&q=85&s=789a28ec4832a09cb725f058a7845520" width="797" height="557" data-path=".assets/images/second-version.png" />
   </Frame>

<Info>
  If you want to reference your project in the Edge Impulse [public project repository](https://edgeimpulse.com/projects/overview), check the **Publish this version under the Apache 2.0 license**. This is a great way to share your work with the community.
</Info>

4. **Save the Version**: Click "Save" to create the version. Your project is now versioned, and the current state is saved, much like creating a commit in Git.

   <Frame caption="Save Version">
     <img src="https://mintcdn.com/edgeimpulse/BCrJzLAs8FGQ0Eny/.assets/images/save-version.png?fit=max&auto=format&n=BCrJzLAs8FGQ0Eny&q=85&s=f8b2dfad4583ca6fba87466516c0217e" width="1600" height="736" data-path=".assets/images/save-version.png" />
   </Frame>

## Viewing Versions

You will see a list of all versions created for the project.

Each version includes:

* The version number
* The creation date
* The user who created the version
* The description
* The training accuracy
* The testing accuracy
* The number of data samples
* The visibility

<Frame caption="Versioning projects">
  <img src="https://mintcdn.com/edgeimpulse/sFtdfPhSpbLZ2-cz/.assets/images/studio-versioning.png?fit=max&auto=format&n=sFtdfPhSpbLZ2-cz&q=85&s=fe0a8f1ee895c0fae879e6c08db31205" width="1600" height="824" data-path=".assets/images/studio-versioning.png" />
</Frame>

## Reverting to a Previous Version

1. **Select a Version**: Choose the version you want to revert to from the list.

   <Frame caption="Select Version">
     <img src="https://mintcdn.com/edgeimpulse/Z-eQceB7ehSwo9rf/.assets/images/select-version.png?fit=max&auto=format&n=Z-eQceB7ehSwo9rf&q=85&s=5a00c36fe16e657e4667d4a353886144" width="1600" height="801" data-path=".assets/images/select-version.png" />
   </Frame>

2. **Revert**: Click the "Revert to this version" button. Confirm your choice in the dialog that appears, similar to checking out a previous commit or branch in Git.

   <Frame caption="Revert Version">
     <img src="https://mintcdn.com/edgeimpulse/KpGxseVgo6WAQqJB/.assets/images/revert-version.png?fit=max&auto=format&n=KpGxseVgo6WAQqJB&q=85&s=eccac6605bf02519ca42ac84c338a1a2" width="1600" height="729" data-path=".assets/images/revert-version.png" />
   </Frame>

## Working with Organizations

Edge Impulse also supports organizational management, allowing multiple users to collaborate on projects within a structured environment. Here’s how versioning can be particularly beneficial within organizations:

* **Centralized Management**: Administrators can oversee all projects, ensuring consistent versioning practices across the team.
* **Team Collaboration**: Multiple team members can access and work on the same project versions, facilitating smoother collaboration.
* **Access Control**: Set permissions to control who can create, view, or revert versions, ensuring that only authorized personnel can make significant changes.
* **Audit Trails**: Maintain an audit trail of all version changes across projects within the organization, which is essential for accountability and compliance.

## Best Practices

* **Regular Versioning**: Create versions at key milestones in your project development to ensure you have a record of significant changes, similar to making frequent commits in Git.
* **Meaningful Descriptions**: When creating a version, use descriptive names and detailed descriptions to help identify the purpose and changes included in that version, akin to writing clear commit messages in Git.
* **Collaborative Versioning**: Encourage team members to create versions before making significant changes. This practice ensures that everyone can revert to a stable state if needed, much like using branches in Git for collaboration.

## Conclusion

Versioning is an essential feature for managing machine learning projects in Edge Impulse. By creating and managing versions, you can track changes, collaborate effectively, and maintain a history of your project’s development. Start versioning your projects today to enhance your workflow and project management.

For further assistance, visit our [forum](https://forum.edgeimpulse.com).


Built with [Mintlify](https://mintlify.com).