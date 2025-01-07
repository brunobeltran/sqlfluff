from pathlib import Path
from typing import NamedTuple

from sqlfluff.core import FluffConfig, Linter
from sqlfluff.core.linter.linted_file import LintedFile


class LintOutput(NamedTuple):
    query: str
    result: LintedFile


def lint_query(query_file: Path | str) -> LintOutput:
    query_path = Path(query_file)
    config_file = query_path.parent / ".sqlfluff"
    config = (
        FluffConfig.from_path(str(config_file))
        if config_file.exists()
        else FluffConfig()
    )
    with open(query_path) as f:
        query = f.read()
    return LintOutput(query, Linter(config=config).lint_string(query))


# b ~/developer/sqlfluff/src/sqlfluff/rules/references/RF01.py:120
