<!-- Source: https://namespace.so/docs/architecture/compute/windows -->

# Windows

Namespace now offers early access to Windows instances, using the same AMD EPYC processors that power our Linux environments.
During the early access not all Namespace features may be available yet.

## Key Features

- **Native Windows builds**
  Compile and package your application using Windows-native toolchains, libraries, and build systems.
- **Cross-platform validation**
  Test and verify behavior in real Windows environments to ensure full compatibility across macOS, Linux, and Windows.
- **Scalable memory configurations**
  Run memory-intensive Windows workloads with support for large-memory instance shapes.

## RDP Access

Namespace supports visual debug access which is invaluable for debugging GUI applications, testing user interfaces, and investigating display-related issues.

To gain interactive, visual access to your Windows runners, you can rely on our RDP integration.

![Windows RDP](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fwindows-demo.338ac8f5.png&w=1200&q=75)

You can start an RDP session using our [CLI](/docs/reference/cli/installation).

```
$

```
nsc rdp <instance-id>
```
```

RDP credentials are printed on the CLI and currently need to be entered in the RDP client manually.

Last updated September 17, 2025
