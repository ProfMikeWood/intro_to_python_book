# Installing Python and Jupyter

## Download Miniconda
There are many ways to install python for use on your machine. One of the most popular ways is to use Anaconda - a distribution of Python designed for data science. Anaconda contains many programs that may not be applicable to your application. Miniconda, on the other hand, is a paired-down version of Anaconda that allows you to install new modules as you need them. As a result, it takes up far less storage on your machine. Miniconda will include Python (the programming language) and conda (the package manager).

To download Miniconda, navigate to https://docs.conda.io/en/latest/miniconda.html and choose a Conda Installer that pertains to your system. For Windows machines, the majority of machines are 64-bit. For MacOS, choose the pkg file which pertains to your chip (see [HERE](https://support.apple.com/en-us/HT211814)).


## Set up a conda environment
After you have downloaded miniconda, set up a conda environment. Begin by opening up a terminal of your choice. On Windows, you can open the "Anaconda Prompt" application by searching for it in the start menu. On Mac, you can open a standard Terminal in the Applications/Utilities directory. 

With your terminal open, create a conda environment called cs122 with Python version 3.11 using the following command:

```
conda create --name cs122 python=3.11
```
By default, conda will automatically activate a "base" environment on your machine. To disable this behavior, you may want to run the following:
```
conda config --set auto_activate_base false
```

Now, activate your environment as follows:
```
conda activate cs122
```

Every time you use your environment, you will need to activate it from the command line.

Next, download the pertinent modules required for this course:

```
conda install numpy
conda install matplotlib
```

Finally, configure your environment to use in a jupyter notebook. 

On machine running MacOS use:

```
python3 -m ipykernel install --user --name=cs122
```

On Windows, use:
```
python -m ipykernel install --user --name=cs122
```



