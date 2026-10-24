import unittest

from bot_manager import BotManager, BotState


class BotManagerTests(unittest.TestCase):
    def setUp(self):
        self.manager = BotManager()

    def test_create_bots(self):
        self.manager.create_bots(3, "Test")
        self.assertEqual(len(self.manager.bots), 3)
        self.assertEqual(self.manager.bots[1].nickname, "Test1")

    def test_reject_invalid_count(self):
        with self.assertRaises(ValueError):
            self.manager.create_bots(51)

    def test_target_assignment(self):
        self.manager.create_bots(2)
        self.manager.set_target("  TEST-UID  ")
        self.assertTrue(
            all(bot.target_uid == "TEST-UID"
                for bot in self.manager.bots.values())
        )

    def test_start_does_not_claim_connection(self):
        self.manager.create_bots(2)
        self.manager.start_all()
        for bot in self.manager.bots.values():
            self.assertEqual(bot.state, BotState.NOT_IMPLEMENTED)
            self.assertIsNotNone(bot.last_error)

    def test_stop_all(self):
        self.manager.create_bots(2)
        self.manager.start_all()
        self.manager.stop_all()
        for bot in self.manager.bots.values():
            self.assertEqual(bot.state, BotState.STOPPED)
            self.assertIsNone(bot.last_error)


if __name__ == "__main__":
    unittest.main(verbosity=2)
