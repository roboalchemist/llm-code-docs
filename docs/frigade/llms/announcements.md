# Source: https://docs.frigade.com/guides/announcements.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.frigade.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Guide: Product Announcements

<Frame className="h-96 items-center px-4">
  <img
    src="https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/components/announcement.svg?fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=1feb6c3c3162ad5dcfb671cee05b2720"
    style={{
                                                    width: '350px',
                                                    }}
    data-og-width="470"
    width="470"
    data-og-height="533"
    height="533"
    data-path="images/components/announcement.svg"
    data-optimize="true"
    data-opv="3"
    srcset="https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/components/announcement.svg?w=280&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=fa0489f75065c31f350c1bae87fb694d 280w, https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/components/announcement.svg?w=560&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=9c312391ce3bead7af2a56d8091fba32 560w, https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/components/announcement.svg?w=840&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=160d89e44ac348fcd7acda99c3c72fd1 840w, https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/components/announcement.svg?w=1100&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=aecd9e5384c9c04f4d4088a4e118c861 1100w, https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/components/announcement.svg?w=1650&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=1d46eb5279067aa5749f69eca67d26e7 1650w, https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/components/announcement.svg?w=2500&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=d2621dab38c40ab54856d4019ca57730 2500w"
  />
</Frame>

## Targeting announcements

You can target [announcements](/component/announcement) to specific groups of users using the [Targeting](/platform/targeting) section on the flow detail page.
By default, an announcement will show up for all users once the flow code is live in production.

## Launching additional announcements without code changes

We recommend using the [Dialogs Collection](/platform/collections) to launch new announcements without updating your product codebase. The Dialogs Collection is built-in to the Frigade SDK and can be used to launch Frigade Announcements, Surveys, and other Dialog-based components.

## Launching another Flow from an Announcement

You may want to launch another Flow when a user clicks on the primary button of a different Flow. For example, you can launch a tour Flow when a user clicks on the primary button of an announcement. You can achieve this my modifying the [Targeting](/platform/targeting) of the tour Flow directly in the Frigade dashboard, locating the given announcement under **Flows** and selecting **Completed** (typically initiated by the primary button) or **Dismissed** (if the user clicks the X button in the announcement).

<Frame>
  <img src="https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/guides/announcement/announcement-launch-tour.png?fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=0ed035d90662d8aa9f2d1949d08c6fc3" data-og-width="1051" width="1051" data-og-height="610" height="610" data-path="images/guides/announcement/announcement-launch-tour.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/guides/announcement/announcement-launch-tour.png?w=280&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=a5d00c1de983ab24674affc473944955 280w, https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/guides/announcement/announcement-launch-tour.png?w=560&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=80735621f0800fe1958ef45b6c781a5f 560w, https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/guides/announcement/announcement-launch-tour.png?w=840&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=b06efb5a4f391087cc1b152062e3a93c 840w, https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/guides/announcement/announcement-launch-tour.png?w=1100&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=ffe1eb01da8245cd28bbc9e590bd1cbc 1100w, https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/guides/announcement/announcement-launch-tour.png?w=1650&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=abe7033b8f1317666a7fc81de3c8a35b 1650w, https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/guides/announcement/announcement-launch-tour.png?w=2500&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=1b2e9fea09f8df95e1e59b3d446f1d73 2500w" />
</Frame>
