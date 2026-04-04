# Source: https://docs.upsun.com/create-apps/hooks/hooks-and-dependencies.md

# Use hooks with dependencies

If you use a specific package in a hook, you may want to manage dependencies for it.
For example, you may want to compile Sass files as part of your build process.
You can set dependencies along with hooks in your [app configuration](https://docs.upsun.com/create-apps/app-reference/single-runtime-image.md#dependencies).

The following example assumes you have some Sass source files, such as a `index.scss` file.
You also need a script to compile the files, such as the following:

```json  {location="package.json"}
{
  "scripts": {
    "build-css": "sass index.scss css/index.css"
  },
}
```

Set your app configuration to have Sass available globally and use it:

```yaml  {location=".upsun/config.yaml"}
applications:
  myapp:
    # Ensure sass is available globally
    dependencies:
      nodejs:
        sass: "^1.47.0"

    hooks:
      # Run the script defined in package.json
      build: |
        npm run build-css
```

