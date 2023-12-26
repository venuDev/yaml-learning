import yaml
import os
from pathlib import Path

import argparse
 
def get_files(filetype:str):
    return [ k.name for k in Path.cwd().glob(f'*.{filetype}')]


def show_yaml(file_name:str):
    
    with open(file_name,'r') as yml_file:
        try:
            yml_content=yaml.safe_load(yml_file)
            print('\nYAML Content\t:')
            # print(yaml.dump(yml_content,default_flow_style=False))
            print(yml_content)
        except yaml.YAMLError as e:
            print(e)

def main(filename:str):
    print(filename)

if __name__=="__main__":
    # parser = argparse.ArgumentParser(description="YMAL Parser & View",
    #                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    # parser.add_argument("filename", help="YAML File")
    # args = parser.parse_args()
    # config = vars(args)
    file_list=get_files('yaml')
    print('Please select YAML File # you want to view:')
    while True:
        for i,k in enumerate(file_list,1):
            print(f'{i}\t{k}')
        file_selection=input("Enter File Index you would like to View or Any other Key to Exist:\t")
        if not file_selection.isdigit():
            break
        file_index =int(file_selection)-1
        if 0<=file_index<len(file_list):
            show_yaml(file_list[file_index])
        else:
            print('Invalid Selection Please try agin')
