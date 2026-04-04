# Source: https://docs.edgeimpulse.com/studio/projects/data-acquisition/multi-label.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Multi-label

The multi-label feature brings considerable value by preserving the context of longer data samples, simplifying data preparation, and enabling more efficient and effective data analysis.

The first improvement is in the way you can analyze and process complex datasets, especially for applications where context and continuity are crucial. With this feature, you can maintain the integrity of longer-duration samples, such as hour-long exercise sessions or night-long sleep studies, without the need to segment these into smaller fragments every time there is a change in activity. This holistic view not only preserves the context but also provides a richer data set for analysis.

Then, the ability to select window sizes directly in Edge Impulse addresses a common pain point - data duplication. Without the multi-label feature, you need to pre-process data, either externally or using [transformation jobs](/studio/organizations/custom-blocks/custom-transformation-blocks), creating multiple copies of the same data with different window sizes to determine the optimal configuration. This process is not only time-consuming but also prone to errors and inefficiencies. With multi-label samples, adjusting the window size becomes a simple parameter change in the "[Impulse design](/studio/projects/impulse-design)", streamlining the process significantly. This flexibility saves time, reduces the risk of errors, and allows for more dynamic experimentation with data, leading to potentially more accurate and insightful models.

<Frame caption="Multi-label">
  <img src="https://mintcdn.com/edgeimpulse/UMiv9oezYdq-CZ8W/.assets/images/studio-data-acquisition-multi-label-2.png?fit=max&auto=format&n=UMiv9oezYdq-CZ8W&q=85&s=0375c45bbf2d7b88ba0a3a2ebdfc1f8d" width="1600" height="972" data-path=".assets/images/studio-data-acquisition-multi-label-2.png" />
</Frame>

## Detecting key events in multi-label samples

When working with time-series data labeled using the multi-label format, detecting short-duration or critical events (e.g. tamper detection, fall detection or short noises among others) is possible. Edge Impulse provides flexible strategies for assigning labels to windows of data during training and inference to ensure the events represented.

During the data acquisition process, it's important to understand the available labeling strategies. Choosing the right approach for handling multi-label events ensure accurate detections. The labeling strategies are selected when designing your impulse in the [Create Impulse](/studio/projects/impulse-design) screen. You need to define your appropriate strategy to detect multi-label events in your data.

<Frame caption="Handling multi-label samples option">
  <img src="https://mintcdn.com/edgeimpulse/yWZVbRGeek_I_Jpe/.assets/images/input-block-multi-label-samples-field.png?fit=max&auto=format&n=yWZVbRGeek_I_Jpe&q=85&s=986028316b97b6dcaec4751cf1cc8b3c" width="467" height="1000" data-path=".assets/images/input-block-multi-label-samples-field.png" />
</Frame>

### Use label at the end of the window

This strategy assigns the label that is active at the end of each window as the label for the entire window. It works well for scenarios where the primary interest lies in the resulting state or activity of the window such as recognizing sustained motions or transitions.

If a sample transitions from `idle` to `running` within a window, and the last timestamp in the window corresponds to `running`, the window will be labeled as `running`.

### Use label X if anywhere present in the window

This strategy assigns a label to the window if a specific event label is present anywhere within the windows' duration (e.g. `tamper`, `fall`, etc). It is particularly useful for detecting short or sparse events that may not occupy the full window but are critical to capture when they occur.

With this option, you can configure which label(s) to prioritize. If the selected label is found within any part of the window, the window will be assigned to that label, even if the short event occurs alongside other labels.

<Frame caption="Use label X if anywhere present in the window">
  <img src="https://mintcdn.com/edgeimpulse/b53JLZcI-O3Jueox/.assets/images/tamper-label-edgeimpulse.png?fit=max&auto=format&n=b53JLZcI-O3Jueox&q=85&s=b54135b5a4849bc12a4e44e9a229cb26" width="1462" height="868" data-path=".assets/images/tamper-label-edgeimpulse.png" />
</Frame>

This approach ensures better coverage for rare or time-sensitive events and improves the model sensitivity to important transitions or anomalies.

In the situation when multiple selected label appear within the same window, the label with the highest number of occurrences will be assigned to that window. And in the case that none of the selected labels are found, the system defaults to using the label at the end of the window.

## Upload multi-label samples

### 1. Using the CSV Wizard

