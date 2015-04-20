#Python for Data Analysis and Visualisation

[NIWA](http://www.niwa.co.nz), Wellington, Wednesday 22 and Thursday 23 April 2015

Contact:

Nicolas Fauchereau

+ [@gmail](mailto:Nicolas.Fauchereau@gmail.com)
+ [@niwa](mailto:Nicolas.Fauchereau@niwa.co.nz)

<hr size=5>

### Table of contents

- [The Anaconda python distribution](#the-anaconda-python-distribution)
- [Installation of Some additional libraries](#installation-of-additional-libraries)
  - [Basemap](#basemap)
  - [Bokeh](#bokeh)
  - [Seaborn](#seaborn)
  - [mplD3](#mplD3)
  - [bearcart](#bearcart)
  - [folium](#folium)
- [Running the IPython notebooks](#running-the-ipython-notebooks)
- [Troubleshooting](#troubleshooting)

<hr size=5>

## The Anaconda python distribution

For this tutorial, I **strongly** recommend installing the **Anaconda Python distribution**. It is a completely free enterprise-ready Python distribution for large-scale data processing, predictive analytics, and scientific computing. It includes the python interpreter itself, the python standard library as well as a set of packages exposing data structures and methods for data manipulation and scientific computing and visualization. In particular it provides [Numpy](http://www.numpy.org/), [Scipy](http://www.scipy.org/), [Pandas](http://pandas.pydata.org/), [Matplotlib](http://matplotlib.org/), [scikit-learn](http://scikit-learn.org/stable/) and [statmodels](http://statsmodels.sourceforge.net/), i.e. all the main packages we will be using during the tutorial. The full list of packages is available at:

[http://docs.continuum.io/anaconda/pkgs.html](http://docs.continuum.io/anaconda/pkgs.html)

The Anaconda python distribution must be downloaded from:

[http://continuum.io/downloads](http://continuum.io/downloads)

For your platform.

Once you have installed Anaconda, you can update to the latest compatible versions of all the pre-installed packages by running:

```
$ conda update conda
```

Then

```
$ conda update anaconda
```

In a terminal.

You also need to install [pip](https://github.com/pypa/pip) to install packages from the [Python Package Index](http://pypi.python.org/pypi).

```
$ conda install pip
```

## Installation of additional libraries

### Basemap

**Basemap** is a graphic library for plotting (static, publication quality) geographical maps (see [http://matplotlib.org/basemap/](http://matplotlib.org/basemap/)). **Basemap** is available directly in **Anaconda** using the conda package manager, install with:

```
$ conda install basemap
```

### Bokeh

[Bokeh]() is a new interactive plotting library developed by the team behind **anaconda**: it is thus installable with conda (if not already installed):

```
$ conda install bokeh
```

### Seaborn

[seaborn](http://web.stanford.edu/~mwaskom/software/seaborn/) is a Python visualization library based on matplotlib. It provides a high-level interface for drawing attractive statistical graphics. You should be able to install it with ```conda``` as well:

```
$ conda install seaborn
```

### mplD3

[mplD3](http://mpld3.github.io/) aims at *bringing matplotlib to the browser*. It has been developed by Jake VanDerPlas. It is installable using ```pip```:

```
$ pip install mpld3
```

### bearcart

[bearcart](https://github.com/wrobstory/bearcart) has been developed by [Rob Story](http://wrobstory.github.io/) and provides an interface to the rickshaw JavaScript library. It is also installable via ```pip```:

```
$ pip install bearcart
```

### folium

[folium](https://github.com/wrobstory/folium)  has been also been developed by [Rob Story](http://wrobstory.github.io/) to provide an interface to the [leaflet.js](http://leafletjs.com/) JavaScript mapping library. Install with:

```
$ pip install folium
```

<hr size=5>

## Running the IPython notebooks

The material of the tutorial is in the form of [IPython notebooks](http://ipython.org/notebook.html). In a nutshell an IPython notebook is a web-based (i.e. running in the browser) interactive computational environment where you can combine Python code execution, text, mathematics, plots and rich media into a single document, which makes it an ideal medium for teaching and exploring code.


After uncompressing the archive of the repo (or after cloning it with ```git```), navigate to the corresponding directory (containing the ```*.ipynb``` files) and type:

```
$ ipython notebook
```

That should bring up the IPython notebook dashboard (looking as below), you should be ready to go !

![](https://github.com/nicolasfauchereau/Python-for-data-analysis-and-visualisation/blob/master/session_1/notebooks/images/ipython_dashboard.png)

You should see in particular a ```test.ipynb``` notebook: please run it to make sure all the necessary libraries have been installed correctly. If you followed the instructions above (install the [anaconda python distribution](http://continuum.io/downloads)) it should be fine, this test notebook is mostly intended for those who have a *custom* python installation.

## Troubleshooting

You might run into some problems installing additional libraries via `conda` or `pip` and / or running the IPython notebooks, especially on Windows machines behind a proxy, here are a few solutions that may work:

**1. Proxy settings for conda:**

create a `.condarc` file (the '.' is important) in your HOME directory (on windows it should be `C:\Users\YOU`) and add the following lines:

```
proxy_servers:
    http: http://url:port
    https: http://url:port
```  

**2. specify proxy when using pip**

If you are running into issues installing libraries via pip, try specifying the proxy to use at the command line, e.g.

```
pip install --proxy=http://url:port bearcart
```

**3. Set-up system-wide proxy settings**

+ On Macs: in your `${HOME}/.bash_profile`, insert these lines

```
export http_proxy=http://url:port
export https_proxy=http://url:port

```

+ On Linux machines, do the same as above in your `${HOME}/.bashrc`

+ On Windows machines:

  + As an administrator go to `Control Panel | System | Advanced Systems Settings | Advanced Tab | Environment Variables | System Variables | New` and set

  ```
  HTTP_PROXY=http://url:port/
  HTTPS_PROXY=https://url:port/
  ```

  + You can also do that in a command window by typing (the `$` represents the prompt)

  ```
  $ SET HTTP_PROXY=http://url:port/
  $ SET HTTPS_PROXY=http://url:port/
  ```

**4. use Firefox instead of internet explorer to open the notebooks**

  The IPython notebook is an interactive web-based 'notebook', where executable python code can be weaved with rich comments, graphic outputs etc, which make it ideal for presenting interactive tutorials. When (in a command prompt) you navigate to the directory where you have downloaded the notebooks and type (the $ sign represent the prompt):

  ```
  $ ipython notebook
  ```

  a 'dashboard' with the list of notebooks should come up in your browser ... now if you are on windows, chances are that your default browser is Internet Explorer, which is generally bad news. If you encounter problems (blank page, notebooks not loading, kernel interruptions etc), it's probably because of Internet Explorer. What I suggest is that you download Firefox for windows and make it the default browser to open IPython notebooks. To do that you need (once firefox is installed) to do the following :

  i) in a command prompt type (again $ is the prompt):

  ```
  $ ipython profile create default
  ```

  it should create a bunch of configuration files in the following directory:

  ```
  C:\Users\YOU\.ipython\profile_default
  ```

  go and edit the `ipython_notebook_config.py` file

  search for the line

  ```
  #c.NotebookApp.browser =''
  ```

  and replace it by:

  ```
  import webbrowser
  webbrowser.register('firefox', None, webbrowser.GenericBrowser('C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe'))
  c.NotebookApp.browser = 'firefox'
  ```

**5. Specify localhost when calling the IPython notebook**

On some configurations, you might also need to call:

```
$ ipython notebook --ip=127.0.0.1
```

To specify that the browser should connect to *localhost*

**6. Clear the cache**

If you are still running into issues (notably dashboard or IPython notebook not displaying correctly), try clearing the cache of your browser

**7. Use an `incognito` window**

If all else fails (!), one thing that has been reported working is:

+ launch the `ipython notebook` in no-browser mode:

```
ipython notebook --no-browser
```

You should see an output in the terminal looking like:

```
...
The IPython Notebook is running at: http://localhost:8888/
...
```

Note that the URL and port could be different in your case.

Open an `incognito` window from your browser and copy the URL (`http://localhost:8888/`) in the address bar
