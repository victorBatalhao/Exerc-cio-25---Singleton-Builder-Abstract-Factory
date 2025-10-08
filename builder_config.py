class Configuration:
    def __init__(self, host=None, port=None, user=None, password=None):
        self.host = host
        self.port = port
        self.user = user
        self.password = password

    def __str__(self):
        return f"Host: {self.host}, Port: {self.port}, User: {self.user}, Password: {self.password}"


class ConfigurationBuilder:
    def __init__(self):
        self._host = None
        self._port = None
        self._user = None
        self._password = None

    def set_host(self, host):
        self._host = host
        return self

    def set_port(self, port):
        self._port = port
        return self

    def set_user(self, user):
        self._user = user
        return self

    def set_password(self, password):
        self._password = password
        return self

    def build(self):
        return Configuration(self._host, self._port, self._user, self._password)


def main():
    print("=== Sistema de Configuração (Builder) ===")

    config = (
        ConfigurationBuilder()
        .set_host("127.0.0.1")
        .set_port(3306)
        .set_user("root")
        .set_password("senha123")
        .build()
    )

    print("Configuração construída com sucesso:")
    print(config)


if __name__ == "__main__":
    main()
