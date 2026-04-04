# Source: https://docs.jit.io/docs/jit-teams-sync.md

# Jit Teams sync

By default, Jit uploads GitHub teams and their ownership on GitHub repositories to [Jit teams](https://docs.jit.io/docs/teams).

Use the `sync-teams` scripts as follows:

1. If you are not using GitHub for team management, to manually run this command to sync teams data.
2. To connect teams (also those originating from GitHub) to external resources like AWS accounts or Web Apps.

## Generating API keys

Before working with the sync-teams script, the following API keys must be created.

* **GitHub Personal Access Token (PAT)**, refer to the [Managing your personal access tokens](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens#creating-a-personal-access-token-classic) guide to generate.\
  We recommend generating a fine-grained PAT with read-only access to the organization.
* **Jit API key**, generated from the Jit platform, under [Settings > Users and Permissions](https://docs.jit.io/docs/managing-users), go to **API Tokens**, and create a token with an appropriate name and `member` role. Make sure to copy the values.

## Sync teams command

This command has three sub-commands:

| Command   | Description                                                                                                                                                             |
| :-------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| install   | Ensures Python 3 is installed, sets up a virtual environment and installs the required dependencies.                                                                    |
| configure | Prompts you to input configuration details like the GitHub organization name, API client ID, client secret and GitHub token. The responses are written to an .env file. |
| run       | Activates the virtual environment and runs two Python scripts in succession to generate teams.                                                                          |

## Usage examples

1. Make sure you have installed the prerequisites and cloned the repo.
   ```Text Amazon Linux
   sudo yum install -y git make
   git clone https://github.com/jitsecurity/jit-customer-scripts.git
   cd jit-customer-scripts
   ```
   ```Text Ubuntu
   sudo apt update
   sudo apt install -y git make
   git clone https://github.com/jitsecurity/jit-customer-scripts.git
   cd jit-customer-scripts
   ```
2. If you haven't cloned the repo recently, make sure to update it.
   ```
   git pull https://github.com/jitsecurity/jit-customer-scripts.git
   ```
3. Run the sub-command
   ```
   make sync-teams install
   make sync-teams configure
   make sync-teams run
   ```

### Creating teams from GitHub topics

Use the following command to run the script, sync teams and update assets:

To extract the teams from GitHub topics, this command runs the following sub-commands to fetch the repository names and topics from the GitHub API. It then generates the JSON file and syncs between the teams and updates the assets.

```
python src/utils/github_topics_to_json_file.py

python src/scripts/sync_teams.py teams.json
```

To automate the process for this script so that your teams are always synchronized, we recommend using the provided GitHub actions and GitHub secrets discussed below or a similar command.

For more information, see [Classifying repositories with topics](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/classifying-your-repository-with-topics).

### Using a custom JSON file as a source for syncing teams

If you prefer using a custom file as a source for syncing your teams, provide a file with the following structure:

(**Note for GitLab users**: When referencing GitLab projects, provide the relative path from the group to the project, without mentioning the group name. For example, use `"name": "some-subgroup/some-project"`, and **not** `"name": "my-group/some-subgroup/some-project"`.

(**Note for Azure users**: When referencing an Azure resource, the name of the resource should start with the account\_id(Azure tenant ID).`"name": "<azure tenant id>/azure_account"`.

```Text json
{
  "teams": [
    {
      "name": "Team 1",
      "members": [
        "Member 1",
        "Member 2",
        "Member 3"
      ],
      "resources": [
        {
          "type": "repo",
          "name": "github-repository-name",
          "vendor": "github"
        },
        {
          "type": "repo",
          "name": "some-subgroup/nested-subgroup/project1",
          "vendor": "gitlab"
        },
        {
            "type": "repo",
            "name": "bitbucket-repository-name"
            "vendor": "bitbucket"
        },
        {
            "type": "repo",
            "name": "ado-repository-name"
            "vendor": "azure_devops"
        },
        {
          "type": "aws_account",
          "name": "aws_account1",
          "vendor": "aws"
        },
        {
          "type": "azure_account",
          "name": "1234abcd-aa11-2234-8aa8-123456abcd/azure_account",
          "vendor": "azure"
        }
      ]
    },
    {
      "name": "Team 2",
      "members": [
        "Member 1",
        "Member 2",
        "Member 3"
      ],
      "resources": [
        {
          "type": "repo",
          "name": "repo2",
          "vendor": "github"
        },
        {
          "type": "repo",
          "name": "project2",
          "vendor": "gitlab"
        },
        {
          "type": "aws_account",
          "name": "aws_account2",
          "vendor": "aws"
        }
      ]
    }
  ]
}

```

Sync the teams by running the following command and replace the `path/to/teams.json` with the actual path to your JSON file.

```
python scripts/sync_teams.py path/to/teams.json
```

### Excluding names

When creating teams, you can exclude team names by either:

* Using the make configure command.
* Updating the env var in the TEAM\_WILDCARD\_TO\_EXCLUDE .env file.

For example, to exclude teams named `test`, set the following variable:

```
TEAM_WILDCARD_TO_EXCLUDE=\_test_
```

The following topics will be excluded:

* Test
* my-test
* test123
* mytestproject

### Sync teams Github action

You can sync teams using a GitHub action. For example, use this workflow file for the GitHub action:

```
name: Sync Jit Teams
on:
  schedule:
    - cron: "0 3 * * *"
  workflow_dispatch:

jobs:
  sync-teams:
    runs-on: ubuntu-latest
    steps:
    - name: Check out code
      uses: actions/checkout@v3
    - name: Call action
      uses: jitsecurity/jit-sync-teams-github-action@v1.1.0
      with:
        JIT_CLIENT_ID: ${{ secrets.JIT_CLIENT_ID }}
        JIT_CLIENT_SECRET: ${{ secrets.JIT_CLIENT_SECRET }}
        ORGANIZATION_NAME: ${{ github.repository_owner }}
        GITHUB_API_TOKEN: ${{ secrets.MY_GITHUB_API_TOKEN }}
        TEAM_WILDCARD_TO_EXCLUDE: "*dev*, *test*"
```

```
name: Sync Jit Teams
on:
  schedule:
    - cron: "0 3 * * *"
  workflow_dispatch:

jobs:
  sync-teams:
    runs-on: ubuntu-latest
    steps:
    - name: Check out code
      uses: actions/checkout@v3
    - name: Call action
      uses: jitsecurity/jit-sync-teams-github-action@v1.1.0
      with:
        JIT_CLIENT_ID: ${{ secrets.JIT_CLIENT_ID }}
        JIT_CLIENT_SECRET: ${{ secrets.JIT_CLIENT_SECRET }}
        ORGANIZATION_NAME: ${{ github.repository_owner }}
        GITHUB_API_TOKEN: ${{ secrets.MY_GITHUB_API_TOKEN }}
        TEAM_WILDCARD_TO_EXCLUDE: "*dev*, *test*"
```