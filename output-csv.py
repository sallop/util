#!/usr/bin/env python

# see also: https://docs.python.org/3.6/library/fileformats.html
#           https://docs.python.org/3.6/library/json.html

import sys
import os
import subprocess
import json

# malformed_jsonfile = "malformed_json.txt"
# with open(malformed_jsonfile, 'r') as fr:
#     fr.write('hello world,\n')
#     fr.write('next line,\n')
#     fr.write('and next,\n')


#
# malformed json
malformed_jsonstr = """
All Work and No Play Makes Jack a Dull Boy
All Work and No Play Makes Jack a Dull Boy
All Work and No Play Makes Jack a Dull Boy
{
  "foo": 1,
  "bar": 2,
  "baz": 3
}
"""


lines = malformed_jsonstr.split('\n')
for i, ln in enumerate(lines):
    print(i, ln)

# eliminate lines
jsonlines = lines[4:9]
for i, ln in enumerate(jsonlines):
    print(i, ln)

jsonstr = "".join([ln.strip() for ln in jsonlines])

print(jsonstr)
print(json.dumps(jsonstr, indent=4))

# "{ }".format("foo.json")
jqp = subprocess.Popen(["jq"])
# jqp = subprocess.Popen(["jq", "'.'"])
# jqp = subprocess.Popen(["jq", "'.'" "foo.json"])
stdout = jqp.communicate()[0]

# json.loads('{}')
# json.dumps('')

# fname = sys.argv[1]
# 
# print(fname)
# 
# with open(fname, 'w') as fw:
#     for ln in jsonstr:
#         fw.write(ln)
# 
# # "start excel"
# #subprocess.poen()
# subprocess.run(["libreoffice", "--calc", fname])
