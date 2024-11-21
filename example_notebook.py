# Databricks notebook source

import uv_wheel.example_module
import yaml

settings = {
    "key": "value"
}

print(yaml.dump(settings))

df = uv_wheel.example_module.example_function()
