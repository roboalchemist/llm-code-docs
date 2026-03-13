# Source: https://docs.nexus.xyz/zkvm/specifications/proving-an-example.md

# Proving — An Example

In order to illustrate how these different components work together, let us consider an example in which the program counter pc points to memory location 0x00000004, containing the binary encoding of the instruction `ADDI x10 x8 3`. Moreover, for the sake of this example, let us assume the following about the state of the VM.

* Current clock cycle: 256
* Current trace row: 255
* Total number of rows: 2^16
* R\[x8] = 0x000000FF was last updated with timestamp 323
* R\[x10] = 0x00000005 was last updated with timestamp 77
* Prog\[0x00000004] has been accessed 222 times before the current clock cycle

In the following we describe the relevant trace columns associated with each component, their expected values at row 255 associated with the current clock cycle 256, and the associated constraints that they must satisfy.

### CPU Component Trace Columns and Constraints

In order to verify the correct execution of the `ADDI x10 x8 3` instruction at clock cycle 256, the CPU component will perform the following operations:

* Ensure a correct state transition;
* Fetch the instruction `ADDI x10 x8 3` from the program memory component;
* Decode the contents of the instruction and check the correctness of its format;
* Read contents of register x8 from the register memory component;
* Interact with the execution component to execute the instruction `ADDI x10 x8 3`; and
* Update the contents of register x10 based on the output of the execution component.

Let us now show how each of these operations is performed.

#### Ensuring a Correct State Transition

The CPU component ensures the state transition is performed correctly to guarantee correct ordering of instructions. It performs these checks:

{% stepper %}
{% step %}

### Verify program counter continuity

* Verify that the program counter in the present row matches the value of the next program counter from the preceding row (accounting for limb decomposition).
* Transition constraints (comparing two limbs at a time):
  * (1 - is\_first\[i]) \* (1 - is\_pad\[i]) \* (pc(1)\[i] + pc(2)\[i] \* 2^8 - pc\_next(1)\[i-1] - pc\_next(2)\[i-1] \* 2^8) = 0
  * (1 - is\_first\[i]) \* (1 - is\_pad\[i]) \* (pc(3)\[i] + pc(4)\[i] \* 2^8 - pc\_next(3)\[i-1] - pc\_next(4)\[i-1] \* 2^8) = 0

For our concrete state at row 255:

* i = 255
* pc(1)\[255] = 0x04, pc(2)\[255] = 0x00, pc(3)\[255] = 0x00, pc(4)\[255] = 0x00
* is\_pad\[255] = 0, is\_first\[255] = 0

Therefore pc\_next limbs on row 254 must equal 0x04, 0x00, 0x00, 0x00 respectively.
{% endstep %}

{% step %}

### Check clock update correctness

* Transition constraints for clk\[i] for row i > 0:
  * Use clk\_carry(1), clk\_carry(2) for carries.
  * Adding two limbs at a time:
    * clk(1)\[i] + clk(2)\[i] \* 2^8 + clk\_carry(1)\[i] \* 2^16 = clk(1)\[i-1] + clk(2)\[i-1] \* 2^8 + 1
    * clk(3)\[i] + clk(4)\[i] \* 2^8 + clk\_carry(2)\[i] \* 2^16 = clk(3)\[i-1] + clk(4)\[i-1] \* 2^8 + clk\_carry(1)\[i]
  * Enforce clk\_carry(j) in {0,1} via (clk\_carry(j))\*(1 - clk\_carry(j)) = 0
  * Range-check clk(j) ∈ \[0, 2^8 - 1] for each limb.

For our state, to increment clock from 255 → 256 it must hold that on row 254:

* clk(1)\[254] = 0xFF, clk(2)\[254] = 0x00, clk(3)\[254] = 0x00, clk(4)\[254] = 0x00
* clk\_carry(1)\[255] = 0, clk\_carry(2)\[255] = 0
  {% endstep %}

{% step %}

### Prevent padding rows from being followed by non-padding rows

* Enforce: (1 - is\_first\[i]) \* (1 - is\_pad\[i]) \* (is\_pad\[i-1]) = 0

With is\_pad\[255] = 0 and is\_first\[255] = 0, this implies is\_pad\[254] = 0.
{% endstep %}
{% endstepper %}

#### Fetching the Instruction

The CPU must read the instruction stored at the memory location pointed by pc and ensure pc is memory-aligned (multiple of 4).

Remark: Whenever constraints involve columns restricted to the same row, we omit explicit \[i] index for readability (values below apply to row 255 unless otherwise noted).

