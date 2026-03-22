<!-- Source: https://docs.verda.com/infrastructure-as-code/terraform/compute-ssh-keys.md -->

# Compute – SSH Keys

SSH keys are used to securely access Verda compute instances. With Terraform, you can manage SSH keys declaratively and attach them to instances as part of your infrastructure-as-code workflow.

Managing SSH keys in Terraform ensures access is reproducible, auditable, and version controlled.

***

## What this page covers

* Creating and managing SSH keys with Terraform
* Attaching SSH keys to compute instances
* Using existing SSH keys
* Rotating and removing keys safely

***

## Basic example

```hcl
resource "verda_ssh_key" "main" {
  name        = "admin-key"
  public_key = file("~/.ssh/id_rsa.pub")
}
```

Once created, the SSH key can be attached to one or more compute instances.

***

## Required fields

The following arguments are **required** when creating an SSH key:

* **`name`** *(String)*\
  A human-readable name for the SSH key.
* **`public_key`** *(String)*\
  The SSH public key material (for example, the contents of `id_rsa.pub`).

***

## Attaching SSH keys to instances

To allow SSH access to an instance, reference one or more SSH key IDs in the instance configuration:

```hcl
resource "verda_instance" "example" {
  description   = "GPU instance for training"
  hostname      = "training-01"
  image         = "ubuntu-22.04"
  instance_type = "1B200.30V"

  ssh_key_ids = [
    verda_ssh_key.main.id
  ]
}
```

You can attach multiple SSH keys if multiple users or automation systems require access.

***

## Using existing SSH keys

If an SSH key already exists in Verda, you can reference it by ID without recreating it:

```hcl
resource "verda_instance" "example" {
  # ...

  ssh_key_ids = [
    "existing-ssh-key-id"
  ]
}
```

This is useful when gradually adopting Terraform for existing infrastructure.

***

## SSH key generation

If you do not already have an SSH key pair, you can generate one locally:

```bash
ssh-keygen -t ed25519 -C "your-email@example.com"
```

Then reference the generated public key file in Terraform:

```hcl
public_key = file("~/.ssh/id_ed25519.pub")
```

***

## Key rotation and removal

To rotate an SSH key:

1. Create a new `verda_ssh_key` resource
2. Attach it to your instances
3. Apply the Terraform changes
4. Remove the old key from configuration
5. Apply again

This avoids accidental lockout during key rotation.

***

## Importing existing SSH keys

You can import an existing SSH key into Terraform state:

```bash
terraform import verda_ssh_key.main <ssh-key-id>
```

After importing, run:

```bash
terraform plan
```

Update your configuration until Terraform reports no changes.

***

## Best practices

* Use one SSH key per user or automation system
* Avoid sharing private keys between users
* Rotate keys periodically
* Manage SSH keys through Terraform for consistent access control

***

## Troubleshooting

* **SSH access denied**\
  Ensure the correct SSH key is attached to the instance and that you are using the matching private key.
* **Key not applied to instance**\
  Confirm the instance was updated after adding the SSH key and that `ssh_key_ids` is set correctly.
* **Lost access after changes**\
  Always add new keys before removing old ones when rotating credentials.
