
class CommandLocal:

    def __init__(self, connection, taskConfig, logging):
        self.command = taskConfig["command"]
        self.connection = connection
        self.logging = logging

    def run(self):
        self.connection.execute_local(self.command)