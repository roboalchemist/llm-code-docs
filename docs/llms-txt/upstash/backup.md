# Source: https://upstash.com/docs/redis/features/backup.md

# Backup/Restore

You can create a manual backup of your database and restore that backup to any of your databases. Both backup and restore operations require that your database is in one of the AWS regions.

Additionally, you can utilize the daily backup feature to automatically create backups of your database on a daily basis.

### Create A Manual Backup

To create a manual backup of your database:

* Go to the database details page and navigate to the `Backups` tab

<Frame>
  <img src="https://mintcdn.com/upstash/ZVIIe-nWA4-ORRYS/img/backuprestore/backuptab.png?fit=max&auto=format&n=ZVIIe-nWA4-ORRYS&q=85&s=0fc546f743bdb77b3e003f9cf1cbacf1" width="800" data-og-width="885" data-og-height="473" data-path="img/backuprestore/backuptab.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/upstash/ZVIIe-nWA4-ORRYS/img/backuprestore/backuptab.png?w=280&fit=max&auto=format&n=ZVIIe-nWA4-ORRYS&q=85&s=40895bfb6190be782e5c37724f5b4bf7 280w, https://mintcdn.com/upstash/ZVIIe-nWA4-ORRYS/img/backuprestore/backuptab.png?w=560&fit=max&auto=format&n=ZVIIe-nWA4-ORRYS&q=85&s=5e6fc8771720267e891aabdb02ec3232 560w, https://mintcdn.com/upstash/ZVIIe-nWA4-ORRYS/img/backuprestore/backuptab.png?w=840&fit=max&auto=format&n=ZVIIe-nWA4-ORRYS&q=85&s=a313cb647ee9a94d4a8467ab04f7f4b2 840w, https://mintcdn.com/upstash/ZVIIe-nWA4-ORRYS/img/backuprestore/backuptab.png?w=1100&fit=max&auto=format&n=ZVIIe-nWA4-ORRYS&q=85&s=87d10052079d834e213f7e3d8c131de6 1100w, https://mintcdn.com/upstash/ZVIIe-nWA4-ORRYS/img/backuprestore/backuptab.png?w=1650&fit=max&auto=format&n=ZVIIe-nWA4-ORRYS&q=85&s=dc5f3677bbaa816928eeb54ef8a90c1d 1650w, https://mintcdn.com/upstash/ZVIIe-nWA4-ORRYS/img/backuprestore/backuptab.png?w=2500&fit=max&auto=format&n=ZVIIe-nWA4-ORRYS&q=85&s=99cd36e9bc57f918800f2fcafda7a5cb 2500w" />
</Frame>

* Click on the `Backup` button and fill in a name for your backup. **Your backup name must be unique.**
* Then click on the `Create` button.

<Frame>
  <img src="https://mintcdn.com/upstash/ZVIIe-nWA4-ORRYS/img/backuprestore/backupmodal.png?fit=max&auto=format&n=ZVIIe-nWA4-ORRYS&q=85&s=bb329420779fd6700e45ca1733be4360" width="600" data-og-width="544" data-og-height="263" data-path="img/backuprestore/backupmodal.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/upstash/ZVIIe-nWA4-ORRYS/img/backuprestore/backupmodal.png?w=280&fit=max&auto=format&n=ZVIIe-nWA4-ORRYS&q=85&s=4719feb0fa4951f76798c3642af825dc 280w, https://mintcdn.com/upstash/ZVIIe-nWA4-ORRYS/img/backuprestore/backupmodal.png?w=560&fit=max&auto=format&n=ZVIIe-nWA4-ORRYS&q=85&s=457c88dd4e57f1d49fac8a5e4abf9eb6 560w, https://mintcdn.com/upstash/ZVIIe-nWA4-ORRYS/img/backuprestore/backupmodal.png?w=840&fit=max&auto=format&n=ZVIIe-nWA4-ORRYS&q=85&s=0fdd04b60d618a0957b80dae6dfb18e3 840w, https://mintcdn.com/upstash/ZVIIe-nWA4-ORRYS/img/backuprestore/backupmodal.png?w=1100&fit=max&auto=format&n=ZVIIe-nWA4-ORRYS&q=85&s=9e3d6db3afbdd708f35baf784797a876 1100w, https://mintcdn.com/upstash/ZVIIe-nWA4-ORRYS/img/backuprestore/backupmodal.png?w=1650&fit=max&auto=format&n=ZVIIe-nWA4-ORRYS&q=85&s=e08fc748f34f93ad5ddff1b930aa07c3 1650w, https://mintcdn.com/upstash/ZVIIe-nWA4-ORRYS/img/backuprestore/backupmodal.png?w=2500&fit=max&auto=format&n=ZVIIe-nWA4-ORRYS&q=85&s=4bf13ed7341fbc39dd697318a4b01f56 2500w" />
