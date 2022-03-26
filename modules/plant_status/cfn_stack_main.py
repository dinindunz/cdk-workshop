from aws_cdk import (
    core as cdk,
    aws_ssm as _ssm,
    aws_lambda_python as _lambPi
)
import cdk_alexa_skill as _ask

class PlantStatusStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, aws_account, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        stack_version='1.0.0'

        alexa_vendor_id=_ssm.StringParameter.value_for_string_parameter(self, '/alexa-cdk-blog/alexa-developer-vendor-id')
        lwa_client_id=_ssm.StringParameter.value_for_string_parameter(self, '/alexa-cdk-blog/lwa-client-id')
        lwa_client_secret=cdk.SecretValue.secrets_manager('/alexa-cdk-blog/lwa-client-secret')
        lwa_refresh_token=cdk.SecretValue.secrets_manager('/alexa-cdk-blog/lwa-refresh-token')


        skill_backend=_lambPi.PythonFunction(
            self, 'skill_backend',
            entry='modules/plant_status/src/lambda/alexa_skill_backend',
            timeout=cdk.Duration.seconds(10)
        )

        alexa_skill=_ask.Skill(
            self, 'alexa_skill',
            endpoint_lambda_function=skill_backend,
            skill_package_path='modules/plant_status/src/alexa_skill_package',
            alexa_vendor_id=alexa_vendor_id,
            lwa_client_id=lwa_client_id,
            lwa_client_secret=lwa_client_secret,
            lwa_refresh_token=lwa_refresh_token
        )