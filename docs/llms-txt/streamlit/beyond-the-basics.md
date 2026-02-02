# Beyond the basics of app testing

Now that you're comfortable with executing a basic test for a Streamlit app let's cover the mutable attributes of [AppTest](/develop/api-reference/app-testing/st.testing.v1.apptest):

- `AppTest.secrets`
- `AppTest.session_state`
- `AppTest.query_params`

You can read and update values using dict-like syntax for all three attributes. For `.secrets` and `.query_params`, you can use key notation but not attribute notation. For example, the `.secrets` attribute for `AppTest` accepts `at.secrets["my_key"]` but **not** `at.secrets.my_key`. This differs from how you can use the associated command in the main library. On the other hand, `.session_state` allows both key notation and attribute notation.

## Using secrets with app testing

Be careful not to include secrets directly in your tests. Consider this simple project with `pytest` executed in the project's root directory:

```none
myproject/
├── .streamlit/
│   ├── config.toml
│   └── secrets.toml
├── app.py
└── tests/
    └── test_app.py
```

In the above scenario, your simulated app will have access to your `secrets.toml` file. However, since you don't want to commit your secrets to your repository, you may need to write tests where you securely pull your secrets into memory or use dummy secrets.

### Example: declaring secrets in a test

Within a test, declare each secret after initializing your `AppTest` instance but before the first run. (A missing secret may result in an app that doesn't run!) For example, consider the following secrets file and corresponding test initialization to assign the same secrets manually:

**Secrets file:**

```toml
db_username = "Jane"
db_password = "mypassword"

[my_other_secrets]
things_i_like = ["Streamlit", "Python"]
```

**Testing file with equivalent secrets:**

```python
# Initialize an AppTest instance.
at = AppTest.from_file("app.py")
# Declare the secrets.
at.secrets["db_username"] = "Jane"
at.secrets["db_password"] = "mypassword"
at.secrets["my_other_secrets.things_i_like"] = ["Streamlit", "Python"]
# Run the app.
at.run()
assert at.markdown[0].value == ":balloon:"
```

By setting the value `at.session_state["magic_word"] = "Balloons"` within the test, you can simulate a user navigating to `second.py` after entering and saving "Balloons" on `first.py".