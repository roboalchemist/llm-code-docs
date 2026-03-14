# Source: https://docs.flux.ai/tutorials/publishing-a-part-to-the-library.md

# Publishing Components to the Flux Library

Learn how to get your components and changes to show up in the Flux library, making them accessible to your team or the broader community.

![](https://uploads.developerhub.io/prod/86Yw/adcf4hxh9hu1biagxyf1iyt5hq403ft7qw1599s8ol4tlcp2l0z1stmm6sdqrt3l.png)

## Overview

Publishing is the act of sharing your brand new component, or updates to your component, to the Flux library. This process makes your components discoverable and usable by others according to the permissions you set.

Publishing is important because new projects in Flux don't show up in the library by default. You have to intentionally choose to share them there. The same is true for making changes to published components. After you've made the changes you want, you must publish again to make those changes visible to others.

## Publishing a New Component

When you've created a new component and want to make it available in the library, follow these steps:

- Type `⌘P` on Mac or `Ctrl P` on Windows, or
- Click on the Flux Menu in the upper left corner of the screen
- Choose "Publish to Library..."
- Select "Publish"

![](https://uploads.developerhub.io/prod/86Yw/bvt8iarwexiwhasmstfseyx1juu4w10iwltb84po0ovim5xfrj5ij3otcafojsrx.png)

The publishing process involves these key steps:

1. Open the component project you want to publish
2. Click on the Flux Menu in the top-left corner of the screen
3. Choose "Publish to library..."
4. Review the component details
5. Click "Publish"

Once published, your component will appear in the library for users who have permission to access it, based on your project's permission settings.

## Publishing Component Updates

After publishing a component, any subsequent changes must also be published for others to see them. This versioning approach allows you to control when updates become available.

Think of it like software development: developers edit an app and only push an update when the next version is complete. Similarly, you can edit your component and publish the updated version only when you're ready.

To publish changes to an existing component:

1. Type `⌘P` on Mac or `Ctrl P` on Windows, or
2. Click on the Flux Menu on the top-left corner of the screen
3. Choose "Publish changes..."
4. Review the changes
5. Click "Publish"

![](https://uploads.developerhub.io/prod/86Yw/0z9cyjayzpjfql8mzt089s1je7c0bugueomz2rebmej4pcjp71b4ylomvsasy8de.png)

Once changes are published, users of your component will be notified and can choose to accept the updates or continue using the previous version.

![](https://uploads.developerhub.io/prod/86Yw/av5iclkd4goymmd9dncmxves166mrdt0cvd49ewa804eh4ftp1qgvn9pbtmq1utx.png)

## Managing Component Visibility

### Understanding Permissions

Publishing a component to the library **doesn't automatically make it publicly accessible to all users**. Only people specified in your project's [permissions](https://docs.flux.ai/flux/reference/reference-sharing-and-permissions) can find and use your component in the library.

This permission-based approach gives you control over who can access your components:

- **Private components**: Set permissions to limit access to just yourself or your team
- **Public components**: Set permissions to "Everyone" to make your component available to the entire Flux community

By default, a project's permissions are set to Private, meaning only you can access it.

To manage permissions:

1. Click on the ["Share" button](https://docs.flux.ai/flux/reference/reference-sharing-and-permissions) in the menu of your project
2. Adjust the permissions as needed
3. Publish the changes for the new permissions to take effect in the library

Remember that a change to your permissions is a change to your project, and must be published again to be reflected in the library.

### Component Persistence

Once a part is published, it cannot be un-published. This ensures that your component doesn't disappear from projects that utilize it.

However, you can:

1. **Change permissions**: Modify who can access your component in the library
2. **Archive the component**: When you [archive](https://docs.flux.ai/flux/reference/delete-archive-project#archive-a-project) a component, its permissions are changed to Private, hiding it from others in the library

Regardless of these changes, if anyone is already using your published component in a project, it will persist in that project, ensuring design continuity.

## Best Practices for Publishing Components

1. **Complete all elements**: Ensure your component has all necessary elements (terminals, symbol, footprint) before publishing
2. **Verify accuracy**: Double-check all dimensions, pin numbers, and properties against datasheets
3. **Add comprehensive metadata**: Include manufacturer part numbers, descriptions, and tags to make your component discoverable
4. **Test before publishing**: Create a test project to verify your component works as expected
5. **Document special features**: Add notes about any unique characteristics or usage requirements
6. **Set appropriate permissions**: Consider who needs access to your component