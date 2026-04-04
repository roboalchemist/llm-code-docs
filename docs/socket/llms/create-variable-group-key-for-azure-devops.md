# Source: https://docs.socket.dev/docs/create-variable-group-key-for-azure-devops.md

# Create Variable Group for ADO

An Azure DevOps project requires the creation of a **Variable Group** named **socket\_security.** This group will contain an **api\_key** variable, assigned the value of *SOCKET\_SECURITY\_API\_KEY*, and can be shared across multiple pipelines.

1. To begin, select your **ADO** project
2. Click on **Pipelines** from the left menu
3. Then select **Library** item under **Pipelines** menu
4. Click on **+Variable group** button
5. Under *Properties* section, on the **”Variable group name”** field, enter **socket\_security** (all lower case)
6. Under the *Variables* section, click on  **+ Add** button
   1. In the **Name** field, set as api\_key
   2. In the **Value** field,  place your generated *SOCKET\_SECURIY\_API\_KEY* here
7. Click **Save**