from flask import Flask, request

app = Flask(__name__)
cluster_spec = {"ps": ["localhost:65062"], "worker": []}
#ps = tf.train.Server(cluster, job_name="ps", task_index=0)


@app.route("/api/get_cluster_spec")
def get_cluster_spec():
    return str(cluster_spec)


@app.route("/api/ready")
def is_ready():
    return str(False)


@app.route("/api/worker/add", methods=["POST"])
def add_worker():
    host = request.args["host"]
    cluster_spec['worker'].append(host)
    return get_cluster_spec()


@app.route("/api/worker/del", methods=["POST"])
def del_worker():
    host = request.args["host"]
    cluster_spec['worker'].remove(host)
    return get_cluster_spec()


if __name__ == '__main__':
    app.run(debug=True, port=9001)
