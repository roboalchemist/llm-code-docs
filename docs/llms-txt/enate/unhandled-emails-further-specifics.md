# Source: https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/emails/unprocessed-emails/unhandled-emails-further-specifics.md

# Unhandled Emails Further Specifics

### When do emails appear in the Unhandled Emails view?

Emails will appear in the Unhandled Emails view of your 'Email Inbox' view in Work Manager if they meet one of the following conditions:

1. None of the To and/or CC email addresses have a matching email route.
2. There are only BCC email addresses in an email, no To or CC addresses.

See the table below for further detailed information on how emails arriving into Enate are treated, depending on the combinations of Enate-relevant email addresses may appear in the TO, CC or BCC fields.

| **Scenario**                                                                                                 | **Number of work Items Created**   | **Will they appear in the Unhandled View**                                   |
| ------------------------------------------------------------------------------------------------------------ | ---------------------------------- | ---------------------------------------------------------------------------- |
| Email to just one email address in either the TO or CC field                                                 | 1                                  | <mark style="color:orange;">No</mark>                                        |
| Email to 2 or more email addresses in either TO or CC field                                                  | 2 or more                          | <mark style="color:orange;">No</mark>                                        |
| Email to 1 email address in TO, another in CC field, and one in BCC field                                    | 1 for each TO & CC address         | <mark style="color:orange;">No</mark>                                        |
| \*Email to 1 email address in TO and another in BCC field                                                    | 1 for TO field                     | <mark style="color:orange;">No</mark>                                        |
| Email to 1 or more email addresses in BCC only. Nothing in TO or CC fields.                                  | 0                                  | <mark style="color:green;">Yes - for the BCC email mailbox</mark>            |
| Email to just 1 email address that is not correctly configured in Enate                                      | 0                                  | <mark style="color:green;">Yes - for the non-configured email address</mark> |
| Email to 1 email address that is not configured correctly in Enate and one email address configured in Enate | 1 for the configured email address | <mark style="color:orange;">No</mark>                                        |
