# Source: https://docs.redwoodjs.com/docs/how-to/role-based-access-control-rbac

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [How To](/docs/how-to/index)
-   [Role-based Access Control (RBAC)]

[Version: 8.8]

On this page

<div>

# Role-based Access Control (RBAC)

</div>

Role-based access control (RBAC) in RedwoodJS aims to be a simple, manageable approach to access management. It adds control over who can access routes, see features, or invoke services or functions to the existing `useAuth()` hook on the web side and `requireAuth()` helper on the api side.

A **role** is a collection of permissions applied to a set of users based on the part they play in an organization or setting. Using roles makes it easier to add, remove, and adjust these permissions as your user base increases in scale and functionality increases in complexity.

This how to examines how RBAC is implemented in RedwoodJS and [how to protect](#how-to-code-examples) areas of your app\'s sides \-- web, api, or custom.

### Quick Links[​](#quick-links "Direct link to Quick Links") 

-   [Authentication vs Authorization](#authentication-vs-authorization)
-   [House and Blog Role-access Examples](#house-and-blog-role-access-examples)
-   [Identity as a Service](#identity-as-a-service)
-   [How To Code Examples](#how-to-code-examples)
-   [Additional Resources](#additional-resources)

## Authentication vs Authorization[​](#authentication-vs-authorization "Direct link to Authentication vs Authorization") 

How is Authorization different from Authentication?

-   **Authentication** is the act of validating that users are who they claim to be.
-   **Authorization** is the process of giving the user permission to access a specific resource or function.

In even more simpler terms authentication is the *process* of verifying oneself, while authorization is the *process* of verifying what you have access to.

### House and Blog Role-access Examples[​](#house-and-blog-role-access-examples "Direct link to House and Blog Role-access Examples") 

When thinking about security, it helps to think in terms of familiar examples.

Let\'s consider one from the physical world \-- access to the various rooms of a 🏠 house \-- and compare it to a digital example of a Blog.

#### RBAC Example: House[​](#rbac-example-house "Direct link to RBAC Example: House") 

Consider a 🏠 while you are away on vacation.

You are the ***owner*** and have given out 🔑 keys to your **neighbor** and a **plumber** that unlock the 🏠 🚪 door.

You\'ve assigned them passcodes to turn off the 🚨 alarm that identifies them as either a neighbor or plumber.

Your neighbor can enter the kitchen to get food to feed your 😸 and the your office to water your 🌵 and also use the 🚽.

The plumber can access the basement to get at the pipes, use the 🚽, access the laundry or 🍴 kitchen to fix the sink, but not your office.

Neither of them should be allowed into your 🛏 bedroom.

The owner knows who they claim to be and has given them keys.

The passcodes inform what access they have because it says if they are a neighbor or plumber.

If your 🏠 could enforce RBAC, it needs to know the rules.

#### Role Matrix for House RBAC[​](#role-matrix-for-house-rbac "Direct link to Role Matrix for House RBAC") 

Role

Kitchen

Basement

Office

Bathroom

Laundry

Bedroom

Neighbor

✅

✅

✅

Plumber

✅

✅

✅

✅

Owner

✅

✅

✅

✅

✅

✅

#### RBAC Example: Blog[​](#rbac-example-blog "Direct link to RBAC Example: Blog") 

In our Blog example anyone can view Posts (authenticated or not). They are *public*.

-   Authors can write new Posts.
-   Editors can update them.
-   Publishers can write, review, edit and delete Posts.
-   And admins can do it all (and more).

#### Role Matrix for Blog RBAC[​](#role-matrix-for-blog-rbac "Direct link to Role Matrix for Blog RBAC") 

Role

View

New

Edit

Delete

Manage Users

Author

✅

✅

Editor

✅

✅

Publisher

✅

✅

✅

✅

Admin

✅

✅

✅

✅

✅

## Auth and RBAC Checklist[​](#auth-and-rbac-checklist "Direct link to Auth and RBAC Checklist") 

In order to integrate RBAC in a RedwoodJS app, you will have to:

-   Implement an Identity as a Service/Authentication Provider
-   Define and Assign Roles
-   Set Roles to Current User
-   Enforce Access
-   Secure Web and Api sides

Helps to be familiar with [Blog Tutorial](/docs/tutorial/foreword) as well as pages, cells, services, authentication, and routes.

## Identity as a Service[​](#identity-as-a-service "Direct link to Identity as a Service") 

> \"Doing authentication correctly is as hard, error-prone, and risky as rolling your own encryption.\"

Developers no longer need to be responsible for developing their own identity service. The identity service manages authentication and the complexity associated.

RedwoodJS generates Authentication Providers for several common Identity Services.

Some offer RBAC support natively together with a UI to manage users and role assignment.

-   Netlify Identity
-   Auth0

In other cases, you can still use an Identity Service such as:

-   Magic.link
-   Custom

However, in these cases you must provide the `currentUser.roles` information directly, such as from a User to Role database table or other source.

### Netlify Identity Access Token (JWT) & App Metadata[​](#netlify-identity-access-token-jwt--app-metadata "Direct link to Netlify Identity Access Token (JWT) & App Metadata") 

The following is a brief example of a **decoded** JSON Web Token (JWT) similar to that issued by Netlify Identity.

There are the following standard claims:

-   `exp`: When the token expires.
-   `sub`: The token\'s subject, in this case the user identifier.

Other common claims are `iss` for issuer and `aud` for audience (ie, the recipient for which the JWT is intended).

Please see [Introduction to JSON Web Tokens](https://jwt.io/introduction/) for a complete discussion.

This decoded token also includes:

-   `app_metadata`: Stores information (such as, support plan subscriptions, security roles, or access control groups) that can impact a user\'s core functionality, such as how an application functions or what the user can access. Data stored in app_metadata cannot be edited by users
-   `user_metadata`: Stores user attributes such as preferences that do not impact a user\'s core functionality. Logged in users can edit their data stored in user_metadata typically by making an api call the Identity service user profile endpoint with their access_token to identify themselves.

Roles may be stored within `app_metadata` or sometimes within `authorization` under `app_metadata`.

``` 
,
  "user_metadata": 
}
```

## How To Code Examples[​](#how-to-code-examples "Direct link to How To Code Examples") 

### Set Roles to Current User[​](#set-roles-to-current-user "Direct link to Set Roles to Current User") 

Roles may be stored within `app_metadata` or sometimes within `authorization` under `app_metadata`.

The `parseJWT` helper will consider both locations to extract roles on the decoded JWT.

api/lib/auth.js

``` 
import  from '@redwoodjs/api'

export const getCurrentUser = async (decoded) => ).roles }
  )
}
```

#### Roles from a Database[​](#roles-from-a-database "Direct link to Roles from a Database") 

If your AuthProvider does not set the role information in the token, you can query roles from a database table.

Consider the following schema where a `User` has many `UserRoles`.

``` 
model User 

model UserRole 
```

You can have seeded the `User` and `UserRole` tables with a new User that has a `uuid` from your identity service and also assigned that user a role of `editor`:

``` 
const uuid = '1683d760-5b4d-2ced-a078-23fdfebe2e19'

const newUser = await db.user.create(,
})

const userRole = await db.userRole.create(,
    },
  },
})
```

Given that your decoded JWT `sub` claim will contain the `uuid`, you can fetch the roles by querying the `UserRoles` table and join in on the `User` via its `uuid`.

Once you have the `UserRole`s, then you can set an array of their `name`s on the `currentUser`.

api/lib/auth.js

``` 
export const getCurrentUser = async (decoded) =>  },
    select: ,
  })

  const roles = userRoles.map((role) => )

  return context.currentUser || 
}
```

### Web-side RBAC[​](#web-side-rbac "Direct link to Web-side RBAC") 

-   useAuth() hook
-   hasRole also checks if authenticated.

```
<!-- -->
```
-   Routes
-   NavLinks in a Layout
-   Cells/Components
-   Markup in Page

#### How to Protect a Route[​](#how-to-protect-a-route "Direct link to How to Protect a Route") 

To protect a `PrivateSet` route for access by a single role:

``` 
import  from '@redwoodjs/router'

const Routes = () =>  name="users" />
      </PrivateSet>
    </Router>
  )
}
```

To protect a `PrivateSet` route for access by a multiple roles:

``` 
import  from '@redwoodjs/router'

const Routes = () => >
        <Route path="/admin/posts//edit" page= name="editPost" />
      </PrivateSet>
    </Router>
  )
}
```

> Note: If you are using `Set` you can use its `private` attribute instead of the `<PrivateSet>` component.

If the currentUser is not assigned the role, they will be redirected to the page specified in the `unauthenticated` property. Therefore, you can define a specific page to be seen when attempting to access the protected route and denied access such as a \"forbidden\" page:

``` 
import  from '@redwoodjs/router'

const Routes = () =>  name="settings" />
        <Route path="/admin" page= name="sites" />
      </PrivateSet>

      <Route notfound page= />
      <Route path="/forbidden" page= name="forbidden" />
    </Router>
  )
}
```

#### How to Protect a NavLink in a Layout[​](#how-to-protect-a-navlink-in-a-layout "Direct link to How to Protect a NavLink in a Layout") 

A `NavLink` is a specialized `Link` used for navigation or menu links that is styled differently when the current route is active.

To protect the `NavLink` for access by a single role:

``` 
import  from '@redwoodjs/router'
import  from '@redwoodjs/auth'

const SidebarLayout = () =>  = useAuth()

  return (
    ...
     className="text-gray-600" activeClassName="text-gray-900"
      >
      Manage Users
    </NavLink>
    ...
   )}
 )
}
```

To protect the `NavLink` for access by multiple roles:

``` 
import  from '@redwoodjs/router'
import  from '@redwoodjs/auth'

const SidebarLayout = () =>  = useAuth()

  return (
    ...
     className="text-gray-600" activeClassName="text-gray-900"
      >
      Manage Posts
    </NavLink>
    ...
   )}
 )
}
```

Note that `hasRole()` also checks if the currentUser is authenticated.

#### How to Protect a Component[​](#how-to-protect-a-component "Direct link to How to Protect a Component") 

To protect content in a `Component` for access by a single role:

``` 
import  from '@redwoodjs/auth'

const Post = () =>  = useAuth()

  return (
    <nav className="rw-button-group">
      >
            Delete
          </a>
        ))}
    </nav>
  )
}
```

To protect content in a `Component` for access by multiple roles:

``` 
import  from '@redwoodjs/auth'

const Post = () =>  = useAuth()

  return (
    <nav className="rw-button-group">
      >
            Delete
          </a>
        ))}
    </nav>
  )
}
```

Note that `hasRole()` also checks if the currentUser is authenticated.

#### How to Protect Markup in a Page[​](#how-to-protect-markup-in-a-page "Direct link to How to Protect Markup in a Page") 

To protect markup in a `Page` for access by a single role:

``` 
import  from "@redwoodjs/auth";
import SidebarLayout from "src/layouts/SidebarLayout";

const SettingsPage = () =>  = useAuth();

  return (
    /identity/$`}
            target="_blank"
            rel="noreferrer"
          >
            Edit on Netlify
          </a>
        )}
      </div>
    )}
  )}
}
```

To protect markup in a `Page` for access by multiple roles:

``` 
import  from "@redwoodjs/auth";
import SidebarLayout from "src/layouts/SidebarLayout";

