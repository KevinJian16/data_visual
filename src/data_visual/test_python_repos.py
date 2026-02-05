import unittest

from python_repos import fetch_python_repositories


class TestPythonRepos(unittest.TestCase):
    def test_status_code(self):
        """Test that the status code of the response is 200."""
        r = fetch_python_repositories(
            "https://api.github.com/search/repositories?q=language:python&sort=stars"
        )
        self.assertEqual(r.status_code, 200)
        r = fetch_python_repositories(
            "https://api.github.com/search/repositories?q=language:c&sort=stars"
        )
        self.assertEqual(r.status_code, 200)
        r = fetch_python_repositories(
            "https://api.github.com/search/repositories?q=language:ruby&sort=stars"
        )
        self.assertEqual(r.status_code, 200)
        r = fetch_python_repositories(
            "https://api.github.com/search/repositories?q=language:java&sort=stars"
        )
        self.assertEqual(r.status_code, 200)
        r = fetch_python_repositories(
            "https://api.github.com/search/repositories?q=language:go&sort=stars"
        )
        self.assertEqual(r.status_code, 200)


unittest.main()