* The CPU interaction with program memory is captured by ReadProg interface with parameters (pc, clk) to obtain instr\_val. In the trace, instr\_val and pc are shared between CPU and program memory.

As a result at row 255:

* instr\_val(1) = Prog\[0x00000004] = 0b00010011
* instr\_val(2) = Prog\[0x00000005] = 0b00000101
* instr\_val(3) = Prog\[0x00000006] = 0b00110100
* instr\_val(4) = Prog\[0x00000007] = 0b00000000

Binary encoding breakdown for `ADDI x10 x8 3`:

* Bits 0–6: 0b0010011 (ADDI constant)
* Bits 7–11: 0b01010 → destination register x10 (op\_a)
* Bits 12–14: 0b000 (ADDI constant)
* Bits 15–19: 0b01000 → source register x8 (op\_b)
* Bits 20–31: 0b000000000011 → immediate 3 (op\_c)

Memory alignment constraint for pc:

* pc\_aux(1) \* 4 - pc(1) = 0
* pc\_aux(1) ∈ \[0, 2^6 - 1]

For this example, set pc\_aux(1) = 0x01 to show pc is multiple of 4.

#### Decoding the Instruction

The prover provides auxiliary values (advices) to help verify the binary encoding:

* op\_a = destination register (10)
* op\_b = source register (8)
* op\_c = immediate (3)
* op\_b\_flag = 1 (operand b used)
* imm\_c = 1 (operand c is immediate)
* is\_add = 1 (selector for ADD/ADDI)
* is\_alu\_imm\_no\_shift = 1
* is\_type\_i = 1
* is\_pad = 0, is\_first = 0, is\_last = 0

Operand decomposition advices (bits split across limbs):

* op\_a0 = 0 (bit 0 of op\_a)
* op\_a1\_4 = 5 (bits 1–4 of op\_a)
* op\_b0 = 0 (bit 0 of op\_b)
* op\_b1\_4 = 4 (bits 1–4 of op\_b)
* op\_c0\_3 = 3 (bits 0–3 of op\_c)
* op\_c4\_7 = 0 (bits 4–7 of op\_c)
* op\_c8\_10 = 0 (bits 8–10 of op\_c)
* op\_c11 = 0 (bit 11 of op\_c)

Convert the numbered set of constraints used to validate decoding into steps:

{% stepper %}
{% step %}

### 1) Exactly one instruction or padding flag is set

Enforce sum of instruction flags + is\_pad = 1. Since is\_add = 1, all other flags are 0.
{% endstep %}

{% step %}

### 2) op\_b\_flag correctness

Enforce op\_b\_flag = 1 for all instructions except {LUI, AUIPC, JAL, UNIMP}. This is satisfied by is\_add = 1 and op\_b\_flag = 1.
{% endstep %}

{% step %}

### 3) imm\_c correctness

Enforce imm\_c = 1 for all non-ALU instructions (constraint used to ensure correctness across instruction types). Given imm\_c = 1 in our example, constraints are satisfied.
{% endstep %}

{% step %}

### 4) Match instruction flag with opcode

For ADD/ADDI: (is\_add) \* (opcode - ADD) = 0. With is\_add = 1 and opcode set to ADD constant, satisfied.
{% endstep %}

{% step %}

### 5) ALU flags grouping

Define aggregated flags:

* is\_alu = sum of ALU instruction selectors
* is\_alu\_imm\_shift = imm\_c \* (is\_sll + is\_srl + is\_sra)
* is\_alu\_imm\_no\_shift = imm\_c \* (is\_add + is\_slt + is\_sltu + is\_xor + is\_or + is\_and)
* is\_type\_i\_no\_shift = is\_load + is\_alu\_imm\_no\_shift + is\_jalr
* is\_type\_i = is\_load + is\_alu\_imm\_no\_shift + is\_alu\_imm\_shift + is\_jalr

With is\_add = 1 and imm\_c = 1 we get:

* is\_alu = 1
* is\_alu\_imm\_shift = 0
* is\_alu\_imm\_no\_shift = 1
* is\_type\_i\_no\_shift = 1
* is\_type\_i = 1
  {% endstep %}

{% step %}

### 6) Operand decomposition consistency and range checks

* Ensure op\_a0 + op\_a1\_4 \* 2 - op\_a = 0 (when is\_type\_i\_no\_shift = 1)
* Range-check op\_a0 is binary, op\_a1\_4 ∈ \[0, 2^4 - 1]
* Ensure op\_b0 + op\_b1\_4 \* 2 - op\_b = 0
* Range-check op\_b parts
* Ensure op\_c0\_3 + op\_c4\_7 \* 2^4 + op\_c8\_10 \* 2^8 + op\_c11 \* 2^11 - op\_c = 0
* Range-check op\_c parts

