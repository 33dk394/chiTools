import pathlib
[p.unlink() for p in pathlib.Path.cwd().rglob('*.py[co]')]
[p.rmdir() for p in pathlib.Path.cwd().rglob('__pycache__')]