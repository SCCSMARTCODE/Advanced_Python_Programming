from config_manager import ConfigManager

# Example Usage
config = ConfigManager(initial_data={"api_key": "123456", "timeout": 30}, readonly_keys={"api_key"})

# Access like a dictionary
print(config["timeout"])
print(config.api_key)

# Modify an entry
config["timeout"] = 60
print(config["timeout"])

# Attempting to modify a read-only key will raise an error
try:
    config["api_key"] = "NEW_KEY"
except ValueError as e:
    print(e)

# Iterate over keys
for key in config:
    print(f"{key}: {config[key]}")
