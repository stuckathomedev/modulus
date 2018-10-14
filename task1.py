import tensorflow as tf

# In task 1:
cluster = tf.train.ClusterSpec({"local": ["localhost:2222", "localhost:2223"]})
server = tf.train.Server(cluster, job_name="local", task_index=1)

x = tf.constant(2)

server.start()
server.join()
