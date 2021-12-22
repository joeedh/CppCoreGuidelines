import os, io

ENCODING = "utf8"

with io.open("build/CppCoreGuidelines.md.indexed", "r", encoding=ENCODING) as readfile:
    buf = readfile.read()

buf = buf.replace("{{", "{{  \"{{\"  }}")
with io.open("../CppCoreGuidelines.md", "w", encoding=ENCODING) as writefile:
    writefile.write(buf)
