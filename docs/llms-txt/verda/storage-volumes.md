# Source: https://docs.verda.com/infrastructure-as-code/terraform/storage-volumes.md

# Storage – Volumes

## Volume lifecycle behavior

Storage volumes are managed independently from compute instances. This separation allows you to safely reuse volumes across instance restarts or replacements.

Key lifecycle characteristics:

* Deleting an instance does **not** delete attached volumes by default
* Volumes can be detached and reattached to other instances
* Volume data persists until the volume itself is explicitly deleted

For production workloads, it is strongly recommended to protect important volumes using Terraform lifecycle rules.

***

## Safe updates and lifecycle controls

Some operations can permanently affect stored data. To avoid accidental data loss, use Terraform lifecycle settings:

```hcl
resource "verda_volume" "data" {
  name    = "training-data"
  size_gb = 500

  lifecycle {
    prevent_destroy = true
  }
}
```

This prevents the volume from being destroyed unless the protection is explicitly removed.

***

## Resizing volumes

* **Increasing** the volume size is typically supported and does not require recreation
* **Decreasing** the volume size usually requires deleting and recreating the volume
* After resizing, filesystem expansion may be required inside the instance

Always verify resizing behavior in a non-production environment first.

***

## Importing existing volumes

If a volume already exists in Verda, you can bring it under Terraform management:

```bash
terraform import verda_volume.data <volume-id>
```

After importing:

1. Run `terraform plan`
2. Adjust your configuration until the plan shows **no changes**

This ensures Terraform accurately reflects the existing resource state.

***

## Troubleshooting

### Volume not visible inside the instance

* Confirm the volume is attached to the instance
* Verify the device is detected by the operating system
* Ensure the volume is mounted to a directory

### Data not persisting after instance recreation

* Ensure the volume itself was not deleted
* Confirm the same volume ID is reattached to the new instance

### Unexpected volume recreation

* Reducing `size_gb` will force recreation
* Removing lifecycle protection may allow deletion
* Review `terraform plan` output carefully before applying

### Permission or mount errors

* Check filesystem formatting
* Verify mount options and ownership
* Ensure startup scripts handle mounting correctly

For automated mounting and initialization, see **Compute – Startup Scripts**.

***

## Next steps

Once volumes are configured, you can:

* Attach them to compute instances
* Automate mounting using startup scripts
* Use them for datasets, checkpoints, logs, and other stateful workloads
