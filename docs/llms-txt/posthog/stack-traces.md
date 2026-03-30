# Source: https://posthog.com/docs/error-tracking/stack-traces.md

# Stack traces - Docs

Error tracking enables you to view the stack trace and code context associated with an exception. This can help understand, identify and resolve the root cause of an issue.

Stack traces are available for all languages and can be found in the details page of an issue.

![Stack traces example](https://res.cloudinary.com/dmukukwp6/image/upload/Screenshot_2025_01_30_at_09_48_09_63dd3c5241.png)![Stack traces example](https://res.cloudinary.com/dmukukwp6/image/upload/Screenshot_2025_01_30_at_09_48_39_1030eea240.png)

## Resolving stack traces

If you use a compiled language or server minified bundles, you'll need to [upload source maps](/docs/error-tracking/upload-source-maps.md) to get stack traces. Compiled or minified code obfuscates the original source code, so PostHog uses the source map to resolve the stack trace to the original source code.

For languages like Python, the stack trace and code context can be gathered by the PostHog client and requires no additional processing.

### Uploading source maps

If your source maps are not publicly hosted, you will need to upload them during your build process to see unminified code in your stack traces. You can either use the `@posthog/nextjs-config` package or the `posthog-cli` to handle this process. Select your platform to view instructions.

-   [![](https://res.cloudinary.com/dmukukwp6/image/upload/posthog.com/contents/images/docs/integrate/js.svg)Web](/docs/error-tracking/upload-source-maps/web.md)
-   [![](https://res.cloudinary.com/dmukukwp6/image/upload/posthog.com/contents/images/docs/integrate/frameworks/nextjs.svg)Next.js](/docs/error-tracking/upload-source-maps/nextjs.md)
-   [![](https://res.cloudinary.com/dmukukwp6/image/upload/posthog.com/contents/images/docs/integrate/nodejs.svg)Node.js](/docs/error-tracking/upload-source-maps/node.md)
-   [![](https://res.cloudinary.com/dmukukwp6/image/upload/posthog.com/contents/images/docs/integrate/react.svg)React](/docs/error-tracking/upload-source-maps/react.md)
-   [![](https://res.cloudinary.com/dmukukwp6/image/upload/posthog.com/contents/docs/integrate/frameworks/angular.svg)Angular](/docs/error-tracking/upload-source-maps/angular.md)
-   [![](https://res.cloudinary.com/dmukukwp6/image/upload/posthog.com/contents/images/docs/integrate/frameworks/nuxt.svg)Nuxt](/docs/error-tracking/upload-source-maps/nuxt.md)
-   [![](https://res.cloudinary.com/dmukukwp6/image/upload/posthog.com/contents/images/docs/integrate/react.svg)React Native](/docs/error-tracking/upload-source-maps/react-native.md)
-   [![](https://res.cloudinary.com/dmukukwp6/image/upload/Android_robot_bec2fb7318.svg)Android](/docs/error-tracking/upload-mappings/android.md)
-   [![](https://res.cloudinary.com/dmukukwp6/image/upload/posthog.com/contents/images/docs/integrate/flutter.svg)Flutter](/docs/error-tracking/upload-source-maps/flutter.md)
-   [![](https://res.cloudinary.com/dmukukwp6/image/upload/posthog.com/contents/images/docs/integrate/ios.svg)iOS](/docs/error-tracking/upload-source-maps/ios.md)
-   [![](https://res.cloudinary.com/dmukukwp6/image/upload/Rollup_js_c306a2fde3.svg)Rollup](/docs/error-tracking/upload-source-maps/rollup.md)
-   [![](https://res.cloudinary.com/dmukukwp6/image/upload/webpack_3fc774b5a5.svg)Webpack](/docs/error-tracking/upload-source-maps/webpack.md)
-   [![](https://res.cloudinary.com/dmukukwp6/image/upload/Vitejs_logo_98ffe5d5ee.svg)Vite](/docs/error-tracking/upload-source-maps/vite.md)
-   [CLI](/docs/error-tracking/upload-source-maps/cli.md)
-   [![](https://res.cloudinary.com/dmukukwp6/image/upload/github_mark_903e35d471.svg)GitHub Action](/docs/error-tracking/upload-source-maps/github-actions.md)

## Release context in stack traces

Error tracking displays release information over stack traces to help you track down the root cause of an issue, down to the commit and version that produced it. This context can be defined when you [upload sourcemaps](/docs/error-tracking/upload-source-maps.md).

![Error tracking releases](https://res.cloudinary.com/dmukukwp6/image/upload/w_1600,c_limit,q_auto,f_auto/release_light_d5955d3b5e.png)![Error tracking releases](https://res.cloudinary.com/dmukukwp6/image/upload/w_1600,c_limit,q_auto,f_auto/release_dark_67fed14b12.png)

Learn more about [releases](/docs/error-tracking/releases.md) in error tracking.

## Source linking

When viewing stack traces in PostHog, you can click directly through to the relevant code in your GitHub or GitLab repository. Each stack frame includes a **View commit** button (displayed using a GitHub or GitLab icon) that links to the exact file and line where the error occurred.

![Stacktrace with GitLab source link](https://res.cloudinary.com/dmukukwp6/image/upload/q_auto,f_auto/Clean_Shot_2025_11_20_at_14_37_09_2x_2ff2e56430.png)![Stacktrace with GitLab source link](https://res.cloudinary.com/dmukukwp6/image/upload/q_auto,f_auto/Clean_Shot_2025_11_20_at_14_37_09_2x_2ff2e56430.png)

Source linking requires a [GitHub or GitLab integration](/docs/error-tracking/integrations.md) and a [release](/docs/error-tracking/releases.md) with repository information. Once set up, PostHog automatically adds source links to your stack traces.

## Troubleshooting symbol sets

Compiled or minified languages requires additional information to perform a process called symbolification to produce the same stack trace and code context output shown above. The additional information is known as a symbol set.

The `source` of a frame in the exception stack trace should point to the minified code of your application which should contain the `sourceMappingUrl` parameter denoting the location of the source map. These files must either be publicly accessible for PostHog to fetch or uploaded manually to symbolify the stack trace.

You can see the symbol sets fetched by PostHog and the associated frames within the [error tracking settings](https://app.posthog.com/settings/project-error-tracking#error-tracking-symbol-sets). Any missing symbol sets will also be present along with the failure reason. From here, you can also manually upload missing symbol sets or replace existing ones.

![Symbol set examples](https://res.cloudinary.com/dmukukwp6/image/upload/Screenshot_2025_01_29_at_21_24_09_7b244773eb.png)![Symbol set examples](https://res.cloudinary.com/dmukukwp6/image/upload/Screenshot_2025_01_29_at_21_24_27_d8ab1b154b.png)

We strongly recommend you follow the [upload source maps](/docs/error-tracking/upload-source-maps.md) guide to ensure your stack traces are uploaded automatically in CI instead of manually debugging the process. If you're still having issues, [let us know in-app](https://us.posthog.com/project/2#panel=support%3Afeedback%3Aerror_tracking%3A%3Afalse).

### Community questions

Ask a question

### Was this page useful?

HelpfulCould be better