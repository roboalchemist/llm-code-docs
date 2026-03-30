# Source: https://docs.portainer.io/2.33-lts/faqs/installing/which-arm-architectures-does-portainer-support.md

# Source: https://docs.portainer.io/sts/faqs/installing/which-arm-architectures-does-portainer-support.md

# Source: https://docs.portainer.io/faqs/installing/which-arm-architectures-does-portainer-support.md

# Which ARM architectures does Portainer support?

We build our ARM images to support the ARM64 architecture primarily (as indicated in our [requirements and prerequisites](https://docs.portainer.io/start/requirements-and-prerequisites)), with ARMv7 support also available. We do not provide or support builds below ARMv7 (such as ARMv6) for Portainer.

As architectures evolve and the world moves more toward 64-bit as the default, there is less and less support for 32-bit architectures available. In the case of Portainer, some of the binaries we embed are no longer available for ARMv6 and below, preventing us from being able to provide a fully functioning Portainer environment on these older systems.
