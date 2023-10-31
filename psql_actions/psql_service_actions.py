from psql_actions import terminalClass


class serviceClass:
    def enable_postgresql_service(self):
        """ Enable PostgreSQL service"""
        # 'systemctl' used to manage the system's services.
        
        command = "systemctl enable postgresql"

        terminalClass().sudo(command)

    def start_postgresql_service(self):
        """ Start PostgreSQL service"""
        # 'systemctl' used to manage the system's services.
        
        command = "systemctl start postgresql"

        terminalClass().sudo(command)

    def stop_postgresql_service(self):
        """ Stop PostgreSQL service"""
        # 'systemctl' used to manage the system's services.
        
        command = "systemctl stop postgresql"

        terminalClass().sudo(command)

    def restart_postgresql_service(self):
        """ Restart PostgreSQL service"""
        # 'systemctl' used to manage the system's services.
        
        command = "systemctl restart postgresql"

        terminalClass().sudo(command)
