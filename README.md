# BBC Datalab ML Training

## Objectives
The goals of this training is to:
- Get you excited about Data Science
- Give a quick introduction for some of the Python's libraries available: Pandas (data wrangling), Scikit-learn (ML), Matplotlib (visualisation)
- Give a quick overview of an approach to tackling Data Science problems

It will not:
- Make you an expert Data Scientist
- Go into details (or do the maths) for the techniques / algorithms we will use
- Properly cover any deep learning / neural networks

## Setting Up Your Environment
This course is delivered using Jupyter Notebooks so if you're not familiar with them some helpful documentation is [What is the Jupyter Notebook?](http://jupyter-notebook-beginner-guide.readthedocs.io/en/latest/what_is_jupyter.html) and [Notebook Basics](http://jupyter-notebook.readthedocs.io/en/stable/examples/Notebook/Notebook%20Basics.html).
The notebooks contain Python code which you will run during the exercises; this is done by highlighting the cell then
clicking `Run` in Jupyter. Bear in mind that this code should be executed in order and each cell should complete before running the next cell.

## Dependencies
This training requires a number of libraries which are installed, for example, with `pip3`. These libraries are:
- [Jupyter](http://jupyter.org/) - An interactive programming environment that runs in the browser.
- [scikit-learn](http://scikit-learn.org/) - Powerful and easy-to-use machine learning algorithms.
- [pandas](https://pandas.pydata.org/) - A powerful way of handling dataframes which are two-dimensional tabular data structures with labeled axes.
- [numpy](http://www.numpy.org/) - Scientific computing capability providing support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays.
- [scipy](https://www.scipy.org/) - Similar to Numpy, it gives you access to key mathematical modules such as optimization, linear algebra, integration, and interpolation, etc
- [matplotlib](https://matplotlib.org/) - A plotting library for the Python programming language and NumPy.

### Jupyter with Virtualenv
This training also uses Python 3 and a number of Python libraries, so before starting the training you will need to:
- Install Python 3 following the [Python Beginners Guide](https://wiki.python.org/moin/BeginnersGuide/Download) or you might find [Installing Python 3 on Mac OS X](http://docs.python-guide.org/en/latest/starting/install3/osx/) useful if you use Mac OS X.
- Install [Virtualenv](https://virtualenv.pypa.io) using the [Installation](https://virtualenv.pypa.io/en/stable/installation/) documentation.
- In your project directory create a new virtual environment by running `virtualenv -p python3.6 env`
- Enable your virtual environment by running `source env/bin/activate`
- Install the [dependencies](#dependencies) by running `pip3 install -r requirements.txt`
- Finally, in order to start your development environment, type `jupyter notebook` in your terminal. This should automatically open a tab in your browser or you can visit [localhost:8888](http://localhost:8888/). To shut down Jupyter type `ctrl + c`.
- When you are finished with the training you can run `deactivate` to deactivate your virtualenv.

### Jupyter with Docker
If you are familiar with Docker, you can use the Jupyter [`datascience-notebook`](https://hub.docker.com/r/jupyter/datascience-notebook/) image to spin up everything you need for the course. As a starting point, the following command creates a passwordless instance of Jupyter at http://localhost:8888/, mapped to your current working directory:

```bash
docker run \
    -d --rm -p 127.0.0.1:8888:8888 \
    --name=datascience-notebook \
    --mount type=bind,source="$(pwd)",target=/home/jovyan \
    jupyter/datascience-notebook \
    start-notebook.sh --NotebookApp.token=''
```

### Jupyter with Anaconda
Alternatively, you can install [Anaconda](https://www.anaconda.com/download/#macos) which aims to simplify package management.

## Agenda
The training is split into 4 courses:
- [One: Data Exploration](iPlayerForecast_course1.ipynb)
- [Two: Data Preparation](iPlayerForecast_course2.ipynb)
- [Three: Build a Classifier](iPlayerForecast_course3.ipynb)
- [Four: Build a Regressor](iPlayerForecast_course4.ipynb)

This training is still work-in-progress. Please send us any feedback to `datalab @ bbc.co.uk` to help us improve it!

**And if you found this training easy and had fun doing it, why not join us? https://findouthow.datalab.rocks/** 
