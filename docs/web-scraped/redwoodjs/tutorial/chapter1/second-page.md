# Source: https://docs.redwoodjs.com/docs/tutorial/chapter1/second-page

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [Tutorial]
-   [Chapter 1]
-   [A Second Page and a Link]

[Version: 8.8]

On this page

<div>

# A Second Page and a Link

</div>

Let\'s create an \"About\" page for our blog so everyone knows about the geniuses behind this achievement. We\'ll create another page using `redwood`:

``` 
yarn redwood generate page about
```

Notice that we didn\'t specify a route path this time. If you leave it off the `redwood generate page` command, Redwood will create a `Route` and give it a path that is the same as the page name you specified, prepended with a slash. In this case it will be `/about`.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTcgMi4zYzMuMTQgMCA1LjcgMi41NiA1LjcgNS43cy0yLjU2IDUuNy01LjcgNS43QTUuNzEgNS43MSAwIDAgMSAxLjMgOGMwLTMuMTQgMi41Ni01LjcgNS43LTUuN3pNNyAxQzMuMTQgMSAwIDQuMTQgMCA4czMuMTQgNyA3IDcgNy0zLjE0IDctNy0zLjE0LTctNy03em0xIDNINnY1aDJWNHptMCA2SDZ2Mmgydi0yeiI+PC9wYXRoPjwvc3ZnPg==)]Code-splitting each page

As you add more pages to your app, you may start to worry that more and more code has to be downloaded by the client on any initial page load. Fear not! Redwood will automatically code-split on each Page, which means that initial page loads can be blazingly fast, and you can create as many Pages as you want without having to worry about impacting overall bundle size. If, however, you do want specific Pages to be included in the main bundle, you can [override the default behavior](/docs/router#not-code-splitting).

[http://localhost:8910/about](http://localhost:8910/about) should show our new page:

![About page](https://user-images.githubusercontent.com/300/145647906-56b02a6c-b92c-40c6-9d37-860584ffaa6b.png)

But no one\'s going to find it by manually changing the URL so let\'s add a link from our homepage to the About page and vice versa. We\'ll start by creating a simple header and nav bar at the same time on the HomePage:

-   JavaScript
-   TypeScript

web/src/pages/HomePage/HomePage.jsx

``` 
import  from '@redwoodjs/router'
import  from '@redwoodjs/web'

const HomePage = () => >About</Link>
            </li>
          </ul>
        </nav>
      </header>
      <main>Home</main>
    </>
  )
}

export default HomePage
```

web/src/pages/HomePage/HomePage.tsx

``` 
import  from '@redwoodjs/router'
import  from '@redwoodjs/web'

const HomePage = () => >About</Link>
            </li>
          </ul>
        </nav>
      </header>
      <main>Home</main>
    </>
  )
}

export default HomePage
```

Let\'s point out a few things here:

-   Redwood loves [Function Components](https://www.robinwieruch.de/react-function-component). We\'ll make extensive use of [React Hooks](https://react.dev/reference/react) as we go and these are only enabled in function components. Now that Redwood is on React 18, we discourage using class components since they won\'t be able to take advantage of React\'s concurrent rendering features.

-   Redwood\'s `<Link>` tag, in its most basic usage, takes a single `to` attribute. That `to` attribute calls a [*named route function*](/docs/router#link-and-named-route-functions) to generate the correct URL. The function has the same name as the `name` attribute on the `<Route>`:

    `<Route path="/about" page= name="about" />`

    If you don\'t like the name or path that `redwood generate` created for your route, feel free to change it in `Routes.tsx`! Named routes are awesome because if you ever change the path associated with a route (like going from `/about` to `/about-us`), you need only change it in `Routes.tsx` and every link using a named route function (`routes.about()`) will still point to the correct place! You can also pass a string to the `to` prop (`to="/about"`), but now if your path ever changed you would need to find and replace every instance of `/about` to `/about-us`.

### Back Home[​](#back-home "Direct link to Back Home") 

Once we get to the About page we don\'t have any way to get back so let\'s add a link there as well:

-   JavaScript
-   TypeScript

web/src/pages/AboutPage/AboutPage.jsx

``` 
import  from '@redwoodjs/router'
import  from '@redwoodjs/web'

const AboutPage = () => >About</Link>
            </li>
          </ul>
        </nav>
      </header>
      <main>
        <p>
          This site was created to demonstrate my mastery of Redwood: Look on my
          works, ye mighty, and despair!
        </p>
        <Link to=>Return home</Link>
      </main>
    </>
  )
}

export default AboutPage
```

web/src/pages/AboutPage/AboutPage.tsx

``` 
import  from '@redwoodjs/router'
import  from '@redwoodjs/web'

const AboutPage = () => >About</Link>
            </li>
          </ul>
        </nav>
      </header>
      <main>
        <p>
          This site was created to demonstrate my mastery of Redwood: Look on my
          works, ye mighty, and despair!
        </p>
        <Link to=>Return home</Link>
      </main>
    </>
  )
}

export default AboutPage
```

Great! Try that out in the browser and verify that you can get back and forth.

![image](https://user-images.githubusercontent.com/300/145899850-2906c2e3-4ec1-4f8a-9c95-e43b0f7da73f.png)

As a world-class developer you probably saw that copy-and-pasted `<header>` and gasped in disgust. We feel you. That\'s why Redwood has a little something called *Layouts*.

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6Ij48L3BhdGg+PC9nPjwvc3ZnPg==)Edit the latest version of this page](https://github.com/redwoodjs/graphql/blob/main/docs/docs/tutorial/chapter1/second-page.md)