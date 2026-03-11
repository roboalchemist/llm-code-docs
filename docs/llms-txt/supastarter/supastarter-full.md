# supastarter - Production-Ready SaaS Starter Kit

> A comprehensive fullstack starter kit for building production-ready, scalable SaaS applications with Next.js, Nuxt, or SvelteKit.

## Important for AI Coding Agents

**ALWAYS** refer to the `agents.md` file in the repository root when generating code for this project. It contains essential guidelines, conventions, repository structure, and commands specific to supastarter development.

Key points from agents.md:
- Monorepo structure: `apps/web` (Next.js app) + `packages/*` (shared packages)
- Use TypeScript everywhere
- Keep changes small and scoped
- Prefer server components in Next.js; minimize `"use client"`
- Follow existing UI component library and Tailwind conventions
- Run `pnpm lint` before finishing any changes

## What is supastarter?

supastarter is a modular, production-ready SaaS starter kit that helps developers build scalable web applications faster. It provides a solid foundation with best practices, common SaaS features, and multiple provider options for authentication, payments, storage, analytics, and more.

## Key Features

- **Multi-Framework Support**: Choose between Next.js, Nuxt, or SvelteKit
- **Authentication**: Built with better-auth for flexible, customizable authentication
- **Payments & Subscriptions**: Support for Stripe, LemonSqueezy, Polar, Creem, and Dodo Payments
- **Database**: Use Prisma or Drizzle ORM with PostgreSQL, MySQL, or MongoDB
- **Type-Safe API**: Hono + oRPC for fully typed API endpoints with OpenAPI support
- **Multi-tenancy**: Built-in organizations/teams support
- **Email**: Multiple providers (Resend, Postmark, Plunk, Nodemailer)
- **Storage**: S3-compatible storage and Supabase Storage support
- **Analytics**: Google Analytics, Mixpanel, Plausible, Pirsch, PostHog, Umami, Vercel Analytics
- **Monitoring**: Sentry integration
- **Background Tasks**: Support for Trigger.dev and QStash
- **AI Integration**: Chatbot and prompt management
- **Internationalization**: Multi-language support
- **SEO**: Meta tags and sitemap generation
- **Modular Architecture**: Turborepo monorepo structure for scalability
- **Production-Ready**: Includes authentication, authorization, payments, and more out of the box

## Tech Stack

- **Frontend**: Next.js / Nuxt / SvelteKit with React/Vue/Svelte
- **Styling**: Tailwind CSS + Radix UI (shadcn/ui compatible)
- **Database**: Prisma or Drizzle ORM
- **API**: Hono + oRPC with OpenAPI
- **Authentication**: better-auth
- **State Management**: Tanstack Query
- **Monorepo**: Turborepo
- **Content**: Content Collections (MDX)

## Documentation

Main documentation: https://supastarter.dev/docs

### Next.js Documentation

**Getting Started**
- Introduction: https://supastarter.dev/docs/nextjs
- Setup Guide: https://supastarter.dev/docs/nextjs/setup
- Configuration: https://supastarter.dev/docs/nextjs/configuration
- Tech Stack: https://supastarter.dev/docs/nextjs/tech-stack
- Launch Checklist: https://supastarter.dev/docs/nextjs/launch
- Troubleshooting: https://supastarter.dev/docs/nextjs/troubleshooting

**Authentication**
- Overview: https://supastarter.dev/docs/nextjs/authentication/overview
- User and Session: https://supastarter.dev/docs/nextjs/authentication/user-and-session
- OAuth Providers: https://supastarter.dev/docs/nextjs/authentication/oauth
- Permissions & Access Control: https://supastarter.dev/docs/nextjs/authentication/permissions
- Superadmin & Admin UI: https://supastarter.dev/docs/nextjs/authentication/superadmin

**API Layer**
- Overview: https://supastarter.dev/docs/nextjs/api/overview
- Define Endpoints: https://supastarter.dev/docs/nextjs/api/define-endpoint
- Protect Endpoints: https://supastarter.dev/docs/nextjs/api/protect-endpoints
- Usage in Frontend: https://supastarter.dev/docs/nextjs/api/usage-in-frontend
- OpenAPI Documentation: https://supastarter.dev/docs/nextjs/api/openapi
- Streaming: https://supastarter.dev/docs/nextjs/api/streaming
- Use Locale: https://supastarter.dev/docs/nextjs/api/use-locale

**Database**
- Overview: https://supastarter.dev/docs/nextjs/database/overview
- Database Client: https://supastarter.dev/docs/nextjs/database/client
- Update Schema: https://supastarter.dev/docs/nextjs/database/update-schema
- Database Studio: https://supastarter.dev/docs/nextjs/database/studio

