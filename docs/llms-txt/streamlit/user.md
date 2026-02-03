# Source: https://docs.streamlit.io/develop/api-reference/user

# Authentication and user info

Streamlit provides native support for user authentication so you can personalize your apps. You can also directly read headers and cookies.

## Log in a user

```python
st.login()
```

## Log out a user

```python
st.logout()
```

## User info

```python
if st.user.is_logged_in:
  st.write(f"Welcome back, {st.user.name}!")
```

[forum](https://docs.streamlit.io/develop/api-reference/user#authentication-and-user-info) Still have questions? Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

## Previous: Third-party components

[previous: Third-party components](/develop/api-reference/user/st.login)

## Next: st.login

[next: st.login](/develop/api-reference/user/st.login)