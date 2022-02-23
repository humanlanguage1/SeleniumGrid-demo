from tests.base_test import BaseTest

class TestSearchResultPage(BaseTest):

  def perform_search_by_submit_expects_no_results(self):
    self.page.type("dsfdskmfksdfsmdfkl")
    return self.page.submit()

  def test_search_by_submit_check_no_results(self):
    result_page = self.perform_search_by_submit_expects_no_results()
    assert result_page.get_result_count() == 0

  def test_search_by_click_check_multiple_results(self):
    self.page.type("Selenium live codie interview")
    result_page = self.page.click_to_search()
    assert result_page.get_result_count() > 1


