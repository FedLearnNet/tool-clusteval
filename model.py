import os

from clusteval import clusteval


def execute_clustering_evaluation(clusteval_object, dataset, output_dir: str):
    """Execute clustering evaluation and generate plots"""
    results = clusteval_object.fit(dataset)
    print(results)
    print(results["max_d"])
    print(results["max_d_lower"])  # DB index frequently overshoots. Use these to finetune.
    print(results["max_d_upper"])

    if clusteval_object.cluster == "hdbscan":
        print("Get results")  # TODO Not much to acquire.
    elif clusteval_object.evaluate == "dbindex":
        print(
            results["fig"]["scores"]
        )  # TODO Show average? #For silhouette Many low or negative ones indicate too many or too few clusters. For DB index: Many low ones better
    else:
        print(
            results["fig"]["silscores"]
        )  # For silhouette Many low or negative ones indicate too many or too few clusters. For DB index: Many low ones better

    # Generate plots
    clusteval_object.plot(
        savefig={
            'dpi': 300,  # Set DPI for high resolution
            'facecolor': 'auto',  # Use auto facecolor
            'fname': os.path.join(output_dir, "num_of_cluster_scores.png"),  # File name to save
            'format': 'png',  # File format
            'orientation': 'portrait'  # Orientation
        },
    )
    clusteval_object.plot_silhouette(
        savefig={
            'dpi': 300,  # Set DPI for high resolution
            'facecolor': 'auto',  # Use auto facecolor
            'fname': os.path.join(output_dir, 'silhouette_plot.png'),  # File name to save
            'format': 'png',  # File format
            'orientation': 'portrait'  # Orientation
        },
    )  # Only the first two features can be used
    clusteval_object.scatter(
        savefig={
            'dpi': 300,  # Set DPI for high resolution
            'facecolor': 'auto',  # Use auto facecolor
            'fname': os.path.join(output_dir, 'scatter_plot.png'),  # File name to save
            'format': 'png',  # File format
            'orientation': 'portrait'  # Orientation
        },
    )  # Only the first two features can be used


def choose_method_and_execute(clustering_alg: str, evaluation_method: str, linkage: str,
                              dataset, max_clusters: int, output_dir: str):
    """Choose clustering method and execute evaluation"""
    c = None

    if len(clustering_alg) == 0 and len(evaluation_method) == 0 and len(linkage) == 0:
        c = clusteval()
    elif len(clustering_alg) > 0 and len(evaluation_method) == 0:
        c = clusteval(cluster=clustering_alg)
    elif len(clustering_alg) == 0 and len(evaluation_method) > 0:
        c = clusteval(evaluate=evaluation_method)
    else:
        c = clusteval(cluster=clustering_alg, evaluate=evaluation_method)

    if max_clusters > -1:  # default value is 25
        c.max_clust = max_clusters

    if len(linkage) != 0:
        c.linkage = linkage

    execute_clustering_evaluation(c, dataset, output_dir=output_dir)
