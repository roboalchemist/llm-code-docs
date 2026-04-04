# Source: https://help.cloudsmith.io/docs/recycle-bin.md

# Recycle Bin

Temporary storage for deleted artifacts

The repository recycle bin allows you to store deleted artifacts pending permanent deletion.

You can also restore artifacts to the repository from the Recycle Bin. This can be useful in cases of accidental artifact deletion or when evaluating/configuring [Artifact Lifecycle](https://help.cloudsmith.io/docs/retention-lifecycle) rules.

> 📘 Early Access Feature
>
> The Recycle Bin is currently an early access feature. If you would like to try this feature, please [Contact Us](https://help.cloudsmith.io/docs/contact-us).

> 🚧 Artifact Retention
>
> Artifacts in the recycle bin are retained for a 2 week period and then are automatically deleted.

# Restore an Artifact

To restore an artifact from the Recycle Bin, click the orange "Perform Actions" button and then click "Restore":

<Image alt="Restore an artifact from the Recycle Bin" align="center" src="https://files.readme.io/3c588a7-recycle-bin-restore.png">
  Restore an artifact
</Image>

You then need to confirm that you wish to restore the artifact:

<Image alt="Restore Confirmation" align="center" width="75% " border={true} src="https://files.readme.io/cc4f39b-recycle-bin-restore-confirmation.png">
  Restore Confirmation
</Image>

Click the blue "Restore" button to restore the artifact to the repository.

# Restore multiple artifacts

To restore multiple artifacts from the Recycle Bin, select all or just the specific artifacts you wish to restore, then click the blue "Restore Package" button.

<Image alt="Restore multiple artifacts" align="center" src="https://files.readme.io/4f72713-recycle-bin-restore-multiple.png">
  Restore multiple artifacts
</Image>

By setting the artifact count to "100 per page" you can restore up to 100 artifacts at once using this method.

You then need to confirm that you wish to restore the artifacts:

<Image align="center" className="border" width="75% " border={true} src="https://files.readme.io/4cef609-Screenshot_2024-07-26_at_11.21.31.png" />

Click the blue "Restore" button to restore the selected artifacts to the repository.

# Permanently Delete an Artifact

To permanently remove an artifact from the Recycle Bin, click the orange "Perform Actions" button and then click "Delete":

<Image align="center" src="https://files.readme.io/b29925f-recycle-bin-delete.png" />

You then need to confirm that you wish to permanently delete the artifact:

<Image align="center" className="border" width="75% " border={true} src="https://files.readme.io/f6d126e-recycle-bin-delete-confim.png" />

<br />

Click "Delete" to permanently delete the artifact from the Recycle Bin. The artifact can no longer be restored to the repository.