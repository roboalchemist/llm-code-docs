# Source: https://docs.redwoodjs.com/docs/how-to/dbauth-passwordless

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [How To](/docs/how-to/index)
-   [Setting up dbAuth to be passwordless]

[Version: 8.8]

On this page

<div>

# Setting up dbAuth to be passwordless

</div>

Security is really important. Sometimes you don\'t want to integrate with a third-party authentication services. Whatever the reason, Redwood has you covered with Redwood\'s dbAuth to authenticate users. This is a great option.

One thing though is now you\'re collecting the user\'s login and password. If you\'d like to not collect that, an alternative is to generate a token in place of the password. The only data needed for passwordless is the user\'s email address.

In this how-to I\'ll show you how to set up dbAuth to be passwordless, you\'ll still need to set up a way to [send emails](/docs/how-to/sending-emails), but there\'s plenty of ways to do that.

## Background[​](#background "Direct link to Background") 

Let me start by sharing a little bit about how passwordless works.

### What is a passwordless authentication method?[​](#what-is-a-passwordless-authentication-method "Direct link to What is a passwordless authentication method?") 

A passwordless authentication method is a method of authentication where the user is not required to enter a password. Instead, the user is sent a link to their email address. When they click the link, they are logged in.

Passwordless uses a token that is time-sensitive. So instead of storing a password, we store a token, and an expiration.

That token is generated randomly and is stored in the database.

## How to do it[​](#how-to-do-it "Direct link to How to do it") 

### 1. Modify the Prisma schema[​](#1-modify-the-prisma-schema "Direct link to 1. Modify the Prisma schema") 

First, you need to modify the Prisma schema.

If you followed the tutorial you\'ll have a `User` model. Here\'s is what it looks like with the changes you need to make.

``` 
model User 
```

Make note of the optional `salt` field.

Once you\'ve made the changes, you\'ll need to migrate your database.

``` 
yarn rw prisma migrate dev
```

### 2. Setting up the generateToken function[​](#2-setting-up-the-generatetoken-function "Direct link to 2. Setting up the generateToken function") 

Next, we need to create a function that will generate a token and an expiration date. For this you will need a Users service. If you don\'t already have a `/api/src/services/users/users.` file you can generate one with the following command.

``` 
yarn rw g service users
```

Now that you have the file, let\'s add the `generateToken` function.

/api/src/services/users/users.js

``` 
// add the following three imports to the top of the file
import crypto from 'node:crypto'

import  from '@redwoodjs/auth-dbauth-api'
import  from '@redwoodjs/graphql-server'

// add this to the bottom of the file
export const generateLoginToken = async () =>  })

    if (!lookupUser) 
    }

    // here we're going to generate a random password of 6 numbers
    const randomNumber = crypto
      .randomInt(0, 1_000_000)
      .toString()
      .padStart(6, '0')
    console.log('OTP:', randomNumber) // email the user this number

    const [loginToken, salt] = hashPassword(randomNumber)

    const loginTokenExpiresAt = new Date()
    loginTokenExpiresAt.setMinutes(loginTokenExpiresAt.getMinutes() + 15)

    // now we'll update the user with the new salt and loginToken
    await db.user.update(,
      data: ,
    })

    return 
  } catch (error) )
    throw new UserInputError(error.message)
  }
}
```

### 3. Add generateToken to the SDL and secure loginToken[​](#3-add-generatetoken-to-the-sdl-and-secure-logintoken "Direct link to 3. Add generateToken to the SDL and secure loginToken") 

In addition to the new function, we need to add it to the sdl file. While we\'re here let\'s also ensure we do not expose the loginToken. This file may be users.sdl.js or users.sdl.ts depending on if you set up Redwood to use JavaScript or TypeScript.

/api/src/graphql/users.sdl.js

``` 
export const schema = gql`
  type User 

  input CreateUserInput 

  input UpdateUserInput 

  type UserTokenResponse 

  type Mutation 
```

### 4. Modify the auth function[​](#4-modify-the-auth-function "Direct link to 4. Modify the auth function") 

We need to consider how we want to limit the authentication. I\'ve added an expiration date to the token, so we\'ll need to check that.

/api/src/functions/auth.js

``` 
// ... other functions
const loginOptions = 

    // If the user logged in with a token we need to break the token. We'll do
    // this by clearing the salt and expiration. This will make the token a
    // one-time use token
    db.user.update(,
      data: ,
    })

    return user
  },
  errors: ,
}

// we also need to update signupOptions
const signupOptions = ) => ,
    })
  },
  // ... othter stuff
}

