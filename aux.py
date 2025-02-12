import jax 
import time

def time_loop_method(func, params):
    start = time.time()
    for p in params:
        res = func(p).block_until_ready()
    return time.time() - start

def time_vectorized_method(func, params):
    start = time.time()
    res = func(params).block_until_ready()
    return time.time() - start


def get_batch_params(batch_size, key):
    key, subkey = jax.random.split(key)
    return jax.random.uniform(subkey, shape=(batch_size,))