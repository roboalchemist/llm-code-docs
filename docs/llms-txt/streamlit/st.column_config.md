# st.column_config

When working with data in Streamlit, the `st.column_config` class is a powerful tool for configuring data display and interaction. Specifically designed for the `column_config` parameter in [st.dataframe](/develop/api-reference/data/st.dataframe) and [st.data_editor](/develop/api-reference/data/st.data_editor), it provides a suite of methods to tailor your columns to various data types - from simple text and numbers to lists, URLs, images, and more.

Whether it's translating temporal data into user-friendly formats or utilizing charts and progress bars for clearer data visualization, column configuration not only provides the user with an enriched data viewing experience but also ensures that you're equipped with the tools to present and interact with your data, just the way you want it.

## Column configuration

### Column

Configure a generic column.

```python
Column("Streamlit Widgets", width="medium", help="Streamlit **widget** commands 🎈")
```

### Text column

Configure a text column.

```python
TextColumn("Widgets", max_chars=50, validate="^st.[a-z_]+$")
```

### Number column

Configure a number column.

```python
NumberColumn("Price (in USD)", min_value=0, format="$%d")
```

### Checkbox column

Configure a checkbox column.

```python
CheckboxColumn("Your favorite?", help="Select your **favorite** widgets")
```

### Selectbox column

Configure a selectbox column.

```python
SelectboxColumn("App Category", options=["🤖 LLM", "📈 Data Viz"])
```

### Multiselect column

Configure a multiselect column.

```python
MultiselectColumn("App Category", options=["LLM", "Visualization"])
```

### Datetime column

Configure a datetime column.

```python
DatetimeColumn("Appointment", min_value=datetime(2023, 6, 1), format="D MMM YYYY, h:mm a")
```

### Date column

Configure a date column.

```python
DateColumn("Birthday", max_value=date(2005, 1, 1), format="DD.MM.YYYY")
```

### Time column

Configure a time column.

```python
TimeColumn("Appointment", min_value=time(8, 0, 0), format="hh:mm a")
```

### JSON column

Configure a JSON column.

```python
JSONColumn("Properties", width="medium")
```

### List column

Configure a list column.

```python
ListColumn("Sales (last 6 months)", width="medium")
```

### Link column

Configure a link column.

```python
LinkColumn("Trending apps", max_chars=100, validate="^https://.*$")
```

### Image column

Configure an image column.

```python
ImageColumn("Preview Image", help="The preview screenshots")
```

### Area chart column

Configure an area chart column.

```python
AreaChartColumn("Sales (last 6 months)", y_min=0, y_max=100)
```

### Line chart column

Configure a line chart column.

```python
LineChartColumn("Sales (last 6 months)", y_min=0, y_max=100)
```

### Bar chart column

Configure a bar chart column.

```python
BarChartColumn("Marketing spend", y_min=0, y_max=100)
```

### Progress column

Configure a progress column.

```python
ProgressColumn("Sales volume", min_value=0, max_value=1000, format="$%f")