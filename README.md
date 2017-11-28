# Datalab ML Training

## Objectives
The goals of this training is to:
- Get you excited about Data Science
- Give a quick introduction for some of the Python's libraries available: Pandas (data wrangling), Scikit-learn (ML), Matplotlib (visualisation)
- Give a quick overview of an approach to tackling Data Science problems

It will not:
- Make you an expert Data Scientist
- Go into details (or do the maths) for the techniques / algorithms we will use
- Properly cover any deep learning / neural networks

## Getting Ready
This course is delivered using Jupyter Notebooks so if you're not familiar with them some helpful documentation is [What is the Jupyter Notebook?](http://jupyter-notebook-beginner-guide.readthedocs.io/en/latest/what_is_jupyter.html) and [Notebook Basics](http://jupyter-notebook.readthedocs.io/en/stable/examples/Notebook/Notebook%20Basics.html).
The notebooks contain Python code which you will run during the exercises; this is done by highlighting the cell then
clicking `Run` in Jupyter. Bear in mind that this code should be executed in order and each cell should complete before running the next cell.
This training also uses Python 3 and a number of Python libraries, so before starting the training you will need to:
- Install Python 3 following the [Python Beginners Guide](https://wiki.python.org/moin/BeginnersGuide/Download) or you might find [Installing Python 3 on Mac OS X](http://docs.python-guide.org/en/latest/starting/install3/osx/) useful if you use Mac OS X.
- Install [Virtualenv](https://virtualenv.pypa.io) using the [Installation](https://virtualenv.pypa.io/en/stable/installation/) documentation.
- In your project directory create a new virtual environment by running `virtualenv -p python3.6 env`
- Enable your virtual environment by running `source env/bin/activate`
- Install the dependencies by running `pip3 install -r requirements.txt` which will install:
  - *Jupyter* - This will give you an interactive programming environment that runs in the browser
  - *scikit-learn* - This will provide you with powerful and easy to use machine learning algorithms
  - *pandas* - This will give you a powerful way of handling dataframes
  - *numpy* - This gives you access to scientific computing capability
  - *scipy* - Similar to Numpy, it gives you access to key mathematical functions
  - *matplotlib* - This will be used for plotting
- Alternatively, you can install [Anaconda](https://www.anaconda.com/download/#macos) which aims to simplify package management or follow the [Using Docker](#using-docker) instructions below.
- Download the dataset used in these exercises [iplayer_data_sample_janapr2017.csv.zip](https://storage.googleapis.com/datalab-datasets/iplayer_data_sample_janapr2017.csv.zip). (This file is approximately 40mb in size and is a direct link so will start to download immediately).
- Unzip the dataset and ensure it is named `iplayer_data_sample_janapr2017.csv` and in the project directory with the training notebooks.
- Finally, in order to start your development environment, type `jupyter notebook` in your terminal. This should automatically open a tab in your browser or you can visit [localhost:8888](http://localhost:8888/). To shut down Jupyter type `ctrl + c`.
- When you are finished with the training you can run `deactivate` to deactivate your virtualenv.

### Using Docker
If you are familiar with Docker, you can use the Jupyter [`datascience-notebook`](https://hub.docker.com/r/jupyter/datascience-notebook/) image to spin up everything you need for the course. As a starting point, the following command creates a passwordless instance of Jupyter at http://localhost:8888/, mapped to your current working directory:

```bash
docker run \
    -d --rm -p 127.0.0.1:8888:8888 \
    --name=datascience-notebook \
    --mount type=bind,source="$(pwd)",target=/home/jovyan \
    jupyter/datascience-notebook \
    start-notebook.sh --NotebookApp.token=''
```

## Agenda
The training is split into 4 courses:
- [One: Data Exploration](iPlayerForecast_course1.ipynb)
- [Two: Data Preparation](iPlayerForecast_course2.ipynb)
- [Three: Build a Classifier](iPlayerForecast_course3.ipynb)
- [Four: Build a Regressor](iPlayerForecast_course4.ipynb)

This training is still work-in-progress. Please send us any feedback to `datalab@bbc.co.uk` to help us improve it!
