# Source: https://docs.redwoodjs.com/docs/accessibility

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [Reference](/docs/index)
-   [Accessibility (aka a11y)]

[Version: 8.8]

On this page

<div>

# Accessibility (aka a11y)

</div>

We built Redwood to make building websites more accessible (we write all the config so you don\'t have to), but Redwood\'s also built to help you make more accessible websites. Accessibility shouldn\'t be a nice-to-have. It should be a given from the start. A core feature that\'s built-in and well-supported.

There\'s a lot of great tooling out there that\'ll not only help you build accessible websites, but also help you learn exactly what that means.

> **Does tooling obviate the need for manual testing?**
>
> No---even with all the tooling in the world, manual testing is still important, especially for accessibility. But just because tooling doesn\'t catch everything doesn\'t mean it\'s not valuable. It\'d be much harder to learn what to look for without it.

## Accessible Routing[​](#accessible-routing "Direct link to Accessible Routing") 

For single-page applications (SPAs), accessibility starts with the router. Without a full-page refresh, you just can\'t be sure that things like announcements and focus are being taken care of the way they\'re supposed to be. Here\'s a great example of [how disorienting SPAs can be to screen-reader users](https://www.youtube.com/watch?v=NKTdNv8JpuM). On navigation, nothing\'s announced. The lack of an announcement isn\'t just buggy behavior---it\'s broken.

Normally, the onus would be on you as a developer to announce to screen-reader users that they\'ve navigated somewhere new. That\'s a lot to ask---and hard to get right---especially when you\'re just trying to build your app.

Luckily, if you\'re writing thoughtful content and marking it up semantically, there\'s nothing you have to do! The router automatically announces pages on navigation, and looks for announcements in this order:

1.  The `RouteAnnouncement` component
2.  The page\'s `<h1>`
3.  `document.title`
4.  `location.pathname`

The reason for this order is that announcements should be as specific as possible. more specific usually means more descriptive, and more descriptive usually means that users can not only orient themselves and navigate through the content, but also find it again.

> If you\'re not sure if your content is descriptive enough, see the [W3 guidelines](https://www.w3.org/WAI/WCAG21/Techniques/general/G88.html).

Even though Redwood looks for a `RouteAnnouncement` component first, you don\'t have to have one on every page---it\'s more than ok for the `<h1>` to be what\'s announced. `RouteAnnouncement` is there for when the situation calls for a custom announcement.

### `RouteAnnouncement`[​](#routeannouncement "Direct link to routeannouncement") 

The way `RouteAnnouncement` works is simple: its children will be announced. Note that this can be something on the page or can be something that\'s visually hidden using the `visuallyHidden` prop:

web/src/pages/HomePage/HomePage.js

``` 
import  from '@redwoodjs/router'

const HomePage = () => 

export default HomePage
```

web/src/pages/AboutPage/AboutPage.js

``` 
import  from '@redwoodjs/router'

const AboutPage = () => 

export default AboutPage
```

`visuallyHidden` shouldn\'t be the first thing you reach for---it\'s good to maintain parity between your site\'s visual and audible experiences. But it\'s there if you need it.

## Focus[​](#focus "Direct link to Focus") 

On page change, Redwood Router resets focus to the top of the DOM so that users can navigate through the new page. While this is the expected behavior (and the behavior you usually want), for some pages---especially those with a lot of navigation---it can be cumbersome for users to have tab through navigation before getting to the main point. (And that goes for every page change!)

Right now, there\'s two ways to alleviate this: with skip links or the `RouteFocus` component.

### Skip Links[​](#skip-links "Direct link to Skip Links") 

Since the main content isn\'t usually the first thing on the page, it\'s a best practice to provide a shortcut for keyboard and screen-reader users to skip to it. Skip links do just that, and if you generate a layout using the `--skipLink` option, you\'ll get one with a skip link:

``` 
yarn rw g layout main --skipLink
```

web/src/layouts/MainLayout/MainLayout.js

``` 
import  from '@redwoodjs/router'
import '@redwoodjs/router/skip-nav.css'

const MainLayout = () => </main>
    </>
  )
}

export default MainLayout
```

`SkipNavLink` renders a link that remains hidden till focused and `SkipNavContent` renders a div as the target for the link. The code for these components comes from Reach UI. For more details, see [Reach UI\'s docs](https://reach.tech/skip-nav/#reach-skip-nav).

One thing you\'ll probably want to do is change the URL the skip link sends the user to when activated. You can do that by changing the `contentId` and `id` props of `SkipNavLink` and `SkipNavContent` respectively:

``` 
<SkipNavLink contentId="main-content" />

<SkipNavContent id="main-content" />
```

If you\'d prefer to implement your own skip link, [Ben Myers\' blog](https://benmyers.dev/blog/skip-links/) is a great resource, and a great place to read about accessibility in general.

### `RouteFocus`[​](#routefocus "Direct link to routefocus") 

Sometimes you don\'t want to just skip the nav, but send a user somewhere. In this situation, you of course have the foresight that that place is where the user wants to be. So please use this at your discretion---sending a user to an unexpected location can be worse than sending them back the top.

Having said that, if you know that on a particular page change a user\'s focus is better off being directed to a particular element, the `RouteFocus` component is what you want:

web/src/pages/ContactPage/ContactPage.js

``` 
import  from '@redwoodjs/router'

const ContactPage = () => (
  <nav>
    
  </nav>

  // The contact form the user actually wants to interact with
  <RouteFocus>
    <TextField name="name" />
  </RouteFocus>
)

export default ContactPage
```

`RouteFocus` tells the router to send focus to it\'s child on page change. In the example above, when the user navigates to the contact page, the name text field on the form is focused---the first field of the form they\'re here to fill out.

# An error occurred. 

Unable to execute JavaScript.

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6Ij48L3BhdGg+PC9nPjwvc3ZnPg==)Edit the latest version of this page](https://github.com/redwoodjs/graphql/blob/main/docs/docs/a11y.md)