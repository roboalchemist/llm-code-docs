# Source: https://docs.curator.interworks.com/embedding_using_analytics/report_builder/powerpoint.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.curator.interworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# PowerPoint

> Generate PowerPoint presentations from dashboard content using Report Builder for professional report delivery.

The [Report Builder](/embedding_using_analytics/report_builder/overview_and_enabling_report_builder)
functionality in Curator allows users to create Microsoft PowerPoint presentations of Tableau dashboards. We'll guide
you through setting up a template for these presentations, which can be automatically applied to your exported images.

## Setting Up PowerPoint Template

1. Create or open an existing Microsoft PowerPoint presentation.
2. Access Slide Master by clicking on the "View" ribbon and then the "Slide Master" button.
3. Identify Blank Layout: Look for the Blank layout in the Slide Master. This layout is used by the [Report Builder](/embedding_using_analytics/report_builder/overview_and_enabling_report_builder).
   * If Blank Layout is Missing:
     * Right-click in the left pane and select "Insert Layout".
     * Right-click on the newly created layout and select "Rename Layout".
     * In the pop-up, change the name to "Blank" and click "Rename".
4. Save Template: Save the presentation in an easy-to-find location on your computer.

**Note**: Powerpoint Presentations cannot contain more than one Slide Master.  In addition, some images formats are
unsupported as they become blended with Dashboard images on export.  If you need to convert these images, typically
clicking the "Convert to shape" button on the "Graphics Format" tab will suffice.

## Applying Template in Portal Settings

1. Access Portal Settings: Navigate to Settings > Portal Settings > Layout in your portal's backend.
2. Upload Template: In the "Powerpoint Template" field, upload the saved PowerPoint presentation.
3. Save Changes: Click the "Save" button to apply the template.

## Group Override settings

Utilize group override functionality to apply different templates for various Tableau user groups, adding excitement
and customization to presentations.