If your dataset is in the CSV format and contains a label column, the [CSV Wizard](/studio/projects/data-acquisition/csv-wizard) is probably the easiest method to import your multi-label data.

For example:

```
seconds_elapsed,    accX,   accY,    accZ,    label

0.00,               0.14642,-0.01645,-0.00858,idle
0.16,               0.15051,-0.01149,-0.00345,idle
0.32,               0.15546,-0.02141,-0.00342,idle
...
20.48,              0.14347,-0.03758,-0.00369,running
20.56,              0.13447,-0.01657,-0.01520,running
20.72,              0.11453,-0.00961,-0.01021,running
```

<Frame caption="Multi-label workflow">
  <img src="https://mintcdn.com/edgeimpulse/knIbhhrHdvFnasBb/.assets/images/multi-label.gif?s=194ce0db229fd093f55e1f54406038dd" width="1544" height="936" data-path=".assets/images/multi-label.gif" />
</Frame>

Once your CSV Wizard is configured, you can use the [Studio Uploader](/studio/projects/data-acquisition/uploader), the [CLI Uploader](/tools/clis/edge-impulse-cli/uploader) or the [Ingestion API](/apis/ingestion):

### 2. Using Edge Impulse `info.labels` description file

The other way is to create a `info.labels` file, present in your dataset. Edge Impulse will automatically detect it when you upload your dataset and will use this file to set the labels.

The `info.labels` looks like the following:

```
{
    "version": 1,
    "files": [{
        "path": "audio1.wav",
        "category": "split",
        "label": {
                "type": "multi-label",
                "labels": [
                    {
                        "label": "noise",
                        "startIndex": 0,
                        "endIndex": 5000
                    },
                    {
                        "label": "nominal_mode",
                        "startIndex": 5001
                        "endIndex": 60000
                    },
                    {
                        "label": "defect",
                        "startIndex": 60001
                        "endIndex": 60200
                    }
                ],
        "metadata": {
            "site_collected": "Factory_01"
            }
        }
    },
    {
        "path": "audio2.wav",
        "category": "split",
        "label": {
                "type": "multi-label",
                "labels": [
                    {
                        "label": "noise",
                        "startIndex": 0,
                        "endIndex": 2000
                    },
                    {
                        "label": "nominal_mode",
                        "startIndex": 2001
                        "endIndex": 40000
                    }
                ],
        "metadata": {
            "site_collected": "Factory_02"
            }
        }
    },
    ]
}
```

