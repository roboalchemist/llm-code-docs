# st.column_config.SelectboxColumn

Configure a selectbox column in `st.dataframe` or `st.data_editor`.

This is the default column type for Pandas categorical values. This command needs to be used in the `column_config` parameter of `st.dataframe` or `st.data_editor`. When used with `st.data_editor`, editing will be enabled with a selectbox widget.

## Examples

```python
import pandas as pd
import streamlit as st

data_df = pd.DataFrame(
    {
        "category": [
            "📊 Data Exploration",
            "📈 Data Visualization",
            "🤖 LLM",
            "📊 Data Exploration",
        ],
    }
)

st.data_editor(
    data_df,
    column_config={
        "category": st.column_config.SelectboxColumn(
            "App Category",
            help="The category of the app",
            width="medium",
            options=[
                "📊 Data Exploration",
                "📈 Data Visualization",
                "🤖 LLM",
            ],
            required=True,
        )
    },
    hide_index=True,
)
```

## Notes

Streamlit Version: Version 1.52.0

## Caching and state

### Application Logic

- **Authentication and user info**
  - `st.login`
  - `st.logout`
- **Navigation and pages**
  - `st.navigation`
  - `st.Page`
  - `st.page_link`
- **Execution flow**
  - `st.dialog`
  - `st.form`
  - `st.form_submit_button`
  - `st.fragment`
  - `st.rerun`
  - `st.stop`
- **Caching and state**
  - `st.cache_data`
  - `st.cache_resource`
  - `st.experimental_memo`
  - `st.experimental_singleton`
  - `st.session_state`
  - `st.context`
  - `st.query_params`
  - `st.experimental_get_query_params`
  - `st.experimental_set_query_params`
- **Status elements**
  - `st.success`
  - `st.info`
  - `st.warning`
  - `st.error`
  - `st.exception`
  - `st.progress`
  - `st.spinner`
  - `st.status`
  - `st.toast`
  - `st.balloons`
  - `st.snow`

## Tools

- **App testing**
  - `st.testing.v1.apptest`
  - `element_tree`

## Quick reference

- **Cheat sheet**
- **Release notes**
  - 2025
  - 2024
  - 2023
  - 2022
  - 2021
  - 2020
  - 2019
- **Pre-release features**
- **Roadmap**

## Get started

- **Installation**
  - [Install and update Streamlit](/get-started/installation)
  - [Streamlit Playground](/get-started/installation/streamlit-playground)
  - [Install via command line](/get-started/installation/command-line)
  - [Install via Anaconda Distribution](/get-started/installation/anaconda-distribution)
  - [Streamlit in Snowflake](/get-started/installation/streamlit-in-snowflake)
- **Fundamentals**
  - [Basic concepts](/get-started/fundamentals/main-concepts)
  - [Advanced concepts](/get-started/fundamentals/advanced-concepts)
  - [Additional features](/get-started/fundamentals/additional-features)
  - [Summary](/get-started/fundamentals/summary)
- **First steps**
  - [Create an app](/get-started/tutorials/create-an-app)
  - [Create a multipage app](/get-started/tutorials/create-a-multipage-app)

## Develop

