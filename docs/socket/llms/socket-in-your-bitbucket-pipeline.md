# Source: https://docs.socket.dev/docs/socket-in-your-bitbucket-pipeline.md

# Socket for Bitbucket Pipeline

Socket fights vulnerabilities and provides visibility, defense-in-depth, and proactive supply chain protection for your open source dependencies. It is easy to integrate Socket into your Bitbucket Pipeline to provide an extra layer of security against Supply Chain Attacks.

## Adding Socket to your pipeline

<br />

### Create your Socket Environment variable

1. Create a Socket API Key ([Directions](https://docs.socket.dev/docs/create-socket-api-key-for-cicd))
2. Log into Bitbucket
3. Navigate to your repository
4. Go to **Repository Settings**
5. Go to **Repository variables**
6. Add a New variable

   1. **Name:** SOCKET\_SECURITY\_API\_KEY
   2. **Value:** Your Socket API token
   3. **Secured:** Checked
7. Click **Add**

### Example Bitbucket Pipeline Setup

1. Go to **Source**
2. Select the `...` menu
3. Select **Add file**

   1. **filename:** bitbucket-pipelines.yml
   2. Paste the following YAML or integrate into your existing pipeline

      ```yaml
      # Socket Security Bitbucket Pipelines
      # This pipeline runs Socket Security scans on every commit to any branch
      # The CLI automatically detects most information from the git repository

      image: socketdev/cli:latest

      definitions:
        steps:
          - step: &socket-scan
              name: Socket Security Scan
              script:
                # Run Socket CLI with minimal required parameters
                # The CLI automatically detects:
                # - Repository name from git
                # - Branch name from git
                # - Commit SHA from git
                # - Commit message from git
                # - Committer information from git
                # - Default branch status from git repository
                # - Changed files from git commit
                - |
                  socketcli \
                    --scm bitbucket \
                    --pr-number ${BITBUCKET_PR_ID:-0}
              # Repository variables needed (set in Bitbucket repo settings)
              # SOCKET_SECURITY_API_KEY: Your Socket Security API token

      pipelines:
        # Run on all branches
        branches:
          '**':
            - step: *socket-scan
        
        # Run on pull requests
        pull-requests:
          '**':
            - step: *socket-scan
      ```
4. Commit changes to your main branch or the current branch you are working on

### Testing pipeline

1. Create a new branch
2. Modify or add a `package.json`
3. Create a new Pull request
4. Confirm that the Socket CI pipeline job ran

   <Image align="left" src="https://files.readme.io/a8967560d3b63b1642d43f1d74ebb87d5a3829e7cd75b0a1344f31c80e168dfa-Screenshot_2024-09-23_at_1.43.33_AM.png" />