</Frame>

During the process of creating a backup for your database, it is important to note that your database will be temporarily locked, which means these operations will be unavailable during this time:

* Create Database Backup
* Enable TLS
* Move Database to Team
* Restore Database Backup
* Update Eviction
* Update Password
* Delete Database

<Frame>
  <img src="https://mintcdn.com/upstash/ZVIIe-nWA4-ORRYS/img/backuprestore/backupinprogressscreen.png?fit=max&auto=format&n=ZVIIe-nWA4-ORRYS&q=85&s=6d6c07d95ee5a7454e0c8e211c3476f6" width="800" data-og-width="1035" data-og-height="492" data-path="img/backuprestore/backupinprogressscreen.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/upstash/ZVIIe-nWA4-ORRYS/img/backuprestore/backupinprogressscreen.png?w=280&fit=max&auto=format&n=ZVIIe-nWA4-ORRYS&q=85&s=8718d6ddb01ae1f16244a96a826635be 280w, https://mintcdn.com/upstash/ZVIIe-nWA4-ORRYS/img/backuprestore/backupinprogressscreen.png?w=560&fit=max&auto=format&n=ZVIIe-nWA4-ORRYS&q=85&s=afb5b7fa562d7e68a77c24c5dc987a3b 560w, https://mintcdn.com/upstash/ZVIIe-nWA4-ORRYS/img/backuprestore/backupinprogressscreen.png?w=840&fit=max&auto=format&n=ZVIIe-nWA4-ORRYS&q=85&s=058397de1c75bd0ecf3114ca3158f4d6 840w, https://mintcdn.com/upstash/ZVIIe-nWA4-ORRYS/img/backuprestore/backupinprogressscreen.png?w=1100&fit=max&auto=format&n=ZVIIe-nWA4-ORRYS&q=85&s=00b83b578bb7e14455cf922f74677e73 1100w, https://mintcdn.com/upstash/ZVIIe-nWA4-ORRYS/img/backuprestore/backupinprogressscreen.png?w=1650&fit=max&auto=format&n=ZVIIe-nWA4-ORRYS&q=85&s=aa755c478c391a361dae3f622cd91227 1650w, https://mintcdn.com/upstash/ZVIIe-nWA4-ORRYS/img/backuprestore/backupinprogressscreen.png?w=2500&fit=max&auto=format&n=ZVIIe-nWA4-ORRYS&q=85&s=b802850bbf2152fde81d81c238a3b70b 2500w" />
</Frame>

### Restore A Backup

To restore a backup that was created from your current database, follow the steps below:

* Go to the database details page and navigate to the `Backups` tab
* Click on the `Restore` button next to the backup record listed.

