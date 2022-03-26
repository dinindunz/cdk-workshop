from aws_cdk import (
    core as cdk,
    aws_codedeploy as _codedeploy
)

class PiDeployStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, aws_account, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        stack_version='1.0.0'
        stack_name=self.stack_name

        pi_code_deploy_app=_codedeploy.ServerApplication(
            self, 'pi_code_deploy_app',
            application_name='Pi-Deploy-App'
        )

        pi_depoy_group=_codedeploy.ServerDeploymentGroup(
            self, 'pi_depoy_group',
            deployment_group_name='Pi-Deploy-Group',
            
        )