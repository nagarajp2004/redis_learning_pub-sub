import redis

def listen():
    r = redis.Redis(host='localhost', port=6379, db=0)
    pubsub = r.pubsub()
    pubsub.subscribe('mychannel')
    print("Listening to 'mychannel'...")

    for msg in pubsub.listen():
        if msg['type'] == 'message':
            print("📩 Received:", msg['data'].decode())

if __name__ == "__main__":
    listen()
