import os

from dotenv import load_dotenv
from pydantic import BaseModel
from utils import file_path


class Settings(BaseModel):
    context: str
    var1: str = os.getenv('var1')
    var_em: str = os.getenv('var_em')
    var_re: str = os.getenv('var_re')
    var_bs: str = os.getenv('var_bs')

    login: str = os.getenv('LOGIN')
    password: str = os.getenv('PASSWORD')
    appWaitActivity: str = os.getenv('appWaitActivity')
    remote_url: str = os.getenv('remote_url')
    udid: str = os.getenv('udid')
    app: str = os.getenv('app')
    platformVersion: str  = os.getenv('platformVersion')
    deviceName: str = os.getenv('deviceName')
    projectName: str = os.getenv('projectName')
    buildName: str = os.getenv('buildName')
    sessionName: str = os.getenv('sessionName')


    def to_driver_options(self, context):
        options: str = '0000000'

        if context == 'local_emulator':
            options: str = {
                'app': file_path.abs_path_from_project(self.app),
                'appWaitActivity': self.appWaitActivity,
                'udid': self.udid,
            }

        if context == 'local_real':
            options: str = {
                'app': file_path.abs_path_from_project(self.app),
                'appWaitActivity': self.appWaitActivity,
                'udid': self.udid
            }

        if context == 'bstack':
            options: str = {
                'platformVersion': self.platformVersion,
                'deviceName': self.deviceName,
                'app': self.app,
                'bstack:options': {
                    'projectName': self.projectName,
                    'buildName': self.buildName,
                    'sessionName': self.sessionName,
                    'userName': self.login,
                    'accessKey': self.password,
                }
            }

        print(f'options_to_driver_optionc = {options}')

        return options


settings = Settings(context="local_emulator")