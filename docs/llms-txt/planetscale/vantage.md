# Source: https://planetscale.com/docs/vitess/integrations/vantage.md

# Source: https://planetscale.com/docs/plans/vantage.md

# Vantage integration

> With [Vantage](https://www.vantage.sh/), you can set up [PlanetScale cost management](https://vantage.sh/integrations/planetscale) to report on PlanetScale costs alongside other infrastructure providers, such as AWS or GCP.

After integrating, you can create [cost reports](https://docs.vantage.sh/cost_reports) to break down costs per database and branch.

Beyond reporting, set up budget alerts, forecast usage, and view active database costs in Vantage. Vantage connects to your PlanetScale organizations using an OAuth flow.

## Prerequisites

* The [Organization Admin role](/docs/security/access-control) in PlanetScale
* A [Vantage account](https://console.vantage.sh/signup)

<Note>
  Database cost reporting in Vantage is not available for [PlanetScale Managed](/docs/vitess/managed) customers via the integration.
</Note>

## Configure the Vantage integration

<Steps>
  <Step>
    From the Vantage console, navigate to the [Integrations page](https://console.vantage.sh/settings/integrations).
  </Step>

  <Step>
    Select **PlanetScale**, then click **Connect PlanetScale Account**.
  </Step>

  <Step>
    The PlanetScale login screen is displayed. Log in to your PlanetScale account and select the organizations you want to connect with.
  </Step>

  <Step>
    Click **Authorize access**.
  </Step>

  <Step>
    On the [PlanetScale Settings](https://console.vantage.sh/settings/planetscale/) page in Vantage, you should see the status of your connection change to **Importing**.
  </Step>
</Steps>

Costs will be ingested and processed in Vantage once you add the integration. It typically takes less than 15 minutes to ingest PlanetScale costs. The costs will be available on your **All Resources** Cost Report in Vantage as soon as they are processed.

<Note>
  PlanetScale data refreshes daily in Vantage.
</Note>

## View PlanetScale costs in Vantage

In Vantage, you can create cost reports to drill down into your costs. Vantage displays PlanetScale costs by Organization, Service, Category, and Resource.

<Frame>
    <img src="https://mintcdn.com/planetscale-cad1a68a/vjR5C2sTgdIGKQJc/docs/images/assets/docs/integrations/vantage/vantage-console.png?fit=max&auto=format&n=vjR5C2sTgdIGKQJc&q=85&s=46b4fe1abdb755f67231f53402352c7f" alt="Image of a PlanetScale Cost Report in Vantage showing costs per database" data-og-width="2792" width="2792" data-og-height="1878" height="1878" data-path="docs/images/assets/docs/integrations/vantage/vantage-console.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/vjR5C2sTgdIGKQJc/docs/images/assets/docs/integrations/vantage/vantage-console.png?w=280&fit=max&auto=format&n=vjR5C2sTgdIGKQJc&q=85&s=b001625dbe59b47c07774ad1284fd129 280w, https://mintcdn.com/planetscale-cad1a68a/vjR5C2sTgdIGKQJc/docs/images/assets/docs/integrations/vantage/vantage-console.png?w=560&fit=max&auto=format&n=vjR5C2sTgdIGKQJc&q=85&s=5aa483c616a9a0625a89e14637137ddd 560w, https://mintcdn.com/planetscale-cad1a68a/vjR5C2sTgdIGKQJc/docs/images/assets/docs/integrations/vantage/vantage-console.png?w=840&fit=max&auto=format&n=vjR5C2sTgdIGKQJc&q=85&s=2faa0509aaf6a18ed782d10e8ca41b01 840w, https://mintcdn.com/planetscale-cad1a68a/vjR5C2sTgdIGKQJc/docs/images/assets/docs/integrations/vantage/vantage-console.png?w=1100&fit=max&auto=format&n=vjR5C2sTgdIGKQJc&q=85&s=fb76560995d65e83cbfac4e1cf5ec213 1100w, https://mintcdn.com/planetscale-cad1a68a/vjR5C2sTgdIGKQJc/docs/images/assets/docs/integrations/vantage/vantage-console.png?w=1650&fit=max&auto=format&n=vjR5C2sTgdIGKQJc&q=85&s=106ba6087edd5e910c04fbccbef41ff7 1650w, https://mintcdn.com/planetscale-cad1a68a/vjR5C2sTgdIGKQJc/docs/images/assets/docs/integrations/vantage/vantage-console.png?w=2500&fit=max&auto=format&n=vjR5C2sTgdIGKQJc&q=85&s=9e57eb2651cd3fe225c3740607b52171 2500w" />
</Frame>

In the graphic above, PlanetScale costs are grouped by database for the month. For complete cost reporting dimensions and more information, see the [PlanetScale documentation](https://docs.vantage.sh/connecting_planetscale) for Vantage.

## Billing

The Vantage integration is available on all our [plans](/docs/planetscale-plans).

## Need help?

Get help from [the PlanetScale Support team](https://support.planetscale.com/), or join our [GitHub discussion board](https://github.com/planetscale/discussion/discussions) to see how others are using PlanetScale.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://planetscale.com/llms.txt