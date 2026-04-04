# Source: https://docs.kaisar.io/kaisar-network/kaisar-ai-ops/deep-learning-platform/jobs.md

# Jobs

Submit and manage training jobs on cluster resources.

![Jobs Overview](https://3962875474-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F01Fyr0ujWr1ipjmUOTbr%2Fuploads%2Fgit-blob-48a776e177d6b5895b6dd63408a4290fcacfc60d%2Fjobs_list_view.png?alt=media)

## Overview

The Jobs section allows you to submit, monitor, and manage ML training jobs that run on cluster nodes. Track job status, progress, and resource utilization in real-time.

## Jobs Dashboard

The dashboard displays key job metrics at a glance:

**Summary Cards**:

* **Total Jobs**: Total number of jobs in the system
* **Running**: Number of jobs currently running
* **Completed**: Number of jobs completed successfully
* **Failed**: Number of jobs that failed

## Job List View

The jobs table shows all submitted jobs with the following information:

**Columns**:

* **Job Name**: Job name and type (Training, Inference, etc.)
* **Status**: Current status with color-coded badges
* **Priority**: Job priority (High, Medium, Low)
* **Experiment**: Associated experiment name
* **Progress**: Progress bar with percentage
* **Created**: Job creation date
* **Actions**: Quick actions menu

**Filtering and Search**:

* Search by job name
* Filter by status, priority, or experiment

## Creating a Job

Navigate to **Deep Learning Platform** → **Jobs** → Click **Create**

![Create Job](https://3962875474-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F01Fyr0ujWr1ipjmUOTbr%2Fuploads%2Fgit-blob-0aafb742bf687d90f07e871d4394faaea90b7810%2Fjob_create_form.png?alt=media)

### Basic Information

**Job Name**\* (Required)

* Enter a descriptive name for the job
* Example: `BERT Fine-tuning - Sentiment Analysis`
* Helper text: "Enter a descriptive name for the job"

**Description**

* Detailed description of the job
* Example: "Fine-tuning BERT-base model for sentiment analysis on IMDB movie reviews"

**Job Type**\* (Required)

* Select from dropdown: Training, Inference, Hyperparameter Tuning, etc.
* Default: `Training`
* Helper text: "training"

**Priority**\* (Required)

* Select priority level: High, Medium, Low
* Default: `High`
* Helper text: "high"

### Configuration

**Epochs**

* Number of training epochs
* Example: `3`
* Helper text: "Number of training epochs"

**Batch Size**

* Training batch size
* Example: `16`
* Helper text: "Training batch size"

**Learning Rate**

* Initial learning rate
* Example: `0.00002`
* Helper text: "Initial learning rate"

**Optimizer**

* Select optimizer from dropdown
* Options: AdamW, Adam, SGD, etc.
* Default: `AdamW`
* Helper text: "adamw"

### Resources

**CPU Cores**

* Number of CPU cores required
* Example: `4`

**Memory (GB)**

* Memory allocation in GB
* Example: `16`

**GPU Count**

* Number of GPUs required
* Example: `0` (for CPU-only jobs)

### Actions

* **Cancel**: Discard and close
* **Create Job**: Submit the job to the queue

## Viewing Job Details

To view detailed information about a job:

1. Navigate to **Deep Learning Platform** → **Jobs**
2. Click on a job from the list
3. View comprehensive details in the modal dialog

![View Job Details](https://3962875474-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F01Fyr0ujWr1ipjmUOTbr%2Fuploads%2Fgit-blob-da266bc2025ac5c0dbe66542a2683138c1fb7691%2Fjob_details_view.png?alt=media)

**Details Panel Sections**:

**Basic Information**:

* **Job Name**: e.g., "BERT Fine-tuning - Sentiment Analysis"
* **Description**: Full description of the job
* **Job Type**: Training, Inference, etc.
* **Priority**: High, Medium, Low

**Configuration**:

* **Epochs**: Number of training epochs (e.g., 3)
* **Batch Size**: Training batch size (e.g., 16)
* **Learning Rate**: Initial learning rate (e.g., 0.00002)
* **Optimizer**: Optimizer used (e.g., AdamW)

**Resources**:

* **CPU Cores**: Allocated CPU cores (e.g., 4)
* **Memory (GB)**: Allocated memory (e.g., 16)
* **GPU Count**: Number of GPUs (e.g., 0)

## Editing a Job

To update job configuration:

1. Open job details page
2. Click **Edit** button (or three-dot menu → Edit)
3. Modify editable fields in the Edit Job modal

![Edit Job Form](https://3962875474-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F01Fyr0ujWr1ipjmUOTbr%2Fuploads%2Fgit-blob-ff7c5ba93d83d520e56fb6d7ab1598efd1d785ee%2Fjob_edit_form.png?alt=media)

4. Click **Update Job** to save changes

> \[!NOTE] You can only edit jobs that are in Pending or Failed status. Running or Completed jobs cannot be edited.

**Editable Fields**:

* ✅ Job Name
* ✅ Description
* ✅ Priority (can change to expedite or delay)
* ✅ Configuration (epochs, batch size, learning rate, optimizer)
* ✅ Resources (CPU, memory, GPU)
* ❌ Job Type (cannot edit)
* ❌ Status (managed by system)

## Job Status

**Status Types**:

**Pending** (Orange):

* Job is queued, waiting for resources
* Will start when cluster resources become available

**Running** (Blue):

* Job is actively executing
* Resources are allocated
* Progress is being tracked

**Completed** (Green):

* Job finished successfully
* Results are available
* Resources have been released

**Failed** (Red):

* Job encountered an error
* Check logs for error details
* Can be restarted or debugged

## Managing Jobs

### Stopping a Running Job

To stop a job that's currently running:

1. Open job details or click actions menu
2. Click **Stop** button
3. Confirm action
4. Job will be terminated and resources released

> \[!WARNING] Stopping a job will lose all progress. Consider checkpointing your training jobs.

### Restarting a Failed Job

To restart a job that failed:

1. Open failed job details
2. Click **Restart** button
3. Job will be resubmitted to the queue
4. Monitor for success

### Deleting a Job

To remove a job:

1. Navigate to job details or list
2. Click **Delete** button
3. Confirm deletion

> \[!WARNING] Deleting a job will permanently remove:
>
> * Job configuration
> * Training logs
> * Checkpoints and outputs
> * This action cannot be undone!

**Before Deleting**:

* Download important logs
* Save model checkpoints
* Export results if needed

## Job Monitoring

### Real-time Progress

Monitor job progress in real-time:

* Progress bar shows completion percentage
* View live logs in job details
* Track resource utilization
* Monitor metrics and loss curves

### Job Logs

Access job logs:

1. Open job details
2. Navigate to **Logs** tab
3. View stdout/stderr output
4. Filter by log level
5. Download logs for offline analysis

### Resource Usage

Monitor resource consumption:

* CPU utilization
* Memory usage
* GPU utilization (if applicable)
* Network I/O
* Disk I/O

## Job Scheduling

**Priority-based Scheduling**:

* **High** priority jobs run first
* **Medium** priority jobs run when high-priority queue is empty
* **Low** priority jobs run when resources are available

**Resource Allocation**:

* Jobs are matched to suitable cluster nodes
* GPU jobs require GPU-enabled nodes
* CPU/Memory requirements must be met

**Queue Management**:

* View pending jobs in queue
* Estimate wait time based on current load
* Adjust priority if needed

## Best Practices

**Job Naming**:

* Use descriptive names: `bert-sentiment-imdb-v1`
* Include model, task, and version
* Keep names concise but informative

**Resource Requests**:

* Request only what you need
* Don't over-allocate resources
* Monitor actual usage and adjust

**Checkpointing**:

* Save checkpoints regularly
* Enable auto-save in training code
* Store checkpoints in persistent storage

**Error Handling**:

* Implement retry logic
* Log errors comprehensively
* Set up failure notifications

**Priority Usage**:

* Use High priority sparingly
* Reserve for urgent production jobs
* Most jobs should be Medium priority

## Next Steps

* Run jobs on [Cluster](https://docs.kaisar.io/kaisar-network/kaisar-ai-ops/deep-learning-platform/cluster) nodes
* Link jobs to [Experiments](https://docs.kaisar.io/kaisar-network/kaisar-ai-ops/deep-learning-platform/experiments)
* Monitor performance in [Analytics](https://docs.kaisar.io/kaisar-network/kaisar-ai-ops/deep-learning-platform/analytics)
* Deploy successful models via [Deployments](https://docs.kaisar.io/kaisar-network/kaisar-ai-ops/deep-learning-platform/deployments)
