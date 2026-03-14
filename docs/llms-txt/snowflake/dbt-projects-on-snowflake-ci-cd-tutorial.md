# Source: https://docs.snowflake.com/en/user-guide/tutorials/dbt-projects-on-snowflake-ci-cd-tutorial.md

dbt

data engineering

tasty bytes

getting started

# Tutorial: Set up CI/CD integrations on dbt Projects on Snowflake

## Introduction

This tutorial guides you through building a secure CI/CD pipeline for dbt Projects on Snowflake using GitHub Actions, OIDC authentication, Snowflake CLI, and
dbt project objects to automate testing, deployment, and orchestration with minimal overhead.

For more information, see [CI/CD integrations on dbt Projects on Snowflake](../data-engineering/dbt-projects-on-snowflake-ci-cd.md).

### Overview

This tutorial walks you through the following steps:

1. Setting up your Snowflake environment:

   * You choose one of three ways to prepare dev and prod targets (full database clone, partial clone, or brand-new databases).
   * Your dbt project must include a `profiles.yml` that refers to these dev and prod targets.
2. Setting up an OIDC service user for secure authentication: Instead of passwords or long-lived tokens, you create a Snowflake service user
   that trusts GitHub through [OpenID Connect](../workload-identity-federation.md). This enables secure, short-lived, per-run
   authentication.
3. Setting up network policies: (Optional) If your Snowflake account restricts inbound IPs, you can use [Snowflake-managed network rules](../network-rules.md)
   to add Github Actions runner IPs to your service user’s network policy. Otherwise, you can skip this step.
4. Storing GitHub secrets and repository variables to configure Snowflake CLI in your workflows:

   * Your Snowflake account identifier
   * (Optionally) the Snowflake username
   * The target database and schema where dbt project objects will be deployed
5. Creating GitHub Actions workflows:

> * CI workflow that triggers on pull requests, deploys a tester dbt project, and runs dbt tests. If anything breaks, the pull request fails.
> * CD workflow that triggers on merges to main, deploys the production dbt project object, and optionally applies scheduling.

At the end of the tutorial, you will have:

* A fully automated, GitHub-driven dbt workflow
* Secure OIDC authentication
* Consistent, tested deployments into Snowflake
* Version-controlled orchestration (optional)
* A repeatable template for scaling dbt workflows across teams

### Prerequisites

* **GitHub**

  * An existing dbt Project in a GitHub account that can create a repository and manage access to that repository.
* **Snowflake**

  * Basic understanding of dbt Projects on Snowflake. For more information, see [dbt Projects on Snowflake](../data-engineering/dbt-projects-on-snowflake.md).
  * A Snowflake account and user with privileges as described in [Access control for dbt projects on Snowflake](../data-engineering/dbt-projects-on-snowflake-access-control.md).
  * Privileges or administrator assistance to create and edit the following:

    * GitHub repository secrets to specify the account and (optional) username
    * A Snowflake service user
    * Network policy

## Set up your environment

Set up where your dbt project will read and write in Snowflake, then update your `profiles.yml` file.

### Create dev and prod databases and schemas

To set up where your dbt project will read and write in Snowflake, choose one of the following options:

1. Clone your production database using zero-copy cloning
2. Create an empty dev database and clone the production schemas you need
3. Create new dev and prod databases and schemas

#### Clone your production database

Use Snowflake’s [zero-copy cloning](../../sql-reference/sql/create-clone.md) to create a full replica of your production database, as shown in
the following example. This gives you a high-fidelity testing environment and is cost-effective because you only pay storage for tables that
change during dbt runs.

```sqlexample
CREATE DATABASE my_dev_db CLONE my_db;
```

#### Create an empty dev database and clone the production schemas you need

Use this method when you only need specific schemas for testing.

```sqlexample
CREATE DATABASE my_dev_db;

-- Repeat the line below for other necessary schemas
CREATE SCHEMA my_dev_db.dev CLONE my_db.my_schema;
```

