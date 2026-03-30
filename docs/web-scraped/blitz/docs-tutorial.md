# Source: https://blitzjs.com/docs/tutorial

Title: Tutorial - Blitz.js

URL Source: https://blitzjs.com/docs/tutorial

Markdown Content:
In this tutorial, we’ll walk you through the creation of a basic voting application.

We’ll assume that you have [Blitz installed](https://blitzjs.com/docs/get-started) already. You can tell if Blitz is installed, and which version you have by running the following command in your terminal:

If Blitz is installed, you should see the version of your installation. If it isn’t, you’ll get an error saying something like “command not found: blitz”.

[](https://blitzjs.com/docs/tutorial#creating-a-new-app)Creating a new app
--------------------------------------------------------------------------

From the command line, `cd` into the folder where you’d like to create your app, and then run the following command:

Blitz will create a `my-blitz-app` folder in your current folder. You will be asked how you want your new app to be. For this tutorial, select all the default values by only pressing **Enter** when asked (you'll create a Full Blitz app with TypeScript, npm and React Final Form).

Let’s look at what `blitz new` created:

These files are:

* The `src/` folder has Blitz setup files — `blitz-client.ts` and `blitz-server.ts`. This is also where you’ll put any queries/mutations or some of your components.

* The `src/pages/` folder is the primary pages folder. You'll put all your pages and API routes here.

* The `src/core/` folder is the main place to put components, hooks, etc that are used throughout your app.

* `db/` is where your database configuration goes. If you’re writing models or checking migrations, this is where to go.

* `public/` is a folder where you will put any static assets. If you have images, files, or videos which you want to use in your app, this is where to put them.

* `.npmrc`, `.env`, etc. ("dotfiles") are configuration files for various bits of JavaScript tooling.

* `next.config.js` is for advanced custom configuration of Blitz and Next.js.

* `tsconfig.json` is our recommended setup for TypeScript.

You can read more about the [file structure here](https://blitzjs.com/docs/file-structure).

[](https://blitzjs.com/docs/tutorial#the-development-server)The development server
----------------------------------------------------------------------------------

Now make sure you are in the `my-blitz-app` folder, if you haven’t already, and run the following command:

You’ll see the following output on the command line:

Now that the server’s running, visit [localhost:3000](http://localhost:3000/) with your web browser. You’ll see a welcome page, with the Blitz logo. It worked!

[](https://blitzjs.com/docs/tutorial#sign-up-as-a-user)Sign up as a user
------------------------------------------------------------------------

Blitz apps are created with user signup and login already set up! So let's try it. Click on the **Sign Up** button. Enter any email and password and click **Create Account**. Then you'll be redirected back to the home page where you can see your user `id` and `role`.

If you want, you can also try logging out and logging back in. Or click **Forgot your password?** on the login page to try that flow.

[](https://blitzjs.com/docs/tutorial#write-your-first-page)Write your first page
--------------------------------------------------------------------------------

Next let's create your first page.

Open the file `pages/index.tsx` and replace the contents of the `Home` component with this:

Save the file and you should see the page update in your browser. You can customize this as much as you want. When you’re ready, move on to the next section.

[](https://blitzjs.com/docs/tutorial#database-setup)Database setup
------------------------------------------------------------------

Good news, an SQLite database was already set up for you! You can run `blitz prisma studio` in the terminal to open a web interface where you can see the data in your database.

Note that when starting your first real project, you may want to use a more scalable database like PostgreSQL, to avoid the pains of switching your database down the road. For more information, see [Database overview](https://blitzjs.com/docs/database-overview). For now, we will continue with the default SQLite database.

[](https://blitzjs.com/docs/tutorial#scaffolding-code-for-our-models)Scaffolding code for our models
----------------------------------------------------------------------------------------------------

Blitz provides a handy CLI command called [`generate`](https://blitzjs.com/docs/cli-generate) for scaffolding out boilerplate code. We'll use `generate` to create two models: `Question` and `Choice`. A `Question` has the text of the question and a list of choices. A `Choice` has the text of the choice, a vote count, and an associated question. Blitz will automatically generate an id, a creation timestamp, and a last updated timestamp for both models.

#### First, we'll generate everything pertaining to the `Question` model

And when prompted, press the **Enter** to run `prisma migrate` which will update your database schema with the new model. It will ask for a name, so type something like "add question".

The `generate` command with a type of `all` generates a model and queries, mutation and page files. See the [Blitz generate](https://blitzjs.com/docs/cli-generate) page for a list of available type options.

#### Next we'll generate the `Choice` model with corresponding queries and mutations

We'll pass a type of `resource` this time as we don't need to generate pages for the `Choice` model:

If you get an error run `blitz prisma format`

Note that this doesn't require a database migration because we haven't added the `Choice` field to the `Question` model yet. So we are choosing `false` when prompted to run the migration:

#### Lastly let's update the `Question` model to have a relationship back to `Choice`

Open `db/schema.prisma` and add `choices Choice[]` to the `Question` model.

Now we can run the migration to update our database:

And again, enter a name for the migration, like "add choice":

Now our database is ready and a Prisma client is also generated. Lets move on to play with the Prisma client!

[](https://blitzjs.com/docs/tutorial#update-generated-code-for-our-model-attributes)Update generated code for our model attributes
----------------------------------------------------------------------------------------------------------------------------------

##### Info

Before running the app again, we need to customize some of the code that has been generated. Ultimately, these fixes will not be needed - but for now, we need to work around a couple outstanding issues.

The generated page content does not currently use the actual model attributes you defined during generation. It will soon, but in the meantime, let's fix the generated pages.

### [](https://blitzjs.com/docs/tutorial#question-pages)Question pages

Jump over to `src/pages/questions/index.tsx`. Notice that a `QuestionsList` component has been generated for you:

This won’t work though! Remember that the `Question` model we created above doesn’t have any `name` field. To fix this, replace `question.name` with `question.text`:

Next, let’s apply a similar fix to `src/questions/components/QuestionForm.tsx`. In the form submission, replace the `LabeledTextField``name` to be `"text"`

### [](https://blitzjs.com/docs/tutorial#create-question-mutation)`createQuestion` mutation

In `src/questions/mutations/createQuestion.ts`, we need to update the `CreateQuestion` zod validation schema to use `text` instead of `name`.

### [](https://blitzjs.com/docs/tutorial#update-question-mutation)`updateQuestion` mutation

In `src/questions/mutations/updateQuestion.ts`, we need to update the `UpdateQuestion` zod validation schema to use `text` instead of `name`.

### [](https://blitzjs.com/docs/tutorial#delete-question-mutation)`deleteQuestion` mutation

Prisma does not yet support "cascading deletes". In the context of this tutorial, that means it does not currently delete the `Choice` data when deleting a `Question`. We need to temporarily augment the generated `deleteQuestion` mutation in order to do this manually. Open up `src/questions/mutations/deleteQuestion.ts` in your text editor and add the following to the top of the function body:

The end result should be as such:

This mutation will now delete the choices associated with the question prior to deleting the question itself.

### [](https://blitzjs.com/docs/tutorial#update-choice-mutation)`updateChoice` mutation

In `src/choices/mutations/updateChoice.ts`, we need to update the `UpdateChoice` zod validation schema to use `text` instead of `name`.

[](https://blitzjs.com/docs/tutorial#remove-unnecessary-file)Remove unnecessary file
------------------------------------------------------------------------------------

Our scaffolding created a mutation file for us that is no longer needed. In order for `yarn tsc` or `git push` to succeed, you'll need to delete `src/choices/mutations/createChoice.ts` (unused) or update the CreateChoice zod schema to include the required fields.

#### Now try creating, updating, and deleting questions

Great! Now make sure you stop the application, start it again with `blitz dev` in your terminal, and visit `localhost:3000/questions`. Try creating questions, editing, and deleting them.

[](https://blitzjs.com/docs/tutorial#adding-choices-to-the-question-form)Adding choices to the question form
------------------------------------------------------------------------------------------------------------

You’re doing great so far! The next thing we’ll do is add choices to our question form. Open `src/questions/components/QuestionForm.tsx` in your editor.

Add three more `<LabeledTextField>` components as choices.

Now open `src/questions/mutations/createQuestion.ts` and update the zod schema so that the choice data is accepted in the mutation. We also need to update the `db.question.create()` call so that the choices will be created. After that we need to export the `CreateQuestion` zod schema because we will be using it in the next step to create a validation schema for our `QuestionForm`.

Next we're going to create a separate file to store the validation schema for our `QuestionForm`. In the `src/questions` folder create a new file called `validations.ts` and move the `CreateQuestion` variable from `./mutations/createQuestion.ts` to the new `validations.ts` file. Then, in `src/questions/mutations/createQuestion.ts` import `CreateQuestion` from `../validations`.

##### Info

We create a shared `validations.ts` file because we cannot import anything from a query (or mutation) file other than the query itself into the client. You can read more about why in [Query Usage](https://blitzjs.com/docs/query-usage) and [Mutation Usage](https://blitzjs.com/docs/mutation-usage).

Now open `src/pages/questions/new.tsx` and import `CreateQuestion` from `src/questions/validations.ts` and set it as the schema for `QuestionForm`. Also, we need set `{{text: "", choices: []}}` as our `initialValues` for `QuestionForm`:

#### Try it out

Now you can go to `localhost:3000/questions/new` and create a new question with choices!

[](https://blitzjs.com/docs/tutorial#listing-choices)Listing choices
--------------------------------------------------------------------

Time for a breather. Go back to `localhost:3000/questions` in your browser and look at all the questions you‘ve created. How about we list these questions’ choices here too? First, we need to customize the question queries. In Prisma, you need to manually let the client know that you want to query for nested relations. Change your `getQuestion.ts` and `getQuestions.ts` files to look like this:

Now hop back to our main questions page (`src/pages/questions/index.tsx`)in your editor, and we can list the choices of each question. And add this code beneath the `Link` in our `QuestionsList`:

Restart your app — stop dev server and run `yarn dev`, `npm dev`, or `pnpm dev` again. Now check `/questions` in the browser. **Magic!**

[](https://blitzjs.com/docs/tutorial#let-people-vote-on-questions)Let’s let people vote on these questions
-----------------------------------------------------------------------------------------------------------

Open `src/pages/questions/[questionId].tsx` in your editor. First, we’re going to improve this page somewhat.

1. Replace `<title>Question {question.id}</title>` with `<title>{question.text}</title>`.

2. Replace `<h1>Question {question.id}</h1>` with `<h1>{question.text}</h1>`.

3. Delete the `pre` element, and copy in our choices list which we wrote before:

If you go back to your browser, your page should now look something like this!

![Image 1: Screenshot](https://user-images.githubusercontent.com/24858006/80387990-3c3d8b80-88a1-11ea-956a-5be85f1e8f12.png)

#### Now it’s time to add voting

First we need to open `src/choices/mutations/updateChoice.ts`, update the zod schema, and add a vote increment.

Now go back to `src/pages/questions/[questionId].tsx` and make the following changes:

In our `li`, add a `button` like so:

Then, import the `updateChoice` mutation we updated and create a `handleVote` function in our page:

And then we need to update the question `useQuery` call to return the `refetch` function which we use inside `handleVote`:

Finally, we’ll tell our new `button` to call that function!

The final `Question` component should now look like this:

[](https://blitzjs.com/docs/tutorial#edit-choices-for-question)Lastly, let's allow editing choices for an existing question
---------------------------------------------------------------------------------------------------------------------------

If you click the **Edit** button on one of your existing questions, you'll see it uses the same form as creating questions. So that part is already done! We only need to update our mutation.

Open `src/questions/mutations/updateQuestion.ts` and make the following changes:

[`upsert`](https://www.prisma.io/docs/reference/api-reference/prisma-client-reference#upsert) is a special operation that means, "If this item exists, update it. Else create it". This is perfect for this case because we didn't require the user to add three choices when creating the question. So if later the user adds another choice by editing the question, then it'll be created here.

[](https://blitzjs.com/docs/tutorial#conclusion)Conclusion
----------------------------------------------------------

🥳 Congrats! You created your very own Blitz app! Have fun playing around with it, or sharing it with your friends. Now that you’ve finished this tutorial, why not try making your voting app even better? You could try:

* Adding styling
* Showing some more statistics about votes

If you want to share your project with the world wide Blitz community there is no better place to do that than on Discord.

Visit [discord.blitzjs.com](https://discord.blitzjs.com/). Then, post the link to the **#built-with-blitz** channel to share it with everyone!

* * *

[Idea for improving this page? Edit it on GitHub.](https://github.com/blitz-js/blitzjs.com/edit/main/app/pages/docs/tutorial.mdx)
