# -*- coding: utf-8 -*-
"""
Created on Sun Apr  1 10:21:16 2018
"""

import os
import shutil

root_dir_names = ['train', 'test']

for root_dir_name in root_dir_names:
    root_dir = './{}'.format(root_dir_name)
    sub_dirs = os.listdir(root_dir)
    for sub_dir in sub_dirs:
        f_list_path = os.path.join(root_dir, sub_dir)
        f_list = os.listdir(f_list_path)
        f_list.sort()
        if f_list:
            sum = int(len(f_list) / 150)
            for i in range(sum):
                f_list_new_path = (f_list_path + '_{:0>1d}').format(i + 1)
                if not os.path.exists(f_list_new_path):
                    os.mkdir(f_list_new_path)
            temp = 1
            for idx, f_name in enumerate(f_list):
                f_path = os.path.join(f_list_path, f_name)
                if sub_dir[:2] == 'LD':
                    os.rename(f_path, os.path.join(f_list_path,
                                                   'LD_' + sub_dir[3:5] + '.{:0>4d}.jpg'.format(idx + 1)))

for root_dir_name in root_dir_names:
    root_dir = './{}'.format(root_dir_name)
    sub_dirs = os.listdir(root_dir)
    for sub_dir in sub_dirs:

        f_list_path = os.path.join(root_dir, sub_dir)
        f_list = os.listdir(f_list_path)
        f_list.sort()
        if f_list:
            temp = 1
            for idx, f_name in enumerate(f_list):
                f_path = os.path.join(f_list_path, f_name)
                boundry = temp * 150 - 1
                if idx > boundry and idx <= (boundry + 150):
                    new_f_name = os.path.join(
                        (f_list_path + '_{:0>1d}').format(temp),
                        (f_name[:5] + '_{:0>1d}.{:0>4d}.jpg').format(temp,
                                                                     idx - 150 * temp + 1))
                    shutil.move(f_path, new_f_name)
                if idx == (boundry + 150):
                    temp += 1


