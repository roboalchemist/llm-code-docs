# Source: https://docs.xano.com/troubleshooting-and-support/plan-comparison-refactor.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Plan Comparison

> Understand how legacy plans (Starter, Launch, Scale) map to the current lineup (Free, Essential, Pro).

export const PLAN_META = {
  free: {
    label: "Free",
    status: "current"
  },
  starter_legacy: {
    label: "Starter (legacy $29)",
    status: "legacy"
  },
  launch_legacy: {
    label: "Launch (legacy)",
    status: "legacy"
  },
  essential: {
    label: "Essential",
    status: "current"
  },
  pro: {
    label: "Pro",
    status: "current"
  }
};


export const OVERVIEW_ROWS = [{
  "label": "Infrastructure",
  "values": {
    "free": "Shared Infrastructure",
    "starter_legacy": "Standalone, but not guaranteed \"Dedicated\"",
    "launch_legacy": "100% Dedicated",
    "essential": "100% Dedicated",
    "pro": "100% Dedicated"
  }
}, {
  "label": "Price",
  "values": {
    "free": "$0",
    "starter_legacy": "Monthly - $29/workspace\nAnnual - $25/month or $300/year",
    "launch_legacy": "$99/month\n$85/month ($1020) for annual",
    "essential": "$99/month\n$85/month ($1020) for annual",
    "pro": "$249/month\n$224/month ($$2,688) for annual"
  }
}];


