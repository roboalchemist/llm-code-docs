# Source: https://docs.redwoodjs.com/docs/tutorial/intermission

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [Tutorial]
-   [Intermission]

[Version: 8.8]

On this page

<div>

# Intermission

</div>

Let\'s take a break! If you really went through the whole tutorial so far: congratulations! If you just skipped ahead to this page to try and get a free congratulations: tsk, tsk!

That was potentially a lot of new concepts to absorb all at once so don\'t feel bad if all of it didn\'t fully sink in. React, GraphQL, Prisma, serverless functions\...so many things! Even those of us working on the framework are heading over to Google multiple times per day to figure out how to get these things to work together.

As an anonymous Twitter user once mused: \"If you enjoy switching between feeling like the smartest person on earth and the dumbest person in history all in the same day, programming may be the career for you!\"

## What\'s Next?[​](#whats-next "Direct link to What's Next?") 

Starting in Chapter 5 We\'ll look at Storybook and Jest and build a new feature for the blog: comments. Storybook introduces a new way to build components. We\'ll also add tests and run them with Jest to make sure things keep working as we expect. We cover authorization as well by giving a special role to comment moderators.

If you\'ve been through the tutorial so far, you can pick up where you left off and continue from here with Chapter 5. However, going forward we assume a complete test suite and several Storybook components, which we didn\'t get a chance to build in the first half. To get to the same starting point as the beginning of Chapter 5 you can start from this [example repo](https://github.com/redwoodjs/redwood-tutorial) (which we highly recommend) that picks up at the end of chapter 4, but already has additional styling, a starting test suite, and several Storybook components already built for you.

### Using Your Current Codebase[​](#using-your-current-codebase "Direct link to Using Your Current Codebase") 

If you want to use the same CSS classes we use in the following examples you\'ll need to add Tailwind to your repo:

``` 
yarn rw setup ui tailwindcss
```

However, none of the screenshots that follow will come anywhere close to what you\'re seeing in your browser (except for those isolated components you build in Storybook) so you may want to just start with the [example repo](https://github.com/redwoodjs/redwood-tutorial). You\'ll also be missing out on a good starting test suite that we\'ve added!

If you\'re *still* set on continuing with your own repo, and you deployed to a service like Netlify, you would have changed the database provider in `schema.prisma` to `postgresql`. If that\'s the case then make sure your local development environment has changed over as well. Check out the [Local Postgres Setup](/docs/local-postgres-setup) for assistance. If you stick with the [example repo](https://github.com/redwoodjs/redwood-tutorial) instead, you can go ahead with good ol\' SQLite (what we were using locally to build everything in the first half).

Once you\'re ready, start up the dev server:

``` 
yarn rw dev
```

### Using the Example Repo (Recommended)[​](#using-the-example-repo-recommended "Direct link to Using the Example Repo (Recommended)") 

If you haven\'t been through the first tutorial, or maybe you went through it on an older version of Redwood (anything pre-0.41) you can clone [this repo](https://github.com/redwoodjs/redwood-tutorial) which contains everything built so far and also adds a little styling so it isn\'t quite so\...tough to look at. The example repo includes [TailwindCSS](https://tailwindcss.com) to style things up and adds a `<div>` or two to give us some additional hooks to hang styling on.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTguODkzIDEuNWMtLjE4My0uMzEtLjUyLS41LS44ODctLjVzLS43MDMuMTktLjg4Ni41TC4xMzggMTMuNDk5YS45OC45OCAwIDAgMCAwIDEuMDAxYy4xOTMuMzEuNTMuNTAxLjg4Ni41MDFoMTMuOTY0Yy4zNjcgMCAuNzA0LS4xOS44NzctLjVhMS4wMyAxLjAzIDAgMCAwIC4wMS0xLjAwMkw4Ljg5MyAxLjV6bS4xMzMgMTEuNDk3SDYuOTg3di0yLjAwM2gyLjAzOXYyLjAwM3ptMC0zLjAwNEg2Ljk4N1Y1Ljk4N2gyLjAzOXY0LjAwNnoiPjwvcGF0aD48L3N2Zz4=)]The TypeScript version of the Example Repo is currently in progress

If you want to complete the tutorial in TypeScript, continue with your own repo, making any necessary edits. Don\'t worry, the remainder of the tutorial continues to offer both TypeScript and JavaScript example code changes.

``` 
git clone https://github.com/redwoodjs/redwood-tutorial
cd redwood-tutorial
yarn install
yarn rw prisma migrate dev
yarn rw g secret
```

That\'ll check out the repo, install all the dependencies, create your local database (SQLite) and fill it with a few blog posts. After that last command (`yarn rw g secret`) you\'ll need to copy the string that\'s output and add it to a file `.env` in the root of your project:

.env

``` 
SESSION_SECRET=JV2kA48ZU4FnLHwqaydy9beJ99qy4VgWXPkvsaw3xE2LGyuSur2dVq2PsPkPfygr
```

This is the encryption key for the secure cookies used in [dbAuth](/docs/tutorial/chapter4/authentication#session-secret).

Now just run `yarn rw dev` to start your development server. Your browser should open to a fresh new blog app:

![image](https://user-images.githubusercontent.com/300/101423176-54e93780-38ad-11eb-9230-ba8557764eb4.png)

Take a bathroom break and grab a fresh beverage, then let\'s get on with it!

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6Ij48L3BhdGg+PC9nPjwvc3ZnPg==)Edit the latest version of this page](https://github.com/redwoodjs/graphql/blob/main/docs/docs/tutorial/intermission.md)