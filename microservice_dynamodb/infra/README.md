# Microservice DynamoDB
A simple Flask API that is deployed to AWS and uses DynamoDB as a database.

## Development
Configure your AWS credentials:
```bash
aws configure --profile test
```
Bootstrap your AWS account:
```bash
cdk bootstrap aws://113106252872/us-west-2 --profile test
```
Deploy the stack:
```bash
cdk deploy --profile test
```
Build the stack:
```bash
npm run build
```
Destroy the stack:
```bash
cdk destroy --profile test
```