import unittest
from unittest.mock import patch, MagicMock

from src.app import save_reputation_scores
from src.model import ReputationScore


class TestSaveReputationScores(unittest.TestCase):

    def setUp(self):
        self.records = [("address1", "type1", 10), ("address2", "type2", 20)]
        self.mock_session = MagicMock()

    def test_save_reputation_scores(self):
        save_reputation_scores(self.records, self.mock_session)

        expected_reputation_scores = [ReputationScore(address="address1", wallet_type="type1", score=10),
                                      ReputationScore(address="address2", wallet_type="type2", score=20)]

        for rs in expected_reputation_scores:
            self.mock_session.add.assert_any_call(rs)

        self.mock_session.commit.assert_called_once()


if __name__ == '__main__':
    unittest.main()
