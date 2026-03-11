# Source: https://novita.ai/docs/guides/sandbox-mount-cloudstorage.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Mount object storage bucket in sandbox

export const SandboxConfigHint = () => {
  if (typeof document === "undefined") {
    return null;
  } else {
    return <Note>Before running the example code in this document, please ensure you have properly configured environment variables. For details, please refer to <a href="/guides/sandbox-your-first-agent-sandbox#configure-environment-variables">Configure Environment Variables</a>.</Note>;
  }
};

Each sandbox instance is provisioned with 20GB of ephemeral system disk storage by default for temporary data operations. <u>Upon sandbox termination or timeout, all data within this storage space is automatically purged</u>. Consequently, persistent data requiring long-term retention should be stored in external cloud storage services.

<Tip>
  Sandbox storage allocation specifications are subject to modification. Consult the [Pricing](/guides/sandbox-pricing) documentation for current resource allocations and associated costs.
</Tip>

Object Storage represents a highly scalable, durable, and cost-efficient cloud storage architecture offered by major cloud service providers. Within sandbox environments, object storage can be accessed through two primary methodologies: direct programmatic interaction via cloud provider SDKs or CLI utilities, or through FUSE (Filesystem in Userspace) implementations that present object storage buckets as standard POSIX-compliant filesystem mounts.

