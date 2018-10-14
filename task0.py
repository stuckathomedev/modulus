import tensorflow as tf

# In task 0:
cluster = tf.train.ClusterSpec({"local": ["128.119.225.161:2222", "serveo.net:1498"]})
server = tf.train.Server(cluster, job_name="local", task_index=0)

x = tf.constant(2)

# Assigning tasks
with tf.device("/job:local/task:1"):
    y2 = x - 66

with tf.device("/job:local/task:0"):
    y1 = x + 300
    y = y1 + y2


with tf.Session("grpc://localhost:2222") as sess:
    result = sess.run(y)
    print(result)

server.start()