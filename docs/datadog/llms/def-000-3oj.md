# Source: https://docs.datadoghq.com/security/default_rules/def-000-3oj.md

---
title: 'Linux Hardening: LOCKDOWN mode should be ''none confidentiality'''
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Linux Hardening: LOCKDOWN mode should
  be 'none confidentiality'
---

# Linux Hardening: LOCKDOWN mode should be 'none confidentiality'

## Security recommendation{% #security-recommendation %}

| Impact | Remediation complexity | Severity | Recommended value                  |
| ------ | ---------------------- | -------- | ---------------------------------- |
| 5      | 2                      | 5        | "none [integrity] confidentiality" |

In production environments, it is recommended to set the Lockdown mode to integrity. Although confidentiality would provide a higher level of security, the Lockdown mode can't be downgraded to integrity on demand, thus making it impossible to run debugging tools when needed, even by privileged users. As such, integrity is a good compromise to reduce the kernel attack surface and enforce kernel module signatures while not interfering with monitoring and performance analysis tools.

## Compliance{% #compliance %}

- Audit lockdown mode, [Found in CIS](https://www.cisecurity.org/cis-benchmarks)

## Documentation{% #documentation %}

The Kernel Lockdown feature is designed to prevent both direct and indirect access to a running kernel image, attempting to protect against unauthorized modification of the kernel image and to prevent access to security and cryptographic data located in kernel memory, whilst still permitting driver modules to be loaded.

It is implemented as a Linux Security Module that can be configured in integrity or confidentiality mode. If set to integrity, kernel features that allow userland to modify the running kernel are disabled. If set to confidentiality, kernel features that allow userland to extract confidential information from the kernel are also disabled. Configuration can be done at runtime (through securityfs), boot time (via a kernel parameter) or build time (via a kconfig option).

Under integrity mode, the following security features are enforced:

- `LOCKDOWN_MODULE_SIGNATURE`: This restriction enforces that only signed kernel modules can be loaded, preventing the execution of unauthorized or malicious code within the kernel. It protects against rootkits and other unauthorized kernel modifications.

- `LOCKDOWN_DEV_MEM`: Prevents direct access to /dev/mem, which exposes physical memory. This protects against attackers trying to modify kernel structures or inject malicious code into the system memory.

- `LOCKDOWN_EFI_TEST`: Blocks access to EFI (Extensible Firmware Interface) test interfaces, which could otherwise be abused to modify the firmware. This helps prevent persistent malware from being embedded into the system firmware.

- `LOCKDOWN_KEXEC`: Restricts the ability to load and execute a new kernel via kexec(). This prevents attackers from replacing the running kernel with a compromised one, maintaining system integrity.

- `LOCKDOWN_HIBERNATION`: Prevents the system from entering hibernation, as hibernation images contain sensitive memory data that could be tampered with or stolen by an attacker.

- `LOCKDOWN_PCI_ACCESS`: Restricts direct access to PCI devices to prevent unauthorized manipulation of hardware components, which could be used to compromise the system.

- `LOCKDOWN_IOPORT`: Blocks access to I/O ports, preventing userspace programs from directly controlling hardware, which could lead to privilege escalation or data corruption.

- `LOCKDOWN_MSR`: Restricts access to Model-Specific Registers (MSRs), which control CPU behavior. This protects against attackers modifying CPU settings to enable debugging modes or other exploits.

- `LOCKDOWN_ACPI_TABLES`: Prevents modification of ACPI (Advanced Configuration and Power Interface) tables, which could be exploited to execute unauthorized code in the kernel.

- `LOCKDOWN_DEVICE_TREE`: Blocks modifications to the device tree, which describes the hardware to the kernel. Preventing this helps maintain a trusted hardware configuration.

- `LOCKDOWN_PCMCIA_CIS`: Restricts access to PCMCIA Card Information Structures (CIS) to prevent tampering with legacy hardware interfaces that could be used for privilege escalation.

- `LOCKDOWN_TIOCSSERIAL`: Prevents unauthorized modifications to serial port settings that could be exploited to alter system communications or gain unauthorized access.

- `LOCKDOWN_MODULE_PARAMETERS`: Blocks modifications to kernel module parameters to prevent attackers from altering the behavior of loaded kernel modules, which could lead to security bypasses.

- `LOCKDOWN_MMIOTRACE`: Disables MMIO (Memory-Mapped I/O) tracing, which could otherwise be used to inspect or manipulate sensitive hardware interactions.

- `LOCKDOWN_DEBUGFS`: Restricts access to debugfs, a filesystem that provides deep insights into kernel internals. This restriction helps prevent attackers from gaining system information useful for exploits.

- `LOCKDOWN_XMON_WR`: Restricts write access in the XMON debugger, used on PowerPC systems, to prevent unauthorized kernel debugging or modification.

- `LOCKDOWN_BPF_WRITE_USER`: Prevents eBPF programs from writing to user-space memory, reducing the risk of privilege escalation via manipulated execution flows.

- `LOCKDOWN_DBG_WRITE_KERNEL`: Blocks debug-related writes to kernel memory, preventing attackers from injecting malicious modifications into the kernel.

- `LOCKDOWN_RTAS_ERROR_INJECTION`: Disables error injection via RTAS (Run-Time Abstraction Services), which could be used to manipulate system state or cause deliberate crashes.

Under confidentiality mode, the following security features are enforced on top of the integrity ones:

- `LOCKDOWN_KCORE`: Blocks access to /proc/kcore, which exposes a live dump of kernel memory, protecting against memory disclosure attacks.

- `LOCKDOWN_KPROBES`: Disables kernel probes (kprobes) that allow dynamic instrumentation of the kernel, preventing attackers from using them for kernel exploits.

- `LOCKDOWN_BPF_READ_KERNEL`: Prevents eBPF programs from reading kernel memory, reducing the risk of leaking sensitive kernel data.

- `LOCKDOWN_DBG_READ_KERNEL`: Blocks unauthorized debugging reads from kernel memory, protecting sensitive system information from being disclosed.

- `LOCKDOWN_PERF`: Restricts access to performance monitoring tools that could be used to infer sensitive information or conduct side-channel attacks.

- `LOCKDOWN_TRACEFS`: Prevents access to tracefs, which contains detailed system tracing data, protecting against unauthorized kernel introspection.

- `LOCKDOWN_XMON_RW`: Restricts both read and write access in the XMON debugger to prevent kernel debugging and potential exploitation.

- `LOCKDOWN_XFRM_SECRET`: Prevents unauthorized access to cryptographic secrets stored in XFRM (IPsec framework), ensuring secure communication remains protected.

## Remediation{% #remediation %}

### Prerequisites{% #prerequisites %}

- You must have `root` privileges.
- Secure Boot must be enabled and the kernel must be booted in UEFI Secure Boot mode.
- The kernel must support the Lockdown feature (Linux 5.4+).

### Step-by-step guide{% #step-by-step-guide %}

**Step 1: Check Current Lockdown Mode** Run the following command to see the current mode:

```bash
cat /sys/kernel/security/lockdown
```

You'll see an output similar to `[none] integrity confidentiality`. The brackets `[]` indicate the current active mode.

**Step 2: Enable Lockdown via `sysfs`**

If the current mode is `none`, you can switch to `integrity` (this action is irreversible until reboot). Note that you cannot lower the lockdown level (e.g. from `confidentiality` to `integrity`) or disable Lockdown once it's active: only increasing the level is allowed. Run the following command:

```bash
echo integrity > /sys/kernel/security/lockdown
```

**Step 3: Verify the New Mode**

Run the command from step one again, and check if the Lockdown mode has correctly been updated.

Note that you can also set the Lockdown mode at boot time using the `lockdown=integrity` boot command line argument.
