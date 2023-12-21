from psql_actions import TerminalClass


class ServiceClass:
    def enable_postgresql_service(self):
        """ Enable PostgreSQL service"""
        # 'systemctl' used to manage the system's services.
        
        command = "systemctl enable postgresql"

        TerminalClass().sudo(command)

    def start_postgresql_service(self):
        """ Start PostgreSQL service"""
        # 'systemctl' used to manage the system's services.
        
        command = "systemctl start postgresql"

        TerminalClass().sudo(command)

    def stop_postgresql_service(self):
        """ Stop PostgreSQL service"""
        # 'systemctl' used to manage the system's services.
        
        command = "systemctl stop postgresql"

        TerminalClass().sudo(command)

    def restart_postgresql_service(self):
        """ Restart PostgreSQL service"""
        # 'systemctl' used to manage the system's services.
        
        command = "systemctl restart postgresql"

        TerminalClass().sudo(command)
