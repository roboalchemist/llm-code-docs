# Source: https://docs.snowflake.com/en/sql-reference/expressions-byte-bit.md

# Bitwise expression functions

This family of functions can be used to perform bitwise operations on numbers or a group of numeric records.

| Function Name | Syntax | Summary Description |
| --- | --- | --- |
| [BITAND](functions/bitand.md) | `BITAND(a, b)` | Bitwise AND of two numeric or binary expressions (`a` and `b`). |
| [BITAND_AGG](functions/bitand_agg.md) | `BITAND_AGG(a)` | Bitwise AND value of all non-NULL numeric records in a group `a`. |
| [BITNOT](functions/bitnot.md) | `BITNOT(a)` | Bitwise negation of `a` numeric or binary expression. |
| [BITOR](functions/bitor.md) | `BITOR(a, b)` | Bitwise OR of two numeric or binary expressions (`a` and `b`). |
| [BITOR_AGG](functions/bitor_agg.md) | `BITOR_AGG(a)` | Bitwise OR value of all non-NULL numeric records in a group `a`. |
| [BITSHIFTLEFT](functions/bitshiftleft.md) | `BITSHIFTLEFT(a, n)` | Shift the bits for `a` numeric or binary expression `n` positions to the left. |
| [BITSHIFTRIGHT](functions/bitshiftright.md) | `BITSHIFTRIGHT(a, n)` | Shift the bits for `a` numeric or binary expression `n` positions to the right, with sign extension. |
| [BITXOR](functions/bitxor.md) | `BITXOR(a, b)` | Bitwise XOR of two numeric or binary expressions (`a` and `b`). |
| [BITXOR_AGG](functions/bitxor_agg.md) | `BITXOR_AGG(a)` | Bitwise XOR value of all non-NULL numeric records in a group `a`. |
| [GETBIT](functions/getbit.md) | `GETBIT(a, n)` | Return the bit at position `n` in `a` numeric expression. |
