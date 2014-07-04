import os
import pip
import glob
import unittest
from subprocess import check_output

from pip.req import parse_requirements


def dependencies(pkg):
    """List of all transitive dependencies"""
    bash = ["rm -rf .pkg_test_venv",
            "virtualenv .pkg_test_venv > /dev/null",
            "source .pkg_test_venv/bin/activate",
            "pip install --quiet --download-cache=.pkg_cache %s" % pkg,
            "pip freeze"]
    return check_output("; ".join(bash), shell=True).split()


def requirement_files():
    folder = os.path.dirname(os.path.realpath(__file__))
    for filename in glob.iglob(os.path.join(folder, "../requirements/*.txt")):
        content = [r.req for r in parse_requirements(filename)]
        yield filename, content 


def as_strings(requirements):
    return (str(r).lower() for r in requirements)


class TestCompliance(unittest.TestCase):
    """
    Performed checks:
      * all transitive dependencies listed in the same requirement file
    """
    def test_all_packages(self):
        for filename, content in requirement_files():
            for requirement in content:
                print "Checking", requirement
                content_strings = as_strings(content)
                for installed in dependencies(requirement):  
                    self.assertIn(installed.lower(), content_strings, msg="Unspecified upstream dependency: %s" % installed)


if __name__ == '__main__':
    unittest.main()
