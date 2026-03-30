# Source: https://docs.socket.dev/docs/socket-in-your-gitlab-pipeline.md

# Socket for Gitlab Pipeline

Socket fights vulnerabilities and provides visibility, defense-in-depth, and proactive supply chain protection for your open source dependencies. It is easy to integrate Socket into your Gitlab Pipeline to provide an extra layer of security against Supply Chain Attacks.

## Adding Socket to your pipeline

### Create your Socket Environment variables

1. Create a Socket API Key ([Directions](https://docs.socket.dev/docs/create-socket-api-key-for-cicd))

2. Log into Gitlab

3. Navigate to your project

4. Go to **Settings** -> **CI/CD**

5. Expand **Variables**

   <Image align="left" border={false} src="https://files.readme.io/d7d3efe-Screenshot_2023-12-11_at_3.07.45_PM.png" />

6. Do **Add Variable**

   1. Tick the "**Masked and hidden**" radio button for "**Visibility**" option
   2. Check the "**Expand variable reference**" box for the "**Flags**" option so that the variable can be expanded in the pipeline job execution. Note: "$" literals in variable values need to be escaped in GitLab.
   3. For the "**Key:**" field, enter the name "**SOCKET\_SECURITY\_API\_KEY**"
   4. For the "**Value:**" field, enter your \<**Socket API Token**>

7. Next, to add another variable called "**GITLAB\_TOKEN**" for your Gitlab Token that has access to the Project
   1. First, let’s go generate the gitlab project access token value
   2. Go to **Setting** -> **Access tokens**
   3. Click on “**Add new token**” button
      1. Give a “**Token name**”
      2. Optional, given a token description
      3. For the role select the scoping as required per permission needs:
         1. Personal Access Token
            * Role **Reporter** with scope **api**
         2. Group Access Tokens
            * Role **Reporter** with scope **api**
            * The Token needs to be granted access to the project or group
      4. Then click on “Create project access token” button
      5. You will need to make a copy of the generated ***project access token*** for the next step.
   4. Go back to the **CI/CD** -> **Variables** (Expand it) -> Click on “**Add variable**”
      1. Tick the “**Masked**” radio button for “**Visibility**” option
      2. Check the "**Expand variable reference**" box for the "**Flags**" option

         Protect variable:

         * ✅ Enable if your jobs run only on protected branches/tags (recommended for secrets). Note that "**Allow merge request pipelines to access protected variables and runners**" should be enabled.
         * ❌ Disable (uncheck) if your jobs must run on unprotected branches and need this token (Important!)
           Environment scope: All (or narrow if needed)

         Why this matters

         * Protected = safer: Protected variables are only available in pipelines on protected branches/tags.

         * Unprotected usage: If a job needs the token on unprotected branches, you must uncheck Protect variable, or provide a separate, least-privilege token as an unprotected variable.

         > Tip: Prefer keeping sensitive tokens protected. Use $CI\_JOB\_TOKEN or a restricted-scope token for unprotected branches; reserve powerful tokens for protected branches only.
      3. For the "**Key:**" field, enter the name "**GITLAB\_TOKEN**"
      4. For the "**Value:**" field,  paste the generated \<***project\_access\_token***> here

8. Sample screenshot

   <Image align="center" border={false} src="https://files.readme.io/5841c81e5a5720421f25e804fc1149da0d6c2be42fb4ed398543dce95b413775-Gitlab_APIKEY_and_AccessToken.png" />

### Example Gitlab Pipeline Setup

1. Go to **Build**
2. Go to **Pipeline Editor**
3. Paste the following Pipeline Yaml, or integrate with your existing code

   ```yaml yaml
   # Socket Security GitLab CI Pipeline
   # This pipeline runs Socket Security scans on every commit to any branch
   # The CLI automatically detects most information from the git repository

   stages:
     - security-scan

   socket-security:
     stage: security-scan
     image:
       name: socketdev/cli:latest
       entrypoint: [""]
       # Override the entrypoint to run commands directly
     
     # Run on all branches and merge requests
     rules:
       - if: $CI_PIPELINE_SOURCE == "push"
         # Uncomment rule below to only run Socket CLI on changes to manifest files.
         # Note: You may miss new alerts for existing packages
         # changes:
         #   - <manifest file>
       - if: $CI_PIPELINE_SOURCE == "merge_request_event"
         # Uncomment rule below to only run Socket CLI on changes to manifest files.
         # Note: You may miss new alerts for existing packages
         # changes:
         #   - <manifest file>
     
     # Required for GitLab integration to work properly
     variables:
       SOCKET_SECURITY_API_KEY: $SOCKET_SECURITY_API_KEY
       GITLAB_TOKEN: $GITLAB_TOKEN
       # This is an option to help speed up the processing
       PIP_CACHE_DIR: "$CI_PROJECT_DIR/.cache/pip"
       
     # This variable is optional, configuration for the runner
     cache:
       paths:
         - .cache/pip/
     
     script:
       # Run Socket CLI with minimal required parameters
       # The CLI automatically detects:
       # - Repository name from git
       # - Branch name from git 
       # - Commit SHA from git (or CI_COMMIT_SHA)
       # - Commit message from git
       # - Committer information from git
       # - Default branch status from GitLab CI environment variables
       # - Changed files from git commit
       # - Merge request number from CI_MERGE_REQUEST_IID
       - |
         socketcli \
           --target-path $CI_PROJECT_DIR \
           --scm gitlab \
           --pr-number ${CI_MERGE_REQUEST_IID:-0}
    

   ```
4. Commit changes to your main branch or the current branch you are working on

### Testing pipeline

1. Create a new branch
2. Modify or add a `package.json`
3. Create a new Merge request
4. Confirm that the Socket CI pipeline job ran

   <Image border={false} src="https://files.readme.io/48c7aa8-image.png" />
5. Confirm that for an unhealthy report a comment is left on the Merge request

   <Image border={false} src="https://files.readme.io/5b6e660-image.png" />