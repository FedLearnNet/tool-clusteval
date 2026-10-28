from pathlib import Path
from typing import Any

from pydantic.dataclasses import dataclass
from pyfedappwrap.learning.run_runfig import AppConfig, AppInputConfig, AppOutputConfig


@dataclass
class MyAppConfig(AppConfig):
    """Configuration for ClustEval clustering evaluation app."""

    clustering_algorithm: str =  None
    evaluation_method: str =  None
    linkage: str =  None
    max_clusters: int = None


@dataclass
class MyAppInputConfig(AppInputConfig):
    """Input configuration for ClustEval app."""
    data: Any = None


@dataclass
class MyAppOutputConfig(AppOutputConfig):
    """Output configuration for ClustEval app."""

    cluster_scores: Path | None = None
    silhouette_plot: Path | None = None
    scatter_plot: Path | None = None
