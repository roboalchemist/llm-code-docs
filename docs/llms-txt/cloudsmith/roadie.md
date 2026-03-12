# Source: https://help.cloudsmith.io/docs/roadie.md

# Roadie (Backstage)

How to integrate Roadie (Backstage) with Cloudsmith

<Image align="center" border={false} src="https://files.readme.io/e1cd016-cloudsmith-roadie-partner-banner.png" />

<Anchor label="Roadie (Backstage)" target="_blank" href="https://roadie.io/">Roadie (Backstage)</Anchor> is a service catalog platform that allows users to integrate a number of different APIs into one dashboard for ease of tracking key metrics in one place. Roadie currently has many <Anchor label="available plugins" target="_blank" href="https://roadie.io/backstage/plugins/">available plugins</Anchor> and we are happy to announce that Cloudsmith is one of them. An example picture of what is possible to have displayed through this integration:

<Image border={false} src="https://files.readme.io/8ae2f47-210829090-6a2c7da5-12b4-4702-92f0-0093f87887ef.png" title="210829090-6a2c7da5-12b4-4702-92f0-0093f87887ef.png" />

# Getting Started:

In order to get started please visit Roadie's [GitHub Page](https://github.com/cloudsmith-io/roadie-backstage-plugins#getting-started) and follow the steps of spinning up your own open-source instance.

Once setup and running, you can add Cloudsmith Plugins by inserting them into `packages/app/src/components/home/HomePage.tsx`.

**There are currently 4 available plugins:&#xA;**

### **CloudsmithStatsCard:**

Displays how many packages are in use/inactive in the provided repository

<Image align="center" alt={1016} border={false} caption="Repository Stats" title="Screenshot 2022-12-27 at 16.43.20.png" src="https://files.readme.io/5724e07-Screenshot_2022-12-27_at_16.43.20.png" />

### **CloudsmithQuotaCard:**

Displays the current bandwidth and storage usage and how much is available.

<Image align="center" alt={876} border={false} caption="Repository Stats" title="Screenshot 2023-01-05 at 16.51.30.png" src="https://files.readme.io/15a8d3d-Screenshot_2023-01-05_at_16.51.30.png" />

### **CloudsmithRepositoryAuditLogCard:**

Displays audit logs for a specified repository.

<Image align="center" alt={3064} border={false} caption="Repository Audit Logs" title="Screenshot 2022-12-27 at 16.45.10.png" src="https://files.readme.io/0113d2f-Screenshot_2022-12-27_at_16.45.10.png" />

### **CloudsmithRepositorySecurityCard:**

Displays Medium to Critical vulnerabilities found in a specified repository.

<Image align="center" alt={1486} border={false} caption="Repository Security Scan Results" title="Screenshot 2022-12-27 at 16.46.16.png" src="https://files.readme.io/ec22797-Screenshot_2022-12-27_at_16.46.16.png" />

***

## Integration

In order to use the plugins import them into `HomePage.tsx`:

```typescript
import { CloudsmithStatsCard, CloudsmithQuotaCard, CloudsmithRepositoryAuditLogCard, CloudsmithRepositorySecurityCard } from '@roadiehq/backstage-plugin-cloudsmith';
```

Once imported you can add them to your grid:

```typescript
<Grid  item  xs={12}  md={6}>
   <CloudsmithStatsCard  repo="repo-name"  owner="org-name"  />
</Grid>

<Grid  item  xs={12}  md={6}>
   <CloudsmithQuotaCard  owner='org-name'/>
</Grid>

<Grid  item  xs={12}  md={6}>
   <CloudsmithRepositoryAuditLogCard  owner='org-name'  repo='repo-name'/>
</Grid>

<Grid  item  xs={12}  md={6}>
   <CloudsmithRepositorySecurityCard  owner='org-name'  repo='repo-name'/>
</Grid>
```

You can add multiple elements by copying and pasting the code above and changing `CloudsmithStatsCard`. Some elements will only require `owner` field and the syntax should highlight in red that it only takes one argument.

Then you can edit the  `app-config.yaml`  for the backstage backend application, adding the following proxy configuration.

```
...
proxy:
  ...
  '/cloudsmith':
    target: 'https://api.cloudsmith.io/v1'
    headers:
      X-Api-Key: ${CLOUDSMITH_API_KEY}
```

When you run the backstage backend, you will need to set the  `CLOUDSMITH_API_KEY`  environment variable.