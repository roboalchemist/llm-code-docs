# Source: https://docs.redwoodjs.com/docs/how-to/sending-emails

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [How To](/docs/how-to/index)
-   [Sending Emails]

[Version: 8.8]

On this page

<div>

# Sending Emails

</div>

Something a lot of applications will eventually have to do is send emails. To demonstrate how you can do that with RedwoodJS we\'re going to build a simple list of users and their email addresses, and allow you to trigger an email to them. We\'ll also include some auditing features, so you get a history of emails you sent to your users. The audit logs will be implemented by using one service from within another service --- a powerful RedwoodJS feature.

The emails will be sent using the npm package [nodemailer](https://www.npmjs.com/package/nodemailer) together with [SendInBlue](https://sendinblue.com).

## Setup[​](#setup "Direct link to Setup") 

The first thing to do is to create a new RedwoodJS project.

``` 
yarn create redwood-app --typescript email
```

When that\'s done, go into the `email` directory and install the `nodemailer` package.

``` 
yarn workspace api add nodemailer
```

### DB design[​](#db-design "Direct link to DB design") 

Now, fire up your editor of choice and find the `schema.prisma` file and remove the example model. The app we\'re building is going to have two models. One for our users and one for the audit logs. Paste the following two models in your schema file.

``` 
model User 

model Audit 
```

Technically all we really need in the User model is the email address and the Audit relation field. But personally I have never regretted having an id, and the two timestamps in my models. But I *have* regretted *not* having them, having to go back to add them later. So now I always include them from the start. And I also added a `name` field to the user, to make this example at least a little bit realistic 😁. A proper user model would most likely have way more fields. The audit model is also overly simplistic. Especially the single `log` string. A proper audit trail needs way more info. But for demo purposes it\'s good enough. Final thing I wanted to mention was the relation. We set up a one-to-many relation from the user to the audit logs so that we can easily find all logs belonging to a user by simply following the relation.

Now we can go ahead and migrate our database and create the SDLs and services needed to interact with the Prisma model using GraphQL.

``` 
yarn rw prisma migrate dev --name email
```

### Scaffold[​](#scaffold "Direct link to Scaffold") 

One of Redwood\'s stand-out features is the scaffolds. We\'ll be using scaffolds here to quickly get a nice visual list of the users in our database to work with.

``` 
yarn rw g scaffold User
```

Let\'s do it for Audit as well

``` 
yarn rw g scaffold Audit
```

Now let\'s run the Redwood dev server to see what we\'ve created so far.

``` 
yarn rw dev
```

Your web browser should open up and show the default Redwood app home page with a list of links to all your pages. Click on the `/users` link and then go ahead and create a few users. Since we\'re going to send emails to these users, use emails you can actually check. So you can make sure it works. A service I like to use for generating random users with real email addresses is [https://www.fakenamegenerator.com](https://www.fakenamegenerator.com). Just click the link on that page to activate the email address and you\'ll be able to send emails from your app, and see them arrive.

So if you create three users you should see something like this

![Screenshot showing list scaffolded list of users, with three example users](https://user-images.githubusercontent.com/30793/150651281-051d49d0-659c-481c-bed3-17a629d290e4.png)

Clicking to show the details on one of the users you should see a page similar to what I have below here. To that page I\'ve also added a button to send an email to the user. I\'ll show you how next!

![Detailed view of single user, with button to send email](https://user-images.githubusercontent.com/30793/150651287-258e923e-9446-4bde-8e9c-c81275b8590c.png)

### Button to send email[​](#button-to-send-email "Direct link to Button to send email") 

To add our button, and the actions connected to it, we need to add a fair bit of code to the User component. I\'ve put the full code below to make sure you don\'t miss anything.

src/components/User/User.tsx

``` 
import  from '@redwoodjs/web'
import  from '@redwoodjs/web/toast'
import  from '@redwoodjs/router'

const DELETE_USER_MUTATION = gql`
  mutation DeleteUserMutation($id: String!) 
  }
`

const EMAIL_USER_MUTATION = gql`
  mutation EmailUserMutation($id: String!) 
  }
`

const timeTag = (datetime) =>  title=>
      
    </time>
  )
}

const User = () => ,
    onError: (error) => ,
  })

  const [emailUser] = useMutation(EMAIL_USER_MUTATION, ,
    onError: (error) => ,
  })

  const onDeleteClick = (id) =>  })
    }
  }

  const onEmailClick = (user) => ?`))  })
    }
  }

  return (
    <>
      <div className="rw-segment">
        <header className="rw-segment-header">
          <h2 className="rw-heading rw-heading-secondary">
            User  Detail
          </h2>
        </header>
        <table className="rw-table">
          <tbody>
            <tr>
              <th>Id</th>
              <td></td>
            </tr>
            <tr>
              <th>Created at</th>
              <td></td>
            </tr>
            <tr>
              <th>Updated at</th>
              <td></td>
            </tr>
            <tr>
              <th>Email</th>
              <td></td>
            </tr>
            <tr>
              <th>Name</th>
              <td></td>
            </tr>
          </tbody>
        </table>
      </div>
      <nav className="rw-button-group">
        <Link
          to=)}
          className="rw-button rw-button-blue"
        >
          Edit
        </Link>
        <button
          type="button"
          className="rw-button rw-button-red"
          onClick=
        >
          Delete
        </button>
        <button
          type="button"
          className="rw-button rw-button-blue"
          onClick=
        >
          Send email
        </button>
      </nav>
    </>
  )
}

