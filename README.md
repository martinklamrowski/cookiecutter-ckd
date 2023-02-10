# Cookiecutter CKD

Spork of: [cookiecutter-data-science](http://drivendata.github.io/cookiecutter-data-science/).

_A very niche template for kick-starting Chronic Kidney Disease analyses._


#### [Project Homepage](https://www.goodreads.com/book/show/24445517-maybe-someday)


### Requirements to use the cookiecutter template:
-----------
 - Python 2.7 or 3.5+
 - [Cookiecutter Python package](http://cookiecutter.readthedocs.org/en/latest/installation.html) >= 1.4.0: This can be installed with pip by or conda depending on how you manage your Python packages:

``` bash
$ pip install cookiecutter
```

or

``` bash
$ conda config --add channels conda-forge
$ conda install cookiecutter
```


### To start a new project, run:
------------

    cookiecutter https://github.com/martinklamrowski/cookiecutter-ckd


[![asciicast](https://asciinema.org/a/244658.svg)](https://asciinema.org/a/244658)

### New version of Cookiecutter Data Science
------------
Cookiecutter data science is moving to v2 soon, which will entail using
the command `ccds ...` rather than `cookiecutter ...`. The cookiecutter command
will continue to work, and this version of the template will still be available.
To use the legacy template, you will need to explicitly use `-c v1` to select it.
Please update any scripts/automation you have to append the `-c v1` option (as above),
which is available now.


### The resulting directory structure
------------

The directory structure of your new project looks like this: 

```
├── LICENSE
├── Makefile           <- Makefile with commands like `make data` or `make train`.
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── public         <- Publicly available datasets. Populated with some samples by default.
│   └── confidential   <- Confidential patient data. Explicitly marked for no oopsies.
│       ├── interim    <- Intermediate data that has been transformed.
│       ├── versioned  <- Versioned datasets for specific analyses.
│       └── source     <- The original, immutable data dump(s).
│
├── docs               <- A default Sphinx project; see sphinx-doc.org for details.
│
├── models             <- Frozen and serialized models.
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `1.0-jqp-initial-data-exploration`.
│
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting.
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`.
│
├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
├── src                <- Source code for use in this project.
│   ├── __init__.py    <- Makes src a Python module.
│   │
│   ├── data           <- Scripts to download or generate data.
│   │   └── make_dataset.py
│   │
│   ├── features       <- Scripts to turn raw data into features for modeling.
│   │   └── build_features.py
│   │
│   ├── models         <- Scripts to train models and then use trained models to make
│   │   │                 predictions.
│   │   ├── predict_model.py
│   │   └── train_model.py
│   │
│   └── visualization  <- Scripts to create exploratory and results oriented visualizations.
│       └── visualize.py
│
└── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io.
```

## Contributing

This template is a work in progress.

TODOs:
- Drop Python 2.
- Utils.
- Public dataset pulls.
- ...and more.

### Installing development requirements
------------

    pip install -r requirements.txt

### Running the tests
------------

    py.test tests
