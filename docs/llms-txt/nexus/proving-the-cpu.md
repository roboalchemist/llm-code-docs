# Source: https://docs.nexus.xyz/zkvm/specifications/proving-the-cpu.md

# Proving the CPU

The CPU component of the Nexus zkVM’s constraint system is responsible for ensuring that each state transition is correct. In particular, it is responsible for ensuring that the [instruction fetch](https://en.wikipedia.org/wiki/Classic_RISC_pipeline#Instruction_fetch), [instruction decode](https://en.wikipedia.org/wiki/Classic_RISC_pipeline#Instruction_decode), and [write-back](https://en.wikipedia.org/wiki/Classic_RISC_pipeline#Writeback) stages of the classic RISC pipeline are correct. It also facilitates connecting other stages of the pipeline with their respective constraint circuits.

Concretely, the CPU component performs the following tasks for each CPU cycle:

* Interacts with the program memory to fetch the next instruction pointed to by the program counter.
* Decodes that instruction and verifies that it is well-formed.
* Interacts with the register memory component to read the values associated with the instruction’s operands.
* Interacts with the execution component to execute the just-fetched instruction.
* Interacts with the register memory to perform write-back.

We discuss some of the constraints for this component when we describe our [example](https://docs.nexus.xyz/zkvm/specifications/proving-an-example), but details of all the constraints for this component can be found in Section 4 of [the specification](https://docs.nexus.xyz/zkvm/specifications/the-complete-specification).
