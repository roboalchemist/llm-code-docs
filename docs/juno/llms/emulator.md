# Source: https://juno.build/docs/reference/emulator.md

# Emulator

The emulator provides a complete local environment to build, test, and run your project without deploying anything live. There are two images available, depending on your needs:

[## ðï¸ Skylab

The junobuild/skylab image is an all-in-one emulator for local development. It bundles everything you need to build, test, and explore the Juno ecosystem:](/docs/reference/emulator/skylab.md)

[## ðï¸ Satellite

Unlike Skylab, the image junobuild/satellite runs a single Satellite in a headless environment, without the Console UI. It always mounts the same Satellite, using the fixed ID jx5yt-yyaaa-aaaal-abzbq-cai.](/docs/reference/emulator/satellite.md)

[## ðï¸ Infrastructure

In the local environment, several services (which can be either canisters or apps on the Internet Computer) are automatically spun up. This ensures that developers have everything they need to start building right out of the box. Thanks to built-in plugins and tooling, these services are automatically integrated into the environment, eliminating the need for developers to manually manage their bindings.](/docs/reference/emulator/infrastructure.md)