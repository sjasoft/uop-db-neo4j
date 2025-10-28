from uop.core.plugin_testing.harness import test_general_db, db_harness

# By importing these fixtures, pytest will automatically discover and use them.
# The `db_harness` fixture will be created using the `db_plugin` fixture
# defined in conftest.py. The `test_general_db` function will then be
# run with the fully configured harness.

# This file is intentionally simple. The actual test logic is in the harness.