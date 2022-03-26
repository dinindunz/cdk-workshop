#!/bin/bash

vendor_id='M24W8QHNRLRFOB'
client_id='amzn1.application-oa2-client.6e1e1c74c38e408f96dcb693a2a2463a'
client_secret='005fbb344d50dba312338b3c9b8b43b61803f09c2230dd719c11cc7ae145e7af'
refresh_token='Atzr|IwEBIHyMu3953reXGQcy9yw0XrG2Uvm7nBvI6-B3fQ-ngZlMryuu6_QW7ldYuv9cQVwJV4epQFA3Bz5n534iZ6HE5OdFJtJ-QC5uTr6bQ84g3XqdDVlYm4fBA1_PX_yMYHvR1kMjL94kpuTwE86txJYpfcbJMtrR-V4xEzLEkPO1pr5Japl8pFPvvngPxHFQgXcWO-ik2ecy8uZKSSHFq0f4GW6rD1QBvGVEdQ2Z3mPZSjKJ5OaLHj7KD6DvfpXhOoT9fzgRYJOWQipWN8vJ_kBYGMys_9k9LBbJDtfGhu6Z0F-1Qm_RlCHa77IbOhF8SCIDYtG0aShI2E2mzYHS2anIdE8Sw1_MlK0sc-oBmaicZ3OdPDut0m3nQCKKfan7wiIz2-b_HkWx2m2ciixwNYf4AZZ5JdmsruSzLUopV83uJI_CChgORdbWg_P0BGmQ2e2Nk63cra-zt53gCscybZxomNuSJ4Q0Jlwcd61SS2sOONfCucdfcOrlxki9PUHPLR4dxfU'

aws ssm put-parameter --overwrite --name '/alexa-cdk-blog/alexa-developer-vendor-id' --type 'String' --value $vendor_id --profile din_tooling
aws ssm put-parameter --overwrite --name '/alexa-cdk-blog/lwa-client-id' --type 'String' --value $client_id --profile din_tooling
aws secretsmanager create-secret  --name '/alexa-cdk-blog/lwa-client-secret' --secret-string $client_secret --profile din_tooling
aws secretsmanager create-secret  --name '/alexa-cdk-blog/lwa-refresh-token' --secret-string $refresh_token --profile din_tooling
