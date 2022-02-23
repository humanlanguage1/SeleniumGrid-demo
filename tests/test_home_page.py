from tests.base_test import BaseTest

class TestHomePage(BaseTest):

  def test_search_bar_should_be_visible(self):
    assert self.page.is_search_bar_dislayed()


