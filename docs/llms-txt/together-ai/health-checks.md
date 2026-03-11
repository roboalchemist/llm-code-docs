# Source: https://docs.together.ai/docs/health-checks.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.together.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Health Checks and Node Repair

> Proactively validate GPU node health and trigger repair actions for issues

## Overview

This page covers two key features for maintaining healthy GPU nodes:

1. **Health Checks** - Proactive stress testing and validation of GPU nodes and underlying hardware
2. **Node Repair** - User-triggered remediation actions for node health issues

Together, these features help you maintain optimal cluster performance by identifying issues early and resolving them quickly.

## Health Checks

Health Checks allow you to proactively stress test and validate the health of your GPU nodes and underlying hardware. You can run targeted diagnostic tests to ensure your GPUs, InfiniBand networking, and other components are functioning correctly.

## How to Run Health Checks

### Quick Steps

1. Navigate to your cluster in the Together Cloud UI
2. Go to the **Cluster Details** tab and select the **Health Checks** sub-tab
3. Click the **Run a health check** button (top right)
4. In the "Run Health Checks" dialog:
   * **Select tests** - Choose one or more health check tests to run:
     * **DCGM Diag** - NVIDIA GPU diagnostics
     * **GPU Burn** - GPU stress test
     * **Single-Node NCCL** - Single-node GPU communication test
     * **NVBandwidth: CPU to GPU Bandwidth** - PCIe bandwidth test
     * **NVBandwidth: GPU to CPU Bandwidth** - PCIe bandwidth test
     * **NVBandwidth: GPU-CPU Latency** - PCIe latency test
     * **InfiniBand Write Bandwidth** - InfiniBand network performance test
5. Click **Next: Select Nodes**
6. Choose which nodes to test
7. (Optional) Configure test parameters like duration or diagnostic level
8. Click **Run** to start the health checks

<Note>
  **Active Tests:** These health checks require full GPU utilization from the node and will impact any running workloads during the test.
</Note>

## Available Health Check Tests

Each health check validates different aspects of your GPU infrastructure:

### GPU Diagnostics

**DCGM Diag**

