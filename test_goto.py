import parso

# load("lib2.py", "CoolFunc")
source = '''
from lib2 import  CoolFunc

CoolFunc()
'''

print(parso.parse(source).children[1].children[0].children[0].get_definition())
