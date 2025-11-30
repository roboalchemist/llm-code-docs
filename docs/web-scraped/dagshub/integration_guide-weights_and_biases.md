# Source: https://dagshub.com/docs/integration_guide/weights_and_biases/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTggMTJoOHYySDh6bTIgOEg2VjRoN3Y1aDV2My4xbDItMlY4bC02LTZINmEyIDIgMCAwIDAtMiAydjE2YTIgMiAwIDAgMCAyIDJoNHptLTItMmg0LjFsLjktLjlWMTZIOHptMTIuMi01Yy4xIDAgLjMuMS40LjJsMS4zIDEuM2MuMi4yLjIuNiAwIC44bC0xIDEtMi4xLTIuMSAxLTFjLjEtLjEuMi0uMi40LS4ybTAgMy45TDE0LjEgMjNIMTJ2LTIuMWw2LjEtNi4xeiIgLz48L3N2Zz4=)](https://dagshub.com/DagsHub-Official/dagshub-docs/src/main/docs/integration_guide/weights_and_biases.md "Edit this page")

# Weights & Biases to DagsHub Migration[¶](#weights-biases-to-dagshub-migration "Permanent link")

Migrating your machine learning (ML) experiments from Weights & Biases (W&B) to DagsHub facilitates enhanced collaboration, version control, and comprehensive experiment tracking. This page explains how to transfer run data, metrics, parameters, and artifacts seamlessly from W&B to DagsHub.

This migration leverages MLflow for consistent logging and tracking, ensuring your experiments are well-documented and easily accessible.

## How Does the Migration Work?[¶](#how-does-the-migration-work "Permanent link")

The migration tool automatically extracts experiment data from W&B, including metrics, parameters, and artifacts. It then logs this information to DagsHub using MLflow, which is integrated into DagsHub\'s platform. This process not only preserves the integrity of your experiment data but also enhances its accessibility and usability within DagsHub\'s collaborative environment.

## How to Migrate Your Experiments?[¶](#how-to-migrate-your-experiments "Permanent link")

Migrate your W&B experiments to DagsHub in a few simple steps:

### 1. Clone the Migration Project[¶](#1-clone-the-migration-project "Permanent link") 

First, clone the migration tool repository from DagsHub:

    git clone https://dagshub.com/DagsHub/import_from_wb.git
    cd import_from_wb

### 2. Install Necessary Packages[¶](#2-install-necessary-packages "Permanent link") 

Ensure you have Python 3.8 or later and install all required packages:

    pip install -r requirements.txt

### 3. Set Up Environment Variables[¶](#3-set-up-environment-variables "Permanent link") 

Configure your environment with the necessary credentials for W&B and DagsHub to ensure secure and smooth migration.

### 4. Run the Migration Script[¶](#4-run-the-migration-script "Permanent link") 

Execute the migration script with the required parameters:

    python import_from_wb.py <wb_owner> <wb_project> <dh_owner> <dh_repo> --run_id <optional_run_id>

Replace the placeholders with your specific W&B and DagsHub project details. Optionally, specify a single run ID to migrate a specific experiment.

------------------------------------------------------------------------

**Congratulations!** You\'ve successfully migrated your experiments from W&B to DagsHub. Now, your ML experiments can benefit from DagsHub\'s collaborative features, such as pull requests for data and models, issue tracking for experiments, and more.

### Additional Resources[¶](#additional-resources "Permanent link")

- [Experiment Tracking in DagsHub](../../feature_guide/experiment_tracking/) - Explore more on how to leverage DagsHub for your ML experiments.

### Known Issues, Limitations & Restrictions[¶](#known-issues-limitations-restrictions "Permanent link")

Currently, the migration tool does not support the transfer of certain W&B artifact types due to compatibility issues. However, we are actively working to expand support and enhance the tool\'s capabilities.

Was this page helpful?

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTIwIDEyYTggOCAwIDAgMC04LTggOCA4IDAgMCAwLTggOCA4IDggMCAwIDAgOCA4IDggOCAwIDAgMCA4LThtMiAwYTEwIDEwIDAgMCAxLTEwIDEwQTEwIDEwIDAgMCAxIDIgMTIgMTAgMTAgMCAwIDEgMTIgMmExMCAxMCAwIDAgMSAxMCAxME0xMCA5LjVjMCAuOC0uNyAxLjUtMS41IDEuNVM3IDEwLjMgNyA5LjUgNy43IDggOC41IDhzMS41LjcgMS41IDEuNW03IDBjMCAuOC0uNyAxLjUtMS41IDEuNVMxNCAxMC4zIDE0IDkuNSAxNC43IDggMTUuNSA4czEuNS43IDEuNSAxLjVtLTUgNy43M2MtMS43NSAwLTMuMjktLjczLTQuMTktMS44MUw5LjIzIDE0Yy40NS43MiAxLjUyIDEuMjMgMi43NyAxLjIzczIuMzItLjUxIDIuNzctMS4yM2wxLjQyIDEuNDJjLS45IDEuMDgtMi40NCAxLjgxLTQuMTkgMS44MSIgLz48L3N2Zz4=)

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTIwIDEyYTggOCAwIDAgMC04LTggOCA4IDAgMCAwLTggOCA4IDggMCAwIDAgOCA4IDggOCAwIDAgMCA4LThtMiAwYTEwIDEwIDAgMCAxLTEwIDEwQTEwIDEwIDAgMCAxIDIgMTIgMTAgMTAgMCAwIDEgMTIgMmExMCAxMCAwIDAgMSAxMCAxMG0tNi41LTRjLjggMCAxLjUuNyAxLjUgMS41cy0uNyAxLjUtMS41IDEuNS0xLjUtLjctMS41LTEuNS43LTEuNSAxLjUtMS41TTEwIDkuNWMwIC44LS43IDEuNS0xLjUgMS41UzcgMTAuMyA3IDkuNSA3LjcgOCA4LjUgOHMxLjUuNyAxLjUgMS41bTIgNC41YzEuNzUgMCAzLjI5LjcyIDQuMTkgMS44MWwtMS40MiAxLjQyQzE0LjMyIDE2LjUgMTMuMjUgMTYgMTIgMTZzLTIuMzIuNS0yLjc3IDEuMjNsLTEuNDItMS40MkM4LjcxIDE0LjcyIDEwLjI1IDE0IDEyIDE0IiAvPjwvc3ZnPg==)

Thanks for your feedback!

Thanks for your feedback! Help us improve this page by creating an [issue in our Docs repo](https://dagshub.com/DAGsHub-Official/dagshub-docs/issues).