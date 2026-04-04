# Source: https://docs.redwoodjs.com/docs/typescript/utility-types

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [Reference](/docs/index)
-   [TypeScript](/docs/typescript/index)
-   [Utility Types]

[Version: 8.8]

On this page

<div>

# Redwood Utility Types

</div>

Besides generating types for you, Redwood exposes a handful of utility types for Cells, Scenarios, and DbAuth. You\'ll see these helpers quite often if you use the generators, so let\'s walk through some of them. By the end of this, you\'ll likely see a pattern in these types and their use of [Generics](https://www.typescriptlang.org/docs/handbook/2/generics.html).

## Cells[​](#cells "Direct link to Cells") 

Cells created using the generators come with all the types your normally need, including the `CellSuccessProps`, `CellFailureProps`, and `CellLoadingProps` utility types.

### `CellSuccessProps<TData, TVariables>`[​](#cellsuccesspropstdata-tvariables "Direct link to cellsuccesspropstdata-tvariables") 

This is used to type the props of your Cell\'s `Success` component. It takes two arguments as generics:

Generic

Description

`TData`

The type of data you\'re expecting to receive (usually the type generated from the query)

`TVariables`

An optional second parameter for the type of the query\'s variables

Not only does `CellSuccessProps` type the data returned from the query, but it also types the variables and methods returned by Apollo Client\'s `useQuery` hook!

web/src/components/BlogPostCell.tsx

``` 
import type  from 'types/graphql'

import type  from '@redwoodjs/web'

// ...

type SuccessProps = CellSuccessProps<
  FindBlogPostQuery,
  FindBlogPostQueryVariables
>

export const Success = (: SuccessProps) => 
```

### `CellFailureProps<TVariables>`[​](#cellfailurepropstvariables "Direct link to cellfailurepropstvariables") 

This gives you the types of the props in your Cell\'s `Failure` component. It takes `TVariables` as an optional generic parameter, which is useful if you want to print error messages like `"Couldn't load data for $"`:

web/src/components/BlogPostCell.tsx

``` 
import type  from 'types/graphql'

import type  from '@redwoodjs/web'

// ...

export const Failure = (: CellFailureProps<FindBlogPostQueryVariables>) => (
  // ...
)
```

### `CellLoadingProps<TVariables>`[​](#cellloadingpropstvariables "Direct link to cellloadingpropstvariables") 

Similar to `CellFailureProps`, but for the props of your Cell\'s `Loading` component:

web/src/components/BlogPostCell.tsx

``` 
import type  from 'types/graphql'

import type  from '@redwoodjs/web'

// ...

export const Loading = (props: CellLoadingProps<FindBlogPostQueryVariables>) => (
  <div>Loading...</div>
)
```

## Scenarios & Testing[​](#scenarios--testing "Direct link to Scenarios & Testing") 

Over on the api side, when you generate SDLs and Services, Redwood generates tests and scenarios with all the types required. Let\'s take a deeper look at scenario types.

### `defineScenario`[​](#definescenario "Direct link to definescenario") 

This is actually a function, not a type, but it takes a lot of generics. Use as many or as few as you find helpful.

``` 
defineScenario<PrismaCreateType, TName, TKey>
```

Generic

Description

`PrismaCreateType`

(Optional) the type imported from Prisma\'s create operation that goes into the \"data\" key

`TName`

(Optional) the name or names of the models in your scenario

`TKeys`

(Optional) the key(s) in your scenario. These are really only useful while you write out the scenario

An example:

posts.scenarios.ts

``` 
import type  from '@prisma/client'

export const standard = defineScenario<Prisma.PostCreateArgs, 'post', 'one'>( },
    },
  },
})
```

If you have more than one model in a single scenario, you can use unions:

``` 
defineScenario<Prisma.PostCreateArgs | Prisma.UserCreateArgs, 'post' | 'user'>
```

### `ScenarioData<TModel, TName, TKeys>`[​](#scenariodatatmodel-tname-tkeys "Direct link to scenariodatatmodel-tname-tkeys") 

This utility type makes it easy for you to access data created by your scenarios in your tests. It takes three generic parameters:

Generic

Description

`TData`

The Prisma model that\'ll be returned

