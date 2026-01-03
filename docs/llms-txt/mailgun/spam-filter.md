# Source: https://documentation.mailgun.com/docs/mailgun/user-manual/receive-forward-store/spam-filter.md

# Spam Filter

A spam filter is necessary when receiving email. Mailgun is powered by an army of SpamAssassin machines. Mailgun gives you three ways to configure spam filtering.

Click the Domains tab on the Control Panel and select from one of the following three options:

- Disabled (default)
- Delete Spam (spam is removed and you won't see it)
- Mark spam with MIME headers (You decide what to do with it)


If you choose to mark spam with MIME headers, Mailgun provides you with these four:

- **X-Mailgun-Sflag** - Inserted with the value `Yes` if the message was classified as spam.
- **X-Mailgun-Sscore**  **-** A 'spamicity' score that you can use to calibrate your own filter. Inserted for every message checked for spam. The score ranges from low negative digits (very unlikely to be spam) to 20 and occasionally higher (very likely to be spam).
- **X-Mailgun-Dkim-Check-Result** - If DKIM is used to sign an inbound message, Mailgun will attempt DKIM validation, the results will be stored in this header. Possible values are: `Pass` or `Fail`
- **X-Mailgun-Spf -Mailgun** will perform an SPF validation, and results will be stored in this header. Possible values are: `Pass`, `Neutral`, `Fail` or `SoftFail`.