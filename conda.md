## 1. Environments
### What is an environment?
Just a 'box' (a directory, really) where you can safely install Python flavors of choice (2.X, 3.X) and packages. 

### Why would I want to use environments?
* You can install and use as many flavors of Python 2.X and Python 3.X on the same machine without conflicts.
* Avoid conflicts where you need different versions of a package (e.g., numpy) for different projects you are working on.
* Easily share your environment (Python version and all dependencies) with other people so they can run your awesome scripts without:
  * breaking their current Python setup, or 
  * requiring them to manually install packages they are missing.

### Multiple environment management tools
* pip virtualenv (Python 2.X) or pip venv (Python 3.X)
* pipenv
* Conda, which is what we will use

### Why Conda?
* It's what I know :-)
* Not limited to Python (this is useful to us in terms of being able to use PDAL command line applications)


## 2. Install Conda
### Check if already installed
* Look for **Anaconda Prompt** in your programs

### If not installed
* Download and install [Miniconda](https://docs.conda.io/en/latest/miniconda.html)
* Launch **Anaconda Prompt**
* You will need to add a few items to your PATH if you want to use Conda in the standard Command Prompt, similar to these:
  * `C:\Users\prest\Miniconda2`
  * `C:\Users\prest\Miniconda2\Scripts`


## 3. Using Conda
* The default "base" environment
  * Note that there is a default environment named "base"
  * You can see that the base environment is active because `(base)` precedes the directory at the prompt
  * Don't install stuff in your base environment
* Create a new environment with the latest version of Python
  * `conda create --name my_environment Python=3`
  * `conda create -n my_environment Python=3`
* Activate an environment
  * `conda activate my_environment`
  * Note how `(my_environment)` now precedes the directory name at the prompt:
```
C:\dev\python\conda-pdal-tech-talk>conda activate

(base) C:\dev\python\conda-pdal-tech-talk>conda activate pdal-tech-talk

(pdal-tech-talk) C:\dev\python\conda-pdal-tech-talk>
```

* List all your environments (in case you forget their names)
  * `conda env list`, or
  * `conda info --env`
* Delete an environment
  * `conda remove -n my_environment --all`
* Update conda
  * conda will occasionally let you know it is out of date
  * activate the base environment and `conda update conda`
* More info [here](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)
  

## 4. Installing packages into your environment
* Remember not to install packages in your (base) environment. 
* I find it easiest to first activate the environment in which I want to modify packages, and then install a package:
  * `conda activate my_environment`
  * `conda install numpy` (numpy used as the example package)
* To install a package into an environment different than the current active environment you need to specify the environment name: `conda install -n different_environment numpy`
* Install a package from a non-default "channel": `conda install -c conda-forge pdal-python`
* List installed packages: `conda list`
* Delete a package: `conda remove numpy`
* More info [here](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-pkgs.html)


## 5. Sharing an environment with a colleague
* You:
  * Create a file that specs your environment: `conda env export > awesome_environment.yml`
  * Send the "awesome_environment.yml" file to your colleague
* Colleague:
  * Navigate to the directory where I saved the "awesome_environment.yml" file and run `conda env create -f awesome_environment.yml`
  * Activate the new environment with `conda activate awesome_environment`
  * I can now run your awesome script without worrying about breaking my Python or package installations due to different versions


## Notes from a MATLAB user on using a Command Prompt for Python
* Being "in" and "out" of Python
* When you run a script from the prompt, nothing remains when you are done (all the variables have vaporized)
  * Look into Jupyter notebook, Spyder, PyCharm (?) if you want a more "MATLAB" type of experience