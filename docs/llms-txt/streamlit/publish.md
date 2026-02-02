# Publish a Component

Publishing your Streamlit Component to [PyPI](https://pypi.org/) makes it easily accessible to Python users around the world. This step is completely optional, so if you won’t be releasing your component publicly, you can skip this section!

## Prepare your Component

A bi-directional Streamlit Component varies slightly from a pure Python library in that it must contain pre-compiled frontend code. This is how base Streamlit works as well; when you `pip install streamlit`, you are getting a Python library where the HTML and frontend code contained within it have been compiled into static assets.

The [component-template](https://github.com/streamlit/component-template) GitHub repo provides the folder structure necessary for PyPI publishing. But before you can publish, you'll need to do a bit of housekeeping:

1. Give your Component a name, if you haven't already
    - Rename the `template/my_component/` folder to `template/<component name>/`
    - Pass your component's name as the the first argument to `declare_component()`
2. Edit `MANIFEST.in`, change the path for recursive-include from `package/frontend/build *` to `<component name>/frontend/build *`
3. Edit `setup.py`, adding your component's name and other relevant info
4. Create a release build of your frontend code. `twine` will prompt you for a username and password. For the username, use `__token__`. For the password, use your token value from the previous step, including the `pypi-` prefix:
    ```bash
    python -m twine upload --repository testpypi dist/*
    ```
5. Install your newly-uploaded package in a new Python project to make sure it works:
    ```bash
    python -m pip install --index-url https://test.pypi.org/simple/ --no-deps example-pkg-YOUR-USERNAME-HERE
    ```

If all goes well, you're ready to upload your library to PyPI by following the instructions at [https://packaging.python.org/tutorials/packaging-projects/#next-steps](https://packaging.python.org/tutorials/packaging-projects/#next-steps).

## Promote your Component!

We'd love to help you share your Component with the Streamlit Community! To share it:

1. If you host your code on GitHub, add the tag `streamlit-component`, so that it's listed in the [GitHub `streamlit-component` topic](https://github.com/topics/streamlit-component):
    - ![Add the streamlit-component tag to your GitHub repo](https://docs.streamlit.io/images/component-tag.gif)
2. Post on the Streamlit Forum in [Show the Community!](https://discuss.streamlit.io/c/streamlit-examples/9). Use a post title similar to `New Component: <your component name>`, a new way to do X.
3. Add your component to the [Community Component Tracker](https://discuss.streamlit.io/t/streamlit-components-community-tracker/4634).
4. Tweet us at [@streamlit](https://twitter.com/streamlit) so that we can retweet your announcement for you.

Our [Components Gallery](https://streamlit.io/components) is updated approximately every month. Follow the above recommendations to maximize the likelihood of your component landing in our Components Gallery. Community Components featured in our docs are hand-curated on a less-regular basis. Popular components with many stars and good documentation are more likely to be selected.