# Source: https://docs.socket.dev/docs/socket-for-github-actions.md

# Socket for GitHub Actions

Socket fights vulnerabilities and provides visibility, defense-in-depth, and proactive supply chain protection for your open source dependencies. It is easy to integrate Socket into your Github Actions to provide an extra layer of security against Supply Chain Attacks.

## Adding Socket to your Github Actions Workflow

### Create your Socket Environment variables

1. Create a Socket API Key ([Directions](https://docs.socket.dev/docs/create-socket-api-key-for-cicd))
2. Log into your Github Org
3. Set up your Action Secret at either the Repo or Org level
   1. For the repo level
      1. Go to Settings
      2. Secrets and variables
      3. Actions
      4. New repository secret

<br />

### Setup the Github Actions Workflow

The Action Workflow currently uses the auto generated Github Actions token based on the permissions that are requested in the Workflow. The sample Workflow Yaml can be customized to your needs. It currently runs on every push and issue\_comment type event.

1. Go to your repo
2. Create a new file with the name `.github/workflows/socket.yml`
3. Add in the Socket Actions Yaml from below.

```yaml yaml
# Socket Security GitHub Actions Workflow
# This workflow runs Socket Security scans on every commit to any branch
# It automatically detects git repository information and handles different event types

name: socket-security-workflow
run-name: Socket Security Github Action

on:
  push:
    branches: ['**']  # Run on all branches, all commits
  pull_request:
    types: [opened, synchronize, reopened]
  issue_comment:
    types: [created]

# Prevent concurrent runs for the same commit
concurrency:
  group: socket-scan-${{ github.ref }}-${{ github.sha }}
  cancel-in-progress: true

jobs:
  socket-security:
    permissions:
      issues: write
      contents: read
      pull-requests: write
    runs-on: ubuntu-latest
    
    steps:
      - uses: actions/checkout@v4
        with:
          # For PRs, fetch one additional commit for proper diff analysis
          fetch-depth: ${{ github.event_name == 'pull_request' && 2 || 0 }}
      
      - uses: actions/setup-python@v5
        with:
          python-version: '3.12'
      
      - name: Install Socket CLI
        run: pip install socketsecurity --upgrade
      
      - name: Run Socket Security Scan
        env:
          SOCKET_SECURITY_API_KEY: ${{ secrets.SOCKET_SECURITY_API_KEY }}
          GH_API_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: |
          # Determine PR number based on event type
          PR_NUMBER=0
          if [ "${{ github.event_name }}" == "pull_request" ]; then
            PR_NUMBER=${{ github.event.pull_request.number }}
          elif [ "${{ github.event_name }}" == "issue_comment" ]; then
            PR_NUMBER=${{ github.event.issue.number }}
          fi
          
          # Run Socket CLI with minimal required parameters
          # The CLI automatically detects:
          # - Repository name from git
          # - Branch name from git
          # - Commit SHA from git
          # - Commit message from git
          # - Committer information from git
          # - Default branch status from git and GitHub environment
          # - Changed files from git commit
          socketcli \
            --target-path $GITHUB_WORKSPACE \
            --scm github \
            --pr-number $PR_NUMBER

```

#### With Support for Kotlin, Scala, and Gradle

```yaml
# Socket Security GitHub Actions Workflow
# This workflow runs Socket Security scans on every commit to any branch
# It automatically detects git repository information and handles different event types

name: socket-security-workflow
run-name: Socket Security Github Action

on:
  push:
    branches: ['**']  # Run on all branches, all commits
  pull_request:
    types: [opened, synchronize, reopened]
  issue_comment:
    types: [created]

# Prevent concurrent runs for the same commit
concurrency:
  group: socket-scan-${{ github.ref }}-${{ github.sha }}
  cancel-in-progress: true

jobs:
  socket-security:
    permissions:
      issues: write
      contents: read
      pull-requests: write
    runs-on: ubuntu-latest
    
    steps:
      - uses: actions/checkout@v4
        with:
          # For PRs, fetch one additional commit for proper diff analysis
          fetch-depth: ${{ github.event_name == 'pull_request' && 2 || 0 }}
      
      - uses: actions/setup-python@v5
        with:
          python-version: '3.12'

      - uses: actions/setup-node@v4
        with:
          node-version: '20'
      
      - name: Install npm Socket CLI
        run: npm i -g socket
      
      - name: Generate CycloneDX SBOM
        run: |
          socket cdxgen -t gradle -t kotlin -t scala -o socket.cdx.json --install-deps --lifecycle build
      
      - name: Install Socket CLI
        run: pip install socketsecurity --upgrade
      
      - name: Run Socket Security Scan
        env:
          SOCKET_SECURITY_API_KEY: ${{ secrets.SOCKET_SECURITY_API_KEY }}
          GH_API_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: |
          # Determine PR number based on event type
          PR_NUMBER=0
          if [ "${{ github.event_name }}" == "pull_request" ]; then
            PR_NUMBER=${{ github.event.pull_request.number }}
          elif [ "${{ github.event_name }}" == "issue_comment" ]; then
            PR_NUMBER=${{ github.event.issue.number }}
          fi
          
          # Run Socket CLI with minimal required parameters
          # The CLI automatically detects:
          # - Repository name from git
          # - Branch name from git
          # - Commit SHA from git
          # - Commit message from git
          # - Committer information from git
          # - Default branch status from git and GitHub environment
          # - Changed files from git commit
          socketcli \
            --target-path $GITHUB_WORKSPACE \
            --scm github \
            --pr-number $PR_NUMBER
```