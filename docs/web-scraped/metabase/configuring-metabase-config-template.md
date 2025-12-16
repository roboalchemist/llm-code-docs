# Source: https://www.metabase.com/docs/latest/configuring-metabase/config-template

<div>

1.  [Home](/docs/latest/)
2.  [Configuring Metabase](/docs/latest/configuring-metabase/start)

</div>

<div>

[ v0.57 ![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzIiIGhlaWdodD0iMzIiIHZpZXdib3g9IjAgMCAzMiAzMiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBjbGFzcz0iY2hldnJvbiI+CjxwYXRoIG9wYWNpdHk9IjAuOSIgZD0iTTMgOC45NjMzOEwxNiAyMS45NjM0TDI5IDguOTYzMzgiIHN0cm9rZT0iIzUwOWVlMyIgc3Ryb2tlLXdpZHRoPSI1IiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiPjwvcGF0aD4KPC9zdmc+) ]

-   [v0.56](/docs/v0.56)
-   [v0.55](/docs/v0.55)
-   [v0.54](/docs/v0.54)
-   [v0.53](/docs/v0.53)
-   [v0.52](/docs/v0.52)
-   [v0.51](/docs/v0.51)
-   [v0.50](/docs/v0.50)
-   [v0.49](/docs/v0.49)
-   [v0.48](/docs/v0.48)
-   [See more](/docs/all)

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgdmlld2JveD0iMCAwIDI0IDI0IiBmaWxsPSJub25lIj48cGF0aCBzdHJva2U9IiM1MDlFRTMiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIxLjUiIGQ9Ik0xNi4yODMgMTIuMjYgMTUuNSAxNWwtLjc4My0yLjc0YTQuMzMzIDQuMzMzIDAgMCAwLTIuOTc1LTIuOTc2TDkgOC41bDIuNzQtLjc4M2E0LjMzMyA0LjMzMyAwIDAgMCAyLjk3Ni0yLjk3NUwxNS41IDJsLjc4MyAyLjc0YTQuMzMzIDQuMzMzIDAgMCAwIDIuOTc1IDIuOTc2TDIyIDguNWwtMi43NC43ODNhNC4zMzQgNC4zMzQgMCAwIDAtMi45NzYgMi45NzVsLS4wMDEuMDAxWk02LjUgMjJsLjU5MS0xLjc3NGEzLjM3NSAzLjM3NSAwIDAgMSAyLjEzNS0yLjEzNUwxMSAxNy41bC0xLjc3NC0uNTkxYTMuMzc1IDMuMzc1IDAgMCAxLTIuMTM1LTIuMTM0TDYuNSAxM2wtLjU5MSAxLjc3NGEzLjM3NSAzLjM3NSAwIDAgMS0yLjEzNCAyLjEzNUwyIDE3LjVsMS43NzUuNTkxYTMuMzc1IDMuMzc1IDAgMCAxIDIuMTM0IDIuMTM0TDYuNSAyMloiPjwvcGF0aD48L3N2Zz4=) What's new](/releases)

</div>

<div>

</div>

# Metabase config file template

You can generate this doc page by changing into the top-level Metabase directory and running:

``` highlight
clojure -M:doc:ee config-template
```

The template lists example `database`, `user`, and `settings` sections for the [config file](./config-file).

