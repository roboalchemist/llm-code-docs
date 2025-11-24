# Source: https://docs.baseten.co/training/management.md

# Management

> How to monitor, manage, and interact with your Baseten Training projects and jobs.

Once you have submitted training jobs, Baseten provides tools to manage your `TrainingProject`s and individual `TrainingJob`s. You can use the [CLI](/reference/cli/training/training-cli) or the [API](/reference/training-api/overview) to manage your jobs.

## `TrainingProject` management

* **Listing Projects:** To view all your training projects:
  ```bash  theme={"system"}
  truss train view
  ```
  This command will list all `TrainingProject`s you have access to, typically showing their names and IDs. Additionally, this command will show all active jobs.

* **Viewing Jobs within a Project:** To see all jobs associated with a specific project, use its `project` (obtained when creating the project or from `truss train view`):
  ```bash  theme={"system"}
  truss train view --project <project_id or project_name>
  ```

## `TrainingJob` management

After submitting a job with `truss train push config.py`, you receive a `project_id` and `job_id`.

* **Listing Jobs:** As shown above, you can list all jobs within a project using:
  ```bash  theme={"system"}
  truss train view --project <project_id or project_name>
  ```
  This will typically show job IDs, statuses, creation times, etc.

* **Checking Status and Retrieving Logs:** To view the logs for a specific job, you can tail them in real-time or fetch existing logs.
  * To view logs for the most recently submitted job in the current context (e.g., if you just pushed a job from your current terminal directory):
    ```bash  theme={"system"}
    truss train logs --tail
    ```
  * To view logs for a specific job using its `job-id`:
    ```bash  theme={"system"}
    truss train logs --job-id <your_job_id> [--tail]
    ```
    Add `--tail` to follow the logs live.

* **Understanding Job Statuses:**
  The `truss train view` and `truss train logs` commands will help you track which status a job is in. For more on the job lifecycle, see the [Lifecycle](/training/lifecycle) page.

* **Stopping a `TrainingJob`:** If you need to stop a running job, use the `stop` command with the job's project ID and job ID:
  ```bash  theme={"system"}
  truss train stop --job-id <your_job_id>
  truss train stop --all # Stops all active jobs; Will prompt the user for confirmation.
  ```
  This will transition the job to the `TRAINING_JOB_STOPPED` state.

* **Understanding Job Outputs & Checkpoints:**
  * The primary outputs of a successful `TrainingJob` are model **checkpoints** (if checkpointing is enabled and configured).
  * These checkpoints are stored by Baseten. Refer to the [Checkpointing section in Core Concepts](/training/concepts#checkpointing) for how `CheckpointingConfig` works.
  * When you are ready to [deploy a model](/training/deployment), you will specify which checkpoints to use. The `model_name` you assign during deployment (via `DeployCheckpointsConfig`) becomes the identifier for this trained model version derived from your specific job's checkpoints.
  * You can see the available checkpoints for a job via the [Training API](/reference/training-api/get-training-job-checkpoints).
