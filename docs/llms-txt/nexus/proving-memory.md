# Source: https://docs.nexus.xyz/zkvm/specifications/proving-memory.md

# Proving Memory

The Nexus zkVM has three different components for handling the behavior of each type of memory used by the zkVM. Those types are:

* Program memory: a byte-addressed read-only memory space that contains the program being executed.
* Register memory: a word-addressed read-write memory space that contains the 32 32-bit registers specified by RISC-V RV32I.
* Data memory: a byte-addressed read-write memory space that accounts for all remaining memory used by the program.

To maintain consistency of accesses to the register and data memories, the Nexus zkVM uses a well-known offline memory checking technique (see [BEG+94](#references)). In this technique, each memory cell is associated with a timestamp which serves as a unique identifier for each memory access. In addition to the timestamps, the memory checking algorithm also maintains read and write sets, whose purpose is to record a trace of the program’s memory access pattern.

The main advantage of offline memory checking techniques is that one does not need to keep track of the actual status of the running memory. Instead, the memory checking algorithm only keeps a trace digest of memory accesses, which is inexpensive and can be updated at a cost that is independent of the size of the memory.

For program memory, a simpler memory checking technique can be used to maintain the consistency of the memory accesses. Instead of keeping a timestamp for each memory cell, it suffices to associate a counter to each memory cell to keep track of the number of times that each cell has been read.

In this version of the Nexus zkVM, the computation of the digest is implemented using logarithmic derivatives (also known as logups). See [EKRN24](#references) and [Hab22](#references).

We discuss some of the constraints for these components when we describe our [example](https://docs.nexus.xyz/zkvm/specifications/proving-an-example). Full details of all the constraints for these components can be found in:

* Section 5 of the specification for register memory: <https://docs.nexus.xyz/zkvm/specifications/zkvm-overview>
* Section 6 of the specification for program memory: <https://docs.nexus.xyz/zkvm/specifications/zkvm-overview>
* Section 7 of the specification for data memory: <https://docs.nexus.xyz/zkvm/specifications/zkvm-overview>

## References

* [BEG+94](https://doi.org/10.1007/BF01185212) Manuel Blum, William S. Evans, Peter Gemmell, Sampath Kannan, and Moni Naor. “Checking the correctness of memories”. Algorithmica, 12(2/3):225–244, 1994.
* [EKRN24](https://eprint.iacr.org/2022/510) Liam Eagen, Sanket Kanjalkar, Tim Ruffing, and Jonas Nick. “Bulletproofs++: Next Generation Confidential Transactions via Reciprocal Set Membership Arguments”. In EUROCRYPT 2024.
* [Hab22](https://eprint.iacr.org/2022/1530) Ulrich Haböck. “Multivariate lookups based on logarithmic derivatives”. In: Cryptology ePrint Archive (2022).

Related pages:

* [Proving the CPU](https://docs.nexus.xyz/zkvm/specifications/proving-the-cpu)
* [Proving Instructions](https://docs.nexus.xyz/zkvm/specifications/proving-instructions)
* [Nexus zkVM overview](https://docs.nexus.xyz/zkvm/specifications/the-complete-specification)
* Example: <https://docs.nexus.xyz/zkvm/specifications/example>
