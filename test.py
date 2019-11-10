import parso

print(parso.parse('from dir.file import func1, func2').children[0].children)
print(parso.parse('load("dir/file.py", "func1", "func2")').children[0].children)
