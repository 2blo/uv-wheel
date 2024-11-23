# Readme

```bash
uv init
uv venv
source .venv/bin/activate
uv export --extra databricks_15_4  --format requirements-txt --output-file requirements.txt --no-hashes --no-editable --no-emit-project
databricks auth login --configure-cluster -p DEFAULT --host $BUNDLE_VAR_workspace_host
cp env.example .env
code .env
source .env
cp example.databricks.yml databricks.yml
yq e ".workspace.host=strenv(BUNDLE_VAR_workspace_host)" databricks.yml -i
databricks bundle deploy
databricks bundle run
```

Build with lock is not supported: <https://github.com/astral-sh/uv/issues/5190>
it just emits what is in pyproject to METADATA

Instead, requirements.txt is added as a dependency in databricks.yml.

Build a specific package, without its dependencies:

```bash
python -m pip wheel -w pip_dist "deutils @ git+https://github.com/2blo/deutils.git@1.0.0" --no-deps
```

Includes deps of deutils unfortunately

```bash
uv export --extra deutils  --format requirements-txt --output-file deutils.requirements.txt --no-hashes --no-editable --no-emit-project --only-group deutils
```

python -m pip wheel -w pip_dist "deutils @ git+<https://github.com/2blo/deutils.git@1.0.0>" --no-deps

```

This is nice, because your librarie are usually architecture agnostic,
but dependencies like pandas are not.
