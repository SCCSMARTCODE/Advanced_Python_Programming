import unittest
import os
import json
from .config_manager import ConfigManager

TEST_CONFIG_FILE = "test_config.json"

class TestConfigManager(unittest.TestCase):

    def setUp(self):
        """Set up a fresh ConfigManager instance before each test."""
        self.config = ConfigManager(
            config_file_path=TEST_CONFIG_FILE,
            initial_data={"api_key": "123456", "timeout": 30},
            readonly_keys={"api_key"}
        )

    def tearDown(self):
        """Clean up the test JSON file after each test."""
        if os.path.exists(TEST_CONFIG_FILE):
            os.remove(TEST_CONFIG_FILE)

    # ✅ 1. Test Dictionary-Style Get/Set Access
    def test_getitem(self):
        self.assertEqual(self.config["timeout"], 30)

    def test_setitem(self):
        self.config["timeout"] = 60
        self.assertEqual(self.config["timeout"], 60)

    # ✅ 2. Test Attribute-Style Get/Set Access
    def test_getattr(self):
        self.assertEqual(self.config.api_key, "123456")

    def test_setattr(self):
        self.config.timeout = 90
        self.assertEqual(self.config.timeout, 90)

    # ✅ 3. Test Read-Only Keys
    def test_readonly_key_set(self):
        with self.assertRaises(ValueError):
            self.config["api_key"] = "new_value"

    def test_readonly_key_set_attr(self):
        with self.assertRaises(AttributeError):
            self.config.api_key = "new_value"

    def test_readonly_key_delete(self):
        with self.assertRaises(AttributeError):
            del self.config.api_key

    # ✅ 4. Test Safe Deletion
    def test_delete_key(self):
        del self.config["timeout"]
        with self.assertRaises(KeyError):  # ✅ Expect KeyError, not AttributeError
            _ = self.config["timeout"]

    def test_delete_attr(self):
        del self.config.timeout
        with self.assertRaises(AttributeError):
            _ = self.config.timeout

    # ✅ 5. Test Iteration
    def test_iteration(self):
        keys = list(iter(self.config))
        self.assertIn("api_key", keys)
        self.assertIn("timeout", keys)

    # ✅ 6. Test Membership (`in` Operator)
    def test_contains(self):
        self.assertTrue("api_key" in self.config)
        self.assertFalse("non_existent_key" in self.config)

    # ✅ 7. Test Persistence (Saving & Loading)
    def test_persistence(self):
        # Modify and save config
        self.config["theme"] = "dark"
        self.config.save_config()

        # Load a new instance to check if data persists
        new_config = ConfigManager(config_file_path=TEST_CONFIG_FILE)
        self.assertEqual(new_config["theme"], "dark")

    def test_readonly_persistence(self):
        """Ensure read-only keys persist properly."""
        self.config["theme"] = "dark"  # Ensure the key exists
        self.config.set_readonly("theme")  # Now it can be marked read-only

        # Reload and check if "theme" is still read-only
        new_config = ConfigManager(config_file_path=TEST_CONFIG_FILE)
        self.assertTrue("theme" in new_config.readonly_keys)


if __name__ == "__main__":
    unittest.main()
