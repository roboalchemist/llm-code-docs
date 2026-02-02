# Annotate an Altair chart

Altair allows you to annotate your charts with text, images, and emojis. You can do this by overlaying two charts to create a layered chart.

Within the data layer, you'll add a multi-line tooltip to show information about datapoints. To learn more about multi-line tooltips, see this example in Vega-Altair's documentation. You'll add another tooltip to the annotation layer.

## Build the data layer

You'll build an interactive time-series chart of the stock prices with a multi-line tooltip. The x-axis represents the date, and the y-axis represents the stock price.

1. Import data from `vega_datasets`.
2. Define a mouseover selection event in Altair.
3. Define a basic line chart to graph the five series in your data set.
4. Draw points on the lines and highlight them based on the mouseover selection.
5. Draw a vertical rule at the location of the mouseover selection.
6. Combine the lines, points, and tooltips into a single chart.
7. Optional: Test out your code by rendering your data layer.
8. Save your file and examine the chart in your app. Use your mouse to hover over points. Observe the circle marks, vertical line, and tooltip as you hover over a point. Delete the line or keep it at the end of your app to be updated as you continue.

## Build the annotation layer

Now that you have the first chart that shows the data, you can annotate it with text and an emoji. In this section, you'll add some emojis and tooltips to mark specific points of interest.

1. Create a list of annotations.
2. Create a scatter plot with the x-axis representing the date and the y-axis representing the height (price) of each annotation.
3. Define the combined chart.
4. Display the chart in Streamlit.

## Combine the chart layers

1. Define the combined chart.
2. Display the chart in Streamlit.

## Next steps

Play around with your new app.

- If you want to use custom images instead of text or emojis to annotate your chart, you can replace the line containing `.mark_text()` with `.mark_image()`. For some URL string stored in a variable `IMAGE_URL`, you could do something like this:
- If you want to enable panning and zooming for your chart, add `.interactive()` when you define your combined chart: