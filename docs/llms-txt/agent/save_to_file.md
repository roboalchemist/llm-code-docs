# Source: https://docs.agent.ai/actions/save_to_file.md

# Save To File

## Overview

Save text content as a downloadable file in various formats, including PDF, Microsoft Word, HTML, and more within workflows.

### Use Cases

* **Content Export**: Allow users to download generated content in their preferred file format.
* **Report Generation**: Create downloadable reports from workflow data.
* **Documentation**: Generate and save technical documentation or user guides.

<iframe width="560" height="315" src="https://www.youtube.com/embed/EAbJ9ksHbP8?si=Oyym3CNsMFR98heg" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />

## Configuration Fields

### File Type

* **Description**: Select the output file format for the saved content.
* **Options**: PDF, Microsoft Word, HTML, Markdown, OpenDocument Text, TeX File, Amazon Kindle Book File, eBook File, PNG Image File
* **Default**: PDF
* **Required**: Yes

### Body

* **Description**: Provide the content to be saved in the file, including text, bullet points, or other structured information.
* **Example**: "# Project Summary\n\nThis document outlines the key deliverables for the Q3 project."
* **Required**: Yes

### Output Variable Name

* **Description**: Assign a variable name to store the file URL for later reference in the workflow.
* **Example**: "saved\_file" or "report\_document"
* **Validation**: Only letters, numbers, and underscores (\_) are allowed in variable names.
* **Required**: Yes

## Beta Feature

This action is currently in beta. While fully functional, it may undergo changes based on user feedback.
