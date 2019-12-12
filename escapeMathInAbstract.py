#!/usr/bin/env python3
import sys, io, os, re

isInAbstract = False

def _lineIsInAbstract(line):
    global isInAbstract    
    if not isInAbstract:
        if re.search(r"[Aa]bstract\s*=\s*\{", line):      
            isInAbstract = True
    else:
        if re.search(r"\},|\S+\s*=\s*\{", line):
            isInAbstract = False
    return isInAbstract

def _escapeInAbstract(line):
    currentLine = line
    if _lineIsInAbstract(currentLine):
        # Escape backslashes
        currentLine = re.sub(r"\\(?<!\\)(?!%|\&|\\)", r"\\\\", currentLine)
        # Escape dollar signs
        currentLine = re.sub(r"\$(.*?)\$", r"\\\$latex \1\\\$", currentLine)
    return currentLine

if __name__ == '__main__':
    inputFileName = sys.argv[1]
    outputFileName = sys.argv[2]

    inputFile = io.open(inputFileName, mode="r", encoding="utf-8")
    outputFile = io.open(outputFileName, mode="w", encoding="utf-8")

    for line in inputFile:
        updatedLine = _escapeInAbstract(line)
        outputFile.write(updatedLine + os.linesep)

