name: Deploying multiple Lambdas
on:
    workflow_dispatch:
jobs:
  PCI_Audit:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Setup AW CLI
        uses: aws-actions/configure-aws-credentials@v2
        with:
          aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
          aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
          aws-region: us-east-2
      - run: zip -j DatadogLambda.zip ./DatadogLambda/*
      - run: aws lambda update-function-code --function-name=PCI_Audit --zip-file=fileb://PCI_Audit.zip

#   lambda2:
#     runs-on: ubuntu-latest
#     steps:
#       - uses: actions/checkout@v3
#       - uses: actions/setup-node@v3
#         with:
#           node-version: 16
#       - uses: aws-actions/configure-aws-credentials@v2
#         with:
#           aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
#           aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
#           aws-region: us-east-2
#       - run: zip -j lambda2.zip ./lambda2/index.js
#       - run: aws lambda update-function-code --function-name=lambda1  --zip-file=fileb://lambda1.zip
