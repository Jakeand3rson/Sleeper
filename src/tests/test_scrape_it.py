import pytest
import os
from .. import scrape_it


def test_missing_email():
    os.environ['SLACK_EMAIL'] = None
    with pytest.raises(LookupError):
        scrape_it.main()
