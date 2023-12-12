from fastapi import FastAPI

from .routes import diagnostics
from .routes import activities

api_version:str = '1.0'
api_root:str = f'/pams/api/{api_version}'
app_description = '''
Process Activity & Monitor Service (PAMS) helps log Activity messages from consuming applications to capture process execution data.

## Activity Items
Consuming applications can read, write and modify Activity entries.

**Supported Operations:**

* **Create Activity Entry**
* **Update Activity Entry** (__not_implemented__)
* **Get Activity Entry** (__not_implemented__)
* **Search Activity Entry**  (__not_implemented__)
* **Delete Activity Entry** (__not_implemented__)
'''

app = FastAPI(title='Process Activity Monitor (PAM)',
              description=app_description,
              summary='Process state logging API',
              version=api_version,
              contact={
                'name': 'Debojit Sinha',
                'email': 'tahecef461@gyxmz.com'
              },
              license_info={
                'name': 'Apache 2.0',
                'identifier': 'Apache-2.0',
              })

app.include_router(diagnostics.router, prefix=api_root)
app.include_router(activities.router, prefix=api_root)