const SettingsPage = () =>  = useAuth();

  return (
    /identity/$`}
            target="_blank"
            rel="noreferrer"
          >
            Edit on Netlify
          </a>
        )}
      </div>
    )}
  )}
}
```

Note that `hasRole()` also checks if the currentUser is authenticated.

### Api-side RBAC[​](#api-side-rbac "Direct link to Api-side RBAC") 

-   Example `requireAuth()`
-   Services
-   Functions
-   Default Roles using [Netlify Identity Triggers](https://docs.netlify.com/functions/trigger-on-events/)

#### Example `requireAuth()`[​](#example-requireauth "Direct link to example-requireauth") 

Use `requireAuth()` in your services to check that a user is logged in, whether or not they are assigned a role, and optionally raise an error if they\'re not.

It checks for a single role:

``` 
requireAuth()
```

or multiple roles:

``` 
requireAuth()
```

This function should be located in `api/src/lib/auth.js` for your RedwoodJS app (ie, where your `getCurrentUser()` is located).

``` 
export const requireAuth = ( = ) => 

  if (roles && !hasRole(roles)) 
}
```

#### How to Protect a Service[​](#how-to-protect-a-service "Direct link to How to Protect a Service") 

``` 
import  from 'src/lib/db'
import  from 'src/lib/auth'

const CREATE_POST_ROLES = ['admin', 'author', 'publisher']

export const createPost = () => )

  return db.post.create(,
  })
}
```

#### How to Protect a Function[​](#how-to-protect-a-function "Direct link to How to Protect a Function") 

Since `requireAuth()` raises an exception, catch and return a `HTTP 401 Unauthorized` or `HTTP 403 Forbidden` client error status response code.

``` 
import  from 'src/lib/auth'
import  from '@redwoodjs/api'

export const handler = async (event, context) => )

    return ,
      statusCode: 200,
      body: JSON.stringify(),
    }
  } catch (e) 
    } else if (e instanceof ForbiddenError) 
    } else 
    }
  }
}
```

#### How to Default Roles on Signup using Netlify Identity Triggers[​](#how-to-default-roles-on-signup-using-netlify-identity-triggers "Direct link to How to Default Roles on Signup using Netlify Identity Triggers") 

You can trigger serverless function calls when certain Identity events happen, like when a user signs up.

Netlify Identity currently supports the following events:

-   `identity-validate`: Triggered when an Identity user tries to sign up via Identity.
-   `identity-signup`: Triggered when an Identity user signs up via Netlify Identity. (Note: this fires for only email+password signups, not for signups via external providers e.g. Google/GitHub)
-   `identity-login`: Triggered when an Identity user logs in via Netlify Identity

To set a serverless function to trigger on one of these events, match the name of the function file to the name of the event. For example, to trigger a serverless function on identity-signup events, name the function file `identity-signup.js`.

If you return a status other than 200 or 204 from one of these event functions, the signup or login will be blocked.

If your serverless function returns a 200, you can also return a JSON object with new user_metadata or app_metadata for the Identity user.

api/src/functions/identity-signup.js

``` 
export const handler = async (req, _context) => 

    if (email.includes('+editor')) 

    if (email.includes('+publisher')) 

    return ,
      statusCode: 200,
      body: JSON.stringify( }),
    }
  } else 
  }
}
```

#### How to invoke serverless functions while in dev[​](#how-to-invoke-serverless-functions-while-in-dev "Direct link to How to invoke serverless functions while in dev") 

So long as `yarn rw dev` is running, `netlify-cli` can be used to invoke your function. Steps are:

``` 
# Install the cli
yarn add netlify-cli -g

# Rebuild api after any changes to /functions
yarn rw build api

# Invoke your function with the CLI, pointing it to the rw dev port
netlify functions:invoke 8910 < function-name > --port
```

`<function-name>` should be replaced by `identity-validate`, `identity-signup`, `identity-login` or your own function.

Note that the netlify-cli does not generate fake user data for each invocation of an identity function. It always provides the same `Test Person` data.

## Additional Resources[​](#additional-resources "Direct link to Additional Resources") 

-   [RBAC Example & Demo Site](https://redwoodblog-with-identity.netlify.app/)
-   [RBAC Example & Demo Site GitHub Repo](https://github.com/dthyresson/redwoodblog-rbac)
-   [Netlify Identity](https://docs.netlify.com/visitor-access/identity/)
-   [Netlify Identity Triggers](https://docs.netlify.com/functions/trigger-on-events/)
-   [JSON Web Tokens (JWT)](https://jwt.io/)
-   [5 Massive Benefits Of Identity As A Service](https://auth0.com/blog/5-massive-benefits-of-identity-as-a-service-for-developers/)

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6Ij48L3BhdGg+PC9nPjwvc3ZnPg==)Edit the latest version of this page](https://github.com/redwoodjs/graphql/blob/main/docs/docs/how-to/role-based-access-control.md)