class configerror(ValueError):
    def __init__(self, key_name, invalid_value, message="Invalid configuration value."):

        self.key_name = key_name
        self.invalid_value = invalid_value

        full_message = f"{message} for key '{key_name}': received '{invalid_value}'"

        super().__init__(full_message)

try:
    raise configerror("timeout", -5, message="Timeout cannot be negative")
except configerror as e:
    print(f"{e}")
    print(f"   -> key: {e.key_name}")
    print(f"   -> value: {e.invalid_value}")