<Frame>
  <img src="https://mintcdn.com/upstash/ZVIIe-nWA4-ORRYS/img/backuprestore/backuptabdailyenabled.png?fit=max&auto=format&n=ZVIIe-nWA4-ORRYS&q=85&s=40d627e5cd687455b0becbfae97eb3d3" width="800" data-og-width="1020" data-og-height="415" data-path="img/backuprestore/backuptabdailyenabled.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/upstash/ZVIIe-nWA4-ORRYS/img/backuprestore/backuptabdailyenabled.png?w=280&fit=max&auto=format&n=ZVIIe-nWA4-ORRYS&q=85&s=fd2de7c4f9b2f24473f74c9ac3cbe2f6 280w, https://mintcdn.com/upstash/ZVIIe-nWA4-ORRYS/img/backuprestore/backuptabdailyenabled.png?w=560&fit=max&auto=format&n=ZVIIe-nWA4-ORRYS&q=85&s=710f6de85d63d7961ff1dab81ea2ad59 560w, https://mintcdn.com/upstash/ZVIIe-nWA4-ORRYS/img/backuprestore/backuptabdailyenabled.png?w=840&fit=max&auto=format&n=ZVIIe-nWA4-ORRYS&q=85&s=2a7d5252b75242813deee6ee7a498bf6 840w, https://mintcdn.com/upstash/ZVIIe-nWA4-ORRYS/img/backuprestore/backuptabdailyenabled.png?w=1100&fit=max&auto=format&n=ZVIIe-nWA4-ORRYS&q=85&s=01fd05412906015fc7aa5e67d33ddb1c 1100w, https://mintcdn.com/upstash/ZVIIe-nWA4-ORRYS/img/backuprestore/backuptabdailyenabled.png?w=1650&fit=max&auto=format&n=ZVIIe-nWA4-ORRYS&q=85&s=11368f5f74aa1893e5979b4efec6ced1 1650w, https://mintcdn.com/upstash/ZVIIe-nWA4-ORRYS/img/backuprestore/backuptabdailyenabled.png?w=2500&fit=max&auto=format&n=ZVIIe-nWA4-ORRYS&q=85&s=e43725ecf184c2c75dd0c67637ff27b5 2500w" />
</Frame>

* Click on `Restore`. **Be aware of the fact that your target database will be flushed with this operation.**

<Frame>
  <img src="https://mintcdn.com/upstash/ZVIIe-nWA4-ORRYS/img/backuprestore/restorebackupfromcurrentdatabase.png?fit=max&auto=format&n=ZVIIe-nWA4-ORRYS&q=85&s=1965caef45339b88c3e0a208abce4366" width="700" data-og-width="724" data-og-height="523" data-path="img/backuprestore/restorebackupfromcurrentdatabase.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/upstash/ZVIIe-nWA4-ORRYS/img/backuprestore/restorebackupfromcurrentdatabase.png?w=280&fit=max&auto=format&n=ZVIIe-nWA4-ORRYS&q=85&s=bf7fec0c2a3051ab22af1f9e1e6800ea 280w, https://mintcdn.com/upstash/ZVIIe-nWA4-ORRYS/img/backuprestore/restorebackupfromcurrentdatabase.png?w=560&fit=max&auto=format&n=ZVIIe-nWA4-ORRYS&q=85&s=c3706c3b3d7e83be685a29724bc250dc 560w, https://mintcdn.com/upstash/ZVIIe-nWA4-ORRYS/img/backuprestore/restorebackupfromcurrentdatabase.png?w=840&fit=max&auto=format&n=ZVIIe-nWA4-ORRYS&q=85&s=bf0087e49e0347ffeea8d4921615f509 840w, https://mintcdn.com/upstash/ZVIIe-nWA4-ORRYS/img/backuprestore/restorebackupfromcurrentdatabase.png?w=1100&fit=max&auto=format&n=ZVIIe-nWA4-ORRYS&q=85&s=dd663f032b742a3003729670bb2e0d94 1100w, https://mintcdn.com/upstash/ZVIIe-nWA4-ORRYS/img/backuprestore/restorebackupfromcurrentdatabase.png?w=1650&fit=max&auto=format&n=ZVIIe-nWA4-ORRYS&q=85&s=1c57fd10f2dd39248e388d943e7a95ea 1650w, https://mintcdn.com/upstash/ZVIIe-nWA4-ORRYS/img/backuprestore/restorebackupfromcurrentdatabase.png?w=2500&fit=max&auto=format&n=ZVIIe-nWA4-ORRYS&q=85&s=d50832d92cfc592e40d26d267eb0cc78 2500w" />
