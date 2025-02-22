# SchemaRegistry Performance Tests

In order to run the performance tests, the `azure-devtools` package must be installed. This is done as part of the `dev_requirements`.
Start by creating a new virtual environment for your perf tests. This will need to be a Python 3 environment, preferably >=3.7.

### Setup for test resources

These tests will run against a pre-configured SchemaRegistry. The following environment variable will need to be set for the tests to access the live resources:
```
SCHEMAREGISTRY_FULLY_QUALIFIED_NAMESPACE=<the connection string of a Schema Registry.>
SCHEMAREGISTRY_GROUP=<a schema group in a Schema Registry.>
```

### Setup for perf test runs

```cmd
(env) ~/azure-schemaregistry> pip install -r dev_requirements.txt
(env) ~/azure-schemaregistry> pip install -e .
```

## Test commands

When `azure-devtools` is installed, you will have access to the `perfstress` command line tool, which will scan the current module for runable perf tests. Only a specific test can be run at a time (i.e. there is no "run all" feature).

```cmd
(env) ~/azure-schemaregistry> cd tests
(env) ~/azure-schemaregistry/tests> perfstress
```
Using the `perfstress` command alone will list the available perf tests found.

### Common perf command line options
These options are available for all perf tests:
- `--duration=10` Number of seconds to run as many operations (the "run" function) as possible. Default is 10.
- `--iterations=1` Number of test iterations to run. Default is 1.
- `--parallel=1` Number of tests to run in parallel. Default is 1.
- `--warm-up=5` Number of seconds to spend warming up the connection before measuring begins. Default is 5.
- `--sync` Whether to run the tests in sync or async. Default is False (async).
- `--no-cleanup` Whether to keep newly created resources after test run. Default is False (resources will be deleted).

### Schema Registry command line options
The options are available for all SR perf tests:
- `--schema-size=150` Number of bytes each schema contains, rounded down to nearest multiple of 50. Default is 150.
- `--num-schemas` Number of schemas to register/get by ID/get properties for. Default is 10. May result in 'Forbidden' Exception for `RegisterSchemaTest` operation, if reached the limit of schemas allowed for Schema Registry tier.

### T2 Tests
The tests currently written for the T2 SDK:
- `RegisterSchemaTest` Registers `num-schemas` of size `schema-size` per run.
- `GetSchemaByIdTest` Gets a registered schema of `schema-size` size `num-schemas` number of times.
- `ReceiveEventBatchTest` Gets properties of a registered schema of `schema-size` size `num-schemas` number of times.

## Example command
```cmd
(env) ~/azure-schemaregistry/tests> perfstress GetSchemaByIdTest --parallel=2 --duration=100 --schema-size=500 --num-schemas=100
```
