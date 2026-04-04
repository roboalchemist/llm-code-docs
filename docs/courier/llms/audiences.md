# Source: https://www.courier.com/docs/platform/users/audiences.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Lists & Audiences

> Manage user groups with static lists and dynamic audiences. Target users through manual curation or automated segmentation based on profile attributes and rules.

## Overview

Courier provides two approaches for targeting groups of users: static lists for manual curation and dynamic audiences for automated segmentation. Understanding when to use each method helps you build effective targeting strategies for your notifications.

## Key Features

Courier's group targeting provides flexible options for reaching the right users:

* **Static Lists** - Manually curated collections with complete membership control
* **Dynamic Audiences** - Automated segmentation based on real-time profile evaluation
* **Advanced Operators** - Comprehensive filtering with equality, string, numeric, and date comparisons
* **Logical Combinations** - Complex targeting using AND/OR logic
* **Real-Time Evaluation** - Audience membership updates automatically as user data changes

## Static Lists

Lists are manually managed collections of users that you control completely. They're ideal for curated groups where you want precise control over membership.

<Frame caption="List Management Interface">
  <img src="https://mintcdn.com/courier-4f1f25dc/ocKTSyLlc6Ky9Ivc/assets/platform/users/list-management-interface.png?fit=max&auto=format&n=ocKTSyLlc6Ky9Ivc&q=85&s=3944fd2b71511bb2d7f3f490e17d9cda" alt="List Management Interface" width="2514" height="1544" data-path="assets/platform/users/list-management-interface.png" />
</Frame>

### API Usage

Target a list using the `list_id` parameter in your send request:

```json  theme={null}
{
  "to": {
    "list_id": "beta_testers"
  }
}
```

## Dynamic Audiences

Audiences automatically include or exclude users based on rules and filters you define. Instead of manually managing membership, audiences evaluate user profile data in real-time to determine targeting.

<Frame caption="Audience Builder Interface">
  <img src="https://mintcdn.com/courier-4f1f25dc/ocKTSyLlc6Ky9Ivc/assets/platform/users/audience-builder.png?fit=max&auto=format&n=ocKTSyLlc6Ky9Ivc&q=85&s=fbc9ddec2525106c941751a824c1d911" alt="Audience Builder Interface" width="2518" height="1550" data-path="assets/platform/users/audience-builder.png" />
</Frame>

### API Usage

Target an audience using the `audience_id` parameter in your send request:

```json  theme={null}
{
  "to": {
    "audience_id": "active_premium_users"
  }
}
```

## Audience Configuration

Audiences use **operators** to evaluate user profile data against specified conditions. When you send to an audience, Courier evaluates each user's profile in real-time to determine if they match the audience criteria.

**Benefits of dynamic audiences:**

* **Automatic updates** - Membership changes as user data changes
* **Complex targeting** - Combine multiple conditions with logical operators
* **Real-time evaluation** - Users matched at send time for accuracy
* **Scalable segmentation** - No manual list maintenance required

### Available Operators

The table below summarizes the operators available to you when building an audience. We've included both the operator as shown in the UI, and also what the operator is when used in code as described in the [API Reference](/api-reference/audiences/list-all-audiences).

| Category      | Operator                    | Code          | Use Cases                                                |
| ------------- | --------------------------- | ------------- | -------------------------------------------------------- |
| **Equality**  | is                          | `EQ`          | Match exact values (subscription tiers, roles, statuses) |
|               | is not                      | `NEQ`         | Exclude specific values (not free tier, not inactive)    |
| **String**    | includes                    | `INCLUDES`    | Email domains, name patterns, job titles                 |
|               | does not include            | `OMIT`        | Exclude patterns or keywords                             |
|               | starts with                 | `STARTS_WITH` | Email prefixes, ID patterns                              |
|               | ends with                   | `ENDS_WITH`   | Email domains (@company.com), file extensions            |
| **Numeric**   | is greater than             | `GT`          | Age minimums, spending thresholds                        |
|               | is greater than or equal to | `GTE`         | Account limits, minimum values                           |
|               | is less than                | `LT`          | Age maximums, company size limits                        |
|               | is less than or equal to    | `LTE`         | Budget caps, usage limits                                |
| **Date**      | is greater than             | `AFTER`       | Recent activity, future dates                            |
|               | is less than                | `BEFORE`      | Historical data, cutoff dates                            |
| **Existence** | exists                      | `EXISTS`      | Has premium features, has phone number                   |

### Combining Conditions

Use logical operators to create complex audience rules:

* **AND**: All conditions must be true (premium users in California)
* **OR**: At least one condition must be true (admin or manager roles)

## Related Resources

<CardGroup cols={2}>
  <Card title="User Management" href="/platform/users/users" icon="user">
    Individual user profiles and targeting
  </Card>

  <Card title="Audiences API" href="/api-reference/audiences/get-an-audience" icon="code">
    Create and manage audiences programmatically
  </Card>
</CardGroup>
