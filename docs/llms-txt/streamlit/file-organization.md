# File organization for your Community Cloud app

Streamlit Community Cloud copies all the files in your repository and executes `streamlit run` from its root directory. Because Community Cloud is creating a new Python environment to run your app, you need to include a declaration of any [App dependencies](/deploy/streamlit-community-cloud/deploy-your-app/app-dependencies) in addition to any [Configuration](/develop/concepts/configuration) options.

You can have multiple apps in your repository, and their entrypoint files can be anywhere in your repository. However, you can only have one configuration file. This page explains how to correctly organize your app, configuration, and dependency files. The following examples assume you are using `requirements.txt` to declare your dependencies because it is the most common. As explained on the next page, Community Cloud supports other formats for configuring your Python environment.

## Basic example

In the following example, the entrypoint file (`your_app.py`) is in the root of the project directory alongside a `requirements.txt` file to declare the app's dependencies.

```
your_repository/
├── requirements.txt
└── your_app.py
```

If you are including custom configuration, your config file must be located at `.streamlit/config.toml` within your repository.

```
your_repository/
├── .streamlit/
│   └── config.toml
├── requirements.txt
└── your_app.py
```

Additionally, any files that need to be locally available to your app should be included in your repository.

### Tip

If you have really big or binary data that you change frequently, and git is running slowly, you might want to check out [Git Large File Store (LFS)](https://git-lfs.github.com/) as a better way to store large files in GitHub. You don't need to make any changes to your app to start using it. If your GitHub repository uses LFS, it will _just work_ with Streamlit Community Cloud.

### Next Steps

- [Previous: Deploy your app](/deploy/streamlit-community-cloud/deploy-your-app)
- [Next: App dependencies](/deploy/streamlit-community-cloud/deploy-your-app/app-dependencies)