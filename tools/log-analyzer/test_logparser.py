"""Unit tests for the SSH log analyzer."""

import tempfile
import unittest
from pathlib import Path

from logparser import count_failed_attempts, status_for, write_report


class CountFailedAttemptsTests(unittest.TestCase):
    def test_counts_failed_password_events_by_ipv4(self):
        lines = [
            "Jan 01 host sshd: Failed password for root from 192.0.2.10 port 2222 ssh2",
            "Jan 01 host sshd: Failed password for invalid user admin from 192.0.2.10 port 2223 ssh2",
            "Jan 01 host sshd: Accepted password for user from 192.0.2.10 port 2224 ssh2",
        ]
        self.assertEqual(count_failed_attempts(lines), {"192.0.2.10": 2})

    def test_ignores_invalid_address_and_ipv6(self):
        lines = [
            "Failed password for root from 999.999.999.999 port 22 ssh2",
            "Failed password for root from 2001:db8::1 port 22 ssh2",
        ]
        self.assertEqual(count_failed_attempts(lines), {})

    def test_ignores_unrelated_lines(self):
        self.assertEqual(count_failed_attempts(["Connection closed by authenticating user"]), {})


class ReportTests(unittest.TestCase):
    def test_threshold_boundary(self):
        self.assertEqual(status_for(4, 5), "Normal")
        self.assertEqual(status_for(5, 5), "SUSPICIOUS")

    def test_csv_output(self):
        with tempfile.TemporaryDirectory() as directory:
            report = Path(directory) / "report.csv"
            write_report({"192.0.2.10": 5, "192.0.2.25": 1}, report, 5)
            content = report.read_text(encoding="utf-8")
            self.assertIn("IP Address,Failed Attempts,Status", content)
            self.assertIn("192.0.2.10,5,SUSPICIOUS", content)
            self.assertIn("192.0.2.25,1,Normal", content)


if __name__ == "__main__":
    unittest.main()
