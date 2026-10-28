from pathlib import Path
from typing import Optional

from pyfedappwrap.learning.app_types import BaseEvaluationApp
from typing_extensions import override

from config import MyAppConfig, MyAppInputConfig, MyAppOutputConfig
from model import choose_method_and_execute


class ClusterEval(BaseEvaluationApp[MyAppConfig, MyAppInputConfig, MyAppOutputConfig]):
    """ClustEval clustering evaluation application."""

    def run_evaluate(self, data: MyAppInputConfig) -> MyAppOutputConfig:
        """Run ClustEval clustering evaluation prediction."""
        self.logger.info("Starting ClustEval prediction...")

        output_dir = Path("./output")
        output_dir.mkdir(exist_ok=True, parents=True)
        df = data.data
        choose_method_and_execute(
            clustering_alg=self.config.clustering_algorithm,
            evaluation_method=self.config.evaluation_method,
            linkage=self.config.linkage,
            dataset=df,
            max_clusters=self.config.max_clusters,
            output_dir=str(output_dir),
        )

        self.logger.info("Finished ClustEval prediction.")
        return MyAppOutputConfig(
            cluster_scores=output_dir / "num_of_cluster_scores.png",
            silhouette_plot=output_dir / "silhouette_plot.png",
            scatter_plot=output_dir / "scatter_plot.png"
        )

    @override
    def get_test_data(self) -> Optional[dict[str, Path]]:
        return {"data": Path("data/X.csv")}
