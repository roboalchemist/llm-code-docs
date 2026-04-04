# Source: https://docs.streamlit.io/develop/quick-reference/cheat-sheet

# Source: https://docs.streamlit.io/develop/concepts/app-testing/cheat-sheet

# App testing cheat sheet

## Text elements

### Headers
- Assert "My app" in at.title[0].value
- Assert "New topic" in at.header[0].value
- Assert "Interesting sub-topic" in at.subheader[0].value
- Assert len(at.divider) == 2

### Body / code
- Assert "Hello, world!" in at.markdown[0].value
- Assert "import streamlit as st" in at.code[0].value
- Assert "A cool diagram" in at.caption[0].value
- Assert "Hello again, world!" in at.text[0].value
- Assert "\\int a x^2 \\,dx" in at.latex[0].value

## Input widgets

### Button
- Assert at.button[0].value == False
- at.button[0].click().run()
- Assert at.button[0].value == True

### Checkbox
- Assert at.checkbox[0].value == False
- at.checkbox[0].check().run() # uncheck() is also supported
- Assert at.checkbox[0].value == True

### Color_picker
- Assert at.color_picker[0].value == "#FFFFFF"
- at.color_picker[0].pick("#000000").run()

### Date_input
- Assert at.date_input[0].value == datetime.date(2019, 7, 6)
- at.date_input[0].set_value(datetime.date(2022, 12, 21)).run()

### Form_submit_button
- Assert at.button[0].value == False
- at.button[0].click().run()
- Assert at.button[0].value == True

### Multiselect
- Assert at.multiselect[0].value == ["foo", "bar"]
- at.multiselect[0].select("baz").unselect("foo").run()

### Number_input
- Assert at.number_input[0].value == 5
- at.number_input[0].increment().run()

### Radio
- Assert at.radio[0].value == "Bar"
- Assert at.radio[0].index == 3
- at.radio[0].set_value("Foo").run()

### Selectbox
- Assert at.selectbox[0].value == "Bar"
- Assert at.selectbox[0].index == 3
- at.selectbox[0].set_value("Foo").run()

### Select_slider
- Assert at.select_slider[0].value == "Feb"
- at.select_slider[0].set_value("Mar").run()
- at.select_slider[0].set_range("Apr", "Jun").run()

### Slider
- Assert at.slider[0].value == 2
- at.slider[0].set_value(3).run()
- at.slider[0].set_range(4, 6).run()

### Text_area
- Assert at.text_area[0].value == "Hello, world!"
- at.text_area[0].set_value("Hello, yourself!").run()

### Text_input
- Assert at.text_input[0].value == "Hello, world!"
- at.text_input[0].set_value("Hello, yourself!").run()

### Time_input
- Assert at.time_input[0].value == datetime.time(8, 45)
- at.time_input[0].set_value(datetime.time(12, 30))

### Toggle
- Assert at.toggle[0].value == False
- Assert at.toggle[0].label == "Debug mode"
- at.toggle[0].set_value(True).run()
- Assert at.toggle[0].value == True

## Data elements

### DataFrame
- Assert at.dataframe[0].value.equals(expected_df)

### Metric
- Assert at.metric[0].value == "9500"
- Assert at.metric[0].delta == "1000"

### JSON
- Assert at.json[0].value == '[\"hi\", {\"foo\": \"bar\"}]'

### Table
- Assert at.table[0].value.equals(table_df)

## Layouts and containers

### Sidebar
- Assert at.sidebar.text_input[0].set_value("Jane Doe")

### Columns
- Assert at.columns[1].markdown[0].value == "Hello, world!"

### Tabs
- Assert at.tabs[2].markdown[0].value == "Hello, yourself!"

## Chat elements

### Chat_input
- Assert at.chat_input[0].set_value("Do you know any jokes?")
- Assert at.chat_message[0].markdown[0].value == "Do you know any jokes?"
- Assert at.chat_message[0].avatar == "user"

## Status elements

### Exception
- Assert len(at.exception) == 1
- Assert "TypeError" in at.exception[0].value

### Other in-line alerts
- Assert at.success[0].value == "Great job!"
- Assert at.info[0].value == "Please enter an API key to continue"
- Assert at.warning[0].value == "Sorry, the passwords didn't match"
- Assert at.error[0].value == "Something went wrong :("

### Toast
- Assert at.toast[0].value == "That was lit!"
- Assert at.toast[0].icon == "🔥"

## Limitations

As of Streamlit 1.28, the following Streamlit features are not natively supported by `AppTest`. However, workarounds are possible for many of them by inspecting the underlying proto directly using `AppTest.get()`. We plan to regularly add support for missing elements until all features are supported.

- Chart elements (st.bar_chart, st.line_chart, etc)
- Media elements (st.image, st.video, st.audio)
- st.file_uploader
- st.data_editor
- st.expander
- st.status
- st.camera_input
- st.download_button
- st.link_button