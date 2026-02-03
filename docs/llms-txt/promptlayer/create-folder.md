# Source: https://docs.promptlayer.com/reference/create-folder.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.promptlayer.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Create Folder

> Creates a new folder in the workspace. Folders can be nested within other folders by providing a parent_id. The folder name must be unique within its parent folder (or at the root level if no parent is specified).

Creates a new folder in the workspace. Folders can be nested within other folders by providing a parent\_id. The folder name must be unique within its parent folder (or at the root level if no parent is specified).


## OpenAPI

````yaml POST /api/public/v2/folders
openapi: 3.1.0
info:
  title: FastAPI
  version: 0.1.0
servers: []
security: []
paths:
  /api/public/v2/folders:
    post:
      tags:
        - folders
      summary: Create Folder
      description: >-
        Creates a new folder in the workspace. Folders can be nested within
        other folders by providing a parent_id. The folder name must be unique
        within its parent folder (or at the root level if no parent is
        specified).
      operationId: create_folder_api_public_v2_folders_post
      parameters:
        - required: true
          schema:
            type: string
            title: X-Api-Key
          name: X-API-KEY
          in: header
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CreateFolderRequest'
      responses:
        '201':
          description: Folder created successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/CreateFolderSuccessResponse'
        '400':
          description: Bad request - Invalid input or folder name already exists
          content:
            application/json:
              schema:
                anyOf:
                  - $ref: '#/components/schemas/FolderExistsError'
                  - type: string
                    example: Invalid workspace_id
        '401':
          description: Unauthorized - Missing or invalid API key
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/UnauthorizedError'
        '404':
          description: Parent folder not found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ParentFolderNotFoundError'
components:
  schemas:
    CreateFolderRequest:
      type: object
      required:
        - name
      properties:
        name:
          type: string
          minLength: 1
          maxLength: 255
          description: The name of the folder. Must be unique within its parent folder.
        parent_id:
          type: integer
          nullable: true
          description: >-
            The ID of the parent folder. If null or not provided, the folder
            will be created at the root level of the workspace.
      title: CreateFolderRequest
    CreateFolderSuccessResponse:
      type: object
      properties:
        success:
          type: boolean
          description: Indicates if the operation was successful
        folder:
          $ref: '#/components/schemas/Folder'
      title: CreateFolderSuccessResponse
    FolderExistsError:
      type: object
      properties:
        success:
          type: boolean
        message:
          type: string
      title: FolderExistsError
    UnauthorizedError:
      type: object
      properties:
        error:
          type: string
        message:
          type: string
      title: UnauthorizedError
    ParentFolderNotFoundError:
      type: object
      properties:
        success:
          type: boolean
        message:
          type: string
      title: ParentFolderNotFoundError
    Folder:
      type: object
      properties:
        id:
          type: integer
          description: Unique identifier for the folder
        name:
          type: string
          description: The name of the folder
        created_at:
          type: string
          format: date-time
          description: Timestamp when the folder was created
        updated_at:
          type: string
          format: date-time
          description: Timestamp when the folder was last updated
        path:
          type: array
          nullable: true
          items:
            type: object
          description: >-
            JSON array representing the folder hierarchy path. Contains the IDs
            and names of all parent folders. Null for root-level folders.
        workspace_id:
          type: integer
          description: ID of the workspace this folder belongs to
        parent_id:
          type: integer
          nullable: true
          description: ID of the parent folder. Null for root-level folders.
      title: Folder

````