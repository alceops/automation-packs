import subprocess
import sys
import unittest
from pathlib import Path

import upwork_proposal_scorer_slim as scorer

ROOT = Path(__file__).parent


class SlimScorerTests(unittest.TestCase):
    def test_sample_scores_and_keeps_safety_boundary(self):
        job = (ROOT / "sample_job.txt").read_text()
        proposal = (ROOT / "sample_proposal.txt").read_text()
        out = scorer.render(job, proposal, "agency")
        self.assertIn("Upwork Proposal Scorer Slim Report", out)
        self.assertIn("Score:", out)
        self.assertIn("Recommended fixes:", out)
        self.assertIn("Niche tweak (agency):", out)
        self.assertIn("no scraping, login, auto-send, guaranteed wins", out)

    def test_risky_auto_submit_claim_is_penalized_and_flagged(self):
        job = "Need Upwork proposals for Python automation."
        proposal = "I guarantee more jobs and automatically submit messages for you."
        result = scorer.score(job, proposal)
        self.assertIn("guaranteed outcome", result["risky"])
        self.assertIn("platform automation", result["risky"])
        self.assertLess(result["total"], 60)
        self.assertTrue(any("guaranteed-win or auto-submit" in item for item in scorer.fixes(result)))

    def test_cli_runs_without_dependencies(self):
        proc = subprocess.run(
            [sys.executable, str(ROOT / "upwork_proposal_scorer_slim.py"), "--job", str(ROOT / "sample_job.txt"), "--proposal", str(ROOT / "sample_proposal.txt")],
            text=True,
            capture_output=True,
            check=True,
        )
        self.assertIn("Score:", proc.stdout)
        self.assertIn("Safety boundary:", proc.stdout)

    def test_intake_template_keeps_payment_gate_and_private_data_out(self):
        out = scorer.intake_template("agency")
        self.assertIn("Buyer intake for one proposal QA sample", out)
        self.assertIn("Preferred niche/rubric: agency", out)
        self.assertIn("do not send login credentials", out)
        self.assertIn("route Corey approval before any invoice", out)

    def test_cli_can_append_intake_template(self):
        proc = subprocess.run(
            [
                sys.executable,
                str(ROOT / "upwork_proposal_scorer_slim.py"),
                "--job",
                str(ROOT / "sample_job.txt"),
                "--proposal",
                str(ROOT / "sample_proposal.txt"),
                "--niche",
                "agency",
                "--intake-template",
            ],
            text=True,
            capture_output=True,
            check=True,
        )
        self.assertIn("Upwork Proposal Scorer Slim Report", proc.stdout)
        self.assertIn("Buyer intake for one proposal QA sample", proc.stdout)
        self.assertIn("custom $49 rubric pilot", proc.stdout)

    def test_reply_template_routes_to_sample_or_payment_hold(self):
        out = scorer.reply_template("coach")
        self.assertIn("Qualified intake reply for one proposal QA sample", out)
        self.assertIn("one coach proposal sample locally", out)
        self.assertIn("public/redacted job post", out)
        self.assertIn("pause for Corey to approve the payment collection path", out)
        self.assertIn("count this only if the buyer sends paste-safe job/proposal text", out)

    def test_cli_can_append_reply_template(self):
        proc = subprocess.run(
            [
                sys.executable,
                str(ROOT / "upwork_proposal_scorer_slim.py"),
                "--job",
                str(ROOT / "sample_job.txt"),
                "--proposal",
                str(ROOT / "sample_proposal.txt"),
                "--niche",
                "coach",
                "--reply-template",
            ],
            text=True,
            capture_output=True,
            check=True,
        )
        self.assertIn("Upwork Proposal Scorer Slim Report", proc.stdout)
        self.assertIn("Qualified intake reply for one proposal QA sample", proc.stdout)
        self.assertIn("custom $49 rubric pilot", proc.stdout)

    def test_signal_decision_template_separates_pipeline_from_no_count(self):
        out = scorer.signal_decision_template("agency")
        self.assertIn("Buyer response signal decision log", out)
        self.assertIn("Target niche: agency", out)
        self.assertIn("Count as qualified pipeline only if", out)
        self.assertIn("No-count outcomes", out)
        self.assertIn("Corey hold when paid intent appears", out)
        self.assertIn("after 5 no-count outcomes", out)

    def test_cli_can_append_signal_decision(self):
        proc = subprocess.run(
            [
                sys.executable,
                str(ROOT / "upwork_proposal_scorer_slim.py"),
                "--job",
                str(ROOT / "sample_job.txt"),
                "--proposal",
                str(ROOT / "sample_proposal.txt"),
                "--niche",
                "agency",
                "--signal-decision",
            ],
            text=True,
            capture_output=True,
            check=True,
        )
        self.assertIn("Upwork Proposal Scorer Slim Report", proc.stdout)
        self.assertIn("Buyer response signal decision log", proc.stdout)
        self.assertIn("Corey hold when paid intent appears", proc.stdout)


if __name__ == "__main__":
    unittest.main()
