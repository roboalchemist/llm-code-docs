# How to create admin permissions from plugins

When [developing a Strapi plugin](/cms/plugins-development/developing-plugins), you might want to create admin permissions for your plugin. By doing that you can hook in to the [RBAC system](/cms/features/rbac) of Strapi to selectively grant permissions to certain pieces of your plugin.

To create admin permissions for your Strapi plugin, you'll need to register them on the server side before implementing them on the admin side.

## Register the permissions server side

Each individual permission has to registered in the bootstrap function of your plugin, as follows:

</Tabs>

## Implement permissions on the admin panel side

Before we can implement our permissions on the admin panel side we have to define them in a reusable configuration file. This file can be stored anywhere in your plugin admin code. You can do that as follows:

```js title="/src/plugins/my-plugin/admin/src/permissions.js|ts"
const pluginPermissions = {
  'accessOverview': [{ action: 'plugin::my-plugin.overview.access', subject: null }],
  'accessSidebar': [{ action: 'plugin::my-plugin.sidebar.access', subject: null }],
};

```

### Page permissions

Once you've created the configuration file you are ready to implement your permissions. If you've bootstrapped your plugin using the [plugin SDK init command](/cms/plugins-development/plugin-sdk#npx-strapisdk-plugin-init), you will have an example `HomePage.tsx` file. To implement page permissions you can do the following:

```js title="/src/plugins/my-plugin/admin/src/pages/HomePage.jsx|tsx" {2,5,12,16}

const HomePage = () => {
  const { formatMessage } = useIntl();

  return (
    
    </Page.Protect>
  );
};

```

You can see how we use our permissions configuration file together with the `<Page.Protect>` component to require specific permissions in order to view this page.

### Menu link permissions

The previous example makes sure that the permissions of a user that visits your page directly will be validated. However, you might want to remove the menu link to that page as well. To do that, you'll have to make a change to the `addMenuLink` implementation. You can do as follows:

```js title="/src/plugins/my-plugin/admin/src/index.js|ts" {21-23,5}

  register(app) {
    app.addMenuLink({
      to: `plugins/${PluginIcon}`,
      icon: PluginIcon,
      intlLabel: {
        id: `${PLUGIN_ID}.plugin.name`,
        defaultMessage: PLUGIN_ID,
      },
      Component: async () => {
        const { App } = await import('./pages/App');

        return App;
      },
      permissions: [
        pluginPermissions.accessOverview[0],
      ],
    });

    app.registerPlugin({
      id: PLUGIN_ID,
      initializer: Initializer,
      isReady: false,
      name: PLUGIN_ID,
    });
  },
};

```

### Custom permissions with the `useRBAC` hook

To get even more control over the permission of the admin user you can use the `useRBAC` hook. With this hook you can use the permissions validation just like you want, as in the following example:

```js title="/src/plugins/my-plugin/admin/src/components/Sidebar.jsx|tsx" 

const Sidebar = () => {
  const {
    allowedActions: { canAccessSidebar },
  } = useRBAC(pluginPermissions);

  if (!canAccessSidebar) {
    return null;
  }

  return (
    <div>Sidebar component</div>
  );
};

```