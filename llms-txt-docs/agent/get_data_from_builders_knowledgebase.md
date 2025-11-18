# Source: https://docs.agent.ai/actions/get_data_from_builders_knowledgebase.md

# Get Data from Builder's Knowledge Base

## Overview

Fetch semantic search results from the builder's knowledge base, enabling you to use structured data for analysis and decision-making.

### Use Cases

* **Content Retrieval**: Search for specific information in a structured knowledge base, such as FAQs or product documentation.
* **Automated Assistance**: Power AI agents with relevant context from internal resources.

## Configuration Fields

### Query

* **Description**: Enter the search query to retrieve relevant knowledge base entries.
* **Example**: "Latest sales strategies" or "Integration instructions."
* **Required**: Yes

### Builder Knowledge Base to Use

* **Description**: Select the knowledge base to search from.
* **Example**: "Product Documentation" or "Employee Handbook."
* **Required**: Yes

### Max Number of Document Chunks to Retrieve

* **Description**: Specify the maximum number of document chunks to return.
* **Example**: "5" or "10."
* **Required**: Yes

### Qualitative Vector Score Cutoff for Semantic Search Cosine Similarity

* **Description**: Set the score threshold for search relevance.
* **Example**: "0.2" for broad results or "0.7" for precise matches.
* **Required**: Yes

### Output Variable Name

* **Description**: Assign a variable name to store the search results.
* **Example**: "knowledge\_base\_results" or "kb\_entries."
* **Validation**: Only letters, numbers, and underscores (\_) are allowed.
* **Required**: Yes
