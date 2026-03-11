# Source: https://docs.axonius.com/docs/text-only.md

# Text

Use the Text widget to display static text in a tile on the dashboard. You can also select the perform standard formatting changes (size, color, bold, italics, alignment, etc.) on the text to create visually appealing texts to display on your Dashboards. This can be used to add titles or section dividers to your dashboards. You can also add [clickable hyperlinks](/docs/text-only#using-hyperlinks-in-text-charts) to navigate to other platform pages or external sources.

<Image alt="TextFormatting" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/TextFormatting.png" />

**To configure a text widget**

1. In the **Chart title** text box, enter a title for the chart.
2. In the **Description** text box, you can add an optional description.
3. From the **Widget** drop-down, select **Text**.
4. In the right pane, enter the message you want displayed.
5. Use the options on the Formatting toolbar to apply any formatting you want to the text.
6. Select if you want to display the chart title in the dashboard and if you want the text displayed against a transparent background.
7. Click **Save**. The widget is added to the Dashboard.

<Image align="center" alt="FormattedSectionText" border={false} width="400px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/FormattedSectionText.png" />

## Using Hyperlinks in Text Charts

Use hyperlinks in Text widgets to include external references or internal navigation directly within dashboard content.

**Supported Link Types**
There are two types of links: **external paths** and **relative paths**.

* **External Path** - A hyperlink is treated as *external* if it begins with `http://` or `https://`. These links open in a new browser tab.
  For example: `[https://www.google.com](https://www.google.com/)`

* **Relative Path** - A hyperlink that does **not** begin with `http://` or `https://` is treated as a *relative path*. This type of link is interpreted relative to the Axonius instance URL and is useful for linking to internal pages within the platform.
  Examples:

  * `/dashboard/657aDESHE75f1dES#%^a0?chartId=682cADFE5b10143adDD33e981` — directs the user to a specific dashboard and highlights a chart.
  * `/case_management` — navigates the user to the Case Management page.

  Relative paths are helpful for creating guided workflows or cross-linking different areas within the Axonius platform. However, they should not be used for linking to external websites.**Best Practices for Adding Links**

<Callout icon="📘" theme="info">
  Notes

  To ensure hyperlinks work as intended:

  * Use `https://` or `http://` when linking to external websites.

  * Use relative paths (starting with `/`) to link to specific pages within the Axonius interface.

  * Avoid entering partial domains like `[www.example.com](http://www.example.com/)` — they are treated as relative paths and may not work as expected.
</Callout>

**To insert a hyperlink into a text widget:**

1. When in edit mode of a text widget, enter the text of the hyperlink and then select that text.
2. Click the hyperlink icon ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/hyperlinkicon.png) in the formatting toolbar.
3. In the link box, enter the link according to the rules described above and click **Save**.

<Image align="center" alt="HyperlinkChartSave.png" border={false} width="350px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/HyperlinkChartSave.png" />

Hyperlinks are formatted in customary blue and underlined.

4. When you are finished configuring the widget, click **Save** at the bottom of the chart edit window.
   5\. To remove a link, click in the link text. Then, in the link window,  click **Remove**.
   6\. To edit a link, click in the link text. Then, in the link window,  click **Edit**. Enter the correct link and click **Save**.