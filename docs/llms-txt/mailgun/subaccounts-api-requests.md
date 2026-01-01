# Source: https://documentation.mailgun.com/docs/mailgun/user-manual/subaccounts/subaccounts-api-requests.md

# Performing API requests "on behalf of" Subaccounts

Primary accounts can make API calls on behalf of their subaccounts, e.g. sending messages, managing mailing lists, etc. This is accomplished by using the `X-Mailgun-On-Behalf-Of` header, which must contain the **subaccountâs account ID**.

Info
Moreover, this header is a **request** header, not a **message** header. As such, this is not the `h:header_value` construct used for adding Reply-To fields, for instance. How to add request headers differs with each language; nonetheless, the below example shows how to add a request header in cURL.

**Important Note**:
If the `X-Mailgun-On-Behalf-Of` header is NOT included, the action could occur on the primary account rather than the subaccount.

## Request Header


```
X-Mailgun-On-Behalf-Of: SUBACCOUNT_ACCOUNT_ID
```

Where `SUBACCOUNT_ACCOUNT_ID` is a value like `646d00a1b32c35364a2ad34f`. The headerâs data type is a string, and each programming language likely will have the entire header (i.e. the header name and value) enclosed in single- or double-quotes (as shown in the below example).

## Example cURL


```
curl -s --user 'api:PRIMARY_ACCOUNT_API_KEY' \
    https://api.mailgun.net/v3/SUBACCOUNT_DOMAIN/messages \
    -H "X-Mailgun-On-Behalf-Of: SUBACCOUNT_ACCOUNT_ID" \
    -F from='Excited User <YOU@SUBACCOUNT_DOMAIN>' \
    -F to='foo@example.com' \
    -F subject='Hello' \
    --form-string html='<html>HTML version of the body</html>'
```

As you'll notice in the above example, the API key used is that of the primary account whereas the domain and account ID used is that of the subaccount.