# Source: https://www.apollographql.com/docs/graphos/schema-design/guides/sdui/schema-design.md

# Server-Driven UI Schema Design

If you're an enterprise customer looking for more material on this topic, try the [Enterprise best practices: Schema design](https://www.apollographql.com/tutorials/schema-design-best-practices) course on Odyssey.

Not an enterprise customer? [Learn about GraphOS for Enterprise.](https://www.apollographql.com/pricing?referrer=docs-content)

These patterns provide examples of server-driven UI (SDUI) and how to structure your graph's schema to encode and represent UI elements. Clients can then use platform-specific rendering engines to interpret the schema and generate UI components.

For more information on SDUI in general, see [Server-driven UI basics](https://www.apollographql.com/docs/graphos/schema-design/guides/sdui/basics).

## Device-based SDUI with enums

Different devices (for example, mobile, web, Roku, Apple TV) may require different UI layouts or components. You can use enums for device type lists to declare which UI type to retrieve.

```graphql
enum UIDeviceType {
  MOBILE
  WEB
  ROKU
  APPLETV
}

interface UIApp {}

type WebApp implements UIApp {}
type IOSApp implements UIApp {}
type AndroidApp implements UIApp {}
type AppleTVApp implements UIApp {}
type RokuApp implements UIApp {}

type Query {
  app(type: UIDeviceType! = WEB): UIApp!
}
```

In this example, the `UIDeviceType` enum lets you specify the type of device you want to retrieve the `UIApp` for.

## Device-based SDUI with contracts

You can use a similar device-based SDUI with [contracts](https://www.apollographql.com/docs/graphos/platform/schema-management/delivery/contracts/overview) to remove UI components that are unrelated to the target platform from your schema.

```graphql
type UIApp {
  spotlight: UISpotlightComponent @tag(name: "DESKTOP")
  dashboard: UIDashboardComponent
  mobileMenu: UIMenuComponent @tag(name: "MOBILE")
  menu: UIMenuComponent @tag(name: "WEB")
}

type Query {
  app: UIApp!
}
```

Read more on [contracts usage patterns](https://www.apollographql.com/docs/graphos/platform/schema-management/delivery/contracts/usage-patterns).

## SDUI web dashboard

The following example shows a schema with a static structure that clients can use to create a web dashboard UI.

```graphql
type AppLogo {
  url: String
  alt: String
}

type AppLink {
  icon: String
  label: String
  path: String
}

type AppUserMenu {
  user: User
}

type AppNavbar {
  logo: AppLogo
  items: [AppLink]
  user: AppUserMenu
}

type AppMobileMenu {
  items: [AppLink]
  user: AppUserMenu
}

type AppHomePage {
  recommended: [AppLink]
}

type WebApp {
  navbar: AppNavbar
  menu: AppMobileMenu
  home: AppHomePage
  settings: AppSettingsPage
  profile: AppProfilePage
}

type Query {
  app: WebApp!
}
```

## SDUI web dashboard using interfaces

The example schema below is also for a web dashboard UI, but it uses [interfaces](https://www.apollographql.com/docs/apollo-server/schema/unions-interfaces/#interface-type) to construct dynamic responses for the UI. By using interfaces, an "experience" subgraph can dynamically return different UI components.

```graphql
interface UIComponent {
  id: ID
}

type UILogo implements UIComponent {
  id: ID
  url: String
  alt: String
}

interface UINavbarItem implements UIComponent {
  id: ID
  label: String
  path: String
  icon: String
}

interface UINavbar implements UIComponent {
  id: ID
  logo: UILogo
  items: [UINavbarItem]
}

interface UIMenuItem implements UIComponent {
  id: ID
  label: String
  path: String
  icon: String
}

interface UIMenu implements UIComponent {
  id: ID
  logo: UILogo
  items: [UIMenuItem]
}

interface UISidebar implements UIComponent {
  id: ID
  title: String
  content: [UIComponent]
}

interface UILayout implements UIComponent {
  id: ID
  content: [UIComponent]
}

interface UIScreen implements UIComponent {
  id: ID
  current: UIPage
  navbar: UINavbar
  menu: UIMenu
  main: UILayout
  sidebar: UISidebar
}

enum UIPage {
  HOME
  DASHBOARD
  SETTINGS
}

type Query {
  app(page: UIPage!): UIScreen!
}
```
