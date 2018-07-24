import json



#读取
notebook1 = open('1.ipynb')
notebook1_str = notebook1.read()
notebook1_json = json.loads(notebook1_str)

cells1 = notebook1_json['cells']

notebook2 = open('2.ipynb')
notebook2_str = notebook2.read()
notebook2_json = json.loads(notebook2_str)

cells2 = notebook2_json['cells']

#拼接
cells = cells1 + cells2

cells_json = json.dumps(cells)

target = open('target_notebook.ipynb','w')
target.write(cells_json)
