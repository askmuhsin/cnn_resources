import tensorflow as tf
## Variables
## A TensorFlow variable is the best way to represent shared, persistent state
## manipulated by your program.
## Create a variable.
w = tf.Variable(<initial-value>, name=<optional-name>)
## The best way to create a variable is to call the tf.get_variable function.
## This function requires you to specify the Variable's name.
## This name will be used by other replicas to access the same variable,
## as well as to name this variable's value when checkpointing and exporting models.
## tf.get_variable also allows you to reuse a previously created variable of the
## same name, making it easy to define models which reuse layers.
my_variable = tf.get_variable("my_variable", [1, 2, 3])
