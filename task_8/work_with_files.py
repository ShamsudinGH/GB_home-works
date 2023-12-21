import os
import json
import csv
import pickle

def size_get(path):
    object_size = 0
    for root, dirs, files in os.walk(path):
        for f in files:
            object_size += os.path.getsize(os.path.join(root, f))
    return object_size

def directory_walker(dir_path):
    finaly_list = []
    for root, dirs, files in os.walk(dir_path):
        for f_name in files:
            path_f_size = os.path.join(root, f_name)
            finaly_list.append({'parent_dir': root,
                                'is_file': True,
                                'size': os.path.getsize(path_f_size)}
                               )
        for d_name in dirs:
            path_f_size = os.path.join(root, d_name)
            finaly_list.append({'parent_dir': root,
                                'is_file': False,
                                'size': size_get(path_f_size)})

        with open('result.json', 'w', encoding='UTF-8') as jf:
            json.dump(finaly_list, jf, ensure_ascii=False, indent=2)

        with open('result.csv', 'w', encoding='UTF-8') as cf:
            writer = csv.DictWriter(cf, fieldnames=finaly_list[0].keys())
            writer.writeheader()
            writer.writerows(finaly_list)

        with open("output.pickle", "wb") as pf:
            pickle.dump(finaly_list, pf)

directory_walker(os.getcwd())