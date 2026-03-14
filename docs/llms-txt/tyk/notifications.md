# Source: https://tyk.io/docs/ai-management/ai-studio/notifications.md

> ## Documentation Index
> Fetch the complete documentation index at: https://tyk.io/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Notification

> How to configure notifications in Tyk AI Studio?

Tyk AI Studio includes a centralized Notification System responsible for generating and delivering alerts and messages to users and administrators based on specific system events.

## Purpose

The Notification System aims to:

* **Inform Stakeholders:** Keep users and administrators aware of important events or required actions.
* **Enable Proactive Management:** Alert administrators to potential issues or thresholds being reached (e.g., budget limits).
* **Improve User Experience:** Provide timely feedback on asynchronous processes or user-related events.

## Key Features

* **Event-Driven:** Notifications are triggered by specific occurrences within the Tyk AI Studio platform.
* **Configurable Channels:** Supports multiple delivery methods, primarily:
  * **Email:** Sending notifications to registered user email addresses.
  * **In-App Notifications:** Displaying messages directly within the Tyk AI Studio UI.
* **User Preferences:** Allows users (and potentially administrators) to configure which notifications they wish to receive and via which channels (where applicable).
* **Centralized Logic:** Provides a single system for managing notification templates and delivery rules.

## Common Notification Triggers

Examples of events that might trigger notifications include:

* **[Budget Control](/ai-management/ai-studio/llm-management):**
  * Approaching spending limit threshold (e.g., 80% of budget).
  * Reaching or exceeding spending limit.
* **[User Management](/ai-management/ai-studio/user-management):**
  * New user registration/invitation.
  * Password reset request.
  * Changes in user roles or group memberships.
* **System Health & Errors:**
  * Significant system errors or failures.
  * Service degradation alerts.
* **Security Events:**
  * Suspicious login activity (if monitored).
  * Changes to critical security settings.

## Configuration

* **System-Level (Admin):** Administrators typically configure the core settings for the notification system, such as:
  * Email server (SMTP) details for sending emails.
  * Default notification templates.
  * Enabling/disabling specific system-wide notification types.
* **User-Level:** Users can often manage their notification preferences in their profile settings:

  * Opt-in/opt-out of specific notification categories.
  * Choose preferred delivery channels (e.g., receive budget alerts via email).

  <img src="https://mintcdn.com/tyk/KUyxLx5tNlKCB02w/img/ai-management/notification-preferences.png?fit=max&auto=format&n=KUyxLx5tNlKCB02w&q=85&s=fa9ac19db37a4a448bc33848f16ac3b9" alt="Notification Prefs UI" width="1024" height="597" data-path="img/ai-management/notification-preferences.png" />

## Integration

The Notification System integrates with various other Tyk AI Studio components that generate relevant events, including:

* Budget Control System
* User Management System
* Analytics System (potentially for performance alerts)
* Proxy/Gateway (for error or security event alerts)

This system ensures timely communication, helping users and administrators stay informed about the status and activity within the Tyk AI Studio platform.


Built with [Mintlify](https://mintlify.com).