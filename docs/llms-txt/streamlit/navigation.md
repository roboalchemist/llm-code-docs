# Navigation and pages

## Navigation

Configure the available pages in a multipage app.

```python
st.navigation({
    "Your account" : [log_out, settings],
    "Reports" : [overview, usage],
    "Tools" : [search]
})
```

## Page

Define a page in a multipage app.

```python
home = st.Page(
    "home.py",
    title="Home",
    icon=":material/home:"
)
```

## Page link

Display a link to another page in a multipage app.

```python
st.page_link("app.py", label="Home", icon="🏠")
st.page_link("pages/profile.py", label="Profile")
```

## Switch page

Programmatically navigates to a specified page.

```python
st.switch_page("pages/my_page.py")
```

## Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

## Previous: Authentication and user info

## Next: st.navigation

## Forum

### Ask AI

## Footer

### Social Links

- [GitHub](https://github.com/streamlit)
- [YouTube](https://www.youtube.com/channel/UC3LD42rjj-Owtxsa6PwGU5Q)
- [Twitter](https://twitter.com/streamlit)
- [LinkedIn](https://www.linkedin.com/company/streamlit)
- [Newsletter](https://info.snowflake.com/streamlit-newsletter-sign-up.html)

© 2025 Snowflake Inc.