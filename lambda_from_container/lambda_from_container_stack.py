from aws_cdk import (
    aws_lambda as _lambda,
    aws_ecr as ecr,
    Stack,
    Aws
)
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
            ecr_repository = ecr.Repository.from_repository_attributes(
                self, 
                id="ECR",
                repository_arn="arn:aws:ecr:{0}:{1}".format(Aws.REGION, Aws.ACCOUNT_ID),
                repository_name=image_name
            )             
