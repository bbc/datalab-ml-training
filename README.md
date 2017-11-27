# datalab-ml-training

## Objectives
The goals of this training is to:
- Get you excited about Data Science
- Give a quick introduction for some of the Python's libraries available: Pandas (data wrangling), Scikit-learn (ML), Matplotlib (visualisation)
- Give a quick overview of an approach to tackling Data Science Problems

We will not:
- Make you an expert Data Scientist
- Go into details (or do the maths) for the techniques / algorithms we will use
- Properly cover any deep learning / neural networks

## Getting ready
Before starting the training be sure to:
- Have the elevated access rights to be able to install softwares
- Install Python 3
  - Download it from here: https://www.python.org/ftp/python/3.6.1/python-3.6.1-macosx10.6.pkg
  - Then run in the following in your terminal:
    - pip3 install Jupyter - This will give you an interactive programming environment that runs in the browser (and created this notebook)
    - pip3 install scikit-learn - This will provide you with powerful and easy to use machine learning algorithms
    - pip3 install pandas - This will give you a powerful way of handling dataframes
    - pip3 install numpy - This gives you access to scitific computing capability
    - pip3 install scipy - Similar to Numpy, it gives you access to key mathematical functions
    - pip3 install matplotlib - This will be used for plotting
  - Alternatively, you can also install Anaconda (https://www.anaconda.com/download/#macos) that aims to simplify package management.
- Finally, in order to start your developing environment, type Jupyter Notebook in your terminal. This should open a tab in your browser

### Using Docker

Jupyter also provide a Docker image that runs everything you need for these exercises. If you have Docker, this command creates a passwordless instance of Jupyter at http://localhost/, mapped to your current working directory:

```bash
docker run \
    -d --rm -p 127.0.0.1:80:8888 \
    --name=datascience-notebook \
    --mount type=bind,source="$(pwd)",target=/home/jovyan \
    jupyter/datascience-notebook \
    start-notebook.sh --NotebookApp.token=''
```

## Agenda
The training is split in 4 courses:
- Course One: Data Exploration
- Course Two: Data Preparation
- Course Three: Build a Classifier
- Course Four: Build a Regressor

This training is still WIP. Please give us any feedback to help us improve it!