// and last we need to update the authFields
const authHandler = new DbAuthHandler(event, context, ,
  // ... other stuff
})
```

As of right now, nothing works -- let\'s fix that!

### 5. Making the login form[​](#5-making-the-login-form "Direct link to 5. Making the login form") 

We need to make a form that will allow the user to enter their email address.

Let\'s start with the generator.

``` 
yarn rw g component LoginPasswordlessForm
```

This created a component in `web/src/components/LoginPasswordlessForm/LoginPasswordlessForm.`. Let\'s update it.

/web/src/components/LoginPasswordlessForm/LoginPasswordlessForm.js

``` 
import  from '@redwoodjs/forms'
import  from '@redwoodjs/router'
import  from '@redwoodjs/web'
import  from '@redwoodjs/web/toast'

const GENERATE_LOGIN_TOKEN_MUTATION = gql`
  mutation GenerateLoginTokenMutation($email: String!) 
  }
`

const LoginPasswordlessForm = () => ,
  })

  const onSubmit = async (data) => ,
      fetchPolicy: 'no-cache',
    })

    if (response.error) 
  }

  return (
    <>
      <Metadata title="Login" />
      <main className="rw-main">
        <Toaster toastOptions=} />
        <div className="rw-scaffold rw-login-container">
          <div className="rw-segment">
            <header className="rw-segment-header">
              <h2 className="rw-heading rw-heading-secondary">Login</h2>
            </header>

            <div className="rw-segment-main">
              <div className="rw-form-wrapper">
                <Form onSubmit= className="rw-form-wrapper">
                  <Label
                    name="email"
                    className="rw-label"
                    errorClassName="rw-label rw-label-error"
                  >
                    Email
                  </Label>
                  <TextField
                    name="email"
                    className="rw-input"
                    errorClassName="rw-input rw-input-error"
                    validation=,
                    }}
                  />

                  <FieldError name="email" className="rw-field-error" />
                  <div className="rw-button-group">
                    <Submit className="rw-button rw-button-blue">
                      Send Token
                    </Submit>
                  </div>
                </Form>
              </div>
            </div>
          </div>
          <div className="rw-login-link">
            <span>Don&apos;t have an account?</span>
            <Link to= className="rw-link">
              Sign up!
            </Link>
          </div>
        </div>
      </main>
    </>
  )
}

export default LoginPasswordlessForm
```

We aren\'t rendering it anywhere yet, but when we do it will look like this.

![image](https://user-images.githubusercontent.com/638764/220204773-6c6aaf86-680f-4e2c-877c-3876070254d3.png)

### 6. Making the login with token form[​](#6-making-the-login-with-token-form "Direct link to 6. Making the login with token form") 

Now we also need a form that will accept the code that was sent to the user.

``` 
yarn rw g component LoginPasswordlessTokenForm
```

/web/src/components/LoginPasswordlessTokenForm/LoginPasswordlessTokenForm.js

``` 
import  from 'react'

import  from '@redwoodjs/forms'
import  from '@redwoodjs/router'
import  from '@redwoodjs/web'
import  from '@redwoodjs/web/toast'

import  from 'src/auth'

const LoginPasswordlessTokenForm = () =>  = useAuth()
  useEffect(() => 

    if (email && code) )
    }
  }, [isAuthenticated, email, code, logIn])

  const onSubmit = async (data) => )

    if (response.error) 
  }

  return (
    <>
      <Metadata title="Login" />
      <main className="rw-main">
        <Toaster toastOptions=} />
        <div className="rw-scaffold rw-login-container">
          <div className="rw-segment">
            <header className="rw-segment-header">
              <h2 className="rw-heading rw-heading-secondary">
                Login with Token
              </h2>
            </header>

            <div className="rw-segment-main">
              <div className="rw-form-wrapper">
                <Form onSubmit= className="rw-form-wrapper">
                  <Label
                    name="email"
                    className="rw-label"
                    errorClassName="rw-label rw-label-error"
                  >
                    Email
                  </Label>
                  <TextField
                    name="email"
                    className="rw-input"
                    errorClassName="rw-input rw-input-error"
                    readOnly=
                    defaultValue=
                  />

                  <FieldError name="email" className="rw-field-error" />
                  <Label
                    name="loginToken"
                    className="rw-label"
                    errorClassName="rw-label rw-label-error"
                  >
                    Token
                  </Label>
                  <TextField
                    name="loginToken"
                    className="rw-input"
                    errorClassName="rw-input rw-input-error"
                  />

                  <FieldError name="loginToken" className="rw-field-error" />
                  <div className="rw-button-group">
                    <Submit className="rw-button rw-button-blue">Login</Submit>
                  </div>
                  <div className="rw-button-group">
                    <button
                      className="rw-button rw-button-blue"
                      onClick=}
                    >
                      Get another Token
                    </button>
                  </div>
                </Form>
              </div>
            </div>
          </div>
          <div className="rw-login-link">
            <span>Don&apos;t have an account?</span>
            <Link to= className="rw-link">
              Sign up!
            </Link>
          </div>
        </div>
      </main>
    </>
  )
}

