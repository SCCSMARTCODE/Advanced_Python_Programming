# **Smart Config Manager**
A Python-based **configuration manager** that allows **dictionary-style** and **attribute-style** access to settings. It supports:
- ✅ **Persistent Storage** – Configurations are stored in a JSON file.
- ✅ **Read-Only Keys** – Protect important configurations from being modified.
- ✅ **Dynamic Access** – Retrieve and modify settings like a dictionary (`config["key"]`) or as an object (`config.key`).
- ✅ **Safe Deletion** – Prevents accidental deletion of critical settings.

---

## **📂 Project Structure**
```
smart_config_manager/
├── config_manager.py   # Core logic for managing configurations
├── example.py          # Example usage
├── test_config.py      # Unit tests
├── config.json         # Stored configuration file
└── README.md           # Documentation
```

---

## **📌 Features**
### 🔹 **1. Dictionary-Style Access**
```python
from config_manager import ConfigManager
config = ConfigManager(initial_data={"api_key": "123456", "timeout": 30})

print(config["timeout"])  # ✅ 30
config["timeout"] = 60  # ✅ Update config value
del config["timeout"]  # ✅ Delete a key
```

### 🔹 **2. Attribute-Style Access**
```python
print(config.api_key)  # ✅ 123456
config.timeout = 90  # ✅ Change config like an object
```

### 🔹 **3. Read-Only Keys**
```python
config.set_readonly("api_key")  # ✅ Make "api_key" read-only

config.api_key = "new_value"  # ❌ Raises ValueError
del config.api_key  # ❌ Raises AttributeError
```

### 🔹 **4. Safe Iteration & Membership**
```python
for key in config:
    print(key, config[key])

print("api_key" in config)  # ✅ True
```

---

## **⚙ Installation**
No installation required! Just clone the repository:
```bash
git clone https://github.com/SCCSMARTCODE/Advanced_Python_Programming
cd metaprogramming/smart_config_manager
```

---

## **✅ Running Tests**
To validate the functionality, run:
```bash
python -m unittest test_config.py
```

---

## **🚀 Future Enhancements**
🔹 Auto-load from **environment variables**  
🔹 Support for **YAML files**  
🔹 Web-based UI for editing configurations  

---

### **👨‍💻 Author**
Developed by **SCCSMARTCODE** as part of mastering **Python Metaprogramming**.