#### Create new dev and prod databases and schemas

This is the simplest approach when you’re starting from scratch.

```sqlexample
CREATE DATABASE my_dev_db;
CREATE SCHEMA my_dev_db.my_dev_schema;

CREATE DATABASE my_prod_db;
CREATE SCHEMA my_prod_db.my_prod_schema;
```

### Update your profiles.yml file

To manage CI/CD for a dbt project object in GitHub Actions, you must include a `profiles.yml` file inside your dbt project folder (for
example, `my_dbt_project/profiles.yml`). This file defines your dev and prod targets and uses placeholder values that GitHub repository secrets will later replace.

Edit this file *directly on GitHub* to reference the dev and prod databases and schemas you created, as shown below:

```sqlexample
default:
outputs:
target: dev
  dev:
    account: '_' # Put any value here, it will be overwritten by a GitHub repository secret
    database: my_dev_db
    schema: my_dev_schema
    role: <role_name> # Use whichever role has USAGE on the database and schema
    type: snowflake
    warehouse: <warehouse_name> # Replace with your active warehouse name, e.g., my_wh
    user: '_' # Put any value here, it will be overwritten by a GitHub repository secret
  prod:
    account: '_' # Put any value here, it will be overwritten by a GitHub repository secret
    database: my_prod_db
    schema: my_prod_schema
    role: <role_name> # Use whichever role has USAGE on the database and schema
    type: snowflake
    warehouse: <warehouse_name> # Replace with your active warehouse name
    user: '_' # Put any value here, it will be overwritten by a GitHub repository secret
```

Key points from the example:

* `target: dev` sets the default target of the dbt project. This value can be overridden by Snowflake CLI or a dbt project object.
* `dev` and `prod` both use `type: snowflake`.
* Database and schema point to the databases and schemas you created in the previous step.
* Warehouse is an existing Snowflake warehouse name (for example, `my_wh`).
* Account and user are set to dummy values like ‘_’ because they’ll be replaced by GitHub repository secrets later.

## Create a GitHub service user in Snowflake (recommended)

GitHub Actions run using the Snowflake user specified in your Snowflake CLI commands. To keep things clean and secure, create a dedicated
Snowflake user for all GitHub workflows and grant it the required privileges.

### Recommended: OIDC-based service user

This approach uses OpenID Connect (OIDC) rather than long-lived credentials. The service user trusts GitHub as an identity provider, allowing
GitHub Actions to request short-lived tokens for each workflow run. You will map this user to an environment subject like
`environment:prod` in a later step.

Each OIDC service user must have a unique subject. We recommend using a repo path and an environment name, for example
`repo:<org>/<repo>:environment:<environment_name>`. The environment name can be anything, as long as it matches exactly in your GitHub
Action YAML file. For more information, see [Workload identity federation](../workload-identity-federation.md).

Create an OIDC-based service user as follows:

```sqlexample
CREATE USER IF NOT EXISTS github_actions_service_user
  TYPE = SERVICE
  WORKLOAD_IDENTITY = (
    TYPE = OIDC
    ISSUER = 'https://token.actions.githubusercontent.com',
    SUBJECT = 'repo:your_repo_org/your_dbt_repo:environment:prod'
  )
  DEFAULT_ROLE = <role_name>
  COMMENT = 'Service user for GitHub Actions';
```

After you create your user, explicitly grant the default role for the service user to assume that role. The DEFAULT_ROLE parameter only sets the
user’s default role and doesn’t grant it.

```sqlexample
GRANT ROLE <role_name> TO USER github_actions_service_user;
```

Set a default warehouse:

```sqlexample
ALTER USER github_actions_service_user SET DEFAULT_WAREHOUSE = 'mywh';
```

### Alternative: PAT-based authentication (less secure)

If you prefer to use one Snowflake user across multiple repositories, or cannot use OIDC, you can create the user with a personal access
token (PAT) instead.