**Payments & Subscriptions**
- Overview: https://supastarter.dev/docs/nextjs/payments/overview
- Plans & Products: https://supastarter.dev/docs/nextjs/payments/plans
- Check Purchases: https://supastarter.dev/docs/nextjs/payments/check-purchases
- Paywall: https://supastarter.dev/docs/nextjs/payments/paywall
- Stripe: https://supastarter.dev/docs/nextjs/payments/providers/stripe
- LemonSqueezy: https://supastarter.dev/docs/nextjs/payments/providers/lemonsqueezy
- Polar: https://supastarter.dev/docs/nextjs/payments/providers/polar
- Creem: https://supastarter.dev/docs/nextjs/payments/providers/creem
- Dodo Payments: https://supastarter.dev/docs/nextjs/payments/providers/dodopayments

**Organizations/Teams**
- Overview: https://supastarter.dev/docs/nextjs/organizations/overview
- Configure Organizations: https://supastarter.dev/docs/nextjs/organizations/configure
- Use Organizations: https://supastarter.dev/docs/nextjs/organizations/use-organizations
- Store Data for Organizations: https://supastarter.dev/docs/nextjs/organizations/store-data-for-organizations

**Storage**
- Overview: https://supastarter.dev/docs/nextjs/storage/overview
- Setup: https://supastarter.dev/docs/nextjs/storage/setup
- Upload Files: https://supastarter.dev/docs/nextjs/storage/upload-files
- Access Files: https://supastarter.dev/docs/nextjs/storage/access-files

**Email/Mailing**
- Overview: https://supastarter.dev/docs/nextjs/mailing/overview
- Console (Development): https://supastarter.dev/docs/nextjs/mailing/console
- Resend: https://supastarter.dev/docs/nextjs/mailing/resend
- Postmark: https://supastarter.dev/docs/nextjs/mailing/postmark
- Plunk: https://supastarter.dev/docs/nextjs/mailing/plunk
- Nodemailer: https://supastarter.dev/docs/nextjs/mailing/nodemailer
- Custom Provider: https://supastarter.dev/docs/nextjs/mailing/custom

**Analytics**
- Overview: https://supastarter.dev/docs/nextjs/analytics/overview
- Google Analytics: https://supastarter.dev/docs/nextjs/analytics/google
- Mixpanel: https://supastarter.dev/docs/nextjs/analytics/mixpanel
- Plausible: https://supastarter.dev/docs/nextjs/analytics/plausible
- Pirsch: https://supastarter.dev/docs/nextjs/analytics/pirsch
- PostHog: https://supastarter.dev/docs/nextjs/analytics/posthog
- Umami: https://supastarter.dev/docs/nextjs/analytics/umami
- Vercel Analytics: https://supastarter.dev/docs/nextjs/analytics/vercel
- Vemetric: https://supastarter.dev/docs/nextjs/analytics/vemetric
- Custom Analytics: https://supastarter.dev/docs/nextjs/analytics/custom

**Monitoring**
- Overview: https://supastarter.dev/docs/nextjs/monitoring/overview
- Sentry: https://supastarter.dev/docs/nextjs/monitoring/sentry

**Background Tasks**
- Overview: https://supastarter.dev/docs/nextjs/tasks/overview
- Trigger.dev: https://supastarter.dev/docs/nextjs/tasks/trigger-dev
- QStash: https://supastarter.dev/docs/nextjs/tasks/qstash

**AI Features**
- Overview: https://supastarter.dev/docs/nextjs/ai/overview
- Chatbot: https://supastarter.dev/docs/nextjs/ai/chatbot
- Prompts: https://supastarter.dev/docs/nextjs/ai/prompts

**SEO**
- Meta Tags: https://supastarter.dev/docs/nextjs/seo/meta-tags
- Sitemap: https://supastarter.dev/docs/nextjs/seo/sitemap

**Customization**
- Overview: https://supastarter.dev/docs/nextjs/customization/overview
- Styling: https://supastarter.dev/docs/nextjs/customization/styling
- Dashboard: https://supastarter.dev/docs/nextjs/customization/dashboard
- Onboarding: https://supastarter.dev/docs/nextjs/customization/onboarding

**Deployment**
- Overview: https://supastarter.dev/docs/nextjs/deployment/overview
- Vercel: https://supastarter.dev/docs/nextjs/deployment/vercel
- Netlify: https://supastarter.dev/docs/nextjs/deployment/netlify
- Docker: https://supastarter.dev/docs/nextjs/deployment/docker
- Fly.io: https://supastarter.dev/docs/nextjs/deployment/flydotio
- Render: https://supastarter.dev/docs/nextjs/deployment/render
- Coolify: https://supastarter.dev/docs/nextjs/deployment/coolify
- Standalone API: https://supastarter.dev/docs/nextjs/deployment/standalone-api

