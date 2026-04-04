# Source: https://docs.redwoodjs.com/docs/typescript/strict-mode

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [Reference](/docs/index)
-   [TypeScript](/docs/typescript/index)
-   [Strict Mode]

[Version: 8.8]

On this page

<div>

# TypeScript Strict Mode

</div>

Looks like you\'re ready to level up your TypeScript game! Redwood supports [strict mode](https://www.typescriptlang.org/docs/handbook/2/basic-types.html#strictness), but doesn\'t enable it by default. While strict mode gives you a lot more safety, it makes your code a bit more verbose and requires you to make small manual changes if you use the generators.

## Enabling strict mode[​](#enabling-strict-mode "Direct link to Enabling strict mode") 

Enable strict mode by setting `strict` to true in `web/tsconfig.json` and `api/tsconfig.json`, and if you\'re using scripts in `scripts/tsconfig.json`:

web/tsconfig.json, api/tsconfig.json, scripts/tsconfig.json

``` 

  // ...
}
```

Redwood\'s type generator behaves a bit differently in strict mode, so now that you\'ve opted in, make sure to generate types:

``` 
yarn rw g types
```

## Manual tweaks to generated code[​](#manual-tweaks-to-generated-code "Direct link to Manual tweaks to generated code") 

Now that you\'re in strict mode, there are some changes you need to make to get rid of those pesky red underlines!

### `null` and `undefined` in Services[​](#null-and-undefined-in-services "Direct link to null-and-undefined-in-services") 

One of the challenges in the GraphQL-Prisma world is the difference in the way they treats optionals:

-   for GraphQL, optional fields can be `null`
-   but For Prisma, `null` is a value, and `undefined` means \"do nothing\"

This is covered in detail in [Prisma\'s docs](https://www.prisma.io/docs/concepts/components/prisma-client/null-and-undefined), which we strongly recommend reading. But the gist of it is that, for Prisma\'s create and update operations, you may have to make sure `null`s are converted to `undefined` from your GraphQL mutation inputs. You\'ll have to think carefully about the behaviour you want - if the client is expected to send null, and you expect those fields to be set to null, you can make the field nullable in your Prisma schema. Sending a null will mean removing that value, sending undefined will mean that the field won\'t be updated.

For most cases however, you probably want to convert nulls to undefined - one way to do this is to use the `removeNulls` utility function from `@redwoodjs/api`:

api/src/services/users.ts

``` 
import  from '@redwoodjs/api'

export const updateUser: MutationResolvers['updateUser'] = () => ,
  })
}
```

### Relation resolvers in services[​](#relation-resolvers-in-services "Direct link to Relation resolvers in services") 

Let\'s say you have a `Post` model in your `schema.prisma` that has an `author` field which is a relation to the `Author` model. It\'s a required field. This is what the `Post` model\'s SDL would probably look like:

``` 
export const schema = gql`
  type Post 
```

When you generate SDLs or Services, the resolver for `author` is generated at the bottom of `post.service.ts` on the `Post` object. Because `Post.author` can\'t be null (we said it\'s required in the Prisma schema)---and because `findUnique` always returns a nullable value---in strict mode, you\'ll have to tweak this resolver:

``` 
// Option 1: Override the type
// The typecasting here is OK. `root` is the post that was _already found_
// by the `post` function in your Services, so `findUnique` will always find it!
export const Post: PostRelationResolvers = ) =>
    db.post.findUnique( }).author() as Promise<Author>, // 👈
}

// Option 2: Check for null
export const Post: PostRelationResolvers = ) =>  })
      .author()

    if (!maybeAuthor) 

    return maybeAuthor
  },
}
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTIgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuNSAwQzMuNDggMCAxIDIuMTkgMSA1YzAgLjkyLjU1IDIuMjUgMSAzIDEuMzQgMi4yNSAxLjc4IDIuNzggMiA0djFoNXYtMWMuMjItMS4yMi42Ni0xLjc1IDItNCAuNDUtLjc1IDEtMi4wOCAxLTMgMC0yLjgxLTIuNDgtNS01LjUtNXptMy42NCA3LjQ4Yy0uMjUuNDQtLjQ3LjgtLjY3IDEuMTEtLjg2IDEuNDEtMS4yNSAyLjA2LTEuNDUgMy4yMy0uMDIuMDUtLjAyLjExLS4wMi4xN0g1YzAtLjA2IDAtLjEzLS4wMi0uMTctLjItMS4xNy0uNTktMS44My0xLjQ1LTMuMjMtLjItLjMxLS40Mi0uNjctLjY3LTEuMTFDMi40NCA2Ljc4IDIgNS42NSAyIDVjMC0yLjIgMi4wMi00IDQuNS00IDEuMjIgMCAyLjM2LjQyIDMuMjIgMS4xOUMxMC41NSAyLjk0IDExIDMuOTQgMTEgNWMwIC42Ni0uNDQgMS43OC0uODYgMi40OHpNNCAxNGg1Yy0uMjMgMS4xNC0xLjMgMi0yLjUgMnMtMi4yNy0uODYtMi41LTJ6Ij48L3BhdGg+PC9zdmc+)]An optimization tip

