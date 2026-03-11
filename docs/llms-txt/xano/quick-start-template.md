# Source: https://docs.xano.com/quick-start-template.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Quick Start Template

> Spin up a working B2B SaaS backend in minutes with Xano’s Quick Start template.

The **Quick Start template** is a fully functional B2B SaaS backend that’s auto-created when you sign up for Xano.

Use it to run a live example instantly, then dive into each API group and function stack to **learn Xano by doing**.

It includes:

* A clean database model
* Grouped API endpoints
* Reusable custom functions
* A pre-configured AI Agent
* A lightweight HTML demo front end

Explore the demo, peek into the function stacks, and see exactly how it all fits together.\
You can expand the template for your use case — or simply use it as a **learning accelerator**.

<Card title="Watch the Demo" icon="youtube" horizontal href="https://www.youtube.com/watch?v=P-0NnpPl3fQ" />

***

## What's included?

### Authentication

Pre-built authentication flows, including password reset for when a user forgets their password.

### Members & Accounts

Users belong to accounts (organizations). **Roles** determine which endpoints they can access.

### Event Logging

A custom function records user actions to an `event_log` table for analytics and reporting.

### AI Agent

The `Xano_Example_Agent` uses a Tool connected to the Xano docs. Conversations and messages are stored for reference.

### Hosted Front-end Chatbot Demo

A lightweight HTML demo that showcases how a front end can interact with your Xano backend. It uses the APIs and data included in the template to build a simple chatbot that can answer questions about the Xano platform.

### Database

## A clean database model is included, with tables for users, accounts, logs, and agent messages.

## Demo

### Try the Chatbot

The demo (inside the **Authentication API group**) showcases how a front end communicates with your Xano backend. It includes signup, login, and password reset flows — plus a built-in **AI chatbot** powered by Google Gemini.

<Steps>
  <Step title="Open the demo">
    Open the demo by clicking <span class="ui-bubble"><Icon icon="layer-group" /> API</span>, choose the Authentication API group, and then click on the <span class="ui-bubble"><Icon icon="arrow-up-right-from-square" /> Launch Demo</span> button.
  </Step>

  <Step title="Sign up with a new user account" />

  <Step title="Chat with the AI Agent">
    You can ask the agent questions about Xano. It's linked to our documentation, so it can also serve as a general learning assistant as you learn how Xano works.
  </Step>
</Steps>

After signing up and using the chatbot, you'll see in the database records created for your user account, and the messages sent to and from the agent in the appropriate tables.

#### Password Reset (Optional)

1. **Request link:** `GET reset/request-reset-link` (ensure a user exists with the instance owner’s email)
2. **Magic login:** `POST reset/magic-login` → click the link in the email
3. **Update password:** `POST reset/update-password` → set a new password

<Info>
  The Send Email function allows up to 100 test emails to the **instance owner’s email** (the one you signed up with).\
  To send more or use different recipients, add your **Resend API key** or connect a provider via Action or External API Request.
</Info>

***

## Authentication & Password Reset

```http  theme={null}
POST auth/signup
→ Create a user and return auth token

POST auth/login
→ Exchange credentials for auth token

GET auth/me
→ Return the current authenticated user

# Password reset flow
GET reset/request-reset-link → email link
→ POST reset/magic-login
→ POST reset/update-password
```

***

## AI Agent

The `Xano_Example_Agent` works **out of the box**, complete with complimentary tokens.\
It uses a single Tool to call an MCP Server and access Xano documentation — perfect for building your own prompt-based or tool-augmented workflows.

Check out the `demo-agent/conversation` function stack to see how the agent calls the Tool. Use it as a **blueprint** for your own agentic features.

***

## Event Logging

The template includes a **custom function** that logs events into the `event_log` table. It’s woven into many API endpoints, so you can track:

* Which features users engaged with
* What happened before a support ticket
* How usage varies by account or user

This is your launchpad for reporting, analytics, and monitoring.

***

## Members & Accounts

Common B2B app patterns are built in:

* Users can **create new accounts** (e.g., their team’s organization)
* Users can **join existing accounts**, **view teammates**, and **update their profile**
* **Role-based access control (RBAC)** is baked in:
  * Admins can manage roles on their account
  * Members have restricted access
  * Admins can view all event logs; users can only see their own

<Warning>
  RBAC is crucial for securing your app. Admin-only endpoints check user roles before proceeding.\
  Use the built-in `role-based access control` function in your middleware for consistent enforcement.
</Warning>

***

## Database

| Table                | Purpose                                             |
| -------------------- | --------------------------------------------------- |
| `user`               | App users (email, password hash, role, account\_id) |
| `account`            | Organizations/teams; multiple users per account     |
| `event_log`          | Records of user actions for analytics               |
| `agent_message`      | Stores messages within conversations                |
| `agent_conversation` | Parent threads for agent messages                   |

***

## APIs

The Quick Start template organizes endpoints into **API groups**:

### Authentication

Handles login, signup, password reset, welcome emails, and demo interactions.

* `GET 1_start_here_demo` — Launch the demo UI
* `POST auth/login` — Log in
* `GET auth/me` — Get authenticated user details
* `POST auth/signup` — Sign up
* `GET demo-agent/conversation` — Interact with the AI Agent
* `POST message/send_welcome_email` — Send a test welcome email
* `GET reset/request-reset-link` / `POST reset/magic-login` / `POST reset/update-password` — Password reset flow

<Info>
  `message/send-welcome-email` and `reset/request-reset-link` use the Xano Send Email function for **free testing emails** (up to 100).\
  For production, add your own API key or external service.
</Info>

***

### Event Logs

* `GET logs/admin/account_events` — Admins can pull logs for their entire account (with RBAC enforcement).
* `GET logs/user/my_events` — Users can view their own logs.

***

### Members & Accounts

* `POST account` — Create a new account
* `GET account/details` — Retrieve account info
* `GET account/my_team_members` — View team members
* `POST admin/user_role` — Admin updates user roles (RBAC enforced)
* `PATCH user/edit_profile` — Update user profile
* `POST user/join_account` — Join an existing account

***

## AI

### Xano Example Agent

A fully functional AI agent connected to a **Tool** that accesses Xano Docs via MCP Server. Complimentary tokens are included so you can start experimenting right away.

When ready, plug in your own provider keys to go beyond the example setup.

***

<Icon icon="gears" /> ## Functions

Custom functions provide **reusable logic** for any API stack:

| Function                    | Purpose                                              |
| --------------------------- | ---------------------------------------------------- |
| `Create_event_log`          | Adds a record to the event logs table                |
| `Generate_magic_link`       | Helper for password reset flows                      |
| `Role-based access control` | Enforces permissions at the start of function stacks |

<Info>
  These functions can also be used as middleware when upgrading your workspace to enforce business rules consistently.
</Info>

***

<Icon icon="arrow-right" /> ## Next Steps

The Quick Start template is a **launchpad**. You can:

* Expand and adapt it for production use
* Use it purely as a **learning sandbox**
* Or reset your workspace and build from scratch

<Warning>
  The demo isn’t meant for production — it’s a guided example of how a front end can interact with a Xano backend.
</Warning>


Built with [Mintlify](https://mintlify.com).