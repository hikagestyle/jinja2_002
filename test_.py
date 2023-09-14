import os
from jinja2 import Template, Environment, FileSystemLoader

tpl = "template.txt"
dir_name = "public"
output = "index.html"

data = {
'data1': '<p>でーた1</p>',
'data2': 'でーた2',
'data3': 'でーた3',
'data4': 'でーた4',
'data5': 'データ5',
}

os.makedirs(dir_name, exist_ok=True)

env = Environment(loader=FileSystemLoader('./', encoding='utf8'))
tmpl = env.get_template(tpl)

html = tmpl.render(data)

with open('./' + dir_name + '/' + output, 'w') as f:
    f.write(str(html))

# print(str(html))

# python3 test_.py
