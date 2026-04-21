# Architecture - Machine Shapes

Documentation on flexible compute resources at Namespace through machine shapes, which define CPU, memory, and storage allocations.

## Machine Shape Notation

Follows an "AxB" format where:

- A = vCPUs
- B = GB RAM

Example: 4x16 = 4 vCPUs + 16GB RAM

## Standard Shapes

**Linux/Windows**: 2x4 (minimum) through 32x64 (maximum)

**macOS**: Different shapes with different pricing

## Common Standard Shapes

- 2x4: 2 vCPU, 4GB RAM
- 4x8: 4 vCPU, 8GB RAM
- 4x16: 4 vCPU, 16GB RAM
- 8x16: 8 vCPU, 16GB RAM
- 8x32: 8 vCPU, 32GB RAM
- 16x32: 16 vCPU, 32GB RAM
- 32x64: 32 vCPU, 64GB RAM

## Non-Standard Shapes

Custom configurations allowed. Billing based on the formula:

```text
unit_count = max(vCPU_count, RAM_GB / 2)
```

## High-Memory Options

Extended options up to 512GB require special access.

## Pricing Models

The documentation provides detailed pricing tables showing:

**Linux**: Starting at $0.001/min for 1vCPU2GB

**Windows**: Costs double that of Linux equivalents

**macOS**: Different shapes/pricing (6vCPU14GB starting at $0.06/min)

Prepaid and overage rates differ across tiers.

## Storage & Billing

**Ephemeral storage** scales with machine shape:

- Linux 1x2: 40GB
- Increases proportionally with larger shapes

**Billing**: Per-minute basis with 1-minute minimum; next 15 seconds round down

## Optimization Tips

- Select standard shapes for cost efficiency
- Larger shapes may reduce workflow duration while smaller ones suit non-intensive workloads
- Consider your workload requirements before selecting a shape
