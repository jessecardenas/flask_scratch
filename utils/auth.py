from utils import auth_mock

def check_auth(usr, pwd, auth_source='mock'):
    '''Return True or False'''
    if auth_source == 'mock':
        return auth_mock.check_auth(usr, pwd)
    # Add your alternate auth backend here
    # if auth_source == 'mysql':
    #   return mysql.check_auth(usr, pwd)
    return False # not implemented



