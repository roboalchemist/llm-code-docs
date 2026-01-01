# Source: https://documentation.mailgun.com/docs/mailgun/user-manual/reporting/rate-definitions.md

# Rate Definitions

html
table
tr
th
Rate Label
th
API Variable Name
th
Calculation
th
Definition (Used in tooltip)
tr
td
Bounced
td
bounce_rate
td
bounced_count / processed_count
td
Bounce rate measures the percentage of emails that bounce back, or the number of emails that couldnât be delivered to users over the total number of emails sent.
tr
td
Clicked
td
clicked_rate
td
clicked_count / delivered_count
td
The rate at which delivered emails are clicked. This calculation uses total clicks, not unique clicks. Use the unique click rate if percentages exceed 100%.
tr
td
Complained
td
complained_rate
td
complained_count / delivered_count
td
Complaint rate measures the percentages of delivered emails reported as spam by recipients. This rate should be kept below 0.1%. Please note that Gmail does not provide complaints, to see Gmail complaint data, sign up for Google Postmaster Tools.
tr
td
Delayed
td
delayed_rate
td
delivered_two_plus_attempts_count / delivered_count
td
The percentage of emails that were delivered with two or more delivery attempts. This rate does not include delayed emails that could not be delivered.
tr
td
Delivered
td
delivered_rate
td
delivered_count / sent_count
td
The rate at which sent emails are delivered to recipient addresses. This calculation does not include suppressed emails.
tr
td
Failed
td
permanent_fail_rate
td
permanent_failed_count / processed_count
td
The percentage of sent emails that resulted in a permanent failure. These emails could not be delivered and will not be retried.
tr
td
Opened
td
opened_rate
td
opened_count / delivered_count
td
The rate at which delivered emails are opened. This calculation uses total opens, not unique opens. Use the unique open rate if percentages exceed 100%.
tr
td
Unique clicked
td
unique_clicked_rate
td
unique_clicked_count / delivered_count
td
The percentage of delivered emails that resulted in a unique click event. This calculation will exceed 100% if your date filter excludes a large amount of delivery events.
tr
td
Unique opened
td
unique_opened_rate
td
unique_opened_count / delivered_count
td
The percentage of delivered emails that resulted in a unique open event. This calculation will exceed 100% if your date filter excludes a large amount of delivery events.
tr
td
Unsubscribed
td
unsubscribed_rate
td
unsubscribed_count / delivered_count
td
The unsubscribe rate accounts for the total number of unsubscribes divided by the total number of emails delivered and multiplied by 100, expressed as a percentage.