# Source: https://docs.agent.ai/actions/get_data_from_users_uploaded_files.md

# Get Data from User's Uploaded Files

## Overview

Retrieve semantic search results from user-uploaded files for targeted information extraction.

### Use Cases

* **Data Analysis**: Quickly retrieve insights from reports or project files uploaded by users.
* **Customized Searches**: Provide tailored responses by extracting specific data from user-uploaded files.

## Configuration Fields

### Query

* **Description**: Enter the search query to find relevant information in uploaded files.
* **Example**: "Revenue breakdown" or "Budget overview."
* **Required**: Yes

### User Uploaded Files to Use

* **Description**: Specify which uploaded files to search within.
* **Example**: "Recent uploads" or "project\_documents."
* **Required**: Yes

### Max Number of Document Chunks to Retrieve

* **Description**: Set the maximum number of document chunks to return.
* **Example**: "5" or "10."
* **Required**: Yes

### Qualitative Vector Score Cutoff for Semantic Search Cosine Similarity

* **Description**: Adjust the score threshold for search relevance.
* **Example**: "0.2" for broad results or "0.5" for specific results.
* **Required**: Yes

### Output Variable Name

* **Description**: Assign a variable name to store the search results.
* **Example**: "file\_search\_results" or "upload\_data."
* **Validation**: Only letters, numbers, and underscores (\_) are allowed.
* **Required**: Yes
