#!/usr/bin/env python3
import os

import aws_cdk as cdk

from lambda_from_container.lambda_from_container_stack import LambdaFromContainerStack


app = cdk.App()
LambdaFromContainerStack(app, "LambdaFromContainerStack")

app.synth()