This method is easier to reuse across repositories but less secure because it relies on long-lived credentials and requires manual rotation.

```sqlexample
CREATE USER IF NOT EXISTS github_actions_service_user
TYPE = SERVICE
COMMENT = 'Service user for GitHub Actions';

-- Grant the level of access to your user that can create network, auth policies,
-- and objects such as DBs and schemas
GRANT ROLE ACCOUNTADMIN TO USER github_actions_service_user;

-- Setting up databases and schemas to store policies and network rules
CREATE DATABASE IF NOT EXISTS github_actions_access_management;
CREATE SCHEMA IF NOT EXISTS github_actions_access_management.NETWORKS;
CREATE SCHEMA IF NOT EXISTS github_actions_access_management.POLICIES;

CREATE AUTHENTICATION POLICY github_actions_access_management.POLICIES.github_auth_policy
authentication_methods = ('PROGRAMMATIC_ACCESS_TOKEN')
pat_policy = (
default_expiry_in_days = 15, -- default value
max_expiry_in_days = 365, -- default value
network_policy_evaluation = ENFORCED_NOT_REQUIRED -- this is needed to ensure you can generate a PAT on Snowsight
);

ALTER USER github_actions_service_user SET AUTHENTICATION POLICY github_actions_access_management.POLICIES.github_auth_policy;
```

## (Optional) Set up a network policy for GitHub Actions

Now that you’ve created the service user that Snowflake CLI will use, let’s configure this user to connect to your Snowflake account from within GitHub Actions.

> **Note:**
>
> Creating or modifying network policies requires ACCOUNTADMIN or an equivalent role.

### Determine whether you need a network policy

* If your account restricts inbound access, you must create or update a network policy to add GitHub Actions runner IPs to your allowlist. Snowflake
  simplifies this with Snowflake-managed network rules. For more information, see [Network rules](../network-rules.md).
* If your account does *not* restrict inbound access, no network policy changes are required.

If you’re unsure, skip this step for now and return only if you see an error like: `Incoming request with IP/Token <IP> is not allowed to access Snowflake.`

To create and apply a network policy to a user, choose one of the following options:

* Create a new network policy and assign it to the service user, or
* Add the GitHub Actions network rule to an existing network policy that the user already uses.

> **Note:**
>
> Before doing this, consult your Snowflake account admin. They must ensure the policy includes not only the GitHub Actions network rule but
> also any other IP ranges your organization requires.
>
> Once a network policy is applied, Snowflake restricts user access based on its allowed and blocked IP ranges. Your account admin might need
> to adjust the policy or apply it account wide to avoid unintentionally blocking essential access.

#### Option 1: Create a new network policy and apply it to the user

A Snowflake user can have only one network policy at a time. If the user doesn’t have one or you want to replace the existing policy, complete
the following steps:

```sqlexample
CREATE NETWORK POLICY github_actions_policy
  ALLOWED_NETWORK_RULE_LIST = ('SNOWFLAKE.NETWORK_SECURITY.GITHUBACTIONS_GLOBAL', <other required rules>)
  BLOCKED_NETWORK_RULE_LIST = ();

ALTER USER GitHub_Actions_Service_User
  SET NETWORK_POLICY = github_actions_policy;
```

#### Option 2: Add a network rule to an existing network policy

If the user already has a network policy, you can add the GitHub Actions rule to it.

```sqlexample
-- Check the user’s current network policy:
SHOW PARAMETERS LIKE 'NETWORK_POLICY' FOR USER <user_name>;
```

> **Note:**
>
> If the network policy is applied at the account level or shared by many users, updating it will affect everyone.

```sqlexample
-- Add the new rule:
ALTER NETWORK POLICY <name>

ADD ALLOWED_NETWORK_RULE_LIST = ('SNOWFLAKE.NETWORK_SECURITY.GITHUBACTIONS_GLOBAL');
```

The user inherits the update automatically since they’re already assigned to this policy.

## Configure GitHub repository secrets and variables

