# Source: https://docs.curator.interworks.com/embedding_using_analytics/thoughtspot_content/thoughtspot_full_app.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.curator.interworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# ThoughtSpot Full App Embed

> Embed the complete ThoughtSpot application experience within Curator using the Page Builder.

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

If you have [integrated ThoughtSpot](/creating_integrations/thoughtspot_connection/integrating_thoughtspot_with_curator),
you can follow this guide to add a ThoughtSpot Full App Embed to Curator.

## Creating the ThoughtSpot Full App Embed

The ThoughtSpot Full App Embed is available directly in the Page Builder, allowing you to embed the complete
ThoughtSpot application experience within your Curator pages.

1. <BackendNavPath levelOne="Content" levelTwo="Pages" /> Find the page you'd like to add your embed to, or create a new page.
2. In the Page Builder, select an existing element from the preview and click the "Change Element" button. You can also
   add a new element.
3. Choose the "Analytic Elements" category then the "THOUGHTSPOT FULL APP" element.
   <img src="https://mintcdn.com/interworks/3RotvmSfKD9xBISI/assets/images/thoughtspot/full_app_embed_pb.png?fit=max&auto=format&n=3RotvmSfKD9xBISI&q=85&s=4f6216b99aff7fbdfbffb64279502814" alt="Full app modal element" data-og-width="1840" width="1840" data-og-height="1642" height="1642" data-path="assets/images/thoughtspot/full_app_embed_pb.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/interworks/3RotvmSfKD9xBISI/assets/images/thoughtspot/full_app_embed_pb.png?w=280&fit=max&auto=format&n=3RotvmSfKD9xBISI&q=85&s=2fea27dfd66419670288aee1a54f9511 280w, https://mintcdn.com/interworks/3RotvmSfKD9xBISI/assets/images/thoughtspot/full_app_embed_pb.png?w=560&fit=max&auto=format&n=3RotvmSfKD9xBISI&q=85&s=eb0c1e431adb5045e6e62bd12058de24 560w, https://mintcdn.com/interworks/3RotvmSfKD9xBISI/assets/images/thoughtspot/full_app_embed_pb.png?w=840&fit=max&auto=format&n=3RotvmSfKD9xBISI&q=85&s=e34ebdb3bd6bb96b5dade701dba1b7c9 840w, https://mintcdn.com/interworks/3RotvmSfKD9xBISI/assets/images/thoughtspot/full_app_embed_pb.png?w=1100&fit=max&auto=format&n=3RotvmSfKD9xBISI&q=85&s=a0b01049d6951573028c03ea9fe1e135 1100w, https://mintcdn.com/interworks/3RotvmSfKD9xBISI/assets/images/thoughtspot/full_app_embed_pb.png?w=1650&fit=max&auto=format&n=3RotvmSfKD9xBISI&q=85&s=b7d61d45812cb605a6acee3c3ef3c005 1650w, https://mintcdn.com/interworks/3RotvmSfKD9xBISI/assets/images/thoughtspot/full_app_embed_pb.png?w=2500&fit=max&auto=format&n=3RotvmSfKD9xBISI&q=85&s=ef9a914680cbb3ff6cb4969bba32651c 2500w" />
4. Once the element is added, choose the Org where your ThoughtSpot data lives from the left-hand panel:
   <img src="https://mintcdn.com/interworks/3RotvmSfKD9xBISI/assets/images/thoughtspot/full_app_embed_page_builder_org_dropdown.png?fit=max&auto=format&n=3RotvmSfKD9xBISI&q=85&s=c5428290bfddfc482907316e0a74c9de" alt="Import SAML metadata" data-og-width="316" width="316" data-og-height="523" height="523" data-path="assets/images/thoughtspot/full_app_embed_page_builder_org_dropdown.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/interworks/3RotvmSfKD9xBISI/assets/images/thoughtspot/full_app_embed_page_builder_org_dropdown.png?w=280&fit=max&auto=format&n=3RotvmSfKD9xBISI&q=85&s=305bafbd1cd55f1e6a571a6bd73732d1 280w, https://mintcdn.com/interworks/3RotvmSfKD9xBISI/assets/images/thoughtspot/full_app_embed_page_builder_org_dropdown.png?w=560&fit=max&auto=format&n=3RotvmSfKD9xBISI&q=85&s=cebc1b547d9dc93fa95c19d923258439 560w, https://mintcdn.com/interworks/3RotvmSfKD9xBISI/assets/images/thoughtspot/full_app_embed_page_builder_org_dropdown.png?w=840&fit=max&auto=format&n=3RotvmSfKD9xBISI&q=85&s=b2feb6f873966c874be1119790cd60a5 840w, https://mintcdn.com/interworks/3RotvmSfKD9xBISI/assets/images/thoughtspot/full_app_embed_page_builder_org_dropdown.png?w=1100&fit=max&auto=format&n=3RotvmSfKD9xBISI&q=85&s=b1a403dc12e99106ffe90fc021ba8fbf 1100w, https://mintcdn.com/interworks/3RotvmSfKD9xBISI/assets/images/thoughtspot/full_app_embed_page_builder_org_dropdown.png?w=1650&fit=max&auto=format&n=3RotvmSfKD9xBISI&q=85&s=9a69ea65d294efe1c14e806d9cd5435f 1650w, https://mintcdn.com/interworks/3RotvmSfKD9xBISI/assets/images/thoughtspot/full_app_embed_page_builder_org_dropdown.png?w=2500&fit=max&auto=format&n=3RotvmSfKD9xBISI&q=85&s=1ca2493bd4383e045d61a0cf12b5751b 2500w" />
