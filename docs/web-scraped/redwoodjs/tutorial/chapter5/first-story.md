# Source: https://docs.redwoodjs.com/docs/tutorial/chapter5/first-story

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [Tutorial]
-   [Chapter 5]
-   [Our First Story]

[Version: 8.8]

On this page

<div>

# Our First Story

</div>

Let\'s say that on our homepage we only want to show the first couple of sentences in our blog post as a short summary, and then you\'ll have to click through to see the full post.

First let\'s update the `Article` component to contain that functionality:

-   JavaScript
-   TypeScript

web/src/components/Article/Article.jsx

``` 
import  from '@redwoodjs/router'

const truncate = (text, length) => 

const Article = () => )}></Link>
        </h2>
      </header>
      <div className="mt-2 text-gray-900 font-light">
        
      </div>
    </article>
  )
}

export default Article
```

web/src/components/Article/Article.tsx

``` 
import  from '@redwoodjs/router'

import type  from 'types/graphql'

const truncate = (text: string, length: number) => 

interface Props 

const Article = (: Props) => )}></Link>
        </h2>
      </header>
      <div className="mt-2 text-gray-900 font-light">
        
      </div>
    </article>
  )
}

export default Article
```

We\'ll pass an additional `summary` prop to the component to let it know if it should show just the summary or the whole thing. We default it to `false` to preserve the existing behavior---always showing the full body.

Now in the Storybook story let\'s create a `summary` story that uses the `Article` component the same way that `generated` does, but adds the new `summary` prop. We\'ll take the content of the sample post and put that in a constant that both stories will use. We\'ll also rename `generated` to `full` to make it clear what\'s different between the two:

-   JavaScript
-   TypeScript

web/components/Article/Article.stories.jsx

``` 
import Article from './Article'

const ARTICLE = 

export const full = () =>  />
}

export const summary = () =>  summary= />
}

export default 
```

web/components/Article/Article.stories.tsx

``` 
import Article from './Article'

const ARTICLE = 

export const full = () =>  />
}

export const summary = () =>  summary= />
}

export default 
```

As soon as you save the change the stories Storybook should refresh and may show an error: there\'s no longer a \"Generated\" story to show! In the tree on the left, expand \"Article\" and the \"Full\" version should show right away. Click on \"Summary\" to see the difference:

![image](https://user-images.githubusercontent.com/300/153311838-595b8b38-d899-4d7b-891b-a492f0c8f2e2.png)

### Displaying the Summary[​](#displaying-the-summary "Direct link to Displaying the Summary") 

Great! Now to complete the picture let\'s use the summary in our home page display of blog posts. The actual Home page isn\'t what references the `Article` component though, that\'s in the `ArticlesCell`. We\'ll add the `summary` prop and then check the result in Storybook:

-   JavaScript
-   TypeScript

web/src/components/ArticlesCell/ArticlesCell.jsx

``` 
import Article from 'src/components/Article'

export const QUERY = gql`
  query ArticlesQuery 
  }
`

export const Loading = () => <div>Loading...</div>

export const Empty = () => <div>Empty</div>

export const Failure = () => <div>Error: </div>

export const Success = () =>  key= summary= />
      ))}
    </div>
  )
}
```

web/src/components/ArticlesCell/ArticlesCell.tsx

``` 
import type  from 'types/graphql'

import type  from '@redwoodjs/web'

import Article from 'src/components/Article'

export const QUERY: TypeDocumentNode<ArticlesQuery, ArticlesQueryVariables> =
  gql`
    query ArticlesQuery 
    }
  `

export const Loading = () => <div>Loading...</div>

export const Empty = () => <div>Empty</div>

export const Failure = (: CellFailureProps<ArticlesQueryVariables>) => (
  <div>Error: </div>
)

export const Success = (: CellSuccessProps<ArticlesQuery, ArticlesQueryVariables>) =>  key= summary= />
      ))}
    </div>
  )
}
```

Check out the story to see the new summary view:

![image](https://user-images.githubusercontent.com/300/153312022-1cfbf696-b2cb-4fca-b640-4111643fb396.png)

And if you head to the real site you\'ll see the summary there as well:

![image](https://user-images.githubusercontent.com/300/101545160-b2d45880-395b-11eb-9a32-f8cb8106de7f.png)

We can double check that our original usage of `Article` (the one without the `summary` prop) in `ArticleCell` still renders the entire post, not just the truncated version:

![image](https://user-images.githubusercontent.com/300/153312180-2a80df75-ea95-4e7b-9eb5-45fa900333e9.png)

Storybook makes it easy to create and modify your components in isolation and actually helps enforce a general best practice when building React applications: components should be self-contained and reusable by just changing the props that are sent in.

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6Ij48L3BhdGg+PC9nPjwvc3ZnPg==)Edit the latest version of this page](https://github.com/redwoodjs/graphql/blob/main/docs/docs/tutorial/chapter5/first-story.md)