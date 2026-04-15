from setuptools import setup, Extension

# Define the C extension module
qgate_engine = Extension(
    'qgate_lib.engine', # This maps to qgate_lib/engine.so (or .pyd)
    sources=['src/engine.c'],
    include_dirs=['src']  # Add paths to headers if you have them
)

setup(
    ext_modules=[qgate_engine]
)