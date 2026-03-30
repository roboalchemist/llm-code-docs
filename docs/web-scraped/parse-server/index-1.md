# Source: https://parseplatform.org/

Title: Parse Platform - Open Source Backend

URL Source: https://parseplatform.org/

Published Time: Tue, 10 Mar 2026 14:40:38 GMT

Markdown Content:
![Image 1: Parse Platform](blob:http://localhost/de22e51cfe1cf8757b525adc3fdaa6a6)Parse Platform

Build a mobile |

for your
---------------------------

Parse Platform is your complete backend solution for mobile and web applications.

Deploy anywhere, scale infinitely, own your data.

[Start Building](https://parseplatform.org/#get-started)[Documentation](https://parseplatform.org/#docs)

13,197

GitHub Stars

3,604

Forks

4

SDK Platforms

206+

Contributors

Powerful Features
-----------------

Everything you need to build modern applications

MongoDB and PostgreSQL support with flexible file storage options including Amazon S3, Google Cloud Storage, and local storage.

*   Real-time data synchronization
*   GridFS default storage
*   Multi-database support

Comprehensive user management with OAuth support, email verification, and flexible authentication options.

*   OAuth integration
*   Email verification
*   Custom authentication

REST and GraphQL APIs with multi-platform SDKs for seamless integration across all major platforms.

*   REST & GraphQL APIs
*   Multi-Platform SDKs
*   Custom queries & mutations

Live queries for real-time data updates and built-in push notification support across all platforms.

*   Live Queries
*   Push notifications
*   Real-time updates

Server-side logic execution with custom functions, database triggers, and background job processing.

*   Custom cloud functions
*   Database triggers
*   Background jobs

Deploy anywhere that runs Node.js. Full control over your infrastructure and data with Parse Dashboard for management.

*   Any Node.js infrastructure
*   Parse Dashboard included
*   Complete data ownership

Parse Server
------------

Core backend services and APIs for your applications

### Cloud Code

Custom server-side JavaScript functions for advanced business logic.

[Documentation](https://docs.parseplatform.org/cloudcode/guide/)

### REST API

A RESTful HTTP API for interacting with all Parse Platform services.

[Documentation](https://docs.parseplatform.org/rest/guide/)

### GraphQL API

A modern GraphQL API supporting queries, mutations, and subscriptions.

[Documentation](https://docs.parseplatform.org/graphql/guide/)

### Extensions

Enhance Parse Server with official and community-built extensions.

[Explore Extensions](https://parseplatform.org/extensions)

Multi-Platform SDKs
-------------------

Build for every platform with our comprehensive SDK collection

Parse Dashboard
---------------

Powerful web interface for managing your Parse Server data and configuration

#### Data Browser

Browse, edit, and query your application data with an intuitive table interface

#### User Management

Manage user accounts, roles, and permissions directly from the dashboard

#### API Console

Test queries and execute code directly in the dashboard with an interactive console

#### Configuration

Configure app settings, push notifications, and security parameters

Parse Dashboard

Data Browser

objectId username createdAt

xK7m1Pq9 user_1 2024-01-01

xK7m2Pq9 user_2 2024-01-02

xK7m3Pq9 user_3 2024-01-03

3 of 127 objects

Get Started in Minutes
----------------------

Deploy your Parse Server with just a few commands

1

### Install

Install Parse Server via npm

2

### Configure

Set up your database and keys

3

### Deploy

Launch your backend

install.sh

```
# Install Parse Server
npm install -g parse-server

# Start Parse Server
parse-server --appId myAppId --masterKey myMasterKey --databaseURI mongodb://localhost:27017/dev

# Your Parse Server is running on http://localhost:1337/parse
```

Then save and find your first object using Parse Server's [REST API](https://parseplatform.org/#server-apis)

install.sh

```
# Create a new Booking object
curl -X POST \
  -H "X-Parse-Application-Id: myAppId" \
  -H "X-Parse-Master-Key: myMasterKey" \
  -H "Content-Type: application/json" \
  -d '{"room":101,"guests":2,"nights":4}' \
  http://localhost:1337/parse/classes/Booking

# Get all bookings of room 101
curl -X GET \
  -H "X-Parse-Application-Id: myAppId" \
  -H "X-Parse-Master-Key: myMasterKey" \
  -G \
  --data-urlencode 'where={"room":{"$eq":101}}' \
  http://localhost:1337/parse/classes/Booking
```

Documentation & Resources
-------------------------

Comprehensive guides and references for every platform

### Parse Server Guide

Complete guide for deploying and configuring Parse Server

### Postman Template

Ready-to-use Postman collection for Parse Server REST API testing

### Client SDK Guides

Platform-specific integration guides for all supported SDKs
