# Update it
flatpak -y --user update <your flatpak id>
```

## Adding additional libraries

If your final binary requires more libraries than the default tauri app, you need to add them in your flatpak manifest.
There are two ways to do this. For fast local development, it may work to simply include the already built library file (`.so`) from your local system.
However, this is not recommended for the final build of the flatpak, as your local library file is not built for the flatpak runtime environment.
This can introduce various bugs that can be very hard to find.
Therefore, it is recommended to build the library your program depends on from source inside the flatpak as a build step.

## Submitting to flathub

**_1. Fork The [Flathub Repository](https://github.com/flathub/flathub/fork)_**

**_2. Clone the Fork_**

```shell
git clone --branch=new-pr git@github.com:your_github_username/flathub.git
```

**_3. Enter the repository_**

```shell
cd flathub
```

**_4. Create a new branch_**

```shell
git checkout -b your_app_name
```

**_5. Add your apps manifest to the branch. Commit your changes, and then push them._**

**_6. Open a pull request against the `new-pr` branch on github_**

**_7. Your app will now enter the review process in which you may be asked to make changes to your project._**

When your pull request is approved then you will receive an invitation to edit your apps repository. From here on you can update your app continuously.

You can read more about this [in the flatpak documentation](https://docs.flatpak.org/en/latest/dependencies.html#bundling)