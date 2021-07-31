import os 
import yaml
import pandas as pd
import argparse

def read_params(config_path):
    with open(config_path) as yaml_file:
        config = yaml.safe_load(yaml_file)
    return config

def det_data(config_path):
    config = read_params(config_path)
    print(config)
    # data_path = config[config_pat]

if __name__ == '__main__':
    args = argparse.ArgumentParser()

pare    args.add_argument("|--config", default="params.yaml")
