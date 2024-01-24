# 0x02. Redis basic


















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








