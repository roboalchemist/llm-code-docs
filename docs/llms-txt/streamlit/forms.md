# Source: https://docs.streamlit.io/develop/concepts/architecture/forms

# Using forms

When you don't want to rerun your script with each input made by a user, [st.form](https://docs.streamlit.io/develop/api-reference/execution-flow/st.form) is here to help! Forms make it easy to batch user input into a single rerun. This guide to using forms provides examples and explains how users interact with forms.

## Example

In the following example, a user can set multiple parameters to update the map. As the user changes the parameters, the script will not rerun and the map will not update. When the user submits the form with the button labeled "Update map", the script reruns and the map updates.

If at any time the user clicks "Generate new points" which is outside of the form, the script will rerun. If the user has any unsubmitted changes within the form, these will not be sent with the rerun. All changes made to a form will only be sent to the Python backend when the form itself is submitted.

### Execute the process after the form

If you need to execute a one-time process as a result of a form submission, you can condition that process on the `st.form_submit_button` and execute it after the form. If you need results from your process to display above the form, you can use containers to control where the form displays relative to your output.

### Use `st.rerun`

If your process affects content above your form, another alternative is using an extra rerun. This can be less resource-efficient though, and may be less desirable that the above options.

## Limitations

- Every form must contain a `st.form_submit_button`.
- `st.button` and `st.download_button` cannot be added to a form.
- `st.form` cannot be embedded inside another `st.form`.
- Callback functions can only be assigned to `st.form_submit_button` within a form; no other widgets in a form can have a callback.
- Interdependent widgets within a form are unlikely to be particularly useful. If you pass `widget1`'s value into `widget2` when they are both inside a form, then `widget2` will only update when the form is submitted.