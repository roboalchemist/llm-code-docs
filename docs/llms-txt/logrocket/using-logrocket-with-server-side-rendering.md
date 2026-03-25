# Source: https://docs.logrocket.com/docs/using-logrocket-with-server-side-rendering.md

# Using LogRocket with server-side rendering

If you are using LogRocket with a server-side rendering framework, like [Next.js](https://github.com/zeit/next.js), be sure to initialize LogRocket (and any plugins you are using) on the client and not on the server.

## Example with Next.js

NextJS has a built-in way of adding third-party web-only scripts using the next/script package. You can [learn more from their documentation](https://nextjs.org/docs/app/building-your-application/optimizing/scripts) .

## Other options

Your server-side rendering framework likely has a way of adding web-only scripts (including analytics SDKs like ours), check with the relevant documentation to learn more.