</Frame>

### Restore A Backup From Another Database

To restore a backup that was created from one of your databases other than the current one, follow the steps below:

* Go to the database details page and navigate to the `Backups` tab
* Click on the `Restore...` button

<Frame>
  <img src="https://mintcdn.com/upstash/ZVIIe-nWA4-ORRYS/img/backuprestore/backuptabdailyenabled.png?fit=max&auto=format&n=ZVIIe-nWA4-ORRYS&q=85&s=40d627e5cd687455b0becbfae97eb3d3" width="800" data-og-width="1020" data-og-height="415" data-path="img/backuprestore/backuptabdailyenabled.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/upstash/ZVIIe-nWA4-ORRYS/img/backuprestore/backuptabdailyenabled.png?w=280&fit=max&auto=format&n=ZVIIe-nWA4-ORRYS&q=85&s=fd2de7c4f9b2f24473f74c9ac3cbe2f6 280w, https://mintcdn.com/upstash/ZVIIe-nWA4-ORRYS/img/backuprestore/backuptabdailyenabled.png?w=560&fit=max&auto=format&n=ZVIIe-nWA4-ORRYS&q=85&s=710f6de85d63d7961ff1dab81ea2ad59 560w, https://mintcdn.com/upstash/ZVIIe-nWA4-ORRYS/img/backuprestore/backuptabdailyenabled.png?w=840&fit=max&auto=format&n=ZVIIe-nWA4-ORRYS&q=85&s=2a7d5252b75242813deee6ee7a498bf6 840w, https://mintcdn.com/upstash/ZVIIe-nWA4-ORRYS/img/backuprestore/backuptabdailyenabled.png?w=1100&fit=max&auto=format&n=ZVIIe-nWA4-ORRYS&q=85&s=01fd05412906015fc7aa5e67d33ddb1c 1100w, https://mintcdn.com/upstash/ZVIIe-nWA4-ORRYS/img/backuprestore/backuptabdailyenabled.png?w=1650&fit=max&auto=format&n=ZVIIe-nWA4-ORRYS&q=85&s=11368f5f74aa1893e5979b4efec6ced1 1650w, https://mintcdn.com/upstash/ZVIIe-nWA4-ORRYS/img/backuprestore/backuptabdailyenabled.png?w=2500&fit=max&auto=format&n=ZVIIe-nWA4-ORRYS&q=85&s=e43725ecf184c2c75dd0c67637ff27b5 2500w" />
</Frame>

* Select the source database, referring to the database from which the backup was generated.
* Select the backup record that you want to restore to the current database.
* Click on `Start Restore`. **Be aware of the fact that your target database will be flushed with this operation.**

<Frame>
  <img src="https://mintcdn.com/upstash/ZVIIe-nWA4-ORRYS/img/backuprestore/restorebackupmodal.png?fit=max&auto=format&n=ZVIIe-nWA4-ORRYS&q=85&s=4fb9163488e04b207de89d4d0d4870e4" width="700" data-og-width="749" data-og-height="525" data-path="img/backuprestore/restorebackupmodal.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/upstash/ZVIIe-nWA4-ORRYS/img/backuprestore/restorebackupmodal.png?w=280&fit=max&auto=format&n=ZVIIe-nWA4-ORRYS&q=85&s=f52cc22791ec090798708d13465ad16c 280w, https://mintcdn.com/upstash/ZVIIe-nWA4-ORRYS/img/backuprestore/restorebackupmodal.png?w=560&fit=max&auto=format&n=ZVIIe-nWA4-ORRYS&q=85&s=c50177d4ae0a3c53a39c7c45738585c3 560w, https://mintcdn.com/upstash/ZVIIe-nWA4-ORRYS/img/backuprestore/restorebackupmodal.png?w=840&fit=max&auto=format&n=ZVIIe-nWA4-ORRYS&q=85&s=cf57a498a3e4d17f3e6779b86944fdf4 840w, https://mintcdn.com/upstash/ZVIIe-nWA4-ORRYS/img/backuprestore/restorebackupmodal.png?w=1100&fit=max&auto=format&n=ZVIIe-nWA4-ORRYS&q=85&s=706017a05bb4a68cd0fc73f153140135 1100w, https://mintcdn.com/upstash/ZVIIe-nWA4-ORRYS/img/backuprestore/restorebackupmodal.png?w=1650&fit=max&auto=format&n=ZVIIe-nWA4-ORRYS&q=85&s=6548fa295b5a642ba81da2b0369cf229 1650w, https://mintcdn.com/upstash/ZVIIe-nWA4-ORRYS/img/backuprestore/restorebackupmodal.png?w=2500&fit=max&auto=format&n=ZVIIe-nWA4-ORRYS&q=85&s=17132459f602a815c2e84287d2bccf5c 2500w" />
