# Source: https://gitbook.com/docs/help-center/account-management/managing-your-account/sign-up-and-login-issues.md

# Sign up and login issues

## Why has my account been disabled by administrator?

Our platform employs an automatic system designed to block accounts exhibiting suspicious behaviour. This measure is crucial for preventing spammers and scam accounts from compromising the integrity of our service.

We acknowledge that this system might occasionally block legitimate accounts in its effort to maintain security. If you believe your account has been unfairly blocked, please contact our support team.

Our support team is available to assess unblocking requests on a case-by-case basis.

***

## The link to join the organization isn't working

#### Error: auth/invalid-email

This error message typically comes up when the email address invited to join a GitBook organization does not match the email address of the logged-in GitBook user attempting to accept the invitation.

{% code fullWidth="false" %}

```
Error: auth/invalid-email
Firebase: The email provided does not match the sign-in email address. (auth/invalid-email).
```

{% endcode %}

Please contact the person who invited you and ask them which email address they used to invite you. If needed, they can invite a different email address instead.

***

## Error: auth/expired-action-code

This error typically occurs when a link, such as a sign-in or invitation link, has passed its validity period. For security reasons, these links have a limited lifespan.

{% code overflow="wrap" fullWidth="false" %}

```
Error: auth/expired-action-code
Firebase: The action code has expired. (auth/expired-action-code).
```

{% endcode %}

If you created the link yourself (like a sign-in link), please initiate the process again to generate a new link. If you received the link from someone else, kindly request that they send you a fresh one.&#x20;

***

## Error: auth/email-already-in-use

This error usually occurs when the GitHub account that you use to set up the sync is already associated with a different GitBook user account.

{% code overflow="wrap" fullWidth="false" %}

```
Error: auth/email-already-in-use
Firebase: The email address is already in use by another account. (auth/email-already-in-use).
```

{% endcode %}

#### How to identify which GitBook account is linked to the GitHub account:

1. Log out from your current GitBook user session (i.e. **<name@email.com>**)
2. Log out from any GitHub user sessions.
3. Go to [the login page](https://app.gitbook.com/login).
4. Select the "Sign in with GitHub" option.
5. Enter your GitHub credentials.
6. Once logged in, go to [the account settings](https://app.gitbook.com/account) and either:
   1. Unlink the account from the "Third-party Login > GitHub" section in the Personal setting
   2. Delete the account altogether if you do not need it.
7. Log out from the session.
8. Log back in using your **<name@email.com>** GitBook account.
9. Try to set up Git Sync again.

***
