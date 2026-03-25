# Source: https://doc.keepnetlabs.com/next-generation-product/miscellaneous/allow-listing/understanding-email-delivery-errors.md

# Understanding Email Delivery Errors

This document provides an overview of the common issues related to the non-delivery of training emails sent to users. It is designed to help system users understand the error messages they may encounter, specifically focusing on the "bounce" and "dropped" statuses.

## Email Delivery Error Types

### **1. Bounce Errors**

A "bounce" error occurs when an email is returned to the sender because it could not be delivered to the recipient. Bounces are classified based on the nature of the problem that caused the non-delivery.

#### **Common Bounce Error:**

* 550 5.1.1 Recipient Address Rejected: User Unknown

This error signifies that the recipient's email server has permanently rejected the message because the specified email address does not exist on the recipient server. This is a common issue when the email address is misspelled, outdated, or the recipient's mailbox has been deleted.

#### **Examples:**

<table><thead><tr><th width="257">Delivery Message</th><th>Explanation</th></tr></thead><tbody><tr><td><strong>550 5.7.129 RESOLVER.RST.RestrictedToRecipientsPermission</strong></td><td>The sending email address is not permitted to email the recipient, possibly due to a allow list or exclusive permissions setting</td></tr><tr><td><strong>550 5.7.1 TRANSPORT.RULES.RejectMessage</strong></td><td>The email was rejected due to an organization's policy, which might be a rule set to prevent certain types of emails from being received</td></tr><tr><td><strong>550 5.7.134 RESOLVER.RST.SenderNotAuthenticatedForMailbox</strong></td><td>The sender's identity could not be verified by the recipient's server, necessary for mail delivery</td></tr><tr><td><strong>554 5.4.14 Hop count exceeded</strong></td><td>The email was caught in a routing loop and exceeded the allowed number of transfers between servers</td></tr><tr><td><strong>554 5.2.2 mailbox full</strong></td><td>The recipient's email inbox is full and cannot accept new messages until space is freed</td></tr><tr><td><strong>Administrative prohibition - envelope blocked</strong></td><td>The email was prevented from delivery by a policy, likely as a security measure against spam or unauthorized content</td></tr><tr><td><strong>550 5.1.1: The email account that you tried to reach does not exist</strong></td><td>The email address you're trying to send a message to does not exist or is misspelled</td></tr><tr><td><strong>550 5.1.1: Recipient address rejected: User unknown</strong></td><td>The email server could not deliver the message because it couldn't find a user with the email address</td></tr><tr><td><strong>554 5.7.1</strong> <a href="mailto:user3@website.org"><strong>user3@website.org</strong></a><strong>: Relay access denied</strong></td><td>The email server receiving your message has rejected it because it refuses to relay the message to the intended recipient's email address. The server may be configured to only relay emails for certain domains or to only accept emails for local users</td></tr><tr><td><strong>Error dialing remote address: dial tcp 149.92: i/o timeout</strong></td><td><p>This error indicates that there was a timeout while attempting to establish a TCP connection. This error commonly occurs due to network issues, such as:</p><p>the remote server being unreachable or offline, network congestion or connectivity problems.</p></td></tr></tbody></table>

These errors indicate that the sending server is trying to relay an email through the recipient's email server without proper authorization. This can occur if the sender's email server is not allowed to send emails on behalf of the email address it is using.

**Handling Errors**

To minimize these errors, ensure that:

* The best way to reduce not delivery is [Allow Listing](https://doc.keepnetlabs.com/next-generation-product/miscellaneous/allow-listing) across all your security solutions
* Do not sync services accounts which are unlikely manned such as <donotdelete@example.com>, <noreply@domain.com>, etc.
* Check emails for spelling mistakes or formatting issues
* Check for any network issues or firewalls blocking the connection.
* If you notice one of these errors, please try resending the email to the user [following the steps on this page](https://doc.keepnetlabs.com/platform/awareness-educator/training-reports#resend-training)

### **2. Dropped Errors**

"Dropped" errors occur when the email server has stopped attempting to deliver an email after previous attempts resulted in a bounce. This usually happens when the email address has been flagged from prior bounce records, and the server opts not to waste resources on future attempts.

#### **Common Dropped Error:**

**Bounced Address**

This status is given when an email address has previously been marked as bounced, and further emails to this address are automatically dropped without attempting delivery.\
Examples:

* "Email to <user3@domain.com> dropped: previously bounced address"
* "Email to <person4@website.org> dropped: bounced address"
* "Email to <info@company.net> dropped: bounced address"

**Handling Errors**

To minimize these errors, ensure that:

* Email addresses are collected accurately and verified at the point of entry.
* Regular updates and checks are performed on your email lists to remove outdated or incorrect addresses.
* Utilize double opt-in methods where recipients must confirm their email addresses, reducing the chances of typing errors.

## Handling Email Training Enrollment for Users Without Initial Inbox Setup in Microsoft Office 365

If a company uses Microsoft Office 365, they can set up a user account that doesn't initially have an email inbox, like "<user2@company.com>". This account details can then be automatically synchronized with Keepnet's Target Users database using SCIM (System for Cross-domain Identity Management).

#### Here's what happens next:

1. **Automatic Training Enrollment:** As soon as Keepnet detects this new user in the company's list, it tries to send a training email. However, because this user doesn't have an email inbox set up yet, the attempt to send the training email fails.
2. **Manual Training Enrollment:** Later on, when a system user manually tries to enroll the same user in training, the email is successfully delivered. This success occurs because, by this time, the system administrator has created an inbox for that user.

In simple terms, if the user doesn't have an email inbox at first, Keepnet's automatic email will fail. But if the inbox is set up later, any following attempts to send emails will succeed.

#### Suggested Solution

To avoid the issue of training emails failing due to no inbox being set up initially, we strongly suggest adjusting the settings to "Automatically enroll new users in target group: next day" rather than "the same day". This delay allows time for the inbox to be established, ensuring that training emails are successfully delivered.

#### Summary

By implementing this adjustment, companies can enhance the effectiveness of their training programs and ensure smooth communication workflows within Microsoft Office 365 environments.
