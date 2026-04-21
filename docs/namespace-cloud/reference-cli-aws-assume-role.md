<!-- Source: https://namespace.so/docs/reference/cli/aws-assume-role -->

# nsc aws assume-role

Uses Workload Federation to assume a particular AWS role.

`aws assume-role` uses Namespace [Workload Federation](/docs/federation) to assume an AWS IAM role. This allows your Namespace workloads to securely access AWS resources without long-lived credentials.

## Usage

```
nsc aws assume-role --role_arn <arn>
```

### Example

```
$ nsc aws assume-role --role_arn arn:aws:iam::123456789012:role/my-role
Obtained credentials from Namespace (took 234ms).
Obtained credentials from AWS (took 456ms).
export AWS_ACCESS_KEY_ID=AKIAIOSFODNN7EXAMPLE
export AWS_SECRET_ACCESS_KEY=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
export AWS_SESSION_TOKEN=AQoDYXdzEJr...
```

## Options

### --role\_arn <arn>

The ARN of the role to assume.

### --aws\_profile <profile>

Use the specified AWS profile.

### --write\_env <path>

Instead of outputting, write the environment variables to the specified file.

### --duration <duration>

For how long the resulting AWS credentials should be valid for. Default is `1h`.

Last updated February 13, 2026
