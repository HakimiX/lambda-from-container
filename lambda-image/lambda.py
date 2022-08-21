import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def handler(event, context):
  logger.info("incoming event: {}".format(event))

  return {
    "statusCode": 200,
    "body": "success"
  }