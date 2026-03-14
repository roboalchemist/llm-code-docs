# Source: https://docs.snowflake.com/en/sql-reference/functions/system_get_cmk_info.md

Categories:
:   [System functions](../functions-system.md) (System Information)

# SYSTEM$GET_CMK_INFO

Returns the status of your customer-managed key (CMK) for use with Tri-Secret Secure.

See also:
:   [Understanding CMK self-registration with support activation of Tri-Secret Secure](../../user-guide/security-encryption-tss.md)

## Syntax

```sqlsyntax
SYSTEM$GET_CMK_INFO( [ '<ssa_account_name>' ] )
```

## Arguments

**Required:**

None.

**Optional:**

`ssa_account_name`
:   A string that specifies the name of SSA account name for which you want to retrieve the CMK status.

## Returns

Returns a status message indicating the state of your CMK. The output includes the values that you specified when calling
[SYSTEM$REGISTER_CMK_INFO](system_register_cmk_info.md). If you have enabled private connectivity, the status message returned by SYSTEM$GET_CMK_INFO includes
whether your CMK is privately connected.

The following messages are possible, using CMKs on Amazon Web Services as a representative example:

* Your CMK is registered, but not yet enabled, to use Tri-Secret Secure:

  ```output
  CMK with ARN: arn:aws:kms:us-west-2:736112632310:key/ceab36e4-f0e5-4b46-9a78-86e8f17a0f59
  is pre-registered for Tri-Secret Secure.
  ```

* Your CMK is activated and in use with Tri-Secret Secure:

  ```output
  CMK with ARN: arn:aws:kms:us-west-2:736112632310:key/ceab36e4-f0e5-4b46-9a78-86e8f17a0f59
  is activated for Tri-Secret Secure.
  ```

* You have an active CMK, but you just pre-registered a new key:

  ```output
  CMK with ARN: arn:aws:kms:us-west-2:736112632310:key/ceab36e4-f0e5-4b46-9a78-86e8f17a0f59
  is activated with Tri-Secret Secure, but
  CMK with ARN: arn:aws:kms:us-west-2:481048248138:key/e08cb6c0-7c09-4f37-8e55-e395a12fe965
  is pre-registered for Tri-Secret Secure.
  ```

* You have an active key, but have not registered any CMK to use Tri-Secret Secure:

  ```output
  CMK info has not been pre-registered in this account yet, but
  CMK arn:aws:kms:us-west-2:736112632310:key/ceab36e4-f0e5-4b46-9a78-86e8f17a0f59
  is activated with Tri-Secret Secure.
  ```

* You have not registered any CMK to use Tri-Secret Secure:

  ```output
  CMK info has not been pre-registered in this account yet.
  ```

* Your active CMK is registered with private connectivity *enabled*.

  ```output
  CMK with ARN: arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab
  with PrivateLink enabled is activated for Tri-Secret Secure.
  ```

* Your active CMK is registered with private connectivity *not enabled*.

  ```output
  CMK with ARN: arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab
  is activated for Tri-Secret Secure.
  ```

## Access control requirements

* Only users with the ACCOUNTADMIN role or with a role that is granted the MONITOR SECURITY privilege can call this
  function.
* Only users with the GLOBALORGADMIN role or ORGADMIN role can specify an SSA account name.

## Examples

Obtain the status of the CMK for your Snowflake account:

> ```sqlexample
> SELECT SYSTEM$GET_CMK_INFO();
> ```

Obtain the status of the CMK for a specific SSA account:

> ```sqlexample
> SELECT SYSTEM$GET_CMK_INFO('AUTO_FULFILLMENT_AREA$PUBLIC_AZURE_EASTUS2');
> ```
