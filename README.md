# clusteval

Evaluates clustering results with ClustEval and exports quality scores and visual reports.

## Runtime inputs

Supply input files according to the schemas in `app.yml`.

## Inputs and outputs

### Inputs

| Name | Type | Description |
| --- | --- | --- |
| `data` | CSV | Data in CSV format |

### Outputs

| Name | Type | Description |
| --- | --- | --- |
| `cluster_scores` | IMAGE | Clustering evaluation scores plot. |
| `silhouette_plot` | IMAGE | Silhouette analysis plot. |
| `scatter_plot` | IMAGE | Scatter plot of clustered data. |

## Configuration

| Name | Default | Description |
| --- | --- | --- |
| `clustering_algorithm` | `agglomerative` | Clustering algorithm to use. |
| `evaluation_method` | `silhouette` | Evaluation method for clustering. |
| `linkage` | `ward` | Linkage method for hierarchical clustering. |
| `max_clusters` | `25` | Maximum number of clusters (-1 for no restriction). |

## Development

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
cp .env.example .env
# Set APP_ID and platform URLs before connecting.
python main.py
```

The Docker base image provides the FL-Net API. `requirements.txt` lists additional
runtime dependencies; `requirements-dev.txt` includes the API for local development.
Runtime datasets and trained models must be supplied separately; see `data/README.md`.

Build with `docker build -t tool-clusteval .`.
