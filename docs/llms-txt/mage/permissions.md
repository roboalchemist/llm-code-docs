# Source: https://docs.mage.ai/production/authentication/permissions/permissions.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.mage.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Permissions

> Create granular permissions for CRUD operations on any API endpoint.

<Frame>
  <p align="center">
    <img alt="User defined permissions" src="https://media.tenor.com/NFeV9svhtREAAAAC/community-ken-jeong.gif" />
  </p>
</Frame>

## Overview

* A permission grants or denies read and write operations and access on a specific entity.
* An entity maps to an existing API endpoint in the Mage application.
* A permission can grant or deny access to a specific entity with a specific UUID.
* Each operation and attribute operation has an access level that denies access
  to a specific entity for that particular operation or attribute operation.

  * When denying an attribute operation,
    define the set of attributes that the permission forbids the user from
    querying, reading, or writing.

## Operations

<AccordionGroup>
  <Accordion title="List">
    This access level grants permission to perform a `GET` request
    to the collections API endpoint for a specific entity.
  </Accordion>

  <Accordion title="Create">
    This access level grants permission to perform a `POST` request
    to an API endpoint for a specific entity.
  </Accordion>

  <Accordion title="Detail">
    This access level grants permission to perform a `GET` request
    to the details API endpoint for a specific entity.
  </Accordion>

  <Accordion title="Update">
    This access level grants permission to perform a `PUT` request
    to an API endpoint for a specific entity.
  </Accordion>

  <Accordion title="Delete">
    This access level grants permission to perform a `DELETE` request
    to an API endpoint for a specific entity.
  </Accordion>

  <Accordion title="All operations">
    This access level grants allows the following operations to be
    performed for a specific entity:

    * List
    * Create
    * Detail
    * Update
    * Delete
  </Accordion>
</AccordionGroup>

## Attribute operations

<AccordionGroup>
  <Accordion title="Query">
    This access level grants permission to use a specific set of query parameters
    when making an API request for a given entity.
  </Accordion>

  <Accordion title="Read">
    This access level grants permission to read a specific set of attributes
    from an API response for a specific entity.
  </Accordion>

  <Accordion title="Write">
    This access level grants permission to write a specific set of attributes
    when submitting a payload in the API request body for a specific entity.
  </Accordion>
</AccordionGroup>

### Query attributes

When granting `Query` access, you must define the set of query parameters this permission allows.

### Read attributes

When granting `Read` access, you must define the set of attributes this permission
allows the user to read.

### Write attributes

When granting `Write` access, you must define the set of attributes this permission
allows the user to write.

***

## Groups

The following access levels contain logic that grants access to multiple operations
and attribute operations.

<Note>
  The attribute operation that the group access grants still requires you
  to define the specific set of attributes that the user is permitted to
  query, read, or write.
</Note>

<AccordionGroup>
  <Accordion title="Viewer">
    This access level grants the following for a specific entity:

    * Operations
      * List
      * Detail
    * Attribute operations
      * Read
  </Accordion>

  <Accordion title="Editor">
    This access level grants the following for a specific entity:

    * Operations
      * *Everything from Viewer*
      * Create
      * Update
      * Delete
    * Attribute operations
      * *Everything from Viewer*
      * Query
      * Write
  </Accordion>

  <Accordion title="Admin">
    This access level grants the following for a specific entity:

    * Operations
      * *Everything from Viewer*
      * *Everything from Editor*
    * Attribute operations
      * *Everything from Viewer*
      * *Everything from Editor*
  </Accordion>

  <Accordion title="Owner">
    This access level grants the following for a specific entity:

    * Operations
      * *Everything from Viewer*
      * *Everything from Editor*
      * *Everything from Admin*
    * Attribute operations
      * *Everything from Viewer*
      * *Everything from Editor*
      * *Everything from Admin*
  </Accordion>

  <Accordion title="All">
    This access level grants every operation, attribute operation,
    all query attributes, all read attributes, and all write attributes
    for a specific entity.
  </Accordion>
</AccordionGroup>

***

## Special conditions

<AccordionGroup>
  <Accordion title="Disable unless user has notebook edit access">
    This access level will deny the user from performing an operation or attribute operation
    on a specific entity
    unless the user has notebook edit access.
  </Accordion>

  <Accordion title="Disable unless user has pipeline edit access">
    This access level will deny the user from performing an operation or attribute operation
    on a specific entity
    unless the user has pipeline edit access.
  </Accordion>

  <Accordion title="Disable unless user owns the current entity">
    This access level will deny the user from performing an operation or attribute operation
    on a specific entity
    unless the user owns the current entity they are attempting to perform an action on.

    <Warning>
      The only entity this access level supports currently is the `User` entity.
    </Warning>
  </Accordion>
</AccordionGroup>

***

## Entity names

<Accordion title="List of available entities">
  1. `ALL`
  2. `ALL_EXCEPT_RESERVED`
  3. `AutocompleteItem`
  4. `Backfill`
  5. `Block`
  6. `BlockLayoutItem`
  7. `BlockOutput`
  8. `BlockRun`
  9. `BlockTemplate`
  10. `Chart`
  11. `ClientPage`
  12. `Cluster`
  13. `CustomTemplate`
  14. `DataProvider`
  15. `Database`
  16. `EventMatcher`
  17. `EventRule`
  18. `ExtensionOption`
  19. `Feature`
  20. `File`
  21. `FileContent`
  22. `FileVersion`
  23. `Folder`
  24. `GitBranch`
  25. `GitCustomBranch`
  26. `GitFile`
  27. `GlobalDataProduct`
  28. `IntegrationDestination`
  29. `IntegrationSource`
  30. `IntegrationSourceStream`
  31. `Interaction`
  32. `Kernel`
  33. `Llm`
  34. `Log`
  35. `MonitorStat`
  36. `Oauth`
  37. `OauthAccessToken`
  38. `OauthApplication`
  39. `Output`
  40. `PageBlockLayout`
  41. `PageComponent`
  42. `Permission`
  43. `Pipeline`
  44. `PipelineInteraction`
  45. `PipelineRun`
  46. `PipelineSchedule`
  47. `PipelineTrigger`
  48. `Project`
  49. `PullRequest`
  50. `Role`
  51. `RolePermission`
  52. `Scheduler`
  53. `SearchResult`
  54. `Secret`
  55. `Session`
  56. `SparkApplication`
  57. `SparkEnvironment`
  58. `SparkExecutor`
  59. `SparkJob`
  60. `SparkSql`
  61. `SparkStage`
  62. `SparkStageAttempt`
  63. `SparkStageAttemptTask`
  64. `SparkStageAttemptTaskSummary`
  65. `SparkThread`
  66. `Status`
  67. `Sync`
  68. `Tag`
  69. `User`
  70. `UserRole`
  71. `Variable`
  72. `Widget`
  73. `Workspace`
</Accordion>

### `ALL`

Using this entity for a permission will grant the operation or attribute operation
for every entity listed above.

### `ALL_EXCEPT_RESERVED`

Using this entity for a permission will grant the operation or attribute operation
for every entity listed except the following entities:

1. `Oauth`
2. `OauthAccessToken`
3. `OauthApplication`
4. `Workspace`


Built with [Mintlify](https://mintlify.com).