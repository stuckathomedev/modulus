from flask import Flask, request

api = Flask(__name__)
cluster_spec = {"ps": ["localhost:65062"], "worker": []}
#ps = tf.train.Server(cluster, job_name="ps", task_index=0)


@api.route("/api/get_cluster_spec")
def get_cluster_spec():
    return str(cluster_spec)


@api.route("/api/ready")
def is_ready():
    return str(False)


@api.route("/api/worker/add", methods=["POST"])
def add_worker():
    host = request.args["host"]
    cluster_spec['worker'].append(host)
    return get_cluster_spec()


@api.route("/api/worker/del", methods=["POST"])
def del_worker():
    host = request.args["host"]
    cluster_spec['worker'].remove(host)
    return get_cluster_spec()