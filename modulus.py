import tensorflow as tf


cluster = tf.train.ClusterSpec({"ps": ["localhost:65062"], "worker": ["localhost:65063"]})
ps = tf.train.Server(cluster, job_name="ps", task_index=0)
worker = tf.train.Server(cluster, job_name="worker", task_index=0)

print("PS: {0}".format(ps.target))
print("Worker: {0}".format(worker.target))

ps.join()
