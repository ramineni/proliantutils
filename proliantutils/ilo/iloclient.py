import ris
import ribcl

class IloClient(object) :
    
    def __new__(self, host, login, password, timeout=60, port=443, bios_password=None ):
         
        client = ribcl.RIBCLClient(host, login, password, timeout, port)
        model = client.get_product_name()
         
        if 'Gen9' in model:
            client = ris.RISClient(host, login, password, bios_password)
        
        return client
    
class IloError(Exception):
    """This exception is used when a problem is encountered in
    executing an operation on the iLO
    """
    def __init__(self, message, errorcode=None):
        super(IloError, self).__init__(message)


class IloClientInternalError(IloError):
    """This exception is raised when iLO client library fails to
    communicate properly with the iLO
    """
    def __init__(self, message, errorcode=None):
        super(IloError, self).__init__(message)

class IloCommandNotSupportedError(IloError):
    """This exception is raised when iLO client library fails to
    communicate properly with the iLO
    """
    def __init__(self, message, errorcode=None):
        super(IloError, self).__init__(message)


class IloLoginFailError(IloError):
    """This exception is used to communicate a login failure to
    the caller.
    """
    messages = ['User login name was not found',
                    'Login failed', 'Login credentials rejected']
    statuses = [0x005f, 0x000a]
    message = 'Authorization Failed'
    def __init__(self, message, errorcode=None):
        super(IloError, self).__init__(message)
        

class IloConnectionError(IloError):
    """This exception is used to communicate an HTTP connection
    error from the iLO to the caller.
    """
    def __init__(self, message):
        super(IloConnectionError, self).__init__(message)


class IloInvalidInputError(IloError):
    """This exception is used when invalid inputs are passed to
    the APIs exposed by this module.
    """
    def __init__(self, message):
        super(IloInvalidInputError, self).__init__(message)
