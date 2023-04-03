def token(seconds):
    s=Serializer(app.configp['SECRET_KEY'],seconds)
    return s.dumps({'user':rollno}).decode('utf-8')
