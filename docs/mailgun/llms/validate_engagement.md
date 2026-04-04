# Source: https://documentation.mailgun.com/docs/validate/validate_engagement.md

# Engagement Validation

## What is Engagement Validation?

Validateâs engagement results are a macro-level view that explain an email recipientâs propensity to engage. For contract customers, when an email list is validated, we assign a behavior type to each email recipient based on the email recipientâs engagement activity over the last 30-days. These results are included with every bulk validations and single validations job. For self-serve customers, we provide a modified version of engagement results.

## Engagement Results for Contract Customers

Contract customers will see the following engagement behavior types assigned to each email recipient. For customers using the UI, in addition to the results that are included in the .csv file, a third chart will display the breakdown of engagement behavior types.

### For engaging behavior types

| Behavior Type | Description |
|  --- | --- |
| Bot | An unreasonably high number of clicks in a 30-day period. |
| Complainer | Recipient has complained, reported to spam, in a 30-day period. |
| High Engager | Recipient has clicked on or opened several emails in a 30-day period (excludes automatic opens). |
| Engager | Recipient has clicked on or opened emails but not enough to identify the recipient as a High Engager. |


### For non-engaging behavior types

| Behavior Type | Description |
|  --- | --- |
| Disengaged | Recipient only has delivered emails. |
| No data | No data because the email was validated via 'provider lookup' in the last 30 days. |


## Engagement Results for Self-Service Customers

Self-serve customers will receive Boolean results for engagement and whether the email recipient is a bot. The results are available in the downloadable `.csv` or `json` file.

| Type | Settings |
|  --- | --- |
| Engaging | true or false |
| Bot | true or false |


Note:
We ignore automatic opens and clicks when calculating the validate emailâs behavior type.

## What is the value of Validateâs engagement results?

Validateâs engagement results can help segment your email list more effectively. Not only do we provide information on whether a validated email address exists and is deliverable, we provide additional information as to whether the email recipient has engaged with their emails in the last 30-days. Senders can now segment their lists based on engagement behavior and adjust the content and tone of their email campaigns according to the behavior type for best results. This will help the sender maximize their opens, clicks, conversions, and ultimately their reputation as a sender.