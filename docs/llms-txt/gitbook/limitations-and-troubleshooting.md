# Source: https://gitbook.com/docs/help-center/published-documentation/adaptive-content/limitations-and-troubleshooting.md

# Limitations and troubleshooting

## **If a section, page, or block is restricted with Adaptive Content, will it still appear in search results?**

Search results only reflect the content that a user has access to. Any section, page, or block behind Adaptive Content will only be indexed and visible in search for users who meet the conditions to view it.

***

## **Do JWT claim schemas support free-form strings?**

Not yet. JWT claim schemas currently only support enums for string values. Free-form strings aren’t supported, so the only option is to define all required string values within an enum.

***

## **Can Adaptive Content work with arrays in JWT claims?**

No, arrays aren’t supported. A claim can only provide a single value, and it must be either a string (enum) or a boolean. If multiple values are needed, they must be transformed on the claims provider side (e.g., Azure, Okta).

***

## **How do I test and debug Adaptive Content conditions?**

Try these checks:

* Case sensitivity: Property names are case-sensitive (e.g., `role` ≠ `Role`).
* Data types: Boolean vs string mismatches (true vs "true")
* Nesting: Incorrect property path in conditions
* You can check the claims attached to a token on <https://www.jwt.io/>. You should see your expected claims being passed with the token.