</Frame>

### Enable Daily Automated Backup

To enable daily automated backup for your database:

* Go to the database details page and navigate to the `Backups` tab

<Frame>
  <img src="https://mintcdn.com/upstash/ZVIIe-nWA4-ORRYS/img/backuprestore/backuptabwide.png?fit=max&auto=format&n=ZVIIe-nWA4-ORRYS&q=85&s=b2fe0e0e7f8b9b23b1ec5fd4c9df1807" width="800" data-og-width="1027" data-og-height="404" data-path="img/backuprestore/backuptabwide.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/upstash/ZVIIe-nWA4-ORRYS/img/backuprestore/backuptabwide.png?w=280&fit=max&auto=format&n=ZVIIe-nWA4-ORRYS&q=85&s=b6358222859407014b3931a248a9fc25 280w, https://mintcdn.com/upstash/ZVIIe-nWA4-ORRYS/img/backuprestore/backuptabwide.png?w=560&fit=max&auto=format&n=ZVIIe-nWA4-ORRYS&q=85&s=254173a5df25bbc628486c3277a4280a 560w, https://mintcdn.com/upstash/ZVIIe-nWA4-ORRYS/img/backuprestore/backuptabwide.png?w=840&fit=max&auto=format&n=ZVIIe-nWA4-ORRYS&q=85&s=f339443376b328e48b91df63e2471da0 840w, https://mintcdn.com/upstash/ZVIIe-nWA4-ORRYS/img/backuprestore/backuptabwide.png?w=1100&fit=max&auto=format&n=ZVIIe-nWA4-ORRYS&q=85&s=11518960f63853e01c45fdec391951af 1100w, https://mintcdn.com/upstash/ZVIIe-nWA4-ORRYS/img/backuprestore/backuptabwide.png?w=1650&fit=max&auto=format&n=ZVIIe-nWA4-ORRYS&q=85&s=af4eb4ebaf53473026d24f6834a3fd0a 1650w, https://mintcdn.com/upstash/ZVIIe-nWA4-ORRYS/img/backuprestore/backuptabwide.png?w=2500&fit=max&auto=format&n=ZVIIe-nWA4-ORRYS&q=85&s=24b3eeb6b2094a781be1087bf6a82d4d 2500w" />
</Frame>

* Enable the switch next to the `Daily Backup`
* Click on `Enable`

### Disable Daily Automated Backup

To disable the daily automated backup for your database, please follow the steps below:

* Go to the database details page and navigate to the `Backups` tab