export default User
```

We\'re using a GraphQL mutation here to trigger the sending of the email. To make that mutation work we need to add it to the users SDL.

users.sdl.ts

``` 
export const schema = gql`
  // ...

  type Mutation 
`
```

And then in the users service we\'ll just create a dummy method to start with.

users.ts

``` 
// ...

import type  from '@prisma/client'

// ...

export const emailUser = async (: Prisma.UserWhereUniqueInput) => ,
  })

  console.log('Sending email to', user)

  return user
}

// ...
```

Now is a good time to go get a fresh cup of coffee, or other beverage of choice. When you come back we\'ll create an account at [SendInBlue](https://www.sendinblue.com) and use the credentials from there to send an email.

## SendInBlue[​](#sendinblue "Direct link to SendInBlue") 

To actually send an email you need a mail server that you can talk to using SMTP. `nodemailer` has a really [simple example](https://nodemailer.com/about/#example) on their webpage that uses Ethereal. But that\'s only for test messages. The emails will never actually be delivered beyond Ethereal. Another option is to use your own GMail address (if you have one). But to get that working reliably you need to set up OAuth2, which isn\'t very straight forward. So your best bet here is actually to use a dedicated Cloud/SaaS solution. A lot of them have a free tier that lets you send enough emails for a small production app. We\'ll be using SendInBlue that offers 300 free emails per day.

So go ahead and create an account with SendInBlue. They\'ll ask for an address and a phone number. They need it to prevent users from creating accounts to send spam emails from. When your account is created and set up you need to click on the menu in the upper right with your company name and select the \"SMTP & API\" option.

![SendInBlue top right menu](https://user-images.githubusercontent.com/30793/150651291-21f5a7bd-6148-4cfe-97a1-2e9c3cab2d81.png)

Then click on \"SMTP\"

![SendInBlue SMTP tab-bar option](https://user-images.githubusercontent.com/30793/150651295-929e671a-da38-46ab-937c-a976b23a0fa0.png)

Finally you need to generate a new SMTP key. Name it whatever you want, doesn\'t matter. You should get a dialog that looks like the screenshot below. Copy your key.

![SendInBlue SMTP key dialog](https://user-images.githubusercontent.com/30793/150651301-523750b3-7732-4a15-bc0e-746811a4bb20.png)

Now switch to your code editor and open the `.env` file. At the bottom, on a new row, create a new environment variable called SEND_IN_BLUE_KEY. It should look like this, but with your unique key.

```
SEND_IN_BLUE_KEY=xsmtpsib-REDACTED_TEST_KEY
```

That\'s it for SendInBlue. It\'s set up, and you have the key you need to send emails. If you have your dev server still running, you need to restart it for the new environment variable to be picked up.

## Sending an email[​](#sending-an-email "Direct link to Sending an email") 

Now let\'s write the function that\'ll fire off the email. On the api side, in the `lib` folder, create a new file named `email.ts`. Paste this code in the file

email.ts

``` 
import * as nodemailer from 'nodemailer'

