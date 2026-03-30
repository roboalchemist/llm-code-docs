# Source: https://docs.curator.interworks.com/site_content_design/content_discovery/favorites.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.curator.interworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Favorites

> Enable user favoriting functionality to personalize homepages and prioritize frequently accessed content.

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

Curator has the ability to mark dashboards as favorites.  Favorited dashboards will show up first on the home page once
the user logs in.

This functionality requires any authentication method other than "Pass-Through".  See the [Authentication Methods](/setup/authentication/overview)
section for more information.

If you have a [Tableau Connection](/creating_integrations/tableau_connection/creating_a_connection)
the favorites will also synchronize across to Tableau Server/Cloud.

You can also display the number of favorites a Dashboard has. This number shows up in both the Dashboard action-buttons
area when viewing a Dashboard and on the homepage when showing Dashboard tiles.

## Enabling Favorites

1. <BackendNavPath levelOne="Settings" levelTwo="Curator" levelThree="Portal Settings" tab="Features" section="Toolbar Buttons (Tableau Actions)" />
2. Find the "Favorites" setting and toggle it on.
3. Be sure to save your changes.

## Favoriting a Dashboard

1. Navigate to the frontend of the system (e.g. `http://curatorexample.com`).
2. Log in if prompted.
3. Navigate to the desired Dashboard by using the navigation menu.
4. Click on the star icon at the top right portion of the screen. Normally this is displayed on the right side of the
   title bar in the Dashboard.

## Showing the Number of Favorites

1. <BackendNavPath levelOne="Settings" levelTwo="Curator" levelThree="Portal Settings" tab="Features" section="Toolbar Buttons (Tableau Actions)" />
2. Find the "Favorites" setting and toggle it on.
3. Be sure to save your changes.
