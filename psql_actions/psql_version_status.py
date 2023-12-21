from psql_actions import TerminalClass


class VersionClass:
    def get_postgresql_status(self):
        """ Check PostgreSQL status """
        # 'systemctl' used to manage the system's services.
        
        command = "systemctl status postgresql"

        TerminalClass().sudo(command)

    def get_postgresql_version(self):
        """ Check PostgreSQL version """
        # 'systemctl' used to manage the system's services.
        
        command = "psql --version"

        TerminalClass().sudo(command)
