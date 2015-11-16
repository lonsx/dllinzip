# dllinzip
When you run py2exe to build Windows executable programs from Python scripts `eg. xyz.py` with `bundle_files=1` & without `zipfile=None`,

actully you usually get two files:

1. xyz.exe
2. library.zip (packed with the python-dll into it)

If you want to modify the zip-archive,just replace something in the zipfile,and then repack it.

Now it is `pure zipfile` without DLL bundled.

This script does what py2exe do with `bundle_files=1`,

it help you to add `python##.dll` rebundled in the zipfile after.

The source code was from build_exe.py in `C:\Python27\Lib\site-packages\py2exe\`.

--------Remember to replace the zipfile name in arc.py in your case-----------

			********Run with Python Installed**********