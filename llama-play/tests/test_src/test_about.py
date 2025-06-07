import pytest
from assertpy import assert_that

import src.about as about

class TestAbout:
    def test_package_name(self):
        assert_that(about.package).is_equal_to('llama-play')

    def test_version(self):
        assert_that(about.version).is_not_empty()

    def test_description(self):
        assert_that(about.description).is_not_empty()

    def test_author(self):
        assert_that(about.author).is_not_empty()

    def test_license(self):
        assert_that(about.license).is_not_empty()