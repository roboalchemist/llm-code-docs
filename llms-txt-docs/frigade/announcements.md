# Source: https://docs.frigade.com/guides/announcements.md

# Guide: Product Announcements

<Frame className="h-96 items-center px-4">
  <img
    src="https://mintlify.s3.us-west-1.amazonaws.com/frigade-docs/images/components/announcement.svg"
    style={{
                                                    width: '350px',
                                                    }}
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
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/frigade-docs/images/guides/announcement/announcement-launch-tour.png" />
</Frame>