GitHub Actions use the Snowflake CLI to connect to your Snowflake account, so you must configure GitHub repository secrets and variables
first. This is how the CI/CD integration passes Snowflake account info into Snowflake CLI inside GitHub Action workflows.

### Configure GitHub repository secrets

Add secrets to securely store the information Snowflake CLI needs to identify your Snowflake account and, if required, the user it should
authenticate as:

1. In your GitHub repository, go to Settings.
2. From the left-hand side navigation, select Secrets and variables » Actions.
3. Under Secrets, select New repository secret.
4. Add a secret to connect your Snowflake account:

   * Name: `SNOWFLAKE_ACCOUNT`
   * Value: Your Snowflake account identifier (for example, `org_name-account_name`). This value tells Snowflake CLI which
     account you want to connect to.
5. Select Add secret.
6. (Optional) If you aren’t using OIDC, select New repository secret to specify the Snowflake username the CLI should use when connecting. It specifies which
   user credentials to run commands under.

   * Name: `SNOWFLAKE_USER`
   * Value: Optional if you’re using OIDC or credential-less authentication.

     * With OIDC, Snowflake CLI automatically matches the GitHub Action’s subject to the OIDC service user (created in Step 3), so this is
       not required.
     * Without OIDC, you must specify a user (and supply password or key credentials). As a recommended best practice, you should create
       a personal access token in Snowsight. For more information, see [Generating a programmatic access token](../programmatic-access-tokens.md).
7. Select Add secret.
8. (Optional) If you aren’t using OIDC, select New repository secret to specify the service user’s personal access token that the CLI should use when connecting.

   * Name: `SNOWFLAKE_PAT`
   * Value: Optional if you’re using OIDC or credential-less authentication.
   * Name: `SNOWFLAKE_PAT`
   * Value: Optional if you’re using OIDC or credential-less authentication.

### Configure GitHub repository variables

These help Snowflake CLI connect to the right database and schema. Complete the following steps:

1. In your GitHub repository, go to Settings.
2. From the left-hand side navigation, select Secrets and variables » Actions.
3. Under Variables, select New repository variable.
4. Add a database variable:

   * Name: `SNOWFLAKE_DATABASE`
   * Value: Enter an existing database where the dbt project object will be created.
5. Select Add variable.
6. Add a schema variable:

   * Name: `SNOWFLAKE_SCHEMA`
   * Value: Enter an existing schema where the dbt project object will be created.
7. Select Add variable.

## Create your Continuous Integration (CI) GitHub Action

This step is where automation starts. This CI workflow runs whenever a pull request targets main. It:

1. Creates a tester dbt project object in Snowflake
2. Runs `dbt run` and `dbt test` against your dev target
3. Fails the pull request if the dbt execution fails

### Create your CI workflow file

