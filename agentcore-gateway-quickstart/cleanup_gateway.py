from bedrock_agentcore_starter_toolkit.operations.gateway.client import GatewayClient
import json

with open("gateway_config.json", "r") as f:
    config = json.load(f)

client = GatewayClient(region_name=config["region"])
client.cleanup_gateway(config["gateway_id"], config["client_info"])
print("✅ Cleanup complete!")
