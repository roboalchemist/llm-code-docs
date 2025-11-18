# Source: https://docs.agent.ai/actions/get_variable_from_database.md

# Get Variable from Database

## Overview

Retrieve stored variables from the agent's database for use in workflows.

### Use Cases

* **Data Reuse**: Leverage previously stored variables for decision-making.
* **Trend Analysis**: Access historical data for analysis.

## Configuration Fields

### Variable

* **Description**: Specify the variable to retrieve from the database.
* **Example**: "user\_input" or "order\_status."
* **Required**: Yes

### Retrieval Depth

* **Description**: Choose how far back to retrieve the data.
* **Options**: Most Recent Value, Historical Values
* **Example**: "Most Recent Value" for the latest data.
* **Required**: Yes

### Historical Data Interval (optional)

* **Description**: Define the interval for historical data retrieval.
* **Options**: Hour, Day, Week, Month, All Time
* **Example**: "Last 7 Days" for weekly data.
* **Required**: No

### Number of Items to Retrieve (optional)

* **Description**: Enter the number of items to retrieve from historical data.
* **Example**: "10" to fetch the last 10 entries.
* **Required**: No

### Output Variable Name

* **Description**: Assign a variable name to store the retrieved data.
* **Example**: "tracked\_values" or "historical\_data."
* **Validation**: Only letters, numbers, and underscores (\_) are allowed.
* **Required**: Yes
