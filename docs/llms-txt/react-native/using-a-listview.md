# Source: https://reactnative.dev/docs/using-a-listview.md

# Using List Views

React Native provides a suite of components for presenting lists of data. Generally, you'll want to use either [FlatList](/docs/flatlist.md) or [SectionList](/docs/sectionlist.md).

The `FlatList` component displays a scrolling list of changing, but similarly structured, data. `FlatList` works well for long lists of data, where the number of items might change over time. Unlike the more generic [`ScrollView`](/docs/using-a-scrollview.md), the `FlatList` only renders elements that are currently showing on the screen, not all the elements at once.

The `FlatList` component requires two props: `data` and `renderItem`. `data` is the source of information for the list. `renderItem` takes one item from the source and returns a formatted component to render.

This example creates a basic `FlatList` of hardcoded data. Each item in the `data` props is rendered as a `Text` component. The `FlatListBasics` component then renders the `FlatList` and all `Text` components.

If you want to render a set of data broken into logical sections, maybe with section headers, similar to `UITableView` on iOS, then a [SectionList](/docs/sectionlist.md) is the way to go.

One of the most common uses for a list view is displaying data that you fetch from a server. To do that, you will need to [learn about networking in React Native](/docs/network.md).
