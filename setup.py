import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
     name='j-funcutils',  
     version='0.0.5',
     author="Juan Manuel Camara Diaz",
     author_email="juanma.caaz@gmail.com",
     description="A basic cost time calculator",
     url="https://github.com/juanmacaaz/FuncUtils",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )