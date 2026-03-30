# Source: https://docs.curator.interworks.com/embedding_using_analytics/tableau_dashboards/url_action_overrides_link_target.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.curator.interworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# URL Action Overrides (Link Target)

> Configure URL actions in Tableau dashboards to control link behavior and user navigation within Curator.

When a URL action gets triggered in Curator, there are different settings that allow Curator to handle these actions in
a more sophisticated manner directing your users to the location they want to end up without much intervention in the
middle.  You can find a description of the available options at the bottom of this page.

## Set the Link Target

1. Login to the backend of your Curator instance (e.g. `https://www.curatorexample.com/backend`).
2. Navigate to the **Tableau** > **Dashboards** section from the left-hand menu.
3. Click the Dashboard you'd like to edit from the list page.
4. Under the "Advanced" tab, look for the *Embedded Options* section.
5. Chang the Link Target field to the desired option (see below for descriptions)
6. Click the "Save" button.

### Available Options

*Default*
By default, Curator handles the URL as defined in the Tableau Dashboard.

*Self*
The URL Action defined in the Tableau Dashboard will load within the embedded frame on the page keeping the user in the
same location.

*Parent*
The URL Action defined in the Tableau Dashboard will change the location of the current browser tab the user is on
navigating them away from the current page.

*Blank*
The URL Action defined in the Tableau Dashboard will open in a new browser tab.

*Curator Detect*
Curator will look at the value of the URL you have defined in your Dashboard's URL Action and if it is a Dashboard that
is hosted on the Tableau Server your Curator instance is connected to, it will look to see if that Dashboard is
available in the current user's navigation within Curator. If accessible, it will direct them to the Curator page where
that Dashboard is hosted in the same browser tab.  If not, it will direct them to the URL opening up a new browser tab.

*Curator Detect New Tab*
The same behavior as Curator Detect, only in both scenarios it opens up a new tab.

### Passing Filters through URL Actions

When passing filters through URL Actions on a Tableau Dashboard, Tableau has good documentation on how to set this up
[here](https://help.tableau.com/current/server-linux/en-gb/actions_url.htm?source=productlink#Using). When you want to
enable your users to send multiple values apply the following settings to your URL Action in Tableau and Curator will
pick up the values correctly:

1. Open the `Data Values`section below the URL field in the URL Action dialog in Tableau.
2. Check the box for *Encode data values that URLs do not support*.
3. Check the box for *Allow multiple values via URL parameters*.
4. Set the *Value Delimiter* to be three pipes (`|||`).
5. Set the *Delimiter Escape Character* to be a backslash (`\`).
6. Click OK to save the URL Action and publish your Dashboard to Tableau Server.
