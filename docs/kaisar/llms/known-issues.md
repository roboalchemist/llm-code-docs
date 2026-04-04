# Source: https://docs.kaisar.io/kaisar-network/kaisar-ai-ops/troubleshooting/troubleshooting/known-issues.md

# Known Issues

Current limitations and known issues in Kaisar AI Ops.

> \[!NOTE] This page is regularly updated. Last updated: 2024-01-15

## Platform Issues

### Cluster and Jobs Sections Not Accessible

**Status**: Under Development **Severity**: Low **Description**: The "Cluster" and "Jobs" menu items are visible in the sidebar but not currently clickable or functional. **Workaround**: Use the Experiments feature for job submission. **ETA**: Q2 2024

### Large Dataset Upload Timeout

**Status**: Known Issue **Severity**: Medium **Description**: Uploading datasets larger than 10GB may timeout in the browser. **Workaround**: Use the CLI or API for large uploads, or split datasets into smaller chunks. **Fix**: Planned for next release

### Dashboard Refresh Delay

**Status**: Known Issue **Severity**: Low **Description**: Dashboard metrics may take up to 60 seconds to refresh. **Workaround**: Manually refresh the page for latest data. **Fix**: Under investigation

## Experiments

### GPU Memory Not Released

**Status**: Known Issue **Severity**: Medium **Description**: In some cases, GPU memory is not fully released after experiment completion. **Workaround**: Restart the experiment or wait for automatic cleanup (5 minutes). **Fix**: Planned for v1.5

### Experiment Logs Truncated

**Status**: Known Issue **Severity**: Low **Description**: Experiment logs longer than 10MB may be truncated in the UI. **Workaround**: Download full logs via API or CLI. **Fix**: Improved log viewer in development

### Concurrent Experiment Limit

**Status**: By Design **Severity**: Low **Description**: Maximum 50 concurrent experiments per organization. **Workaround**: Queue additional experiments or request quota increase. **Note**: This is a configurable limit

## Models

### ONNX Model Preview Not Supported

**Status**: Feature Request **Severity**: Low **Description**: ONNX models cannot be previewed in the UI. **Workaround**: Download and inspect locally. **ETA**: Q3 2024

### Model Download Speed

**Status**: Known Issue **Severity**: Low **Description**: Large model downloads (>5GB) may be slow. **Workaround**: Use direct S3/GCS access if configured. **Fix**: CDN integration planned

## Deployments

### Cold Start Latency

**Status**: Known Issue **Severity**: Medium **Description**: First request to a deployment may take 30-60 seconds (cold start). **Workaround**: Configure minimum instances > 0 to keep instances warm. **Fix**: Improved cold start optimization in progress

### Auto-scaling Delay

**Status**: By Design **Severity**: Low **Description**: Auto-scaling takes 2-3 minutes to provision new instances. **Workaround**: Set appropriate min/max instances based on expected traffic. **Note**: This is normal cloud provider behavior

## API

### Rate Limit Headers Missing

**Status**: Known Issue **Severity**: Low **Description**: Some API endpoints don't return rate limit headers. **Workaround**: Monitor 429 responses. **Fix**: Planned for v1.4

### Webhook Retry Logic

**Status**: Known Issue **Severity**: Medium **Description**: Failed webhooks are retried only 3 times. **Workaround**: Implement your own retry logic or use a message queue. **Fix**: Configurable retry policy in development

## Browser Compatibility

### Safari Private Mode Issues

**Status**: Known Issue **Severity**: Low **Description**: Some features may not work in Safari Private Mode due to cookie restrictions. **Workaround**: Use normal browsing mode or a different browser. **Fix**: Under investigation

### Internet Explorer Not Supported

**Status**: By Design **Severity**: N/A **Description**: Internet Explorer is not supported. **Workaround**: Use Chrome, Firefox, Safari, or Edge. **Note**: No plans to support IE

## Integrations

### GitHub Enterprise Server

**Status**: Limited Support **Severity**: Medium **Description**: GitHub Enterprise Server integration has limited functionality. **Workaround**: Use GitHub.com or manual Git integration. **Fix**: Full support planned for Q2 2024

### Slack Notification Delays

**Status**: Known Issue **Severity**: Low **Description**: Slack notifications may be delayed by 1-2 minutes. **Workaround**: Use email for time-critical notifications. **Fix**: Under investigation

## Performance

### Large Organization Slowdown

**Status**: Known Issue **Severity**: Medium **Description**: Organizations with >10,000 experiments may experience slow dashboard loading. **Workaround**: Use filters and pagination, or archive old experiments. **Fix**: Database optimization in progress

### Search Performance

**Status**: Known Issue **Severity**: Low **Description**: Search may be slow for organizations with many resources. **Workaround**: Use specific filters to narrow results. **Fix**: Search index optimization planned

## Security

### MFA Recovery Codes

**Status**: Known Issue **Severity**: Medium **Description**: Recovery codes are shown only once and cannot be regenerated. **Workaround**: Save recovery codes securely when first generated. **Fix**: Recovery code regeneration feature planned

## Reporting Issues

If you encounter an issue not listed here:

1. Check the [FAQ](https://docs.kaisar.io/kaisar-network/kaisar-ai-ops/troubleshooting/troubleshooting/faq)
2. Review [Troubleshooting](https://docs.kaisar.io/kaisar-network/kaisar-ai-ops/troubleshooting/troubleshooting)
3. Search existing issues
4. Submit a new issue via [Support](https://docs.kaisar.io/kaisar-network/kaisar-ai-ops/troubleshooting/troubleshooting/support)

When reporting, include:

* Steps to reproduce
* Expected vs. actual behavior
* Error messages and logs
* Browser/OS information
* Screenshots if applicable

## Workaround Index

Quick reference for common workarounds:

| Issue                   | Workaround                 |
| ----------------------- | -------------------------- |
| Large dataset upload    | Use CLI/API                |
| GPU memory not released | Wait 5 minutes or restart  |
| Slow dashboard          | Use filters and pagination |
| Cold start latency      | Set min instances > 0      |
| Webhook failures        | Implement retry logic      |
| Safari private mode     | Use normal mode            |

## Next Steps

* Review [FAQ](https://docs.kaisar.io/kaisar-network/kaisar-ai-ops/troubleshooting/troubleshooting/faq) for common questions
* Check [Troubleshooting](https://docs.kaisar.io/kaisar-network/kaisar-ai-ops/troubleshooting/troubleshooting) for solutions
* Contact [Support](https://docs.kaisar.io/kaisar-network/kaisar-ai-ops/troubleshooting/troubleshooting/support) for assistance
