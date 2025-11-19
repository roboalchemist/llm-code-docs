# Source: https://docs.baseten.co/development/model/deploy-and-iterate.md

# Deploy and iterate

> Deploy your model and quickly iterate on it.

In [Your First Model](/development/model/build-your-first-model), we walked through
how to deploy a basic model to Baseten. If you are trying to rapidly make changes
and iterate on your model, you'll notice that there is quite a bit of time between
running `truss push` and when the changes are reflected on Baseten.

Also, a lot of models require special hardware that you may not immediately have
access to.

To solve this problem, we have a feature called **Truss Watch**, that allows you to
live reload your model as you work.

# Truss Watch

To make use of `truss watch`, start by deploying your model:

```bash  theme={"system"}
$ truss push
```

By default, this will deploy a "development" version of your model. This means that the model
has a live reload server attached to it and supports hot reloading. To get the hot reload
loop working, simply run `truss watch` afterwards:

```bash  theme={"system"}
$ truss watch
```

Now, if you make changes to your model, you'll see them reflected in the model logs!

You can now happily iterate on your model without having to go through the entire
build & deploy loop between each change.

# Ready for Production?

Once you've iterated on your model, and you're ready to deploy it to production,
you can use the `truss push --publish` command. This will deploy a "published"
version of your model

```bash  theme={"system"}
truss push --publish
```

Note that development models have slightly worse performance, and have more
limited scaling properites, so it's highly recommend to not use these for
any production use-case.