With provided operand parts and is\_type\_i\_no\_shift = 1, these constraints hold for the example.
{% endstep %}

{% step %}

### 7) Sign-extension for operand c

Compute c\_val from op\_c using sign-extension constraints across limbs. Since op\_c11 = 0, higher limbs become 0. Prover sets:

* c\_val(1) = 0x03
* c\_val(2) = 0x00
* c\_val(3) = 0x00
* c\_val(4) = 0x00
  {% endstep %}

{% step %}

### 8) Instruction format checks across limbs

* Limb 1: (is\_alu\_imm\_no\_shift) \* (0b0010011 + op\_a0 \* 2^7 - instr\_val(1)) = 0
* Limb 2: (is\_add) \* (imm\_c) \* (op\_a1\_4 + 0b000 \* 2^4 + op\_b0 \* 2^7 - instr\_val(2)) = 0
* Limb 3: (is\_type\_i\_no\_shift) \* (op\_b1\_4 + op\_c0\_3 \* 2^4 - instr\_val(3)) = 0
* Limb 4: (is\_type\_i\_no\_shift) \* (op\_c4\_7 + op\_c8\_10 \* 2^4 + op\_c11 \* 2^7 - instr\_val(4)) = 0

With the previously set flags and operand parts, these constraints are satisfied for the given instr\_val limbs.
{% endstep %}
{% endstepper %}

#### Reading the Contents of Register x8

The interaction with register memory is captured by ReadReg interface with parameters (op\_b, clk, 1) where 1 indicates this is source register reg1. In the trace, fields are shared between CPU and register memory.

As a result of the interaction:

* reg1\_addr = op\_b
* b\_val limbs are set equal to reg1\_val\_cur limbs

Given the assumption R\[x8] = 0x000000FF before execution, the limbs are:

* b\_val(1) = reg1\_val\_cur(1) = 0xFF
* b\_val(2) = reg1\_val\_cur(2) = 0x00
* b\_val(3) = reg1\_val\_cur(3) = 0x00
* b\_val(4) = reg1\_val\_cur(4) = 0x00

#### Executing the Instruction

The CPU calls the execution component via exec(pc, opcode, a\_val, b\_val, c\_val) to obtain pc\_next. For ADD, execution updates a\_val.

After execution (ADDI x10 x8 3 → x10 := x8 + 3), the limbs are set as:

* a\_val(1) = 0x02
* a\_val(2) = 0x01
* a\_val(3) = 0x00
* a\_val(4) = 0x00

pc is incremented by 4, so:

* pc\_next(1) = 0x08
* pc\_next(2) = 0x00
* pc\_next(3) = 0x00
* pc\_next(4) = 0x00

(These a\_val limbs follow from b\_val = 0x000000FF and c\_val = 0x00000003.)

#### Updating the contents of register x10

To ensure x0 stays zero, CPU computes a\_val\_effective:

* a\_val\_effective = a\_val when op\_a ≠ 0, otherwise 0.
* Use auxiliary a\_val\_effective\_flag and supporting auxiliaries to enforce this (including multiplicative inverse aux variables).
* Enforce a\_val\_effective\_flag ∈ {0,1} and relation a\_val(limb) \* a\_val\_effective\_flag = a\_val\_effective(limb).

For op\_a = x10 (non-zero) the prover sets:

* a\_val\_effective\_flag = 1
* a\_val\_effective\_flag\_aux = 1 (non-zero aux)
* a\_val\_effective\_flag\_aux\_inv = appropriate inverse
* a\_val\_effective(limbs) = a\_val(limbs) = 0x02, 0x01, 0x00, 0x00 respectively

Then CPU interacts with register memory via WriteReg(op\_a, a\_val\_effective, clk, 3) to write to reg3 (destination). As a result reg3\_val\_cur limbs (for reg3\_addr = op\_a = x10) become:

* reg3\_val\_cur(1) = 0x02
* reg3\_val\_cur(2) = 0x01
* reg3\_val\_cur(3) = 0x00
* reg3\_val\_cur(4) = 0x00

### Execution Component Trace Columns and Constraints

To verify the ADD execution, the execution component enforces carry-handling constraints across limbs and that helper carries are binary.

Carry handling for ADD (per limb):

