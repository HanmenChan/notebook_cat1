import json
import sys

#handle argument exceptions 抛出异常
if len(sys.argv) < 3:
    raise Exception('参数数量必须大于 2！')

#accept argument list 接受变量
notebook_path_lst = sys.argv[1:]

cells_lst = []
target_notebook = {}
#读取 path list

for path in notebook_path_lst:
    with open(path) as notebook:
        notebook_str = notebook.read()
        notebook_json = json.loads(notebook_str)
        cells = notebook_json['cells']
        del notebook_json['cells']
        cells_lst += (cells)

target_notebook['cells'] = cells_lst
target_notebook.update(notebook_json)
target_str = json.dumps(target_notebook)
with open('target_notebook.ipynb','w') as target:
    target.write(target_str)


'''
notebook1 = open(notebook_path1)
notebook1_str = notebook1.read()
notebook1_json = json.loads(notebook1_str)

cells1 = notebook1_json['cells']

notebook2 = open(notebook_path2)
notebook2_str = notebook2.read()
notebook2_json = json.loads(notebook2_str)

cells2 = notebook2_json['cells']

del notebook1_json['cells']


#拼接
target_cells  cells1 + cells2

target_notebook = {}

target_notebook['cells'] = target_cells
target_notebook.update(notebook1_json)

target_str = json.dumps(target_notebook)

target = open('target_notebook.ipynb','w')
target.write(target_str)
'''