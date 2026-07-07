import importlib.metadata
packages = ["langchain", "langchain-core", "langchain-groq", "pydantic"]
print("--- Package Versions ---")
for p in packages:
    try:
        print(f"{p}: {importlib.metadata.version(p)}")
    except importlib.metadata.PackageNotFoundError:
        print(f"{p}: Not Found")
