# AUTOGENERATED! DO NOT EDIT! File to edit: 03_retrieval.ipynb (unless otherwise specified).

__all__ = ['get_data', 'make_url_key', 'RESOURCE']

# Cell
from .discovery import DataSet
from .base import ISTAT
import pandas as pd
import io
from fastcore.test import *
from nbdev import *

# Cell
RESOURCE = "data"
# TODO: accept json response as well (?)


def get_data(dataset: DataSet, **kwargs):
    "returns a dataframe of the filitered 'dataset'"
    flowRef = dataset.identifiers["df_id"]
    filters = dataset.filters
    key = make_url_key(filters)
    path_parts = [RESOURCE, flowRef, key]
    path = "/".join(path_parts)
    request = ISTAT()
    response = request._request(path, headers={"Accept": "text/csv"})
    df = pd.read_csv(io.StringIO(response.text))

    if "TIME_PERIOD" in df.columns:
        df["TIME_PERIOD"] = pd.to_datetime(
            df["TIME_PERIOD"], infer_datetime_format=True
        )
        df = df.sort_values(by=["TIME_PERIOD"])

    return df


def make_url_key(filters: dict):
    key = ""

    for i, filter_tuple in enumerate(filters.items()):

        filter = filter_tuple[0]
        filter_value = filter_tuple[1]

        # add a + and convert to str
        if type(filter_value) == list:
            filter_value = "+".join(filter_value)

        if i != 0:
            if list(filters.values())[i - 1] != ".":
                filter_value = "." + filter_value

        key += filter_value

    return key