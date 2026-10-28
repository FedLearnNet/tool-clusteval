from pyfedappwrap.engine.runtime import FedDBEngine
from app import ClusterEval

engine = FedDBEngine()
engine.register(ClusterEval())
if __name__ == "__main__":
    engine.start()
    engine.wait_until_stop()
