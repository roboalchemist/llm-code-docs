# Source: https://posthog.com/docs/web-analytics/installation/vue.md

# Source: https://posthog.com/docs/session-replay/installation/vue.md

# Source: https://posthog.com/docs/experiments/installation/vue.md

# Vue experiments installation - Docs

1.  1

    ## Install the package

    Required

    Install the PostHog JavaScript library using your package manager:

    PostHog AI

    ### npm

    ```bash
    npm install posthog-js
    ```

    ### yarn

    ```bash
    yarn add posthog-js
    ```

    ### pnpm

    ```bash
    pnpm add posthog-js
    ```

    **Vue version**

    This guide is for Vue 3 and above. For Vue 2.x, see our [Vue docs](/docs/libraries/vue-js.md).

2.  2

    ## Create a composable

    Required

    Create a new file `src/composables/usePostHog.js`:

    src/composables/usePostHog.js

    PostHog AI

    ```javascript
    import posthog from 'posthog-js'
    export function usePostHog() {
      posthog.init('<ph_project_token>', {
        api_host: 'https://us.i.posthog.com',
        defaults: '2026-01-30'
      })
      return { posthog }
    }
    ```

3.  3

    ## Import in your router

    Required

    In `router/index.js`, import the `usePostHog` composable and call it:

    router/index.js

    PostHog AI

    ```javascript
    import { createRouter, createWebHistory } from 'vue-router'
    import HomeView from '../views/HomeView.vue'
    import { usePostHog } from '@/composables/usePostHog'
    const router = createRouter({
      history: createWebHistory(import.meta.env.BASE_URL),
      routes: [
        {
          path: '/',
          name: 'home',
          component: HomeView,
        },
        {
          path: '/about',
          name: 'about',
          component: () => import('../views/AboutView.vue'),
        },
      ],
    })
    const { posthog } = usePostHog()
    export default router
    ```

4.  4

    ## Implement your experiment

    Required

    Experiments run on top of our feature flags. You can define which version of your code runs based on the return value of the feature flag:

    ```javascript
    if (posthog.getFeatureFlag('your-experiment-feature-flag') === 'test') {
        // Do something differently for this user
    } else {
        // It's a good idea to let control variant always be the default behaviour,
        // so if something goes wrong with flag evaluation, you don't break your app.
    }
    // Test that it works
    posthog.featureFlags.overrideFeatureFlags({ flags: {'your-experiment-feature-flag': 'test'} })
    ```

5.  5

    ## Run your experiment

    Required

    Once you've implemented the feature flag in your code, you'll enable it for a target audience by creating a new experiment in the PostHog dashboard.

6.  6

    ## Next steps

    Recommended

    Now that you're running experiments, continue with the resources below to learn what else Experiments enables within the PostHog platform.

    | Resource | Description |
    | --- | --- |
    | [Creating an experiment](/docs/experiments/creating-an-experiment.md) | How to create an experiment in PostHog |
    | [Adding experiment code](/docs/experiments/adding-experiment-code.md) | How to implement experiments for all platforms |
    | [Statistical significance](/docs/experiments/statistics-bayesian.md) | Understanding when results are meaningful |
    | [Experiment insights](/docs/experiments/analyzing-results.md) | How to analyze your experiment data |
    | [More tutorials](/docs/experiments/tutorials.md) | Other real-world examples and use cases |

### Community questions

Ask a question

### Was this page useful?

HelpfulCould be better