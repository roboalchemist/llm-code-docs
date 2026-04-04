# Source: https://kreya.app/docs/scripting-and-tests/samples/previews/preview_sample_chart.md

# Visualize Data as a chart [Pro / Enterprise](/pricing.md)

This sample demonstrates how to use Kreya's scripting capabilities to visualize REST API response data as a chart using [Apache ECharts](https://echarts.apache.org/).

## Overview[​](#overview "Direct link to Overview")

The API returns a simple JSON response with labels and values. The script processes this data and renders it as a bar chart in a preview tab.

### Example API Response[​](#example-api-response "Direct link to Example API Response")

```
[
  { "label": "Value 0", "value": 10 },
  { "label": "Value 1", "value": 20 },
  { "label": "Value 2", "value": 15 }
]
```

### Script[​](#script "Direct link to Script")

The following operation script listens for the API call completion, processes the response, and renders a bar chart:

```
kreya.rest.onCallCompleted(async resp => await kreya.preview.html(`
    <html>
      <body>
        <div id="chart" style="width: 100%; height: 100%;"></div>
        <script src="https://cdn.jsdelivr.net/npm/echarts@5.6.0/dist/echarts.min.js"></script>
        <script>
          const chart = echarts.init(document.getElementById('chart'));
          chart.setOption({
              title: {
                text: 'Values'
              },
              animation: false,
              xAxis: {
                type: 'category',
                data: ${JSON.stringify(resp.response.content.map(d => d.label))}
              },
              yAxis: {
                type: 'value'
              },
              series: [{
                type: 'bar',
                data: ${JSON.stringify(resp.response.content.map(d => d.value))}
              }]
          });
          window.addEventListener('resize', () => chart.resize());
        </script>
      </body>
    </html>
    `, 'Data'));
```

### How it works[​](#how-it-works "Direct link to How it works")

1. **API call completion**: The script listens for the completion of an API call using `kreya.rest.onCallCompleted`.
2. **Data processing**: The API response is parsed to extract labels and values for the chart.
3. **Chart rendering**: The script dynamically generates an HTML page with a `<div>` for the chart and includes the Apache ECharts library.
4. **Chart configuration**: The chart is configured with a title, x-axis (categories), y-axis (values), and a bar series.
5. **Responsive design**: The chart resizes automatically when the window size changes.

### Output[​](#output "Direct link to Output")

When the script runs, the chart will look similar to this:

![Screenshot of the chart preview](/assets/ideal-img/scripting-preview-html-chart.8e0535d.400.png)
