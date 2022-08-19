import aws_cdk as core
import aws_cdk.assertions as assertions

from lambda_from_container.lambda_from_container_stack import LambdaFromContainerStack

# example tests. To run these tests, uncomment this file along with the example
# resource in lambda_from_container/lambda_from_container_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = LambdaFromContainerStack(app, "lambda-from-container")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
