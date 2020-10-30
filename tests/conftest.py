import os
from pathlib import Path

import pytest


@pytest.fixture()
def original_datadir(request):
	# Work around pycharm confusing datadir with test file.
	return Path(os.path.splitext(request.module.__file__)[0] + "_")
