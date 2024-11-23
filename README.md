# Readme

This example shows how to solve these problems:

1. it is annoying to install private application libraries in databricks
2. it is annoying to install private application libraries in databricks

1 can be solved by just pushing the entire source code to databricks, but here we
will build a wheel in local / Ci.

2 is solved by building the library locally / in CI.

## Steps

setup uv:

```bash
uv init
uv venv
source .venv/bin/activate
uv sync --group dev
```

Setup databricks bundle and auth:

```bash
cp env.example .env
code .env
cp example.databricks.yml databricks.yml
yq e ".workspace.host=strenv(BUNDLE_VAR_workspace_host)" databricks.yml -i
databricks auth login --configure-cluster -p DEFAULT --host $BUNDLE_VAR_workspace_host
```

Apply bundle vars, deploy and run:

```bash
source .env
databricks bundle deploy
databricks bundle run
```

Build with lock is not supported: <https://github.com/astral-sh/uv/issues/5190>
it just emits what is in pyproject to METADATA

Instead, requirements.txt is added as a dependency in databricks.yml.

Uv does not seem to be able to build a specific library, so we use pip for that,
see databricks.yml.