<Tip>
  [FUSE (Filesystem in Userspace)](https://www.kernel.org/doc/html/next/filesystems/fuse.html) is a kernel module and userspace library that enables the implementation of fully functional filesystems in userspace applications. This framework provides an abstraction layer that presents remote cloud storage services as standard filesystem hierarchies, enabling transparent file operations through conventional POSIX interfaces.
</Tip>

This documentation provides comprehensive guidance for integrating object storage buckets from leading cloud service providers into sandbox environments through filesystem mounting techniques.

<Warning>
  FUSE-based object storage mounts introduce significant I/O performance overhead due to network latency and protocol translation layers. Applications with stringent performance requirements should avoid this approach. Furthermore, FUSE filesystem operations lack atomicity guarantees inherent to native object storage APIs, creating potential race conditions where local filesystem operations may succeed while corresponding remote operations fail, resulting in data inconsistency.

  This mounting approach is optimal for read-heavy workloads with infrequent write operations and relaxed performance constraints. For performance-critical applications or frequent write patterns, direct integration using cloud provider SDKs or native REST APIs is strongly recommended.
</Warning>

<SandboxConfigHint />

## Amazon S3

Amazon S3 buckets can be mounted as POSIX-compliant filesystems using [s3fs-fuse](https://github.com/s3fs-fuse/s3fs-fuse), a FUSE-based filesystem implementation that provides S3 bucket access through standard file operations.

The s3fs-fuse package can be integrated during [sandbox template](/guides/sandbox-template) creation by incorporating installation commands in the `novita.Dockerfile`, or installed dynamically within active sandbox instances for ad-hoc requirements.

The following `novita.Dockerfile` demonstrates the integration of s3fs-fuse during template building:

<CodeGroup>
  ```dockerfile novita.Dockerfile icon="docker" theme={"system"}
  # Compatible with Debian-based distributions
  FROM ubuntu:latest

  # Critical: s3fs versions below 1.93 contain known mounting issues. Ensure version compatibility.
  RUN DEBIAN_FRONTEND=noninteractive apt-get update && apt-get install -y s3fs
  ```
</CodeGroup>

The following implementation demonstrates programmatic S3 bucket mounting within sandbox environments using s3fs-fuse:

<CodeGroup>
  ```js JavaScript & TypeScript icon="js" theme={"system"}
  import { Sandbox } from 'novita-sandbox'

  const TEMPLATE_ID = process.env.NOVITA_TEMPLATE_ID
  const AWS_ACCESS_KEY_ID = process.env.AWS_ACCESS_KEY_ID
  const AWS_SECRET_ACCESS_KEY = process.env.AWS_SECRET_ACCESS_KEY
  const AWS_BUCKET_NAME = process.env.AWS_BUCKET_NAME
  if (!TEMPLATE_ID || !AWS_ACCESS_KEY_ID || !AWS_SECRET_ACCESS_KEY || !AWS_BUCKET_NAME) {
      throw new Error('Required environment variables not configured: NOVITA_TEMPLATE_ID, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_BUCKET_NAME')
  }

  const MOUNT_DIRECTORY = "/mnt/s3-bucket"

  const sandbox = await Sandbox.create(TEMPLATE_ID)

  // Initialize mount point directory structure
  await sandbox.files.makeDir(MOUNT_DIRECTORY)

  // Configure s3fs credentials using standard credential file location
  // s3fs-fuse reads AWS credentials from /root/.passwd-s3fs by default
  await sandbox.files.write('/root/.passwd-s3fs', `${AWS_ACCESS_KEY_ID}:${AWS_SECRET_ACCESS_KEY}`)

  // Enforce secure credential file permissions (owner read-only)
  await sandbox.commands.run('sudo chmod 600 /root/.passwd-s3fs')

  // Execute S3 bucket mount operation with optimized parameters
  // Configuration parameters:
  // - allow_other: Enable cross-user filesystem access
  // - endpoint: Specify AWS regional endpoint for optimal latency
  // Reference: https://manpages.ubuntu.com/manpages/noble/en/man1/s3fs.1.html
  const mountOptions = 'allow_other,endpoint=us-east-1'
  await sandbox.commands.run(`sudo s3fs ${AWS_BUCKET_NAME} ${MOUNT_DIRECTORY} -o ${mountOptions}`)

  // Validate mount functionality with write operation
  await sandbox.files.write(`${MOUNT_DIRECTORY}/test-file.txt`, 'test-file-content')

  // Verify mount integrity through read operation
  const content = await sandbox.files.read(`${MOUNT_DIRECTORY}/test-file.txt`)
  console.log(content)

  await sandbox.kill()
  ```

  ```python Python icon="python" theme={"system"}
  import os
  from novita_sandbox.core import Sandbox

  TEMPLATE_ID = os.environ.get("NOVITA_TEMPLATE_ID")
  AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
  AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
  AWS_BUCKET_NAME = os.environ.get("AWS_BUCKET_NAME")
  if not TEMPLATE_ID or not AWS_ACCESS_KEY_ID or not AWS_SECRET_ACCESS_KEY or not AWS_BUCKET_NAME:
      raise ValueError("Required environment variables not configured: NOVITA_TEMPLATE_ID, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_BUCKET_NAME")

  MOUNT_DIRECTORY = "/mnt/s3-bucket"

  sandbox = Sandbox.create(TEMPLATE_ID)

  # Initialize mount point directory structure
  sandbox.files.make_dir(MOUNT_DIRECTORY)

  # Configure s3fs credentials using standard credential file location
  # s3fs-fuse reads AWS credentials from /root/.passwd-s3fs by default
  # Custom credential paths require explicit specification via -o passwd_file parameter
  sandbox.files.write("/root/.passwd-s3fs", f"{AWS_ACCESS_KEY_ID}:{AWS_SECRET_ACCESS_KEY}")

  # Enforce secure credential file permissions (owner read-only)
  sandbox.commands.run("sudo chmod 600 /root/.passwd-s3fs")

  # Execute S3 bucket mount operation with optimized parameters
  # Configuration parameters:
  # - allow_other: Enable cross-user filesystem access
  # - endpoint: Specify AWS regional endpoint for optimal latency
  # Reference: https://manpages.ubuntu.com/manpages/noble/en/man1/s3fs.1.html
  mount_options = "allow_other,endpoint=cn-north-1"
  sandbox.commands.run(f"sudo s3fs {AWS_BUCKET_NAME} {MOUNT_DIRECTORY} -o {mount_options}")

  # Validate mount functionality with write operation
  write_result = sandbox.files.write(f"{MOUNT_DIRECTORY}/test-file.txt", "test-file-content")

  # Verify mount integrity through read operation
  content = sandbox.files.read(f"{MOUNT_DIRECTORY}/test-file.txt")
  print("File content:", content)

  sandbox.kill()
  ```
</CodeGroup>


Built with [Mintlify](https://mintlify.com).