class Error(Exception):
    pass


class RuntimeError(Error):
    '''Thrown when JavaScript runtime exits with non zero status'''
    def __init__(self, status, stdout, stderr):
        Error.__init__(self, status, stdout, stderr)
        self.status = status
        self.stdout = stdout
        self.stderr = stderr


class ProgramError(Error):
    '''Thrown when JavaScript script throws some exception'''
    pass


class RuntimeUnavailableError(Error):
    '''Thrown when JavaScript runtime is not available (e.g. not installed)'''
    pass
