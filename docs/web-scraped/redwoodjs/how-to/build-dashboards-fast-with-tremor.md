# Source: https://docs.redwoodjs.com/docs/how-to/build-dashboards-fast-with-tremor

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [How To](/docs/how-to/index)
-   [Build Dashboards Fast with Tremor]

[Version: 8.8]

On this page

<div>

# Build Dashboards Fast with Tremor

</div>

[Tremor](https://www.tremor.so) is a React library to build dashboards fast. Its modular components are fully open-source, made by data scientists and software engineers with a sweet spot for design.

In this how to, you\'ll learn how to

-   setup tremor in a new or existing RedwoodJS app
-   use tremor components to layout a new dashboard
-   use a chart and card component to visualize static data
-   access a GitHub repo to make your dashboard dynamic using an [example RedwoodJS app](https://github.com/redwoodjs/redwoodjs-tremor-dashboard-demo)

## Live Demo[​](#live-demo "Direct link to Live Demo") 

See what\'s possible with a [dynamic dashboard live demo](https://tremor-redwood-dashboard-demo.netlify.app) build with RedwoodJS and Tremor.

Cool, right?

Let\'s get started!

## Create a New RedwoodJS Project[​](#create-a-new-redwoodjs-project "Direct link to Create a New RedwoodJS Project") 

In our terminal, we create a new RedwoodJS project:

``` 
yarn create redwood-app my-project --ts
```

> **Note:** If you already have a RedwoodJS project, you can skip this step and continue with the next section.

If you do not want a TypeScript project, omit the `--ts` flag.

> **Important:** RedwoodJS prefers yarn over npm because a project is monorepo with api and web workspaces. You will install tremor and other web packages using yarn workspaces.

Use the Redwood setup command to install `TailwindCSS`, its peer dependencies, and create the `tailwind.config.js` file.

``` 
yarn rw setup ui tailwindcss
```

Install `tremor` in the web workspace from your command line via yarn.

``` 
yarn workspace web add @tremor/react
```

Install `heroicons version 1.0.6` from your command line via yarn.

``` 
yarn workspace web add @heroicons/react@1.0.6
```

Update tailwind config `web/config/tailwind.config.js` **including the path to the tremor** module.

``` 
/** @type  */
module.exports = ',
    '../node_modules/@tremor/**/*.',
  ],
  theme: ,
  },
  plugins: [],
}
```

> **Note:** the path for node_modules is `../` because the web workspace is in a subdirectory of the root directory.

## Add a Dashboard Page[​](#add-a-dashboard-page "Direct link to Add a Dashboard Page") 

Generate a page from your command line.

``` 
yarn rw g page dashboard /
```

You will now have a new page at `web/src/pages/DashboardPage/DashboardPage.tsx` and `web/src/Routes.tsx` will have a new route added at:

``` 
// web/src/Routes.tsx`

<Route path="/" page= name="dashboard" />
```

Add simple area chart to the `DashboardPage`:

``` 
import  from '@tremor/react'

import  from '@redwoodjs/web'

const DashboardPage = () => ,
    ,
    ,
    ,
    ,
    ,
  ]

  const dataFormatter = (number: number) => 

  return (
    <div className="m-12">
      <MetaTags title="Dashboard" description="Dashboard page" />

      <h1 className="text-2xl mb-12">Dashboard</h1>

      <Grid numCols= numColsSm= numColsLg= className="my-8 gap-6">
        <Col numColSpan= numColSpanLg=>
          <Card>
            <Title>Newsletter revenue over time (USD)</Title>
            <AreaChart
              className="h-72 mt-4"
              data=
              index="date"
              categories=
              colors=
              valueFormatter=
            />
          </Card>
        </Col>
      </Grid>
    </div>
  )
}

