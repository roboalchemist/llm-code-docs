# Source: https://docs.streamlit.io/develop/api-reference/data

# Data elements

When you're working with data, it is extremely valuable to visualize that data quickly, interactively, and from multiple different angles. That's what Streamlit is actually built and optimized for.

You can display data via [charts](/develop/api-reference/data#display-charts), and you can display it in raw form. These are the Streamlit commands you can use to display and interact with raw data.

## Dataframes

Display a dataframe as an interactive table.

```python
st.dataframe(my_data_frame)
```

## Data editor

Display a data editor widget.

```python
edited = st.data_editor(df, num_rows="dynamic")
```

## Column configuration

Configure the display and editing behavior of dataframes and data editors.

```python
st.column_config.NumberColumn("Price (in USD)", min_value=0, format="$%d")
```

## Static tables

Display a static table.

```python
st.table(my_data_frame)
```

## Metrics

Display a metric in big bold font, with an optional indicator of how the metric changed.

```python
st.metric("My metric", 42, 2)
```

## Dicts and JSON

Display object or string as a pretty-printed JSON string.

```python
st.json(my_dict)
```

## Third-party components

These are featured components created by our lovely community. For more examples and inspiration, check out our [Components Gallery](https://streamlit.io/components) and [Streamlit Extras](https://extras.streamlit.app/)!

## App testing

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

### Still have questions?

Our [FAQ](https://discuss.streamlit.io) is full of helpful information and Streamlit experts.

### Previous: Text elements

### Next: st.dataframe