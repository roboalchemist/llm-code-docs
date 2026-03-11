# Source: https://docs.xano.com/xano-cli/platforms.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Platforms

> View platform versions available for tenant deployment

export const BrowserFrame = props => {
  const {url = "xano.run", maxWidth = 820, className = "", lightSrc, darkSrc, alt = "", children} = props || ({});
  const style = typeof maxWidth === "number" ? {
    maxWidth: `${maxWidth}px`,
    margin: "16px 0"
  } : {
    maxWidth,
    margin: "16px 0"
  };
  const hasSwapImages = Boolean(lightSrc && darkSrc);
  return <div className={`browser-frame ${className}`.trim()} style={style}>
      <div className="browser-frame__top">
        <div className="browser-frame__controls" aria-hidden="true">
          <span className="browser-frame__dot browser-frame__dot--red" />
          <span className="browser-frame__dot browser-frame__dot--yellow" />
          <span className="browser-frame__dot browser-frame__dot--green" />
        </div>
        <div className="browser-frame__address">{url}</div>
      </div>

      <div className="browser-frame__body">
        {hasSwapImages ? <>
            <img className="browser-frame__img--light" src={lightSrc} alt={alt} />
            <img className="browser-frame__img--dark" src={darkSrc} alt={alt} />
          </> : children}
      </div>
    </div>;
};

Platforms represent versioned infrastructure configurations that can be deployed to tenants. Platform commands operate at the account level and do not require a workspace.

## List Platforms

<BrowserFrame url="Terminal">
  ```bash  theme={null}
  xano platform list
  ```
</BrowserFrame>

Use `-o json` for the full JSON response.

## Get Platform Details

<BrowserFrame url="Terminal">
  ```bash  theme={null}
  xano platform get PLATFORM_ID
  ```
</BrowserFrame>


Built with [Mintlify](https://mintlify.com).