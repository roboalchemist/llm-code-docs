# Source: https://docs.drip.re/changelog.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.drip.re/llms.txt
> Use this file to discover all available pages before exploring further.

# Changelog

> Product updates and announcements for DRIP platform

# Changelog

Stay up to date with the latest improvements, features, and updates to the DRIP platform.

<Update label="August 20, 2025" description="v2.2.0" tags={["Authentication", "OAuth", "Security", "API"]}>

## User Authentication & OAuth Flow

  We're excited to introduce a secure OAuth-like authentication flow that enables apps to access user data with explicit consent.

### 🔐 New Authentication Features

* **OAuth Consent Flow**: Users can now securely authorize apps to access their DRIP profile data
* **Consent Page**: Beautiful authorization page at `app.drip.re/oauth/authorize` where users review and approve app permissions
* **Secure Authorization Codes**: Short-lived (5-minute) single-use codes for maximum security
* **Minimal Data Exposure**: Apps only receive the user's DRIP ID, protecting sensitive information

### 🚀 Developer Benefits

* **Works for All App Types**: Supports both single-realm and multi-realm applications
* **Simple Integration**: Standard OAuth 2.0-like flow that developers already know
* **Public Client Info API**: Apps can display their verification status and information transparently
* **Comprehensive Documentation**: Full implementation guides with examples in multiple languages

### 🔧 API Endpoints

* `GET /oauth/authorize` - User consent page (browser)
* `POST /api/v1/auth/oauth/token` - Exchange authorization code for user's DRIP ID
* `GET /api/v1/auth/oauth/client` - Fetch public app information

### 📚 Documentation

* New comprehensive guide at [User Authentication & OAuth](/developer/user-authentication)
* Code examples in JavaScript, Python, and TypeScript
* Complete server implementation examples
* Error handling and troubleshooting guides

  This update makes it easier than ever for developers to build secure, user-consented integrations with the DRIP platform while maintaining user privacy and control.
</Update>

<Update label="August 15, 2025" description="v2.1.0" tags={["Documentation", "Developer Experience"]}>

## Documentation Rework

  We've completely revamped our documentation to provide a better developer experience:

### ✨ New Features

* **Enhanced API Reference**: Restructured API documentation with clear separation between current and legacy APIs
* **Expanded Developer Guide**: Added comprehensive guides for authentication, core concepts, and app development
* **Interactive Navigation**: Implemented dropdown navigation for better content organization
* **Dark Mode Optimization**: Full black background theme for improved readability

### 🔧 Improvements

* **Better Search Experience**: Enhanced search functionality with contextual prompts
* **Mobile-Responsive Design**: Optimized documentation layout for all devices
* **Auto-Expanding Accordions**: API reference sections now automatically expand for easier navigation
* **RSS Feed Support**: Subscribe to changelog updates via RSS

### 📚 Additional Content

* **Migration Guidance**: Clear instructions for transitioning from legacy to current API
* **Code Examples**: More comprehensive examples across all endpoints
* **Developer Resources**: Enhanced reference materials for rate limits, errors, and best practices

  The new documentation structure makes it easier than ever to integrate with DRIP's powerful rewards and engagement platform.
</Update>

Built with [Mintlify](https://mintlify.com).
