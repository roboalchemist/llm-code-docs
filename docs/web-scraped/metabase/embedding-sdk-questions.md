# Source: https://www.metabase.com/docs/latest/embedding/sdk/questions

<div>

1.  [Home](/docs/latest/)
2.  [Embedding](/docs/latest/embedding/start)

</div>

<div>

[ v0.57 ![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzIiIGhlaWdodD0iMzIiIHZpZXdib3g9IjAgMCAzMiAzMiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBjbGFzcz0iY2hldnJvbiI+CjxwYXRoIG9wYWNpdHk9IjAuOSIgZD0iTTMgOC45NjMzOEwxNiAyMS45NjM0TDI5IDguOTYzMzgiIHN0cm9rZT0iIzUwOWVlMyIgc3Ryb2tlLXdpZHRoPSI1IiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiPjwvcGF0aD4KPC9zdmc+) ]

-   [v0.56](/docs/v0.56)
-   [v0.55](/docs/v0.55)
-   [v0.54](/docs/v0.54)
-   [v0.53](/docs/v0.53)
-   [v0.52](/docs/v0.52)
-   [v0.51](/docs/v0.51)
-   [v0.50](/docs/v0.50)
-   [v0.49](/docs/v0.49)
-   [v0.48](/docs/v0.48)
-   [See more](/docs/all)

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgdmlld2JveD0iMCAwIDI0IDI0IiBmaWxsPSJub25lIj48cGF0aCBzdHJva2U9IiM1MDlFRTMiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIxLjUiIGQ9Ik0xNi4yODMgMTIuMjYgMTUuNSAxNWwtLjc4My0yLjc0YTQuMzMzIDQuMzMzIDAgMCAwLTIuOTc1LTIuOTc2TDkgOC41bDIuNzQtLjc4M2E0LjMzMyA0LjMzMyAwIDAgMCAyLjk3Ni0yLjk3NUwxNS41IDJsLjc4MyAyLjc0YTQuMzMzIDQuMzMzIDAgMCAwIDIuOTc1IDIuOTc2TDIyIDguNWwtMi43NC43ODNhNC4zMzQgNC4zMzQgMCAwIDAtMi45NzYgMi45NzVsLS4wMDEuMDAxWk02LjUgMjJsLjU5MS0xLjc3NGEzLjM3NSAzLjM3NSAwIDAgMSAyLjEzNS0yLjEzNUwxMSAxNy41bC0xLjc3NC0uNTkxYTMuMzc1IDMuMzc1IDAgMCAxLTIuMTM1LTIuMTM0TDYuNSAxM2wtLjU5MSAxLjc3NGEzLjM3NSAzLjM3NSAwIDAgMS0yLjEzNCAyLjEzNUwyIDE3LjVsMS43NzUuNTkxYTMuMzc1IDMuMzc1IDAgMCAxIDIuMTM0IDIuMTM0TDYuNSAyMloiPjwvcGF0aD48L3N2Zz4=) What's new](/releases)

</div>

<div>

</div>

# Embedded analytics SDK - questions

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcyB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHZpZXdib3g9IjAgMCAyNiAyNiIgZmlsbD0ibm9uZSI+CiAgPHBhdGggZD0iTTEyIDEzVjE1IiBzdHJva2Utd2lkdGg9IjIiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgc3Ryb2tlPSIjNTA5RUUzIj48L3BhdGg+CiAgPHBhdGggZD0iTTEyIDEwQzEyLjU1MjMgMTAgMTMgOS41NTIyOCAxMyA5QzEzIDguNDQ3NzIgMTIuNTUyMyA4IDEyIDhDMTEuNDQ3NyA4IDExIDguNDQ3NzIgMTEgOUMxMSA5LjU1MjI4IDExLjQ0NzcgMTAgMTIgMTBaIiBmaWxsPSIjNTA5RUUzIj48L3BhdGg+CiAgPHBhdGggZD0iTTEyIDE5LjI1QzE2LjAwNDEgMTkuMjUgMTkuMjUgMTYuMDA0MSAxOS4yNSAxMkMxOS4yNSA3Ljk5NTk0IDE2LjAwNDEgNC43NSAxMiA0Ljc1QzcuOTk1OTQgNC43NSA0Ljc1IDcuOTk1OTQgNC43NSAxMkM0Ljc1IDE2LjAwNDEgNy45OTU5NCAxOS4yNSAxMiAxOS4yNVoiIHN0cm9rZS13aWR0aD0iMS41IiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIHN0cm9rZT0iIzUwOUVFMyI+PC9wYXRoPgo8L3N2Zz4=)

