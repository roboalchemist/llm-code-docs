# Source: https://planetscale.com/docs/vitess/tutorials/cloudflare-workers.md

# Source: https://planetscale.com/docs/vitess/integrations/cloudflare-workers.md

# Cloudflare Workers database integration

## Introduction

[Cloudflare Workers database integration](https://developers.cloudflare.com/workers/learning/integrations/databases/#planetscale) is designed to connect your Cloudflare Workers to data sources automatically by generating connection strings and storing them in the worker's secrets.

This article will utilize a sample repository that is a preconfigured Cloudflare Worker you can use to deploy to your Cloudflare account.

## Prerequisites

* [NodeJS](https://nodejs.org) installed
* A [PlanetScale account](https://auth.planetscale.com/sign-up)
* The [PlanetScale CLI](https://github.com/planetscale/cli)
* A [Cloudflare account](https://www.cloudflare.com)

## Set up the database

<Steps>
  <Step>
    Create a database in your PlanetScale account named `bookings_db`.

    ```bash  theme={null}
    pscale database create bookings_db
    ```
  </Step>

  <Step>
    Connect to the `main` branch of the new database.

    ```bash  theme={null}
    pscale shell bookings_db main
    ```
  </Step>

  <Step>
    Run the following commands to create a table in the database and populate it with some data.

    ```sql  theme={null}
    CREATE TABLE hotels (
      id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
      name VARCHAR(50) NOT NULL,
      address VARCHAR(50) NOT NULL,
      stars FLOAT(2) UNSIGNED
    );

    INSERT INTO hotels (name, address, stars) VALUES
      ('Hotel California', '1967 Can Never Leave Ln, San Fancisco CA, 94016', 7.6),
      ('The Galt House', '140 N Fourth St, Louisville, KY 40202', 8.0);
    ```
  </Step>
</Steps>

## Deploy the Cloudflare Worker

<Steps>
  <Step>
    Clone the sample repository.

    ```bash  theme={null}
    git clone https://github.com/planetscale/cloudflare-workers-quickstart.git
    ```
  </Step>

  <Step>
    Navigate to the `worker` folder of the repository and install the dependencies.

    ```bash  theme={null}
    cd cloudflare-workers-quickstart/worker
    npm install
    ```
  </Step>

  <Step>
    Deploy the Worker to your Cloudflare account.

    ```bash  theme={null}
    npx wrangler publish
    ```
  </Step>
</Steps>

## Configure the Cloudflare PlanetScale integration

<Steps>
  <Step>
    Log into the Cloudflare dashboard and navigate to **"Workers"** > **"Overview"**. You should see a service in the list named **"planetscale-worker"**. Select it from the list.

    <Frame>
            <img src="https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/integrations/cloudflare-workers/CleanShot_2023-05-16_at_11.52.48.png?fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=e09de5f7e8e98c67842fd0ef10c72315" alt="PlanetScale Cloudflare integration wizard - step 1" data-og-width="1760" width="1760" data-og-height="903" height="903" data-path="docs/images/assets/docs/integrations/cloudflare-workers/CleanShot_2023-05-16_at_11.52.48.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/integrations/cloudflare-workers/CleanShot_2023-05-16_at_11.52.48.png?w=280&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=9e82d236471d950865b0ddefa84b2ef6 280w, https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/integrations/cloudflare-workers/CleanShot_2023-05-16_at_11.52.48.png?w=560&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=0b4c709602f247d8c6f9c9c53dd4d4c7 560w, https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/integrations/cloudflare-workers/CleanShot_2023-05-16_at_11.52.48.png?w=840&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=807190b415c630258900e2f94b05407b 840w, https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/integrations/cloudflare-workers/CleanShot_2023-05-16_at_11.52.48.png?w=1100&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=cba0647d673ed32e6ef960d9f31bd783 1100w, https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/integrations/cloudflare-workers/CleanShot_2023-05-16_at_11.52.48.png?w=1650&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=6cc676932997cf48d019c6b7edaccfc6 1650w, https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/integrations/cloudflare-workers/CleanShot_2023-05-16_at_11.52.48.png?w=2500&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=7eaa2a858225ca039b7afaa610fdc67c 2500w" />
    </Frame>
  </Step>

  <Step>
    Select the **"Settings"** tab, then **"Integrations"**, and finally **"Add Integration"** in the PlanetScale card.

    <Frame>
            <img src="https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/integrations/cloudflare-workers/CleanShot_2023-05-16_at_11.51.19.png?fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=c3414a459fa818eedadd1d922c5517f2" alt="PlanetScale Cloudflare integration wizard - step 2" data-og-width="1758" width="1758" data-og-height="901" height="901" data-path="docs/images/assets/docs/integrations/cloudflare-workers/CleanShot_2023-05-16_at_11.51.19.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/integrations/cloudflare-workers/CleanShot_2023-05-16_at_11.51.19.png?w=280&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=7f801daa32a939f8b67674c22343ba18 280w, https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/integrations/cloudflare-workers/CleanShot_2023-05-16_at_11.51.19.png?w=560&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=016647eb7a825d1643ec98bcb4c6463d 560w, https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/integrations/cloudflare-workers/CleanShot_2023-05-16_at_11.51.19.png?w=840&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=22e0a31442f969e1c9fe1c89fb5c75df 840w, https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/integrations/cloudflare-workers/CleanShot_2023-05-16_at_11.51.19.png?w=1100&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=217eecee3a12613db8e513785aa284da 1100w, https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/integrations/cloudflare-workers/CleanShot_2023-05-16_at_11.51.19.png?w=1650&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=2bf3f34b10a977fa0259e2ddd03583c8 1650w, https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/integrations/cloudflare-workers/CleanShot_2023-05-16_at_11.51.19.png?w=2500&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=d5d035320351e206ba29636c56967796 2500w" />
    </Frame>
  </Step>

  <Step>
    Click **"Accept"** under **Review and grant permissions** to allow the wizard to write the database connection details to the Worker secrets.

    <Frame>
            <img src="https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/integrations/cloudflare-workers/CleanShot_2023-05-16_at_11.55.06.png?fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=e6c13f25e08ea22dae40c66076ba35c6" alt="PlanetScale Cloudflare integration wizard - step 3" data-og-width="1474" width="1474" data-og-height="1011" height="1011" data-path="docs/images/assets/docs/integrations/cloudflare-workers/CleanShot_2023-05-16_at_11.55.06.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/integrations/cloudflare-workers/CleanShot_2023-05-16_at_11.55.06.png?w=280&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=9ee1a368214784e5e6e0a12c27872c41 280w, https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/integrations/cloudflare-workers/CleanShot_2023-05-16_at_11.55.06.png?w=560&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=b52bf6e6a50c556da6b51f8d3b35044c 560w, https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/integrations/cloudflare-workers/CleanShot_2023-05-16_at_11.55.06.png?w=840&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=b07f79dcd6fa950dbc735226bcd55f75 840w, https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/integrations/cloudflare-workers/CleanShot_2023-05-16_at_11.55.06.png?w=1100&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=2c1992f7cf524ebfee17c0270670d5ed 1100w, https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/integrations/cloudflare-workers/CleanShot_2023-05-16_at_11.55.06.png?w=1650&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=7e7d81b47a9ff64b82096beeb1cc8805 1650w, https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/integrations/cloudflare-workers/CleanShot_2023-05-16_at_11.55.06.png?w=2500&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=a70a2f20732738d0504962d14eddd714 2500w" />
    </Frame>
  </Step>

  <Step>
    Under **Connect to PlanetScale**, click **"Connect"** to start the process of connecting your PlanetScale and Cloudflare accounts.

    <Frame>
            <img src="https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/integrations/cloudflare-workers/CleanShot_2023-05-16_at_11.56.11.png?fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=f2bee6ceff513f228261d8bb2bf575d0" alt="PlanetScale Cloudflare integration wizard - step 4" data-og-width="1467" width="1467" data-og-height="801" height="801" data-path="docs/images/assets/docs/integrations/cloudflare-workers/CleanShot_2023-05-16_at_11.56.11.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/integrations/cloudflare-workers/CleanShot_2023-05-16_at_11.56.11.png?w=280&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=90ae58d9dbbb40907c1277400b84af9b 280w, https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/integrations/cloudflare-workers/CleanShot_2023-05-16_at_11.56.11.png?w=560&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=c5d3113f80618170ab0b3533da4cbe1b 560w, https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/integrations/cloudflare-workers/CleanShot_2023-05-16_at_11.56.11.png?w=840&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=ded7904da2a3d12bd727f9f66818b2af 840w, https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/integrations/cloudflare-workers/CleanShot_2023-05-16_at_11.56.11.png?w=1100&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=b51e5b3846bd7bfc582717255410dbc5 1100w, https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/integrations/cloudflare-workers/CleanShot_2023-05-16_at_11.56.11.png?w=1650&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=1849489e699fed6acf31ee4286bb441c 1650w, https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/integrations/cloudflare-workers/CleanShot_2023-05-16_at_11.56.11.png?w=2500&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=94ddd8b631a271ccc6fca41d34a02d5f 2500w" />
    </Frame>
  </Step>

  <Step>
    A modal will appear allowing you to grant access to your organization, database, and branch. Start by selecting your organization from the list. This demonstration uses an organization named “ps-deved”.

    <Frame>
            <img src="https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/integrations/cloudflare-workers/CleanShot_2023-05-16_at_11.59.44.png?fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=945738456262d053fd1eaafe363b8bb4" alt="PlanetScale Cloudflare integration wizard - step 5" data-og-width="748" width="748" data-og-height="883" height="883" data-path="docs/images/assets/docs/integrations/cloudflare-workers/CleanShot_2023-05-16_at_11.59.44.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/integrations/cloudflare-workers/CleanShot_2023-05-16_at_11.59.44.png?w=280&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=a23568968d710918c8071d769d7bff40 280w, https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/integrations/cloudflare-workers/CleanShot_2023-05-16_at_11.59.44.png?w=560&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=4963680e4bdf3a780c0c8f0cc89a39f2 560w, https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/integrations/cloudflare-workers/CleanShot_2023-05-16_at_11.59.44.png?w=840&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=4375a4a56f1b1a69cfe8d75e9f7895f3 840w, https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/integrations/cloudflare-workers/CleanShot_2023-05-16_at_11.59.44.png?w=1100&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=f3af118b8fb20d61b8e5304a605841a9 1100w, https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/integrations/cloudflare-workers/CleanShot_2023-05-16_at_11.59.44.png?w=1650&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=2b46d1c5bfa99604a8bef2811fb77cd4 1650w, https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/integrations/cloudflare-workers/CleanShot_2023-05-16_at_11.59.44.png?w=2500&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=2a748ef8a2b9c55110fda4713c1f7dac 2500w" />
    </Frame>
  </Step>

  <Step>
    Select the “bookings\_db” database from the list in the **Databases** card, and the “main” branch from the list in the **Branches** card. Finally, click **"Authorize access"**.

    <Frame>
            <img src="https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/integrations/cloudflare-workers/CleanShot_2023-05-16_at_12.00.34.png?fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=d4008ffa166bc2f36c97360b2ee0c7be" alt="PlanetScale Cloudflare integration wizard - step 6" data-og-width="759" width="759" data-og-height="824" height="824" data-path="docs/images/assets/docs/integrations/cloudflare-workers/CleanShot_2023-05-16_at_12.00.34.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/integrations/cloudflare-workers/CleanShot_2023-05-16_at_12.00.34.png?w=280&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=f976c879e7f3c576bb0cb0dae6ca8f42 280w, https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/integrations/cloudflare-workers/CleanShot_2023-05-16_at_12.00.34.png?w=560&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=b770c9bd360aa8693e517c536e828371 560w, https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/integrations/cloudflare-workers/CleanShot_2023-05-16_at_12.00.34.png?w=840&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=f729e75b9db77d391687d471d7b94c0b 840w, https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/integrations/cloudflare-workers/CleanShot_2023-05-16_at_12.00.34.png?w=1100&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=398fca821d8cd31958f6e6ff65a3dbfd 1100w, https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/integrations/cloudflare-workers/CleanShot_2023-05-16_at_12.00.34.png?w=1650&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=cb65a80d695c4831410a54d55ba02595 1650w, https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/integrations/cloudflare-workers/CleanShot_2023-05-16_at_12.00.34.png?w=2500&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=31bb75c37b752a6ad8ed70dea58e95d4 2500w" />
    </Frame>
  </Step>

  <Step>
    Select your organization again from the list and click **"Continue"**.

    <Frame>
            <img src="https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/integrations/cloudflare-workers/CleanShot_2023-05-16_at_12.01.32.png?fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=e184b3f8c80b32d42421f27c59f44b82" alt="PlanetScale Cloudflare integration wizard - step 7" data-og-width="1383" width="1383" data-og-height="960" height="960" data-path="docs/images/assets/docs/integrations/cloudflare-workers/CleanShot_2023-05-16_at_12.01.32.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/integrations/cloudflare-workers/CleanShot_2023-05-16_at_12.01.32.png?w=280&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=1cd7184b03261d7470af344ca055c395 280w, https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/integrations/cloudflare-workers/CleanShot_2023-05-16_at_12.01.32.png?w=560&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=f699f7641313c9b626bc0695322eda03 560w, https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/integrations/cloudflare-workers/CleanShot_2023-05-16_at_12.01.32.png?w=840&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=31cac4bc09fe6ab27fd656535c2f7826 840w, https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/integrations/cloudflare-workers/CleanShot_2023-05-16_at_12.01.32.png?w=1100&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=ae9ee322013959014789a517773233d4 1100w, https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/integrations/cloudflare-workers/CleanShot_2023-05-16_at_12.01.32.png?w=1650&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=fc70027807521177c9a2ff736d2b1a90 1650w, https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/integrations/cloudflare-workers/CleanShot_2023-05-16_at_12.01.32.png?w=2500&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=286310a2226098dbc616702b8b76af2f 2500w" />
    </Frame>
  </Step>

  <Step>
    Select your database and the [user role](/docs/vitess/security/password-roles) you want the integration to have.

    <Frame>
            <img src="https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/integrations/cloudflare-workers/CleanShot_2023-05-16_at_12.02.29.png?fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=75a3f9ca4131241956cdb3fef2a1a9b3" alt="PlanetScale Cloudflare integration wizard - step 8" data-og-width="1402" width="1402" data-og-height="907" height="907" data-path="docs/images/assets/docs/integrations/cloudflare-workers/CleanShot_2023-05-16_at_12.02.29.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/integrations/cloudflare-workers/CleanShot_2023-05-16_at_12.02.29.png?w=280&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=b4b69fde8db00d0faddcb068da3f9604 280w, https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/integrations/cloudflare-workers/CleanShot_2023-05-16_at_12.02.29.png?w=560&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=05f21b792e07a0ecbee3f0f1d4b666e3 560w, https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/integrations/cloudflare-workers/CleanShot_2023-05-16_at_12.02.29.png?w=840&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=4136bcbe4c486ccb4604a6d6254949c1 840w, https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/integrations/cloudflare-workers/CleanShot_2023-05-16_at_12.02.29.png?w=1100&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=d21b05ba311f0803bd65dbdab3f44ea3 1100w, https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/integrations/cloudflare-workers/CleanShot_2023-05-16_at_12.02.29.png?w=1650&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=7fcc9e4b96c6042d656a371719dd8bab 1650w, https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/integrations/cloudflare-workers/CleanShot_2023-05-16_at_12.02.29.png?w=2500&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=e5dab734feb249aea958762ff55638b3 2500w" />
    </Frame>
  </Step>

  <Step>
    Select the “main” branch from the list and click **"Continue"**.

    <Frame>
            <img src="https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/integrations/cloudflare-workers/CleanShot_2023-05-16_at_12.03.07.png?fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=3953c32e12c0ca5d384c5796e3c64208" alt="PlanetScale Cloudflare integration wizard - step 9" data-og-width="1406" width="1406" data-og-height="754" height="754" data-path="docs/images/assets/docs/integrations/cloudflare-workers/CleanShot_2023-05-16_at_12.03.07.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/integrations/cloudflare-workers/CleanShot_2023-05-16_at_12.03.07.png?w=280&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=9ddb6c3c065cb5433c357dbcc6e740fb 280w, https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/integrations/cloudflare-workers/CleanShot_2023-05-16_at_12.03.07.png?w=560&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=15e092e97fcee20c60efac6f66ff0938 560w, https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/integrations/cloudflare-workers/CleanShot_2023-05-16_at_12.03.07.png?w=840&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=66a5ebfb214cfb09fce78d95a1e8b247 840w, https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/integrations/cloudflare-workers/CleanShot_2023-05-16_at_12.03.07.png?w=1100&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=7af23600587fc9f3d9fe1c528c34b193 1100w, https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/integrations/cloudflare-workers/CleanShot_2023-05-16_at_12.03.07.png?w=1650&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=57f8b0a52a96538f76113d7d19581034 1650w, https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/integrations/cloudflare-workers/CleanShot_2023-05-16_at_12.03.07.png?w=2500&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=f61718a70e12c4ff50e8b1856ecf2c20 2500w" />
    </Frame>
  </Step>

  <Step>
    You’ll be given the option to rename the secrets that will be configured on your behalf. These can be left as is. Click **"Add Integration"** to complete the process.

    <Frame>
            <img src="https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/integrations/cloudflare-workers/CleanShot_2023-05-16_at_13.33.05.png?fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=e493ffc599cda78930738030eb5ff2d4" alt="PlanetScale Cloudflare integration wizard - step 10" data-og-width="1441" width="1441" data-og-height="681" height="681" data-path="docs/images/assets/docs/integrations/cloudflare-workers/CleanShot_2023-05-16_at_13.33.05.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/integrations/cloudflare-workers/CleanShot_2023-05-16_at_13.33.05.png?w=280&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=ada2f8018465e4a3d0a4f404d4f80999 280w, https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/integrations/cloudflare-workers/CleanShot_2023-05-16_at_13.33.05.png?w=560&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=55388da6408fc4baf106b989bcceb19c 560w, https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/integrations/cloudflare-workers/CleanShot_2023-05-16_at_13.33.05.png?w=840&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=cb870130ce4c96c29a5241e45a9691b4 840w, https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/integrations/cloudflare-workers/CleanShot_2023-05-16_at_13.33.05.png?w=1100&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=10eb66b595928771b35967bf3595c2d3 1100w, https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/integrations/cloudflare-workers/CleanShot_2023-05-16_at_13.33.05.png?w=1650&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=859b47970a4b02dad289a4202d3f85af 1650w, https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/integrations/cloudflare-workers/CleanShot_2023-05-16_at_13.33.05.png?w=2500&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=026533cc1d16951e861b6736b770ba33 2500w" />
    </Frame>
  </Step>
</Steps>

## Test the integration

Back in the overview of the Worker, there is a preview URL that you can use to open a new tab in your browser that runs the Worker and displays the results. Once you’ve located the preview URL, click it to test the Worker.

<Frame>
    <img src="https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/integrations/cloudflare-workers/CleanShot_2023-05-16_at_13.03.41.png?fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=7d06084c3df1da6de44710146a652871" alt="Cloudflare Worker preview URL in the dashboard" data-og-width="1436" width="1436" data-og-height="546" height="546" data-path="docs/images/assets/docs/integrations/cloudflare-workers/CleanShot_2023-05-16_at_13.03.41.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/integrations/cloudflare-workers/CleanShot_2023-05-16_at_13.03.41.png?w=280&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=49fe3df15b50f25358221e182bd2d492 280w, https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/integrations/cloudflare-workers/CleanShot_2023-05-16_at_13.03.41.png?w=560&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=746e7901b61b9346d6827e59ec2b25cb 560w, https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/integrations/cloudflare-workers/CleanShot_2023-05-16_at_13.03.41.png?w=840&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=b6ccddd8b3184f804665a4f385ad4351 840w, https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/integrations/cloudflare-workers/CleanShot_2023-05-16_at_13.03.41.png?w=1100&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=2c4e0edd7560939c1eaf7cf9eefe343f 1100w, https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/integrations/cloudflare-workers/CleanShot_2023-05-16_at_13.03.41.png?w=1650&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=fc4aae1fd497db3af8f963de47b9d306 1650w, https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/integrations/cloudflare-workers/CleanShot_2023-05-16_at_13.03.41.png?w=2500&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=0e5c28355077c1e17862d2de8afe11a9 2500w" />
</Frame>

Once the integration is configured, you can also run the project on your computer using:

```bash  theme={null}
npx wrangler dev
```

This will automatically use the secrets defined in Cloudflare to run the Worker on your computer.

### Test other database operations (optional)

To test other database operations that are mapped to HTTP methods, you may use the provided `tests.http` file which is designed to work with the [VSCode REST client plugin](https://marketplace.visualstudio.com/items?itemName=humao.rest-client). The file is preconfigured to work with the local environment, or you can change the `@host` variable to match the URL provided in the Cloudflare dashboard that cooresponds with your Worker project.

| Method      | Operation                 |
| :---------- | :------------------------ |
| GET /       | Get a list of all hotels. |
| POST /      | Create a hotel.           |
| PUT /:id    | Update a hotel.           |
| DELETE /:id | Delete a hotel.           |

## What's next?

Once you're done with development, it is highly recommended that [safe migrations](/docs/vitess/schema-changes/safe-migrations) be turned on for your `main` production branch to protect from accidental schema changes and enable zero-downtime deployments.

When you're ready to make more schema changes, you'll [create a new branch](/docs/vitess/schema-changes/branching) off of your production branch. Branching your database creates an isolated copy of your production schema so that you can easily test schema changes in development. Once you're happy with the changes, you'll open a [deploy request](/docs/vitess/schema-changes/deploy-requests). This will generate a diff showing the changes that will be deployed, making it easy for your team to review.

Learn more about how PlanetScale allows you to make [non-blocking schema changes](/docs/vitess/schema-changes) to your database tables without locking or causing downtime for production databases.

## Need help?

Get help from [the PlanetScale Support team](https://support.planetscale.com/), or join our [GitHub discussion board](https://github.com/planetscale/discussion/discussions) to see how others are using PlanetScale.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://planetscale.com/llms.txt