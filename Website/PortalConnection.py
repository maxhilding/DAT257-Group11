import psycopg2


class PortalConnection:
    def __init__(self):
        self.conn = psycopg2.connect(
            host="localhost",
            user="postgres",
            password="elefantSQL")
        self.conn.autocommit = True

    def getInfo(self):
      with self.conn.cursor() as cur:
        # Here's a start of the code for this part
        sql = """
                SELECT jsonb_build_object(
                     'lon', 'lat'
                ) :: TEXT
                FROM Locations;"""
        cur.execute(sql, ())
        res = cur.fetchall()
        if res:
            return (str(res[0]))
        else:
            return """{"fountain":"Not found :("}"""


def getError(e):
    message = repr(e)
    message = message.replace("\\n"," ")
    message = message.replace("\"","\\\"")
    return message

