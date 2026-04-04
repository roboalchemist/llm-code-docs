# Source: https://firebase.google.com/docs/auth/limits.md.txt

The following auth operations have limitations on the frequency you can perform
them. Contact
Firebase
a few weeks in advance
to discuss special use cases.

> [!NOTE]
> **Note:** Limitations apply per customer and can change without notice. Abuse protections may be enabled without warning on accounts that demonstrate suspicious traffic patterns.

## Daily Instrumentless Usage Limits

The following limits are daily usage limits for users of
Firebase Authentication with Identity Platform on the no-cost Spark plan.

These usage limits correspond directly to
[Google Cloud Pricing Tiers](https://cloud.google.com/identity-platform/pricing).

| Usage | Instrumentless Limit |
|---|---|
| Tier 1 Daily Active Users | 3000 per day |
| Tier 2 Daily Active Users | 2 per day |

## Account creation and deletion limits

| Operation | Limit |
|---|---|
| New account creation | 100 accounts/hour for each IP address |
| Account deletion | 10 accounts/second |
| Batch account deletion | 1 request/second |
| Account configuration updates | 10 requests/second |

> [!NOTE]
> **Note:** You can schedule a temporary increase to the account creation limit in the Firebase console

## Account limits

| Account type | Limit |
|---|---|
| Anonymous user accounts | 100 million |
| Registered user accounts | Unlimited |

## Email sending limits

The quotas listed in this section scale with the number of users.

| Operation | Spark plan limit | Blaze plan limit |
|---|---|---|
| Address verification emails | 1000 emails/day | 100,000 emails/day |
| Address change emails | 1000 emails/day | 10,000 emails/day |
| Password reset emails | 150 emails/day | 10,000 emails/day |
| Email link sign-in emails | 5 emails/day | 25,000 emails/day |

> [!NOTE]
> **Note:** The limits for email link sign-in emails were recently changed. Please add a billing instrument to go beyond 5 email link sign-in emails.

## Email link generation limits

The quotas listed in this section scale with the number of users.

| Operation | Spark plan limit | Blaze plan limit |
|---|---|---|
| Address verification links | 10,000 links/day | 1,000,000 links/day |
| Password reset links | 1500 links/day | 100,000 links/day |
| Sign-in links | 20,000 links/day | 250,000 links/day |

## Phone number sign-in limits

| Operation | Limit |
|---|---|
| User sign-ins | 1600/minute, as well as the pricing and limits specified on the [Pricing](https://firebase.google.com/pricing) page |
| Verification code SMS messages | Pay as you go (Blaze) plan only. - Firebase Authentication: 3000 sent SMS/day limit - Firebase Authentication with Identity Platform: No limit |
| Verification requests | 150 requests/IP address/hour |

## Verification SMS sending limits

| Operation | Limit |
|---|---|
| Verification SMS sent. | 1,000 sent/minute |
| Verification SMS sent per IP address | 50 sent/minute, 500 sent/hour |

Additionally, there is a limit on the number of verification SMS messages a project
can send to a single phone number within a set amount of time. You can test with [fictional numbers](https://firebase.google.com/docs/auth/android/phone-auth#test-with-fictional-phone-numbers) or
across multiple devices to ensure a project does not exceed these limits.

Additionally, you can track verification codes sent per phone number if you've enabled
[Activity Logging](https://cloud.google.com/identity-platform/docs/activity-logging) on your project.

## Identity Toolkit API limits

| Operation | Limit |
|---|---|
| Operations per service account | 500 requests/second |
| Operations per project | 1000 requests/second, 10 million requests/day |
| Account uploads per project\* | 3.6M accounts/minute |
| Account downloads per project\* | 21,000 requests/minute |
| UserInfo queries per project\* | 900 requests/minute |
| Configuration updates per project\* | 300 requests/minute |
| Configuration updates per project and user\* | 300 requests/minute |
| Bulk delete accounts per project\* | 3000 requests/minute |
| Custom token sign-ins per project | 45,000 sign-ins/minute |
| `createAuthURI` calls per IP address | 120 requests/hour |
| Blocking function invocations per project | 2000 requests/minute |
| `GetAccountInfo` per project\* | 500,000 requests/minute |

\* Admin-only operations.

The `fetchProvidersForEmail()` and [`fetchSignInMethodsForEmail(email)`](https://firebase.google.com/docs/reference/js/auth.md#fetchsigninmethodsforemail) methods leverage the `createAuthURI` endpoint.

## Token Service API limits

| Operation | Limit |
|---|---|
| Token exchange per project | 18,000 exchanges/minute |