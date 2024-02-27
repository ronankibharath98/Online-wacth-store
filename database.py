from sqlalchemy import create_engine, text
import os

db_connection_string = "mysql+pymysql://27q7ym9q8bnvwai9i946:pscale_pw_XCvhXIRwPqDXoHf23dO2K8eI32sZ2qzKuVJs2rZDjfh@aws.connect.psdb.cloud/kalaonlinestore?charset=utf8mb4"

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
