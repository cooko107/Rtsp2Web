from distutils.core import setup, Extension
import os


library_dir = ['/workspace/HikStream/opencv-2.4.13.5/opencv-debug/lib', '/workspace/HikStream/lib/HCNetSDKCom', '/workspace/HikStream/lib']

library = []

for d in library_dir:
    for l in os.listdir(d):
        if l.endswith('.so') or l.endswith('.a'):
            library.append(l.split('.')[0][3:])

print(library)


cos_doubles_module = Extension('HKIPcamera',
	sources=['HKIPcamera_wrap.cxx', 'HKIPcamera.cpp'],
	libraries=library,
	library_dirs=library_dir
	)

setup (name = 'cos_doubles',
        version = '0.1',
        author      = "SWIG Docs",
        description = """Simple swig example from docs""",
        ext_modules = [cos_doubles_module],
        include_dirs = ['/usr/include/boost', '/workspace/HikStream/include', '/usr/local/include/opencv',
        '/usr/local/include/opencv2', '/usr/include/python2.7/', '/usr/include/'],
        py_modules = ["HKIPcamera"])