# Source: https://learn.microsoft.com/en-us/clarity/click-maps

Title: Click maps

URL Source: https://learn.microsoft.com/en-us/clarity/click-maps

Markdown Content:
Important

Heatmap is only displayed on the site pages where the Clarity tracking code is installed. Check the [Setup](https://learn.microsoft.com/en-us/clarity/setup-and-installation/clarity-setup) process to know how to install it.

Click Heatmap helps you understand the critical content on the page. It also allows you to identify parts of the design user mistake for links.

Clarity uses absolute ranking across all page views. Sometimes the page impression might not show the element the user clicked.

Click Heatmaps can help you determine where your users are clicking, including the nonlinks. On PC, Clarity tracks your user clicks. Clarity tracks your user taps on mobile/tablet.

You can view click maps for a single [page](https://learn.microsoft.com/en-us/clarity/setup-and-installation/glossary-of-terms) or [group of pages](https://learn.microsoft.com/en-us/clarity/heatmaps/heatmaps-features#heatmaps-for-a-group-of-pages).

![Image 1: click maps.](https://learn.microsoft.com/en-us/clarity/media/clickmaps.png)

There are different types of Click maps available:

*   **All clicks**: shows all types of user clicks on a page, including dead clicks, rage clicks, first clicks, and last clicks.

*   **Dead clicks**: shows where users clicked on a page with no effect/response. Learn more about [Dead clicks](https://learn.microsoft.com/en-us/clarity/insights/semantic-metrics#dead-clicks).

*   **Rage clicks**: shows where users clicked rapidly in the same small area within a brief period. Learn more about [Rage clicks](https://learn.microsoft.com/en-us/clarity/insights/semantic-metrics#rage-clicks).

*   **Error clicks**: shows clicks that occur immediately before JavaScript errors. Learn more about [JavaScript errors](https://learn.microsoft.com/en-us/clarity/insights/semantic-metrics#javascript-errors).

*   **First clicks**: shows initial user clicks on a page. These clicks are useful to find out user onboarding patterns.

*   **Last clicks**: shows final user clicks on a page. These clicks are useful to find user flow patterns.

The left panel contains elements ranked by the number of clicks. Click map displays these ranks elements with the most number of clicks on the page. As you change the type, the data is updated accordingly.

Scroll to the bottom to view elements ranked further down the page. Select any clicked element to view the number of clicks (% of clicks). Expand (`>>`) to view or collapse (`<<`) to close the click data.

![Image 2: click maps left panel.](https://learn.microsoft.com/en-us/clarity/media/click-data.png)

You can also view the recordings either by selecting the **recordings icon** or by selecting **View recordings**. View recordings help you watch recordings where the element was clicked.

![Image 3: clicked element view.](https://learn.microsoft.com/en-us/clarity/media/clicked-element.png)

When you select this button an element badge appears, indicating the applied filter. Learn more about [badge labels](https://learn.microsoft.com/en-us/clarity/filters/clarity-filters#badge-labels).

![Image 4: See recordings where users clicked on this element.](https://learn.microsoft.com/en-us/clarity/media/heatmaps-to-recordings.gif)

**Note:**

*   Once applied, this filter appears on Recordings, Dashboard, and Heatmaps verticals.
*   You can access it later by saving it as a segment or sharing it.

**Badge label limitations**:

*   This filter can only be set through a heat map and can’t be selected from filters.
*   If you close the filter, you have to set it through Heatmaps again.

Copy the element to the clipboard by selecting the **copy** icon. This copies the CSS selector of an element that allows you to identify the exact element in the UI. You can use it to change the style of an element.

![Image 5: Copy element to clipboard in click maps.](https://learn.microsoft.com/en-us/clarity/media/copy-element-clickmap.png)

The top panel helps you customize the Click maps visualization:

![Image 6: Click maps top panel.](https://learn.microsoft.com/en-us/clarity/media/clickmaps-top-panel.png)

1.   **Filters**: Refer to the [Filters overview](https://learn.microsoft.com/en-us/clarity/filters/clarity-filters) to learn more.

2.   **Segments**: Refer to [Segments](https://learn.microsoft.com/en-us/clarity/filters/clarity-segments) to learn more.

3.   **Time frame**: Edit the time frame to better view the heatmaps. You can select from today, yesterday, or custom days or time frame.

4.   **Visited URL**: This autofill search bar along with regex match contains all the websites that are part of Clarity's project. You can add [multiple path filters to view heatmaps](https://learn.microsoft.com/en-us/clarity/filters/path-filters-operators#path-filters-in-heatmaps) for group of pages. The other applied filters are also shown here. You can also save the filters as a [segment](https://learn.microsoft.com/en-us/clarity/filters/clarity-segments#create-a-segment) or clear it.

5.   **Supported devices**: Choose PC/Tablet/Mobile view to understand user behavior on these devices.

6.   **Heatmaps types**: You can switch [scroll maps](https://learn.microsoft.com/en-us/clarity/heatmaps/scroll-maps), [area maps](https://learn.microsoft.com/en-us/clarity/heatmaps/area-maps), [attention maps](https://learn.microsoft.com/en-us/clarity/heatmaps/attention-maps), and [conversion maps](https://learn.microsoft.com/en-us/clarity/heatmaps/conversion-maps).

7.   **Sharing**: [Share](https://learn.microsoft.com/en-us/clarity/setup-and-installation/share-clarity) the click map with others.

8.   **Download**: [Download](https://learn.microsoft.com/en-us/clarity/heatmaps/download-heatmaps) the click map as a CSV or PNG.

9.   **Compare**: [Compare](https://learn.microsoft.com/en-us/clarity/heatmaps/heatmaps-compare) two same or different heatmaps.

10.   **Change screenshot**: [Select another screenshot](https://learn.microsoft.com/en-us/clarity/heatmaps/heatmaps-screenshots) to view click maps.

11.   **Summarize heatmaps**: [Summarize heatmaps](https://learn.microsoft.com/en-us/clarity/copilot/heatmaps-insights) to easily understand the user behaviors and trends of your website pages.

![Image 7: Click maps bottom panel.](https://learn.microsoft.com/en-us/clarity/media/clickmaps-bottom-panel.png)

1.   **Page views and Clicks**: The total number of page views and the total number of clicks on a page (or group of pages) for applied filters. The page views are limited to up to 100,000 per Heatmap.

2.   **Color scale**: Colors get warmer as the popularity of a section increases. The warmer the colors, the denser the clicks.

3.   **Show Heatmap ranks**: Toggle to either turn on or off the ranks on a heatmap.

4.   **Opacity**: This control helps change the transparency of heat when the heat covers up the text or images. You can use opacity to view the heat in red zones quickly.

![Image 8: Opacity in click map.](https://learn.microsoft.com/en-us/clarity/media/clickmap-opacity.gif)

For more answers, refer to [Heatmap FAQ](https://learn.microsoft.com/en-us/clarity/faq#heatmaps--or-heat-maps).
