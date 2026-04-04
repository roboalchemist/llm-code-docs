# Source: https://vega.github.io/vega-lite/

Title: A High-Level Grammar of Interactive Graphics

URL Source: https://vega.github.io/vega-lite/

Markdown Content:
**Vega-Lite** is a high-level grammar of interactive graphics. It provides a concise, declarative JSON syntax to create an expressive range of visualizations for data analysis and presentation.

Vega-Lite specifications describe visualizations as encoding mappings from data to **properties of graphical marks** (e.g., points or bars). The Vega-Lite compiler **automatically produces visualization components** including axes, legends, and scales. It determines default properties of these components based on a set of **carefully designed rules**. This approach allows Vega-Lite specifications to be concise for quick visualization authoring, while giving user control to override defaults and customize various parts of a visualization. As we also designed Vega-Lite to support data analysis, Vega-Lite supports both **data transformations** (e.g., aggregation, binning, filtering, sorting) and **visual transformations** (e.g., stacking and faceting). Moreover, Vega-Lite specifications can be **composed** into layered and multi-view displays, and made **interactive with selections**. [Get started Latest Version: 6.4.2](https://vega.github.io/vega-lite/tutorials/getting_started.html)[Try online](https://vega.github.io/editor/#/examples/vega-lite/bar)

Compared to [Vega](https://vega.github.io/vega), Vega-Lite provides a more concise and convenient form to author common visualizations. As Vega-Lite can compile its specifications to Vega specifications, users may use Vega-Lite as the _primary_ visualization tool and, if needed, transition to use the lower-level Vega for advanced use cases.

Check out the [documentation](https://vega.github.io/vega-lite/docs/) and take a look at our [example gallery](https://vega.github.io/vega-lite/examples/). Follow us on [Bluesky](https://bsky.app/profile/vega-vis.bsky.social) to stay informed about updates.

[](https://vega.github.io/vega-lite/#example)Example
----------------------------------------------------

With Vega-Lite, we can start with a [bar chart of the average monthly precipitation](https://vega.github.io/vega-lite/) in Seattle, [overlay a rule for the overall yearly average](https://vega.github.io/vega-lite/), and have it represent [an interactive moving average for a dragged region](https://vega.github.io/vega-lite/).

```
{
  "data": {"url": "data/seattle-weather.csv"},
  "mark": "bar",
  "encoding": {
    "x": {
      "timeUnit": "month",
      "field": "date",
      "type": "ordinal"
    },
    "y": {
      "aggregate": "mean",
      "field": "precipitation"
    }
  }
}
```

```
{
  "data": {"url": "data/seattle-weather.csv"},
  "layer": [{
    "mark": "bar",
    "encoding": {
      "x": {
        "timeUnit": "month",
        "field": "date",
        "type": "ordinal"
      },
      "y": {
        "aggregate": "mean",
        "field": "precipitation",
        "type": "quantitative"
      }
    }
  }, {
    "mark": "rule",
    "encoding": {
      "y": {
        "aggregate": "mean",
        "field": "precipitation",
        "type": "quantitative"
      },
      "color": {"value": "firebrick"},
      "size": {"value": 3}
    }
  }]
}
```

```
{
  "data": {"url": "data/seattle-weather.csv"},
  "layer": [{
    "params": [{
      "name": "brush",
      "select": {"type": "interval", "encodings": ["x"]}
    }],
    "mark": "bar",
    "encoding": {
      "x": {
        "timeUnit": "month",
        "field": "date",
        "type": "ordinal"
      },
      "y": {
        "aggregate": "mean",
        "field": "precipitation",
        "type": "quantitative"
      },
      "opacity": {
        "condition": {
          "param": "brush", "value": 1
        },
        "value": 0.7
      }
    }
  }, {
    "transform": [{
      "filter": {"param": "brush"}
    }],
    "mark": "rule",
    "encoding": {
      "y": {
        "aggregate": "mean",
        "field": "precipitation",
        "type": "quantitative"
      },
      "color": {"value": "firebrick"},
      "size": {"value": 3}
    }
  }]
}
```

[](https://vega.github.io/vega-lite/#additional-links)Additional Links
----------------------------------------------------------------------

*   Award winning [research paper](https://idl.cs.washington.edu/papers/vega-lite) and [video of our OpenVis Conf talk](https://www.youtube.com/watch?v=9uaHRWj04D4) on the design of Vega-Lite
*   [The about page for the Vega project](https://vega.github.io/vega/about/)
*   Watch Dr. Lace Padilla’s [series of videos on Vega-Lite](https://www.youtube.com/playlist?list=PLe9dkYfBBHFktHd5Tn2FAlADEbQ70kUSp)
*   Listen to a Data Stories episode about [Declarative Visualization with Vega-Lite and Altair](http://datastori.es/121-declarative-visualization-with-vega-lite-and-altair-with-dominik-moritz-jacob-vanderplas-kanit-ham-wongsuphasawat/)
*   Learn about visualization design principles in the [Visualization curriculum](https://observablehq.com/@uwdata/data-visualization-curriculum?collection=@uwdata/visualization-curriculum)
*   [JSON schema](http://json-schema.org/) specification for [Vega-Lite](https://github.com/vega/schema) ([latest](https://vega.github.io/schema/vega-lite/v6.json))
*   Ask questions about Vega-Lite on [Stack Overflow](https://stackoverflow.com/tags/vega-lite) or [Slack](https://bit.ly/join-vega-slack-2022)
*   Fork our [Observable Notebook](https://beta.observablehq.com/@domoritz/vega-lite-demo).

[](https://vega.github.io/vega-lite/#users)Users
------------------------------------------------

Vega-Lite is used by thousands of data enthusiasts, developers, journalists, data scientists, teachers, and researchers across many organizations. Here are some of them. Learn about integrations on our [ecosystem page](https://vega.github.io/vega-lite/ecosystem.html).

*   ![Image 1: Airbnb](https://vega.github.io/vega-lite/static/logo_airbnb.png)
*   ![Image 2: Apple](https://vega.github.io/vega-lite/static/logo_apple.png)
*   ![Image 3: Databricks](https://vega.github.io/vega-lite/static/logo_databricks.png)
*   ![Image 4: Google](https://vega.github.io/vega-lite/static/logo_google.png)
*   ![Image 5: Microsoft](https://vega.github.io/vega-lite/static/logo_ms.png)
*   ![Image 6: Tableau](https://vega.github.io/vega-lite/static/logo_tableau.png)
*   ![Image 7: Berkeley](https://vega.github.io/vega-lite/static/logo_berkeley.png)
*   ![Image 8: Carnegie Mellon University](https://vega.github.io/vega-lite/static/logo_cmu.png)
*   ![Image 9: CERN](https://vega.github.io/vega-lite/static/logo_cern.png)
*   ![Image 10: JupyterLab](https://vega.github.io/vega-lite/static/logo_jlab.png)
*   ![Image 11: LA Times](https://vega.github.io/vega-lite/static/logo_la_times.png)
*   ![Image 12: Massachusetts Institute of Technology](https://vega.github.io/vega-lite/static/logo_mit.png)
*   ![Image 13: University of Washington](https://vega.github.io/vega-lite/static/logo_uw.png)

[](https://vega.github.io/vega-lite/#team)Team
----------------------------------------------

The development of Vega-Lite is led by the alumni and members of the [University of Washington Interactive Data Lab](https://idl.cs.washington.edu/) (UW IDL), including [Kanit “Ham” Wongsuphasawat](https://kanitw.github.io/) (now at Databricks), [Dominik Moritz](https://bsky.app/profile/domoritz.de) (now at CMU / Apple), [Arvind Satyanarayan](https://bsky.app/profile/arvind.bsky.social) (now at MIT), and [Jeffrey Heer](https://bsky.app/profile/jheer.org) (UW IDL).

Vega-Lite gets significant contributions from its community. Please see the [contributors page](https://github.com/vega/vega-lite/graphs/contributors) for the full list of contributors.