1. In your GitHub repository, go to Actions.
2. From the left-hand side navigation, select New workflow.
3. Select set up a workflow yourself to create an empty workflow.
4. Name the file `incoming_pr.yml`.
5. Copy and paste the following into the file:

   ```yaml
   name: Incoming PR
   run-name: PR opened by ${{ github.actor }}
   on:
     pull_request:
       types: [opened, synchronize, reopened, ready_for_review]
       branches: [main]

   permissions:
     contents: read
     id-token: write

   jobs:
     run-snowflake-test-dbt-job:
       name: "Run on Incoming PR"
       runs-on: ubuntu-latest
       environment: prod # Must match the OIDC subject's environment
       env:
         SNOWFLAKE_CLI_FEATURES_ENABLE_DBT: true
         SNOWFLAKE_ACCOUNT: ${{ secrets.SNOWFLAKE_ACCOUNT }}
         # SNOWFLAKE_PASSWORD: ${{ secrets.SNOWFLAKE_PAT }} # Snowflake password is required if you aren't using OIDC
         SNOWFLAKE_DATABASE: ${{ vars.SNOWFLAKE_DATABASE }}
         SNOWFLAKE_SCHEMA: ${{ vars.SNOWFLAKE_SCHEMA }}

       steps:
         # Check out repository code
         # Gets the latest code from the incoming pull request
         - name: Check out repository code
           uses: actions/checkout@v4

         - name: Install Snowflake CLI
           uses: snowflakedb/snowflake-cli-action@v2.0
           with: # Ensures Snowflake CLI will search for OIDC users matching this subject
             use-oidc: true

         - name: Check Snowflake CLI Version
           run: snow --version

         # The -x is shorthand for --temporary-connection
         - run: snow connection test -x

         # The --force setting creates the object or updates it if it already exists
         # You can remove the "--source" flag if your dbt_project.yml is at root of your repo
         - name: Create a new tester dbt project object in ${{ vars.SNOWFLAKE_DATABASE }}.${{ vars.SNOWFLAKE_SCHEMA }}
           run: snow dbt deploy my_tester_dbt_project_object_gh_action --source ./tasty_bytes --dbt-version 1.10.15 --force -x

         - name: List all of the snowflake dbt project objects in your account
           run: snow dbt list -x

         - name: Execute run on tester dbt project object in ${{ vars.SNOWFLAKE_DATABASE }}.${{ vars.SNOWFLAKE_SCHEMA }}
           run: snow dbt execute -x my_tester_dbt_project_object_gh_action run --target dev

         - name: Execute data quality test on tester dbt project object in ${{ vars.SNOWFLAKE_DATABASE }}.${{ vars.SNOWFLAKE_SCHEMA }}
           run: snow dbt execute -x my_tester_dbt_project_object_gh_action test --target dev
   ```

6. Select Commit changes.
7. Select Create a new branch for this commit and start a pull request.
8. Select Propose changes.
9. After you finish submitting the pull request, you should see your `incoming_pr.yml` action start to run.
10. After it’s merged, the file will be saved to `.github/workflows/incoming_pr.yml`.

#### Key pieces from the workflow file

* Triggers on pull requests to `main`:

  ```yaml
  on:
    pull_request:
      types: [opened, synchronize, reopened, ready_for_review]
      branches: [main]
  ```

* Grants permissions and sets environment variables for Snowflake CLI:

  ```yaml
  permissions:
    contents: read
    id-token: write

  jobs:
    run-snowflake-test-dbt-job:
      runs-on: ubuntu-latest
      environment: prod # Must match the OIDC subject's environment
      env:
        SNOWFLAKE_CLI_FEATURES_ENABLE_DBT: true
        SNOWFLAKE_ACCOUNT: ${{ secrets.SNOWFLAKE_ACCOUNT }}
        # SNOWFLAKE_PASSWORD: ${{ secrets.SNOWFLAKE_PAT }} # Snowflake password is required if you aren't using OIDC
        SNOWFLAKE_DATABASE: ${{ vars.SNOWFLAKE_DATABASE }}
        SNOWFLAKE_SCHEMA: ${{ vars.SNOWFLAKE_SCHEMA }}
  ```

* Steps in the job:

  1. Check out repository code (`actions/checkout@v4`).
  2. Install Snowflake CLI using `snowflakedb/snowflake-cli-action@v2.0` with `use-oidc: true`.
  3. Run `snow --version`.
  4. Run `snow connection test -x` to verify OIDC connection.
  5. Deploy a tester dbt project object using `snow dbt deploy ... --force -x` (with `--source` if the dbt project is in a subfolder).
  6. Run `snow dbt list -x` to show dbt project objects.
  7. Execute:

     `snow dbt execute -x my_tester_dbt_project_object_gh_action run --target dev`
     `snow dbt execute -x my_tester_dbt_project_object_gh_action test --target dev`
* Once you commit this new workflow on a branch and open a pull request, GitHub Actions will run it. If the dbt project object fails to run or
  test, the CI check fails and the pull request can’t be merged.

## Create your Continuous Deployment (CD) GitHub Action

The CD workflow runs after code is merged to main (or any direct push to main), ensuring the dbt project object in Snowflake reflects the
latest code.

### Create your CD workflow file

1. In your GitHub repository, go to Actions.
2. From the left-hand side navigation, select New workflow.
3. Select set up a workflow yourself to create an empty workflow.
4. Name the file `pr_merged.yml`.
5. Copy and paste the following into the file:

   ```yaml
   name: PR Accepted Deployment
   run-name: PR from ${{ github.actor }} accepted - triggered a ${{ github.event_name }}
   on:
     push:
       branches: [ main ]

   permissions:
     contents: read
     id-token: write

   jobs:
     run-snowflake-dbt-job:
       name: "Run on Accepted PR"
       runs-on: ubuntu-latest
       environment: prod # Must match the OIDC subject's environment
       env:
         SNOWFLAKE_CLI_FEATURES_ENABLE_DBT: true
         SNOWFLAKE_ACCOUNT: ${{ secrets.SNOWFLAKE_ACCOUNT }}
         # SNOWFLAKE_PASSWORD: ${{ secrets.SNOWFLAKE_PAT }} # Snowflake password is required if you aren't using OIDC
         SNOWFLAKE_DATABASE: ${{ vars.SNOWFLAKE_DATABASE }}
         SNOWFLAKE_SCHEMA: ${{ vars.SNOWFLAKE_SCHEMA }}

       steps:
         # Check out repository code
         # Gets the latest code from the pull request branch
         - name: Check out repository code
           uses: actions/checkout@v4

         - name: Install Snowflake CLI
           uses: snowflakedb/snowflake-cli-action@v2.0
           with: # Ensures Snowflake CLI will search for OIDC users matching this subject
             use-oidc: true

         - name: Check Snowflake CLI Version
           run: snow --version

         # The -x is shorthand for --temporary-connection
         - run: snow connection test -x

         # The --force setting creates the object or updates it if it already exists
         # You can remove the "--source" flag if your dbt_project.yml is at root of your repo
         # The --default-target flag ensures the dbt project object compiles and executes with your prod target
         - name: Create a new dbt project object in ${{ vars.SNOWFLAKE_DATABASE }}.${{ vars.SNOWFLAKE_SCHEMA }}
           run: snow dbt deploy tasty_bytes_dbt_object_gh_action --source ./tasty_bytes --default-target prod --dbt-version 1.10.15 --force -x

         - name: List all of the snowflake dbt project objects on your account
           run: snow dbt list -x

         # (optional) Uncomment the lines below and follow Step 7 if you want to manage Task orchestration via source control
         # - name: Run schedules.sql to create or alter tasks for tasty_bytes_dbt_object_gh_action
         #   run: snow sql -f ${{ github.workspace }}/tasty_bytes/schedules.sql -x
   ```

6. Select Commit changes to save the file to `.github/workflows/pr_merged.yml`.
7. Navigate to the Actions tab of your repository to see your `pr_merged.yml` action start to run.

#### Key pieces from the workflow file

* Triggers on pushes to `main`:

  ```yaml
  on:
   push:
     branches: [ main ]
  ```

* Similar permissions/env as CI:

  ```yaml
  permissions:
  contents: read
  id-token: write

  jobs:
    run-snowflake-dbt-job:
      runs-on: ubuntu-latest
      environment: prod # Must match the OIDC subject's environment
      env:
        SNOWFLAKE_CLI_FEATURES_ENABLE_DBT: true
        SNOWFLAKE_ACCOUNT: ${{ secrets.SNOWFLAKE_ACCOUNT }}
        # SNOWFLAKE_PASSWORD: ${{ secrets.SNOWFLAKE_PAT }} # Snowflake password is required if you aren't using OIDC
        SNOWFLAKE_DATABASE: ${{ vars.SNOWFLAKE_DATABASE }}
        SNOWFLAKE_SCHEMA: ${{ vars.SNOWFLAKE_SCHEMA }}
  ```