``` highlight
# A config file template for Metabase.
# You'll need to update (or remove) the `users` and `databases` sections.
# The settings in `settings` include default values. We recommend removing
# or commenting out settings that you don't set.
# To use an env var, you can use a template string: ""
# Note the quote marks wrapping the env var template.
# For more on the configuration file, see:
# https://www.metabase.com/docs/latest/configuring-metabase/config-file
# For more on what each setting does, check out:
# https://www.metabase.com/docs/latest/configuring-metabase/environment-variables
version: 1
config:
  users:
  - first_name: First
    last_name: Person
    password: metabot1
    email: first@example.com
  - first_name: Normal
    last_name: Person
    password: metabot1
    email: normal@example.com
  - first_name: Admin
    last_name: Person
    password: metabot1
    is_superuser: true
    email: admin@example.com
  databases:
  - name: Sample PostgreSQL
    engine: postgres
    details:
      host: postgres-data
      port: 5432
      user: metabase
      password: metasample123
      dbname: sample
  - name: Sample MySQL
    engine: mysql
    details:
      host: mysql-data
      port: 3306
      user: metabase
      password: metasample123
      dbname: sample
  api-keys:
  - name: Admin API key
    group: admin
    creator: first@example.com
    key: mb_firsttestapikey123
  - name: All Users API key
    group: all-users
    creator: first@example.com
    key: mb_secondtestapikey456
  settings:
    admin-email: null
    aggregated-query-row-limit: null
    allowed-iframe-hosts: |-
      youtube.com,
      youtu.be,
      loom.com,
      vimeo.com,
      docs.google.com,
      calendar.google.com,
      airtable.com,
      typeform.com,
      canva.com,
      codepen.io,
      figma.com,
      grafana.com,
      miro.com,
      excalidraw.com,
      notion.com,
      atlassian.com,
      trello.com,
      asana.com,
      gist.github.com,
      linkedin.com,
      twitter.com,
      x.com
    anon-tracking-enabled: true
    api-key: null
    application-colors: 
    application-favicon-url: app/assets/img/favicon.ico
    application-font: Lato
    application-font-files: null
    application-logo-url: app/assets/img/logo.svg
    application-name: Metabase
    attachment-row-limit: null
    attachment-table-row-limit: 20
    audit-max-retention-days: null
    bcc-enabled: true
    breakout-bin-width: 10.0
    breakout-bins-num: 8
    check-for-updates: true
    config-from-file-sync-databases: true
    custom-formatting: 
    custom-geojson: null
    custom-geojson-enabled: true
    custom-homepage: false
    custom-homepage-dashboard: null
    dashboards-save-last-used-parameters: true
    db-connection-timeout-ms: 10000
    db-query-timeout-minutes: 20
    default-maps-enabled: true
    disable-cors-on-localhost: false
    download-row-limit: null
    email-from-address: notifications@metabase.com
    email-from-address-override: notifications@metabase.com
    email-from-name: null
    email-max-recipients-per-second: null
    email-reply-to: null
    email-smtp-host: null
    email-smtp-host-override: null
    email-smtp-password: null
    email-smtp-password-override: null
    email-smtp-port: null
    email-smtp-port-override: null
    email-smtp-security: none
    email-smtp-security-override: ssl
    email-smtp-username: null
    email-smtp-username-override: null
    embedding-app-origins-interactive: null
    embedding-app-origins-sdk: ''
    embedding-homepage: hidden
    embedding-secret-key: null
    enable-embedding-interactive: false
    enable-embedding-sdk: false
    enable-embedding-simple: false
    enable-embedding-static: false
    enable-password-login: true
    enable-pivoted-exports: true
    enable-public-sharing: true
    enable-query-caching: true
    enable-xrays: true
    follow-up-email-sent: false
    google-auth-auto-create-accounts-domain: null
    google-auth-client-id: null
    google-auth-enabled: null
    gsheets: null
    health-check-logging-enabled: true
    help-link: metabase
    help-link-custom-destination: https://www.metabase.com/help/premium
    hide-stacktraces: false
    http-channel-host-strategy: external-only
    humanization-strategy: simple
    index-update-thread-count: 2
    install-analytics-database: true
    jdbc-data-warehouse-max-connection-pool-size: 15
    jwt-attribute-email: email
    jwt-attribute-firstname: first_name
    jwt-attribute-groups: groups
    jwt-attribute-lastname: last_name
    jwt-enabled: false
    jwt-group-mappings: 
    jwt-group-sync: false
    jwt-identity-provider-uri: null
    jwt-shared-secret: null
    jwt-user-provisioning-enabled: true
    landing-page: ''
    landing-page-illustration: default
    landing-page-illustration-custom: null
    ldap-attribute-email: mail
    ldap-attribute-firstname: givenName
    ldap-attribute-lastname: sn
    ldap-bind-dn: null
    ldap-enabled: false
    ldap-group-base: null
    ldap-group-mappings: 
    ldap-group-membership-filter: (member=)
    ldap-group-sync: false
    ldap-host: null
    ldap-password: null
    ldap-port: 389
    ldap-security: none
    ldap-sync-user-attributes: true
    ldap-sync-user-attributes-blacklist: userPassword,dn,distinguishedName
    ldap-timeout-seconds: 15.0
    ldap-user-base: null
    ldap-user-filter: (&(objectClass=inetOrgPerson)(|(uid=)(mail=)))
    ldap-user-provisioning-enabled: true
    license-token-missing-banner-dismissal-timestamp: []
    load-analytics-content: true
    loading-message: doing-science
    login-page-illustration: default
    login-page-illustration-custom: null
    map-tile-server-url: https://.tile.openstreetmap.org///.png
    native-query-autocomplete-match-style: substring
    nested-field-columns-value-length-limit: 50000
    no-data-illustration: default
    no-data-illustration-custom: null
    no-object-illustration: default
    no-object-illustration-custom: null
    non-table-chart-generated: false
    not-behind-proxy: false
    notification-link-base-url: null
    notification-system-event-thread-pool-size: 5
    notification-temp-file-size-max-bytes: 10485760
    notification-thread-pool-size: 3
    persisted-model-refresh-cron-schedule: 0 0 0/6 * * ? *
    persisted-models-enabled: false
    premium-embedding-token: null
    query-caching-max-kb: 2000
    query-caching-max-ttl: 3024000.0
    redirect-all-requests-to-https: false
    remote-sync-auto-import: false
    remote-sync-auto-import-rate: 5
    remote-sync-branch: null
    remote-sync-task-time-limit-ms: 300000
    remote-sync-token: null
    remote-sync-type: production
    remote-sync-url: null
    report-timezone: null
    reset-token-ttl-hours: 48
    retry-initial-interval: 500
    retry-jitter-factor: 0.1
    retry-max-interval-millis: 30000
    retry-max-retries: 6
    retry-multiplier: 2.0
    saml-application-name: Metabase
    saml-attribute-email: null
    saml-attribute-firstname: http://schemas.xmlsoap.org/ws/2005/05/identity/claims/givenname
    saml-attribute-group: null
    saml-attribute-lastname: http://schemas.xmlsoap.org/ws/2005/05/identity/claims/surname
    saml-enabled: false
    saml-group-mappings: 
    saml-group-sync: false
    saml-identity-provider-certificate: null
    saml-identity-provider-issuer: null
    saml-identity-provider-slo-uri: null
    saml-identity-provider-uri: null
    saml-keystore-alias: null
    saml-keystore-password: changeit
    saml-keystore-path: null
    saml-slo-enabled: false
    saml-user-provisioning-enabled: true
    scim-enabled: null
    sdk-encryption-validation-key: null
    search-language: null
    search-typeahead-enabled: true
    send-email-on-first-login-from-new-device: true
    send-new-sso-user-admin-email: null
    session-cookie-samesite: lax
    session-cookies: null
    session-timeout: null
    setup-embedding-autoenabled: false
    setup-license-active-at-setup: false
    show-database-syncing-modal: null
    show-google-sheets-integration: null
    show-homepage-data: true
    show-homepage-xrays: true
    show-metabase-links: true
    show-static-embed-terms: true
    site-locale: en
    site-name: Metabase
    site-url: null
    slack-app-token: null
    slack-bug-report-channel: metabase-bugs
    smtp-override-enabled: false
    source-address-header: X-Forwarded-For
    sql-jdbc-fetch-size: 500
    ssh-heartbeat-interval-sec: 180
    start-of-week: sunday
    subscription-allowed-domains: null
    surveys-enabled: true
    sync-leaf-fields-limit: 1000
    synchronous-batch-updates: false
    unaggregated-query-row-limit: null
    uploads-settings: null
    use-tenants: false
    user-visibility: all
```