**Codebase**
- Structure: https://supastarter.dev/docs/nextjs/codebase/structure
- Dependencies: https://supastarter.dev/docs/nextjs/codebase/dependencies
- Formatting & Linting: https://supastarter.dev/docs/nextjs/codebase/formatting-and-linting
- Local Development: https://supastarter.dev/docs/nextjs/codebase/local-development
- VSCode Setup: https://supastarter.dev/docs/nextjs/codebase/vscode
- Update supastarter: https://supastarter.dev/docs/nextjs/codebase/update
- Dependabot: https://supastarter.dev/docs/nextjs/codebase/dependabot

**Other Features**
- Blog: https://supastarter.dev/docs/nextjs/blog
- Documentation Pages: https://supastarter.dev/docs/nextjs/documentation
- Internationalization: https://supastarter.dev/docs/nextjs/internationalization
- E2E Testing: https://supastarter.dev/docs/nextjs/e2e

**Recipes**
- Build a Feedback Widget: https://supastarter.dev/docs/nextjs/recipes/build-a-feedback-widget
- Supabase Setup: https://supastarter.dev/docs/nextjs/recipes/supabase-setup

### Nuxt Documentation

**Getting Started**
- Introduction: https://supastarter.dev/docs/nuxt
- Setup Guide: https://supastarter.dev/docs/nuxt/setup
- Tech Stack: https://supastarter.dev/docs/nuxt/tech-stack
- Troubleshooting: https://supastarter.dev/docs/nuxt/troubleshooting

**Authentication**
- Overview: https://supastarter.dev/docs/nuxt/authentication/overview
- OAuth Providers: https://supastarter.dev/docs/nuxt/authentication/oauth
- Permissions: https://supastarter.dev/docs/nuxt/authentication/permissions
- Superadmin: https://supastarter.dev/docs/nuxt/authentication/superadmin
- Teams: https://supastarter.dev/docs/nuxt/authentication/teams

**API Layer**
- Overview: https://supastarter.dev/docs/nuxt/api/overview
- Define Endpoints: https://supastarter.dev/docs/nuxt/api/define-endpoint
- Usage in Frontend: https://supastarter.dev/docs/nuxt/api/usage-in-frontend

**Database**
- Overview: https://supastarter.dev/docs/nuxt/database/overview
- Database Client: https://supastarter.dev/docs/nuxt/database/client
- Update Schema: https://supastarter.dev/docs/nuxt/database/update-schema

**Billing**
- Overview: https://supastarter.dev/docs/nuxt/billing/overview
- Stripe: https://supastarter.dev/docs/nuxt/billing/stripe
- LemonSqueezy: https://supastarter.dev/docs/nuxt/billing/lemonsqueezy
- Creem: https://supastarter.dev/docs/nuxt/billing/creem

**Email/Mailing**
- Overview: https://supastarter.dev/docs/nuxt/mailing/overview
- Resend: https://supastarter.dev/docs/nuxt/mailing/resend
- Postmark: https://supastarter.dev/docs/nuxt/mailing/postmark
- Plunk: https://supastarter.dev/docs/nuxt/mailing/plunk
- Nodemailer: https://supastarter.dev/docs/nuxt/mailing/nodemailer
- Custom Provider: https://supastarter.dev/docs/nuxt/mailing/custom

**Analytics**
- Overview: https://supastarter.dev/docs/nuxt/analytics/overview
- Google Analytics: https://supastarter.dev/docs/nuxt/analytics/google
- Mixpanel: https://supastarter.dev/docs/nuxt/analytics/mixpanel
- Plausible: https://supastarter.dev/docs/nuxt/analytics/plausible
- Pirsch: https://supastarter.dev/docs/nuxt/analytics/pirsch
- Umami: https://supastarter.dev/docs/nuxt/analytics/umami
- Vercel Analytics: https://supastarter.dev/docs/nuxt/analytics/vercel
- Custom Analytics: https://supastarter.dev/docs/nuxt/analytics/custom

**Customization**
- Overview: https://supastarter.dev/docs/nuxt/customization/overview
- Styling: https://supastarter.dev/docs/nuxt/customization/styling

**Codebase**
- Structure: https://supastarter.dev/docs/nuxt/codebase/structure
- Dependencies: https://supastarter.dev/docs/nuxt/codebase/dependencies
- VSCode Setup: https://supastarter.dev/docs/nuxt/codebase/vscode
- Update supastarter: https://supastarter.dev/docs/nuxt/codebase/update

