# Source: https://docs.curator.interworks.com/creating_integrations/tableau_connection/tableau_cloud_setup.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.curator.interworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Tableau Cloud Setup

> Configure Tableau Cloud with Curator using connected apps for secure authentication and seamless dashboard integration.

export const BackendNavPath = ({levelOne, levelTwo, levelThree, tab, section}) => {
  const levels = [levelOne, levelTwo, levelThree].filter(Boolean);
  const lastLevel = levels.length ? levels[levels.length - 1] : '';
  return <span>
      In the <a href="/setup/installation/linux_installation">backend of Curator</a> using the left-hand navigation,
      navigate to the
      {levelOne && <strong>{" " + levelOne}</strong>}
      {levelOne && levelTwo && " > "}
      {levelTwo && <strong>{levelTwo}</strong>}
      {levelTwo && levelThree && " > "}
      {levelThree && <strong>{levelThree}</strong>} page.
      {(tab || section) && <>
          {" "}On the {lastLevel} page
          {tab && <> click the <strong>{tab}</strong> tab</>}
          {tab && section && " and"}
          {section && <> expand the <strong>{section}</strong> section</>}.
        </>}
    </span>;
};

## Creating a new Connection

Follow the steps in the [Tableau Connection Setup](/creating_integrations/tableau_connection/creating_a_connection)
section to get connected to your Tableau Server.

## Connected Apps

As of the `01-04-23` Curator release, Tableau's connected apps are now supported as a method of authentication.
This means SSO is no longer required to support a seamless authentication experience for Tableau Cloud users.  All
Tableau Cloud connections in Curator utilize connected apps.  Curator will create a connected app on your Tableau Cloud
site if one doesn't already exist.  You may switch which connected app Curator uses if you need.

For more information and a troubleshooting guide, refer to our article about
[Creating Integrations: Tableau Connection - Connected Apps](/creating_integrations/tableau_connection/embed_authentication)

## Custom Domains

In the August 2025 release of Tableau Cloud, Tableau introduced the ability to use custom domains (also known as vanity
URLs). This feature primarily circumvents the need for users to modify their browser's cookie settings to allow
third-party cookies, creating a truly seamless authentication experience when accessing Tableau dashboards via Curator.
*This feature is only available in Curator versions `2025-10-02` and later.*

### Setting up a Custom Domain on Tableau Cloud

To set up a custom domain on Tableau Cloud, follow the [instructions provided by Tableau](https://help.tableau.com/current/online/en-us/custom_domain.htm).

### Adding your Custom Domain to Curator

Once your custom domain is set up and verified on Tableau Cloud, add your custom domain to Curator  to add it to Curator
to ensure seamless integration.  Begin by navigating to your Tableau Cloud connection in Curator.  Then, follow these
steps:

1. <BackendNavPath levelOne="Integrations" levelTwo="Connections" /> Click on the Tableau connection you'd like to modify.

2. In the **Tableau Connection** section, enter your custom domain URL in the **Custom Domain** field.

3. Confirm that Curator can reach the domain, and that there are no warnings:
   <img src="https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/creating_integrations/tableau_connection/successful_custom_domain.png?fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=ba485d033326065d788f4af5d32716cf" alt="Custom Domain Success" data-og-width="1058" width="1058" data-og-height="446" height="446" data-path="assets/images/creating_integrations/tableau_connection/successful_custom_domain.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/creating_integrations/tableau_connection/successful_custom_domain.png?w=280&fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=c2c8e33bc78375fdec0e44913698d8e4 280w, https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/creating_integrations/tableau_connection/successful_custom_domain.png?w=560&fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=01abf2f381fefa5026127908b6c86a34 560w, https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/creating_integrations/tableau_connection/successful_custom_domain.png?w=840&fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=0ca834972133e37404f93423662c95ed 840w, https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/creating_integrations/tableau_connection/successful_custom_domain.png?w=1100&fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=c64d9704448aaa4f22bc326f34879ea9 1100w, https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/creating_integrations/tableau_connection/successful_custom_domain.png?w=1650&fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=c0fa58c496b8cb85ab92aed090165064 1650w, https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/creating_integrations/tableau_connection/successful_custom_domain.png?w=2500&fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=6ae03653391ca8a679603a702e4f8093 2500w" />

4. Click **Save** to apply your changes.

Now when users access embedded Tableau Cloud dashboards they will be loaded through your Custom Domain in Curator.
