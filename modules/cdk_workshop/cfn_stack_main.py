from aws_cdk import (
    aws_lambda as _lambda,
    aws_apigateway as _apigw,
    core as cdk,
)
from modules.cdk_workshop.hitcounter import HitCounter
from cdk_dynamo_table_view import TableViewer

class CdkWorkshopStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, id: str, aws_account, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        my_lambda=_lambda.Function(
            self, 'HelloHandler',
            runtime=_lambda.Runtime.PYTHON_3_7,
            code=_lambda.Code.from_asset('modules/cdk_workshop/lambda'),
            handler='hello.handler',
        )

        hello_with_counter=HitCounter(
            self, 'HelloHitCounter',
            downstream=my_lambda,
        )

        _apigw.LambdaRestApi(
            self, 'Endpoint',
            handler=hello_with_counter._handler,
        )

        TableViewer(
            self, 'ViewHitCounter',
            title='Hello Hits',
            table=hello_with_counter.table
        )