# Source: https://langfuse.com/self-hosting/deployment/railway.md

---
title: Deploy Langfuse v3 on Railway
description: Use this guide to deploy Langfuse v3 on Railway via the prebuilt template.
label: "Version: v3"
sidebarTitle: "Railway"
---

# Railway

You can deploy Langfuse v3 on [Railway](https://railway.app/) via the prebuilt template.
The template contains all the necessary services and configurations to get you started.
See [architecture overview](/self-hosting#architecture) for more details.

## Deploy

Use the following button to deploy the Langfuse v3 template on Railway:

[![Deploy on Railway](https://railway.com/button.svg)](https://railway.app/template/exma_H?referralCode=513qqz)

Recording of 1-click deployment on Railway:

<Video
  src="https://static.langfuse.com/docs-videos/railway-v3.mp4"
  aspectRatio={16 / 9}
/>

## Features

Langfuse supports many configuration options and self-hosted features.
For more details, please refer to the [configuration guide](/self-hosting/configuration).



import {
  Lock,
  Shield,
  Network,
  Users,
  Brush,
  Workflow,
  UserCog,
  Route,
  Mail,
  ServerCog,
  Activity,
  Eye,
  Zap,
} from "lucide-react";

import { Cards } from "nextra/components";

<Cards num={3}>
  <Cards.Card
    icon={<Lock size="24" />}
    title="Authentication & SSO"
    href="/self-hosting/security/authentication-and-sso"
    arrow
  />
  <Cards.Card
    icon={<UserCog size="24" />}
    title="Automated Access Provisioning"
    href="/self-hosting/administration/automated-access-provisioning"
    arrow
  />
  <Cards.Card
    icon={<Zap size="24" />}
    title="Caching"
    href="/self-hosting/configuration/caching"
    arrow
  />
  <Cards.Card
    icon={<Route size="24" />}
    title="Custom Base Path"
    href="/self-hosting/configuration/custom-base-path"
    arrow
  />
  <Cards.Card
    icon={<Shield size="24" />}
    title="Encryption"
    href="/self-hosting/configuration/encryption"
    arrow
  />
  <Cards.Card
    icon={<Workflow size="24" />}
    title="Headless Initialization"
    href="/self-hosting/administration/headless-initialization"
    arrow
  />
  <Cards.Card
    icon={<Network size="24" />}
    title="Networking"
    href="/self-hosting/security/networking"
    arrow
  />
  <Cards.Card
    icon={<Users size="24" />}
    title="Organization Creators (EE)"
    href="/self-hosting/administration/organization-creators"
    arrow
  />
  <Cards.Card
    icon={<ServerCog size="24" />}
    title="Organization Management API (EE)"
    href="/self-hosting/administration/organization-management-api"
    arrow
  />
  <Cards.Card
    icon={<Activity size="24" />}
    title="Health and Readiness Check"
    href="/self-hosting/configuration/health-readiness-endpoints"
    arrow
  />
  <Cards.Card
    icon={<Eye size="24" />}
    title="Observability via OpenTelemetry"
    href="/self-hosting/configuration/observability"
    arrow
  />
  <Cards.Card
    icon={<Mail size="24" />}
    title="Transactional Emails"
    href="/self-hosting/configuration/transactional-emails"
    arrow
  />
  <Cards.Card
    icon={<Brush size="24" />}
    title="UI Customization (EE)"
    href="/self-hosting/administration/ui-customization"
    arrow
  />
</Cards>


