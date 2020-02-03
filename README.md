# Bibliography

[![CircleCI](https://circleci.com/gh/andpic/bibliography.svg?style=svg&circle-token=d689174ba4c58e3e57b11621c48611738cc7c75d)](https://circleci.com/gh/andpic/bibliography) [![Latest version (PDF)](https://img.shields.io/badge/download-latest-blue)](https://circleci.com/api/v1.1/project/github/andpic/bibliography/latest/artifacts/0/tmp/bibliography.pdf)

A selection of papers on numerical methods, linear algebra, sparse matrices, and GPUs.

[![wordcloud.png](https://i.postimg.cc/Dyz1R7bj/wordcloud.png)](https://postimg.cc/WtQDkL8g)

## Compiling the PDF

On Linux, a base install of TeX Live should be sufficient. On both Windows 
and Linux, the PDF can be generated by calling:
```bash
python compile.py bibliography.tex pdf
```