export default DashboardPage
```

Start your RedwoodJS development server

``` 
yarn rw dev
```

Your app will start up and you should see the Dashboard page with an area with two `Newsletter revenue over time (USD)` data series.

## Add a new component for a KPI Card[​](#add-a-new-component-for-a-kpi-card "Direct link to Add a new component for a KPI Card") 

Generate a component for a KPI (Key Performance Indicator) from your command line.

``` 
yarn rw g component KpiCard
```

You will now have a new React component at `/web/src/components/KpiCard/KpiCard.tsx`.

Update the `KpiCard` component to import the `Card` component and assemble a card using its default styling.

To create our first KPI, we import the `Metric` and `Text` component and place them within the card component. We use [Tailwind CSS\'](https://tailwindcss.com/docs/utility-first) utilities in the **className** property to reduce the card\'s width and to center it horizontally.

To make our KPI card more insightful, we add a `ProgressBar`, providing contextual details about our metric. To align both text elements, we also import the `Flex` component.

``` 
// /web/src/components/KpiCard/KpiCard.tsx

import  from '@tremor/react'

export type Kpi = 

interface Props 

const KpiCard = (: Props) => </Text>
          <Metric></Metric>
        </div>
        <BadgeDelta deltaType=></BadgeDelta>
      </Flex>
      <Flex className="mt-4">
        <Text className="truncate">% ($)`}</Text>
        <Text></Text>
      </Flex>
      <ProgressBar percentageValue= className="mt-2" />
    </Card>
  )
}

export default KpiCard
```

## Add the KPI Card component to your Dashboard[​](#add-the-kpi-card-component-to-your-dashboard "Direct link to Add the KPI Card component to your Dashboard") 

Import the `KpiCard` component and `Kpi` type.

``` 
import KpiCard from 'src/components/KpiCard/KpiCard' // 👈 Import the KpiCard component
import type  from 'src/components/KpiCard/KpiCard' // 👈 Import the Kpi type
```

Next, create the `kpi` data collection with sample data

``` 
const kpis: Kpi[] = [
  // 👈 Create some sample KPI data
  ,
  ,
  ,
]
```

Then iterate over the collection to add a `KpiCard` inside new `Col` for each KPI data item:

``` 
 numColSpan=>
      <KpiCard kpi= />
    </Col>
  ))
}
```

Your Dashboard page should now look like:

``` 
import  from '@tremor/react'

import  from '@redwoodjs/web'

import KpiCard from 'src/components/KpiCard/KpiCard' // 👈 Import the KpiCard component
import type  from 'src/components/KpiCard/KpiCard' // 👈 Import the Kpi type

const DashboardPage = () => ,
    ,
    ,
    ,
    ,
    ,
  ]

  const kpis: Kpi[] = [
    // 👈 Create some sample KPI data
    ,
    ,
    ,
  ]

  const dataFormatter = (number: number) => 

  return (
    <div className="m-12">
      <MetaTags title="Dashboard" description="Dashboard page" />

      <h1 className="mb-12 text-2xl">Dashboard</h1>

      <Grid numCols= numColsSm= numColsLg= className="my-8 gap-6">
         numColSpan=>
            <KpiCard kpi= />
          </Col>
        ))}
        <Col numColSpan= numColSpanLg=>
          <Card>
            <Title>Newsletter revenue over time (USD)</Title>
            <AreaChart
              className="mt-4 h-72"
              data=
              index="date"
              categories=
              colors=
              valueFormatter=
            />
          </Card>
        </Col>
      </Grid>
    </div>
  )
}

export default DashboardPage
```

Congratulations! You made your first dashboard.

## Next Steps[​](#next-steps "Direct link to Next Steps") 

Now that you have a Dashboard

1.  Explore the other [components](https://www.tremor.so/components) and [blocks](https://www.tremor.so/blocks) that you can use to showcase your data

2.  Learn how to make a [dynamic dashboard using RedwoodJS cells](https://github.com/redwoodjs/redwoodjs-tremor-dashboard-demo) to fetch data from a Prisma-backed database using GraphQL.

3.  See a [dynamic dashboard live demo](https://tremor-redwood-dashboard-demo.netlify.app)!

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6Ij48L3BhdGg+PC9nPjwvc3ZnPg==)Edit the latest version of this page](https://github.com/redwoodjs/graphql/blob/main/docs/docs/how-to/build-dashboards-fast-with-tremor.md)