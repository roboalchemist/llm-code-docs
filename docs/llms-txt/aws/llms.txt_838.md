# Source: https://docs.aws.amazon.com/vm-import/latest/userguide/llms.txt

# VM Import/Export User Guide

> VM Import/Export enables you to import virtual machine images from your existing virtualization environment to Amazon EC2, and then export them back.

- [What is VM Import/Export?](https://docs.aws.amazon.com/vm-import/latest/userguide/what-is-vmimport.html)
- [Troubleshooting](https://docs.aws.amazon.com/vm-import/latest/userguide/vmimport-troubleshooting.html)
- [Document history](https://docs.aws.amazon.com/vm-import/latest/userguide/doc-history.html)

## [How to get started with VM Import/Export](https://docs.aws.amazon.com/vm-import/latest/userguide/vmimport-where-do-i-go.html)

- [Accessing VM Import/Export](https://docs.aws.amazon.com/vm-import/latest/userguide/vmimport-interface.html): Understand the different methods to access and use VM Import/Export.


## [How VM Import/Export works](https://docs.aws.amazon.com/vm-import/latest/userguide/how-vm-import-export-works.html)

- [Compare image import with instance import](https://docs.aws.amazon.com/vm-import/latest/userguide/vmimport-differences.html): Compare the different options to import your virtual machine (VM) using VM Import/Export.
- [Image import overview](https://docs.aws.amazon.com/vm-import/latest/userguide/image-import.html): Learn how image import works in VM Import/Export with an overview of the process.
- [Instance import overview](https://docs.aws.amazon.com/vm-import/latest/userguide/instance-import.html): Learn how instance import works in VM Import/Export with an overview of the process.


## [Requirements](https://docs.aws.amazon.com/vm-import/latest/userguide/vmie_prereqs.html)

- [System requirements](https://docs.aws.amazon.com/vm-import/latest/userguide/prerequisites.html): Learn about the requirements for resources that you import into Amazon EC2 using VM Import/Export.
- [Limitations for importing resources](https://docs.aws.amazon.com/vm-import/latest/userguide/limitations-image-importing.html): Learn about the limitations for resources that you import using VM Import/Export
- [Required configurations](https://docs.aws.amazon.com/vm-import/latest/userguide/prepare-vm-image.html): Learn about the required configurations you need to make before exporting your virtual machines (VMs) from your virtualization environment before you use VM Import/Export.
- [Required permissions](https://docs.aws.amazon.com/vm-import/latest/userguide/required-permissions.html): Learn about the required permissions you need to have before you use VM Import/Export.


## [Licensing options](https://docs.aws.amazon.com/vm-import/latest/userguide/licensing.html)

- [Licensing considerations](https://docs.aws.amazon.com/vm-import/latest/userguide/licensing-considerations.html): Learn about licensing considerations for your virtual machines (VMs) that you import into Amazon EC2 using VM Import/Export.
- [Specify a licensing option](https://docs.aws.amazon.com/vm-import/latest/userguide/licensing-specify-option.html): Learn how to specify a licensing option for the virtual machines (VMs) that you import into Amazon EC2 using VM Import/Export.


## [VM Import/Export processes](https://docs.aws.amazon.com/vm-import/latest/userguide/import-export-processes.html)

### [Image import](https://docs.aws.amazon.com/vm-import/latest/userguide/vmimport-image-import.html)

Import a VM from a virtualization environment to Amazon EC2 as an Amazon Machine Image (AMI).

- [Export your VM](https://docs.aws.amazon.com/vm-import/latest/userguide/export-vm-image.html): Learn how to export your virtual machine (VM) from its virtualization environment and import it with VM Import/Export.
- [Programmatic modifications](https://docs.aws.amazon.com/vm-import/latest/userguide/import-modify-vm.html): Learn about the programmatic modifications made to virtual machines (VMs) by VM Import/Export.
- [Import your VM as an image](https://docs.aws.amazon.com/vm-import/latest/userguide/import-vm-image.html): Learn how to import your virtual machine (VM) as an image with VM Import/Export.
- [Monitor an import image task](https://docs.aws.amazon.com/vm-import/latest/userguide/check-import-task-status.html): Learn how to monitor an image import task in VM Import/Export.
- [Cancel an import image task](https://docs.aws.amazon.com/vm-import/latest/userguide/cancel-upload.html): Learn how to cancel an import image task in VM Import/Export.
- [Create an instance from an image](https://docs.aws.amazon.com/vm-import/latest/userguide/import-vm-next-steps.html): Learn how to use the image you imported using VM Import/Export.

### [Snapshot import](https://docs.aws.amazon.com/vm-import/latest/userguide/vmimport-import-snapshot.html)

Import a disk from a virtualization environment to Amazon EC2 as an Amazon EBS snapshot.

- [Monitor an import snapshot task](https://docs.aws.amazon.com/vm-import/latest/userguide/check-status-import-task.html): Learn how to monitor an import snapshot task in VM Import/Export.
- [Cancel an import snapshot task](https://docs.aws.amazon.com/vm-import/latest/userguide/cancel-import-task.html): Learn how to cancel an import image task in VM Import/Export.
- [Create a volume from a snapshot](https://docs.aws.amazon.com/vm-import/latest/userguide/import-snapshot-next-steps.html): Learn how to use the snapshot that you imported to AWS using VM Import/Export.
- [Instance import](https://docs.aws.amazon.com/vm-import/latest/userguide/vmimport-instance-import.html): Import a VM from a virtualization environment to Amazon EC2 as an instance using VM Import/Export.

### [Export from an instance](https://docs.aws.amazon.com/vm-import/latest/userguide/vmexport.html)

Export a copy of an EC2 instance to your on-premises virtualization environment.

- [Prerequisites](https://docs.aws.amazon.com/vm-import/latest/userguide/vmexport-prerequisites.html): Understand the prerequisites to export an instance from Amazon EC2 with VM Import/Export.
- [Considerations for instance export](https://docs.aws.amazon.com/vm-import/latest/userguide/vmexport-limits.html): Review the limitations and considerations for instance export in VM Import/Export.
- [Start an instance export task](https://docs.aws.amazon.com/vm-import/latest/userguide/export-instance.html): Understand how to start an instance export task with VM Import/Export.
- [Monitor an instance export task](https://docs.aws.amazon.com/vm-import/latest/userguide/vmexport-monitor.html): Understand how to monitor an instance export task in VM Import/Export.
- [Cancel an instance export task](https://docs.aws.amazon.com/vm-import/latest/userguide/vmexport-cancel.html): Understand how to cancel an instance export task in VM Import/Export.

### [Export from an AMI](https://docs.aws.amazon.com/vm-import/latest/userguide/vmexport_image.html)

Export a VM from an EC2 AMI for installation in your on-premises virtualization environment.

- [Prerequisites](https://docs.aws.amazon.com/vm-import/latest/userguide/prerequisites-image-export.html): Understand the prerequisites for exporting an image from Amazon EC2 with VM Import/Export.
- [Considerations for image export](https://docs.aws.amazon.com/vm-import/latest/userguide/limits-image-export.html): Understand the considerations and limitations for image export with VM Import/Export.
- [Start an export image task](https://docs.aws.amazon.com/vm-import/latest/userguide/start-image-export.html): Understand how to export an image with VM Import/Export.
- [Monitor an export image task](https://docs.aws.amazon.com/vm-import/latest/userguide/monitor-image-export.html): Understand how to monitor export image tasks in VM Import/Export.
- [Cancel an export image task](https://docs.aws.amazon.com/vm-import/latest/userguide/cancel-image-export.html): Understand how to cancel an export image task in VM Import/Export.


## [Security](https://docs.aws.amazon.com/vm-import/latest/userguide/security.html)

- [Data protection](https://docs.aws.amazon.com/vm-import/latest/userguide/data-protection.html): Learn how the AWS shared responsibility model applies to data protection in VM Import/Export.
- [Compliance validation](https://docs.aws.amazon.com/vm-import/latest/userguide/compliance-validation.html): Learn what AWS services are in scope of a specific compliance program.
- [Resilience](https://docs.aws.amazon.com/vm-import/latest/userguide/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy, and learn about specific VM Import/Export features for data resiliency.
- [Infrastructure security](https://docs.aws.amazon.com/vm-import/latest/userguide/infrastructure-security.html): Learn how VM Import/Export isolates service traffic.
