# Source: https://glow-docs.xrpl-commons.org/technical-resources/platform-architecture.md

# Platform Architecture

## Overview

The Glow platform is a modern web application built with Nuxt.js (Vue 3) to facilitate the retroactive funding process for XRPL ecosystem contributors. The platform connects Scouts, Contributors, Judges, Voters, and Admins in a streamlined workflow.

## Tech Stack

* **Frontend Framework:** [Nuxt.js](https://nuxt.com/) (Vue 3)
* **UI Components:** [@nuxt/ui](https://ui.nuxt.com/)
* **Styling:** Tailwind CSS
* **Server-Side:** Nuxt server middleware
* **Database:** MongoDB
* **Authentication:** Custom auth module with session-based authentication
* **XRPL Integration:** Wallet connectivity for voting and wallet registration

## Core Modules

### 1. Auth Module

Manages user sessions and role-based access control:

* Role management: Admin, Scout, Judge, Contributor, Voter
* Session persistence
* Route protection based on user roles
* Password management

### 2. Wallet Connectivity

Facilitates voting and wallet registration:

* XRP Ledger wallet integration
* Transaction signing
* Wallet address verification
* Support for multiple wallet providers (Xaman, GemWallet, Crossmark, etc.)

### 3. API Services

* RESTful endpoints for all platform operations
* Secure data access and validation
* Integration with external services (XRPL, KYC, etc.)

***

For technical questions or support, contact <info@xrpl-commons.org>.