* (is\_add) \* (op\_a\_val(1) + h\_carry(1) \* 2^8 - op\_b\_val(1) - op\_c\_val(1)) = 0
* (is\_add) \* (op\_a\_val(2) + h\_carry(2) \* 2^8 - op\_b\_val(2) - op\_c\_val(2) - h\_carry(1)) = 0
* (is\_add) \* (op\_a\_val(3) + h\_carry(3) \* 2^8 - op\_b\_val(3) - op\_c\_val(3) - h\_carry(2)) = 0
* (is\_add) \* (op\_a\_val(4) + h\_carry(4) \* 2^8 - op\_b\_val(4) - op\_c\_val(4) - h\_carry(3)) = 0

And enforce (is\_add) \* h\_carry(j) \* (1 - h\_carry(j)) = 0 for each helper carry.

Given b\_val = 0x000000FF and c\_val = 0x00000003, to satisfy these constraints:

* a\_val limbs = 0x02, 0x01, 0x00, 0x00
* h\_carry(1) = 1, h\_carry(2) = 0, h\_carry(3) = 0, h\_carry(4) = 0

Next, execution determines whether pc is incremented by 4 (is\_pc\_inc\_std). It enforces:

* (is\_alu + is\_load + is\_type\_s + is\_type\_u + is\_type\_sys \* (1 - is\_sys\_halt) - is\_pc\_inc\_std) = 0

If is\_pc\_inc\_std = 1 then pc\_next must equal pc + 4, handled limb-wise with pc\_carry auxiliaries:

* (is\_pc\_inc\_std) \* (pc\_next(1) + pc\_next(2) \* 2^8 + pc\_carry(1) \* 2^16 - pc(1) - pc(2) \* 2^8 - 4) = 0
* (is\_pc\_inc\_std) \* (pc\_next(3) + pc\_next(4) \* 2^8 + pc\_carry(2) \* 2^16 - pc(3) - pc(4) \* 2^8 - pc\_carry(1)) = 0
* Enforce pc\_carry(j) binary via (is\_pc\_inc\_std) \* pc\_carry(j) \* (1 - pc\_carry(j)) = 0

For pc = 0x00000004, this yields pc\_next = 0x00000008 and pc\_carry(1) = pc\_carry(2) = 0.

### Program Memory Component Trace Columns and Constraints

The program memory component uses offline memory checking (simplified for read-only memory) with a counter per memory cell tracking read counts. Trace elements include:

* pc (word-aligned base address for instruction)
* instr\_val(1..4): instruction word bytes at pc, pc+1, pc+2, pc+3
* prog\_ctr\_prev (4 limbs): previous counter for base address pc
* prog\_ctr\_cur (4 limbs): current counter for base address pc
* prog\_read\_digest: digest of read set (logup)
* prog\_write\_digest: digest of write set (logup)

Actions per read:

* Check counter update correctness
* Verify read/write set digests updated correctly

#### Enforcing correct update of access counters

Enforce prog\_ctr\_cur = prog\_ctr\_prev + 1 using prog\_ctr\_carry auxiliaries across limbs. Carry bits must be binary.

Given Prog\[0x00000004] was accessed 222 times before current clock, set:

* prog\_ctr\_prev = 222 → limbs: prog\_ctr\_prev(1) = 2, prog\_ctr\_prev(2..4) = 0
* prog\_ctr\_cur = 223 → limbs: prog\_ctr\_cur(1) = 3, prog\_ctr\_cur(2..4) = 0
* prog\_ctr\_carry(1..4) = 0

#### Enforcing correct update of read- and write-set digests

Let fp(pc, instr\_val, prog\_ctr) be a fingerprint function (uses verifier-chosen β). Using random α chosen by verifier, enforce transition constraints for i > 0:

* prog\_read\_digest\[i] - prog\_read\_digest\[i-1] = 1 / (fp(pc\[i], instr\_val\[i], prog\_ctr\_prev\[i]) + α)
* prog\_write\_digest\[i] - prog\_write\_digest\[i-1] = 1 / (fp(pc\[i], instr\_val\[i], prog\_ctr\_cur\[i]) + α)

For row 255 with known pc and instr\_val limbs, these constraints must hold with the corresponding prog\_ctr\_prev and prog\_ctr\_cur.

Remark: instr\_val, prog\_ctr\_prev and prog\_ctr\_cur limbs also have range checks in the formal spec; the values above satisfy those ranges.

### Register Memory Component Trace Columns and Constraints

