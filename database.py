from sqlalchemy import create_engine, text

db_connection_string = "mysql+pymysql://6iwpez5p05n92sz53j5s:pscale_pw_zenagNf28YHNjvzOrZ8sSfByHwGo0cHN7imLuxLj419@aws.connect.psdb.cloud/kalaonlinestore?charset=utf8mb4"

engine = create_engine(db_connection_string, connect_args={
  "ssl": {
    "ssl_ca": "/etc/ssl/cert.pem"
  }
})

with engine.connect() as conn:
  result = conn.execute(text("select * from watch"))
  print(result.all())