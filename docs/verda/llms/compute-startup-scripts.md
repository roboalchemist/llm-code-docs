<!-- Source: https://docs.verda.com/infrastructure-as-code/terraform/compute-startup-scripts.md -->

# Compute – Startup Scripts

Startup scripts allow you to run initialization logic automatically when a Verda compute instance is created. They are commonly used to install system packages, configure services, prepare machine learning environments, or perform other one-time setup tasks.

In Terraform, startup scripts are managed as **first-class resources** using `verda_startup_script` and then attached to compute instances. This separation makes startup scripts reusable across multiple instances and environments.

***

## How startup scripts work

* Startup scripts run **once**, during the **first boot** of an instance.
* Scripts are executed **as root**.
* Updating a startup script does **not** affect existing instances unless they are recreated.
* A single startup script can be reused by multiple instances.

***

## Defining a startup script

Create a startup script using the `verda_startup_script` resource. The script must include a valid shebang (for example, `#!/bin/bash`).

```hcl
resource "verda_startup_script" "basic" {
  name = "basic-setup"
  script = <<-EOF
    #!/bin/bash
    set -e

    apt-get update
    apt-get install -y curl wget git
  EOF
}
```

For more complex setups, startup scripts can install Docker, ML frameworks, or perform custom configuration steps.

***

## Attaching a startup script to an instance

Once defined, reference the startup script from a compute instance using `startup_script_id`:

```hcl
resource "verda_instance" "example" {
  name              = "training-01"
  instance_type     = "gpu-a100-80gb"
  image             = "ubuntu-24.04-cuda-12.8-open-docker"
  startup_script_id = verda_startup_script.basic.id

  ssh_key_ids = [verda_ssh_key.main.id]
}
```

The script will be executed automatically when the instance is created.

***

### Common use cases

Startup scripts are typically used for:

* Installing system packages and drivers
* Setting up Python, CUDA, or ML frameworks
* Configuring users, permissions, or SSH settings
* Pulling application code or model artifacts
* Starting background services or agents

***

### Best practices

* Use `set -e` to fail fast on errors.
* Keep scripts **idempotent** where possible.
* Store scripts in Terraform using heredocs or external files (`file()`).
* Avoid hardcoding secrets — use environment variables or secure storage.
* Treat startup scripts as immutable: recreate instances when scripts change.

***

### Importing existing startup scripts

Existing startup scripts can be imported into Terraform state:

```bash
terraform import verda_startup_script.example <startup-script-id>
```

***

### Notes and limitations

* Startup scripts run only on **initial creation**.
* Changes to `startup_script_id` typically require instance replacement.
* Logs and side effects depend on your script implementation.

For the full schema and advanced examples, see the **Verda Startup Script resource documentation**.
