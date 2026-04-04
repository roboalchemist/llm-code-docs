# Source: https://www.thundercompute.com/docs/vscode/quickstart.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.thundercompute.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Quickstart

> Get started with Thunder Compute using VSCode, Cursor, or Windsurf

export const QuickstartCard = ({ title, icon, href, children, selected }) => {
  const enter = e => { if (selected) return; const el = e.currentTarget; el.style.borderColor = '#555'; el.querySelector('[data-title]').style.color = '#fff'; el.querySelector('[data-sub]').style.opacity = '0.7'; el.querySelector('[data-icon]').style.opacity = '0.7'; };
  const leave = e => { if (selected) return; const el = e.currentTarget; el.style.borderColor = '#333'; el.querySelector('[data-title]').style.color = ''; el.querySelector('[data-sub]').style.opacity = '0.5'; el.querySelector('[data-icon]').style.opacity = '0.35'; };
  return (
  <a href={href} className="group" style={{ textDecoration: 'none', borderBottom: 'none', color: 'inherit', display: 'block', marginBottom: '0.75rem' }}>
    <div className="border rounded-xl p-5 transition-all duration-150 border-zinc-200 dark:border-zinc-800" style={{
      minHeight: '8rem',
      height: '100%',
      borderWidth: '1.5px',
      borderColor: selected ? '#95c5ea' : '#333',
    }} onMouseEnter={enter} onMouseLeave={leave}>
      <div data-icon style={{ marginBottom: '0.75rem', opacity: selected ? 1 : 0.35, transition: 'opacity 0.15s ease' }}>
        <Icon icon={icon} size={24} color="#95c5ea" />
      </div>
      <div data-title style={{ fontWeight: 600, fontSize: '1.05rem', marginBottom: '0.25rem', color: selected ? '#fff' : undefined, transition: 'color 0.15s ease' }}>{title}</div>
      <div data-sub style={{ fontSize: '0.9rem', opacity: selected ? 0.7 : 0.5, transition: 'opacity 0.15s ease' }}>{children}</div>
    </div>
  </a>
  );
};

<Columns cols={3}>
  <QuickstartCard title="VS Code" icon="window" href="/vscode/quickstart" selected={true}>
    Editor extension
  </QuickstartCard>

  <QuickstartCard title="CLI" icon="terminal" href="/cli/quickstart">
    Command line
  </QuickstartCard>

  <QuickstartCard title="Console" icon="browser" href="/console/quickstart">
    Web interface
  </QuickstartCard>
</Columns>

## Installation

Click the following links to access the Thunder Compute extension:

* [VSCode extension](vscode:extension/ThunderCompute.thunder-compute)
* [Cursor extension](cursor:extension/ThunderCompute.thunder-compute)
* [Windsurf extension](windsurf:extension/ThunderCompute.thunder-compute)

You must have already installed the corresponding editor for each link to work.

## Authentication

You may be automatically prompted to login. If not, open the command palette with `Ctrl + Shift + P` (or `Cmd + Shift + P` on macOS) and run `Thunder Compute: Login`.

Your browser will open automatically to complete authentication.

## Add a Payment Method

