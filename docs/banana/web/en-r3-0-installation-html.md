# Source: https://banana.readthedocs.io/en/r3.0/installation.html

Title: Installation — Banana 2.0 documentation

URL Source: https://banana.readthedocs.io/en/r3.0/installation.html

Markdown Content:
Requirements[¶](https://banana.readthedocs.io/en/r3.0/installation.html#requirements "Permalink to this headline")
------------------------------------------------------------------------------------------------------------------

Banana depends on various 3rd party Python libraries which are defined in the **requirements.txt** file. You can install the dependencies using [pip](http://pip.readthedocs.org/):

$ pip install astropy
$ pip install -r requirements.txt

Pip cant figure out dependencies correctly in some cases, so you need to manually install astropy first.

Quick configuration[¶](https://banana.readthedocs.io/en/r3.0/installation.html#quick-configuration "Permalink to this headline")
--------------------------------------------------------------------------------------------------------------------------------

copy the example config file:

$ cp project/settings/local_example.py project/settings/local.py

Now open `project.settings.local` in your favorite editor and configure your database settings.

Runnig the server[¶](https://banana.readthedocs.io/en/r3.0/installation.html#runnig-the-server "Permalink to this headline")
----------------------------------------------------------------------------------------------------------------------------

You can run a Django testing webserver serving the banana project using:

$ ./manage.py runserver

Deployment[¶](https://banana.readthedocs.io/en/r3.0/installation.html#deployment "Permalink to this headline")
--------------------------------------------------------------------------------------------------------------

If you want a more permanent implementation and serve Banana so several users it is adviced to deploy your setup with a dedicated webserver. The Django project itself has [extended documentation](https://docs.djangoproject.com/en/1.6/howto/deployment/) on how to do this.