5. Finally choose the Homepage experience you'd like to use:
   <img src="https://mintcdn.com/interworks/3RotvmSfKD9xBISI/assets/images/thoughtspot/full_app_embed_page_builder_search_bar_dropdown.png?fit=max&auto=format&n=3RotvmSfKD9xBISI&q=85&s=fa9d10c94226b532d848d473f65d88ad" alt="Search bar dropdown" data-og-width="279" width="279" data-og-height="316" height="316" data-path="assets/images/thoughtspot/full_app_embed_page_builder_search_bar_dropdown.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/interworks/3RotvmSfKD9xBISI/assets/images/thoughtspot/full_app_embed_page_builder_search_bar_dropdown.png?w=280&fit=max&auto=format&n=3RotvmSfKD9xBISI&q=85&s=34d657a574af7a17deab641eedcd8115 280w, https://mintcdn.com/interworks/3RotvmSfKD9xBISI/assets/images/thoughtspot/full_app_embed_page_builder_search_bar_dropdown.png?w=560&fit=max&auto=format&n=3RotvmSfKD9xBISI&q=85&s=36d3310b70e21c1d47c71db8d8112b24 560w, https://mintcdn.com/interworks/3RotvmSfKD9xBISI/assets/images/thoughtspot/full_app_embed_page_builder_search_bar_dropdown.png?w=840&fit=max&auto=format&n=3RotvmSfKD9xBISI&q=85&s=0ea22903dc7ec3bc7e4b3bcee5a6980e 840w, https://mintcdn.com/interworks/3RotvmSfKD9xBISI/assets/images/thoughtspot/full_app_embed_page_builder_search_bar_dropdown.png?w=1100&fit=max&auto=format&n=3RotvmSfKD9xBISI&q=85&s=9a976bcd0eafc6bf458927cff69f9fa9 1100w, https://mintcdn.com/interworks/3RotvmSfKD9xBISI/assets/images/thoughtspot/full_app_embed_page_builder_search_bar_dropdown.png?w=1650&fit=max&auto=format&n=3RotvmSfKD9xBISI&q=85&s=a208069cb350adea0b31d1d6bf446156 1650w, https://mintcdn.com/interworks/3RotvmSfKD9xBISI/assets/images/thoughtspot/full_app_embed_page_builder_search_bar_dropdown.png?w=2500&fit=max&auto=format&n=3RotvmSfKD9xBISI&q=85&s=120c53c67e4a23328710e22762912b20 2500w" />
   * **Classic Homepage** (default) - The traditional ThoughtSpot homepage experience
     <img src="https://mintcdn.com/interworks/3RotvmSfKD9xBISI/assets/images/thoughtspot/full_app_embed_classic.png?fit=max&auto=format&n=3RotvmSfKD9xBISI&q=85&s=9477b95faba3a29aa398da05ff084953" alt="Classic homepage embed" data-og-width="1480" width="1480" data-og-height="1019" height="1019" data-path="assets/images/thoughtspot/full_app_embed_classic.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/interworks/3RotvmSfKD9xBISI/assets/images/thoughtspot/full_app_embed_classic.png?w=280&fit=max&auto=format&n=3RotvmSfKD9xBISI&q=85&s=f2d9123169542faf6950254562dfddaf 280w, https://mintcdn.com/interworks/3RotvmSfKD9xBISI/assets/images/thoughtspot/full_app_embed_classic.png?w=560&fit=max&auto=format&n=3RotvmSfKD9xBISI&q=85&s=ed69d1a863be6df1819863a93a6e31a8 560w, https://mintcdn.com/interworks/3RotvmSfKD9xBISI/assets/images/thoughtspot/full_app_embed_classic.png?w=840&fit=max&auto=format&n=3RotvmSfKD9xBISI&q=85&s=464daaf07ace32fea87bb986d75101a1 840w, https://mintcdn.com/interworks/3RotvmSfKD9xBISI/assets/images/thoughtspot/full_app_embed_classic.png?w=1100&fit=max&auto=format&n=3RotvmSfKD9xBISI&q=85&s=15f65bc31a077bc6dbc10d4097a99b6b 1100w, https://mintcdn.com/interworks/3RotvmSfKD9xBISI/assets/images/thoughtspot/full_app_embed_classic.png?w=1650&fit=max&auto=format&n=3RotvmSfKD9xBISI&q=85&s=477d36529e056d7db22d27eb0092d5a3 1650w, https://mintcdn.com/interworks/3RotvmSfKD9xBISI/assets/images/thoughtspot/full_app_embed_classic.png?w=2500&fit=max&auto=format&n=3RotvmSfKD9xBISI&q=85&s=1598c7f668cffad773dfc282736999e4 2500w" />
   * **Spotter Homepage** - ThoughtSpot's new natural language search interface
     <img src="https://mintcdn.com/interworks/3RotvmSfKD9xBISI/assets/images/thoughtspot/full_app_embed_spotter.png?fit=max&auto=format&n=3RotvmSfKD9xBISI&q=85&s=425353287f8c03c7d94725112a16d013" alt="Spotter Homepage embed" data-og-width="1480" width="1480" data-og-height="1116" height="1116" data-path="assets/images/thoughtspot/full_app_embed_spotter.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/interworks/3RotvmSfKD9xBISI/assets/images/thoughtspot/full_app_embed_spotter.png?w=280&fit=max&auto=format&n=3RotvmSfKD9xBISI&q=85&s=2fffb2fe88ff792ec7303c6e548c87c4 280w, https://mintcdn.com/interworks/3RotvmSfKD9xBISI/assets/images/thoughtspot/full_app_embed_spotter.png?w=560&fit=max&auto=format&n=3RotvmSfKD9xBISI&q=85&s=0a87205b379521d4c5b1b39022009ae2 560w, https://mintcdn.com/interworks/3RotvmSfKD9xBISI/assets/images/thoughtspot/full_app_embed_spotter.png?w=840&fit=max&auto=format&n=3RotvmSfKD9xBISI&q=85&s=254001006be893cb36c2fd7af8c6ebae 840w, https://mintcdn.com/interworks/3RotvmSfKD9xBISI/assets/images/thoughtspot/full_app_embed_spotter.png?w=1100&fit=max&auto=format&n=3RotvmSfKD9xBISI&q=85&s=819342b642e6234f6d4049d103a4bcc8 1100w, https://mintcdn.com/interworks/3RotvmSfKD9xBISI/assets/images/thoughtspot/full_app_embed_spotter.png?w=1650&fit=max&auto=format&n=3RotvmSfKD9xBISI&q=85&s=13c6a12905a205a2fb8c7f3f254f4fbb 1650w, https://mintcdn.com/interworks/3RotvmSfKD9xBISI/assets/images/thoughtspot/full_app_embed_spotter.png?w=2500&fit=max&auto=format&n=3RotvmSfKD9xBISI&q=85&s=1de8888b8e8d60a74fcd329952fd677d 2500w" />

## Adding the ThoughtSpot Full App Embed to the Curator Frontend

Once configured in the Page Builder, the ThoughtSpot Full App Embed will be displayed on your page, providing users
with access to the complete ThoughtSpot application interface. Users will need appropriate ThoughtSpot permissions
on the configured Org to access the embedded application.

You can make the page containing the Full App Embed more discoverable by:

1. Adding it to your [navigation](/site_content_design/menus/managing_menus).
2. Creating a [tile](/site_content_design/pages/tiles) that links to the page.
3. Adding keywords to the page so it can be easily found via Curator's search or in the [explorer](/site_content_design/pages/explorer).