export default LoginPasswordlessTokenForm
```

This will be the form loaded after the email is entered. Again, we aren\'t rendering it anywhere, but we will in the next step.

Here\'s a preview of the form.

![image](https://user-images.githubusercontent.com/638764/220212316-bcc5cde6-53cf-4a65-ab54-0e2763da924a.png)

### 7. Making the new login page[​](#7-making-the-new-login-page "Direct link to 7. Making the new login page") 

Now each of those forms are controlled with the props we pass to them. We will make a new page that will control the state of the forms.

``` 
yarn rw g page LoginPasswordless
```

/web/pages/LoginPasswordlessPage/LoginPasswordlessPage.js

``` 
import  from 'react'

import  from '@redwoodjs/router'
import  from '@redwoodjs/web'

import LoginPasswordlessForm from 'src/components/LoginPasswordlessForm/LoginPasswordlessForm'
import LoginPasswordlessTokenForm from 'src/components/LoginPasswordlessTokenForm/LoginPasswordlessTokenForm'

const LoginPasswordlessPage = () =>  = useLocation()

  useEffect(() => 
  }, [search])

  return (
    <>
      <Metadata
        title="LoginPasswordless"
        description="LoginPasswordless page"
      />

      
          setWaitingForCode=
          code=
        />
      ) : (
        <LoginPasswordlessForm
          setWaitingForCode=
          setEmail=
        />
      )}
    </>
  )
}

export default LoginPasswordlessPage
```

### 8. Updating the signup page[​](#8-updating-the-signup-page "Direct link to 8. Updating the signup page") 

We need to update the signup page to just take the email.

/web/src/pages/SignupPage/SignupPage.js

``` 
import  from 'react'

import  from '@redwoodjs/forms'
import  from '@redwoodjs/router'
import  from '@redwoodjs/web'
import  from '@redwoodjs/web/toast'

import  from 'src/auth'

function randomString(length) 

const SignupPage = () =>  = useAuth()

  useEffect(() => 
  }, [isAuthenticated])

  // focus on username box on page load
  const emailRef = useRef(null)
  useEffect(() => , [])

  const onSubmit = async (data) => )

    if (response.message)  else if (response.error)  else 
  }

  return (
    <>
      <Metadata title="Signup" />

      <main className="rw-main">
        <Toaster toastOptions=} />
        <div className="rw-scaffold rw-login-container">
          <div className="rw-segment">
            <header className="rw-segment-header">
              <h2 className="rw-heading rw-heading-secondary">Signup</h2>
            </header>

            <div className="rw-segment-main">
              <div className="rw-form-wrapper">
                <Form onSubmit= className="rw-form-wrapper">
                  <Label
                    name="email"
                    className="rw-label"
                    errorClassName="rw-label rw-label-error"
                  >
                    Email
                  </Label>
                  <TextField
                    name="email"
                    className="rw-input"
                    errorClassName="rw-input rw-input-error"
                    ref=
                    validation=,
                    }}
                  />
                  <FieldError name="email" className="rw-field-error" />

                  <div className="rw-button-group">
                    <Submit className="rw-button rw-button-blue">
                      Sign Up
                    </Submit>
                  </div>
                </Form>
              </div>
            </div>
          </div>
          <div className="rw-login-link">
            <span>Already have an account?</span>
            <Link to= className="rw-link">
              Log in!
            </Link>
          </div>
        </div>
      </main>
    </>
  )
}

export default SignupPage
```

You should see the changes and it should look like this!

![image](https://user-images.githubusercontent.com/638764/220204883-800829ab-e037-41e1-a2da-d47923c4d20c.png)

### 9. Updating the routes[​](#9-updating-the-routes "Direct link to 9. Updating the routes") 

The last thing we need to to do is update the routes to use the new page.

/web/src/Routes.js

``` 
const Routes = () => >
      <Route path="/login" page= name="login" />
      <Route path="/signup" page= name="signup" />
      
    </Router>
  )
}
```

## You did it\![​](#you-did-it "Direct link to You did it!") 

Now that you did you can rest easy. Your authentication relies on just your database but also, if some bad actor got access to it the only user data you have is really the email address.

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6Ij48L3BhdGg+PC9nPjwvc3ZnPg==)Edit the latest version of this page](https://github.com/redwoodjs/graphql/blob/main/docs/docs/how-to/dbauth-passwordless.md)