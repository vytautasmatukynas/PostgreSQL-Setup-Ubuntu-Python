from colors import Color

from psql_actions import TerminalClass


class SetupClass:
    def download_postgresql_key(self):
        """ Download PostgreSQL GPG Key """

        sudo_password = input("Enter sudo password: ")
        key_destination = "/etc/apt/trusted.gpg.d/pgdg.asc"
        key_url = "https://www.postgresql.org/media/keys/ACCC4CF8.asc"
        command = f"wget -qO {key_destination} {key_url} -y"

        TerminalClass().echo_sudo_s(sudo_password, command)

    def add_postgresql_repository(self):
        """ Add PostgreSQL Repository """

        sudo_password = input("Enter sudo password: ")
        command = "echo deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -sc)-pgdg main -y"

        TerminalClass().echo_sudo_s(sudo_password, command)

    def install_postgresql(self):
        """ Install PostgreSQL """

        sudo_password = input("Enter sudo password: ")
        commands = ["apt update -y",
                    "apt install -y postgresql postgresql-contrib"]
        for command in commands:
            TerminalClass().echo_sudo_s(sudo_password, command)
            if "update" in command:
                print(Color.CAYN + "\n/---/ Update was successful. /---/" + Color.DEFAULT)
            elif "upgrade" in command:
                print(Color.CAYN + "\n/---/ Upgrade was successful. /---/" + Color.DEFAULT)

    def exec_postgresql_install(self):
        self.download_postgresql_key()
        self.add_postgresql_repository()
        self.install_postgresql()