export const MATRIX_SECTIONS = [{
  "title": "Limits",
  "rows": [{
    "label": "Rate Limit",
    "values": {
      "free": "10 req/ 20 s",
      "starter_legacy": "No limit",
      "launch_legacy": "No limit",
      "essential": "No limit",
      "pro": "No limit"
    }
  }, {
    "label": "CPU",
    "values": {
      "free": "Shared resources",
      "starter_legacy": "1 CPU included\nWITH BOOST: 2 CPU for an additional $70/month or $720/year",
      "launch_legacy": "3 CPU",
      "essential": "3 CPU",
      "pro": "Same as Scale included\nBOOST = 2x Scale for an additional $180/month or $2160/year"
    }
  }, {
    "label": "Image Watermark",
    "values": {
      "free": "Image Watermark",
      "starter_legacy": "No Watermark",
      "launch_legacy": "No Watermark",
      "essential": "No Watermark",
      "pro": "No Watermark"
    }
  }, {
    "label": "Database Records",
    "values": {
      "free": "100,000",
      "starter_legacy": "No limit",
      "launch_legacy": "No limit",
      "essential": "No limit",
      "pro": "No limit"
    }
  }, {
    "label": "Load Balanced",
    "values": {
      "free": "no",
      "starter_legacy": "no",
      "launch_legacy": "no",
      "essential": "no",
      "pro": "yes"
    }
  }, {
    "label": "Auto Scaling",
    "values": {
      "free": "no",
      "starter_legacy": "no",
      "launch_legacy": "no",
      "essential": "no",
      "pro": "no"
    }
  }]
}, {
  "title": "Key Features",
  "rows": [{
    "label": "Deployment",
    "values": {
      "free": "US only",
      "starter_legacy": "Global regions",
      "launch_legacy": "Global regions",
      "essential": "Global regions",
      "pro": "Global regions"
    }
  }, {
    "label": "Workspaces",
    "values": {
      "free": "1",
      "starter_legacy": "1",
      "launch_legacy": "3",
      "essential": "3",
      "pro": "5"
    }
  }, {
    "label": "Team size",
    "values": {
      "free": "1",
      "starter_legacy": "1",
      "launch_legacy": "Prior to Jan 2026: 1\nAs of Jan 2026: 5",
      "essential": "5",
      "pro": "10"
    }
  }, {
    "label": "Private file storage",
    "values": {
      "free": "no",
      "starter_legacy": "no",
      "launch_legacy": "no",
      "essential": "no",
      "pro": "yes"
    }
  }]
}, {
  "title": "Security & Compliance",
  "rows": [{
    "label": "GDPR with DPA",
    "values": {
      "free": "no",
      "starter_legacy": "yes",
      "launch_legacy": "yes",
      "essential": "yes",
      "pro": "yes"
    }
  }, {
    "label": "SOC 2/3",
    "values": {
      "free": "no",
      "starter_legacy": "no",
      "launch_legacy": "yes",
      "essential": "yes",
      "pro": "yes"
    }
  }, {
    "label": "ISO 42001:2023 + ISO 27001 + ISO 9001",
    "values": {
      "free": "no",
      "starter_legacy": "no",
      "launch_legacy": "yes",
      "essential": "yes",
      "pro": "yes"
    }
  }, {
    "label": "HIPAA with BAA",
    "values": {
      "free": "no",
      "starter_legacy": "no",
      "launch_legacy": "no",
      "essential": "no",
      "pro": "paid add-on"
    }
  }, {
    "label": "HIPAA Hardened Server",
    "values": {
      "free": "no",
      "starter_legacy": "no",
      "launch_legacy": "no",
      "essential": "no",
      "pro": "paid add-on"
    }
  }, {
    "label": "HDS",
    "values": {
      "free": "no",
      "starter_legacy": "no",
      "launch_legacy": "no",
      "essential": "no",
      "pro": "paid add-on"
    }
  }, {
    "label": "Workspace Permissions (RBAC) *note that this does not impact the way you can use RBAC in your logic*",
    "values": {
      "free": "no",
      "starter_legacy": "no",
      "launch_legacy": "no",
      "essential": "no",
      "pro": "yes"
    }
  }, {
    "label": "Compliance Center",
    "values": {
      "free": "no - audit logs only",
      "starter_legacy": "no - audit logs only",
      "launch_legacy": "no - audit logs only",
      "essential": "no - audit logs only",
      "pro": "yes"
    }
  }]
}, {
  "title": "TEAM/DEVELOPMENT LIFECYCLE",
  "rows": [{
    "label": "Real-time Collaboration",
    "values": {
      "free": "yes",
      "starter_legacy": "yes",
      "launch_legacy": "yes",
      "essential": "yes",
      "pro": "yes"
    }
  }, {
    "label": "Branching and Merging",
    "values": {
      "free": "no",
      "starter_legacy": "yes",
      "launch_legacy": "yes",
      "essential": "yes",
      "pro": "yes"
    }
  }, {
    "label": "JS Lambda Functions",
    "values": {
      "free": "yes",
      "starter_legacy": "yes",
      "launch_legacy": "yes",
      "essential": "yes",
      "pro": "yes"
    }
  }, {
    "label": "Direct DB Queries",
    "values": {
      "free": "no",
      "starter_legacy": "unlimited",
      "launch_legacy": "unlimited",
      "essential": "unlimited",
      "pro": "unlimited"
    }
  }, {
    "label": "Middleware",
    "values": {
      "free": "no",
      "starter_legacy": "10",
      "launch_legacy": "Prior to July 2025: 5\nAfter July 2025: 10",
      "essential": "10",
      "pro": "unlimited"
    }
  }, {
    "label": "Unit Tests",
    "values": {
      "free": "unlimited",
      "starter_legacy": "unlimited",
      "launch_legacy": "unlimited",
      "essential": "unlimited",
      "pro": "unlimited"
    }
  }, {
    "label": "Workflow Tests",
    "values": {
      "free": "no",
      "starter_legacy": "10",
      "launch_legacy": "10",
      "essential": "10",
      "pro": "unlimited"
    }
  }, {
    "label": "Database Triggers",
    "values": {
      "free": "no",
      "starter_legacy": "unlimited",
      "launch_legacy": "unlimited",
      "essential": "unlimited",
      "pro": "unlimited"
    }
  }, {
    "label": "Cloud Storage Functions",
    "values": {
      "free": "unlimited",
      "starter_legacy": "unlimited",
      "launch_legacy": "unlimited",
      "essential": "unlimited",
      "pro": "unlimited"
    }
  }, {
    "label": "Static Hosting / Sites",
    "values": {
      "free": "1",
      "starter_legacy": "1",
      "launch_legacy": "1",
      "essential": "1",
      "pro": "3"
    }
  }]
}, {
  "title": "ACCOUNT",
  "rows": [{
    "label": "Workspaces",
    "values": {
      "free": "1",
      "starter_legacy": "1",
      "launch_legacy": "3",
      "essential": "3",
      "pro": "5"
    }
  }, {
    "label": "Team size",
    "values": {
      "free": "1",
      "starter_legacy": "1",
      "launch_legacy": "Prior to Jan 2026: 1\nAfter Jan 2026: 5",
      "essential": "5",
      "pro": "10"
    }
  }, {
    "label": "Custom Domain",
    "values": {
      "free": "no",
      "starter_legacy": "Included",
      "launch_legacy": "Included",
      "essential": "Included",
      "pro": "Included"
    }
  }]
}, {
  "title": "API",
  "rows": [{
    "label": "Visual Builder",
    "values": {
      "free": "Included",
      "starter_legacy": "Included",
      "launch_legacy": "Included",
      "essential": "Included",
      "pro": "Included"
    }
  }, {
    "label": "Webhooks",
    "values": {
      "free": "Included",
      "starter_legacy": "Included",
      "launch_legacy": "Included",
      "essential": "Included",
      "pro": "Included"
    }
  }, {
    "label": "Version History (DB Tables, API Group, Endpoints, etc)",
    "values": {
      "free": "no",
      "starter_legacy": "10",
      "launch_legacy": "10",
      "essential": "10",
      "pro": "20"
    }
  }, {
    "label": "Background Tasks",
    "values": {
      "free": "no",
      "starter_legacy": "10",
      "launch_legacy": "10",
      "essential": "10",
      "pro": "Unlimited"
    }
  }, {
    "label": "Sub-Minute Task Schedules",
    "values": {
      "free": "no",
      "starter_legacy": "no",
      "launch_legacy": "yes",
      "essential": "yes",
      "pro": "yes"
    }
  }, {
    "label": "Xano Link",
    "values": {
      "free": "no",
      "starter_legacy": "no",
      "launch_legacy": "no",
      "essential": "no",
      "pro": "yes - included, prev add-on"
    }
  }]
}, {
  "title": "DATABASE & STORAGE",
  "rows": [{
    "label": "Records",
    "values": {
      "free": "100,000",
      "starter_legacy": "No limit",
      "launch_legacy": "No limit",
      "essential": "No limit",
      "pro": "No limit"
    }
  }, {
    "label": "Database Storage (Database Size)",
    "values": {
      "free": "1GB",
      "starter_legacy": "10GB",
      "launch_legacy": "Prior to July 2025: 3GB\nAfter July 2025: 10GB",
      "essential": "10 GB",
      "pro": "25GB"
    }
  }, {
    "label": "Image/File Storage",
    "values": {
      "free": "1GB",
      "starter_legacy": "100GB",
      "launch_legacy": "Prior to July 2025: 10GB\nAfter July 2025: 100GB",
      "essential": "100GB",
      "pro": "250GB"
    }
  }, {
    "label": "File Bandwidth",
    "values": {
      "free": "64MB",
      "starter_legacy": "250GB",
      "launch_legacy": "Prior to July 2025: 25GB\nAfter July 2025: 250GB",
      "essential": "250GB",
      "pro": "250GB"
    }
  }, {
    "label": "Data Sources",
    "values": {
      "free": "no",
      "starter_legacy": "3",
      "launch_legacy": "Prior to July 2025: 2\nAfter July 2025: 3",
      "essential": "3",
      "pro": "3"
    }
  }, {
    "label": "Direct Database Connector",
    "values": {
      "free": "no",
      "starter_legacy": "add-on",
      "launch_legacy": "add-on",
      "essential": "included",
      "pro": "yes - included, prev add-on"
    }
  }]
}, {
  "title": "INTEGRATIONS",
  "rows": [{
    "label": "Public Xano Marketplace",
    "values": {
      "free": "yes",
      "starter_legacy": "yes",
      "launch_legacy": "yes",
      "essential": "yes",
      "pro": "yes"
    }
  }, {
    "label": "Snippets",
    "values": {
      "free": "yes",
      "starter_legacy": "yes",
      "launch_legacy": "yes",
      "essential": "yes",
      "pro": "yes"
    }
  }, {
    "label": "Actions",
    "values": {
      "free": "yes",
      "starter_legacy": "yes",
      "launch_legacy": "yes",
      "essential": "yes",
      "pro": "yes"
    }
  }]
}, {
  "title": "PERFORMANCE",
  "rows": [{
    "label": "Indexing",
    "values": {
      "free": "yes",
      "starter_legacy": "yes",
      "launch_legacy": "yes",
      "essential": "yes",
      "pro": "yes"
    }
  }, {
    "label": "API Response Caching",
    "values": {
      "free": "no",
      "starter_legacy": "yes",
      "launch_legacy": "yes",
      "essential": "yes",
      "pro": "yes"
    }
  }, {
    "label": "Function Response Caching",
    "values": {
      "free": "no",
      "starter_legacy": "yes",
      "launch_legacy": "yes",
      "essential": "yes",
      "pro": "yes"
    }
  }, {
    "label": "Redis Caching",
    "values": {
      "free": "no",
      "starter_legacy": "no",
      "launch_legacy": "no",
      "essential": "no",
      "pro": "yes"
    }
  }]
}, {
  "title": "INTEROPERABILITY",
  "rows": [{
    "label": "Developer & Metadata API",
    "values": {
      "free": "limited",
      "starter_legacy": "yes",
      "launch_legacy": "yes",
      "essential": "yes",
      "pro": "yes"
    }
  }, {
    "label": "Direct Database Access (Read)",
    "values": {
      "free": "no",
      "starter_legacy": "add-on",
      "launch_legacy": "add-on",
      "essential": "yes",
      "pro": "yes"
    }
  }, {
    "label": "Identity Management (SSO)",
    "values": {
      "free": "no",
      "starter_legacy": "no",
      "launch_legacy": "no",
      "essential": "no",
      "pro": "no"
    }
  }, {
    "label": "Docker Sidecar Microservices",
    "values": {
      "free": "no",
      "starter_legacy": "no",
      "launch_legacy": "no",
      "essential": "no",
      "pro": "no"
    }
  }]
}, {
  "title": "HOSTING & SCALING",
  "rows": [{
    "label": "Hosted with Xano",
    "values": {
      "free": "yes",
      "starter_legacy": "yes",
      "launch_legacy": "yes",
      "essential": "yes",
      "pro": "yes"
    }
  }, {
    "label": "Paid Instance Hosting Regions",
    "values": {
      "free": "US only",
      "starter_legacy": "global choices",
      "launch_legacy": "global choices",
      "essential": "global choices",
      "pro": "global choices"
    }
  }, {
    "label": "Dedicated Resources",
    "values": {
      "free": "no",
      "starter_legacy": "not guaranteed",
      "launch_legacy": "yes",
      "essential": "yes",
      "pro": "yes"
    }
  }, {
    "label": "Load Balanced",
    "values": {
      "free": "no",
      "starter_legacy": "no",
      "launch_legacy": "no",
      "essential": "no",
      "pro": "yes"
    }
  }, {
    "label": "Auto Scaling",
    "values": {
      "free": "no",
      "starter_legacy": "no",
      "launch_legacy": "no",
      "essential": "no",
      "pro": "no"
    }
  }]
}, {
  "title": "SECURITY",
  "rows": [{
    "label": "Automatic Backups",
    "values": {
      "free": "no",
      "starter_legacy": "yes (rolling 7-day)",
      "launch_legacy": "Prior to July 2025: yes (rolling 3-day)\nAfter July 2025: yes (rolling 7-day)",
      "essential": "yes (rolling 7-day)",
      "pro": "yes (rolling 14-day)"
    }
  }, {
    "label": "Audit Logs",
    "values": {
      "free": "24h",
      "starter_legacy": "7d",
      "launch_legacy": "7d",
      "essential": "7d",
      "pro": "28d"
    }
  }, {
    "label": "Dedicated IP",
    "values": {
      "free": "no",
      "starter_legacy": "no",
      "launch_legacy": "no",
      "essential": "no",
      "pro": "no"
    }
  }]
}, {
  "title": "Boosts (Starter +, Pro 2x)",
  "rows": [{
    "label": "Additional Team Member",
    "values": {
      "free": "x",
      "starter_legacy": "$20",
      "launch_legacy": "$20",
      "essential": "$20",
      "pro": "$20"
    }
  }, {
    "label": "Additional Workspace",
    "values": {
      "free": "x",
      "starter_legacy": "$29",
      "launch_legacy": "$29",
      "essential": "$29",
      "pro": "$29"
    }
  }, {
    "label": "Unlimited Background Tasks***",
    "values": {
      "free": "x",
      "starter_legacy": "N/A (Deprecate)",
      "launch_legacy": "If a current Launch or Scale user has an active deprecated add-on, they will continue to pay for it, as long as it's not already included in their improved plan. Those users will see those add-ons on the modify add-ons page, to stop paying for them at anytime.",
      "essential": "N/A (Deprecate)",
      "pro": "N/A (Deprecate)"
    }
  }, {
    "label": "Additional 10 Versions (Version History)",
    "values": {
      "free": "x",
      "starter_legacy": "N/A (Deprecate)",
      "launch_legacy": "",
      "essential": "N/A (Deprecate)",
      "pro": "N/A (Deprecate)"
    }
  }, {
    "label": "Additional 100GB Bandwidth",
    "values": {
      "free": "x",
      "starter_legacy": "N/A (Deprecate)",
      "launch_legacy": "",
      "essential": "N/A (Deprecate)",
      "pro": "N/A (Deprecate)"
    }
  }, {
    "label": "Additional 10GB Media Storage *",
    "values": {
      "free": "x",
      "starter_legacy": "$5",
      "launch_legacy": "$5",
      "essential": "$5",
      "pro": "$5"
    }
  }, {
    "label": "Additional 5GB of Database SSD Storage **",
    "values": {
      "free": "x",
      "starter_legacy": "$10",
      "launch_legacy": "$10",
      "essential": "$10",
      "pro": "$10"
    }
  }, {
    "label": "Additional Data Source",
    "values": {
      "free": "x",
      "starter_legacy": "NA",
      "launch_legacy": "$99",
      "essential": "$99",
      "pro": "$99"
    }
  }, {
    "label": "Private Storage",
    "values": {
      "free": "x",
      "starter_legacy": "no",
      "launch_legacy": "no",
      "essential": "no",
      "pro": "included"
    }
  }, {
    "label": "Direct Database Connector",
    "values": {
      "free": "x",
      "starter_legacy": "As an add-on - $25/m annually",
      "launch_legacy": "Add-on",
      "essential": "Included",
      "pro": "Included"
    }
  }, {
    "label": "Static/dedicated IP",
    "values": {
      "free": "x",
      "starter_legacy": "$99",
      "launch_legacy": "$99",
      "essential": "$99",
      "pro": "$99"
    }
  }, {
    "label": "Xano Link - lite only",
    "values": {
      "free": "x",
      "starter_legacy": "N/A",
      "launch_legacy": "N/A",
      "essential": "N/A",
      "pro": "Included"
    }
  }, {
    "label": "CMC Shield (CUI)",
    "values": {
      "free": "no",
      "starter_legacy": "no",
      "launch_legacy": "no",
      "essential": "no",
      "pro": "Keep as it is today"
    }
  }, {
    "label": "HIPAA / HDS",
    "values": {
      "free": "no",
      "starter_legacy": "no",
      "launch_legacy": "no",
      "essential": "no",
      "pro": "Keep as it is today"
    }
  }]
}];


