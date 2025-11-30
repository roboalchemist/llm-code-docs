# Source: https://developer.1password.com/docs/cli/best-practices

On this page

# 1Password CLI best practices

1Password CLI brings 1Password to your terminal. The following are best practices we recommend when using 1Password CLI.

### Use the latest version of 1Password CLI[â€‹](#use-the-latest-version-of-1password-cli "Direct link to Use the latest version of 1Password CLI") 

Practice good software update hygiene and regularly update to the [latest version of the 1Password CLI](https://app-updates.agilebits.com/product_history/CLI2).

You can check for available updates with [`op update`](/docs/cli/reference/commands/update).

### Apply the principle of least privilege to your infrastructure secrets[â€‹](#apply-the-principle-of-least-privilege-to-your-infrastructure-secrets "Direct link to Apply the principle of least privilege to your infrastructure secrets") 

You can follow the [principle of least privilege ](https://csrc.nist.gov/glossary/term/least_privilege) with [1Password Service Accounts](/docs/service-accounts), which support restricting 1Password CLI access to only the items required for a given purpose.

Use dedicated vaults with service accounts that are properly scoped for secrets management use cases. Do not grant access to more vaults than needed.

Learn more about [managing group and vault permissions using the principle of least privilege](https://support.1password.com/business-security-practices#access-management-and-the-principle-of-least-privilege).

### Use template files when creating items that contain sensitive values[â€‹](#use-template-files-when-creating-items-that-contain-sensitive-values "Direct link to Use template files when creating items that contain sensitive values") 

When creating items with [`op item create`](/docs/cli/reference/management-commands/item#item-create) we recommend using a [JSON template](/docs/cli/item-create#with-an-item-json-template) to enter any sensitive values.