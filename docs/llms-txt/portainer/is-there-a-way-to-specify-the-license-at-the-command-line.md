# Source: https://docs.portainer.io/2.33-lts/faqs/licensing/is-there-a-way-to-specify-the-license-at-the-command-line.md

# Source: https://docs.portainer.io/sts/faqs/licensing/is-there-a-way-to-specify-the-license-at-the-command-line.md

# Source: https://docs.portainer.io/faqs/licensing/is-there-a-way-to-specify-the-license-at-the-command-line.md

# Is there a way to specify the license at the command line?

You can use the \`PORTAINER\_LICENSE\_KEY\` environment variable. &#x20;

For example:

<pre><code><strong>docker run -d -p 8000:8000 -p 9443:9443 --name portainer --restart=always -e "PORTAINER_LICENSE_KEY="&#x3C;license key here>" -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer-ee:latest
</strong></code></pre>
