class ConfigurationManager:
    _instance = None
    _config = {}

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ConfigurationManager, cls).__new__(cls)
            cls._config = {}
        return cls._instance

    def load_config(self, data: dict):
        self._config.update(data)

    def get_config(self):
        return self._config


def main():
    print("=== Sistema de Configuração (Singleton) ===")

    config1 = ConfigurationManager()
    config1.load_config({
        "host": "localhost",
        "port": 8080,
        "user": "admin",
        "password": "1234"
    })

    config2 = ConfigurationManager()

    print("Mesma instância?", config1 is config2)
    print("Configurações carregadas:", config2.get_config())


if __name__ == "__main__":
    main()
