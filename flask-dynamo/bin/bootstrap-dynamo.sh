#!/bin/bash

echo "Running local instance of DynamoDB"
docker-compose up -d dynamodb-local

# Get list of tables
tables=$(aws dynamodb list-tables --endpoint-url http://localhost:8000 \
        | python -c "import sys, json; print(' '.join(json.load(sys.stdin)['TableNames']))")

# Delete each table
for table in $tables
do
    echo "Deleting table $table"
    aws dynamodb delete-table --table-name $table --endpoint-url http://localhost:8000
done

echo "Creating the tables"
aws dynamodb create-table \
    --table-name ExampleTable \
    --attribute-definitions \
        AttributeName=ExampleTableID,AttributeType=S \
        AttributeName=ExampleTableSort,AttributeType=S \
    --key-schema AttributeName=ExampleTableID,KeyType=HASH AttributeName=ExampleTableSort,KeyType=RANGE \
    --provisioned-throughput ReadCapacityUnits=1,WriteCapacityUnits=1 \
    --table-class STANDARD \
    --endpoint-url http://localhost:8000

# List the tables
echo "Tables created:"
aws dynamodb list-tables --endpoint-url http://localhost:8000