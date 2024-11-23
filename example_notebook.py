# Databricks notebook source

import uv_wheel.example_module
import yaml
from IPython.display import display

settings = {
    "key": "value"
}

print(yaml.dump(settings))

df = uv_wheel.example_module.example_function()
display(df)