<div>

Read docs for other [versions of Metabase](/docs/all).

</div>

###### Was this helpful?

![](data:image/svg+xml;base64,PHN2ZyBpZCBjbGFzcz0ibWUtMSIgd2lkdGg9IjE4IiBoZWlnaHQ9IjE4IiB2aWV3Ym94PSIwIDAgMjQgMjQiIGZpbGw9Im5vbmUiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CiAgICA8cGF0aCBkPSJNMTAuNjY2NyA3LjMzMzMzSDE0LjYzNjdDMTQuOTIwNyA3LjMzMzM0IDE1LjIwMDEgNy40MDU5NSAxNS40NDgyIDcuNTQ0MjdDMTUuNjk2MyA3LjY4MjU5IDE1LjkwNDkgNy44ODIwMiAxNi4wNTQzIDguMTIzNjRDMTYuMjAzNiA4LjM2NTI1IDE2LjI4ODggOC42NDEwNCAxNi4zMDE2IDguOTI0OEMxNi4zMTQ0IDkuMjA4NTcgMTYuMjU0NSA5LjQ5MDkgMTYuMTI3NSA5Ljc0NUwxMy4yMTA4IDE1LjU3ODNDMTMuMDcyNCAxNS44NTU0IDEyLjg1OTUgMTYuMDg4NCAxMi41OTYgMTYuMjUxMkMxMi4zMzI1IDE2LjQxNCAxMi4wMjg5IDE2LjUwMDEgMTEuNzE5MiAxNi41SDguMzcxNjdDOC4yMzU4MyAxNi41IDguMSAxNi40ODMzIDcuOTY3NSAxNi40NUw0LjgzMzMzIDE1LjY2NjdNMTAuNjY2NyA3LjMzMzMzVjMuMTY2NjdDMTAuNjY2NyAyLjcyNDY0IDEwLjQ5MTEgMi4zMDA3MiAxMC4xNzg1IDEuOTg4MTZDOS44NjU5NSAxLjY3NTU5IDkuNDQyMDMgMS41IDkgMS41SDguOTIwODNDOC41MDQxNyAxLjUgOC4xNjY2NyAxLjgzNzUgOC4xNjY2NyAyLjI1NDE3QzguMTY2NjcgMi44NDkxNyA3Ljk5MDgzIDMuNDMwODMgNy42NiAzLjkyNTgzTDQuODMzMzMgOC4xNjY2N1YxNS42NjY3TTEwLjY2NjcgNy4zMzMzM0g5TTQuODMzMzMgMTUuNjY2N0gzLjE2NjY3QzIuNzI0NjQgMTUuNjY2NyAyLjMwMDcyIDE1LjQ5MTEgMS45ODgxNiAxNS4xNzg1QzEuNjc1NTkgMTQuODY2IDEuNSAxNC40NDIgMS41IDE0VjlDMS41IDguNTU3OTcgMS42NzU1OSA4LjEzNDA1IDEuOTg4MTYgNy44MjE0OUMyLjMwMDcyIDcuNTA4OTMgMi43MjQ2NCA3LjMzMzMzIDMuMTY2NjcgNy4zMzMzM0g1LjI1IiBzdHJva2U9IiM1MDllZTMiIHN0cm9rZS13aWR0aD0iMS41IiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiPjwvcGF0aD4KPC9zdmc+) Yes