* Runs NVIDIA Data Center GPU Manager diagnostics
* Validates GPU compute capability, memory integrity, and thermal performance
* **Configurable:** Diagnostic level (1-3, where 3 is most comprehensive)
* **Use for:** Comprehensive GPU health validation
* **Learn more:** [NVIDIA DCGM Documentation](https://docs.nvidia.com/datacenter/dcgm/latest/user-guide/dcgm-diagnostics.html)

**GPU Burn**

* Stress tests GPUs with intensive compute workloads
* Validates stability under sustained high utilization
* **Configurable:** Test duration
* **Use for:** Identifying thermal issues, power problems, or instability
* **Learn more:** [GPU Burn on GitHub](https://github.com/wilicc/gpu-burn)

### Network Performance

**Single-Node NCCL**

* Tests NVIDIA Collective Communications Library on a single node
* Validates GPU-to-GPU communication within the node
* **Use for:** Multi-GPU training readiness
* **Learn more:** [NVIDIA NCCL Documentation](https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/index.html)

**InfiniBand Write Bandwidth**

* Measures InfiniBand network write throughput
* Validates high-speed interconnect performance
* **Use for:** Distributed training and multi-node workloads

### PCIe Performance

**NVBandwidth Tests**

* **CPU to GPU Bandwidth** - Host-to-device transfer rates
* **GPU to CPU Bandwidth** - Device-to-host transfer rates
* **GPU-CPU Latency** - Data transfer latency
* **Use for:** Identifying PCIe bottlenecks or degraded lanes
* **Learn more:** [NVIDIA nvbandwidth Documentation](https://github.com/NVIDIA/nvbandwidth)

## Understanding Test Results

Health check results are displayed in the Health Checks table:

* **Status** - Passed (green) or Failed (red) indicator
* **Last Run** - Timestamp of test execution
* **Node Tested** - Which nodes were included in the test
* **Details** - Click "View details" to see:
  * Full test output
  * Detailed metrics and measurements
  * Workflow CR (Custom Resource) with complete results
  * Pass/fail criteria details

## Automatic Acceptance Testing

When you provision a new GPU cluster, Together automatically runs acceptance tests on each node before making it available for your workloads. This ensures that all nodes meet quality standards before joining your cluster.

### During Cluster Provisioning

The cluster provisioning process includes an automatic testing phase:

**Phase: Running Tests**

During this phase, each node undergoes single-node acceptance tests:

* **DCGM Diag Level 2** - Comprehensive GPU diagnostics
* **5-minute GPU Burn** - Sustained GPU stress test
* **Single-Node NCCL** - GPU-to-GPU communication validation
* **Multi-Node NCCL** - GPU-to-GPU communication validation across Node GPUs

You'll see the cluster status as:

* **"Running Tests"** - Acceptance tests are in progress
* **"Tests Failed"** - One or more acceptance tests did not pass
* **"Running"** - Tests passed and cluster is ready

### Viewing Acceptance Test Results

If acceptance tests fail during provisioning:

1. Navigate to your cluster in the Together Cloud UI
2. Go to the **Cluster Details** tab
3. Select the **Health Checks** sub-tab
4. Find the acceptance test runs for the affected nodes
5. Click **"View details"** to see:
   * Which specific test failed (DCGM Diag, GPU Burn, or NCCL)
   * Detailed error messages and logs
   * Performance metrics from the tests

<Note>
  **Automatic Remediation:** If acceptance tests fail, Together's infrastructure team is automatically notified and will investigate. Nodes that fail acceptance tests are not added to your cluster until the issue is resolved.
</Note>

### Why Acceptance Testing Matters

Automatic acceptance testing provides several benefits:

* **Quality Assurance** - Every node is validated before you can use it
* **Early Detection** - Hardware or configuration issues are caught immediately
* **Reduced Downtime** - Problems are fixed before they impact your workloads
* **Consistent Performance** - All nodes meet the same performance standards

<Tip>
  **Provisioning Time:** Acceptance tests typically add 5-10 minutes to cluster provisioning time, but this ensures you receive fully validated, production-ready nodes.
</Tip>

## When to Run Health Checks

**Proactive Testing:**

* Before deploying critical workloads
* After cluster scaling events
* On a regular schedule (weekly/monthly)
* After maintenance windows

**Reactive Testing:**

* When experiencing unexplained job failures
* Before triggering node repair actions
* When investigating performance degradation
* After node repairs to validate fixes

**Specific Issue Investigation:**

* **Training instability** → Run GPU Burn, DCGM Diag
* **Slow data loading** → Run NVBandwidth tests
* **Multi-GPU failures** → Run Single-Node NCCL
* **Distributed training issues** → Run InfiniBand tests

## Best Practices

1. **Schedule workload-free windows** - Health checks require full GPU utilization
2. **Start with DCGM Diag** - Provides comprehensive overview of GPU health
3. **Run baseline tests** - Test new nodes immediately to establish performance baseline
4. **Document results** - Keep records of passed tests for comparison
5. **Test after repair** - Always validate node health after repair actions
6. **Use appropriate test levels** - Higher DCGM diagnostic levels take longer but are more thorough

<Warning>
  **Workload Impact:** Health checks will fully utilize the GPU and may interfere with running workloads. Run tests during maintenance windows or on idle nodes.
</Warning>

## Node Repair

When health checks identify issues or you encounter node problems, you can trigger repair actions directly from the UI to restore node functionality.

### How to Trigger Node Repair

#### Quick Steps

1. Navigate to your cluster in the Together Cloud UI
2. Go to the **Worker Nodes** section
3. Find the problematic node
4. Click the **⋮** (three dots) menu in the **State** column
5. Select **Repair** from the dropdown
6. A repair dialog will appear showing:
   * Node details (name, GPU configuration)
   * Issue detected (if applicable)
   * Impact warning
7. Choose one of the repair actions:
   * **Quick reprovision** - For software issues
   * **Migrate to new host** - For hardware issues
   * **Report an issue** (optional) - To notify support

The repair process will begin immediately and the node will rejoin your cluster once complete.

### Node Repair Lifecycle

When you trigger a repair action, the node goes through the following stages:

```
1. Cordon → 2. Drain → 3. Reprovision/Migrate → 4. Rejoin
```

**1. Cordon**

* Node is marked as unschedulable
* No new workloads will be placed on the node
* Existing workloads continue running

**2. Drain**

* Running workloads are gracefully terminated
* Pods are evicted from the node
* Node becomes empty

**3. Reprovision/Migrate**

* **Quick Reprovision**: VM recreated on a random physical node (could be the same as the original host)
* **Migrate to New Host**: New VM created on different physical hardware

**4. Rejoin**

* Node automatically rejoins the cluster
* Node becomes schedulable again
* Ready to accept new workloads

<Warning>
  **Workload Impact:** All running workloads on the node will be terminated during the drain phase. Ensure your workloads can handle restarts or migrate them before triggering repair.
</Warning>

### Available Repair Actions

**1. Quick Reprovision**

Reprovisions the GPU node VM on a **random underlying physical host**.

**When to use:**

* Software-level issues (driver crashes, library corruption)
* VM configuration problems
* Application-level issues

**What happens:**

* Node follows Cordon → Drain → Reprovision lifecycle
* VM is recreated with fresh software stack
* Node rejoins cluster automatically

<Warning>
  **Data Loss:** You will lose all local VM data during reprovision. Ensure data is stored on PersistentVolumes or backed up.

  **Impact:** No new jobs will be scheduled on this node until remediation completes.
</Warning>

**2. Migrate to New Host**

Provisions a new VM on a **different underlying physical host**.

**When to use:**

* Hardware-level issues (GPU failures, PCIe problems)
* Issues persist after Quick Reprovision
* Physical component failures

**What happens:**

* Node follows Cordon → Drain → Migrate lifecycle
* New VM created on different physical hardware
* Different GPU hardware assigned
* Node rejoins cluster automatically

<Warning>
  **Data Loss:** You will lose all local VM data during migration. Ensure data is stored on PersistentVolumes or backed up.

  **Impact:** No new jobs will be scheduled on this node until remediation completes.
</Warning>

**3. Report an Issue**

Use this option if:

* You're unsure which repair action to use
* You want Together support to investigate before taking action
* The issue requires additional context or diagnosis

### Decision Guide: Which Repair Action to Use

Use this table to determine whether Quick Reprovision can fix your issue or if you need to Migrate to New Host:

| **Issue Type**                         | **Can Reprovision Fix?** | **Needs Physical Repair?** |
| -------------------------------------- | ------------------------ | -------------------------- |
| **Driver crashes/corruption**          | ✓ Yes                    |                            |
| **CUDA/ROCm library issues**           | ✓ Yes                    |                            |
| **GPU process hangs**                  | ✓ Yes                    |                            |
| **Application memory leaks**           | ✓ Yes                    |                            |
| **Incorrect GPU mode settings**        | ✓ Yes                    |                            |
| **GPU not attached to VM**             | ✓ Yes                    |                            |
| **Device permissions/cgroup issues**   | ✓ Yes                    |                            |
| **NUMA affinity problems**             | ✓ Yes                    |                            |
| **Software-based throttling**          | ✓ Yes                    |                            |
| **Recoverable Xid errors**             | ✓ Yes                    |                            |
| **Single-bit ECC errors (occasional)** | ✓ Yes                    |                            |
| **GPU watchdog timeouts**              | ✓ Yes                    |                            |
| **Stuck GPU contexts**                 | ✓ Yes                    |                            |
| **Complete GPU card failure**          |                          | ✓ Yes                      |
| **Persistent multi-bit ECC errors**    |                          | ✓ Yes                      |
| **GPU falling off PCIe bus**           |                          | ✓ Yes                      |
| **Fan failures**                       |                          | ✓ Yes                      |
| **PCIe lane degradation**              |                          | ✓ Yes                      |
| **Power delivery (VRM) issues**        |                          | ✓ Yes                      |
| **Thermal/cooling problems**           |                          | ✓ Yes                      |
| **Persistent Xid errors**              |                          | ✓ Yes                      |
| **Physical connector damage**          |                          | ✓ Yes                      |
| **Backplane/riser issues**             |                          | ✓ Yes                      |

<Note>
  **Key Diagnostic Rule:** If the issue persists after reprovisioning the VM to a fresh instance on the same physical GPU, it's a hardware problem requiring physical node repair (Migrate to New Host).
</Note>

### Monitoring Repair Progress

During the repair process, you'll see the node progress through different states:

1. **Cordoning** - Node marked as unschedulable
2. **Draining** - Workloads being evicted
3. **Repairing** / **Migrating** - VM being recreated or migrated
4. **Joining** - Node rejoining cluster
5. **Running** - Node ready for workloads

You can monitor the progress in the Worker Nodes section of your cluster.

### Best Practices for Node Repair

**Before Triggering Repair:**

1. **Save your data** - Ensure important data is on PersistentVolumes, not local storage
2. **Drain workloads manually** (optional) - For more control over workload migration
3. **Document the issue** - Note symptoms for troubleshooting if repair doesn't resolve the problem
4. **Check running jobs** - Be aware of what will be interrupted

**Choosing the Right Action:**

**Start with Quick Reprovision:**

* Faster (same hardware)
* Resolves most software issues
* Can always escalate to migration if needed

**Use Migrate to New Host when:**

* Quick Reprovision didn't fix the issue
* You see hardware error indicators (ECC errors, Xid errors, thermal warnings)
* GPU diagnostics show hardware problems

**After Repair:**

1. **Verify node health** - Check that the node shows as "Running" in cluster
2. **Test GPU functionality** - Run a simple GPU workload to confirm operation
3. **Monitor for recurrence** - Watch for the same issues returning
4. **Check node metrics** - Ensure GPU metrics look normal

### Common Diagnostic Commands

Before triggering repair, you can SSH into the node to diagnose issues:

```bash  theme={null}
# Check GPU status
nvidia-smi

# Check for Xid errors in system logs
sudo dmesg | grep -i xid

# Check GPU memory errors
nvidia-smi -q | grep -i ecc

# Check GPU temperature and throttling
nvidia-smi -q | grep -E 'Temperature|Throttle'

# Check PCIe link status
nvidia-smi -q | grep -E 'Link Width|Link Speed'

# Check running processes on GPU
nvidia-smi pmon

# Detailed GPU query
nvidia-smi -q
```

[Learn how to SSH into nodes →](/docs/gpu-clusters-management#direct-ssh-access)

### When to Contact Support

Contact [support@together.ai](mailto:support@together.ai) if:

* Issues persist after both repair actions
* You see repeated failures on multiple nodes
* You need help diagnosing whether an issue is software or hardware
* Repair actions fail to complete
* You're unsure which repair action to use
* The node doesn't rejoin after repair completes

Alternatively, use the **Report an issue** button in the repair dialog to notify support directly.

## What's Next?

* [Learn about cluster management](/docs/gpu-clusters-management)
* [Monitor cluster health](/docs/gpu-clusters-management#monitoring-and-status)
* [SSH into nodes for diagnostics](/docs/gpu-clusters-management#direct-ssh-access)
* [Scale your cluster](/docs/gpu-clusters-management#cluster-scaling)


Built with [Mintlify](https://mintlify.com).