#!/bin/bash

cp CppCoreGuidelines.md temp
sed "s/{{/{{\"{{\"}}/" temp > CppCoreGuidelines.md
