---
---
title: React Error Boundary
description: >-
---

The React Native SDK exports an error boundary component that uses [React component APIs](https://react.dev/reference/react/Component#catching-rendering-errors-with-an-error-boundary) to automatically catch and send JavaScript errors from inside a React component tree to Sentry.

## Prerequisites

To use the Error Boundary component, you need to have the React Native SDK [installed and configured for error monitoring](/platforms/react-native/).

## Use `Sentry.ErrorBoundary`

```javascript
An error has occurred</p>}>
  
</Sentry.ErrorBoundary>;
```

The Sentry Error Boundary is also available as a higher-order component.

```javascript
Sentry.withErrorBoundary(Example, { fallback: <p>an error has occurred</p> });
```

In development mode, React will rethrow errors caught within an error boundary to the global error handler. This will result in Sentry only reporting an error from the global error handler, but not from the error boundary itself. We recommend testing the error boundary with a production build of React.

In the example below, when the `` component hits an error, the `` component will send data about that error and the component tree to Sentry, open a user feedback dialog, and render a fallback UI.

```javascript
function FallbackComponent() {
  return <div>An error has occurred</div>;
}

const myFallback = ;
// Alternatively:
// const myFallback = () => ;

class App extends React.Component {
  render() {
    return (
      
        
      </Sentry.ErrorBoundary>
    );
  }
}

export default App;
```

By default, React [logs all errors to the console](https://github.com/facebook/react/blob/493f72b0a7111b601c16b8ad8bc2649d82c184a0/packages/react-reconciler/src/ReactFiberErrorLogger.js#L85), even if you're using a React error boundary. If you're using the `CaptureConsole` integration, Sentry will capture the error there and not through the error boundary.

## Linked Errors

In [React v17 and above](https://reactjs.org/blog/2020/08/10/react-v17-rc.html#native-component-stacks), the SDK will automatically parse the [error boundary](https://react.dev/reference/react/Component#componentdidcatch-parameters) `componentStack` and attach the full stacktrace to the event via `error.cause`. This requires the `nativeLinkedErrorsIntegration` to be enabled. (It's enabled by default.) To get the full source context, we recommend setting up [source maps](/platforms/react-native/sourcemaps/) for your project.

![React Error Boundary stacktrace](./img/errorboundary-error.png)

## Options

The ErrorBoundary component exposes a variety of props that can be passed in for extra configuration. There aren't any required options, but we highly recommend setting a fallback component.

`fallback` (React.ReactNode or Function)

A React element to render when the error boundary catches an error. This can be an actual React element (for example, ``), or a function that returns a React element. If you provide a function, Sentry will call it with additional info and helpers (see example below).

`onError` (Function)

A function that gets called when the Error Boundary encounters an error. `onError` is useful if you want to propagate the error into a state management library like Redux, or if you want to check any side effects that could have occurred due to the error.

`onMount` (Function)

A function that gets called on ErrorBoundary `componentDidMount()`.

`onUnmount` (Function)

A function that gets called on ErrorBoundary `componentWillUnmount()`.

`beforeCapture` (Function)

A function that gets called before an error is sent to Sentry, allowing for extra tags or context to be added to the error.

## Examples

### Setting a Fallback Function (Render Props)

Below, is an example where a fallback prop, using the [render props approach](https://react.dev/reference/react/cloneElement#passing-data-with-a-render-prop), is used to display a fallback UI on error. The fallback UI returns to a standard component state when reset using the `resetError()` API, provided by the component through render props.

```javascript
class MyComponent extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      message: "This is my app",
    };
  }

  render() {
    return (
       (
          
            You have encountered an error
            {error.toString()}
            {componentStack}
             {
                this.setState({ message: "This is my app" });
                // When resetError() is called it will
                // remove the Fallback component and render
                // the Sentry ErrorBoundary's children
                // in their initial state
                resetError();
              }}
            />
          </React.Fragment>
        )}
      >
        {this.state.message}
        {/* on click, this button sets an Object */}
        {/* as a message, not a string. Which will cause */}
        {/* an error to occur in the component tree */}
         this.setState({ message: { text: "Hello World" } })}
        />
      </Sentry.ErrorBoundary>
    );
  }
}

export default MyComponent;
```

### Using multiple error boundaries

When using multiple error boundaries, we recommend using `beforeCapture` to set tags/context so that you can tell which error boundary the error occurred from. In the example below, we attach tags to errors based on what route they rendered in:

```javascript
function MyComponent({ props }) {
  return (
    
       {
          scope.setTag("location", "first");
          scope.setTag("anotherTag", "anotherValue");
        }}
      >
        First
      </Sentry.ErrorBoundary>
       {
          scope.setTag("location", "second");
        }}
      >
        Second
      </Sentry.ErrorBoundary>
    </React.Fragment>
  );
}

export default MyComponent;
```
