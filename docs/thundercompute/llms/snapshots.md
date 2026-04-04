# Source: https://www.thundercompute.com/docs/vscode/operations/snapshots.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.thundercompute.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Snapshots

> Save and restore the state of your Thunder Compute instances

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
  <QuickstartCard title="VS Code" icon="window" href="/vscode/operations/snapshots" selected={true}>
    Editor extension
  </QuickstartCard>

  <QuickstartCard title="CLI" icon="terminal" href="/cli/operations/snapshots">
    Command line
  </QuickstartCard>

  <QuickstartCard title="Console" icon="browser" href="/console/operations/snapshots">
    Web interface
  </QuickstartCard>
</Columns>

## Create a Snapshot

1. Open the Thunder Compute sidebar panel.
2. Right click the running instance.
3. Select **Create Snapshot**.
4. Name the new snapshot.

<img src="https://mintcdn.com/thundercompute/E4VZCfEN9n0k1lco/images/VSCode_Create_Snapshot.png?fit=max&auto=format&n=E4VZCfEN9n0k1lco&q=85&s=6dfcfd566cdab58630c0c69221f31fe4" alt="Step by step on creating a snapshot" data-og-width="1400" width="1400" data-og-height="700" height="700" data-path="images/VSCode_Create_Snapshot.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/thundercompute/E4VZCfEN9n0k1lco/images/VSCode_Create_Snapshot.png?w=280&fit=max&auto=format&n=E4VZCfEN9n0k1lco&q=85&s=a795d31b0ab39d19b21775c25930d1bb 280w, https://mintcdn.com/thundercompute/E4VZCfEN9n0k1lco/images/VSCode_Create_Snapshot.png?w=560&fit=max&auto=format&n=E4VZCfEN9n0k1lco&q=85&s=ae9d77aa69f679bf21fce09ba7832b0f 560w, https://mintcdn.com/thundercompute/E4VZCfEN9n0k1lco/images/VSCode_Create_Snapshot.png?w=840&fit=max&auto=format&n=E4VZCfEN9n0k1lco&q=85&s=f2717ab9417f4e134409e9f306134b01 840w, https://mintcdn.com/thundercompute/E4VZCfEN9n0k1lco/images/VSCode_Create_Snapshot.png?w=1100&fit=max&auto=format&n=E4VZCfEN9n0k1lco&q=85&s=8790736ea507473d25d12c3b5bba3782 1100w, https://mintcdn.com/thundercompute/E4VZCfEN9n0k1lco/images/VSCode_Create_Snapshot.png?w=1650&fit=max&auto=format&n=E4VZCfEN9n0k1lco&q=85&s=220d2d6d33192411d5f781e4d796918a 1650w, https://mintcdn.com/thundercompute/E4VZCfEN9n0k1lco/images/VSCode_Create_Snapshot.png?w=2500&fit=max&auto=format&n=E4VZCfEN9n0k1lco&q=85&s=38ff822d6d65957f18c989e5c51465d8 2500w" />

Snapshotting happens in the background—you can continue using your instance immediately. The snapshot captures the exact state at the moment you initiated it.

## View Snapshots

Your snapshots appear in the Thunder Compute panel below your instances.

## Restore from a Snapshot

1. Create a new instance.
2. Open the template menu.
3. Select your snapshot.