`TName`

(Optional) the name of the model. (\"post\" in the example below)

`TKeys`

(optional) the key(s) used to define the scenario. (\"one\" in the example below)

We know this is a lot of generics, but that\'s so you get to choose how specific you want to be with the types!

api/src/services/posts/posts.scenario.ts

``` 
import type  from '@prisma/client'

//...

export type StandardScenario = ScenarioData<Post, 'post'>
```

api/src/services/posts/posts.test.ts

``` 
import type  from './posts.scenarios'

scenario('returns a single post', async (scenario: StandardScenario) => )
})
```

You can of course just define the type in the test file instead of importing it. Just be aware that if you change your scenario, you need to update the type in the test file too!

## DbAuth[​](#dbauth "Direct link to DbAuth") 

When you setup dbAuth, the generated files in `api/src/lib/auth.ts` and `api/src/functions/auth.ts` have all the types you need. Let\'s break down some of the utility types.

### `DbAuthSession`[​](#dbauthsession "Direct link to dbauthsession") 

You\'ll notice an import at the top of `api/src/lib/auth.ts`:

api/src/lib/auth.ts

``` 
import type  from '@redwoodjs/api'
```

`DbAuthSession` is a utility type that\'s used to type the argument to `getCurrentUser`, `session`:

api/src/lib/auth.ts

``` 
export const getCurrentUser = async (session: DbAuthSession<number>) => ,
    select: ,
  })
}
```

The generic it takes should be the type of your User model\'s `id` field. It\'s usually a `string` or a `number`, but it depends on how you\'ve defined it.

Because a session only ever contains `id`, all we\'re doing here is defining the type of `id`.

### `DbAuthHandlerOptions`[​](#dbauthhandleroptions "Direct link to dbauthhandleroptions") 

`DbAuthHandlerOptions` gives you access to all the types you need to configure your dbAuth handler function in `api/src/function/auth.ts`. It also takes a generic, `TUser`---the type of your User model. Note that this is not the same type as `CurrentUser`.

You can import the type of the User model directly from Prisma and pass it to `DbAuthHandlerOptions`:

``` 
import type  from '@prisma/client'

import type  from '@redwoodjs/api'

export const handler = async (
  event: APIGatewayProxyEvent,
  context: Context
) => ,

      // ...
    }

  // ...
}
```

Note that in strict mode, you\'ll likely see errors where the handlers expect \"truthy\" values. All you have to do is make sure you return a boolean. For example, `return !!user` instead of `return user`.

## Directives[​](#directives "Direct link to Directives") 

### `ValidatorDirectiveFunc`[​](#validatordirectivefunc "Direct link to validatordirectivefunc") 

When you generate a [validator directive](/docs/directives#validators) you will see your `validate` function typed already with `ValidatorDirectiveFunc<TDirectiveArgs>`

``` 
import  from '@redwoodjs/graphql-server'

export const schema = gql`
  directive @myValidator on FIELD_DEFINITION
`
// 👇 makes sure "context" and directive args are typed
const validate: ValidatorDirectiveFunc = () => 
type RequireAuthValidate = ValidatorDirectiveFunc<>

const validate: RequireAuthValidate = () =>  = directiveArgs
  // ....
}
```

Generic

Description

`TDirectiveArgs`

The type of arguments passed to your directive in the SDL

### `TransformerDirectiveFunc`[​](#transformerdirectivefunc "Direct link to transformerdirectivefunc") 

When you generate a [transformer directive](/docs/directives#transformers) you will see your `transform` function typed with `TransformDirectiveFunc<TField, TDirectiveArgs>`.

``` 
// 👇 makes sure the functions' arguments are typed
const transform: TransformerDirectiveFunc = () => 
type MaskedEmailTransform = TransformerDirectiveFunc<
  string,
  
>
```

Generic

Description

`TField`

This will type `resolvedValue` i.e. the type of the field you are transforming

`TDirectiveArgs`

The type of arguments passed to your directive in the SDL

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6Ij48L3BhdGg+PC9nPjwvc3ZnPg==)Edit the latest version of this page](https://github.com/redwoodjs/graphql/blob/main/docs/docs/typescript/utility-types.md)