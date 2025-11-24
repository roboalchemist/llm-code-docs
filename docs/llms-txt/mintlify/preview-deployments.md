# Source: https://mintlify.com/docs/deploy/preview-deployments.md

# Preview deployments

> Get unique preview URLs for pull requests to review changes before merging.

<Info>
  Preview deployments are available on [Pro and Custom plans](https://mintlify.com/pricing?ref=preview-deployments).
</Info>

Preview deployments let you see how changes to your docs will look before merging to production. Each preview creates a shareable URL that updates automatically as you push new changes.

Preview URLs are publicly viewable by default. Share a preview link with anyone who needs to review your changes.

## Create preview deployments

Preview deployments are created automatically through pull requests or manually from your dashboard.

### Automatic previews

When you create a pull request, the Mintlify bot automatically adds a link to view the preview deployment in your pull request. The preview updates each time you push new commits to the branch.

<Frame>
  <img src="https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/previews/preview-deployment-light.png?fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=4cbf574001b521afbd8c9f6717ed907f" alt="Link to view deployment in the pull request timeline" className="block dark:hidden" data-og-width="1704" width="1704" data-og-height="142" height="142" data-path="images/previews/preview-deployment-light.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/previews/preview-deployment-light.png?w=280&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=ffa4ba05f4e3f34bd5ad947743959df2 280w, https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/previews/preview-deployment-light.png?w=560&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=a87ea5b13d3444849a8fab4a43a5fc22 560w, https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/previews/preview-deployment-light.png?w=840&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=1ce1ff2e47b42af3db49c2394f8837f2 840w, https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/previews/preview-deployment-light.png?w=1100&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=f6b44ca1a53080b2d8b8252784aec487 1100w, https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/previews/preview-deployment-light.png?w=1650&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=bd5d0e2d7721005d6d7740a96a996ff5 1650w, https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/previews/preview-deployment-light.png?w=2500&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=e217516260f683cf2417a7ef75e8db8a 2500w" />

  <img src="https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/previews/preview-deployment-dark.png?fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=9fbb5054761316d1bbb8168646ed51bf" alt="Link to view deployment in the pull request timeline" className="hidden dark:block" data-og-width="1704" width="1704" data-og-height="142" height="142" data-path="images/previews/preview-deployment-dark.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/previews/preview-deployment-dark.png?w=280&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=e7b687ed13f8af142c95a89815b42498 280w, https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/previews/preview-deployment-dark.png?w=560&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=ebabc65e5a7fc6852d7c94632119f96a 560w, https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/previews/preview-deployment-dark.png?w=840&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=6ca64fb1d342b667c40a1b7cee5f13f6 840w, https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/previews/preview-deployment-dark.png?w=1100&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=24a0e64ff92331d88950db41a9240409 1100w, https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/previews/preview-deployment-dark.png?w=1650&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=fc090479eb70d57448ad26bf279f8b3a 1650w, https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/previews/preview-deployment-dark.png?w=2500&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=50f581e8856cb179d142197218c956cc 2500w" />
</Frame>

### Manual previews

You can manually create a preview for any branch.

1. Go to your [dashboard](https://dashboard.mintlify.com/).
2. Select **Previews**.
3. Select **Create custom preview**.
4. Enter the name of the branch you want to preview.
5. Select **Create deployment**.

## Redeploy a preview

Redeploy a preview to refresh content or retry after a failed deployment.

1. Select the preview from your [dashboard](https://dashboard.mintlify.com/).
2. Select **Redeploy**.

<Frame>
  <img src="https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/previews/redeploy-preview-light.png?fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=eaa1711b0c580931036f1d1f4685312e" alt="The Previews menu with the deploy button emphasized by an orange rectangle." className="block dark:hidden" data-og-width="2104" width="2104" data-og-height="634" height="634" data-path="images/previews/redeploy-preview-light.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/previews/redeploy-preview-light.png?w=280&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=8e14a4269e5e49c5f58704cfb9c7c3ee 280w, https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/previews/redeploy-preview-light.png?w=560&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=f982b0d0dbb6615c83b1a370e832e22e 560w, https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/previews/redeploy-preview-light.png?w=840&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=bcc1ac87bc01dbd392c2fed61ac977d7 840w, https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/previews/redeploy-preview-light.png?w=1100&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=636df2e9155b22989c03e222db33227a 1100w, https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/previews/redeploy-preview-light.png?w=1650&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=c65406f8131b395506026be9f46dc646 1650w, https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/previews/redeploy-preview-light.png?w=2500&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=1e193e05303626f9c5ea4a03986a33bf 2500w" />

  <img src="https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/previews/redeploy-preview-dark.png?fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=086e0340522fc6a620e47e3e35703ae2" alt="The Previews menu with the deploy button emphasized by an orange rectangle." className="hidden dark:block" data-og-width="2104" width="2104" data-og-height="634" height="634" data-path="images/previews/redeploy-preview-dark.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/previews/redeploy-preview-dark.png?w=280&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=4b646047473c193d3b112a622da00369 280w, https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/previews/redeploy-preview-dark.png?w=560&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=5b1cd268146f7799d9a52e9a960b86bf 560w, https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/previews/redeploy-preview-dark.png?w=840&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=0b1b451fd93ed8c27815db88e77e9daf 840w, https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/previews/redeploy-preview-dark.png?w=1100&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=57d3acd1587110a80bf80ed4d0b23f24 1100w, https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/previews/redeploy-preview-dark.png?w=1650&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=d05748dbe4b8008f53fcc2da6ec3cde7 1650w, https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/previews/redeploy-preview-dark.png?w=2500&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=d084422d4921243da615209a1d92eb89 2500w" />
</Frame>

## Restrict access to preview deployments

By default, preview deployments are publicly accessible to anyone with the URL. You can restrict access to authenticated members of your Mintlify organization.

1. Navigate to the **Previews** section in the [Add-ons](https://dashboard.mintlify.com/products/addons) page of your dashboard.
2. Click the **Preview authentication** toggle to enable or disable preview authentication.

<Frame>
  <img src="https://mintcdn.com/mintlify/JpjPdD_YybFKEYPk/images/previews/preview-auth-light.png?fit=max&auto=format&n=JpjPdD_YybFKEYPk&q=85&s=efbbd50e1a18d29953f17fb8a9d7138b" alt="The preview authentication toggle in the Add-ons page" className="block dark:hidden" data-og-width="1460" width="1460" data-og-height="434" height="434" data-path="images/previews/preview-auth-light.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/JpjPdD_YybFKEYPk/images/previews/preview-auth-light.png?w=280&fit=max&auto=format&n=JpjPdD_YybFKEYPk&q=85&s=0dae11b2586092c797b01bbf904b0509 280w, https://mintcdn.com/mintlify/JpjPdD_YybFKEYPk/images/previews/preview-auth-light.png?w=560&fit=max&auto=format&n=JpjPdD_YybFKEYPk&q=85&s=147721d67152841c352ad17910b26219 560w, https://mintcdn.com/mintlify/JpjPdD_YybFKEYPk/images/previews/preview-auth-light.png?w=840&fit=max&auto=format&n=JpjPdD_YybFKEYPk&q=85&s=807fe277f064e120724fe57c4c181b24 840w, https://mintcdn.com/mintlify/JpjPdD_YybFKEYPk/images/previews/preview-auth-light.png?w=1100&fit=max&auto=format&n=JpjPdD_YybFKEYPk&q=85&s=967903ae94c4e0f307093d3f9f6f7462 1100w, https://mintcdn.com/mintlify/JpjPdD_YybFKEYPk/images/previews/preview-auth-light.png?w=1650&fit=max&auto=format&n=JpjPdD_YybFKEYPk&q=85&s=a6c0d7a59f269fd541ea09fcb0da4929 1650w, https://mintcdn.com/mintlify/JpjPdD_YybFKEYPk/images/previews/preview-auth-light.png?w=2500&fit=max&auto=format&n=JpjPdD_YybFKEYPk&q=85&s=d748446589d44923c0939117db10d04d 2500w" />

  <img src="https://mintcdn.com/mintlify/JpjPdD_YybFKEYPk/images/previews/preview-auth-dark.png?fit=max&auto=format&n=JpjPdD_YybFKEYPk&q=85&s=b5d877ae3918afcd852a8047eab98233" alt="The preview authentication toggle in the Add-ons page" className="hidden dark:block" data-og-width="1460" width="1460" data-og-height="434" height="434" data-path="images/previews/preview-auth-dark.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/JpjPdD_YybFKEYPk/images/previews/preview-auth-dark.png?w=280&fit=max&auto=format&n=JpjPdD_YybFKEYPk&q=85&s=0068da77b2e3323216fbdca747d4cf43 280w, https://mintcdn.com/mintlify/JpjPdD_YybFKEYPk/images/previews/preview-auth-dark.png?w=560&fit=max&auto=format&n=JpjPdD_YybFKEYPk&q=85&s=24f7e4fd385ed7685c3ed1f8beb0cfd7 560w, https://mintcdn.com/mintlify/JpjPdD_YybFKEYPk/images/previews/preview-auth-dark.png?w=840&fit=max&auto=format&n=JpjPdD_YybFKEYPk&q=85&s=649097e668c184de9d2fd10b6471dcbe 840w, https://mintcdn.com/mintlify/JpjPdD_YybFKEYPk/images/previews/preview-auth-dark.png?w=1100&fit=max&auto=format&n=JpjPdD_YybFKEYPk&q=85&s=2909b16edc1aaf5b92f5eb734581f21d 1100w, https://mintcdn.com/mintlify/JpjPdD_YybFKEYPk/images/previews/preview-auth-dark.png?w=1650&fit=max&auto=format&n=JpjPdD_YybFKEYPk&q=85&s=0ce6ee48959b1002fdba61540d24cf0e 1650w, https://mintcdn.com/mintlify/JpjPdD_YybFKEYPk/images/previews/preview-auth-dark.png?w=2500&fit=max&auto=format&n=JpjPdD_YybFKEYPk&q=85&s=d9d85ef0277ff064155f2a95b2ff8a34 2500w" />
</Frame>
