# Architecture - Resource Limits

Resource limits at Namespace enforced by subscription tier and plan type.

## Concurrency Limits by Plan

Namespace enforces concurrency limits per platform for each subscription tier:

### Developer Plan

- **Linux**: 32 vCPU, 64 GB RAM
- **macOS**: 12 vCPU, 28 GB RAM

### Team Plan

- **Linux**: 64 vCPU, 128 GB RAM
- **macOS**: 24 vCPU, 56 GB RAM
- **Windows**: 32 vCPU, 64 GB RAM

### Business Plan

- **Linux**: 160 vCPU, 320 GB RAM
- **macOS**: 48 vCPU, 112 GB RAM
- **Windows**: 80 vCPU, 160 GB RAM

### Custom Plans

Available for higher needs

## Important Note

There are no restrictions on the number of instances that can run in parallel as long as they fit within the concurrency limit.

## Protecting Limits

Organizations can manage resource allocation through:

### Runner Profile Limits

Restrict concurrent instances per profile.

### Multi-tenant Accounts

- Set global limits
- Per-workspace allocations
- Allow resource sharing between workspaces

## API Error Handling

When requests exceed limits, the system returns structured errors:

- **ResourceLimitsError**: Concurrency exceeded
- **UsageLimitsError**: Billing quota exhausted
- **PlatformNotAllowedError**: Platform not enabled for your plan

## Custom Arrangements

For needs exceeding standard plans, contact the sales team for custom arrangements and special access to higher resource tiers.
