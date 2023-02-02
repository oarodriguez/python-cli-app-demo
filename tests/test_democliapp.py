"""Verify the library top-level functionality."""
import democliapp


def test_version():
    """Verify we have updated the package version."""
    assert democliapp.__version__ == "2023.1.0.dev0"
