# Source: https://docs.firehydrant.com/docs/runbook-step-script.md

# Script

<Image alt="Script Runbook step" align="center" width="650px" src="https://files.readme.io/35022b9-image.png">
  Script Runbook step
</Image>

While mitigating an outage, you may run into recurring problems you don't have the engineering resources to address or just can't automate the remediation for various reasons. Engineers commonly write one-off scripts to patch a problem; these one-off solutions end up in GitHub, local text files, Slack code snippets, or Google Docs and are frequently forgotten and then recreated.

FireHydrant lets you store these scripts and track their execution, success, and usefulness with our Runbook Execute a Script step. We'll show the raw script, letting your engineers copy/paste it into their terminal or give you a curl command to execute it and report the status back into FireHydrant. This lets you track when the scripts are executed, by whom, and their output. 

## Configuration

To add this step, Create or Edit a Runbook and then click "+ Add step." Search for "script" and then click on this step.

This Runbook step has two configurable fields:

* **Description** - A blurb or other description about this particular script. It's beneficial to provide information like what this script does, why it should be executed, etc.
* **Script to be executed** - The actual Shell or Bash script to be executed.

## Runbook Execution

Your engineers will be presented with the script itself along with a `curl`  command allowing FireHydrant to capture the error status and output. This is viewable from both Slack as well as the Command Center.

This lets you record when the step was executed, by whom, and if it was successful. 

<Image alt="Viewing the Script step from Slack" align="center" width="400px" src="https://support.firehydrant.com/hc/article_attachments/360088731232/60481c9dad2ed.png">
  Viewing the Script step from Slack
</Image>

If you run the script using the provided `cURL` command, the step will automatically transition from pending to complete or error. You can see below that the error status (missing API token) was recorded by FireHydrant:

<Image alt="Viewing the Script step via Command Center > Runbooks tab" align="center" width="650px" src="https://support.firehydrant.com/hc/article_attachments/360088731252/60481c9edada8.png">
  Viewing the Script step via Command Center > Runbooks tab
</Image>