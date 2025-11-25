# Source: https://docs.upsun.com/development/sanitize-db.md

# Sanitize databases

When working on a new feature on your website, you want to use a new branch.
Using a new branch makes sure that you don't risk breaking your live, production website.

Creating a branch on Upsun copies both the code and the database to that new development branch.
These code and database changes need to be tested before being merged into production.
Depending on your processes, internal or external teams may interact with the preview environment branch.

Databases of live websites often contain personally identifiable information (PII)
such as full names, mailing addresses, and phone numbers.
To ensure people reviewing code changes can't access information they shouldn't,
sanitize your databases of any PII that they may contain.

## Examples

