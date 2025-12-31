# Source: https://docs.kaisar.io/kaisar-network/kaisar-ai-ops/troubleshooting/troubleshooting.md

# Troubleshooting

Common issues and solutions for Kaisar AI Ops.

## Overview

This section covers:

* [FAQ](https://docs.kaisar.io/kaisar-network/kaisar-ai-ops/troubleshooting/troubleshooting/faq) - Frequently asked questions
* [Known Issues](https://docs.kaisar.io/kaisar-network/kaisar-ai-ops/troubleshooting/troubleshooting/known-issues) - Current limitations
* [Support](https://docs.kaisar.io/kaisar-network/kaisar-ai-ops/troubleshooting/troubleshooting/support) - How to get help

## Quick Troubleshooting

### Cannot Log In

**Symptoms**: Login page shows error or redirects back

**Solutions**:

1. Clear browser cache and cookies
2. Try incognito/private mode
3. Verify credentials with admin
4. Check if MFA is required
5. Try password reset

### Experiment Won't Start

**Symptoms**: Experiment stuck in "pending" status

**Solutions**:

1. Check resource quotas
2. Verify compute resources are available
3. Review experiment configuration
4. Check cluster capacity
5. View experiment logs for errors

### Slow Dashboard Loading

**Symptoms**: Dashboard takes long to load

**Solutions**:

1. Check internet connection
2. Clear browser cache
3. Reduce number of displayed items
4. Check system status page
5. Try different browser

### API Requests Failing

**Symptoms**: 401, 403, or 500 errors

**Solutions**:

1. Verify API token is valid
2. Check token permissions
3. Review rate limits
4. Check API endpoint URL
5. Verify request format

## Common Error Messages

### "Quota Exceeded"

**Cause**: Resource limit reached

**Solution**:

1. Check current usage
2. Clean up unused resources
3. Request quota increase
4. Optimize resource allocation

### "Permission Denied"

**Cause**: Insufficient permissions

**Solution**:

1. Check your role
2. Request access from admin
3. Verify resource sharing settings
4. Check organization membership

### "Resource Not Found"

**Cause**: Invalid ID or deleted resource

**Solution**:

1. Verify resource ID
2. Check if resource was deleted
3. Ensure you have access
4. Try listing resources first

## Performance Issues

### Slow Experiment Training

**Possible Causes**:

* Inefficient data loading
* Suboptimal batch size
* CPU bottleneck
* Network I/O issues

**Solutions**:

1. Profile your code
2. Optimize data pipeline
3. Increase batch size
4. Use data caching
5. Check GPU utilization

### High Memory Usage

**Possible Causes**:

* Large batch size
* Memory leaks
* Inefficient model architecture

**Solutions**:

1. Reduce batch size
2. Use gradient accumulation
3. Enable mixed precision training
4. Profile memory usage
5. Clear unused variables

## Integration Issues

### Authentication Service Failing

**Solutions**:

1. Verify Authentication Service is running
2. Check client configuration
3. Review realm settings
4. Verify redirect URIs
5. Check SSL certificates

### Storage Connection Failed

**Solutions**:

1. Verify credentials
2. Check bucket/container exists
3. Review IAM permissions
4. Test network connectivity
5. Verify endpoint URL

## Getting Help

### Self-Service Resources

* [FAQ](https://docs.kaisar.io/kaisar-network/kaisar-ai-ops/troubleshooting/troubleshooting/faq) - Common questions
* [User Guide](https://github.com/Kaisar-Network/docs/blob/kaisar-ai-ops/kaisar-ai-ops/user-guide/README.md) - Feature documentation
* [API Reference](https://github.com/Kaisar-Network/docs/blob/kaisar-ai-ops/kaisar-ai-ops/api-reference/README.md) - API documentation

### Contact Support

* [Support Portal](https://docs.kaisar.io/kaisar-network/kaisar-ai-ops/troubleshooting/troubleshooting/support) - Submit tickets
* Email: <support@kaisar.io>
* Slack: #kaisar-support

### Community

* GitHub Discussions
* Stack Overflow (tag: kaisar-ai-ops)
* Community Forum

## Diagnostic Tools

### Health Check

Check system health:

```bash
curl https://ai.kaisar.io/health
```

### API Verification

Verify API access:

```bash
curl -X GET https://ai.kaisar.io/api/v1/auth/verify \
  -H "Authorization: Bearer YOUR_TOKEN"
```

### Network Test

Test connectivity:

```bash
ping ai.kaisar.io
traceroute ai.kaisar.io
```

## Best Practices

* ✅ Check system status before reporting issues
* ✅ Collect error messages and logs
* ✅ Try basic troubleshooting first
* ✅ Document steps to reproduce
* ✅ Include relevant screenshots
* ✅ Provide system information

## Next Steps

* Review [FAQ](https://docs.kaisar.io/kaisar-network/kaisar-ai-ops/troubleshooting/troubleshooting/faq) for common questions
* Check [Known Issues](https://docs.kaisar.io/kaisar-network/kaisar-ai-ops/troubleshooting/troubleshooting/known-issues)
* Contact [Support](https://docs.kaisar.io/kaisar-network/kaisar-ai-ops/troubleshooting/troubleshooting/support) if needed
