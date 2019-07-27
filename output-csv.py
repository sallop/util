#!/usr/bin/env python

# see also: https://docs.python.org/3.6/library/fileformats.html
#           https://docs.python.org/3.6/library/json.html
#           https://gist.github.com/alswl/eee052f75437445e67f91feac335dc0e

import sys
import os
import subprocess
import json

malformed_json = "malformed.json"

lines = []
with open(malformed_json, 'r') as fr:
    lines = fr.readlines()

print("malformed_json = {0}".format(lines))

# lines = "\n".join([ln.strip() for ln in lines])
lines = [ln.strip() for ln in lines]

# malformed json
# malformed_jsonstr = """
# All Work and No Play Makes Jack a Dull Boy
# All Work and No Play Makes Jack a Dull Boy
# All Work and No Play Makes Jack a Dull Boy
# {
#   "foo": 1,
#   "bar": 2,
#   "baz": 3
# }
# """
# lines = malformed_jsonlines.split('\n')

print("invalid json file")
for i, ln in enumerate(lines):
    print(i, ln)

# eliminate lines
print("eliminate line")
jsonlines = lines[4:]
for i, ln in enumerate(jsonlines):
    print(i, ln)

jsonstr = "".join([ln.strip() for ln in jsonlines])

print(jsonstr)
print(json.dumps(jsonstr, indent=4))

# "{ }".format("foo.json")
# jqp = subprocess.Popen(["jq"])
# jqp = subprocess.Popen(["jq", "'.'"])
# jqp = subprocess.Popen(["jq", ".", "foo.json"])
jqp = subprocess.Popen(["jq", ".baz", "foo.json"], stdout=subprocess.PIPE)
# jqp = subprocess.Popen(["jq", "'.'" "foo.json"])
stdout = jqp.communicate()[0]
# output_json = json.loads('[' + stdout.replace('\n', ',')[:-1] + ']')
# output_json = json.loads('[' + stdout.replace('\n', ',')[:-1] + ']')
output_json = json.loads(stdout) # dictionary
jsonstr = json.dumps(output_json)

print(output_json)
print(jsonstr)

# json.loads('{}')
# json.dumps('')

fname = "output.csv"
#fname = sys.argv[1]
# 
with open(fname, 'w') as fw:
    # fw.writelines(output_json)
    fw.write(jsonstr)
    fw.write("\n")
    fw.write(jsonstr)

# # "start excel"
# #subprocess.poen()
# subprocess.run(["libreoffice", "--calc", fname])
