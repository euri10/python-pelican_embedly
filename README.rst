========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis| |appveyor| |requires|
        | |codecov|
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|

.. |docs| image:: https://readthedocs.org/projects/python-pelican_embedly/badge/?style=flat
    :target: https://readthedocs.org/projects/python-pelican_embedly
    :alt: Documentation Status

.. |travis| image:: https://travis-ci.org/euri10/python-pelican_embedly.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/euri10/python-pelican_embedly

.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/euri10/python-pelican_embedly?branch=master&svg=true
    :alt: AppVeyor Build Status
    :target: https://ci.appveyor.com/project/euri10/python-pelican_embedly

.. |requires| image:: https://requires.io/github/euri10/python-pelican_embedly/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/euri10/python-pelican_embedly/requirements/?branch=master

.. |codecov| image:: https://codecov.io/github/euri10/python-pelican_embedly/coverage.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/euri10/python-pelican_embedly

.. |version| image:: https://img.shields.io/pypi/v/pelican-embedly.svg
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/pelican-embedly

.. |commits-since| image:: https://img.shields.io/github/commits-since/euri10/python-pelican_embedly/v0.1.0.svg
    :alt: Commits since latest release
    :target: https://github.com/euri10/python-pelican_embedly/compare/v0.1.0...master

.. |wheel| image:: https://img.shields.io/pypi/wheel/pelican-embedly.svg
    :alt: PyPI Wheel
    :target: https://pypi.python.org/pypi/pelican-embedly

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/pelican-embedly.svg
    :alt: Supported versions
    :target: https://pypi.python.org/pypi/pelican-embedly

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/pelican-embedly.svg
    :alt: Supported implementations
    :target: https://pypi.python.org/pypi/pelican-embedly


.. end-badges

embed.ly cards for Pelican blog

* Free software: BSD license

Installation
============

::

    pip install pelican-embedly

Documentation
=============

https://python-pelican_embedly.readthedocs.io/

Development
===========

To run the all tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
