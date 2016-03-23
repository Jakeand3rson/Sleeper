import pytest
import os
from .. import scrape_it


ENV_VARS = ["SLACK_EMAIL", "SLACK_PASSWORD"]


@pytest.mark.parametrize('env_var', ENV_VARS)
def test_missing_slack_credentials(env_var):
    """Ensure that we don't start the browser without credentials."""
    try:
        del os.environ[env_var]
    except KeyError:
        # If the env_var is already missing, we're in the right situation.
        pass

    with pytest.raises(LookupError):
        scrape_it.main()
