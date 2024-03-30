#!/usr/bin/env python3

import os

def skip_venv_dir():
    current_dir_files = os.listdir()
    venv = ['bin', 'include', 'lib']
    resp = []
    for dir in venv:
        if dir in current_dir_files:
            resp.append(True)
    filter_resp = set(resp)
    return list(filter_resp)

def dir_checker():
    final_list = []
    venv_check = skip_venv_dir()
    if venv_check:
        print('parent::::')
        final_list.append(os.getcwd())
    for item in os.listdir():
        if not os.path.isfile(item):
            current_dir = os.getcwd()
            os.chdir(os.path.join(current_dir, item))
            venv_check2 = skip_venv_dir()
            if venv_check2:
                print('child::::')
                final_list.append(os.getcwd())
            else:
                final_list.extend(dir_checker())
            os.chdir(current_dir)
    final_list = [i.split('/')[-1] for i in final_list] + ['.git']
    return list(set(final_list))
                
                
if __name__ == '__main__':
    result = dir_checker()
    print('final list:', result)
    print()
    print('list of venvs')
    for i, j in enumerate(result):
        print(f'{i+1}. {j}')
    # print('Venvs: %s' % result)