- **Concepts**
  - [CORE](/develop/concepts/core)
  - [Architecture and execution](/develop/concepts/architecture)
    - [Running your app](/develop/concepts/architecture/run-your-app)
    - [Streamlit's architecture](/develop/concepts/architecture/architecture)
    - [The app chrome](/develop/concepts/architecture/app-chrome)
    - [Caching](/develop/concepts/architecture/caching)
    - [Session State](/develop/concepts/architecture/session-state)
    - [Forms](/develop/concepts/architecture/forms)
    - [Fragments](/develop/concepts/architecture/fragments)
    - [Widget behavior](/develop/concepts/architecture/widget-behavior)
  - [Multipage apps](/develop/concepts/multipage-apps)
    - [Overview](/develop/concepts/multipage-apps/overview)
    - [Page and navigation](/develop/concepts/multipage-apps/page-and-navigation)
    - [Pages directory](/develop/concepts/multipage-apps/pages-directory)
    - [Working with widgets](/develop/concepts/multipage-apps/widgets)
  - [App design](/develop/concepts/design)
    - [Animate and update elements](/develop/concepts/design/animate)
    - [Button behavior and examples](/develop/concepts/design/buttons)
    - [Dataframes](/develop/concepts/design/dataframes)
    - [Multithreading](/develop/concepts/design/multithreading)
    - [Using custom classes](/develop/concepts/design/custom-classes)
    - [Working with timezones](/develop/concepts/design/timezone-handling)
  - [ADDITIONAL](/develop/concepts/additional-features)
  - [Connections, secrets, and authentication](/develop/concepts/connections)
    - [Connecting to data](/develop/concepts/connections/connecting-to-data)
    - [Secrets management](/develop/concepts/connections/secrets-management)
    - [User authentication](/develop/concepts/connections/authentication)
    - [Security reminders](/develop/concepts/connections/security-reminders)
  - [Custom components](/develop/concepts/custom-components)
    - [Intro to custom components](/develop/concepts/custom-components/intro)
    - [Create a Component](/develop/concepts/custom-components/create)
    - [Publish a Component](/develop/concepts/custom-components/publish)
    - [Limitations](/develop/concepts/custom-components/limitations)
    - [Component gallery](https://streamlit.io/components)
  - [Configuration and theming](/develop/concepts/configuration)
    - [Configuration options](/develop/concepts/configuration/options)
    - [HTTPS support](/develop/concepts/configuration/https-support)
    - [Serving static files](/develop/concepts/configuration/serving-static-files)
    - [THEMING](/develop/concepts/configuration/theming)
    - [Customize your theme](/develop/concepts/configuration/theming-customize-colors-and-borders)
    - [Customize fonts](/develop/concepts/configuration/theming-customize-fonts)
  - [App testing](/develop/concepts/app-testing)
    - [Get started](/develop/concepts/app-testing/get-started)
    - [Beyond the basics](/develop/concepts/app-testing/beyond-the-basics)
    - [Automate your tests](/develop/concepts/app-testing/automate-tests)
    - [Example](/develop/concepts/app-testing/examples)
    - [Cheat sheet](/develop/concepts/app-testing/cheat-sheet)

## Deploy

- **Concepts**
  - [CORE](/deploy/concepts/core)
  - [Architecture and execution](/deploy/concepts/architecture)
    - [Running your app](/deploy/concepts/architecture/run-your-app)
    - [Streamlit's architecture](/deploy/concepts/architecture/architecture)
    - [The app chrome](/deploy/concepts/architecture/app-chrome)
    - [Caching](/deploy/concepts/architecture/caching)
    - [Session State](/deploy/concepts/architecture/session-state)
    - [Forms](/deploy/concepts/architecture/forms)
    - [Fragments](/deploy/concepts/architecture/fragments)
    - [Widget behavior](/deploy/concepts/architecture/widget-behavior)
  - [Multipage apps](/deploy/concepts/multipage-apps)
    - [Overview](/deploy/concepts/multipage-apps/overview)
    - [Page and navigation](/deploy/concepts/multipage-apps/page-and-navigation)
    - [Pages directory](/deploy/concepts/multipage-apps/pages-directory)
    - [Working with widgets](/deploy/concepts/multipage-apps/widgets)
  - [App design](/deploy/concepts/design)
    - [Animate and update elements](/deploy/concepts/design/animate)
    - [Button behavior and examples](/deploy/concepts/design/buttons)
    - [Dataframes](/deploy/concepts/design/dataframes)
    - [Multithreading](/deploy/concepts/design/multithreading)
    - [Using custom classes](/deploy/concepts/design/custom-classes)
    - [Working with timezones](/deploy/concepts/design/timezone-handling)
  - [ADDITIONAL](/deploy/concepts/additional-features)
  - [Connections, secrets, and authentication](/deploy/concepts/connections)
    - [Connecting to data](/deploy/concepts/connections/connecting-to-data)
    - [Secrets management](/deploy/concepts/connections/secrets-management)
    - [User authentication](/deploy/concepts/connections/authentication)
    - [Security reminders](/deploy/concepts/connections/security-reminders)
  - [Custom components](/deploy/concepts/custom-components)
    - [Intro to custom components](/deploy/concepts/custom-components/intro)
    - [Create a Component](/deploy/concepts/custom-components/create)
    - [Publish a Component](/deploy/concepts/custom-components/publish)
    - [Limitations](/deploy/concepts/custom-components/limitations)
    - [Component gallery](https://streamlit.io/components)
  - [Configuration and theming](/deploy/concepts/configuration)
    - [Configuration options](/deploy/concepts/configuration/options)
    - [HTTPS support](/deploy/concepts/configuration/https-support)
    - [Serving static files](/deploy/concepts/configuration/serving-static-files)
    - [THEMING](/deploy/concepts/configuration/theming)
    - [Customize your theme](/deploy/concepts/configuration/theming-customize-colors-and-borders)
    - [Customize fonts](/deploy/concepts/configuration/theming-customize-fonts)
  - [App testing](/deploy/concepts/app-testing)
    - [Get started](/deploy/concepts/app-testing/get-started)
    - [Beyond the basics](/deploy/concepts/app-testing/beyond-the-basics)
    - [Automate your tests](/deploy/concepts/app-testing/automate-tests)
    - [Example](/deploy/concepts/app-testing/examples)
    - [Cheat sheet](/deploy/concepts/app-testing/cheat-sheet)

## Knowledge base

- **FAQ**
  - [How do I create an anchor link?](/knowledge-base/using-streamlit/create-anchor-link)
  - [Enabling camera access in your browser](/knowledge-base/using-streamlit/enable-camera)
  - [How to download a file in Streamlit?](/knowledge-base/using-streamlit/how-download-file-streamlit)
  - [How to download a Pandas DataFrame as a CSV?](/knowledge-base/using-streamlit/how-download-pandas-dataframe-csv)
  - [How do I upgrade to the latest version of Streamlit?](/knowledge-base/using-streamlit/how-upgrade-latest-version-streamlit)
  - [How to insert elements out of order?](/knowledge-base/using-streamlit/insert-elements-out-of-order)
  - [How can I make st.pydeck_chart use custom Mapbox styles?](/knowledge-base/using-streamlit/pydeck-chart-custom-mapbox-styles)
  - [How to remove "· Streamlit" from the app title?](/knowledge-base/using-streamlit/remove-streamlit-app-title)
  - [How do you retrieve the filename of a file uploaded with st.file_uploader?](/knowledge-base/using-streamlit/retrieve-filename-uploaded)
  - [Sanity checks](/knowledge-base/using-streamlit/sanity-checks)
  - [How can I make Streamlit watch for changes in other modules I'm importing in my app?](/knowledge-base/using-streamlit/streamlit-watch-changes-other-modules-importing-app)
  - [What browsers does Streamlit support?](/knowledge-base/using-streamlit/supported-browsers)
  - [Where does st.file_uploader store uploaded files and when do they get deleted?](/knowledge-base/using-streamlit/where-file-uploader-store-when-deleted)
  - [Widget updating for every second input when using session state](/knowledge-base/using-streamlit/widget-updating-session-state)
  - [Why does Streamlit restrict nested st.columns?](/knowledge-base/using-streamlit/why-streamlit-restrict-nested-columns)
  - [What is serializable session state?](/knowledge-base/using-streamlit/serializable-session-state)

- **Installing dependencies**
  - [How to install a package not on PyPI or Conda but available on GitHub](/knowledge-base/dependencies/install-package-not-pypi-conda-available-github)
  - [ImportError libGL.so.1 cannot open shared object file No such file or directory](/knowledge-base/dependencies/libgl)
  - [ModuleNotFoundError No module named](/knowledge-base/dependencies/module-not-found-error)
  - [ERROR No matching distribution found for](/knowledge-base/dependencies/no-matching-distribution)

- **Deployment issues**
  - [How can I deploy multiple Streamlit apps on different subdomains?](/knowledge-base/deploy/deploy-multiple-streamlit-apps-different-subdomains)
  - [How do I deploy Streamlit on a domain so it appears to run on a regular port (i.e. port 80)?](/knowledge-base/deploy/deploy-streamlit-domain-port-80)
  - [Does Streamlit support the WSGI Protocol? (aka Can I deploy Streamlit with gunicorn)?](/knowledge-base/deploy/does-streamlit-support-wsgi-protocol)
  - [How do I increase the upload limit of st.file_uploader on Streamlit Community Cloud?](/knowledge-base/deploy/increase-file-uploader-limit-streamlit-cloud)
  - [Invoking a Python subprocess in a deployed Streamlit app](/knowledge-base/deploy/invoking-python-subprocess-deployed-streamlit-app)
  - [App is not loading when running remotely](/knowledge-base/deploy/remote-start)
  - [Argh. This app has gone over its resource limits](/knowledge-base/deploy/resource-limits)
  - [How do I share apps with viewers outside my organization?](/knowledge-base/deploy/share-apps-with-viewers-outside-organization)
  - [Upgrade the Streamlit version of your app on Streamlit Community Cloud](/knowledge-base/deploy/upgrade-streamlit-version-on-streamlit-cloud)
  - [Huh. This is isn't supposed to happen message after trying to log in](/knowledge-base/deploy/huh-this-isnt-supposed-to-happen-message-after-trying-to-log-in)
  - [Login attempt to Streamlit Community Cloud fails with error 403](/knowledge-base/deploy/login-attempt-to-streamlit-community-cloud-fails-with-error-403)
  - [How to submit a support case for Streamlit Community Cloud](/knowledge-base/deploy/how-to-submit-a-support-case-for-streamlit-community-cloud)

## Get started

- **Installation**
  - [Install and update Streamlit](/get-started/installation)
  - [Streamlit Playground](/get-started/installation/streamlit-playground)
  - [Install via command line](/get-started/installation/command-line)
  - [Install via Anaconda Distribution](/get-started/installation/anaconda-distribution)
  - [Streamlit in Snowflake](/get-started/installation/streamlit-in-snowflake)
- **Fundamentals**
  - [Basic concepts](/get-started/fundamentals/main-concepts)
  - [Advanced concepts](/get-started/fundamentals/advanced-concepts)
  - [Additional features](/get-started/fundamentals/additional-features)
  - [Summary](/get-started/fundamentals/summary)
- **First steps**
  - [Create an app](/get-started/tutorials/create-an-app)
  - [Create a multipage app](/get-started/tutorials/create-a-multipage-app)

## Develop

- **Concepts**
  - [CORE](/develop/concepts/core)
  - [Architecture and execution](/develop/concepts/architecture)
    - [Running your app](/develop/concepts/architecture/run-your-app)
    - [Streamlit's architecture](/develop/concepts/architecture/architecture)
    - [The app chrome](/develop/concepts/architecture/app-chrome)
    - [Caching](/develop/concepts/architecture/caching)
    - [Session State](/develop/concepts/architecture/session-state)
    - [Forms](/develop/concepts/architecture/forms)
    - [Fragments](/develop/concepts/architecture/fragments)
    - [Widget behavior](/develop/concepts/architecture/widget-behavior)
  - [Multipage apps](/develop/concepts/multipage-apps)
    - [Overview](/develop/concepts/multipage-apps/overview)
    - [Page and navigation](/develop/concepts/multipage-apps/page-and-navigation)
    - [Pages directory](/develop/concepts/multipage-apps/pages-directory)
    - [Working with widgets](/develop/concepts/multipage-apps/widgets)
  - [App design](/develop/concepts/design)
    - [Animate and update elements](/develop/concepts/design/animate)
    - [Button behavior and examples](/develop/concepts/design/buttons)
    - [Dataframes](/develop/concepts/design/dataframes)
    - [Multithreading](/develop/concepts/design/multithreading)
    - [Using custom classes](/develop/concepts/design/custom-classes)
    - [Working with timezones](/develop/concepts/design/timezone-handling)
  - [ADDITIONAL](/develop/concepts/additional-features)
  - [Connections, secrets, and authentication](/develop/concepts/connections)
    - [Connecting to data](/develop/concepts/connections/connecting-to-data)
    - [Secrets management](/develop/concepts/connections/secrets-management)
    - [User authentication](/develop/concepts/connections/authentication)
    - [Security reminders](/develop/concepts/connections/security-reminders)
  - [Custom components](/develop/concepts/custom-components)
    - [Intro to custom components](/develop/concepts/custom-components/intro)
    - [Create a Component](/develop/concepts/custom-components/create)
    - [Publish a Component](/develop/concepts/custom-components/publish)
    - [Limitations](/develop/concepts/custom-components/limitations)
    - [Component gallery](https://streamlit.io/components)
  - [Configuration and theming](/develop/concepts/configuration)
    - [Configuration options](/develop/concepts/configuration/options)
    - [HTTPS support](/develop/concepts/configuration/https-support)
    - [Serving static files](/develop/concepts/configuration/serving-static-files)
    - [THEMING](/develop/concepts/configuration/theming)
    - [Customize your theme](/develop/concepts/configuration/theming-customize-colors-and-borders)
    - [Customize fonts](/develop/concepts/configuration/theming-customize-fonts)
  - [App testing](/develop/concepts/app-testing)
    - [Get started](/develop/concepts/app-testing/get-started)
    - [Beyond the basics](/develop/concepts/app-testing/beyond-the-basics)
    - [Automate your tests](/develop/concepts/app-testing/automate-tests)
    - [Example](/develop/concepts/app-testing/examples)
    - [Cheat sheet](/develop/concepts/app-testing/cheat-sheet)

## Deploy

- **Concepts**
  - [CORE](/deploy/concepts/core)
  - [Architecture and execution](/deploy/concepts/architecture)
    - [Running your app](/deploy/concepts/architecture/run-your-app)
    - [Streamlit's architecture](/deploy/concepts/architecture/architecture)
    - [The app chrome](/deploy/concepts/architecture/app-chrome)
    - [Caching](/deploy/concepts/architecture/caching)
    - [Session State](/deploy/concepts/architecture/session-state)
    - [Forms](/deploy/concepts/architecture/forms)
    - [Fragments](/deploy/concepts/architecture/fragments)
    - [Widget behavior](/deploy/concepts/architecture/widget-behavior)
  - [Multipage apps](/deploy/concepts/multipage-apps)
    - [Overview](/deploy/concepts/multipage-apps/overview)
    - [Page and navigation](/deploy/concepts/multipage-apps/page-and-navigation)
    - [Pages directory](/deploy/concepts/multipage-apps/pages-directory)
    - [Working with widgets](/deploy/concepts/multipage-apps/widgets)
  - [App design](/deploy/concepts/design)
    - [Animate and update elements](/deploy/concepts/design/animate)
    - [Button behavior and examples](/deploy/concepts/design/buttons)
    - [Dataframes](/deploy/concepts/design/dataframes)
    - [Multithreading](/deploy/concepts/design/multithreading)
    - [Using custom classes](/deploy/concepts/design/custom-classes)
    - [Working with timezones](/deploy/concepts/design/timezone-handling)
  - [ADDITIONAL](/deploy/concepts/additional-features)
  - [Connections, secrets, and authentication](/deploy/concepts/connections)
    - [Connecting to data](/deploy/concepts/connections/connecting-to-data)
    - [Secrets management](/deploy/concepts/connections/secrets-management)
    - [User authentication](/deploy/concepts/connections/authentication)
    - [Security reminders](/deploy/concepts/connections/security-reminders)
  - [Custom components](/deploy/concepts/custom-components)
    - [Intro to custom components](/deploy/concepts/custom-components/intro)
    - [Create a Component](/deploy/concepts/custom-components/create)
    - [Publish a Component](/deploy/concepts/custom-components/publish)
    - [Limitations](/deploy/concepts/custom-components/limitations)
    - [Component gallery](https://streamlit.io/components)
  - [Configuration and theming](/deploy/concepts/configuration)
    - [Configuration options](/deploy/concepts/configuration/options)
    - [HTTPS support](/deploy/concepts/configuration/https-support)
    - [Serving static files](/deploy/concepts/configuration/serving-static-files)
    - [THEMING](/deploy/concepts/configuration/theming)
    - [Customize your theme](/deploy/concepts/configuration/theming-customize-colors-and-borders)
    - [Customize fonts](/deploy/concepts/configuration/theming-customize-fonts)
  - [App testing](/deploy/concepts/app-testing)
    - [Get started](/deploy/concepts/app-testing/get-started)
    - [Beyond the basics](/deploy/concepts/app-testing/beyond-the-basics)
    - [Automate your tests](/deploy/concepts/app-testing/automate-tests)
    - [Example](/deploy/concepts/app-testing/examples)
    - [Cheat sheet](/deploy/concepts/app-testing/cheat-sheet)

## Knowledge base

- **FAQ**
  - [How do I create an anchor link?](/knowledge-base/using-streamlit/create-anchor-link)
  - [Enabling camera access in your browser](/knowledge-base/using-streamlit/enable-camera)
  - [How to download a file in Streamlit?](/knowledge-base/using-streamlit/how-download-file-streamlit)
  - [How to download a Pandas DataFrame as a CSV?](/knowledge-base/using-streamlit/how-download-pandas-dataframe-csv)
  - [How do I upgrade to the latest version of Streamlit?](/knowledge-base/using-streamlit/how-upgrade-latest-version-streamlit)
  - [How to insert elements out of order?](/knowledge-base/using-streamlit/insert-elements-out-of-order)
  - [How can I make st.pydeck_chart use custom Mapbox styles?](/knowledge-base/using-streamlit/pydeck-chart-custom-mapbox-styles)
  - [How to remove "· Streamlit" from the app title?](/knowledge-base/using-streamlit/remove-streamlit-app-title)
  - [How do you retrieve the filename of a file uploaded with st.file_uploader?](/knowledge-base/using-streamlit/retrieve-filename-uploaded)
  - [Sanity checks](/knowledge-base/using-streamlit/sanity-checks)
  - [How can I make Streamlit watch for changes in other modules I'm importing in my app?](/knowledge-base/using-streamlit/streamlit-watch-changes-other-modules-importing-app)
  - [What browsers does Streamlit support?](/knowledge-base/using-streamlit/supported-browsers)
  - [Where does st.file_uploader store uploaded files and when do they get deleted?](/knowledge-base/using-streamlit/where-file-uploader-store-when-deleted)
  - [Widget updating for every second input when using session state](/knowledge-base/using-streamlit/widget-updating-session-state)
  - [Why does Streamlit restrict nested st.columns?](/knowledge-base/using-streamlit/why-streamlit-restrict-nested-columns)
  - [What is serializable session state?](/knowledge-base/using-streamlit/serializable-session-state)

- **Installing dependencies**
  - [How to install a package not on PyPI or Conda but available on GitHub](/knowledge-base/dependencies/install-package-not-pypi-conda-available-github)
  - [ImportError libGL.so.1 cannot open shared object file No such file or directory](/knowledge-base/dependencies/libgl)
  - [ModuleNotFoundError No module named](/knowledge-base/dependencies/module-not-found-error)
  - [ERROR No matching distribution found for](/knowledge-base/dependencies/no-matching-distribution)

- **Deployment issues**
  - [How can I deploy multiple Streamlit apps on different subdomains?](/knowledge-base/deploy/deploy-multiple-streamlit-apps-different-subdomains)
  - [How do I deploy Streamlit on a domain so it appears to run on a regular port (i.e. port 80)?](/knowledge-base/deploy/deploy-streamlit-domain-port-80)
  - [Does Streamlit support the WSGI Protocol? (aka Can I deploy Streamlit with gunicorn)?](/knowledge-base/deploy/does-streamlit-support-wsgi-protocol)
  - [How do I increase the upload limit of st.file_uploader on Streamlit Community Cloud?](/knowledge-base/deploy/increase-file-uploader-limit-streamlit-cloud)
  - [Invoking a Python subprocess in a deployed Streamlit app](/knowledge-base/deploy/invoking-python-subprocess-deployed-streamlit-app)
  - [App is not loading when running remotely](/knowledge-base/deploy/remote-start)
  - [Argh. This app has gone over its resource limits](/knowledge-base/deploy/resource-limits)
  - [How do I share apps with viewers outside my organization?](/knowledge-base/deploy/share-apps-with-viewers-outside-organization)
  - [Upgrade the Streamlit version of your app on Streamlit Community Cloud](/knowledge-base/deploy/upgrade-streamlit-version-on-streamlit-cloud)
  - [Huh. This is isn't supposed to happen message after trying to log in](/knowledge-base/deploy/huh-this-isnt-supposed-to-happen-message-after-trying-to-log-in)
  - [Login attempt to Streamlit Community Cloud fails with error 403](/knowledge-base/deploy/login-attempt-to-streamlit-community-cloud-fails-with-error-403)
  - [How to submit a support case for Streamlit Community Cloud](/knowledge-base/deploy/how-to-submit-a-support-case-for-streamlit-community-cloud)

## Get started

- **Installation**
  - [Install and update Streamlit](/get-started/installation)
  - [Streamlit Playground](/get-started/installation/streamlit-playground)
  - [Install via command line](/get-started/installation/command-line)
  - [Install via Anaconda Distribution](/get-started/installation/anaconda-distribution)
  - [Streamlit in Snowflake](/get-started/installation/streamlit-in-snowflake)
- **Fundamentals**
  - [Basic concepts](/get-started/fundamentals/main-concepts)
  - [Advanced concepts](/get-started/fundamentals/advanced-concepts)
  - [Additional features](/get-started/fundamentals/additional-features)
  - [Summary](/get-started/fundamentals/summary)
- **First steps**
  - [Create an app](/get-started/tutorials/create-an-app)
  - [Create a multipage app](/get-started/tutorials/create-a-multipage-app)

## Develop

- **Concepts**
  - [CORE](/develop/concepts/core)
  - [Architecture and execution](/develop/concepts/architecture)
    - [Running your app](/develop/concepts/architecture/run-your-app)
    - [Streamlit's architecture](/develop/concepts/architecture/architecture)
    - [The app chrome](/develop/concepts/architecture/app-chrome)
    - [Caching](/develop/concepts/architecture/caching)
    - [Session State](/develop/concepts/architecture/session-state)
    - [Forms](/develop/concepts/architecture/forms)
    - [Fragments](/develop/concepts/architecture/fragments)
    - [Widget behavior](/develop/concepts/architecture/widget-behavior)
  - [Multipage apps](/develop/concepts/multipage-apps)
    - [Overview](/develop/concepts/multipage-apps/overview)
    - [Page and navigation](/develop/concepts/multipage-apps/page-and-navigation)
    - [Pages directory](/develop/concepts/multipage-apps/pages-directory)
    - [Working with widgets](/develop/concepts/multipage-apps/widgets)
  - [App design](/develop/concepts/design)
    - [Animate and update elements](/develop/concepts/design/animate)
    - [Button behavior and examples](/develop/concepts/design/buttons)
    - [Dataframes](/develop/concepts/design/dataframes)
    - [Multithreading](/develop/concepts/design/multithreading)
    - [Using custom classes](/develop/concepts/design/custom-classes)
    - [Working with timezones](/develop/concepts/design/timezone-handling)
  - [ADDITIONAL](/develop/concepts/additional-features)
  - [Connections, secrets, and authentication](/develop/concepts/connections)
    - [Connecting to data](/develop/concepts/connections/connecting-to-data)
    - [Secrets management](/develop/concepts/connections/secrets-management)
    - [User authentication](/develop/concepts/connections/authentication)
    - [Security reminders](/develop/concepts/connections/security-reminders)
  - [Custom components](/develop/concepts/custom-components)
    - [Intro to custom components](/develop/concepts/custom-components/intro)
    - [Create a Component](/develop/concepts/custom-components/create)
    - [Publish a Component](/develop/concepts/custom-components/publish)
    - [Limitations](/develop/concepts/custom-components/limitations)
    - [Component gallery](https://streamlit.io/components)
  - [Configuration and theming](/develop/concepts/configuration)
    - [Configuration options](/develop/concepts/configuration/options)
    - [HTTPS support](/develop/concepts/configuration/https-support)
    - [Serving static files](/develop/concepts/configuration/serving-static-files)
    - [THEMING](/develop/concepts/configuration/theming)
    - [Customize your theme](/develop/concepts/configuration/theming-customize-colors-and-borders)
    - [Customize fonts](/develop/concepts/configuration/theming-customize-fonts)
  - [App testing](/develop/concepts/app-testing)
    - [Get started](/develop/concepts/app-testing/get-started)
    - [Beyond the basics](/develop/concepts/app-testing/beyond-the-basics)
    - [Automate your tests](/develop/concepts/app-testing/automate-tests)
    - [Example](/develop/concepts/app-testing/examples)
    - [Cheat sheet](/develop/concepts/app-testing/cheat-sheet)

## Deploy

- **Concepts**
  - [CORE](/deploy/concepts/core)
  - [Architecture and execution](/deploy/concepts/architecture)
    - [Running your app](/deploy/concepts/architecture/run-your-app)
    - [Streamlit's architecture](/deploy/concepts/architecture/architecture)
    - [The app chrome](/deploy/concepts/architecture/app-chrome)
    - [Caching](/deploy/concepts/architecture/caching)
    - [Session State](/deploy/concepts/architecture/session-state)
    - [Forms](/deploy/concepts/architecture/forms)
    - [Fragments](/deploy/concepts/architecture/fragments)
    - [Widget behavior](/deploy/concepts/architecture/widget-behavior)
  - [Multipage apps](/deploy/concepts/multipage-apps)
    - [Overview](/deploy/concepts/multipage-apps/overview)
    - [Page and navigation](/deploy/concepts/multipage-apps/page-and-navigation)
    - [Pages directory](/deploy/concepts/multipage-apps/pages-directory)
    - [Working with widgets](/deploy/concepts/multipage-apps/widgets)
  - [App design](/deploy/concepts/design)
    - [Animate and update elements](/deploy/concepts/design/animate)
    - [Button behavior and examples](/deploy/concepts/design/buttons)
    - [Dataframes](/deploy/concepts/design/dataframes)
    - [Multithreading](/deploy/concepts/design/multithreading)
    - [Using custom classes](/deploy/concepts/design/custom-classes)
    - [Working with timezones](/deploy/concepts/design/timezone-handling)
  - [ADDITIONAL](/deploy/concepts/additional-features)
  - [Connections, secrets, and authentication](/deploy/concepts/connections)
    - [Connecting to data](/deploy/concepts/connections/connecting-to-data)
    - [Secrets management](/deploy/concepts/connections/secrets-management)
    - [User authentication](/deploy/concepts/connections/authentication)
    - [Security reminders](/deploy/concepts/connections/security-reminders)
  - [Custom components](/deploy/concepts/custom-components)
    - [Intro to custom components](/deploy/concepts/custom-components/intro)
    - [Create a Component](/deploy/concepts/custom-components/create)
    - [Publish a Component](/deploy/concepts/custom-components/publish)
    - [Limitations](/deploy/concepts/custom-components/limitations)
    - [Component gallery](https://streamlit.io/components)
  - [Configuration and theming](/deploy/concepts/configuration)
    - [Configuration options](/deploy/concepts/configuration/options)
    - [HTTPS support](/deploy/concepts/configuration/https-support)
    - [Serving static files](/deploy/concepts/configuration/serving-static-files)
    - [THEMING](/deploy/concepts/configuration/theming)
    - [Customize your theme](/deploy/concepts/configuration/theming-customize-colors-and-borders)
    - [Customize fonts](/deploy/concepts/configuration/theming-customize-fonts)
  - [App testing](/deploy/concepts/app-testing)
    - [Get started](/deploy/concepts/app-testing/get-started)
    - [Beyond the basics](/deploy/concepts/app-testing/beyond-the-basics)
    - [Automate your tests](/deploy/concepts/app-testing/automate-tests)
    - [Example](/deploy/concepts/app-testing/examples)
    - [Cheat sheet](/deploy/concepts/app-testing/cheat-sheet)

## Knowledge base

- **FAQ**
  - [How do I create an anchor link?](/knowledge-base/using-streamlit/create-anchor-link)
  - [Enabling camera access in your browser](/knowledge-base/using-streamlit/enable-camera)
  - [How to download a file in Streamlit?](/knowledge-base/using-streamlit/how-download-file-streamlit)
  - [How to download a Pandas DataFrame as a CSV?](/knowledge-base/using-streamlit/how-download-pandas-dataframe-csv)
  - [How do I upgrade to the latest version of Streamlit?](/knowledge-base/using-streamlit/how-upgrade-latest-version-streamlit)
  - [How to insert elements out of order?](/knowledge-base/using-streamlit/insert-elements-out-of-order)
  - [How can I make st.pydeck_chart use custom Mapbox styles?](/knowledge-base/using-streamlit/pydeck-chart-custom-mapbox-styles)
  - [How to remove "· Streamlit" from the app title?](/knowledge-base/using-streamlit/remove-streamlit-app-title)
  - [How do you retrieve the filename of a file uploaded with st.file_uploader?](/knowledge-base/using-streamlit/retrieve-filename-uploaded)
  - [Sanity checks](/knowledge-base/using-streamlit/sanity-checks)
  - [How can I make Streamlit watch for changes in other modules I'm importing in my app?](/knowledge-base/using-streamlit/streamlit-watch-changes-other-modules-importing-app)
  - [What browsers does Streamlit support?](/knowledge-base/using-streamlit/supported-browsers)
  - [Where does st.file_uploader store uploaded files and when do they get deleted?](/knowledge-base/using-streamlit/where-file-uploader-store-when-deleted)
  - [Widget updating for every second input when