interface Options 

export async function sendEmail(: Options) ,
  })

  // send mail with defined transport object
  const info = await transporter.sendMail()

  return info
}
```

In the code above you should replace \"[your@email.com](mailto:your@email.com)\" in two places with the email you used when signing up for SendInBlue. You can also change the name used for \"From:\". Note: Remember to use the email address as it is shown in the SendInBlue website, it is case sensitive.

Now let\'s go back to the users service and add the missing pieces there. At the top, after the db import, add the `sendEmail` import

users.ts

``` 
// ...

import  from 'src/lib/email'

// ...
```

Then paste this function somewhere in the file

users.ts

``` 
// ...

function sendTestEmail(emailAddress: string) )
}

// ...
```

Finally, replace the `console.log` we left earlier with this code

users.ts

``` 
// ...

await sendTestEmail(user.email)

// ...
```

You can now test your app\'s new email sending capabilities by clicking on the email button you added previously. You should see a \"Sending email to: [horacebcarrier@teleworm.us](mailto:horacebcarrier@teleworm.us)\" message in your terminal, and a few minutes later it should pop up in the users email inbox. (If you\'re using the email addresses generated by fakenamegenerator you need to be patient, it does take a while before you can see new emails arriving.)

## Using one service from another service[​](#using-one-service-from-another-service "Direct link to Using one service from another service") 

The final thing to add is the auditing. When the users service sends an email we want to call the audits service to add a new audit log entry. Redwood makes this really easy. All you have to do is import the service and you can use all the functions it exports!

One thing I wanted to note here is that this might bypass security measures you have in place. When you call a service from the web side of your project you use GraphQL and the service is then protected by the `@requireAuth` directive. If you have a service that\'s open for everyone (i.e. that uses `@skipAuth`) and that service imports and uses another service it will be allowed to call any function in there, no matter what directives they use on the graphql side of things. In our case the `emailUser` mutation is using `@requireAuth`, so we\'re not affected by this.

With that little PSA out of the way, let\'s make this auditing stuff happen!

users.ts

``` 
// ...

import  from '../audits/audits'

// ...

export const emailUser = async (: Prisma.UserWhereUniqueInput) => ,
  })

  // ...
}

// ...
```

That\'s it! We just import the audits service and call the exported `createAudit` function. The syntax for the argument object that is passed to `createAudit` might not be super obvious, but the TypeScript types help a lot with how it should be structured! What we\'re doing is we\'re connecting this new audit log with an existing user, and setting the log message. The audit entries will automatically get a timestamp (and a generated id).

To view the audit logs you can use the scaffolded pages we created earlier. Just navigate to [http://localhost:8910/audits](http://localhost:8910/audits) and you should see them there.

Thanks for reading this! If you liked it, or have any questions, don\'t hesitate to reach out on [our forums](https://community.redwoodjs.com) or in our [Discord chat](https://discord.com/invite/redwoodjs).

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6Ij48L3BhdGg+PC9nPjwvc3ZnPg==)Edit the latest version of this page](https://github.com/redwoodjs/graphql/blob/main/docs/docs/how-to/sending-emails.md)