If the relation truly is required, it may make more sense to include `author` in your `post` Service\'s Prisma query and modify the `Post.author` resolver accordingly:

``` 
export const post: QueryResolvers['post'] = () => ,
    where: ,
  })
}

export const Post: PostRelationResolvers = ) => 

  const maybeAuthor = await db.post.findUnique(// ...
```

This will also help Prisma make a more optimized query to the database, since every time a field on `Post` is requested, the post\'s author is too! The tradeoff here is that any query to `Post` (even if the author isn\'t requested) will mean an unnecessary database query to include the author.

### Roles checks for CurrentUser in `src/lib/auth`[​](#roles-checks-for-currentuser-in-srclibauth "Direct link to roles-checks-for-currentuser-in-srclibauth") 

When you setup auth, Redwood includes some template code for handling roles with the `hasRole` function. While Redwood does runtime checks to make sure it doesn\'t access roles if it doesn\'t exist, TypeScript in strict mode will highlight errors, depending on whether you are returning `roles`, and whether those roles are `string` or `string[]`

``` 
export const hasRole = (roles: AllowedRoles): boolean => 

  const currentUserRoles = context.currentUser?.roles
  // Error: Property 'roles' does not exist on type ''.ts(2339)
```

You\'ll have to adjust the generated code depending on your User model.

Example code diffs

<div>

#### A. If your project does not use roles[​](#a-if-your-project-does-not-use-roles "Direct link to A. If your project does not use roles") 

If your `getCurrentUser` doesn\'t return `roles`, and you don\'t use this functionality, you can safely remove the `hasRole` function.

#### B. Roles on current user is a string[​](#b-roles-on-current-user-is-a-string "Direct link to B. Roles on current user is a string") 

Alternatively, if you define the roles as a string, you can remove the code that does checks against Arrays

api/src/lib/auth.ts

``` 
export const hasRole = (roles: AllowedRoles): boolean => 

  const currentUserRoles = context.currentUser?.roles

  if (typeof roles === 'string') 
  }

  if (Array.isArray(roles))  else if (typeof currentUserRoles === 'string') 
  }

  // roles not found
  return false
}
```

#### C. Roles on current user is an Array of strings[​](#c-roles-on-current-user-is-an-array-of-strings "Direct link to C. Roles on current user is an Array of strings") 

If in your User model, roles are an array of strings, and can never be just a string, you can safely remove most of the code

api/src/lib/auth.ts

``` 
export const hasRole = (roles: AllowedRoles): boolean => 

 const currentUserRoles = context.currentUser?.roles

  if (typeof roles === 'string')  else if (Array.isArray(currentUserRoles)) 
  }

  if (Array.isArray(roles))  else if (typeof currentUserRoles === 'string') 
  }

  // roles not found
  return false
}
```

</div>

### `getCurrentUser` in `api/src/lib/auth.ts`[​](#getcurrentuser-in-apisrclibauthts "Direct link to getcurrentuser-in-apisrclibauthts") 

Depending on your auth provider---i.e., anything but dbAuth---because it could change based on your account settings (if you include roles or other metadata), we can\'t know the shape of your decoded token at setup time. So you\'ll have to make sure that the `getCurrentUser` function is typed.

To help you get started, the comments above the `getCurrentUser` function describe its parameters\' types. We recommend typing `decoded` without using imported types from Redwood, as this may be a little too generic!

api/src/lib/auth.ts

``` 
import type  from '@redwoodjs/api'

// Example 1: typing directly
export const getCurrentUser: CurrentUserFunc = async (
  decoded: ,
  : 
) => 

// Example 2: Using AuthContextPayload
export const getCurrentUser: CurrentUserFunc = async (
  decoded: ,
  : AuthContextPayload[1],
  : AuthContextPayload[2]
) => 
```

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6Ij48L3BhdGg+PC9nPjwvc3ZnPg==)Edit the latest version of this page](https://github.com/redwoodjs/graphql/blob/main/docs/docs/typescript/strict-mode.md)