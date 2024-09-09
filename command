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
