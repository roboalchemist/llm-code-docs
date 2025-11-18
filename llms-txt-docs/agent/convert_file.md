# Source: https://docs.agent.ai/actions/convert_file.md

# Convert File

## Overview

Convert uploaded files to different formats, such as PDF, TXT, or PNG, within workflows.

### Use Cases

* **Document Management**: Convert user-uploaded files to preferred formats.
* **Data Transformation**: Process files for compatibility with downstream actions.

<iframe width="560" height="315" src="https://www.youtube.com/embed/WWRn_d4uQhc?si=x_FTZ9AG0fzuNuOR" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />

## Configuration Fields

### Input Files

* **Description**: Select the files to be converted.
* **Example**: "uploaded\_documents" or "images."
* **Required**: Yes

### Show All Conversion Options

* **Description**: Enable to display all available conversion options.
* **Required**: Yes

### Convert to Extension

* **Description**: Specify the desired output file format.
* **Example**: "pdf," "txt," or "png."
* **Required**: No

### Output Variable Name

* **Description**: Assign a variable name to store the converted files.
* **Example**: "converted\_documents" or "output\_images."
* **Validation**: Only letters, numbers, and underscores (\_) are allowed.
* **Required**: Yes