<img src="https://mintcdn.com/thundercompute/E4VZCfEN9n0k1lco/images/VSCode_Restore_Snapshot_New_Instance.png?fit=max&auto=format&n=E4VZCfEN9n0k1lco&q=85&s=79a524fd5d6dd50aeb251acd7c83ad87" alt="Step by step on restoring a snapshot" data-og-width="1400" width="1400" data-og-height="700" height="700" data-path="images/VSCode_Restore_Snapshot_New_Instance.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/thundercompute/E4VZCfEN9n0k1lco/images/VSCode_Restore_Snapshot_New_Instance.png?w=280&fit=max&auto=format&n=E4VZCfEN9n0k1lco&q=85&s=bab0679b68375af3339f47074ea8335d 280w, https://mintcdn.com/thundercompute/E4VZCfEN9n0k1lco/images/VSCode_Restore_Snapshot_New_Instance.png?w=560&fit=max&auto=format&n=E4VZCfEN9n0k1lco&q=85&s=4b7b5c97b02ba91068c32e828ccc8bfa 560w, https://mintcdn.com/thundercompute/E4VZCfEN9n0k1lco/images/VSCode_Restore_Snapshot_New_Instance.png?w=840&fit=max&auto=format&n=E4VZCfEN9n0k1lco&q=85&s=4e16e99404bcd2ac29f304f4abcdfd07 840w, https://mintcdn.com/thundercompute/E4VZCfEN9n0k1lco/images/VSCode_Restore_Snapshot_New_Instance.png?w=1100&fit=max&auto=format&n=E4VZCfEN9n0k1lco&q=85&s=d34136e9c5dc8cf78d971ae03a82709a 1100w, https://mintcdn.com/thundercompute/E4VZCfEN9n0k1lco/images/VSCode_Restore_Snapshot_New_Instance.png?w=1650&fit=max&auto=format&n=E4VZCfEN9n0k1lco&q=85&s=28d3e3a13d1e4f5621af8bfb43fb96f4 1650w, https://mintcdn.com/thundercompute/E4VZCfEN9n0k1lco/images/VSCode_Restore_Snapshot_New_Instance.png?w=2500&fit=max&auto=format&n=E4VZCfEN9n0k1lco&q=85&s=66c888861b4eafc89b0b9f9bd9c3ea30 2500w" />

<Note>
  Restoring from a snapshot can take up to 8 minutes per 100GB of data.
</Note>

## Delete a Snapshot

1. Open the Thunder Compute sidebar panel.
2. Right click the snapshot.
3. Select **Delete Snapshot**.

<img src="https://mintcdn.com/thundercompute/E4VZCfEN9n0k1lco/images/VSCode_Delete_Snapshot.png?fit=max&auto=format&n=E4VZCfEN9n0k1lco&q=85&s=cede99e16c9b5085c4eccd457017a7a0" alt="Step by step on deleting a snapshot" data-og-width="1400" width="1400" data-og-height="700" height="700" data-path="images/VSCode_Delete_Snapshot.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/thundercompute/E4VZCfEN9n0k1lco/images/VSCode_Delete_Snapshot.png?w=280&fit=max&auto=format&n=E4VZCfEN9n0k1lco&q=85&s=223c76f6db9c20276f930659715f2b3d 280w, https://mintcdn.com/thundercompute/E4VZCfEN9n0k1lco/images/VSCode_Delete_Snapshot.png?w=560&fit=max&auto=format&n=E4VZCfEN9n0k1lco&q=85&s=5499b9fdc552ed2b437b6a229eac7042 560w, https://mintcdn.com/thundercompute/E4VZCfEN9n0k1lco/images/VSCode_Delete_Snapshot.png?w=840&fit=max&auto=format&n=E4VZCfEN9n0k1lco&q=85&s=b3ce5b1281a150a69e513894e95cf3ee 840w, https://mintcdn.com/thundercompute/E4VZCfEN9n0k1lco/images/VSCode_Delete_Snapshot.png?w=1100&fit=max&auto=format&n=E4VZCfEN9n0k1lco&q=85&s=f9d819c7d3a028fb746d910cba4fc1ea 1100w, https://mintcdn.com/thundercompute/E4VZCfEN9n0k1lco/images/VSCode_Delete_Snapshot.png?w=1650&fit=max&auto=format&n=E4VZCfEN9n0k1lco&q=85&s=64a8d2f7c7fbfa0ab26e9bfd29b7b5b6 1650w, https://mintcdn.com/thundercompute/E4VZCfEN9n0k1lco/images/VSCode_Delete_Snapshot.png?w=2500&fit=max&auto=format&n=E4VZCfEN9n0k1lco&q=85&s=c692fe27597eb88c88edb339a2389da9 2500w" />

## Best Practices

1. **Name snapshots descriptively**: Include the project, date, or purpose (e.g., `llama-finetuned-jan2026`)

2. **Clean up unused snapshots**: To minimize your bill, remove snapshots you no longer need.

## Snapshots vs External Backups

Snapshots are great for quickly restoring your environment, but they’re meant for convenience rather than long-term data security. We do not provide explicit guarantees about snapshot durability. For long-term data preservation, consider using:

* **GitHub** for code and configuration
* **Local downloads** for important outputs
* **Cloud storage** (R2, Google Drive) for large files

To learn about optimizing the a snapshot for faster creation and restoration, refer to our [Speeding Up Snapshots](/guides/speeding-up-snapshots) guide.
