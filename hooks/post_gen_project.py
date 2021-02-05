# Copyright (c) 2021 Microsoft
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

import os
import shutil

def remove(filepath):
    if os.path.isfile(filepath):
        os.remove(filepath)
    elif os.path.isdir(filepath):
        shutil.rmtree(filepath)    


include_goodbye = "{{cookiecutter.include_goodbye}}" == "True"

if not include_goodbye:
    remove(os.path.join(os.getcwd(), 'code/goodbye'))