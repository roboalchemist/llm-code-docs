# Admin panel customization

The **front-end part of Strapi**  is called the admin panel. The admin panel presents a graphical user interface to help you structure and manage the content that will be accessible through the Content API. To get an overview of the admin panel, please refer to the [Getting Started > Admin panel](/cms/features/admin-panel) page.

From a developer point of view, Strapi's admin panel is a React-based single-page application that encapsulates all the features and installed plugins of a Strapi application.

Admin panel customization is done by tweaking the code of the `src/admin/app` file or other files included in the `src/admin` folder (see [project structure](/cms/project-structure)). By doing so, you can:

- Customize some parts of the admin panel to better reflect your brand identity (logos, favicon) or your language,
- Replace some other parts of the admin panel, such as the Rich text editor and the bundler,
- Extend the theme or the admin panel to add new features or customize the existing user interface.

## General considerations

:::prerequisites
Before updating code to customize the admin panel:

- Rename the default `app.example.tsx|js` file into `app.ts|js`.
- Create a new `extensions` folder in `/src/admin/`.
- If you want to see your changes applied live while developing, ensure the admin panel server is running (it's usually done with the `yarn develop` or `npm run develop` command if you have not changed the default [host, port, and path](/cms/configurations/admin-panel#admin-panel-server) of the admin panel).
:::

Most basic admin panel customizations will be done in the `/src/admin/app` file, which includes a `config` object.

Any file used by the `config` object (e.g., a custom logo) should be placed in a `/src/admin/extensions/` folder and imported inside `/src/admin/app.js`.

</Tabs>

This will replace the folder's content located at `./build`. Visit 

## Basic example

The following is an example of a basic customization of the admin panel:

</Tabs>

:::strapi Detailed examples in the codebase

* You can see the full translation keys, for instance to change the welcome message, [on GitHub](https://github.com/strapi/strapi/blob/develop/packages/core/admin/admin/src/translations).
* Light and dark colors are also found [on GitHub](https://github.com/strapi/design-system/tree/main/packages/design-system/src/themes).
:::