Embedded analytics SDK is only available on [Pro](/product/pro) and [Enterprise](/product/enterprise) plans (both self-hosted and on Metabase Cloud).

There are different ways you can embed questions:

-   [Static question](#staticquestion). Embeds a chart. Clicking on the chart doesn't do anything.
-   [Interactive question](#interactivequestion). Clicking on the chart gives you the drill-through menu.
-   [Query builder](#embedding-the-query-builder-for-creating-new-questions). Embeds the graphical query builder without a pre-defined query.

## Embedding a question

You can embed a question using the one of the question components:

### `StaticQuestion`

A lightweight question component. Use this component when you want to display results without letting people interact with the data.

![Static question](../images/static-question.png)

The component has a default height, which can be customized by using the `height` prop. To inherit the height from the parent container, you can pass `100%` to the height prop.

#### API Reference

-   [Component](./api/StaticQuestion)
-   [Props](./api/StaticQuestionProps)

#### Example

``` highlight
import React from "react";
import  from "@metabase/embedding-sdk-react";

const authConfig = defineMetabaseAuthConfig();

export default function App() >
      <StaticQuestion questionId= withChartTypeSelector= />
    </MetabaseProvider>
  );
}
```

#### Props

  Property                                                                                      Type                                                                                                                                                                                       Description
  --------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [] `className?`                           `string`                                                                                                                                           A custom class name to be added to the root element.
  [] `height?`                                 `Height`\<`string` \| `number`\>                                   A number or string specifying a CSS size value that specifies the height of the component
  [] `hiddenParameters?`             `string`\[\]                                                                                                                                       A list of parameters to hide.
  [] `initialSqlParameters?`     [`SqlParameterValues`](./api/SqlParameterValues)                                                                                                   Initial values for the SQL parameters.
  [] `questionId`                          `null` \| [`SdkQuestionId`](./api/SdkQuestionId)                                                           \-
  [] `style?`                                   [`CSSProperties`](https://github.com/DefinitelyTyped/DefinitelyTyped/blob/0b728411cd1dfb4bd26992bb35a73cf8edaa22e7/types/react/index.d.ts#L2579)   A custom style object to be added to the root element.
  [] `title?`                                   [`SdkQuestionTitleProps`](./api/SdkQuestionTitleProps)                                                                                             Determines whether the question title is displayed, and allows a custom title to be displayed instead of the default question title. Shown by default. Only applicable to interactive questions when using the default layout.
  [] `width?`                                   `Width`\<`string` \| `number`\>                                    A number or string specifying a CSS size value that specifies the width of the component
  [] `withChartTypeSelector?`   `boolean`                                                                                                                                          Determines whether the chart type selector and corresponding settings button are shown. Only relevant when using the default layout.
  [] `withDownloads?`                   `boolean`                                                                                                                                          Enables the ability to download results in the interactive question.

### `InteractiveQuestion`

Use this component when you want to allow people to explore their data and customize question layout.

![Interactive question](../images/interactive-question.png)

#### API Reference

-   [Component](./api/InteractiveQuestion)
-   [Props](./api/InteractiveQuestionProps)

#### Example

``` highlight
import React from "react";
import  from "@metabase/embedding-sdk-react";

const authConfig = defineMetabaseAuthConfig();

export default function App() >
      <InteractiveQuestion questionId= />
    </MetabaseProvider>
  );
}
```

#### Props

  Property                                                                                      Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             Description
  --------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [] `className?`                           `string`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 A custom class name to be added to the root element.
  [] `entityTypes?`                       [`EmbeddingEntityType`](./api/EmbeddingEntityType)\[\]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   An array that specifies which entity types are available in the data picker
  [] `height?`                                 `Height`\<`string` \| `number`\>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         A number or string specifying a CSS size value that specifies the height of the component
  [] `hiddenParameters?`             `string`\[\]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             A list of parameters to hide.
  [] `initialSqlParameters?`     [`SqlParameterValues`](./api/SqlParameterValues)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         Initial values for the SQL parameters.
  [] `isSaveEnabled?`                   `boolean`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                Whether to show the save button.
  [] `onBeforeSave?`                     (`question`: `undefined` \| [`MetabaseQuestion`](./api/MetabaseQuestion), `context`: : `boolean`; }) =\> [`Promise`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Promise)\<`void`\>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              A callback function that triggers before saving. Only relevant when `isSaveEnabled = true`
  [] `onNavigateBack?`                 () =\> `void`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            A callback function that triggers when a user clicks the back button.
  [] `onRun?`                                   (`question`: `undefined` \| [`MetabaseQuestion`](./api/MetabaseQuestion)) =\> `void`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             A callback function that triggers when a question is updated, including when a user clicks the `Visualize` button in the question editor
  [] `onSave?`                                 (`question`: [`MetabaseQuestion`](./api/MetabaseQuestion), `context`: : `number`; `isNewQuestion`: `boolean`; }) =\> `void`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   A callback function that triggers when a user saves the question. Only relevant when `isSaveEnabled = true`
  [] `onVisualizationChange?`   (`display`: \| `"object"` \| `"table"` \| `"bar"` \| `"line"` \| `"pie"` \| `"scalar"` \| `"row"` \| `"area"` \| `"combo"` \| `"pivot"` \| `"smartscalar"` \| `"gauge"` \| `"progress"` \| `"funnel"` \| `"map"` \| `"scatter"` \| `"waterfall"` \| `"sankey"` \| `"list"`) =\> `void`   A callback function that triggers when the visualization type changes.
  [] `plugins?`                               [`MetabasePluginsConfig`](./api/MetabasePluginsConfig)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   \-
  [] `questionId`                          `null` \| [`SdkQuestionId`](./api/SdkQuestionId)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 \-
  [] `style?`                                   [`CSSProperties`](https://github.com/DefinitelyTyped/DefinitelyTyped/blob/0b728411cd1dfb4bd26992bb35a73cf8edaa22e7/types/react/index.d.ts#L2579)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         A custom style object to be added to the root element.
  [] `targetCollection?`             [`SdkCollectionId`](./api/SdkCollectionId)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               The collection to save the question to. This will hide the collection picker from the save modal. Only applicable to interactive questions.
  [] `title?`                                   [`SdkQuestionTitleProps`](./api/SdkQuestionTitleProps)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   Determines whether the question title is displayed, and allows a custom title to be displayed instead of the default question title. Shown by default. Only applicable to interactive questions when using the default layout.
  [] `width?`                                   `Width`\<`string` \| `number`\>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          A number or string specifying a CSS size value that specifies the width of the component
  [] `withChartTypeSelector?`   `boolean`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                Determines whether the chart type selector and corresponding settings button are shown. Only relevant when using the default layout.
  [] `withDownloads?`                   `boolean`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                Enables the ability to download results in the interactive question.
  [] `withResetButton?`               `boolean`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                Determines whether a reset button is displayed. Only relevant when using the default layout.

## Pass SQL parameters to SQL questions with `initialSqlParameters`

You can pass parameter values to questions defined with SQL via the `initialSqlParameters` prop, in the format of ``. Learn more about [SQL parameters](../../questions/native-editor/sql-parameters).

``` highlight
<StaticQuestion
  questionId=
  initialSqlParameters=}
/>
```

`initialSqlParameters` can't be used with questions built using the query builder.

## Questions with natural language

See [AI chat](./ai-chat).

## Customizing interactive questions

By default, the Embedded analytics SDK provides a default layout for interactive questions that allows you to view your questions, apply filters and aggregations, and access functionality within the query builder.

Here's an example of using the `InteractiveQuestion` component with its default layout:

``` highlight
<InteractiveQuestion questionId= />
```

To customize the layout, use namespaced components within the `InteractiveQuestion` component. For example:

``` highlight
<div
  className="App"
  style=}
>
  <MetabaseProvider authConfig= theme=>
    <InteractiveQuestion questionId=>
      <div
        style=}
      >
        <div style=}>
          <InteractiveQuestion.Title />
          <InteractiveQuestion.ResetButton />
        </div>
        <div
          style=}
        >
          <div style=}>
            <InteractiveQuestion.QuestionVisualization />
          </div>
          <div style=}>
            <InteractiveQuestion.Summarize />
          </div>
        </div>
        <div
          style=}
        >
          <InteractiveQuestion.Filter />
        </div>
      </div>
    </InteractiveQuestion>
  </MetabaseProvider>
</div>
```

### Interactive question components

These components are available via the `InteractiveQuestion` namespace (e.g., `<InteractiveQuestion.Filter />`).

#### API Reference:

-   [InteractiveQuestion.BackButton](./api/InteractiveQuestion#backbutton)
-   [InteractiveQuestion.Breakout](./api/InteractiveQuestion#breakout)
-   [InteractiveQuestion.BreakoutDropdown](./api/InteractiveQuestion#breakoutdropdown)
-   [InteractiveQuestion.ChartTypeDropdown](./api/InteractiveQuestion#charttypedropdown)
-   [InteractiveQuestion.ChartTypeSelector](./api/InteractiveQuestion#charttypeselector)
-   [InteractiveQuestion.Editor](./api/InteractiveQuestion#editor)
-   [InteractiveQuestion.EditorButton](./api/InteractiveQuestion#editorbutton)
-   [InteractiveQuestion.Filter](./api/InteractiveQuestion#filter)
-   [InteractiveQuestion.FilterDropdown](./api/InteractiveQuestion#filterdropdown)
-   [InteractiveQuestion.QuestionSettings](./api/InteractiveQuestion#questionsettings)
-   [InteractiveQuestion.QuestionSettingsDropdown](./api/InteractiveQuestion#questionsettingsdropdown)
-   [InteractiveQuestion.QuestionVisualization](./api/InteractiveQuestion#questionvisualization)
-   [InteractiveQuestion.ResetButton](./api/InteractiveQuestion#resetbutton)
-   [InteractiveQuestion.SaveButton](./api/InteractiveQuestion#savebutton)
-   [InteractiveQuestion.SaveQuestionForm](./api/InteractiveQuestion#savequestionform)
-   [InteractiveQuestion.Summarize](./api/InteractiveQuestion#summarize)
-   [InteractiveQuestion.SummarizeDropdown](./api/InteractiveQuestion#summarizedropdown)
-   [InteractiveQuestion.DownloadWidget](./api/InteractiveQuestion#downloadwidget)
-   [InteractiveQuestion.DownloadWidgetDropdown](./api/InteractiveQuestion#downloadwidgetdropdown)
-   [InteractiveQuestion.Title](./api/InteractiveQuestion#title)

## Interactive question plugins

You can use [plugins](./plugins) to add custom functionality to your questions.

### `mapQuestionClickActions`

When people click on a data point in the embedded interactive chart, Metabase shows them a menu of actions by default. The plugin `mapQuestionClickActions` allows you to customize this behavior. You can choose to:

-   Open the default Metabase menu.
-   Add custom actions to that click-through menu.
-   Perform immediate action without opening a menu.

Use `mapQuestionClickActions` globally at the provider level, or on individual `InteractiveQuestion` or `InteractiveDashboard` components. For more on provider scope, see [Plugins](./plugins)

The example below shows all the options for click action behavior. This example will:

-   Open a menu with custom actions when "Last Name" column is clicked.
-   Perform an immediate action (show an alert) when the "Plan" column is clicked.
-   Shows the default menu (available as `clickActions`) in all other cases.

The behavior is determined by what `mapQuestionClickActions` returns: array of actions to open a menu, or a single action to trigger an immediate action.

``` highlight
  <MetabaseProvider
    authConfig=
    pluginsConfig=,
          ];
        }

        if (clicked?.column?.display_name === "Plan") ;
        }
        // default behavior (open Metabase's default click menu) on other columns
        return clickActions;
      },
    }}
  >
    <InteractiveQuestion questionId= />
  </MetabaseProvider>
);
```

You can also customize the appearance of custom actions in the click menu. The example below shows an example of a click menu with default actions, a custom action, and a custom action with customized appearance:

``` highlight
// You can provide a custom action with your own `onClick` logic.
const createCustomAction = clicked => () => : $`);
    closePopover();
  },
});

// Or customize the appearance of the custom action to suit your need.
const createCustomActionWithView = clicked => () => (
    <button
      className="tw-text-base tw-text-yellow-900 tw-bg-slate-400 tw-rounded-lg"
      onClick=: $`);
        closePopover();
      }}
    >
      Custom element
    </button>
  ),
});

const plugins = ,
};

const questionId = 1; // This is the question ID you want to embed

return (
  <MetabaseProvider authConfig= pluginsConfig=>
    <InteractiveQuestion questionId= />
  </MetabaseProvider>
);
```

## Prevent people from saving changes to an `InteractiveQuestion`

To prevent people from saving changes to an interactive question, or from saving changes as a new question, you can set `isSaveEnabled=`:

``` highlight
import React from "react";
import  from "@metabase/embedding-sdk-react";

const authConfig = defineMetabaseAuthConfig();

export default function App() >
      <InteractiveQuestion questionId= isSaveEnabled= />
    </MetabaseProvider>
  );
}
```

## Embedding the query builder for creating new questions

![Query builder](../images/query-builder.png)

You can embed the query builder for creating new questions by passing the `questionId="new"` prop to the `InteractiveQuestion` component. You can use the [`children` prop](#customizing-interactive-questions) to customize the layout for creating new questions.

``` highlight
import React from "react";
import  from "@metabase/embedding-sdk-react";

const authConfig = defineMetabaseAuthConfig();

export default function App() >
      <InteractiveQuestion questionId="new" />
    </MetabaseProvider>
  );
}
```

To customize the question editor's layout, use the `InteractiveQuestion` component [directly with a custom `children` prop](#customizing-interactive-questions).

<div>

Read docs for other [versions of Metabase](/docs/all).

</div>

###### Was this helpful?

![](data:image/svg+xml;base64,PHN2ZyBpZCBjbGFzcz0ibWUtMSIgd2lkdGg9IjE4IiBoZWlnaHQ9IjE4IiB2aWV3Ym94PSIwIDAgMjQgMjQiIGZpbGw9Im5vbmUiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CiAgICA8cGF0aCBkPSJNMTAuNjY2NyA3LjMzMzMzSDE0LjYzNjdDMTQuOTIwNyA3LjMzMzM0IDE1LjIwMDEgNy40MDU5NSAxNS40NDgyIDcuNTQ0MjdDMTUuNjk2MyA3LjY4MjU5IDE1LjkwNDkgNy44ODIwMiAxNi4wNTQzIDguMTIzNjRDMTYuMjAzNiA4LjM2NTI1IDE2LjI4ODggOC42NDEwNCAxNi4zMDE2IDguOTI0OEMxNi4zMTQ0IDkuMjA4NTcgMTYuMjU0NSA5LjQ5MDkgMTYuMTI3NSA5Ljc0NUwxMy4yMTA4IDE1LjU3ODNDMTMuMDcyNCAxNS44NTU0IDEyLjg1OTUgMTYuMDg4NCAxMi41OTYgMTYuMjUxMkMxMi4zMzI1IDE2LjQxNCAxMi4wMjg5IDE2LjUwMDEgMTEuNzE5MiAxNi41SDguMzcxNjdDOC4yMzU4MyAxNi41IDguMSAxNi40ODMzIDcuOTY3NSAxNi40NUw0LjgzMzMzIDE1LjY2NjdNMTAuNjY2NyA3LjMzMzMzVjMuMTY2NjdDMTAuNjY2NyAyLjcyNDY0IDEwLjQ5MTEgMi4zMDA3MiAxMC4xNzg1IDEuOTg4MTZDOS44NjU5NSAxLjY3NTU5IDkuNDQyMDMgMS41IDkgMS41SDguOTIwODNDOC41MDQxNyAxLjUgOC4xNjY2NyAxLjgzNzUgOC4xNjY2NyAyLjI1NDE3QzguMTY2NjcgMi44NDkxNyA3Ljk5MDgzIDMuNDMwODMgNy42NiAzLjkyNTgzTDQuODMzMzMgOC4xNjY2N1YxNS42NjY3TTEwLjY2NjcgNy4zMzMzM0g5TTQuODMzMzMgMTUuNjY2N0gzLjE2NjY3QzIuNzI0NjQgMTUuNjY2NyAyLjMwMDcyIDE1LjQ5MTEgMS45ODgxNiAxNS4xNzg1QzEuNjc1NTkgMTQuODY2IDEuNSAxNC40NDIgMS41IDE0VjlDMS41IDguNTU3OTcgMS42NzU1OSA4LjEzNDA1IDEuOTg4MTYgNy44MjE0OUMyLjMwMDcyIDcuNTA4OTMgMi43MjQ2NCA3LjMzMzMzIDMuMTY2NjcgNy4zMzMzM0g1LjI1IiBzdHJva2U9IiM1MDllZTMiIHN0cm9rZS13aWR0aD0iMS41IiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiPjwvcGF0aD4KPC9zdmc+) Yes

![](data:image/svg+xml;base64,PHN2ZyBpZCBjbGFzcz0icm90YXRlLTE4MCBtZS0xIiB3aWR0aD0iMTgiIGhlaWdodD0iMTgiIHZpZXdib3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICAgIDxwYXRoIGQ9Ik0xMC42NjY3IDcuMzMzMzNIMTQuNjM2N0MxNC45MjA3IDcuMzMzMzQgMTUuMjAwMSA3LjQwNTk1IDE1LjQ0ODIgNy41NDQyN0MxNS42OTYzIDcuNjgyNTkgMTUuOTA0OSA3Ljg4MjAyIDE2LjA1NDMgOC4xMjM2NEMxNi4yMDM2IDguMzY1MjUgMTYuMjg4OCA4LjY0MTA0IDE2LjMwMTYgOC45MjQ4QzE2LjMxNDQgOS4yMDg1NyAxNi4yNTQ1IDkuNDkwOSAxNi4xMjc1IDkuNzQ1TDEzLjIxMDggMTUuNTc4M0MxMy4wNzI0IDE1Ljg1NTQgMTIuODU5NSAxNi4wODg0IDEyLjU5NiAxNi4yNTEyQzEyLjMzMjUgMTYuNDE0IDEyLjAyODkgMTYuNTAwMSAxMS43MTkyIDE2LjVIOC4zNzE2N0M4LjIzNTgzIDE2LjUgOC4xIDE2LjQ4MzMgNy45Njc1IDE2LjQ1TDQuODMzMzMgMTUuNjY2N00xMC42NjY3IDcuMzMzMzNWMy4xNjY2N0MxMC42NjY3IDIuNzI0NjQgMTAuNDkxMSAyLjMwMDcyIDEwLjE3ODUgMS45ODgxNkM5Ljg2NTk1IDEuNjc1NTkgOS40NDIwMyAxLjUgOSAxLjVIOC45MjA4M0M4LjUwNDE3IDEuNSA4LjE2NjY3IDEuODM3NSA4LjE2NjY3IDIuMjU0MTdDOC4xNjY2NyAyLjg0OTE3IDcuOTkwODMgMy40MzA4MyA3LjY2IDMuOTI1ODNMNC44MzMzMyA4LjE2NjY3VjE1LjY2NjdNMTAuNjY2NyA3LjMzMzMzSDlNNC44MzMzMyAxNS42NjY3SDMuMTY2NjdDMi43MjQ2NCAxNS42NjY3IDIuMzAwNzIgMTUuNDkxMSAxLjk4ODE2IDE1LjE3ODVDMS42NzU1OSAxNC44NjYgMS41IDE0LjQ0MiAxLjUgMTRWOUMxLjUgOC41NTc5NyAxLjY3NTU5IDguMTM0MDUgMS45ODgxNiA3LjgyMTQ5QzIuMzAwNzIgNy41MDg5MyAyLjcyNDY0IDcuMzMzMzMgMy4xNjY2NyA3LjMzMzMzSDUuMjUiIHN0cm9rZT0iIzUwOWVlMyIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCI+PC9wYXRoPgo8L3N2Zz4=) No

Send

###### Thanks for your feedback! 

[ Want to improve these docs? [Propose a change.](https://github.com/metabase/metabase/blob/master/docs/embedding/sdk/questions.md) ]