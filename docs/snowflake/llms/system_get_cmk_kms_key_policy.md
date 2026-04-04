# Source: https://docs.snowflake.com/en/sql-reference/functions/system_get_cmk_kms_key_policy.md

Categories:
:   [System functions](../functions-system.md) (System Information)

# SYSTEM$GET_CMK_KMS_KEY_POLICY

Returns an ARRAY containing a snippet of the AWS Key Management Service policy information related to customer-managed keys.

You can use this policy information for your customer-managed keys with [Tri-Secret Secure](../../user-guide/security-encryption-tss.md) for Snowflake accounts on Amazon Web
Services.

See also:
:   [Tri-Secret Secure in Snowflake](../../user-guide/security-encryption-tss.md)

## Syntax

> ```sqlsyntax
> SYSTEM$GET_CMK_KMS_KEY_POLICY()
> ```

## Arguments

None.

## Usage notes

* This function is for use in Snowflake accounts on Amazon Web Services only.
* Only account administrators (i.e. users with the ACCOUNTADMIN role) or a role that is granted the MONITOR SECURITY privilege can call
  this function.

## Examples

Return a snippet of the AWS KMS policy for use with customer-managed keys:

> ```sqlexample
> SELECT SYSTEM$GET_CMK_KMS_KEY_POLICY();
> ```
