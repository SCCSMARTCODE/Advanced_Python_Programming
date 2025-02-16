import json
import os

DEFAULT_CONFIG_FILE_PATH = "config.json"


class ConfigManager:
    def __init__(self, config_file_path: str = None, initial_data: dict = None, readonly_keys: set = None):
        if not config_file_path:
            config_file_path = DEFAULT_CONFIG_FILE_PATH
        else:
            assert config_file_path.endswith(".json"), "Config file must be a JSON file"

        self.config_file_path = config_file_path
        self.config = {}
        self.readonly_keys = set(readonly_keys) if readonly_keys else set()

        # Load existing configuration or initialize with provided data
        if os.path.exists(self.config_file_path):
            with open(self.config_file_path, 'r') as config_file:
                loaded_config = json.load(config_file)
                for key, value in loaded_config.items():
                    self.config[key] = value
                    if value[1]:
                        self.readonly_keys.add(key)
        elif initial_data:
            for key, value in initial_data.items():
                is_readonly = key in self.readonly_keys
                self.config[key] = [value, is_readonly]

            self.save_config()

    def __setitem__(self, key, value):
        """Sets the config item, allowing specification of read-only status."""
        if key in self.readonly_keys:
            raise ValueError(f"{key} is a read-only key and cannot be modified.")
        self.config[key] = [value, False]
        self.save_config()

    def set_readonly(self, key):
        """Marks a config key as read-only, ensuring it exists first."""
        if key not in self.config:
            raise KeyError(f"Cannot mark '{key}' as read-only because it does not exist.")

        self.readonly_keys.add(key)
        self.config[key][1] = True
        self.save_config()

    def __getitem__(self, item):
        """Gets the config item, enforcing read-only restrictions."""
        if item not in self.config:
            raise KeyError(f"{item} not found in configuration.")
        result = self.config.get(item, [None, False])
        return result[0]

    def __setattr__(self, key, value):
        """Sets an attribute, allowing dynamic attribute assignment."""
        if key in ['config_file_path', 'config', 'readonly_keys']:
            super().__setattr__(key, value)
        else:
            if key in self.readonly_keys:
                raise AttributeError(f"{key} is a read-only key and cannot be modified.")
            self.config[key] = [value, False]
            self.save_config()

    def __getattr__(self, item):
        """Gets an attribute, enforcing read-only restrictions."""
        if item in self.config:
            result = self.config[item]
            return result[0]  # Return the value part
        raise AttributeError(f"{item} not found in configuration")

    def __iter__(self):
        """Allows iteration over the configuration keys."""
        return iter(self.config)

    def save_config(self):
        """Saves the current configuration to the JSON file."""
        with open(self.config_file_path, 'w') as config_file:
            json.dump(self.config, config_file, indent=4)

    def __delattr__(self, key):
        """Allows deletion of attributes with read-only checks."""
        if key in self.readonly_keys:
            raise AttributeError(f"{key} is a read-only key and cannot be deleted.")
        if key in self.config:
            del self.config[key]
            self.save_config()
        else:
            raise AttributeError(f"{key} not found in configuration")

    def __delitem__(self, key):
        """Allows deletion of config items while enforcing read-only restrictions."""
        if key in self.readonly_keys:
            raise ValueError(f"{key} is a read-only key and cannot be deleted.")
        if key in self.config:
            del self.config[key]
            self.save_config()
        else:
            raise KeyError(f"{key} not found in configuration.")
