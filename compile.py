#!/usr/bin/python3
#
# compile.py - Compile the input Tex file.

import os, sys, glob, subprocess


def _call_pdflatex(file_name):
    return subprocess.call(
            ["pdflatex", "-halt-on-error", file_name + ".tex"])


def _delete_all_files_with_extension(extension):
    file_list = glob.glob("*." + extension)
    for file_path in file_list:
        if os.path.exists(file_path):
            os.remove(file_path)


def _clean_all_files():
    extensions_to_clean = ("acn", "acr", "alg", "aux", "bbl", "bcf", "blg", 
        "blx.bib", "fdb_latexmk", "fls", "glg", "glo", "gls", "idx", "ind", 
        "ilg", "lof", "loa", "lol", "log", "lot", "run.xml", "toc", "out", 
        "xdy", "4ct", "4tc", "css", "dvi", "html", "idv", "lg", "tmp", 
        "xref", "p")
    for extension in extensions_to_clean:
        _delete_all_files_with_extension(extension)


def _call_htlatex(file_name):
    return subprocess.call(
            ["htlatex", file_name, 
            "\"xhtml, mathml, charset=utf-8\""])


def _call_biber(file_name):
    return subprocess.call(
            ["biber", file_name])


def _compilation_setup(tex_file_path):
    folder_path = os.path.dirname(tex_file_path)
    initial_folder_path = os.getcwd()
    os.chdir(folder_path)
    file_name = os.path.splitext(os.path.basename(tex_file_path))[0]
    _clean_all_files()
    return (initial_folder_path, file_name)


def _compilation_teardown(initial_folder_path):
    os.chdir(initial_folder_path)


def _compile_pdf(tex_file_path):
    initial_folder_path, file_name = _compilation_setup(tex_file_path)

    error_codes = []
    error_codes.append(_call_pdflatex(file_name))
    error_codes.append(_call_biber(file_name))
    error_codes.append(_call_pdflatex(file_name))
    error_codes.append(_call_pdflatex(file_name))

    _compilation_teardown(initial_folder_path)
    return all(code == 0 for code in error_codes)


def _compile_html(tex_file_path):
    initial_folder_path, file_name = _compilation_setup(tex_file_path)

    error_codes = []
    error_codes.append(_call_htlatex(file_name))
    error_codes.append(_call_biber(file_name))
    error_codes.append(_call_htlatex(file_name))
    error_codes.append(_call_htlatex(file_name))

    _compilation_teardown(initial_folder_path)
    return all(code == 0 for code in error_codes)


def main(tex_file_path, command):
    tex_file_path = os.path.realpath(tex_file_path)
    if command == "pdf":
        success = _compile_pdf(tex_file_path)
    elif command == "html":
        success = _compile_html(tex_file_path)
    elif command == "clean":
        _clean_all_files()
        success = True
    else:
        success = False

    if success:
        sys.exit(0)
    else:
        sys.exit(1)


if __name__ == "__main__":
    main("bibliography.tex", sys.argv[1])