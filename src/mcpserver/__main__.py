#mcpserver is the folder we created in src, deployment is file and mcp is the object , mcp = FastMCP("Demo")
from mcpserver.deployment import mcp 

def main():
    mcp.run()


#to trigger the script
if __name__ == "__main__":
    main()