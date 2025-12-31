# Source: https://docs.hypermode.com/dgraph/guides/message-board-app/react-ui/react-app-boiler-plate.md

# React App Boiler Plate

> Jump right in thanks to the Message Board App Tutorial repo on GitHub. Get started with your Message Board App in React with GraphQL.

<Info>
  We're overhauling Dgraph's docs to make them clearer and more approachable. If
  you notice any issues during this transition or have suggestions, please
  [let us know](https://github.com/hypermodeinc/docs/issues).
</Info>

## GitHub repo

All of the code for building the example React app shown in this tutorial is
available in GitHub in the
[Message Board App Tutorial repo](https://github.com/dgraph-io/discuss-tutorial).

Each step in the tutorial is recorded as a tag on the `learn-tutorial` branch in
that repo. That means you can complete each step in the tutorial and also look
at the git diff if you're comparing what's described to the corresponding code
changes.

## Boilerplate

You'd start an app like this with `npx create-react-app ...` and then
`yarn add ...` to add the dependencies listed on the previous page (i.e.,
Tailwind CSS, Semantic UI React, etc.)

This tutorial starts with the minimal boilerplate already complete. To read
through the setup process that was used to build this tutorial, see this
[blog about setting up a Dgraph Cloud app](https://hypermode.com/blog/slash-graphql-app-setup/).

For this tutorial, you can start with the boilerplate React app and CSS by
checking out the setup from GitHub. To do this, see the
[tutorial-boilerplate tag](https://github.com/dgraph-io/discuss-tutorial/releases/tag/tutorial-boilerplate).

You can do this using the `git` CLI.

```sh
git clone https://github.com/dgraph-io/discuss-tutorial
cd discuss-tutorial
git fetch --all --tags
git checkout tags/tutorial-boilerplate -b learn-tutorial
```

Alternatively, you can visit [https://github.com/dgraph-io/discuss-tutorial/tags](https://github.com/dgraph-io/discuss-tutorial/tags)
and download the archive (**.zip** or **.tar.gz**) for the
`tutorial-boilerplate` tag.

## Running app boilerplate

After you have the boilerplate code on your machine, you can start the app using
the following `yarn` command:

```sh
yarn install
yarn start
```

This command builds the source and serves the app UI in development mode. The
app UI is usually served at `http://localhost:3000`, but the exact port may vary
depending on what else is running on your machine. Yarn will report the URL as
soon as it has the server up and running.

Navigate to the provided URL, and you'll see the boilerplate app running, as
seen below:

<img src="https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/message-board-app/app-boilerplate.png?fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=889e56c9035c950aa698cea56aba67e4" alt="running boiler plate app" width="3104" height="974" data-path="images/dgraph/guides/message-board-app/app-boilerplate.png" srcset="https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/message-board-app/app-boilerplate.png?w=280&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=99a2123501f4265bf17b54d480f17fb3 280w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/message-board-app/app-boilerplate.png?w=560&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=4f463d956e2fe760241320e7ff06b405 560w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/message-board-app/app-boilerplate.png?w=840&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=4a57c4b9c7defa4d0ed6f03ab5525445 840w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/message-board-app/app-boilerplate.png?w=1100&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=416f5aec19163bba257dcb71d019c3c0 1100w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/message-board-app/app-boilerplate.png?w=1650&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=78f629956a59c9b40dc3083f79de4e4f 1650w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/message-board-app/app-boilerplate.png?w=2500&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=dd91c5a93c152e21312bb1b88c12a513 2500w" data-optimize="true" data-opv="2" />

At this point, you have just the CSS styling and minimal React setup. Next,
you'll [connect to your graph database](./connect-to-dgraph-cloud).
