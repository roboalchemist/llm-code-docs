# Source: https://docs.trackjs.com/browser-agent/integrations/redux/

Title: Integrating TrackJS with Redux and Redux-Toolkit

URL Source: https://docs.trackjs.com/browser-agent/integrations/redux/

Markdown Content:
[Why Use Redux with TrackJS?](https://docs.trackjs.com/browser-agent/integrations/redux/#why-use-redux-with-trackjs "Permalink Here")
-------------------------------------------------------------------------------------------------------------------------------------

Redux is a predictable state container for JavaScript applications that helps you manage complex application state in a centralized store. When errors occur in production, understanding the state of your application at the time of the error is crucial for debugging.

By integrating TrackJS with Redux, you get:

*   **Automatic Action Logging**: Every Redux action is recorded as telemetry, giving you a complete timeline of what happened before an error
*   **State Snapshots on Errors**: The full Redux state is captured whenever an error occurs, showing you exactly what data was in your app at the time
*   **Better Debugging**: Instead of guessing what led to an error, you can see the exact sequence of actions and state changes

This integration helps you quickly reproduce and fix production issues by providing complete context around every error.

[Redux with TrackJS](https://docs.trackjs.com/browser-agent/integrations/redux/#redux-with-trackjs "Permalink Here")
--------------------------------------------------------------------------------------------------------------------

import { createStore, compose, StoreEnhancer } from 'redux';import { TrackJS } from 'trackjs';import reducers from './reducers';// Initialize TrackJSTrackJS.install({ token: 'YOUR_TRACKJS_TOKEN', /* other config options @see https://docs.trackjs.com/browser-agent/sdk-reference/agent-config/ */});// TrackJSEnhancer is included inline for simplicity of this example. You probably// want to move this into a utility file in your own codebase.const trackJSEnhancer = () => (createStore) => (reducer, initialState) => { const store = createStore(reducer, initialState); // Wrap the dispatch function to add TrackJS hooks const originalDispatch = store.dispatch; store.dispatch = (action) => { // Log all actions to TrackJS Telemetry. TrackJS.console.info(action); try { // Update TrackJS metadata and configuration with state properties so we // get the latest info if an error occurs. const state = store.getState(); TrackJS.addMetadata('todosCount', state.todos?.length || 0); if (state.user?.id) { TrackJS.configure({ userId: state.user.id }); } return originalDispatch(action); } catch (error) { // Include the current state in the error Telemetry. You may want to filter // out sensitive data before sending TrackJS.console.warn(store.getState()); TrackJS.track(error); throw error; // Re-throw to maintain normal error handling } }; return store;};// Create store with TrackJS enhancerconst initialState = {};const store = createStore(reducer, initialState, compose(trackJSEnhancer() /* other enhancers */));

[TrackJS Redux Enhancer](https://docs.trackjs.com/browser-agent/integrations/redux/#code-trackjs-redux-enhancer)

[Redux Toolkit with TrackJS](https://docs.trackjs.com/browser-agent/integrations/redux/#redux-toolkit-with-trackjs "Permalink Here")
------------------------------------------------------------------------------------------------------------------------------------

If you are using the modern Redux-Toolkit approach, the syntax needs to be modified slightly.

import { configureStore, StoreEnhancer } from '@reduxjs/toolkit';import { TrackJS } from 'trackjs';import reducers from './reducers';// Initialize TrackJSTrackJS.install({ token: 'YOUR_TRACKJS_TOKEN', /* other config options @see https://docs.trackjs.com/browser-agent/sdk-reference/agent-config/ */});// TrackJSEnhancer is included inline for simplicity of this example. You probably// want to move this into a utility file in your own codebase.const trackJSEnhancer = () => (createStore) => (reducer, initialState) => { const store = createStore(reducer, initialState); // Wrap the dispatch function to add TrackJS hooks const originalDispatch = store.dispatch; store.dispatch = (action) => { // Log all actions to TrackJS Telemetry. TrackJS.console.info(action); try { // Update TrackJS metadata and configuration with state properties so we // get the latest info if an error occurs. const state = store.getState(); TrackJS.addMetadata('todosCount', state.todos?.length || 0); if (state.user?.id) { TrackJS.configure({ userId: state.user.id }); } return originalDispatch(action); } catch (error) { // Include the current state in the error Telemetry. You may want to filter // out sensitive data before sending TrackJS.console.warn(store.getState()); TrackJS.track(error); throw error; // Re-throw to maintain normal error handling } }; return store;};// Configure store with TrackJS enhancerconst store = configureStore({ reducer: reducers, enhancers: (getDefaultEnhancers) => getDefaultEnhancers().concat( trackJSEnhancer() )});

[TrackJS Redux-Toolkit Enhancer](https://docs.trackjs.com/browser-agent/integrations/redux/#code-trackjs-redux-toolkit-enhancer)

[Redux Dev Tools](https://docs.trackjs.com/browser-agent/integrations/redux/#redux-dev-tools "Permalink Here")
--------------------------------------------------------------------------------------------------------------

It’s great to log the actions that occurred before an error. But what if you could play them back in Redux dev tools? Our awesome community has created a logger that will allow you to replay the actions in a new session!

Check out the [TrackJS Redux Logger on Github](https://github.com/timarney/redux-trackjs-logger).
