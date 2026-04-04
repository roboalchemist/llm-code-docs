# Source: https://developer.zendesk.com/api-reference/conversations/

<!doctype html>
<html>
  <head>
    <title>API Reference | Sunshine Conversations</title>
    <!-- needed for adaptive design -->
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <link rel="icon" type="image/png" href="favicon.ico" />

    <!--
    ReDoc uses font options from the parent element
    So override default browser styles
    -->
    <style>
      body {
        margin: 0;
        padding: 0;
      }
    </style>
    <link rel="stylesheet" type="text/css" href="style.css" />
  </head>
  <body>
    <script>
      // Convert operationIds to screaming camel case in the URL. Fixes broken links due to change in casing
      // of operation IDs
      //
      // e.g. `/rest/#operation/getUser` -> `/rest/#operation/GetUser`
      if (/^#operation\/[a-z]\w+$/.test(window.location.hash)) {
        const [_, operationId] = window.location.hash.split("/")
        const screamingCamelOperationId =
          operationId.charAt(0).toUpperCase() + operationId.slice(1)
        window.location.hash = window.location.hash.replace(
          operationId,
          screamingCamelOperationId
        )
      }

      // A breaking change was introduced in ReDoc 2.0.0-rc.67 which changed the format of section IDs.
      // We have a few specific sections which need to be remapped to prevent breaking links to these old locations.
      //
      // When the page loads or the page hash changes, check for any of the legacy hash patterns, and replace with the
      // new section ID
      const hashCorrectionMap =  {
        '#section/Attachments-for-Messages': '#tag/Attachments/Attachments-for-Messages',
        '#section/Webhook-Triggers': '#tag/Webhooks/Webhook-Triggers',
        '#section/Securing-Sunshine-Conversations-Webhooks': '#tag/Webhooks/Securing-Sunshine-Conversations-Webhooks',
        '#section/Retry-policy': '#tag/Webhooks/Retry-policy',
      }

      function isLegacySectionHash(hash) {
        return Object.keys(hashCorrectionMap).includes(hash);
      }

      function correctLegacySectionHash(hash) {
        return hashCorrectionMap[hash] || hash;
      }

      if (isLegacySectionHash(window.location.hash)) {
        window.location.hash = correctLegacySectionHash(window.location.hash);
      }

      window.addEventListener("hashchange", (ev) => {
        if (isLegacySectionHash(window.location.hash)) {
          window.location.hash = correctLegacySectionHash(window.location.hash);
        }
      }, false);
    </script>
    <div id="redoc"></div>
    <script src="https://cdn.jsdelivr.net/npm/redoc@2.5.0/bundles/redoc.standalone.js"></script>
    <script>
      Redoc.init(
        "https://docs.smooch.io/sunco-openapi/openapi.yaml",
        {
          expandDefaultServerVariables: false,
          hideLoading: true,
          lazyRendering: true,
          hideDownloadButton: true,
          noAutoAuth: true,
          pathInMiddlePanel: true,
          expandResponses: "200,201",
          jsonSampleExpandLevel: "all",
          theme: {
            spacing: {
              sectionVertical: "10"
            },
            colors: {
              primary: {
                main: "rgba(3, 53, 61, 1)",
                light: "#0ab4cf",
                dark: "#000",
                contrastText: "#fff"
              },
              border: {
                light: "rgba(255, 255, 255, 0.01)"
              },
              responses: {
                success: {
                  color: "#001A1D",
                  backgroundColor: "#E3F0D2"
                },
                error: {
                  color: "#001A1D",
                  backgroundColor: "#F6C8BE"
                }
              },
            },
            sidebar: {
              activeTextColor: 'rgba(3, 53, 61, 1)'
            },
            typography: {
              headings: {
                fontWeight: 600
              },
              links: {
                color: "#1f73b7",
                hover: '#144a75',
                textDecoration: 'none',
                hoverTextDecoration: 'underline'
              }
            },
            rightPanel: {
              backgroundColor: "rgba(3, 53, 61, 1)"
            },
            codeSample: {
              backgroundColor: "rgba(1, 42, 47, 1)"
            },
            menu: {
              width: "260px",
              backgroundColor: "#fafafa",
              textColor: "#333333",
              activeTextColor: "#30AABC"
            }
          }
        },
        document.getElementById("redoc")
      )
    </script>
  </body>
</html>
