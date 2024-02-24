from sqlalchemy import create_engine, text

db_connection_string = "mysql+pymysql://0lyxmh4bkvsa87glaeqp:pscale_pw_lCHSp51jXbMON4rvTxmwm7G9pNAu6fPhOw87sDveBXB@aws.connect.psdb.cloud/kalaonlinestore?charset=utf8mb4"

engine = create_engine(db_connection_string,
                       connect_args={"ssl": {
                           "ssl_ca": "/etc/ssl/cert.pem"
                       }})

with engine.connect() as conn:
  result = conn.execute(text("select * from watch"))

  result_dicts = []
  for row in result.all():
    result_dicts.append(row._asdict())
  print(result_dicts)


def load_products_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from watch"))
    products = []
    for row in result.all():
      products.append(row._asdict())
    return products
