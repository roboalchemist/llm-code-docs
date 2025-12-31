# Source: https://docs.asapp.com/security/data-redaction.md

# Data Redaction

> Learn how Data Redaction removes sensitive data from your conversations.

Live conversations are completely uninhibited and as such, customers may mistakenly communicate sensitive information (e.g. credit card number, SSN, etc.) in a manner that increases risk.

In order to mitigate this risk, ASAPP performs redaction logic that can be customized for your business's needs. You also have the ability to add your own [custom redaction rules](#custom-regex-redaction-rules) using regular expressions.

Reach out to your ASAPP account team to learn more.

## Custom Regex Redaction Rules

In AI-Console, you can view existing custom, regex based redaction rules and add new ones for your organization.

Adding rules match specific patterns by using regular expressions. These new rules can be deployed to testing environments and to production.

Custom redaction rules live in the Core Resources section of AI-Console.

* Custom redaction rules are displayed as an ordered list of rules with names.
* Each individual rule will display the underlying regex.

To add a custom rule:

1. Click **Add new**
2. Create a unique Regex Name
3. Add the regex for the particular rule
4. Test your regex rule to ensure it works as expected
5. Add the regex to sandbox

Once a rule has been added to the sandbox environment, test it in your lower environment to ensure it's behaving as expected.
