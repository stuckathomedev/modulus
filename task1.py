import tensorflow as tf
import port_forward

# Using ngrok to get the port
host, port = port_forward.port_forward()
print(host)
# In task 1:
cluster = tf.train.ClusterSpec({"local": ["128.119.225.161:2222", "128.119.235.183:2223"]})
server = tf.train.Server(cluster, job_name="local", task_index=1)

server.start()
server.join()
