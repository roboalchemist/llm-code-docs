# Start and stop a streaming fragment

Streamlit lets you turn functions into [fragments](https://docs.streamlit.io/develop/concepts/architecture/fragments), which can rerun independently from the full script. Additionally, you can tell Streamlit to rerun a fragment at a set time interval. This is great for streaming data or monitoring processes. You may want the user to start and stop this live streaming. To do this, programmatically set the `run_every` parameter for your fragment.

## Applied concepts

- Use a fragment to stream live data.
- Start and stop a fragment from automatically rerunning.

## Prerequisites

- This tutorial requires the following version of Streamlit:
  ```text
  streamlit>=1.37.0
  ```
- You should have a clean working directory called `your-repository`.
- You should have a basic understanding of fragments.

## Build the example

To begin with, you'll define a function to randomly generate some data for two time series, which you'll call "A" and "B". It's okay to skip this section if you just want to copy the function.

```python
def get_recent_data(last_timestamp):
    """Generate and return data from last timestamp to now, at most 60 seconds."""
    now = datetime.now()
    if now - last_timestamp > timedelta(seconds=60):
        last_timestamp = now - timedelta(seconds=60)
    sample_time = timedelta(seconds=0.5)  # time between data points
    next_timestamp = last_timestamp + sample_time
    timestamps = np.arange(next_timestamp, now, sample_time)
    sample_values = np.random.randn(len(timestamps), 2)

    data = pd.DataFrame(sample_values, index=timestamps, columns=["A", "B"])
    return data
```

1. Start your function at the bottom of your code.

```python
show_latest_data()
```

Test out your app by clicking "Start streaming". Try adjusting the frequency of updates.

## Next steps

Try adjusting the frequency of data generation or how much data is kept in Session State. Within `get_recent_data` try setting `sample_time` with a widget.

Try using `st.plotly_chart` or `st.altair_chart` to add labels to your chart.