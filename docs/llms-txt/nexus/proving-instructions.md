# Source: https://docs.nexus.xyz/zkvm/specifications/proving-instructions.md

# Proving Instructions

The final component of the Nexus zkVM is the execution component, which is responsible for enforcing the correct execution of the instructions supported by the VM. It is designed with modularity and extensibility in mind.

Currently, this component provides support for the Nexus Virtual Machine (NVM) instruction set described in Section 2 of [the specification](https://docs.nexus.xyz/zkvm/specifications/the-complete-specification). The NVM instruction set is closely related to the RISC-V RV32I unprivileged instruction set found in [the RISC-V specification](https://drive.google.com/file/d/1s0lZxUZaa7eV_O0_WsZzaurFLLww7ou5/view). As a result, existing tooling for RISC-V RV32I can usually be used without modification.

We discuss some of the constraints for this component when we describe our [example](https://docs.nexus.xyz/zkvm/specifications/proving-an-example), but details of all the constraints for this component can be found in Section 8 of [the specification](https://docs.nexus.xyz/zkvm/specifications/the-complete-specification).
