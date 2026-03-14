# Source: https://documentation.onesignal.com/docs/en/suppressions.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Suppressions

> Manage suppressed emails and phone numbers in OneSignal.

The suppression list is an automated safeguard that helps maintain your email list hygiene and protect your sender reputation. When using OneSignal as your email service provider, this feature automatically manages problematic email addresses to prevent deliverability issues. More on [email deliverability](./email-deliverability)

## How It Works

When OneSignal detects any of the following conditions:

1. An email recipient marks your message as spam
2. An email address has previously bounced

The system automatically adds these email addresses to your suppression list. Once an address is suppressed, OneSignal will no longer attempt to send emails to it, helping to:

1. Maintain a clean email list
2. Improve overall deliverability
3. Protect your sender reputation
4. Reduce bounce rates

## Managing Your Suppression List

You can view and manage your suppression list by navigating to **Settings** > **Email** > **Suppression**:

<Frame caption="A suppression list in OneSignal">
  <img src="https://mintcdn.com/onesignal/0qspEXXeJ8zJbkJ-/images/docs/8ae7682c119f7c82d14e89c43756fd54d61a93899dca9d98ce921b9a0f0199db-Screenshot_2025-04-25_at_15.34.43.png?fit=max&auto=format&n=0qspEXXeJ8zJbkJ-&q=85&s=d13062eeb4b19da44e6bae7f9ba5063c" width="3244" height="1936" data-path="images/docs/8ae7682c119f7c82d14e89c43756fd54d61a93899dca9d98ce921b9a0f0199db-Screenshot_2025-04-25_at_15.34.43.png" />
</Frame>

Here you can find a list of all suppressed email addresses, separated into lists depending on whether they were the result of a bounce, spam report, added manually through the dashboard or uploaded manually via our [CSV Import](./import) tool.

**Note:**&#x49;f you are using another ESP as your email service provider, your suppression list must be managed directly through your ESP's platform.

### Adding new suppressions

To manually add a new email address to your suppression list, you can click the **Add Email** button to add the email manually:

<Frame caption="Adding an email to a suppression list manually">
  <img src="https://mintcdn.com/onesignal/9_Q1FZLh6C0BFLq-/images/docs/c603788e10f852bd760c51ea3161ea888b72c5a90da7d36d93c83593d22cf771-Screenshot_2025-04-25_at_15.42.50.png?fit=max&auto=format&n=9_Q1FZLh6C0BFLq-&q=85&s=b265d96648e22483129026f4de4522e0" width="3244" height="1936" data-path="images/docs/c603788e10f852bd760c51ea3161ea888b72c5a90da7d36d93c83593d22cf771-Screenshot_2025-04-25_at_15.42.50.png" />
</Frame>

Alternatively, you can add email addresses to the suppression list in bulk by using our [CSV Import](./import) tool and ensuring that you include a `suppressed` column with the value set to `true` for each row. You can then map this column to **suppressed** after uploading your CSV:

<Frame caption="Using the CSV import tool to add a suppression list">
  <img src="https://mintcdn.com/onesignal/RWtLFPeffHrC81wI/images/docs/aa517d8a816168bda92088970f31ce0f4cd3565395f45c0a3366076823f32083-Screenshot_2025-04-25_at_15.46.42.png?fit=max&auto=format&n=RWtLFPeffHrC81wI&q=85&s=ae16c18c4f34b7e4317fd24a8a8729a5" width="3244" height="1936" data-path="images/docs/aa517d8a816168bda92088970f31ce0f4cd3565395f45c0a3366076823f32083-Screenshot_2025-04-25_at_15.46.42.png" />
</Frame>

### Removing suppressions

To remove a suppression, you can click the trash icon next to an email in the list to remove that email from the suppression list:

<Frame caption="Deleting a single email from a suppression list">
  <img src="https://mintcdn.com/onesignal/4HyuQPBpu-4xjmQC/images/docs/d01459a38d2a79b829956e7994b5c40c4217e10e209bb821ec2ad57957c3e295-Screenshot_2025-04-25_at_15.48.41.png?fit=max&auto=format&n=4HyuQPBpu-4xjmQC&q=85&s=3078267c8b0c62b002644d3232843444" width="3244" height="1936" data-path="images/docs/d01459a38d2a79b829956e7994b5c40c4217e10e209bb821ec2ad57957c3e295-Screenshot_2025-04-25_at_15.48.41.png" />
</Frame>

To remove emails in bulk from the suppression list, you can use our [CSV Import](./import) tool and ensuring that you include a `suppressed` column with the value set to `false` for each email that you want to remove. You can then map this column to **suppressed** after uploading your CSV:

<Frame caption="Using the CSV import tool to remove multiple email addresses from the suppression list">
  <img src="https://mintcdn.com/onesignal/_KaXe4GQkxsEfa17/images/docs/348618ff0aad3dc1dd48de70f58233f1b0109d5217e02d3a0bb3ab3813cfbb51-Screenshot_2025-04-25_at_15.52.32.png?fit=max&auto=format&n=_KaXe4GQkxsEfa17&q=85&s=bff047b23b459973e65eebba207be495" width="3244" height="1936" data-path="images/docs/348618ff0aad3dc1dd48de70f58233f1b0109d5217e02d3a0bb3ab3813cfbb51-Screenshot_2025-04-25_at_15.52.32.png" />
</Frame>

***

Built with [Mintlify](https://mintlify.com).
