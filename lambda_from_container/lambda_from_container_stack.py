from aws_cdk import (
    aws_lambda as _lambda,
    aws_ecr as ecr,
    Stack,
    Aws,
    App,
    Duration
)
import os
import typing
from constructs import Construct

class LambdaFromContainerStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        image_name = "lambdaContainerFunction"

        """
        if use_pre_existing_image is True
        then use an image that already exists in ECR.
        Otherwise, build a new image
        """
        use_pre_existing_iamge = False

        if (use_pre_existing_iamge):
            # If the image exists, use the the pre-existing image. 
            ecr_repository = ecr.Repository.from_repository_attributes(
                self, 
                id="ECR",
                repository_arn="arn:aws:ecr:{0}:{1}".format(Aws.REGION, Aws.ACCOUNT_ID),
                repository_name=image_name
            )             

            # pull the existing image 
            ecr_image = typing.cast("aws_lambda.Code", _lambda.EcrImageCode(
                repository=ecr_repository
            ))
        else:
            # if the image does not exist, create the image 
            ecr_image = _lambda.EcrImageCode.from_asset_image(
                directory=os.path.join(os.getcwd(), "lambda-image")
            )


        # Lambda function 
        _lambda.Function(
            self, 
            id="lambdaContainerFunction",
            description="sample lambda container function",
            code = ecr_image,
            # Handler must be "FROM_IMAGE" when provisioning lambda from image
            handler = _lambda.Handler.FROM_IMAGE,
            runtime = _lambda.Runtime.FROM_IMAGE,
            environment={
                "HELLO": "WORLD"
            },
            function_name="sampleContainerFuntion",
            memory_size=128,
            reserved_concurrent_executions=10,
            timeout=Duration.seconds(10)
        )