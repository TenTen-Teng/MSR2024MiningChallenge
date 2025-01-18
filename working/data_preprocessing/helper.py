# Helper functions to load JSON data automatically.

import os
import pandas as pd
import json

def read_filepaths(folder_dir, target_json):
    if not os.path.isdir(folder_dir):
        raise FileExistsError("Input a vaild folder directory.")
    
    if target_json.lower() not in [
        "hn", "pr", "issue", "discussion", "commit", "file"
        ]:
        raise ValueError(
            "Input a target from 'hn', 'pr', 'issue', 'discussion', 'commit' \
                or 'file'"
            )

    files = os.listdir(folder_dir)
    file_paths = []
    for file in files:
        if target_json in file:
            file_paths.append(os.path.join(folder_dir, file))
        
    return file_paths


def load_dataframes(file_paths):
    df = pd.DataFrame()
    for file in file_paths:
        date = file.split("_")[-4][:8]

        with open(file, "r") as file:
            dict = json.load(file)
        
        df_tmp = pd.json_normalize(dict["Sources"]) 

        df_tmp["source_date"] = date
        df = pd.concat([df, df_tmp])
    return df

