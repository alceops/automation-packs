import unittest
from pathlib import Path
from pr_readiness_checker_lite import changed_files, score_diff, render, render_service_template


class ReadinessCheckerTests(unittest.TestCase):
    def test_changed_files_from_diff_headers(self):
        diff = "diff --git a/a.py b/a.py\n+++ b/a.py\n"
        self.assertEqual(changed_files(diff), ["a.py"])

    def test_sample_diff_is_ready_with_notes(self):
        diff = Path("sample_diff.txt").read_text(encoding="utf-8")
        result = score_diff(diff)
        self.assertGreaterEqual(result["score"], 60)
        self.assertIn(result["verdict"], {"ready-with-notes", "needs-tightening"})
        self.assertTrue(any("Test signal" in item for item in result["findings"]))

    def test_no_test_diff_is_penalized(self):
        diff = "diff --git a/app.py b/app.py\n+++ b/app.py\n@@\n+print('token payment')\n"
        result = score_diff(diff)
        self.assertLess(result["score"], 60)
        self.assertEqual(result["verdict"], "not-ready")

    def test_render_includes_cash_forward_hook(self):
        text = render(score_diff("diff --git a/tests/t.py b/tests/t.py\n+++ b/tests/t.py\n+def test_x(): pass\n"))
        self.assertIn("Cash-forward service hook", text)

    def test_service_template_routes_safe_qualified_inputs(self):
        text = render_service_template()
        self.assertIn("public or redacted PR/diff", text)
        self.assertIn("Qualified signal", text)
        self.assertIn("payment collection stays on Corey hold", text)
        self.assertIn("no GitHub login", text)


if __name__ == "__main__":
    unittest.main()