In the console, [add a payment method](https://console.thundercompute.com/settings/billing) to your account.

## Using The Extension

You can create instances through the [console](https://console.thundercompute.com) or directly through the extension like so:

<img src="https://mintcdn.com/thundercompute/mmRzgHvGKON9hkSq/images/VSCode_Create_Instance.png?fit=max&auto=format&n=mmRzgHvGKON9hkSq&q=85&s=a80a30dc614d4a4ea83ee7004bbe056b" alt="Create Instance" data-og-width="1092" width="1092" data-og-height="622" height="622" data-path="images/VSCode_Create_Instance.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/thundercompute/mmRzgHvGKON9hkSq/images/VSCode_Create_Instance.png?w=280&fit=max&auto=format&n=mmRzgHvGKON9hkSq&q=85&s=74ffb91abd0deb23947affbdcb590640 280w, https://mintcdn.com/thundercompute/mmRzgHvGKON9hkSq/images/VSCode_Create_Instance.png?w=560&fit=max&auto=format&n=mmRzgHvGKON9hkSq&q=85&s=899cbc77dd389bc8ea90cc134a695cd6 560w, https://mintcdn.com/thundercompute/mmRzgHvGKON9hkSq/images/VSCode_Create_Instance.png?w=840&fit=max&auto=format&n=mmRzgHvGKON9hkSq&q=85&s=b40845857839c1c916804d4298da2a3b 840w, https://mintcdn.com/thundercompute/mmRzgHvGKON9hkSq/images/VSCode_Create_Instance.png?w=1100&fit=max&auto=format&n=mmRzgHvGKON9hkSq&q=85&s=f3620f48b1c9c7d3790cd39d3eba34bb 1100w, https://mintcdn.com/thundercompute/mmRzgHvGKON9hkSq/images/VSCode_Create_Instance.png?w=1650&fit=max&auto=format&n=mmRzgHvGKON9hkSq&q=85&s=d92527e6f6ec0eb5771d688ae4a4ea5f 1650w, https://mintcdn.com/thundercompute/mmRzgHvGKON9hkSq/images/VSCode_Create_Instance.png?w=2500&fit=max&auto=format&n=mmRzgHvGKON9hkSq&q=85&s=1b46b73f0db8d24a6c5a302015d7f6a1 2500w" />

Click on the `Connect` button next to your instance, shaped like two arrows pointing towards each other.

<img src="https://mintcdn.com/thundercompute/mmRzgHvGKON9hkSq/images/VSCode_Connect_Instance.png?fit=max&auto=format&n=mmRzgHvGKON9hkSq&q=85&s=4021cfeb51b37c6263e2d6f85a0a375e" alt="Connect to Instance" data-og-width="656" width="656" data-og-height="183" height="183" data-path="images/VSCode_Connect_Instance.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/thundercompute/mmRzgHvGKON9hkSq/images/VSCode_Connect_Instance.png?w=280&fit=max&auto=format&n=mmRzgHvGKON9hkSq&q=85&s=f4ffdeb5881bd5524a3eb8d5aef53ef5 280w, https://mintcdn.com/thundercompute/mmRzgHvGKON9hkSq/images/VSCode_Connect_Instance.png?w=560&fit=max&auto=format&n=mmRzgHvGKON9hkSq&q=85&s=30c77348af592cbed19f93a3d47c57a0 560w, https://mintcdn.com/thundercompute/mmRzgHvGKON9hkSq/images/VSCode_Connect_Instance.png?w=840&fit=max&auto=format&n=mmRzgHvGKON9hkSq&q=85&s=6e42c91733b7a312224bce5d628075a8 840w, https://mintcdn.com/thundercompute/mmRzgHvGKON9hkSq/images/VSCode_Connect_Instance.png?w=1100&fit=max&auto=format&n=mmRzgHvGKON9hkSq&q=85&s=1929a15e5312834d6ecef6a8415ffd3e 1100w, https://mintcdn.com/thundercompute/mmRzgHvGKON9hkSq/images/VSCode_Connect_Instance.png?w=1650&fit=max&auto=format&n=mmRzgHvGKON9hkSq&q=85&s=44a849fa8069bcbdd870e225cd365d6e 1650w, https://mintcdn.com/thundercompute/mmRzgHvGKON9hkSq/images/VSCode_Connect_Instance.png?w=2500&fit=max&auto=format&n=mmRzgHvGKON9hkSq&q=85&s=8eae3bf2f53d16fd0115ed3634888ec1 2500w" />

<Note>
  If connecting to the instance fails, check that you have the remote-ssh extension installed on your editor.
</Note>

A new window will open connected to your instance. You can drag files you need into the file explorer, run notebooks, scripts, and more as if they were on your local machine.

<img src="https://mintcdn.com/thundercompute/mmRzgHvGKON9hkSq/images/VSCode_SSH.png?fit=max&auto=format&n=mmRzgHvGKON9hkSq&q=85&s=bcddd30a99fa944a6b75e9599ccafea3" alt="SSH View" data-og-width="925" width="925" data-og-height="474" height="474" data-path="images/VSCode_SSH.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/thundercompute/mmRzgHvGKON9hkSq/images/VSCode_SSH.png?w=280&fit=max&auto=format&n=mmRzgHvGKON9hkSq&q=85&s=d339cce570f87bc2e58ef5ac2fe1f53e 280w, https://mintcdn.com/thundercompute/mmRzgHvGKON9hkSq/images/VSCode_SSH.png?w=560&fit=max&auto=format&n=mmRzgHvGKON9hkSq&q=85&s=d137805df66171965d4e560e0c2d4698 560w, https://mintcdn.com/thundercompute/mmRzgHvGKON9hkSq/images/VSCode_SSH.png?w=840&fit=max&auto=format&n=mmRzgHvGKON9hkSq&q=85&s=22ff646f728af98fab4396b7123778a3 840w, https://mintcdn.com/thundercompute/mmRzgHvGKON9hkSq/images/VSCode_SSH.png?w=1100&fit=max&auto=format&n=mmRzgHvGKON9hkSq&q=85&s=7292b83454e13bd9a4d25fcae8baba91 1100w, https://mintcdn.com/thundercompute/mmRzgHvGKON9hkSq/images/VSCode_SSH.png?w=1650&fit=max&auto=format&n=mmRzgHvGKON9hkSq&q=85&s=2d96bc0c23529e0091776ae0ef422aca 1650w, https://mintcdn.com/thundercompute/mmRzgHvGKON9hkSq/images/VSCode_SSH.png?w=2500&fit=max&auto=format&n=mmRzgHvGKON9hkSq&q=85&s=4b6be506c6d192c64894c7a1dc1334d5 2500w" />

That's it! You're now ready to use Thunder Compute.

## Next Steps

* Learn about [Prototyping vs Production](/prototyping-vs-production) to choose the right mode for your workload
* Explore [Technical Specifications](/technical-specs) for hardware, networking, and storage details
* Learn how to [transfer files](/vscode/operations/file-transfers), [create snapshots](/vscode/operations/snapshots), and more in the Operations section
* Learn how to [Run a Jupyter Notebook](/guides/running-jupyter-notebooks-on-thunder-compute)