The register memory component uses offline memory checking for read/write memory and associates a timestamp per cell. It also uses logups for read/write set digest consistency. Each access maintains tuples of (reg\_addr, reg\_val\_prev, reg\_val\_cur, reg\_ts\_prev, reg\_ts\_cur). Up to three register addresses can be accessed in one execution cycle; the trace contains three such sets.

Trace elements include:

* clk
* reg1\_addr, reg2\_addr, reg3\_addr
* reg1\_val\_cur, reg2\_val\_cur, reg3\_val\_cur (32-bit values)
* reg1\_ts\_cur, reg2\_ts\_cur, reg3\_ts\_cur (current timestamps)
* reg1\_val\_prev, reg2\_val\_prev, reg3\_val\_prev
* reg1\_ts\_prev, reg2\_ts\_prev, reg3\_ts\_prev
* reg\_read\_digest, reg\_write\_digest
* reg1\_accessed, reg2\_accessed, reg3\_accessed flags (indicate whether each set is used)

Register memory enforces:

1. Current timestamps for reg1/2/3 satisfy:
   * reg1\_ts\_cur = 3 \* clk - 2
   * reg2\_ts\_cur = 3 \* clk - 1
   * reg3\_ts\_cur = 3 \* clk
2. Previous timestamps precede current timestamps:
   * regj\_ts\_prev ∈ {0, …, regj\_ts\_cur - 1}
3. Read/write digest updates via logup contributions (described below).

Remark: reg1\_addr, reg2\_addr, reg3\_addr should be accessed in order and only reg3\_addr can be modified during a clock cycle.

#### Enforcing the Correct Update of Read- and Write-Set Digests (Registers)

Let fp(reg\_addr, reg\_val, reg\_ts) be a fingerprint function (uses verifier-chosen β). For row index i > 0 and random α:

* reg\_read\_digest\[i] - reg\_read\_digest\[i-1] = reg1\_accessed\[i] / (fp(reg1\_addr\[i], reg1\_val\[i], reg1\_ts\_prev\[i]) + α)
  * reg2\_accessed\[i] / (fp(reg2\_addr\[i], reg2\_val\[i], reg2\_ts\_prev\[i]) + α)
  * reg3\_accessed\[i] / (fp(reg3\_addr\[i], reg3\_val\[i], reg3\_ts\_prev\[i]) + α)
* reg\_write\_digest\[i] - reg\_write\_digest\[i-1] = reg1\_accessed\[i] / (fp(reg1\_addr\[i], reg1\_val\[i], reg1\_ts\_cur\[i]) + α)
  * reg2\_accessed\[i] / (fp(reg2\_addr\[i], reg2\_val\[i], reg3\_ts\_cur\[i]) + α)
  * reg3\_accessed\[i] / (fp(reg3\_addr\[i], reg3\_val\[i], reg3\_ts\_cur\[i]) + α)

For this example, the assumptions and derived values for row 255 are:

* R\[x8] = 0x000000FF with last timestamp 323
* R\[x10] = 0x00000005 with last timestamp 77
* clk\[255] = 256
* reg1\_ts\_cur\[255] = 3 \* 256 - 2 = 766
* reg3\_ts\_cur\[255] = 3 \* 256 = 768
* reg1\_accessed\[255] = 1, reg2\_accessed\[255] = 0, reg3\_accessed\[255] = 1
* R\[x10] updated to 0x00000102 at current clock

To satisfy logup constraints at i = 255, the following must be set consistently (limb decompositions shown):

* reg1\_ts\_prev\[255] limbs: (1) = 32, (2..4) = 0
* reg1\_val\_prev\[255] = reg1\_val\_cur\[255] = 0xFF, 0x00, 0x00, 0x00
* reg1\_ts\_cur\[255] limbs: (1) = 254, (2) = 2, (3..4) = 0 (representation of 766)
* reg3\_ts\_prev\[255] limbs: (1) = 7, (2..4) = 0
* reg3\_val\_prev\[255] limbs: 0x05, 0x00, 0x00, 0x00
* reg3\_ts\_cur\[255] limbs: (1) = 0, (2) = 3, (3..4) = 0 (representation of 768)
* reg3\_val\_cur\[255] limbs: 0x02, 0x01, 0x00, 0x00

With these values, the register read/write digest transition constraints hold for the example.

***

References (kept intact):

* Proving Memory: <https://docs.nexus.xyz/zkvm/specifications/memory-checking>
* Proving Instructions: <https://docs.nexus.xyz/zkvm/specifications/instructions>
* Licensing: <https://docs.nexus.xyz/zkvm/license>

(End of cleaned/import-optimized page content.)
