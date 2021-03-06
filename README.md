# ISTATAPI
> Python API wrapper for ISTAT (The Italian National Institute of Statistics)


`istatapi` is a Python interface to discover and retrieve data from ISTAT API (The Italian National Institute of Statistics). The library is designed to explore ISTAT metadata and to retreive data in different formats. `istatapi` is built on top of [ISTAT SDMX RESTful API](https://developers.italia.it/it/api/istat-sdmx-rest).

Whether you are an existing organization, a curious individual or an academic researcher, `istatapi` aims to allow you to easily access ISTAT databases with just a few lines of code. The library implements functions to:

* Explore all available ISTAT datasets (dataflows in SDMX terminology)
* Search available datasets by keywords
* Retrieve information on a specific dataset like: the ID of the dataflow, the names and available values of the dimensions of the dataset, available filters.
* Get data of an available dataset in a pandas DataFrame, csv or json format.

## Install

You can easily install the library by using the pip command:

`pip install istatapi`

## How to use
