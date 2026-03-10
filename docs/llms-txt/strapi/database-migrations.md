# Database migrations

Database migrations exist to run one-time queries against the database, typically to modify the tables structure or the data when upgrading the Strapi application. These migrations are run automatically when the application starts and are executed before the automated schema migrations that Strapi also performs on boot.

:::callout 🚧  Experimental feature
Database migrations are experimental. This feature is still a work in progress and will continue to be updated and improved. In the meantime, feel free to ask for help on the 

</Tabs>

Additionally, if you want to continue using existing JavaScript migrations alongside TypeScript migrations, you can set `allowJs: true` in your `tsconfig.json` file's compiler options, as mentioned in the [database configuration documentation](/cms/configurations/database#settings-configuration-object).