![](data:image/svg+xml;base64,PHN2ZyBpZCBjbGFzcz0icm90YXRlLTE4MCBtZS0xIiB3aWR0aD0iMTgiIGhlaWdodD0iMTgiIHZpZXdib3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICAgIDxwYXRoIGQ9Ik0xMC42NjY3IDcuMzMzMzNIMTQuNjM2N0MxNC45MjA3IDcuMzMzMzQgMTUuMjAwMSA3LjQwNTk1IDE1LjQ0ODIgNy41NDQyN0MxNS42OTYzIDcuNjgyNTkgMTUuOTA0OSA3Ljg4MjAyIDE2LjA1NDMgOC4xMjM2NEMxNi4yMDM2IDguMzY1MjUgMTYuMjg4OCA4LjY0MTA0IDE2LjMwMTYgOC45MjQ4QzE2LjMxNDQgOS4yMDg1NyAxNi4yNTQ1IDkuNDkwOSAxNi4xMjc1IDkuNzQ1TDEzLjIxMDggMTUuNTc4M0MxMy4wNzI0IDE1Ljg1NTQgMTIuODU5NSAxNi4wODg0IDEyLjU5NiAxNi4yNTEyQzEyLjMzMjUgMTYuNDE0IDEyLjAyODkgMTYuNTAwMSAxMS43MTkyIDE2LjVIOC4zNzE2N0M4LjIzNTgzIDE2LjUgOC4xIDE2LjQ4MzMgNy45Njc1IDE2LjQ1TDQuODMzMzMgMTUuNjY2N00xMC42NjY3IDcuMzMzMzNWMy4xNjY2N0MxMC42NjY3IDIuNzI0NjQgMTAuNDkxMSAyLjMwMDcyIDEwLjE3ODUgMS45ODgxNkM5Ljg2NTk1IDEuNjc1NTkgOS40NDIwMyAxLjUgOSAxLjVIOC45MjA4M0M4LjUwNDE3IDEuNSA4LjE2NjY3IDEuODM3NSA4LjE2NjY3IDIuMjU0MTdDOC4xNjY2NyAyLjg0OTE3IDcuOTkwODMgMy40MzA4MyA3LjY2IDMuOTI1ODNMNC44MzMzMyA4LjE2NjY3VjE1LjY2NjdNMTAuNjY2NyA3LjMzMzMzSDlNNC44MzMzMyAxNS42NjY3SDMuMTY2NjdDMi43MjQ2NCAxNS42NjY3IDIuMzAwNzIgMTUuNDkxMSAxLjk4ODE2IDE1LjE3ODVDMS42NzU1OSAxNC44NjYgMS41IDE0LjQ0MiAxLjUgMTRWOUMxLjUgOC41NTc5NyAxLjY3NTU5IDguMTM0MDUgMS45ODgxNiA3LjgyMTQ5QzIuMzAwNzIgNy41MDg5MyAyLjcyNDY0IDcuMzMzMzMgMy4xNjY2NyA3LjMzMzMzSDUuMjUiIHN0cm9rZT0iIzUwOWVlMyIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCI+PC9wYXRoPgo8L3N2Zz4=) No

Send

###### Thanks for your feedback! 

[ Want to improve these docs? [Propose a change.](https://github.com/metabase/metabase/blob/master/docs/configuring-metabase/config-template.md) ]