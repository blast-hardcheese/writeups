An amusing challenge, "find an 0day in the scoreboard"

One way to pwn the scoreboard was via recognizing that the connection to the scoreboard itself is going over SSH, and that remote-to-local (`-L`) port forwarding was not disabled.

This permitted us to pull port 41337, the port bound by the `collect_keys.py` script, to the jumpbox.

Once we had direct access to the underlying scoreboard protocol, it permitted us to submit unsanitized input into into sqlite (irrelevant bits removed):

    clientsock.sendall("lol goatse")
    data = clientsock.recv(BUFF)
    data = data.strip().split(',')
    team_name, question_id, submitted_hash = data
    question_id = int(question_id)
    db = sqlite3.connect(config.PATH_TO_DB)
    dbc = db.cursor()
    dbc.execute('select challenge_name,point_value,answer_hash,solved from questions where rowid=(?)', [question_id])

Unfortunately, I was unable to finish this exploit. This was a fairly standard SQL injection, and was fun to find.
