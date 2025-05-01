import sys
import os
import shutil




in_dir = sys.argv[1]
out_dir = sys.argv[2]

max_depth = 10**10

if "--max_depth" in sys.argv:
    a = sys.argv.index("--max_depth")
    max_depth = int(sys.argv[a + 1])


for dirpaths, dirs, files in os.walk(in_dir):
    cut_path = os.path.relpath(dirpaths, in_dir )
    depth = cut_path.count(os.sep)

    if depth >= max_depth:
        continue

    for file in files:
        moved_file = os.path.join(dirpaths, file)
        shutil.copy(moved_file, out_dir)

'''отсюда брала большую частьинфо: https://cpp-python-nsu.inp.nsk.su/textbook/sec4/ch3#:~:text=%D0%9C%D0%BE%D0%B4%D1%83%D0%BB%D1%8C%20sys&text=exit%20%D0%BF%D0%BE%D0%B7%D0%B2%D0%BE%D0%BB%D1%8F%D0%B5%D1%82%20%D0%B7%D0%B0%D0%B2%D0%B5%D1%80%D1%88%D0%B8%D1%82%D1%8C%20%D0%B2%D1%8B%D0%BF%D0%BE%D0%BB%D0%BD%D0%B5%D0%BD%D0%B8%D0%B5%20%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D1%8B,%D0%B1%D1%83%D0%B4%D0%B5%D1%82%20%D1%81%D1%87%D0%B8%D1%82%D0%B0%D1%82%D1%8C%20%D0%BF%D1%80%D0%B8%D0%B7%D0%BD%D0%B0%D0%BA%D0%BE%D0%BC%20%D0%BD%D0%B5%D0%BD%D0%BE%D1%80%D0%BC%D0%B0%D0%BB%D1%8C%D0%BD%D0%BE%D0%B3%D0%BE%20%D0%B7%D0%B0%D0%B2%D0%B5%D1%80%D1%88%D0%B5%D0%BD%D0%B8%D1%8F.
https://pythonworld.ru/moduli/modul-os-path.html
https://digitology.tech/docs/python_3/library/os.path.html
'''

