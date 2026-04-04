# Source: https://docs.pinecone.io/reference/cli/command-reference.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.pinecone.io/llms.txt
> Use this file to discover all available pages before exploring further.

# CLI command reference

<Note>
  This feature is in [public preview](/release-notes/feature-availability).
</Note>

This document provides a complete reference for all Pinecone CLI commands.

## Command structure

The Pinecone CLI uses a hierarchical command structure. Each command consists of a primary command followed by one or more subcommands and optional flags.

```bash  theme={null}
pc <command> <subcommand> [flags]
pc <command> <subcommand> <subcommand> [flags]
```

For example:

```bash  theme={null}
# Top-level command with flags
pc target -o "organization-name" -p "project-name"

# Command (index) and subcommand (list)
pc index list

# Command (index) and subcommand (create) with flags
pc index create \
  --name my-index \
  --dimension 1536 \
  --metric cosine \
  --cloud aws \
  --region us-east-1

# Command (auth) and nested subcommands (local-keys prune) with flags
pc auth local-keys prune --id proj-abc123 --skip-confirmation
```

## Getting help

The CLI provides help for commands at every level:

```bash  theme={null}
# top-level help
pc --help
pc -h

# command help
pc auth --help
pc index --help
pc project --help

# subcommmand help
pc index create --help
pc project create --help
pc auth configure --help

# nested subcommand help
pc auth local-keys prune --help
```

## Exit codes

All commands return exit code `0` for success and `1` for error.

## Available commands

This section describes all commands offered by the Pinecone CLI.

### Top-level commands

<AccordionGroup>
  <Accordion title="pc login (Authenticate via user login)">
    **Description**

    Authenticate via a web browser. After login, set a [target org and project](/reference/cli/target-context) with `pc target` before accessing data. This command defaults to an initial organization and project to which
    you have access (these values display in the terminal), but you can change them with `pc target`.

    **Usage**

    ```bash  theme={null}
    pc login
    ```

    **Flags**

    None

    **Global Flags**

    | Long flag | Short flag | Description           |
    | :-------- | :--------- | :-------------------- |
    | `--help`  | `-h`       | Show help information |
    | `--quiet` | `-q`       | Suppress output       |

    **Example**

    ```bash  theme={null}
    # Log in via browser
    pc login

    # Then set target context
    pc target -o "my-org" -p "my-project"
    ```

    <Note>
      This is an alias for `pc auth login`. Both commands perform the same operation.
    </Note>
  </Accordion>

  <Accordion title="pc logout (Clear credentials / log out)">
    **Description**

    Clears all authentication data from local storage, including:

    * User login token
    * Service account credentials (client ID and secret)
    * Default (manually specified) API key
    * Locally managed keys (for all projects)
    * Target organization and project context

    **Usage**

    ```bash  theme={null}
    pc logout
    ```

    **Flags**

    None

    **Global Flags**

    | Long flag | Short flag | Description           |
    | :-------- | :--------- | :-------------------- |
    | `--help`  | `-h`       | Show help information |
    | `--quiet` | `-q`       | Suppress output       |

    **Example**

    ```bash  theme={null}
    # Clear all credentials and context
    pc logout
    ```

    <Note>
      This is an alias for `pc auth logout`. Both commands perform the same operation. Does not delete managed API keys from Pinecone's servers. Run `pc auth local-keys prune` before logging out to fully clean up.
    </Note>
  </Accordion>

  <Accordion title="pc target (Set target organization and project)">
    **Description**

    Set the target organization and project for the CLI. Supports interactive organization and project selection or direct specification via flags.  For details, see [CLI target context](/reference/cli/target-context).

    **Usage**

    ```bash  theme={null}
    pc target [flags]
    ```

    **Flags**

    | Long flag           | Short flag | Description                    |
    | :------------------ | :--------- | :----------------------------- |
    | `--clear`           |            | Clear target context           |
    | `--json`            |            | Output in JSON format          |
    | `--org`             | `-o`       | Organization name              |
    | `--organization-id` |            | Organization ID                |
    | `--project`         | `-p`       | Project name                   |
    | `--project-id`      |            | Project ID                     |
    | `--show`            | `-s`       | Display current target context |

    **Global Flags**

    | Long flag | Short flag | Description           |
    | :-------- | :--------- | :-------------------- |
    | `--help`  | `-h`       | Show help information |
    | `--quiet` | `-q`       | Suppress output       |

    **Example**

    ```bash  theme={null}
    # Interactive targeting after login
    pc login
    pc target

    # Set specific organization and project
    pc target -o "my-org" -p "my-project"

    # Show current context
    pc target --show

    # Clear all context
    pc target --clear
    ```
  </Accordion>

  <Accordion title="pc version (Show CLI version)">
    **Description**

    Displays version information for the CLI, including the version number, commit SHA, and build date.

    **Usage**

    ```bash  theme={null}
    pc version
    ```

    **Flags**

    None

    **Global Flags**

    | Long flag | Short flag | Description           |
    | :-------- | :--------- | :-------------------- |
    | `--help`  | `-h`       | Show help information |
    | `--quiet` | `-q`       | Suppress output       |

    **Example**

    ```bash  theme={null}
    # Display version information
    pc version
    ```
  </Accordion>

  <Accordion title="pc whoami (Show current user)">
    **Description**

    Displays information about the currently authenticated user. To use this command, you must be authenticated via user login.

    **Usage**

    ```bash  theme={null}
    pc whoami
    ```

    **Flags**

    None

    **Global Flags**

    | Long flag | Short flag | Description           |
    | :-------- | :--------- | :-------------------- |
    | `--help`  | `-h`       | Show help information |
    | `--quiet` | `-q`       | Suppress output       |

    **Example**

    ```bash  theme={null}
    pc whoami
    ```

    <Note>
      This is an alias for `pc auth whoami`. Both commands perform the same operation.
    </Note>
  </Accordion>
