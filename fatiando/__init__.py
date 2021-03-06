"""
The ``fatiando`` package contains subpackages for different geophysical methods
and other utilities.

See the API reference for each subpackage for a list of all functions and
classes defined by it.
"""
from ._version import get_versions
__version__ = get_versions()['version']
__commit__ = get_versions()['full']
del get_versions


def test(doctest=True, verbose=False, coverage=False):
    """
    Run the test suite for Fatiando a Terra.

    Uses `py.test <http://pytest.org/>`__ to discover and run the tests. If you
    haven't already, you can install it with `conda
    <http://conda.pydata.org/>`__ or `pip <https://pip.pypa.io/en/stable/>`__.

    Parameters:

    * doctest : bool
        If ``True``, will run the doctests as well (code examples that start
        with a ``>>>`` in the docs).
    * verbose : bool
        If ``True``, will print extra information during the test run.
    * coverage : bool
        If ``True``, will run test coverage analysis on the code as well.
        Requires ``pytest-cov``.

    Returns:

    * exit_code : int
        The exit code for the test run. If ``0``, then all tests pass.

    """
    import pytest
    args = []
    if verbose:
        args.append('-v')
    if coverage:
        args.append('--cov=fatiando')
        args.append('--cov-report')
        args.append('term-missing')
    if doctest:
        args.append('--doctest-modules')
    args.append('--pyargs')
    args.append('fatiando')
    return pytest.main(args)