**Other Features**
- Blog: https://supastarter.dev/docs/nuxt/blog
- Documentation Pages: https://supastarter.dev/docs/nuxt/documentation
- Storage: https://supastarter.dev/docs/nuxt/storage
- Internationalization: https://supastarter.dev/docs/nuxt/internationalization
- Deployment: https://supastarter.dev/docs/nuxt/deployment

### SvelteKit Documentation

**Getting Started**
- Introduction: https://supastarter.dev/docs/sveltekit
- Setup Guide: https://supastarter.dev/docs/sveltekit/setup
- Tech Stack: https://supastarter.dev/docs/sveltekit/tech-stack
- Troubleshooting: https://supastarter.dev/docs/sveltekit/troubleshooting

**Authentication**
- Overview: https://supastarter.dev/docs/sveltekit/authentication/overview
- OAuth Providers: https://supastarter.dev/docs/sveltekit/authentication/oauth
- Permissions: https://supastarter.dev/docs/sveltekit/authentication/permissions
- Superadmin: https://supastarter.dev/docs/sveltekit/authentication/superadmin
- Teams: https://supastarter.dev/docs/sveltekit/authentication/teams

**API Layer**
- Overview: https://supastarter.dev/docs/sveltekit/api/overview
- Define Endpoints: https://supastarter.dev/docs/sveltekit/api/define-endpoint
- Mutations: https://supastarter.dev/docs/sveltekit/api/mutations
- Usage in Frontend: https://supastarter.dev/docs/sveltekit/api/usage-in-frontend

**Database**
- Overview: https://supastarter.dev/docs/sveltekit/database/overview
- Database Client: https://supastarter.dev/docs/sveltekit/database/client
- Update Schema: https://supastarter.dev/docs/sveltekit/database/update-schema

**Billing**
- Overview: https://supastarter.dev/docs/sveltekit/billing/overview
- Stripe: https://supastarter.dev/docs/sveltekit/billing/stripe
- LemonSqueezy: https://supastarter.dev/docs/sveltekit/billing/lemonsqueezy

**Email/Mailing**
- Overview: https://supastarter.dev/docs/sveltekit/mailing/overview
- Resend: https://supastarter.dev/docs/sveltekit/mailing/resend
- Postmark: https://supastarter.dev/docs/sveltekit/mailing/postmark
- Plunk: https://supastarter.dev/docs/sveltekit/mailing/plunk
- Nodemailer: https://supastarter.dev/docs/sveltekit/mailing/nodemailer
- Custom Provider: https://supastarter.dev/docs/sveltekit/mailing/custom

**Analytics**
- Overview: https://supastarter.dev/docs/sveltekit/analytics/overview
- Google Analytics: https://supastarter.dev/docs/sveltekit/analytics/google
- Mixpanel: https://supastarter.dev/docs/sveltekit/analytics/mixpanel
- Plausible: https://supastarter.dev/docs/sveltekit/analytics/plausible
- Pirsch: https://supastarter.dev/docs/sveltekit/analytics/pirsch
- Umami: https://supastarter.dev/docs/sveltekit/analytics/umami
- Vercel Analytics: https://supastarter.dev/docs/sveltekit/analytics/vercel
- Custom Analytics: https://supastarter.dev/docs/sveltekit/analytics/custom

**Customization**
- Overview: https://supastarter.dev/docs/sveltekit/customization/overview
- Styling: https://supastarter.dev/docs/sveltekit/customization/styling
- Dashboard: https://supastarter.dev/docs/sveltekit/customization/dashboard

**Codebase**
- Structure: https://supastarter.dev/docs/sveltekit/codebase/structure
- Dependencies: https://supastarter.dev/docs/sveltekit/codebase/dependencies
- VSCode Setup: https://supastarter.dev/docs/sveltekit/codebase/vscode
- Update supastarter: https://supastarter.dev/docs/sveltekit/codebase/update

**Other Features**
- Blog: https://supastarter.dev/docs/sveltekit/blog
- Documentation Pages: https://supastarter.dev/docs/sveltekit/documentation
- Storage: https://supastarter.dev/docs/sveltekit/storage
- Deployment: https://supastarter.dev/docs/sveltekit/deployment

## Additional Resources

- Website: https://supastarter.dev
- GitHub (Next.js): https://github.com/supastarter/supastarter-nextjs
- Documentation Download: https://supastarter.dev/nextjs-docs.zip

## Principles

- Focus on Developer Experience (DX)
- Fully typed with TypeScript
- Modular & Extensible architecture
- Fully customizable to your needs
- Production-ready from day one
- Scalable infrastructure
- Serverless-friendly

## Use Cases

supastarter is perfect for:
- SaaS applications
- Multi-tenant platforms
- Subscription-based services
- B2B applications
- Membership sites
- API-first applications
- AI-powered applications
- Any production-ready web application requiring authentication, payments, and scalability