</AccordionGroup>

### Authentication

<AccordionGroup>
  <Accordion title="pc auth clear (Clear specific credentials)">
    **Description**

    Selectively clears specific authentication data without affecting other credentials. At least one flag is required.

    **Usage**

    ```bash  theme={null}
    pc auth clear [flags]
    ```

    **Flags**

    | Long flag           | Short flag | Description                                         |
    | :------------------ | :--------- | :-------------------------------------------------- |
    | `--api-key`         |            | Clear only the default (manually specified) API key |
    | `--service-account` |            | Clear only service account credentials              |

    **Global Flags**

    | Long flag | Short flag | Description           |
    | :-------- | :--------- | :-------------------- |
    | `--help`  | `-h`       | Show help information |
    | `--quiet` | `-q`       | Suppress output       |

    **Example**

    ```bash  theme={null}
    # Clear only the default (manually specified) API key
    pc auth clear --api-key
    pc auth status

    # Clear service account
    pc auth clear --service-account
    ```

    <Note>
      More surgical than `pc auth logout`. Does not clear user login token or managed keys. For those, use `pc auth logout` or `pc auth local-keys prune`.
    </Note>
  </Accordion>

  <Accordion title="pc auth configure (Configure service account or API key)">
    **Description**

    Configures service account credentials or a default (manually specified) API key.

    Service accounts automatically target the organization and prompt for project selection, unless there is only one project. A default API key overrides any previously specified target organization/project context. When setting a service account, this operation clears the user login token, if one exists.
    For details, see [CLI target context](/reference/cli/target-context).

    **Usage**

    ```bash  theme={null}
    pc auth configure [flags]
    ```

    **Flags**

    | Long flag               | Short flag | Description                                          |
    | :---------------------- | :--------- | :--------------------------------------------------- |
    | `--api-key`             |            | Default API key to use for authentication            |
    | `--client-id`           |            | Service account client ID                            |
    | `--client-secret`       |            | Service account client secret                        |
    | `--client-secret-stdin` |            | Read client secret from stdin                        |
    | `--json`                |            | Output in JSON format                                |
    | `--project-id`          | `-p`       | Target project ID (optional, interactive if omitted) |
    | `--prompt-if-missing`   |            | Prompt for missing credentials                       |

    **Global Flags**

    | Long flag | Short flag | Description           |
    | :-------- | :--------- | :-------------------- |
    | `--help`  | `-h`       | Show help information |
    | `--quiet` | `-q`       | Suppress output       |

    **Example**

    ```bash  theme={null}
    # Service account setup (auto-targets org and prompts for project)
    pc auth configure --client-id my-id --client-secret my-secret

    # Service account with specific project
    pc auth configure \
      --client-id my-id \
      --client-secret my-secret \
      -p proj-123

    # Default API key (overrides any target context)
    pc auth configure --api-key pcsk_abc123
    ```

    <Note>
      `pc auth configure --api-key "YOUR_API_KEY"` does the same thing as `pc config set-api-key "YOUR_API_KEY"`. To learn about targeting a project after authenticating with a service account, see [CLI target context](/reference/cli/target-context).
    </Note>
  </Accordion>

  <Accordion title="pc auth local-keys list (List managed keys)">
    **Description**

    Displays all [managed API keys](/reference/cli/authentication#managed-keys) stored locally by the CLI, with various details.

    **Usage**

    ```bash  theme={null}
    pc auth local-keys list [flags]
    ```

    **Flags**

    | Long flag  | Short flag | Description                                |
    | :--------- | :--------- | :----------------------------------------- |
    | `--json`   |            | Output in JSON format                      |
    | `--reveal` |            | Show the actual API key values (sensitive) |

    **Global Flags**

    | Long flag | Short flag | Description           |
    | :-------- | :--------- | :-------------------- |
    | `--help`  | `-h`       | Show help information |
    | `--quiet` | `-q`       | Suppress output       |

    **Example**

    ```bash  theme={null}
    # List all locally managed keys
    pc auth local-keys list

    # Show key values
    pc auth local-keys list --reveal

    # After storing a key
    pc api-key create -n "my-key" --store
    pc auth local-keys list
    ```
  </Accordion>

  <Accordion title="pc auth local-keys prune (Delete managed keys)">
    **Description**

    Deletes locally stored [managed API keys](/reference/cli/authentication#managed-keys) from local storage and Pinecone's servers. Filters by origin (`cli`/`user`/`all`) or project ID.

    **Usage**

    ```bash  theme={null}
    pc auth local-keys prune [flags]
    ```

    **Flags**

    | Long flag             | Short flag | Description                                                 |
    | :-------------------- | :--------- | :---------------------------------------------------------- |
    | `--dry-run`           |            | Preview deletions without applying                          |
    | `--id`                |            | Prune keys for specific project ID only                     |
    | `--json`              |            | Output in JSON format                                       |
    | `--origin`            | `-o`       | Filter by origin - `cli`, `user`, or `all` (default: `all`) |
    | `--skip-confirmation` |            | Skip confirmation prompt                                    |

    **Global Flags**

    | Long flag | Short flag | Description           |
    | :-------- | :--------- | :-------------------- |
    | `--help`  | `-h`       | Show help information |
    | `--quiet` | `-q`       | Suppress output       |

    **Example**

    ```bash  theme={null}
    # Preview deletions
    pc auth local-keys prune --dry-run

    # Delete CLI-created keys only
    pc auth local-keys prune -o cli --skip-confirmation

    # Delete for specific project
    pc auth local-keys prune --id proj-abc123

    # Before/after check
    pc auth local-keys list
    pc auth local-keys prune -o cli
    pc auth local-keys list
    ```

    <Note>
      This deletes keys from both local storage and Pinecone servers. Use `--dry-run` to preview before committing.
    </Note>
  </Accordion>

  <Accordion title="pc auth login (Authenticate via user login)">
    **Description**

    Authenticate via user login in the web browser. After login, [set a target org and project](/reference/cli/target-context).

    **Usage**

    ```bash  theme={null}
    pc auth login
    pc login  # shorthand
    ```

    **Flags**

    None

    **Global Flags**

    | Long flag | Short flag | Description           |
    | :-------- | :--------- | :-------------------- |
    | `--help`  | `-h`       | Show help information |
    | `--quiet` | `-q`       | Suppress output       |

    **Example**

    ```bash  theme={null}
    # Login and set target
    pc auth login
    pc target -o "my-org" -p "my-project"
    pc index list
    ```

    <Note>
      Tokens expire after 30 minutes, but they refresh automatically for up to 24 hours. After that point, you must re-authenticate. Logging in clears any existing service account credentials. This command does the same thing as `pc login`.
    </Note>
  </Accordion>

  <Accordion title="pc auth logout (Clear authentication credentials)">
    **Description**

    Clears all authentication data from local storage, including:

    * User login token
    * Service account credentials (client ID and secret)
    * Default (manually specified) API key
    * Locally managed keys (for all projects)
    * Target organization and project context

    **Usage**

    ```bash  theme={null}
    pc auth logout
    ```

    **Flags**

    None

    **Global Flags**

    | Long flag | Short flag | Description           |
    | :-------- | :--------- | :-------------------- |
    | `--help`  | `-h`       | Show help information |
    | `--quiet` | `-q`       | Suppress output       |

    **Example**

    ```bash  theme={null}
    # Clear all credentials and context
    pc auth logout
    ```

    <Note>
      This command does the same thing as `pc logout`. Does not delete managed API keys from Pinecone's servers. Run `pc auth local-keys prune` before logging out to fully clean up.
    </Note>
  </Accordion>

  <Accordion title="pc auth status (Show authentication status)">
    **Description**

    Shows details about all configured authentication methods.

    **Usage**

    ```bash  theme={null}
    pc auth status [flags]
    ```

    **Flags**

    | Long flag | Short flag | Description           |
    | :-------- | :--------- | :-------------------- |
    | `--json`  |            | Output in JSON format |

    **Global Flags**

    | Long flag | Short flag | Description           |
    | :-------- | :--------- | :-------------------- |
    | `--help`  | `-h`       | Show help information |
    | `--quiet` | `-q`       | Suppress output       |

    **Example**

    ```bash  theme={null}
    # Check status after login
    pc auth login
    pc auth status

    # JSON output for scripting
    pc auth status --json
    ```
  </Accordion>

  <Accordion title="pc auth whoami (Show current user information)">
    **Description**

    Displays information about the currently authenticated user. To use this command, you must be authenticated via user login.

    **Usage**

    ```bash  theme={null}
    pc auth whoami
    ```

    **Flags**

    None

    **Global Flags**

    | Long flag | Short flag | Description           |
    | :-------- | :--------- | :-------------------- |
    | `--help`  | `-h`       | Show help information |
    | `--quiet` | `-q`       | Suppress output       |

    **Example**

    ```bash  theme={null}
    pc auth whoami
    ```

    <Note>
      This command does the same thing as `pc whoami`.
    </Note>
  </Accordion>
</AccordionGroup>

### Indexes

<AccordionGroup>
  <Accordion title="pc index configure (Update index configuration)">
    **Description**

    Modifies the configuration of an existing index.

    **Usage**

    ```bash  theme={null}
    pc index configure [flags]
    ```

    **Flags**

    | Long flag               | Short flag | Description                                                    |
    | :---------------------- | :--------- | :------------------------------------------------------------- |
    | `--deletion_protection` | `-p`       | Enable or disable deletion protection -`enabled` or `disabled` |
    | `--json`                |            | Output in JSON format                                          |
    | `--name`                | `-n`       | Index name (required)                                          |

    **Global Flags**

    | Long flag | Short flag | Description           |
    | :-------- | :--------- | :-------------------- |
    | `--help`  | `-h`       | Show help information |
    | `--quiet` | `-q`       | Suppress output       |

    **Example**

    ```bash  theme={null}
    # Enable deletion protection
    pc index configure -n my-index -p enabled

    # Verify changes
    pc index describe -n my-index
    ```

    <Note>
      Configuration changes may take some time to take effect.
    </Note>
  </Accordion>

  <Accordion title="pc index create (Create a new index)">
    **Description**

    Creates a new serverless index in your Pinecone project, with various configuration optons.

    **Usage**

    ```bash  theme={null}
    pc index create [flags]
    ```

    **Flags**

    | Long flag               | Short flag | Description                                                               |
    | :---------------------- | :--------- | :------------------------------------------------------------------------ |
    | `--cloud`               | `-c`       | Cloud provider - `aws`, `gcp`, or `azure` (required for serverless)       |
    | `--deletion_protection` |            | Deletion protection - `enabled` or `disabled`                             |
    | `--dimension`           | `-d`       | Vector dimension (required for standard indexes, optional for integrated) |
    | `--field_map`           |            | Field mapping for integrated embedding (JSON map)                         |
    | `--json`                |            | Output in JSON format                                                     |
    | `--metric`              | `-m`       | Similarity metric - `cosine`, `euclidean`, or `dotproduct` (required)     |
    | `--model`               |            | Integrated embedding model name                                           |
    | `--name`                | `-n`       | Index name (required)                                                     |
    | `--read_parameters`     |            | Read parameters for embedding model (JSON map)                            |
    | `--region`              | `-r`       | Cloud region                                                              |
    | `--source_collection`   |            | Name of the source collection from which to create the index              |
    | `--tags`                |            | Custom user tags (key=value pairs)                                        |
    | `--vector_type`         | `-v`       | Vector type - `dense` or `sparse` (serverless only)                       |
    | `--write_parameters`    |            | Write parameters for embedding model (JSON map)                           |

    **Global Flags**

    | Long flag | Short flag | Description           |
    | :-------- | :--------- | :-------------------- |
    | `--help`  | `-h`       | Show help information |
    | `--quiet` | `-q`       | Suppress output       |

    **Example**

    ```bash  theme={null}
    # Create serverless index
    pc index create -n my-index -d 1536 -m cosine -c aws -r us-east-1

    # With integrated embedding model
    pc index create \
      -n my-index \
      -m cosine \
      -c aws \
      -r us-east-1 \
      --model multilingual-e5-large

    # With deletion protection
    pc index create \
      -n my-index \
      -d 1536 \
      -m cosine \
      -c aws \
      -r us-west-2 \
      --deletion_protection enabled

    # From collection
    pc index create \
      -n my-index \
      -d 1536 \
      -m cosine \
      -c aws \
      -r eu-west-1 \
      --source_collection my-collection
    ```

    <Note>
      For a list of valid regions for a serverless index, see [Create a serverless index](/guides/index-data/create-an-index).
    </Note>
  </Accordion>

  <Accordion title="pc index delete (Delete an index)">
    **Description**

    Permanently deletes an index and all its data. This operation cannot be undone.

    **Usage**

    ```bash  theme={null}
    pc index delete [flags]
    ```

    **Flags**

    | Long flag | Short flag | Description           |
    | :-------- | :--------- | :-------------------- |
    | `--name`  | `-n`       | Index name (required) |

    **Global Flags**

    | Long flag | Short flag | Description           |
    | :-------- | :--------- | :-------------------- |
    | `--help`  | `-h`       | Show help information |
    | `--quiet` | `-q`       | Suppress output       |

    **Example**

    ```bash  theme={null}
    # Delete an index
    pc index delete -n my-index

    # List before and after
    pc index list
    pc index delete -n test-index
    pc index list
    ```
  </Accordion>

  <Accordion title="pc index describe (Show index details)">
    **Description**

    Displays detailed configuration and status information for a specific index.

    **Usage**

    ```bash  theme={null}
    pc index describe [flags]
    ```

    **Flags**

    | Long flag | Short flag | Description           |
    | :-------- | :--------- | :-------------------- |
    | `--json`  |            | Output in JSON format |
    | `--name`  | `-n`       | Index name (required) |

    **Global Flags**

    | Long flag | Short flag | Description           |
    | :-------- | :--------- | :-------------------- |
    | `--help`  | `-h`       | Show help information |
    | `--quiet` | `-q`       | Suppress output       |

    **Example**

    ```bash  theme={null}
    # Describe an index
    pc index describe -n my-index

    # JSON output
    pc index describe -n my-index --json

    # Check newly created index
    pc index create -n test-index -d 1536 -m cosine -c aws -r us-east-1
    pc index describe -n test-index
    ```
  </Accordion>

  <Accordion title="pc index list (List all indexes)">
    **Description**

    Displays all indexes in your current target project, including various details.

    **Usage**

    ```bash  theme={null}
    pc index list [flags]
    ```

    **Flags**

    | Long flag | Short flag | Description           |
    | :-------- | :--------- | :-------------------- |
    | `--json`  |            | Output in JSON format |

    **Global Flags**

    | Long flag | Short flag | Description           |
    | :-------- | :--------- | :-------------------- |
    | `--help`  | `-h`       | Show help information |
    | `--quiet` | `-q`       | Suppress output       |

    **Example**

    ```bash  theme={null}
    # List all indexes
    pc index list

    # JSON output for scripting
    pc index list --json

    # After creating indexes
    pc index create -n test-1 -d 768 -m cosine -c aws -r us-east-1
    pc index list
    ```
  </Accordion>
</AccordionGroup>

### Projects

<AccordionGroup>
  <Accordion title="pc project create (Create a new project)">
    **Description**

    Creates a new project in your [target organization](/reference/cli/target-context), using the specified configuration.

    **Usage**

    ```bash  theme={null}
    pc project create [flags]
    ```

    **Flags**

    | Long flag            | Short flag | Description                                                    |
    | :------------------- | :--------- | :------------------------------------------------------------- |
    | `--force-encryption` |            | Enable encryption with CMEK                                    |
    | `--json`             |            | Output in JSON format                                          |
    | `--name`             | `-n`       | Project name (required)                                        |
    | `--target`           |            | Automatically target the project in the CLI after it's created |

    **Global Flags**

    | Long flag | Short flag | Description           |
    | :-------- | :--------- | :-------------------- |
    | `--help`  | `-h`       | Show help information |
    | `--quiet` | `-q`       | Suppress output       |

    **Example**

    ```bash  theme={null}
    # Basic project creation
    pc project create -n "demo-project"
    ```
  </Accordion>

  <Accordion title="pc project delete (Delete a project)">
    **Description**

    Permanently deletes a project and all its resources. This operation cannot be undone.

    **Usage**

    ```bash  theme={null}
    pc project delete [flags]
    ```

    **Flags**

    | Long flag             | Short flag | Description                                                 |
    | :-------------------- | :--------- | :---------------------------------------------------------- |
    | `--id`                | `-i`       | Project ID (optional, uses target project if not specified) |
    | `--json`              |            | Output in JSON format                                       |
    | `--skip-confirmation` |            | Skip confirmation prompt                                    |

    **Global Flags**

    | Long flag | Short flag | Description           |
    | :-------- | :--------- | :-------------------- |
    | `--help`  | `-h`       | Show help information |
    | `--quiet` | `-q`       | Suppress output       |

    **Example**

    ```bash  theme={null}
    # Delete target project
    pc project delete

    # Delete specific project
    pc project delete -i proj-abc123

    # Skip confirmation
    pc project delete -i proj-abc123 --skip-confirmation
    ```

    <Note>
      Must delete all indexes and collections in the project first. If the deleted project is your current target, set a new target after deleting it.
    </Note>
  </Accordion>

  <Accordion title="pc project describe (Show project details)">
    **Description**

    Displays detailed information about a specific project, including various details.

    **Usage**

    ```bash  theme={null}
    pc project describe [flags]
    ```

    **Flags**

    | Long flag | Short flag | Description           |
    | :-------- | :--------- | :-------------------- |
    | `--id`    | `-i`       | Project ID (required) |
    | `--json`  |            | Output in JSON format |

    **Global Flags**

    | Long flag | Short flag | Description           |
    | :-------- | :--------- | :-------------------- |
    | `--help`  | `-h`       | Show help information |
    | `--quiet` | `-q`       | Suppress output       |

    **Example**

    ```bash  theme={null}
    # Describe a project
    pc project describe -i proj-abc123

    # JSON output
    pc project describe -i proj-abc123 --json

    # Find ID and describe
    pc project list
    pc project describe -i proj-abc123
    ```
  </Accordion>

  <Accordion title="pc project list (List all projects)">
    **Description**

    Displays all projects in your [target organization](/reference/cli/target-context), including various details.

    **Usage**

    ```bash  theme={null}
    pc project list [flags]
    ```

    **Flags**

    | Long flag | Short flag | Description           |
    | :-------- | :--------- | :-------------------- |
    | `--json`  |            | Output in JSON format |

    **Global Flags**

    | Long flag | Short flag | Description           |
    | :-------- | :--------- | :-------------------- |
    | `--help`  | `-h`       | Show help information |
    | `--quiet` | `-q`       | Suppress output       |

    **Example**

    ```bash  theme={null}
    # List all projects
    pc project list

    # JSON output
    pc project list --json

    # List after login
    pc auth login
    pc auth target -o "my-org"
    pc project list
    ```
  </Accordion>

  <Accordion title="pc project update (Update project settings)">
    **Description**

    Modifies the configuration of the [target project](/reference/cli/target-context), or a specific project ID.

    **Usage**

    ```bash  theme={null}
    pc project update [flags]
    ```

    **Flags**

    | Long flag            | Short flag | Description                         |
    | :------------------- | :--------- | :---------------------------------- |
    | `--force-encryption` | `-f`       | Enable/disable encryption with CMEK |
    | `--id`               | `-i`       | Project ID (required)               |
    | `--json`             |            | Output in JSON format               |
    | `--name`             | `-n`       | New project name                    |

    **Global Flags**

    | Long flag | Short flag | Description           |
    | :-------- | :--------- | :-------------------- |
    | `--help`  | `-h`       | Show help information |
    | `--quiet` | `-q`       | Suppress output       |

    **Example**

    ```bash  theme={null}
    # Update name
    pc project update -i proj-abc123 -n "new-name"
    ```
  </Accordion>
</AccordionGroup>

### Organizations

<AccordionGroup>
  <Accordion title="pc organization delete (Delete an organization)">
    **Description**

    Permanently deletes an organization and all its resources. This operation cannot be undone.

    **Usage**

    ```bash  theme={null}
    pc organization delete [flags]
    ```

    **Flags**

    | Long flag             | Short flag | Description                |
    | :-------------------- | :--------- | :------------------------- |
    | `--id`                | `-i`       | Organization ID (required) |
    | `--json`              |            | Output in JSON format      |
    | `--skip-confirmation` |            | Skip confirmation prompt   |

    **Global Flags**

    | Long flag | Short flag | Description           |
    | :-------- | :--------- | :-------------------- |
    | `--help`  | `-h`       | Show help information |
    | `--quiet` | `-q`       | Suppress output       |

    **Example**

    ```bash  theme={null}
    # Delete an organization
    pc organization delete -i org-abc123

    # Skip confirmation
    pc organization delete -i org-abc123 --skip-confirmation
    ```

    <Note>
      This is a highly destructive action. Deletion is permanent. If the deleted organization is your current [target](/reference/cli/target-context), set a new target after deleting.
    </Note>
  </Accordion>

  <Accordion title="pc organization describe (Show organization details)">
    **Description**

    Displays detailed information about a specific organization, including name, ID, creation date, payment status, plan, and support tier.

    **Usage**

    ```bash  theme={null}
    pc organization describe [flags]
    ```

    **Flags**

    | Long flag | Short flag | Description                |
    | :-------- | :--------- | :------------------------- |
    | `--id`    | `-i`       | Organization ID (required) |
    | `--json`  |            | Output in JSON format      |

    **Global Flags**

    | Long flag | Short flag | Description           |
    | :-------- | :--------- | :-------------------- |
    | `--help`  | `-h`       | Show help information |
    | `--quiet` | `-q`       | Suppress output       |

    **Example**

    ```bash  theme={null}
    # Describe an organization
    pc organization describe -i org-abc123

    # JSON output
    pc organization describe -i org-abc123 --json

    # Find ID and describe
    pc organization list
    pc organization describe -i org-abc123
    ```
  </Accordion>

  <Accordion title="pc organization list (List organizations)">
    **Description**

    Displays all organizations that the authenticated user has access to, including name, ID, creation date, payment status, plan, and support tier.

    **Usage**

    ```bash  theme={null}
    pc organization list [flags]
    ```

    **Flags**

    | Long flag | Short flag | Description           |
    | :-------- | :--------- | :-------------------- |
    | `--json`  |            | Output in JSON format |

    **Global Flags**

    | Long flag | Short flag | Description           |
    | :-------- | :--------- | :-------------------- |
    | `--help`  | `-h`       | Show help information |
    | `--quiet` | `-q`       | Suppress output       |

    **Example**

    ```bash  theme={null}
    # List all organizations
    pc organization list

    # JSON output
    pc organization list --json

    # List after login
    pc auth login
    pc organization list
    ```
  </Accordion>

  <Accordion title="pc organization update (Update organization settings)">
    **Description**

    Modifies the configuration of the [target organization](/reference/cli/target-context), or a specific organization ID.

    **Usage**

    ```bash  theme={null}
    pc organization update [flags]
    ```

    **Flags**

    | Long flag | Short flag | Description                |
    | :-------- | :--------- | :------------------------- |
    | `--id`    | `-i`       | Organization ID (required) |
    | `--json`  |            | Output in JSON format      |
    | `--name`  | `-n`       | New organization name      |

    **Global Flags**

    | Long flag | Short flag | Description           |
    | :-------- | :--------- | :-------------------- |
    | `--help`  | `-h`       | Show help information |
    | `--quiet` | `-q`       | Suppress output       |

    **Example**

    ```bash  theme={null}
    # Update name
    pc organization update -i org-abc123 -n "new-name"

    # Verify changes
    pc organization update -i org-abc123 -n "Acme Corp"
    pc organization describe -i org-abc123
    ```
  </Accordion>
</AccordionGroup>

### API keys

<AccordionGroup>
  <Accordion title="pc api-key create (Create a new API key)">
    **Description**

    Creates a new API key for the current [target project](/reference/cli/target-context) or a specific project ID. Optionally stores the key locally for CLI use.

    **Usage**

    ```bash  theme={null}
    pc api-key create [flags]
    ```

    **Flags**

    | Long flag | Short flag | Description                                                                             |
    | :-------- | :--------- | :-------------------------------------------------------------------------------------- |
    | `--id`    | `-i`       | Project ID (optional, uses target project if not specified)                             |
    | `--json`  |            | Output in JSON format                                                                   |
    | `--name`  | `-n`       | Key name (required)                                                                     |
    | `--roles` |            | Roles to assign (default: `ProjectEditor`)                                              |
    | `--store` |            | Store the key locally for CLI use (automatically replaces any existing CLI-managed key) |

    **Global Flags**

    | Long flag | Short flag | Description           |
    | :-------- | :--------- | :-------------------- |
    | `--help`  | `-h`       | Show help information |
    | `--quiet` | `-q`       | Suppress output       |

    **Example**

    ```bash  theme={null}
    # Basic key creation
    pc api-key create -n "my-key"

    # Create and store locally
    pc api-key create -n "my-key" --store

    # Create with specific role
    pc api-key create -n "my-key" --store --roles ProjectEditor

    # Create for specific project
    pc api-key create -n "my-key" -i proj-abc123
    ```

    <Note>
      API keys are scoped to a specific organization and project.
    </Note>
  </Accordion>

  <Accordion title="pc api-key delete (Delete an API key)">
    **Description**

    Permanently deletes an API key. Applications using this key immediately lose access.

    **Usage**

    ```bash  theme={null}
    pc api-key delete [flags]
    ```

    **Flags**

    | Long flag             | Short flag | Description              |
    | :-------------------- | :--------- | :----------------------- |
    | `--id`                | `-i`       | API key ID (required)    |
    | `--skip-confirmation` |            | Skip confirmation prompt |

    **Global Flags**

    | Long flag | Short flag | Description           |
    | :-------- | :--------- | :-------------------- |
    | `--help`  | `-h`       | Show help information |
    | `--quiet` | `-q`       | Suppress output       |

    **Example**

    ```bash  theme={null}
    # Delete an API key
    pc api-key delete -i key-abc123

    # Skip confirmation
    pc api-key delete -i key-abc123 --skip-confirmation

    # Delete and clean up local storage
    pc api-key delete -i key-abc123
    pc auth local-keys prune --skip-confirmation
    ```

    <Note>
      Deletion is permanent. Applications using this key immediately lose access to Pinecone.
    </Note>
  </Accordion>

  <Accordion title="pc api-key describe (Show API key details)">
    **Description**

    Displays detailed information about a specific API key, including its name, ID, project ID, and roles.

    **Usage**

    ```bash  theme={null}
    pc api-key describe [flags]
    ```

    **Flags**

    | Long flag | Short flag | Description           |
    | :-------- | :--------- | :-------------------- |
    | `--id`    | `-i`       | API key ID (required) |
    | `--json`  |            | Output in JSON format |

    **Global Flags**

    | Long flag | Short flag | Description           |
    | :-------- | :--------- | :-------------------- |
    | `--help`  | `-h`       | Show help information |
    | `--quiet` | `-q`       | Suppress output       |

    **Example**

    ```bash  theme={null}
    # Describe an API key
    pc api-key describe -i key-abc123

    # JSON output
    pc api-key describe -i key-abc123 --json

    # Find ID and describe
    pc api-key list
    pc api-key describe -i key-abc123
    ```

    <Note>
      Does not display the actual key value.
    </Note>
  </Accordion>

  <Accordion title="pc api-key list (List all API keys)">
    **Description**

    Displays a list of all of the [target project's](/reference/cli/target-context) API keys, as found in  Pinecone (regardless of whether they are stored locally by the CLI). Displays various details about each key, including name, ID, project ID, and roles.

    **Usage**

    ```bash  theme={null}
    pc api-key list [flags]
    ```

    **Flags**

    | Long flag | Short flag | Description                                                 |
    | :-------- | :--------- | :---------------------------------------------------------- |
    | `--id`    | `-i`       | Project ID (optional, uses target project if not specified) |
    | `--json`  |            | Output in JSON format                                       |

    **Global Flags**

    | Long flag | Short flag | Description           |
    | :-------- | :--------- | :-------------------- |
    | `--help`  | `-h`       | Show help information |
    | `--quiet` | `-q`       | Suppress output       |

    **Example**

    ```bash  theme={null}
    # List keys for target project
    pc api-key list

    # List for specific project
    pc api-key list -i proj-abc123

    # JSON output
    pc api-key list --json
    ```

    <Note>
      Does not display key values.
    </Note>
  </Accordion>

  <Accordion title="pc api-key update (Update API key settings)">
    **Description**

    Updates the name and roles of an API key.

    **Usage**

    ```bash  theme={null}
    pc api-key update [flags]
    ```

    **Flags**

    | Long flag | Short flag | Description           |
    | :-------- | :--------- | :-------------------- |
    | `--id`    | `-i`       | API key ID (required) |
    | `--json`  | `-j`       | Output in JSON format |
    | `--name`  | `-n`       | New key name          |
    | `--roles` | `-r`       | Roles to assign       |

    **Global Flags**

    | Long flag | Short flag | Description           |
    | :-------- | :--------- | :-------------------- |
    | `--help`  | `-h`       | Show help information |
    | `--quiet` | `-q`       | Suppress output       |

    **Example**

    ```bash  theme={null}
    # Update name
    pc api-key update -i key-abc123 -n "new-name"

    # Update roles
    pc api-key update -i key-abc123 -r ProjectEditor

    # Verify changes
    pc api-key update -i key-abc123 -n "production-key"
    pc api-key describe -i key-abc123
    ```

    <Note>
      Cannot change the actual key. If you need a different key, create a new one.
    </Note>
  </Accordion>
</AccordionGroup>

### Config

<AccordionGroup>
  <Accordion title="pc config get-api-key (Show configured API key)">
    **Description**

    Displays the currently configured default (manually specified) API key, if set. By default, the full value of the key is not displayed.

    **Usage**

    ```bash  theme={null}
    pc config get-api-key
    ```

    **Flags**

    | Long flag  | Short flag | Description                               |
    | :--------- | :--------- | :---------------------------------------- |
    | `--reveal` |            | Show the actual API key value (sensitive) |

    **Global Flags**

    | Long flag | Short flag | Description           |
    | :-------- | :--------- | :-------------------- |
    | `--help`  | `-h`       | Show help information |
    | `--quiet` | `-q`       | Suppress output       |

    **Example**

    ```bash  theme={null}
    # Get current API key
    pc config get-api-key

    # Verify after setting
    pc config set-api-key pcsk_abc123
    pc config get-api-key
    ```
  </Accordion>

  <Accordion title="pc config set-api-key (Set default API key)">
    **Description**

    Sets a default API key for the CLI to use for authentication. Provides direct access to control plane operations, but not Admin API operations.

    **Usage**

    ```bash  theme={null}
    pc config set-api-key "YOUR_API_KEY"
    ```

    **Flags**

    None (takes API key as argument)

    **Global Flags**

    | Long flag | Short flag | Description           |
    | :-------- | :--------- | :-------------------- |
    | `--help`  | `-h`       | Show help information |
    | `--quiet` | `-q`       | Suppress output       |

    **Example**

    ```bash  theme={null}
    # Set default API key
    pc config set-api-key pcsk_abc123

    # Use immediately without targeting
    pc config set-api-key pcsk_abc123
    pc index list

    # Verify it's set
    pc auth status
    ```

    <Note>
      `pc config set-api-key "YOUR_API_KEY"` does the same thing as `pc auth configure --api-key "YOUR_API_KEY"`. For control plane operations, a default API key implicitly overrides any previously set [target context](/reference/cli/target-context), because Pinecone API keys are scoped to a specific organization and project.
    </Note>
  </Accordion>

  <Accordion title="pc config set-color (Enable/disable colored output)">
    **Description**

    Enables or disables colored output in CLI responses. Useful for terminal compatibility or log file generation.

    **Usage**

    ```bash  theme={null}
    pc config set-color true
    pc config set-color false
    ```

    **Flags**

    None (takes boolean as argument)

    **Global Flags**

    | Long flag | Short flag | Description           |
    | :-------- | :--------- | :-------------------- |
    | `--help`  | `-h`       | Show help information |
    | `--quiet` | `-q`       | Suppress output       |

    **Example**

    ```bash  theme={null}
    # Enable colored output
    pc config set-color true

    # Disable colored output for CI/CD
    pc config set-color false

    # Test the change
    pc config set-color false
    pc index list
    ```
  </Accordion>
</AccordionGroup>
