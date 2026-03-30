# Source: https://docs.jit.io/docs/configuring-self-hosted-runners-for-jit.md

# Configuring Self-Hosted Runners for Jit

This guide explains how to configure self-hosted runners for Jit. In this guide, we will configure your self-hosted runners so that Jit's security scans can run on them smoothly.

## Prerequisites

Before configuring self-hosted runners, ensure the following:

* Runner Environment: Use a compatible amd64 architecture (x86) machine.
* Tools Installed:
  * git
  * jq
  * nodejs
  * npm
* Docker Installed: Runners rely on Docker to execute jobs.

## Kubernetes Setup

1. Create a runnerDeployment Spec

Use the following Kubernetes RunnerDeployment spec as a reference:

```
apiVersion: actions.summerwind.dev/v1alpha1  
kind: RunnerDeployment  
metadata:  
  name: some-runner-group-name  
spec:  
  template:  
    spec:  
      securityContext:  
        fsGroup: <GID>  
        runAsUser: <UID>  
        runAsNonRoot: true  
      containers:  
        - name: runner  
          securityContext:  
            privileged: false  
            runAsNonRoot: true  
            capabilities:  
              drop:  
                - "ALL"  
      organization: <GH-ORG>  
      image: <CUSTOM-UBUNTU-IMAGE>  
      dockerdWithinRunnerContainer: true  
      dockerEnabled: false  
      labels:  
        - some-runner-group-name
```

2. Configure the Jit Runner

Update the .jit/jit-config.yml file to specify the runner label:

```
github:  
  runner: some-runner-group-name
```

3. Apply the Helm Chart
4. Retrieve credentials from the admin portal - TO VERIFY

Apply the appropriate Helm chart for GitLab runners, ensuring the following values are set:

```
runners:  
  config: |  
    \[[runners]]  
    name = "gitlab-runner"  
    executor = "kubernetes"  
    [runners.kubernetes]  
    image_pull_secrets = ["jit-creds"]  
    pull_policy = ["always"]
    namespace = "\<your_namespace>"
```

5. Verify the Runner - Ensure the runner is registered under Assigned project runners in GitLab.

## EC2 Setup

1. Start an SSH tunnel to the desired instance.
2. Enable privileged mode for Docker in the runner configuration:

```
sudo nano /etc/gitlab-runner/config.toml
```

Add:

```
[runners.docker]
privileged = true
```

## Troubleshooting Common Issues

### Docker Privilege Errors

If you encounter errors like these:

```
AppArmor detection and --privileged mode might break.  
mount: permission denied (are you root?)
```

Ensure the following is set in /etc/gitlab-runner/config.toml:

```
[runners.docker]  
privileged = true
```

### Platform Mismatch Errors

Ensure your runner uses amd64 architecture:

```
WARNING: The requested image's platform (linux/amd64) does not match the detected host platform (linux/arm64/v8)
```

### Jobs Stuck on "Pending"

If jobs are stuck despite the runner being active:

1. Ensure the **Run untagged jobs** is checked.
2. Verify job tags match the runner tags.