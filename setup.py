import os
from setuptools import setup, find_packages

long_description = '''
This package is a package to test importing etc for the 2019 edition 
of the ASPP course. 

I am learning so much!

This setup.py script is based on examples from  
https://pythonhosted.org/an_example_pypi_project/setuptools.html
and
https://docs.python.org/3/distutils/setupscript.
and 
https://github.com/pypa/sampleproject/blob/master/setup.py
'''

setup(
    name = 'test_package',
    version = '0.0.1d',
    install_requires=['numpy>=1.0.0,<1.13.0',
					  'scipy>=1.0.0,<2.0.0'], 
    author = 'ASPP 2019',
    author_email = 'prof_snape@not-gmail.org',
    description = 'an example of a simple python package',
    long_description = long_description,
    license = 'BSD',
    url = 'github page',
    packages=find_packages(),
)



# setup(
#     name = 'test_package',
#     version = version,
#     install_requires=requirements.txt, 
#     author = 'ASPP 2019',
#     author_email = 'prof_snape@not-gmail.org',
#     description = 'an example of a simple python package',
#     license = 'BSD',
#     keywords = 'documentation distribution example',
#     url = 'github page',
#     packages=find_packages(),
#     long_description=long_description,
#     classifiers=[
#         'Development Status :: 3 - Alpha',
#         'Intended Audience :: ASPP students',        
#         'License :: OSI Approved :: BSD License',
#         'Programming Language :: Python :: 3',
#         'Operating System :: OS Independent',
#     ],
# )
