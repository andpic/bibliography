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
	_delete_all_files_with_extension("acn")
	_delete_all_files_with_extension("acr")
	_delete_all_files_with_extension("alg")
	_delete_all_files_with_extension("aux")
	_delete_all_files_with_extension("bbl")
	_delete_all_files_with_extension("bcf")
	_delete_all_files_with_extension("blg")
	_delete_all_files_with_extension("blx.bib")
	_delete_all_files_with_extension("fdb_latexmk")
	_delete_all_files_with_extension("fls")
	_delete_all_files_with_extension("glg")
	_delete_all_files_with_extension("glo")
	_delete_all_files_with_extension("gls")
	_delete_all_files_with_extension("idx")
	_delete_all_files_with_extension("ind")
	_delete_all_files_with_extension("ilg")
	_delete_all_files_with_extension("lof")
	_delete_all_files_with_extension("loa")
	_delete_all_files_with_extension("lol")
	_delete_all_files_with_extension("log")
	_delete_all_files_with_extension("lot")
	_delete_all_files_with_extension("run.xml")
	_delete_all_files_with_extension("toc")
	_delete_all_files_with_extension("out")
	_delete_all_files_with_extension("xdy")
	_delete_all_files_with_extension("4ct")
	_delete_all_files_with_extension("4tc")
	_delete_all_files_with_extension("css")
	_delete_all_files_with_extension("dvi")
	_delete_all_files_with_extension("html")
	_delete_all_files_with_extension("idv")
	_delete_all_files_with_extension("lg")
	_delete_all_files_with_extension("tmp")
	_delete_all_files_with_extension("xref")
	_delete_all_files_with_extension("p")


def _call_htlatex(file_name):
    return subprocess.call(
            ["htlatex", "-halt-on-error", file_name, 
            "'html,charset=utf-8'", "' -cunihtf -utf8'"])


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


def main(tex_file_path, output_format):
    tex_file_path = os.path.realpath(tex_file_path)
    if output_format == "pdf":
        success = _compile_pdf(tex_file_path)
    elif output_format == "html":
        success = _compile_html(tex_file_path)
    else:
        success = False

    if success:
        sys.exit(0)
    else:
        sys.exit(1)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])