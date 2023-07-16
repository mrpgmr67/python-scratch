import tensorflow as tf

# Check for GPU availability
gpus = tf.config.list_physical_devices('GPU')
if not gpus:
    print("No GPU available. Running on CPU.")
    tf.config.set_visible_devices([], 'GPU')
else:
    # Limit GPU memory growth
    for gpu in gpus:
        tf.config.experimental.set_memory_growth(gpu, True)
    print("GPU available. Running on GPU.")

# Rest of your code
