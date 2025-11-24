# Source: https://docs.agent.ai/actions/get_user_file.md

# Get User File

## Overview

The "Get User File" action allows users to upload files for processing, storage, or review.

<Info>
  Most common file types—including `.pdf`, `.txt`, and `.csv`—are supported.\
  Improved CSV handling for Claude Sonnet was introduced in July 2025 to increase reliability with structured data inputs.
</Info>

### Use Cases

* **Resume Collection**: Upload resumes in PDF format.
* **File Processing**: Gather data files for analysis.
* **Document Submission**: Collect required documentation from users.

## Configuration Fields

### User Prompt

* **Description**: Provide clear instructions for users to upload files.
* **Example**: "Upload your resume as a PDF."
* **Required**: Yes

### Required?

* **Description**: Mark this checkbox if file upload is necessary for the workflow to proceed.
* **Required**: No

### Output Variable Name

* **Description**: Assign a variable name for the uploaded files.
* **Example**: "user\_documents" or "uploaded\_images."
* **Validation**:
  * Only letters, numbers, and underscores (\_) are allowed.
  * No spaces, special characters, or dashes.
  * **Regex**: `^[a-zA-Z0-9_]+$`
* **Hint**: This variable will be used to reference the files in subsequent steps.
* **Required**: Yes

### Show Only Files Uploaded in the Current Session

* **Description**: Restrict access to files uploaded only during the current session.
* **Required**: No
