# Source: https://docs.xano.com/troubleshooting-and-support/start.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Troubleshooting and Support - Start Here

Choose the option that best describes the issue you're experiencing to get started with troubleshooting.

## Quick Links

<Columns cols="2">
  <Card href="Xano Status Page" title="Xano Status Page" href="https://status.xano.com" icon="signal-bars" />

  <Card href="Instance Selection Screen" title="Instance Selection Screen" href="https://app.xano.com/instance?mode=master" icon="server" />

  <Card href="Xano Community" title="Xano Community" href="https://community.xano.com" icon="users" />

  <div onClick={() => window.Intercom('show')} class="card block font-normal group relative my-2 ring-2 ring-transparent rounded-2xl bg-white dark:bg-background-dark border border-gray-950/10 dark:border-white/10 overflow-hidden w-full cursor-pointer hover:!border-primary dark:hover:!border-primary-light">
    <div class="px-6 py-5 relative" data-component-part="card-content-container">
      <div id="card-link-arrow-icon" class="absolute text-gray-400 dark:text-gray-500 group-hover:text-primary dark:group-hover:text-primary-light top-5 right-5">
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-arrow-up-right w-4 h-4">
          <path d="M7 7h10v10" />

          <path d="M7 17 17 7" />
        </svg>
      </div>

      <div class="h-6 w-6 fill-gray-800 dark:fill-gray-100 text-gray-800 dark:text-gray-100">
        <svg
          class="h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"
          style={{
      maskImage: "url('https://d3gk2c5xim1je2.cloudfront.net/v7.1.0/regular/life-ring.svg')",
      maskRepeat: "no-repeat",
      maskPosition: "center center"
    }}
        />
      </div>

      <div>
        <h2 class="not-prose font-semibold text-base text-gray-800 dark:text-white mt-4">
          Open Intercom Chat
        </h2>
      </div>
    </div>
  </div>
</Columns>

## Select Your Issue

<Columns cols="2">
  <Card href="/troubleshooting-and-support/my-instance-is-down" title="My Instance Is Down" icon="wifi-slash">Use this option if you're unable to access your Xano instance at all from the [instance selection screen](https://app.xano.com/instance?mode=master).</Card>
  <Card href="/troubleshooting-and-support/my-apis-arent-responding" title="My APIs Aren't Responding" icon="phone-slash">Use this option if you're able to access your Xano instance, but your APIs are not responding or timing out.</Card>
  <Card href="/troubleshooting-and-support/things-feel-slow" title="Things feel slow" icon="gauge-simple-low">Use this option if your APIs are responding, but things just feel slow overall.</Card>
  <Card href="/troubleshooting-and-support/error-reference" title="I see an error" icon="help-circle">Use this option if you're seeing a specific error.</Card>
</Columns>


Built with [Mintlify](https://mintlify.com).