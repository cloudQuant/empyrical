#!/usr/bin/env python
#
# Copyright 2016 Quantopian, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from setuptools import setup

DISTNAME = "empyrical"
DESCRIPTION = """empyrical is a Python library with performance and risk \
statistics commonly used in quantitative finance"""
LONG_DESCRIPTION = """empyrical is a Python library with performance and risk
statistics commonly used in quantitative finance by `Quantopian Inc`_.

.. _Quantopian Inc: https://www.quantopian.com
.. _Zipline: https://zipline.io
.. _pyfolio: https://quantopian.github.io/pyfolio/
"""
MAINTAINER = "Quantopian Inc"
MAINTAINER_EMAIL = "opensource@quantopian.com"
AUTHOR = "Quantopian Inc"
AUTHOR_EMAIL = "opensource@quantopian.com"
URL = "https://github.com/quantopian/empyrical"
LICENSE = "Apache License, Version 2.0"

classifiers = [
    "Development Status :: 4 - Beta",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3.12",
    "Programming Language :: Python :: 3.13",
    "License :: OSI Approved :: Apache Software License",
    "Intended Audience :: Science/Research",
    "Topic :: Scientific/Engineering",
    "Topic :: Scientific/Engineering :: Mathematics",
    "Operating System :: OS Independent"
]

install_requires = [
    "numpy>=1.17.0",
    "pandas>=0.25.0",
    "scipy>=1.3.0",
    "six>=1.10",
]

extras_require = {
    "dev": [
        "pytest>=6.0",
        "pytest-xdist>=2.0",
        "pytest-cov>=2.10",
        "flake8",
    ],
    "datareader": [
        "pandas-datareader>=0.8.0",
    ],
}

if __name__ == "__main__":
    setup(
        name=DISTNAME,
        version="0.6.0",
        maintainer=MAINTAINER,
        maintainer_email=MAINTAINER_EMAIL,
        description=DESCRIPTION,
        license=LICENSE,
        url=URL,
        long_description=LONG_DESCRIPTION,
        packages=["empyrical"],
        classifiers=classifiers,
        install_requires=install_requires,
        extras_require=extras_require,
        python_requires=">=3.8",
    )
