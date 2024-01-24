# 0x02. Redis basic

![40eab4627f1bea7dfe5e](https://github.com/elyse502/alx-backend-storage/assets/125453474/050b93c8-02e7-4122-9291-6a1edff20fda)

# Resources🏗️
### Read or watch:
* [Redis commands](https://redis.io/commands/)
* [Redis python client](https://redis-py.readthedocs.io/en/stable/)
* [How to Use Redis With Python](https://realpython.com/python-redis/)
* [Redis Crash Course Tutorial](https://www.youtube.com/watch?v=Hbt56gFj998)

# Learning Objectives 📖
At the end of this project, you are expected to be able to [explain to anyone](https://fs.blog/feynman-learning-technique/), **without the help of Google**:
## General🧵
* Learn how to use redis for basic operations
* Learn how to use redis as a simple cache

# Requirements 🏛️
* All of your files will be interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7)
* All of your files should end with a new line
* A `README.md` file, at the root of the folder of the project, is mandatory
* The first line of all your files should be exactly `#!/usr/bin/env python3`
* Your code should use the `pycodestyle style` (version 2.5)
* All your modules should have documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
* All your classes should have documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
* All your functions and methods should have documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
* A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
* All your functions and coroutines must be type-annotated.

# Install Redis on Ubuntu 18.04 💼
```groovy
$ sudo apt-get -y install redis-server
$ pip3 install redis
$ sed -i "s/bind .*/bind 127.0.0.1/g" /etc/redis/redis.conf
```

# Use Redis in a container
Redis server is stopped by default - when you are starting a container, you should start it with: `service redis-server start`

# Tasks 📃
## 0. Writing strings to Redis: [exercise.py](exercise.py)
Create a `Cache` class. In the `__init__` method, store an instance of the Redis client as a private variable named `_redis` (using `redis.Redis()`) and flush the instance using `flushdb`.

Create a `store` method that takes a `data` argument and returns a string. The method should generate a random key (e.g. using `uuid`), store the input data in Redis using the random key and return the key.

Type-annotate `store` correctly. Remember that `data` can be a `str`, `bytes`, `int` or `float`.
```groovy
bob@dylan:~$ cat main.py
#!/usr/bin/env python3
"""
Main file
"""
import redis

Cache = __import__('exercise').Cache

cache = Cache()

data = b"hello"
key = cache.store(data)
print(key)

local_redis = redis.Redis()
print(local_redis.get(key))

bob@dylan:~$ python3 main.py 
3a3e8231-b2f6-450d-8b0e-0f38f16e8ca2
b'hello'
bob@dylan:~$
```

## 1. Reading from Redis and recovering original type: [exercise.py](exercise.py)
Redis only allows to store string, bytes and numbers (and lists thereof). Whatever you store as single elements, it will be returned as a byte string. Hence if you store `"a"` as a UTF-8 string, it will be returned as `b"a"` when retrieved from the server.

In this exercise we will create a `get` method that take a `key` string argument and an optional `Callable` argument named `fn`. This callable will be used to convert the data back to the desired format.

Remember to conserve the original `Redis.get` behavior if the key does not exist.

Also, implement 2 new methods: `get_str` and `get_int` that will automatically parametrize `Cache.get` with the correct conversion function.

The following code should not raise:
```groovy
cache = Cache()

TEST_CASES = {
    b"foo": None,
    123: int,
    "bar": lambda d: d.decode("utf-8")
}

for value, fn in TEST_CASES.items():
    key = cache.store(value)
    assert cache.get(key, fn=fn) == value
```    

##



































<div align="center">
    
# ♟️ Reference 📚

</div>

## Troubleshooting
1. **Check if Redis is Running:**

Ensure that the Redis server is running on your machine. You can check this by running:

```groovy
redis-server
```
If it's not running, start it with:

```groovy
redis-server
```

2. **Verify Redis Configuration:**

Open your Redis configuration file, typically located at `/etc/redis/redis.conf`. Check if it's configured to bind to `localhost`. The line should look like this:

```groovy
bind 127.0.0.1
```
If it's commented out (`#` at the beginning of the line), uncomment it and restart Redis.

3. **Check for Other Processes Using Port 6379:**

It's possible that another process is using the same port. You can check this using the following command:

```groovy
sudo lsof -i :6379
```
If another process is using the port, you might need to stop that process or configure Redis to use a different port.

4. **Check Network Configuration:**

Ensure that there are no network issues preventing the connection. The error suggests that there might be an issue with the network configuration.

5. **Restart Redis:**

After making changes to the Redis configuration, restart the Redis server:

```groovy
sudo service redis-server restart
```
6. **Check Firewall Settings:**

If you have a firewall enabled, ensure that it allows connections to port 6379.

















