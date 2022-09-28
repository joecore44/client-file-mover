import os
from pathlib import Path
import shutil
from os.path import splitext

# You can move this directory around if you aren't using this for the /downloads folder
BLOATED_DIR = f'{Path.home()}/Downloads'


def is_file(file:str) -> bool:
    return os.path.isfile(f'{BLOATED_DIR}/{file}')

def get_extension(file:str) -> str:
    return splitext(file)[1]
    
def get_unique_file_extensions(files:list) -> dict:
    suffix = '_downloads'
    extension_dict = {'unknown':'unknown_downloads'}
    for object in files:
        if is_file(object):
            file_ext = get_extension(object)
            if file_ext not in extension_dict and file_ext != '':
                extension_dict[file_ext] = file_ext + suffix
                # Make sure to grab files without extensions
    return extension_dict
            

def create_directories(ext_dict:dict) -> None:
    for dir_name in ext_dict.values():
        extension_dir = f'{BLOATED_DIR}/{dir_name}'
        if not os.path.isdir(extension_dir):
            os.mkdir(extension_dir)

def move_files_to_directory(download_dir_objects:list, ext_dict:dict) -> None:
    for object in download_dir_objects:
        curr_dir = f'{BLOATED_DIR}/{object}'
        file_ext = None
        extension_dir = None

        if is_file(object):
            file_ext = get_extension(object)

        if file_ext == '' or file_ext is None:
            extension_dir = ext_dict['unknown']
        else:
            extension_dir = ext_dict[file_ext]
        
        final_dir = f'{BLOATED_DIR}/{extension_dir}/{object}'

        shutil.move(curr_dir,final_dir)
 
if __name__ == '__main__':
    objectects_in_download_folder = os.listdir(BLOATED_DIR)
    ext_dict = get_unique_file_extensions(objectects_in_download_folder)

    create_directories(ext_dict)
    move_files_to_directory(objectects_in_download_folder, ext_dict)