* Steps in the job:

  1. Check out the repository code.
  2. Install Snowflake CLI with OIDC.
  3. Run `snow --version`.
  4. Run `snow connection test -x` to verify OIDC connection.
  5. Deploy/update the production dbt project object with `snow dbt deploy ... --default-target prod --force -x`.
  6. Run `snow dbt list -x` to show dbt project objects.
  7. (Optional) Run a `schedules.sql` file to manage tasks (see next section).
* Once this workflow is in place, every successful merge to main (or push) updates the dbt project object in Snowflake.

## (Optional) Add orchestration with Snowflake tasks

Orchestrate runs of your dbt project object using a `schedules.sql` file and Snowflake tasks (triggered from the CD workflow):

1. In your GitHub repository, navigate to your dbt project (for example, `tasty_bytes/`).
2. Create a file named `schedules.sql` and copy and paste the following into the file.

   This file:

   * Suspends any existing tasks
   * Creates or alters tasks to:

     * Run a subset of the DAG on a schedule
     * Run the full project
     * Run tests
   * Resumes tasks in the correct order (child → root)

   ```sqlexample
   -- To avoid issues with CREATE OR ALTER, suspend all of the tasks from root to child
   -- ALTER TASK IF EXISTS ensures this file can execute on first run each time a task is added
   ALTER TASK IF EXISTS run_tasty_bytes_subset SUSPEND;
   ALTER TASK IF EXISTS run_tasty_bytes_full SUSPEND;
   ALTER TASK IF EXISTS test_tasty_bytes SUSPEND;

   -- This would be an example scenario where you have a subset of the DAG that needs to be available early for business needs:
   CREATE OR ALTER TASK run_tasty_bytes_subset
     WAREHOUSE = <warehouse_name>
     SCHEDULE = '12 hours'
     AS
         execute dbt project my_dbt_project_object_gh_action args='run --select raw_customers stg_customers customers --target prod';

   -- Kick off a complete run of the full project
   CREATE OR ALTER TASK run_tasty_bytes_full
     WAREHOUSE = <warehouse name>
     AFTER run_tasty_bytes_subset
     AS
         execute dbt project my_dbt_project_object_gh_action args='run --target prod';

   -- Run any data quality tests you've defined
   CREATE OR ALTER TASK test_tasty_bytes
     WAREHOUSE = <warehouse name>
     AFTER run_tasty_bytes_full
     AS
         execute dbt project my_dbt_project_object_gh_action args='test --target prod';

   -- When a task is first created or if an existing task it paused, it MUST BE RESUMED to be activated
   -- The tasks must be enabled in REVERSE ORDER from child to root
   ALTER TASK IF EXISTS test_tasty_bytes RESUME;
   ALTER TASK IF EXISTS run_tasty_bytes_full RESUME;
   ALTER TASK IF EXISTS run_tasty_bytes_subset RESUME;
   ```

3. Select Commit changes.
4. In your GitHub repository, navigate to `.github/workflows/pr_merged.yml` and uncomment the `Run schedules.sql to create...`
   step at the end of the file.
5. Select Commit changes.

## Next steps

Next steps to improve Your workflow:

* Use [zero-copy cloning](../../sql-reference/sql/create-clone.md) in CI:

  Test against fresh production data by adding a step in `incoming_pr.yml` before deploying your tester dbt object:

  ```snowcli
  snow sql -q "CREATE DATABASE <your_user_name>_dev_dbt_DB CLONE YOUR_PRODUCTION_DATABASE".
  ```

* Add alerting:

  Configure Slack or email notifications in GitHub Actions, or use Snowflake task error notifications.

  For more information, see [Configure a task to send error notifications](../tasks-errors-integrate.md).
* Explore [Managing dbt Projects on Snowflake using Snowflake CLI](../../developer-guide/snowflake-cli/data-pipelines/dbt-projects.md).
