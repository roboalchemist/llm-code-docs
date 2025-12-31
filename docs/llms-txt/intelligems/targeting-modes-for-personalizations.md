# Source: https://docs.intelligems.io/personalizations/targeting-personalizations/targeting-modes-for-personalizations.md

# Targeting Modes for Experiences

Intelligems offers two broad modes of Audience Targeting: **Permanent** and **Temporary.**

* [**Permanent**](#permanent-audience) **-** is useful if once someone is eligible for an Experience, and as long as that personalization is active you want them to continue to receive that experience.
* [**Temporary**](#temporary-audience) - is useful if the conditions by which someone qualifies may "expire". For example, if you target New Visitors, a new visitor will see a Experience but eventually no longer qualify. Similarly, if someone who comes via a specific link qualifies, after a certain amount of time they may no longer qualify.

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-aea4c9c323c11010686368771d10f5efbbd4e9e2%2FScreenshot%202024-10-03%20at%2012.29.37%E2%80%AFPM.png?alt=media" alt=""><figcaption></figcaption></figure>

## **Permanent Audience**

A **Permanent Audience** is a group of users that are permanently included or excluded from an Experience. Once a user is evaluated and placed in or excluded from a permanent audience, their status remains unchanged for the duration of the experiment.

#### Characteristics:

* **Static Assignment**: Once assigned, users in a permanent audience will not be re-evaluated for inclusion or exclusion based on behavior or conditions.
* **No Expiration**: Users who are included or excluded from a permanent audience are never automatically re-evaluated after a certain time period.

### Temporary Audience

A **Temporary Audience** is a group of users who are dynamically included or excluded from an Experience based on an evaluation frequency. Users in a temporary audience are re-evaluated periodically to determine if they should remain included in the experiment or be excluded.

#### Characteristics:

* **Dynamic Assignment**: Users are periodically evaluated to see if they should remain in the audience. This re-evaluation happens after a set period (called the **evaluation frequency**).
* **Evaluation Frequency**: This is the number of days between re-evaluations. During each re-evaluation, the user can be included or excluded based on the defined conditions.
