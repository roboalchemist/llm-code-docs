# Source: https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/how-to/build-dynamic-skill-response/graphs-and-charts.md

# Graphs & Charts

You can create chart visualizations such as Pie Chart, Bar Chart, Dial Chart using the data in your agent. The visualizations can be used in the description of cards created from JS or in webview with HTML source.

{% hint style="info" %}
**Note**: The visualizations may not render on other channels such as Facebook and Twitter.
{% endhint %}

### Dial chart

You can find the source [here](https://github.com/avaamo/bot-response-visualizations/blob/master/dial-chart.html). Modify the size of the SVG and viewBox property values, as required.

{% hint style="info" %}
**Note**: Pass one of these values to the *getChart* method \[*low*, *moderately\_low*, *moderate*, *moderately\_high*, *high*] and the pointer points to the respective part of the dial.
{% endhint %}

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M69hMczO_Yc87dxfZGi%2F-M69pmOq29s_fJqGBbJC%2Fdial-chart.png?alt=media\&token=81fe7010-501f-41f4-9938-a3f6d80f5609)

### Pie chart

Find the source code [here](https://github.com/avaamo/bot-response-visualizations/blob/master/pie-chart.html). The pie chart has its own legend too. The color of each slice of pie is customizable. The size of the overall pie is also customizable.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M69hMczO_Yc87dxfZGi%2F-M69q56-FW4tAq9r_Cmw%2Fpie-chart.png?alt=media\&token=8e1d6905-eab9-472a-8ef7-c66e44d24baf)

### Bar chart

Find the source [here](https://github.com/avaamo/bot-response-visualizations/blob/master/bar-chart.html). The bar chart has its own legend too. The color of each bar is customizable.&#x20;

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M69hMczO_Yc87dxfZGi%2F-M69qpVkMBaFsJeUKxs3%2Fbar-chart.png?alt=media\&token=85530985-fcf2-4692-ab13-aa3aee7e347c)
