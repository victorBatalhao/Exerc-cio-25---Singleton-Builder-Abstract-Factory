from abc import ABC, abstractmethod

class Configuration:
    def __init__(self, host, port, user, password):
        self.host = host
        self.port = port
        self.user = user
        self.password = password

    def __str__(self):
        return f"Host: {self.host}, Port: {self.port}, User: {self.user}, Password: {self.password}"


class ConfigurationFactory(ABC):
    @abstractmethod
    def create_configuration(self):
        pass


class DevConfigFactory(ConfigurationFactory):
    def create_configuration(self):
        return Configuration("localhost", 5000, "dev_user", "dev_pass")


class ProdConfigFactory(ConfigurationFactory):
    def create_configuration(self):
        return Configuration("192.168.1.10", 8080, "prod_user", "prod_pass")


def main():
    print("=== Sistema de Configuração (Abstract Factory) ===")

    env = input("Digite o ambiente (dev/prod): ").strip().lower()

    factory = DevConfigFactory() if env == "dev" else ProdConfigFactory()
    config = factory.create_configuration()

    print("\nConfiguração do ambiente selecionado:")
    print(config)


if __name__ == "__main__":
    main()
