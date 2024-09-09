aws neptune create-db-cluster \
    --db-cluster-identifier my-neptune-cluster \
    --engine neptune \
    --master-username <your-username> \
    --master-user-password <your-password>


  aws neptune create-db-instance \
    --db-instance-identifier my-neptune-instance \
    --db-instance-class db.r5.large \
    --engine neptune \
    --db-cluster-identifier my-neptune-cluster


  aws neptune describe-db-clusters --db-cluster-identifier my-neptune-cluster



aws neptune create-db-subnet-group \
    --db-subnet-group-name my-neptune-subnet-group \
    --db-subnet-group-description "My Neptune subnet group" \
    --subnet-ids <subnet-id-1> <subnet-id-2>


aws neptune create-db-cluster \
    --db-cluster-identifier my-neptune-cluster \
    --engine neptune \
    --master-username <your-username> \
    --master-user-password <your-password> \
    --db-subnet-group-name my-neptune-subnet-group \
    --vpc-security-group-ids <security-group-id>


aws neptune create-db-instance \
    --db-instance-identifier my-neptune-instance \
    --db-instance-class db.r5.large \
    --engine neptune \
    --db-cluster-identifier my-neptune-cluster



# Create a security group with a description for Neptune and DynamoDB access
aws ec2 create-security-group \
    --group-name my-neptune-sg \
    --description "Security group for Neptune and DynamoDB access" \
    --vpc-id <your-vpc-id>



# Allow inbound access to Neptune (Gremlin) from your IP or trusted IP range
aws ec2 authorize-security-group-ingress \
    --group-id <security-group-id> \
    --protocol tcp \
    --port 8182 \
    --cidr <your-ip>/32  # Replace <your-ip> with your actual IP or range

# Allow inbound access to DynamoDB via HTTPS (Port 443)
aws ec2 authorize-security-group-ingress \
    --group-id <security-group-id> \
    --protocol tcp \
    --port 443 \
    --cidr 0.0.0.0/0  # Open for DynamoDB access (can be restricted by CIDR if needed)


# Allow outbound traffic to DynamoDB
aws ec2 authorize-security-group-egress \
    --group-id <security-group-id> \
    --protocol tcp \
    --port 443 \
    --cidr 0.0.0.0/0



