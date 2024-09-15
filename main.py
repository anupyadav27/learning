import os
import logging
from google.cloud import resourcemanager_v3
from neo4j import GraphDatabase

# Configure logging
logging.basicConfig(level=logging.INFO)

# Function to fetch enabled GCP resources
def fetch_gcp_resources():
    client = resourcemanager_v3.ProjectsClient()
    enabled_resources = []
    for project in client.list_projects():
        if project.state == resourcemanager_v3.Project.State.ACTIVE:
            enabled_resources.append(project.project_id)
    return enabled_resources

# Neo4j connection setup using environment variables
uri = "neo4j+s://7d76c4ea.databases.neo4j.io"
username = "neo4j"
password = "JZXfDTU7pl8wOPfrnaUujXnX8zvanhYn_bn5j53NeXg"

# Function to upload resources to Neo4j
def upload_to_neo4j(enabled_resources):
    driver = GraphDatabase.driver(uri, auth=(username, password))
    with driver.session() as session:
        for resource in enabled_resources:
            session.run("MERGE (r:Resource {name: $name})", name=resource)
    driver.close()

# Main function to run as a Cloud Run Job
def main():
    try:
        logging.info("Fetching enabled GCP resources...")
        enabled_resources = fetch_gcp_resources()
        logging.info(f"Fetched {len(enabled_resources)} resources.")

        logging.info("Uploading resources to Neo4j...")
        upload_to_neo4j(enabled_resources)
        logging.info("Data uploaded to Neo4j successfully.")

    except Exception as e:
        logging.error(f"Error occurred: {str(e)}")

if __name__ == "__main__":
    main()