<Info>
  #### Tip

  You can export a public project dataset that uses the multi-label feature to understand how the `info.labels` is structured.

  Check the [Resources](/studio/projects/data-acquisition/multi-label#resources) section for multi-label public projects.
</Info>

Once you have your `info.labels` file available, to upload it, you can use:

#### The [Studio Uploader](/studio/projects/data-acquisition/uploader):

The Studio Uploader will automatically detect the `info.labels` file:

<Frame caption="Studio Uploader multi-label dataset">
  <img src="https://mintcdn.com/edgeimpulse/knIbhhrHdvFnasBb/.assets/images/multi-label-uploader.png?fit=max&auto=format&n=knIbhhrHdvFnasBb&q=85&s=d09b4b103fea7d87128bdc2b659e6dab" width="1569" height="1000" data-path=".assets/images/multi-label-uploader.png" />
</Frame>

#### The [CLI Uploader](/tools/clis/edge-impulse-cli/uploader):

```
> edge-impulse-uploader * --info-file info.labels

Edge Impulse uploader v1.23.0
Endpoints:
    API:         https://studio.edgeimpulse.com
    Ingestion:   https://ingestion.edgeimpulse.com

Upload configuration:
    Label:       Not set, will be inferred from file name
    Category:    training
    Project:     Example Multi-label upload (ID: XXXXX)

[ 1/11] Uploading training/machine_multilabel_8.json OK (1589 ms)
[ 2/11] Uploading testing/machine_multilabel_3.json OK (2024 ms)
[ 3/11] Uploading training/machine_multilabel_6.json OK (2176 ms)
[ 4/11] Uploading training/machine_multilabel_2.json OK (2224 ms)
[ 5/11] Uploading testing/machine_multilabel_1.json OK (2394 ms)
[ 6/11] Uploading training/machine_multilabel_8.json OK (2395 ms)
[ 7/11] Uploading training/machine_multilabel_9.json OK (2485 ms)
[ 8/11] Uploading training/machine_multilabel_7.json OK (2603 ms)
[ 9/11] Uploading testing/machine_multilabel_4.json OK (2617 ms)
[10/11] Uploading training/machine_multilabel_11.json OK (3426 ms)
[11/11] Uploading training/machine_multilabel_10.json OK (3488 ms)

Done. Files uploaded successful: 11. Files that failed to upload: 0.
```

### 2. Using Edge Impulse `structured_labels.labels` description file

If you want to use the [Ingestion API](/apis/ingestion), you need to use the `structured_labels.labels` format:

The `structured_labels.labels` format looks like the following:

```
{
    "version": 1,
    "type": "structured-labels",
    "structuredLabels": {
        "updown.3.json": [{
            "startIndex": 0,
            "endIndex": 300,
            "label": "first_label"
        }, {
            "startIndex": 301,
            "endIndex": 621,
            "label": "second_label"
        }]
    }
}
```

Then you can run the following command:

```
curl -X POST \
    -H "x-api-key: $EI_PROJECT_API_KEY" \
    -H "Content-Type: multipart/form-data" \
    -F "data=@updown.3.json" \
    -F "data=@structured_labels.labels" \
    https://ingestion.edgeimpulse.com/api/training/files
```

You can have a look at this tutorial for a better understanding: [Ingest multi-label data with Edge Impulse API](/tutorials/tools/apis/ingestion/ingest-structured-label-data).

### Visualizing multi-label samples

<Frame caption="Multi-label sample preview">
  <img src="https://mintcdn.com/edgeimpulse/VpF_Einsy6qHCvhZ/.assets/images/data-acquisition-sample-preview-time-series-multi-label.png?fit=max&auto=format&n=VpF_Einsy6qHCvhZ&q=85&s=968590aa74dab7a7bd12f5c3ac5c41bb" width="1344" height="956" data-path=".assets/images/data-acquisition-sample-preview-time-series-multi-label.png" />
</Frame>

Please note that you can also hide the sensors in the graph:

<Frame caption="Multi-label sample preview - Hide sensors">
  <img src="https://mintcdn.com/edgeimpulse/VpF_Einsy6qHCvhZ/.assets/images/data-acquisition-sample-preview-time-series-multi-label-hide-sensor.png?fit=max&auto=format&n=VpF_Einsy6qHCvhZ&q=85&s=b3954266badfce4276881bf031f4bc2b" width="1344" height="956" data-path=".assets/images/data-acquisition-sample-preview-time-series-multi-label-hide-sensor.png" />
</Frame>

### Edit multi-label samples

To edit the labels using the UI, click **⋮** -> **Edit labels**. The following model will appear:

<Frame caption="Edit labels">
  <img src="https://mintcdn.com/edgeimpulse/UMiv9oezYdq-CZ8W/.assets/images/studio-data-acquition-edit-labels.png?fit=max&auto=format&n=UMiv9oezYdq-CZ8W&q=85&s=502e2381140c480bcf8325ebc12ce634" width="1585" height="1000" data-path=".assets/images/studio-data-acquition-edit-labels.png" />
</Frame>

Please note that you will need to provide continuous and non-overlapping labels for the full length of your data sample.

The format is the like following:

```
[
    {
        "label": "label 1",
        "startMs": 0,
        "endMs": 2000
    },
    {
        "label": "label 2",
        "startMs": 2001,
        "endMs": 4000
    },
    {
        "label": "label 3",
        "startMs": 4001,
        "endMs": 4500
    }
]
```

### Classify multi-label data

In the **Live classification** tab, you can classify your multi-label test samples:

<Frame caption="Test multi-label sampled">
  <img src="https://mintcdn.com/edgeimpulse/knIbhhrHdvFnasBb/.assets/images/multi-label-test-data.gif?s=811b86236d5fdc1586c1d8e76a7d8ad5" width="1788" height="890" data-path=".assets/images/multi-label-test-data.gif" />
</Frame>

### Limitations

* Labeling UI is available but is only text-based.
* Overlapping labels are not supported
* The entire data sample needs to have a label, you cannot leave parts unlabeled.

Please, leave us a note on the forum or feedback using the **"?"** widget (bottom-right corner) if you see a need or an issue. This can help us prioritize the development or improvement of the features.

### Resources

#### Public projects

* [Coffee Machine Stages - Multi-label data](https://studio.edgeimpulse.com/public/315514/latest)


Built with [Mintlify](https://mintlify.com).