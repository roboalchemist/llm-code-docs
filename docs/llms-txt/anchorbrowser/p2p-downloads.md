# Source: https://docs.anchorbrowser.io/advanced/p2p-downloads.md

# P2P Download

> Capture files directly in the browser without cloud storage

## What is P2P Download?

P2P (Peer-to-Peer) downloads capture files directly in the browser memory without ever uploading them to cloud storage. When a user downloads a file in your browser session, instead of the file going to Anchor's servers, it's intercepted and made available to you immediately through browser hooks.

## How It Works

Traditional downloads follow this path:

* User clicks download → File goes to browser → File uploads to Anchor's servers → You fetch from Anchor's servers

P2P downloads work differently:

* User clicks download → File captured in browser memory → You fetch from the browser

The browser intercept download events, allowing you to extract the file data directly without any cloud storage involved.

## Implementation Example

<CodeGroup>
  ```tsx node.js theme={null}
  import { promises as fs, existsSync } from "node:fs";
  import { chromium } from "playwright";
  import AnchorBrowser from 'anchorbrowser';

  const { ANCHOR_API_KEY } = process.env;

  /**
   * Save a download to disk.
   * Handles three possible formats:
   *   1. Playwright Download object
   *   2. Base‑64 string
   *   3. Fallback text scraped from the page
   */
  async function saveDownload(download, filePath, page) {
    // 1. Playwright Download object
    if (download && typeof download.path === "function") {
      try {
        const tmpPath = await download.path();
        if (tmpPath && existsSync(tmpPath)) {
          await download.saveAs(filePath);
          return filePath;
        }
      } catch {
        /* ignore and fall through */
      }
    }

    // 2. Raw base64 string
    if (typeof download === "string") {
      try {
        await fs.writeFile(filePath, Buffer.from(download, "base64"));
        return filePath;
      } catch {
        /* ignore and fall through */
      }
    }

    // 3. Fallback – ask the page for data or capture visible text
    if (page) {
      try {
        const blob = await page.evaluate(() => window._anchorExtractDownloadData());
        return saveDownload(blob, filePath);
      } catch {
        /* ignore and fall through */
      }

      const fallbackText = await page.evaluate(() => {
        const el = document.querySelector("main") || document.body;
        return el.innerText || "";
      });
      await fs.writeFile(filePath, fallbackText, "utf8");
      return filePath;
    }
    throw new Error("Failed to save download");
  }

  const downloadHandler = (filePath) => async (page, info) => {
    if (info?.value) {
      try {
        return await saveDownload(info.value, filePath);
      } catch {
        /* ignore and fall through */
      }
    }
    return saveDownload(null, filePath, page);
  };

  async function createSession() {
    const anchor_client = new AnchorBrowser({apiKey: ANCHOR_API_KEY});
    const session = await anchor_client.sessions.create({
      browser: { p2p_download: { active: true } }
    });
    return session.data;
  }

  (async () => {
    const session = await createSession();
    if (!session?.cdp_url) throw new Error("No CDP URL in session");

    const browser = await chromium.connectOverCDP(session.cdp_url);
    const context = browser.contexts()[0];
    const page = context.pages()[0];

    await page.goto("https://v0-download-and-upload-text.vercel.app/");
    await page.waitForSelector("button");

    const [download] = await Promise.all([
      page.waitForEvent("download", { timeout: 5000 }),
      page.click("button"),
      page.waitForTimeout(500), // allow JS to finish
    ]);

    const filename = download.suggestedFilename();
    await downloadHandler(filename)(page, { value: download });

    const content = await fs.readFile(filename, "utf8");
    console.log(`Downloaded '${filename}', content:\n${content}`);

    await browser.close();
  })();

  ```

  ```python python theme={null}
  import os, base64, json
  from playwright.sync_api import sync_playwright
  from anchorbrowser import Anchorbrowser

  ANCHOR_API_KEY = os.getenv("ANCHOR_API_KEY")

  def save_download(src, path, page=None):
      """Persist a Playwright Download object or base‑64 string to *path*.
      Falls back to blob extraction or page text when needed.
      """
      if hasattr(src, "path"):
          try:
              tmp = src.path()
              if tmp and os.path.exists(tmp):
                  src.save_as(path)
                  return path
          except Exception:
              pass

      if isinstance(src, str):
          try:
              with open(path, "wb") as f:
                  f.write(base64.b64decode(src))
              return path
          except Exception:
              pass

      if page:
          try:
              blob = page.evaluate("() => window._anchorExtractDownloadData()")
              return save_download(blob, path)
          except Exception:
              # As a last resort, dump visible page text
              text = page.evaluate(
                  "() => (document.querySelector('main')||document.body).innerText"
              )
              with open(path, "w") as f:
                  f.write(text)
              return path

      raise RuntimeError("Failed to save download")

  def download_handler(path):
      """Return a function (page, download_info) that writes to *path*."""
      def _handle(page, info=None):
          if info and hasattr(info, "value"):
              try:
                  return save_download(info.value, path)
              except Exception:
                  pass
          # Fallback to blob extraction
          return save_download(None, path, page)
      return _handle

  def create_session():
      anchor_client = Anchorbrowser(api_key=ANCHOR_API_KEY)
      session = anchor_client.sessions.create({
          "browser": {
              "p2p_download": {
                  "active": True
              }
          }
      })
      return session.data

  with sync_playwright() as p:
      session = create_session()
      if not session or "cdp_url" not in session:
          print("Could not obtain a valid browser session – exiting.")
          raise SystemExit(1)

      browser = p.chromium.connect_over_cdp(session["cdp_url"])
      page = browser.contexts[0].pages[0]

      page.goto("https://v0-download-and-upload-text.vercel.app/")
      page.wait_for_selector("button", state="visible")

      with page.expect_download(timeout=5000) as dl:
          page.click("button")
          page.wait_for_timeout(500)  # allow JS to finish

      filename = dl.value.suggested_filename
      handler = download_handler(filename)
      handler(page, dl)

      with open(filename) as f:
          snippet = f.read()
      print(f"Downloaded '{filename}', content:\n{snippet}")
  ```
</CodeGroup>
