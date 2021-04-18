import pathlib
from setuptools import setup

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()

setup(
    name="westerly",
    version="0.2.1",
    description="Turns west-const C/C++ source files into east-const",
    long_description=README,
    long_description_content_type="text/markdown",
    url="http://github.com/biasmv/westerly",
    author="Marco Biasini",
    author_email="mvbiasini@gmail.com",
    license="lgpl3",
    packages=[],
    classifiers=[
        "License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)",
        "Topic :: Software Development :: Code Generators",
    ],
    install_requires=["pygments", "click",],
    scripts=["bin/westerly"],
    zip_safe=False,
)