export const CURRENT_PLAN_IDS = ["free", "essential", "pro"];
export const ALL_PLAN_IDS = ["free", "starter_legacy", "launch_legacy", "essential", "pro"];


export const Cell = ({value}) => {
  if (!value) return <span>—</span>;
  const parts = String(value).split("\n");
  return <span>
      {parts.map((line, idx) => <span key={idx}>
          {line}
          {idx < parts.length - 1 ? <br /> : null}
        </span>)}
    </span>;
};


export const PlanTable = ({rows, planIds}) => <div className="overflow-x-auto">
  <table className="w-full">
    <thead>
      <tr>
        <th style={{
  width: "28%"
}}>Feature</th>
        {planIds.map(id => <th key={id}>{PLAN_META[id].label}</th>)}
      </tr>
    </thead>
    <tbody>
      {rows.map(row => <tr key={row.label}>
          <td>
            <strong>{row.label}</strong>
          </td>
          {planIds.map(id => <td key={id}>
              <Cell value={row.values[id]} />
            </td>)}
        </tr>)}
    </tbody>
  </table>
  </div>;


export const PlanMatrix = ({planIds}) => <AccordionGroup>
    {MATRIX_SECTIONS.map(section => <Accordion key={section.title} title={section.title}>
        <PlanTable rows={section.rows} planIds={planIds} />
      </Accordion>)}
  </AccordionGroup>;


<Info>
  This page is designed for **existing customers** who are currently on a legacy plan and want to understand the current pricing lineup. New customers should start on the [pricing](https://xano.com/pricing) page.
</Info>

## Start here: what plan are you on?

<Tabs>
  <Tab title="Starter ($29 legacy)">
    **Good news:** If you're already on the \$29 Starter plan, you can keep it.

    **When to consider switching to Essential**

    * You want **more CPU / more workspaces / more seats**
    * You want **Direct Database Connector included**
    * You need **ISO / SOC compliance** included

    <Tip>
      Essential is the new “real app / production” entry point. Starter remains a great grandfathered option for hobby projects and low-usage workloads.
    </Tip>
  </Tab>

  <Tab title="Launch (legacy)">
    If you're on Launch today, you can generally stay where you are.

    **Closest current plan:** **Essential**

    **When switching to Essential makes sense**

    * You currently pay for the **Direct Database Connector** as an add-on on Launch (it is included in Essential)
    * You want to align with the newest plan naming and packaging, and ensure you have access to the latest upcoming features included in Essential

    <Note>
      If Launch still meets your needs and your billing is favorable, staying put is totally reasonable.
    </Note>
  </Tab>

  <Tab title="Scale (legacy)">
    If you're on Scale today, you can generally stay where you are.

    **Closest current plan:** **Pro**

    **How to think about Pro vs Scale**

    * **Pro** bundles some items that used to be add-ons (ex: Database Connector, Xano Link)
    * If you rely on **auto-scaling**, you may prefer to stay on Scale, or evaluate **Pro + Autoscale Boost**

    <Warning>
      Scale has had multiple iterations. If you’re not sure if your current Scale tier is the right choice, contact Support and we’ll help you map your current usage to the right option.
    </Warning>
  </Tab>

  <Tab title="Not sure">
    In your Xano dashboard, check **Billing → Plan** to confirm your plan name.

    If you’re still unsure about what to do, message Support with:

    * Your plan name (and whether you see any add-ons)
    * Your current CPU usage / scaling needs
    * How many workspaces and team seats you need
    * If you use any of our Enterprise-grade features, such as Database Connector or Xano Link
  </Tab>
</Tabs>

***

## Scale → Pro cheat sheet (legacy)

<AccordionGroup>
  <Accordion title="If you're on Scale 1x">
    Pro is the closest match in the current lineup, and it bundles some capabilities that historically were add-ons.

    * If you need **auto-scaling**, check whether you have access to **Pro + Autoscale Boost** (or stay on Scale).
    * If you want a simpler bundle and you use the **Database Connector** and/or **Xano Link**, Pro may be a better fit.
  </Accordion>

  <Accordion title="If you're on Scale 2x or higher">
    You’re likely already getting more performance than Pro provides by default.

    * If performance and built-in scaling are the priority, staying on Scale is often the simplest path.
    * If your workload has changed and you no longer need the higher Scale tier, Pro can be a cost-optimization option (especially if you want bundled add-ons).

    <Tip>
      If you share your current CPU utilization and scaling pattern, Support can recommend whether it’s worth switching.
    </Tip>
  </Accordion>
</AccordionGroup>

***

## Current plans at a glance

<PlanTable rows={OVERVIEW_ROWS} planIds={CURRENT_PLAN_IDS} />

<Note>
  For details on a Custom/Enterprise plan, route customers to Sales / Support (this comparison page intentionally focuses on self-serve plans).
</Note>

***

## Full feature comparison

<Tabs>
  <Tab title="Current lineup (recommended)">
    <PlanMatrix planIds={CURRENT_PLAN_IDS} />
  </Tab>

  <Tab title="Include legacy plans">
    <PlanMatrix planIds={ALL_PLAN_IDS} />

    <Info>
      Legacy plans are shown for comparison only. They may no longer be sold to new customers.
    </Info>
  </Tab>
</Tabs>

***

## FAQs and edge cases

<AccordionGroup>
  <Accordion title="Do I have to switch off my current plan?">
    In most cases: **no**. If your current plan still fits, you can usually stay on it.

    If you want help deciding, contact Support with your current plan + usage pattern.
  </Accordion>

  <Accordion title="Should I switch from Starter ($29 legacy) to Essential?">
    Switch to **Essential** if you need: more CPU, more workspaces, more seats, compliance, or Direct Database Connector included.

    Otherwise, staying on Starter is fine for smaller projects.
  </Accordion>

  <Accordion title="Should I switch from Launch to Essential?">
    Essential is the closest match to Launch in the current lineup.

    If you pay for add-ons on Launch that are bundled into Essential, switching may simplify your bill.
  </Accordion>

  <Accordion title="What if I rely heavily on auto-scaling?">
    If auto-scaling is critical:

    * You may prefer to stay on **Scale** (if that’s what you’re on today), or
    * Evaluate **Pro + Autoscale Boost** (if offered on your account), or
    * Talk to Sales/Support about a Custom plan for higher-scale needs.
  </Accordion>

  <Accordion title="Who can I contact for more questions?">
    Reach out via:

    * Support chat in your Xano dashboard
    * Email support for detailed migration planning
    * Schedule a call for complex migration scenarios
  </Accordion>
</AccordionGroup>


Built with [Mintlify](https://mintlify.com).