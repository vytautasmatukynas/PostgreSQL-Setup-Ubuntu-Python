from colors import Color
import subprocess


class terminalClass:
    def echo_sudo_S(self, sudo_password, command):
        """ Create a string that combines the password and the command
        'echo' print password to standard  output
        '|' pipe symbol redirects 'echo' standard output to the standard input of the subsequent command
        '-S' tells 'sudo' to read password from input """
        terminal_command = f'echo "{sudo_password}" | sudo -S {command}'

        self.install(terminal_command, command, sudo_password)

    def sudo(self, command):
        """ Create a string that combines the password and the command """
        terminal_command = f'sudo {command}'

        self.install(terminal_command, command)

    def install(self, *args):
        """ Run the sudo command using subprocess """
        terminal_command = args[0]
        command = args[1]

        try:
            # 'shell=True' This parameter indicates that the command should be executed within a shell. When
            # 'stdout=subprocess.PIPE' specifies that the standard output (stdout) of the command being
            #  executed should be captured. By setting it to subprocess.PIPE, you're redirecting the command's
            #  stdout to a pipe.
            # 'stderr=subprocess.PIPE' this parameter specifies that the standard error (stderr) of the
            # command should also be captured. By setting it to subprocess.PIPE, you're redirecting the command's
            # stderr to a pipe.
            # 'text=True' used to indicate that the command's output (both stdout and stderr) should be treated
            # as text rather than binary data.
            process = subprocess.Popen(terminal_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                       text=True)

            # The subprocess.Popen() function starts a new subprocess and returns a Popen object that represents
            # the running subprocess.
            # The communicate() method returns a tuple containing captured output data from subprocess -
            # stdout and stderr.
            stdout, stderr = process.communicate()

            # 'process.returncode == 0' exit status or return code of the executed subprocess. In many programming
            # environments, including Unix-like systems, an exit status of 0 typically indicates successful execution
            # without any errors. Exit status of 1 (or any non-zero value) typically indicates that an error occurred
            # during execution.
            if process.returncode == 0:
                if "wget -qO" in command:
                    print(
                        Color.CAYN 
                        + f"\n/---/ PostgreSQL GPG key downloaded. /---/\n" + f"{stdout}" 
                        + Color.DEFAULT)
                elif command == "echo deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -sc)-pgdg main":
                    print(
                        Color.CAYN 
                        + f"\n/---/ PostgreSQL repository added. /---/\n" 
                        + f"{stdout}" 
                        + Color.DEFAULT)
                elif "install -y postgresql postgresql-contrib" in command:
                    print(
                        Color.CAYN 
                        + f"\n/---/ PostgreSQL installation complete. /---/\n" 
                        + f"{stdout}" 
                        + Color.DEFAULT)
                elif command == "systemctl status postgresql":
                    print(Color.YELLOW 
                          + f"\nStatus:\n{stdout}" 
                          + Color.DEFAULT)
                elif command == "psql --version":
                    print(Color.YELLOW 
                          + f"\nVersion:\n{stdout}" 
                          + Color.DEFAULT)
                elif command == "systemctl enable postgresql":
                    print(
                        Color.CAYN 
                        + f"\n/---/ PostgreSQL service enabled successfully. /---/\n" 
                        + f"{stdout}" 
                        + Color.DEFAULT)
                elif command == "systemctl start postgresql":
                    print(
                        Color.CAYN 
                        + f"\n/---/ PostgreSQL service started successfully. /---/\n" 
                        + f"{stdout}" 
                        + Color.DEFAULT)
                elif command == "systemctl stop postgresql":
                    print(
                        Color.CAYN 
                        + f"\n/---/ PostgreSQL service stopped successfully. /---/\n" 
                        + f"{stdout}" 
                        + Color.DEFAULT)
                elif command == "systemctl restart postgresql":
                    print(
                        Color.CAYN 
                        + f"\n/---/ PostgreSQL service restarted successfully. /---/\n" 
                        + f"{stdout}" + Color.DEFAULT)

            else:
                # print error if 'sudo -S' commands are used
                if len(args) == 3:
                    print(
                        Color.RED 
                        + f"\nPassword '{args[2]}' is incorrect or an error occurred.\n" 
                        + f"{stderr}" 
                        + Color.DEFAULT)
                # print error if 'sudo' commands are used
                else:
                    print(Color.RED 
                            + f"\nError occurred.\n" 
                            + f"{stderr}" 
                            + Color.DEFAULT)

        except subprocess.CalledProcessError as error:
            print(Color.RED +
                  f"\nError occurred.\nError:\n{error}" 
                  + Color.DEFAULT)
