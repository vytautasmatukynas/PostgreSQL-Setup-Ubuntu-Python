from psql_actions import terminalClass


class versionClass:
    def get_postgresql_status(self):
        """ Check PostgreSQL status """
        # 'systemctl' used to manage the system's services.
        
        command = "systemctl status postgresql"

        terminalClass().sudo(command)

    def get_postgresql_version(self):
        """ Check PostgreSQL version """
        # 'systemctl' used to manage the system's services.
        
        command = "psql --version"

        terminalClass().sudo(command)
