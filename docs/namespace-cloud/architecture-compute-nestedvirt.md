<!-- Source: https://namespace.so/docs/architecture/compute/nestedvirt -->

# Nested Virtualization

Nested virtualization allows workloads running on Namespace compute instances to use hardware-assisted virtualization (for example through `/dev/kvm` on Linux).

This is commonly used for Android emulator workloads and other virtualization-based CI tasks.

## Linux

Nested virtualization support on Linux depends on architecture and machine family:

| Linux platform | Nested virtualization support |
| --- | --- |
| `linux/amd64` | Supported |
| `linux/arm64` | Not supported on all machine families |

For `linux/arm64`, support is currently available on Linux instances backed by Apple Virtualization.
It is not yet available across every Linux ARM64 machine family.

## macOS

Nested virtualization is not currently available on macOS instances.
This is limited by Apple's Virtualization Framework and its nested virtualization constraints.

## Windows

Nested virtualization is not currently available on Windows instances.

## Android emulators

Android emulator hardware acceleration on Namespace currently requires `linux/amd64`.
For setup guidance, see [Android Emulators](/docs/integrations/android-emulators).

Last updated April 17, 2026
