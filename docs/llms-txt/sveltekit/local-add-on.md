# Local add-on
npx sv add file:../path/to/my-addon
```

### How to create a community add-on

To start on a good track, create your add-on with the `addon` template.

```sh
npx sv create --template addon [path]
```

In your new add-on directory, check out the `README.md` and `CONTRIBUTING.md` to get started.

Then you can continue with the [API docs](/docs/cli/add-on) to start building your add-on. You can also have a look at the [official addons source code](https://github.com/sveltejs/cli/tree/main/packages/sv/src/addons) to get some inspiration on what can be done.