<Frame>
  <img src="https://mintcdn.com/upstash/ZVIIe-nWA4-ORRYS/img/backuprestore/backuptabdailyenabled.png?fit=max&auto=format&n=ZVIIe-nWA4-ORRYS&q=85&s=40d627e5cd687455b0becbfae97eb3d3" width="800" data-og-width="1020" data-og-height="415" data-path="img/backuprestore/backuptabdailyenabled.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/upstash/ZVIIe-nWA4-ORRYS/img/backuprestore/backuptabdailyenabled.png?w=280&fit=max&auto=format&n=ZVIIe-nWA4-ORRYS&q=85&s=fd2de7c4f9b2f24473f74c9ac3cbe2f6 280w, https://mintcdn.com/upstash/ZVIIe-nWA4-ORRYS/img/backuprestore/backuptabdailyenabled.png?w=560&fit=max&auto=format&n=ZVIIe-nWA4-ORRYS&q=85&s=710f6de85d63d7961ff1dab81ea2ad59 560w, https://mintcdn.com/upstash/ZVIIe-nWA4-ORRYS/img/backuprestore/backuptabdailyenabled.png?w=840&fit=max&auto=format&n=ZVIIe-nWA4-ORRYS&q=85&s=2a7d5252b75242813deee6ee7a498bf6 840w, https://mintcdn.com/upstash/ZVIIe-nWA4-ORRYS/img/backuprestore/backuptabdailyenabled.png?w=1100&fit=max&auto=format&n=ZVIIe-nWA4-ORRYS&q=85&s=01fd05412906015fc7aa5e67d33ddb1c 1100w, https://mintcdn.com/upstash/ZVIIe-nWA4-ORRYS/img/backuprestore/backuptabdailyenabled.png?w=1650&fit=max&auto=format&n=ZVIIe-nWA4-ORRYS&q=85&s=11368f5f74aa1893e5979b4efec6ced1 1650w, https://mintcdn.com/upstash/ZVIIe-nWA4-ORRYS/img/backuprestore/backuptabdailyenabled.png?w=2500&fit=max&auto=format&n=ZVIIe-nWA4-ORRYS&q=85&s=e43725ecf184c2c75dd0c67637ff27b5 2500w" />
</Frame>

* Disable the switch next to the `Daily Backup`
* Click on `Disable`

<Frame>
  <img src="https://mintcdn.com/upstash/ZVIIe-nWA4-ORRYS/img/backuprestore/dailybackupdisablemodal.png?fit=max&auto=format&n=ZVIIe-nWA4-ORRYS&q=85&s=c0246bd6bb8a3c5e9f383040f7159586" width="700" data-og-width="732" data-og-height="523" data-path="img/backuprestore/dailybackupdisablemodal.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/upstash/ZVIIe-nWA4-ORRYS/img/backuprestore/dailybackupdisablemodal.png?w=280&fit=max&auto=format&n=ZVIIe-nWA4-ORRYS&q=85&s=28e5517e8292179ae735e2cf8afc7c50 280w, https://mintcdn.com/upstash/ZVIIe-nWA4-ORRYS/img/backuprestore/dailybackupdisablemodal.png?w=560&fit=max&auto=format&n=ZVIIe-nWA4-ORRYS&q=85&s=5be3d9a160c2948f115c26943888ea27 560w, https://mintcdn.com/upstash/ZVIIe-nWA4-ORRYS/img/backuprestore/dailybackupdisablemodal.png?w=840&fit=max&auto=format&n=ZVIIe-nWA4-ORRYS&q=85&s=1f321710a754b10b81d6e358ae3f3bf3 840w, https://mintcdn.com/upstash/ZVIIe-nWA4-ORRYS/img/backuprestore/dailybackupdisablemodal.png?w=1100&fit=max&auto=format&n=ZVIIe-nWA4-ORRYS&q=85&s=e314a836e10bbbd1d3589e263ba97754 1100w, https://mintcdn.com/upstash/ZVIIe-nWA4-ORRYS/img/backuprestore/dailybackupdisablemodal.png?w=1650&fit=max&auto=format&n=ZVIIe-nWA4-ORRYS&q=85&s=fc66da756cff1b257542eb9232c8a7e3 1650w, https://mintcdn.com/upstash/ZVIIe-nWA4-ORRYS/img/backuprestore/dailybackupdisablemodal.png?w=2500&fit=max&auto=format&n=ZVIIe-nWA4-ORRYS&q=85&s=9b96d510c5249fa2c392641d2964dc20 2500w" />
</Frame>
