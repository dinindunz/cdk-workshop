from aws_cdk import (
    core as cdk
)
from modules.cdk_workshop.cfn_stack_main import CdkWorkshopStack
from modules.plant_status.cfn_stack_main import PlantStatusStack
from common.get_environment import GetEnvironment

class DeployModules(cdk.Stage):

    def __init__(self, scope: cdk.Construct, id: str, aws_account, **kwargs):
        super().__init__(scope, id, **kwargs)

        tooling_env=GetEnvironment.aws_enviromnet('tooling')
        dev_env=GetEnvironment.aws_enviromnet('dev')
        prod_env=GetEnvironment.aws_enviromnet('prod')

        PlantStatusStack(self, 'Plant-Status-Stack', aws_account, env=tooling_env[0])