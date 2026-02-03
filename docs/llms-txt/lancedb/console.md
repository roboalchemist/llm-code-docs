# Source: https://docs.lancedb.com/geneva/jobs/console.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.lancedb.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Geneva Console

The Geneva Console provides a web-based interface for monitoring and managing Geneva jobs, clusters, and manifests.

<img src="https://mintcdn.com/lancedb-bcbb4faf/Na_g-iJjGoOj162o/static/assets/images/geneva/console_screenshot.png?fit=max&auto=format&n=Na_g-iJjGoOj162o&q=85&s=e61c30626c0b3b9a456208775727ccc9" alt="geneva-console" data-og-width="1460" width="1460" data-og-height="602" height="602" data-path="static/assets/images/geneva/console_screenshot.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lancedb-bcbb4faf/Na_g-iJjGoOj162o/static/assets/images/geneva/console_screenshot.png?w=280&fit=max&auto=format&n=Na_g-iJjGoOj162o&q=85&s=e4b52701a81836e7c8ae7d705bcb8a6b 280w, https://mintcdn.com/lancedb-bcbb4faf/Na_g-iJjGoOj162o/static/assets/images/geneva/console_screenshot.png?w=560&fit=max&auto=format&n=Na_g-iJjGoOj162o&q=85&s=1743d163ab0c602d33a0c03b7ac7e2a9 560w, https://mintcdn.com/lancedb-bcbb4faf/Na_g-iJjGoOj162o/static/assets/images/geneva/console_screenshot.png?w=840&fit=max&auto=format&n=Na_g-iJjGoOj162o&q=85&s=10c0575adb2fc51389cca1910038483c 840w, https://mintcdn.com/lancedb-bcbb4faf/Na_g-iJjGoOj162o/static/assets/images/geneva/console_screenshot.png?w=1100&fit=max&auto=format&n=Na_g-iJjGoOj162o&q=85&s=5e93be7c07ad13a48c4a93b2b7b0b470 1100w, https://mintcdn.com/lancedb-bcbb4faf/Na_g-iJjGoOj162o/static/assets/images/geneva/console_screenshot.png?w=1650&fit=max&auto=format&n=Na_g-iJjGoOj162o&q=85&s=4d4a674d67fcb5517fed01896c8d4f0d 1650w, https://mintcdn.com/lancedb-bcbb4faf/Na_g-iJjGoOj162o/static/assets/images/geneva/console_screenshot.png?w=2500&fit=max&auto=format&n=Na_g-iJjGoOj162o&q=85&s=2fa23a0303167c05601af524e7c97c45 2500w" />

## Why a Geneva Console?

* Collaboration: The console helps multiple people work together. Individual jobs can be run in a notebook or workflow, but to collaborate on jobs, it helps to be able to see everything that's running on a given database.
* History: See what has run in the past and diagnose any problems with your jobs.
* Shared resources: The console stores definitions of clusters and manifests, so you can easily tell what resources you want to use to run your job.

## Getting Started

The Geneva console is installed with the Geneva Helm chart; [contact LanceDB](https://lancedb.com/contact/) for access to the Helm chart).

1. Install or upgrade the Geneva Helm chart (see [Helm Deployment](/geneva/deployment/helm/)).
2. Find the pod that's running the console:

```bash  theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
kubectl get pods -l app.kubernetes.io/name=geneva-console -n $NAMESPACE

NAME                          READY   STATUS    RESTARTS   AGE
geneva-console-abc123-abcde   2/2     Running   0          4m58s
```

3. Forward port 3000 to access the console:

```bash  theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
kubectl port-forward -n $NAMESPACE geneva-console-abc123-abcde 3000:3000
```

4. Open `http://localhost:3000` in your browser. When prompted, enter your bucket and database, like:

```
s3://my-bucket/my-db
```

## What's in the Console?

### Jobs Overview

The heart of the console is an overview of all jobs that are running on a given database. See each job's status, progress, timing, and initiator.

### Job Details

Click on a job's ID to get more details, especially events that have happened in a job's life cycle, and metrics such as number of workers, rows, and fragments written.

### Clusters

See the Geneva clusters that you have defined to run jobs. Because clusters can be reused by name, this view can help you run a new job with the same resource constraints as a previous job.

### Manifests

See the Manifests you've defined and what packages/dependencies they contain. As with clusters, manifests are reusable, so it's easy to start a new job with the same dependencies as an old one by just specifying the manifest name.
